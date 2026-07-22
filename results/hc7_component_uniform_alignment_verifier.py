#!/usr/bin/env python3
"""Classify the exceptional component-alignment pole quotients.

The only non-standard executable is Brendan McKay's ``geng`` from nauty.
The Python search uses only the standard library.

For each finite layer needed by the accompanying proof, the verifier takes
an unlabelled nine-vertex graph H, marks a two-vertex set T with
S=V(H)-T, requires d_H(s)>=5 for every s in S, and adds c adjacent exactly
to S.  It then searches exhaustively for a K_6-minor model in H+c whose six
branch sets all meet H.  Vertices of H and c may be unused.  Exactly two
marked quotients survive; their analytic completion is given in the
accompanying theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import shutil
import subprocess
from collections.abc import Iterator, Sequence
from dataclasses import dataclass


H_ORDER = 9
CLIQUE_ORDER = 6


@dataclass(frozen=True)
class Layer:
    edges: int
    expected_graphs: int
    expected_marked: int
    expected_residues: int


LAYERS = (
    Layer(18, 34_040, 2, 0),
    Layer(19, 32_403, 26, 0),
    Layer(20, 27_987, 236, 0),
    Layer(21, 21_933, 1_270, 1),
    Layer(22, 15_615, 4_379, 1),
)

EXPECTED_RESIDUES = {
    (21, "HQjVRjf", (3, 4)),
    (22, "HQjVRjv", (3, 4)),
}


def parse_graph6(encoded: str) -> tuple[int, ...]:
    """Decode the short graph6 form used here."""

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
    command = [executable, "-q", str(H_ORDER), f"{edges}:{edges}"]
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
        graphs.append((encoded, adjacency))
    return tuple(graphs)


def set_partitions(vertices: tuple[int, ...]) -> Iterator[tuple[int, ...]]:
    blocks: list[list[int]] = []

    def recurse(index: int) -> Iterator[tuple[int, ...]]:
        if index == len(vertices):
            if len(blocks) == CLIQUE_ORDER:
                yield tuple(sum(1 << member for member in block) for block in blocks)
            return
        vertex = vertices[index]
        for block in blocks:
            block.append(vertex)
            yield from recurse(index + 1)
            block.pop()
        if len(blocks) < CLIQUE_ORDER:
            blocks.append([vertex])
            yield from recurse(index + 1)
            blocks.pop()

    yield from recurse(0)


def rooted_partial_partitions() -> tuple[tuple[int, ...], ...]:
    """All six-block partitions of an arbitrary H-subset, spanning first."""

    answer: list[tuple[int, ...]] = []
    for used_count in range(H_ORDER, CLIQUE_ORDER - 1, -1):
        for used in itertools.combinations(range(H_ORDER), used_count):
            answer.extend(set_partitions(used))
    if len(answer) != 5_880 or len(set(answer)) != 5_880:
        raise RuntimeError("partial partition generation failed")
    return tuple(answer)


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
    if len(model) != CLIQUE_ORDER:
        return False
    h_mask = (1 << H_ORDER) - 1
    used = 0
    for bag in model:
        if not bag or not bag & h_mask or used & bag or not connected(bag, adjacency):
            return False
        used |= bag
    return all(
        adjacent(model[left], model[right], adjacency)
        for left in range(CLIQUE_ORDER)
        for right in range(left + 1, CLIQUE_ORDER)
    )


def augmented_graph(h_adjacency: Sequence[int], boundary_mask: int) -> tuple[int, ...]:
    adjacency = list(h_adjacency) + [boundary_mask]
    for vertex in range(H_ORDER):
        if boundary_mask & (1 << vertex):
            adjacency[vertex] |= 1 << H_ORDER
    return tuple(adjacency)


def find_model(
    adjacency: Sequence[int],
    partitions: Sequence[tuple[int, ...]],
) -> tuple[int, ...] | None:
    c_bit = 1 << H_ORDER
    for partition in partitions:
        for attachment in range(-1, CLIQUE_ORDER):
            model = list(partition)
            if attachment >= 0:
                model[attachment] |= c_bit
            candidate = tuple(model)
            if valid_model(candidate, adjacency):
                return candidate
    return None


def format_bag(mask: int) -> str:
    names = ["c" if vertex == H_ORDER else str(vertex) for vertex in vertices(mask)]
    return "{" + ",".join(names) + "}"


def serialize_witness(
    layer: Layer,
    encoded: str,
    outside: tuple[int, ...],
    model: tuple[int, ...],
) -> str:
    omitted = ",".join(str(vertex) for vertex in outside)
    bags = ",".join(f"{mask:03x}" for mask in model)
    return f"{layer.edges}:{encoded}:{omitted}:{bags}\n"


def locate_geng(requested: str | None) -> str:
    executable = shutil.which(requested or "geng")
    if executable is None:
        raise SystemExit(
            "nauty's `geng` executable was not found; install nauty and put geng on PATH, "
            "or pass --geng /path/to/geng"
        )
    return executable


def run(executable: str, emit_all: bool) -> int:
    partitions = rooted_partial_partitions()
    catalogue_hash = hashlib.sha256()
    witness_hash = hashlib.sha256()
    residue_hash = hashlib.sha256()
    actual_residues: set[tuple[int, str, tuple[int, ...]]] = set()
    total_marked = total_residues = 0

    print("component_uniform_alignment_verifier version=1")
    print(f"partial_partitions={len(partitions)}")

    for layer in LAYERS:
        graphs = geng_graphs(executable, layer.edges)
        if len(graphs) != layer.expected_graphs:
            raise RuntimeError(
                f"expected {layer.expected_graphs} graphs with {layer.edges} edges, "
                f"received {len(graphs)}"
            )
        for encoded, _ in graphs:
            catalogue_hash.update(f"{layer.edges}:{encoded}\n".encode("ascii"))

        marked = residues = 0
        sample: tuple[str, tuple[int, ...], tuple[int, ...]] | None = None
        for encoded, h_adjacency in graphs:
            for outside in itertools.combinations(range(H_ORDER), 2):
                outside_mask = sum(1 << vertex for vertex in outside)
                boundary_mask = ((1 << H_ORDER) - 1) ^ outside_mask
                if any(
                    h_adjacency[vertex].bit_count() < 5
                    for vertex in vertices(boundary_mask)
                ):
                    continue
                marked += 1
                adjacency = augmented_graph(h_adjacency, boundary_mask)
                model = find_model(adjacency, partitions)
                if model is None:
                    residues += 1
                    residue = (layer.edges, encoded, outside)
                    actual_residues.add(residue)
                    serialized = f"{residue!r}\n"
                    residue_hash.update(serialized.encode("ascii"))
                    if emit_all:
                        print("residue " + serialized.rstrip())
                    continue
                if not valid_model(model, adjacency):
                    raise RuntimeError("model finder returned an invalid certificate")
                serialized = serialize_witness(layer, encoded, outside, model)
                witness_hash.update(serialized.encode("ascii"))
                if emit_all:
                    print("witness " + serialized.rstrip())
                if sample is None:
                    sample = (encoded, outside, model)

        if marked != layer.expected_marked or residues != layer.expected_residues:
            raise RuntimeError(
                f"layer {layer} expected marked/residues "
                f"{layer.expected_marked}/{layer.expected_residues}, received {marked}/{residues}"
            )
        if sample is None:
            raise RuntimeError(f"no positive certificate in layer {layer}")
        encoded, outside, model = sample
        formatted = " ".join(format_bag(bag) for bag in model)
        print(
            f"layer e={layer.edges} graphs={len(graphs)} "
            f"marked={marked} residues={residues}"
        )
        print(f"certificate H={encoded} T={outside} bags={formatted}")
        total_marked += marked
        total_residues += residues

    print(f"total_marked={total_marked} residues={total_residues}")
    print(f"catalogue_sha256={catalogue_hash.hexdigest()}")
    print(f"witness_sha256={witness_hash.hexdigest()}")
    print(f"residue_sha256={residue_hash.hexdigest()}")
    if actual_residues != EXPECTED_RESIDUES:
        print(f"unexpected_residues={sorted(actual_residues ^ EXPECTED_RESIDUES)!r}")
        print("FAIL component-uniform alignment classification")
        return 1
    print("PASS component-uniform alignment classification")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--geng", help="path or command name for nauty's geng")
    parser.add_argument(
        "--emit-all",
        action="store_true",
        help="print every deterministic model and both residual marked quotients",
    )
    arguments = parser.parse_args()
    return run(locate_geng(arguments.geng), arguments.emit_all)


if __name__ == "__main__":
    raise SystemExit(main())
