#!/usr/bin/env python3
"""Exhaust the exceptional degree-nine pole quotients.

The only non-standard dependency is Brendan McKay's ``geng`` executable
from nauty.  The search itself uses only the Python standard library.

For every complement F on nine vertices with maximum degree at most three
and 12 or 13 edges, put H = complement(F).  In each of the three exceptional
edge-count regimes, add a vertex c with the prescribed number of
non-neighbours in H.  The verifier finds a K_6-minor model in H+c whose six
branch sets all meet H.  It searches only the stronger certificate type
consisting of three H-edges, three singleton H-vertices, and c adjoined to
one of those six branch sets.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import shutil
import subprocess
from collections.abc import Iterable, Iterator, Sequence
from dataclasses import dataclass


H_ORDER = 9
C_VERTEX = 9
ALL_H = (1 << H_ORDER) - 1
ALL_VERTICES = (1 << (H_ORDER + 1)) - 1


@dataclass(frozen=True)
class Case:
    complement_edges: int
    c_nonneighbours: int
    expected_complements: int
    expected_instances: int


CASES = (
    Case(13, 2, 20, 720),
    Case(13, 1, 20, 180),
    Case(12, 2, 103, 3708),
)


def parse_graph6(encoded: str) -> tuple[int, ...]:
    """Decode the short graph6 format used here (orders at most 62)."""

    data = [ord(char) - 63 for char in encoded.strip()]
    if not data or data[0] != H_ORDER:
        raise ValueError(f"expected graph6 order {H_ORDER}: {encoded!r}")
    if any(value < 0 or value > 63 for value in data):
        raise ValueError(f"invalid graph6 data: {encoded!r}")

    bits: list[int] = []
    for value in data[1:]:
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))

    adjacency = [0] * H_ORDER
    cursor = 0
    for upper in range(1, H_ORDER):
        for lower in range(upper):
            if bits[cursor]:
                adjacency[lower] |= 1 << upper
                adjacency[upper] |= 1 << lower
            cursor += 1
    return tuple(adjacency)


def edge_count(adjacency: Sequence[int]) -> int:
    return sum(neighbours.bit_count() for neighbours in adjacency) // 2


def geng_graphs(executable: str, edges: int) -> tuple[tuple[str, tuple[int, ...]], ...]:
    """Return all unlabelled nine-vertex graphs in one nauty class."""

    command = [executable, "-q", str(H_ORDER), f"{edges}:{edges}", "-D3"]
    completed = subprocess.run(
        command,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if completed.stderr:
        raise RuntimeError(f"geng wrote to stderr: {completed.stderr.strip()}")

    graphs: list[tuple[str, tuple[int, ...]]] = []
    seen: set[str] = set()
    for raw in completed.stdout.splitlines():
        encoded = raw.strip()
        if not encoded:
            continue
        if encoded in seen:
            raise RuntimeError(f"duplicate graph6 representative: {encoded}")
        seen.add(encoded)
        adjacency = parse_graph6(encoded)
        if edge_count(adjacency) != edges:
            raise RuntimeError(f"wrong edge count from geng: {encoded}")
        if max(neighbours.bit_count() for neighbours in adjacency) > 3:
            raise RuntimeError(f"wrong maximum degree from geng: {encoded}")
        graphs.append((encoded, adjacency))
    return tuple(graphs)


def complement_on_h(adjacency: Sequence[int]) -> tuple[int, ...]:
    return tuple(ALL_H ^ (1 << vertex) ^ adjacency[vertex] for vertex in range(H_ORDER))


def perfect_matchings(vertices: tuple[int, ...]) -> Iterator[tuple[tuple[int, int], ...]]:
    if not vertices:
        yield ()
        return
    first = vertices[0]
    for index in range(1, len(vertices)):
        second = vertices[index]
        rest = vertices[1:index] + vertices[index + 1 :]
        for matching in perfect_matchings(rest):
            yield ((first, second),) + matching


def restricted_partitions() -> tuple[tuple[int, ...], ...]:
    """Partition H into three pairs and three singletons, without repeats."""

    answer: list[tuple[int, ...]] = []
    for paired in itertools.combinations(range(H_ORDER), 6):
        paired_set = set(paired)
        singletons = tuple(1 << vertex for vertex in range(H_ORDER) if vertex not in paired_set)
        for matching in perfect_matchings(paired):
            pairs = tuple((1 << left) | (1 << right) for left, right in matching)
            answer.append(tuple(sorted(pairs + singletons)))
    if len(answer) != 1260 or len(set(answer)) != 1260:
        raise RuntimeError("restricted partition generation failed")
    return tuple(sorted(answer))


PARTITIONS = restricted_partitions()


def vertices(mask: int) -> Iterator[int]:
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def connected(mask: int, adjacency: Sequence[int]) -> bool:
    reached = mask & -mask
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        vertex = bit.bit_length() - 1
        new = adjacency[vertex] & mask & ~reached
        reached |= new
        frontier |= new
    return reached == mask


def adjacent(left: int, right: int, adjacency: Sequence[int]) -> bool:
    return any(adjacency[vertex] & right for vertex in vertices(left))


def valid_model(model: Sequence[int], adjacency: Sequence[int]) -> bool:
    if len(model) != 6 or any(not bag & ALL_H for bag in model):
        return False
    if sum(bag.bit_count() for bag in model) != 10:
        return False
    union = 0
    for bag in model:
        if union & bag or not connected(bag, adjacency):
            return False
        union |= bag
    if union != ALL_VERTICES:
        return False
    return all(
        adjacent(model[i], model[j], adjacency)
        for i in range(6)
        for j in range(i + 1, 6)
    )


def augmented_graph(h_adjacency: Sequence[int], missing: tuple[int, ...]) -> tuple[int, ...]:
    missing_mask = sum(1 << vertex for vertex in missing)
    c_neighbours = ALL_H ^ missing_mask
    adjacency = list(h_adjacency) + [c_neighbours]
    for vertex in range(H_ORDER):
        if c_neighbours & (1 << vertex):
            adjacency[vertex] |= 1 << C_VERTEX
    return tuple(adjacency)


def find_model(adjacency: Sequence[int]) -> tuple[int, ...] | None:
    c_neighbours = adjacency[C_VERTEX]
    for partition in PARTITIONS:
        pair_edges_ok = True
        for block in partition:
            if block.bit_count() == 2:
                left, right = tuple(vertices(block))
                if not (adjacency[left] & (1 << right)):
                    pair_edges_ok = False
                    break
        if not pair_edges_ok:
            continue

        for attachment, block in enumerate(partition):
            if not (block & c_neighbours):
                continue
            model = list(partition)
            model[attachment] |= 1 << C_VERTEX
            candidate = tuple(model)
            if valid_model(candidate, adjacency):
                return candidate
    return None


def format_bag(mask: int) -> str:
    names = ["c" if vertex == C_VERTEX else str(vertex) for vertex in vertices(mask)]
    return "{" + ",".join(names) + "}"


def serialize_witness(
    case: Case,
    encoded: str,
    missing: tuple[int, ...],
    model: tuple[int, ...],
) -> str:
    bags = ",".join(f"{mask:03x}" for mask in model)
    omitted = ",".join(str(vertex) for vertex in missing)
    return f"{case.complement_edges}:{case.c_nonneighbours}:{encoded}:{omitted}:{bags}\n"


def locate_geng(requested: str | None) -> str:
    if requested:
        executable = shutil.which(requested)
    else:
        executable = shutil.which("geng")
    if executable is None:
        raise SystemExit(
            "nauty's `geng` executable was not found; install nauty and put geng on PATH, "
            "or pass --geng /path/to/geng"
        )
    return executable


def run(executable: str, emit_all: bool) -> int:
    catalogue: dict[int, tuple[tuple[str, tuple[int, ...]], ...]] = {}
    catalogue_hash = hashlib.sha256()
    witness_hash = hashlib.sha256()
    total_instances = 0
    total_bad = 0

    print("degree9_pole_verifier version=1")
    print(f"restricted_partitions={len(PARTITIONS)}")

    for case in CASES:
        if case.complement_edges not in catalogue:
            graphs = geng_graphs(executable, case.complement_edges)
            catalogue[case.complement_edges] = graphs
            for encoded, _ in graphs:
                catalogue_hash.update(f"{case.complement_edges}:{encoded}\n".encode("ascii"))
        graphs = catalogue[case.complement_edges]
        if len(graphs) != case.expected_complements:
            raise RuntimeError(
                f"expected {case.expected_complements} complements with {case.complement_edges} "
                f"edges, received {len(graphs)}"
            )

        instances = 0
        bad = 0
        sample: tuple[str, tuple[int, ...], tuple[int, ...]] | None = None
        for encoded, f_adjacency in graphs:
            h_adjacency = complement_on_h(f_adjacency)
            if min(neighbours.bit_count() for neighbours in h_adjacency) < 5:
                raise RuntimeError(f"complement minimum degree check failed: {encoded}")
            for missing in itertools.combinations(range(H_ORDER), case.c_nonneighbours):
                instances += 1
                adjacency = augmented_graph(h_adjacency, missing)
                model = find_model(adjacency)
                if model is None:
                    bad += 1
                    continue
                if sample is None:
                    sample = (encoded, missing, model)
                serialized = serialize_witness(case, encoded, missing, model)
                witness_hash.update(serialized.encode("ascii"))
                if emit_all:
                    print("witness " + serialized.rstrip())

        if instances != case.expected_instances:
            raise RuntimeError(f"expected {case.expected_instances} instances, received {instances}")
        if sample is None:
            raise RuntimeError("no sample certificate was generated")
        encoded, missing, model = sample
        formatted_model = " ".join(format_bag(bag) for bag in model)
        missing_text = ",".join(str(vertex) for vertex in missing)
        print(
            f"case F_edges={case.complement_edges} c_nonneighbours={case.c_nonneighbours} "
            f"complements={len(graphs)} instances={instances} bad={bad}"
        )
        print(f"certificate F={encoded} missing={missing_text} bags={formatted_model}")
        total_instances += instances
        total_bad += bad

    print(f"total_instances={total_instances} bad={total_bad}")
    print(f"catalogue_sha256={catalogue_hash.hexdigest()}")
    print(f"witness_sha256={witness_hash.hexdigest()}")
    if total_bad:
        print("FAIL degree-nine local completion")
        return 1
    print("PASS degree-nine local completion")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--geng", help="path or command name for nauty's geng")
    parser.add_argument(
        "--emit-all",
        action="store_true",
        help="print the deterministic certificate for every rooted instance",
    )
    arguments = parser.parse_args()
    return run(locate_geng(arguments.geng), arguments.emit_all)


if __name__ == "__main__":
    raise SystemExit(main())
