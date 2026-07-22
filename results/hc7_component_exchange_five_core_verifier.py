#!/usr/bin/env python3
"""Verify the two-support exceptions in the neighbourhood 4-core proof.

The analytic edge count leaves only two finite layers when d(u)=9:

* a seven-vertex graph F with 18 edges and minimum degree five, with two
  support vertices each missing two vertices of F; and
* an eight-vertex graph F with 20 edges and minimum degree five, with the
  same marked supports.

The verifier enumerates every unlabelled F and every unordered pair of
two-vertex miss sets.  It produces and independently checks a K7-minor
model in the graph obtained by adding a universal vertex u and two
nonadjacent support vertices with the marked contacts.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import itertools
import shutil
import subprocess
from collections.abc import Sequence
from dataclasses import dataclass


TARGET = 7
EXPECTED_CATALOGUE_SHA256 = (
    "0ef56bb5ba5a44e5c699f2d0a81c1f74cc9eb35e5a52aed4dc6846817948900d"
)
EXPECTED_WITNESS_SHA256 = (
    "b5af511f5eccf17baf6bd2dc8affa792d1391eb3128bc57111d4703227277caa"
)


@dataclass(frozen=True)
class Layer:
    order: int
    edges: int
    expected_graphs: int
    expected_marks: int


LAYERS = (
    Layer(7, 18, 1, 231),
    Layer(8, 20, 3, 1_218),
)


def parse_graph6(encoded: str, order: int) -> tuple[int, ...]:
    data = [ord(char) - 63 for char in encoded.strip()]
    if not data or data[0] != order:
        raise ValueError(f"expected graph6 order {order}: {encoded!r}")
    if any(value < 0 or value > 63 for value in data):
        raise ValueError(f"invalid graph6 data: {encoded!r}")
    bits: list[int] = []
    for value in data[1:]:
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    adjacency = [0] * order
    cursor = 0
    for upper in range(1, order):
        for lower in range(upper):
            if bits[cursor]:
                adjacency[lower] |= 1 << upper
                adjacency[upper] |= 1 << lower
            cursor += 1
    return tuple(adjacency)


def geng_graphs(executable: str, layer: Layer) -> tuple[tuple[str, tuple[int, ...]], ...]:
    completed = subprocess.run(
        [executable, "-q", str(layer.order), f"{layer.edges}:{layer.edges}"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if completed.stderr:
        raise RuntimeError(f"geng wrote to stderr: {completed.stderr.strip()}")
    answer = []
    for raw in completed.stdout.splitlines():
        encoded = raw.strip()
        if not encoded:
            continue
        adjacency = parse_graph6(encoded, layer.order)
        if sum(mask.bit_count() for mask in adjacency) // 2 != layer.edges:
            raise RuntimeError(f"wrong edge count: {encoded}")
        if min(mask.bit_count() for mask in adjacency) >= 5:
            answer.append((encoded, adjacency))
    return tuple(answer)


def augment(
    base: Sequence[int], first_miss: tuple[int, int], second_miss: tuple[int, int]
) -> tuple[int, ...]:
    base_order = len(base)
    universal, first_support, second_support = (
        base_order,
        base_order + 1,
        base_order + 2,
    )
    adjacency = list(base) + [0, 0, 0]
    full = (1 << base_order) - 1
    adjacency[universal] = full
    first_contacts = full ^ sum(1 << vertex for vertex in first_miss)
    second_contacts = full ^ sum(1 << vertex for vertex in second_miss)
    for vertex in range(base_order):
        adjacency[vertex] |= 1 << universal
        if first_contacts & (1 << vertex):
            adjacency[vertex] |= 1 << first_support
            adjacency[first_support] |= 1 << vertex
        if second_contacts & (1 << vertex):
            adjacency[vertex] |= 1 << second_support
            adjacency[second_support] |= 1 << vertex
    return tuple(adjacency)


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
    while left:
        bit = left & -left
        left ^= bit
        if adjacency[bit.bit_length() - 1] & right:
            return True
    return False


def find_k7_model(adjacency: tuple[int, ...]) -> tuple[int, ...] | None:
    order = len(adjacency)
    vertices = tuple(range(order))
    full = (1 << order) - 1

    @functools.lru_cache(maxsize=None)
    def is_connected(mask: int) -> bool:
        return connected(mask, adjacency)

    @functools.lru_cache(maxsize=None)
    def are_adjacent(left: int, right: int) -> bool:
        return adjacent(left, right, adjacency)

    minimum_singletons = max(0, 2 * TARGET - order)
    for singleton_count in range(TARGET, minimum_singletons - 1, -1):
        nonsingleton_count = TARGET - singleton_count
        for singletons in itertools.combinations(vertices, singleton_count):
            if any(
                not adjacency[left] & (1 << right)
                for left, right in itertools.combinations(singletons, 2)
            ):
                continue
            singleton_masks = tuple(1 << vertex for vertex in singletons)
            singleton_union = sum(singleton_masks)
            remainder = full ^ singleton_union
            if nonsingleton_count == 0:
                return singleton_masks
            maximum_size = remainder.bit_count() - 2 * (nonsingleton_count - 1)
            candidates = []
            subset = remainder
            while subset:
                if (
                    2 <= subset.bit_count() <= maximum_size
                    and is_connected(subset)
                    and all(are_adjacent(subset, old) for old in singleton_masks)
                ):
                    candidates.append(subset)
                subset = (subset - 1) & remainder
            candidates.sort(key=lambda mask: (mask.bit_count(), mask))

            def search(start: int, chosen: tuple[int, ...], used: int):
                if len(chosen) == nonsingleton_count:
                    return singleton_masks + chosen
                missing = nonsingleton_count - len(chosen)
                if (remainder & ~used).bit_count() < 2 * missing:
                    return None
                for position in range(start, len(candidates)):
                    candidate = candidates[position]
                    if candidate & used:
                        continue
                    if not all(are_adjacent(candidate, old) for old in chosen):
                        continue
                    result = search(
                        position + 1,
                        chosen + (candidate,),
                        used | candidate,
                    )
                    if result is not None:
                        return result
                return None

            result = search(0, (), 0)
            if result is not None:
                return result
    return None


def verify_model(adjacency: tuple[int, ...], model: tuple[int, ...]) -> None:
    if len(model) != TARGET or any(not bag for bag in model):
        raise RuntimeError("wrong model order")
    if any(left & right for left, right in itertools.combinations(model, 2)):
        raise RuntimeError("overlapping branch sets")
    if any(not connected(bag, adjacency) for bag in model):
        raise RuntimeError("disconnected branch set")
    if any(
        not adjacent(left, right, adjacency)
        for left, right in itertools.combinations(model, 2)
    ):
        raise RuntimeError("missing branch-set adjacency")


def serialize_model(model: Sequence[int]) -> str:
    return ",".join(f"{bag:03x}" for bag in model)


def locate_geng(requested: str | None) -> str:
    executable = shutil.which(requested or "geng")
    if executable is None:
        raise SystemExit("nauty geng not found; pass --geng /path/to/geng")
    return executable


def self_test() -> None:
    """Exercise graph6 decoding, augmentation, and both model outcomes."""
    triangle = parse_graph6("Bw", 3)
    if any(mask.bit_count() != 2 for mask in triangle):
        raise RuntimeError("graph6 parser self-test failed")

    clique7 = tuple(((1 << 7) - 1) ^ (1 << vertex) for vertex in range(7))
    positive = find_k7_model(clique7)
    if positive is None:
        raise RuntimeError("positive K7-model self-test failed")
    verify_model(clique7, positive)

    clique6 = tuple(((1 << 6) - 1) ^ (1 << vertex) for vertex in range(6))
    if find_k7_model(clique6) is not None:
        raise RuntimeError("negative K7-model self-test failed")

    augmented = augment(clique7, (0, 1), (1, 2))
    if augmented[8] & ((1 << 0) | (1 << 1)):
        raise RuntimeError("first support miss-set self-test failed")
    if augmented[9] & ((1 << 1) | (1 << 2)):
        raise RuntimeError("second support miss-set self-test failed")
    if augmented[7] != (1 << 7) - 1:
        raise RuntimeError("universal-vertex self-test failed")


def run(executable: str, emit_all: bool) -> int:
    self_test()
    catalogue_hash = hashlib.sha256()
    witness_hash = hashlib.sha256()
    total_marks = 0
    print("component_exchange_five_core_verifier version=1")
    for layer in LAYERS:
        graphs = geng_graphs(executable, layer)
        if len(graphs) != layer.expected_graphs:
            raise RuntimeError(
                f"layer {layer.order} expected {layer.expected_graphs} graphs, "
                f"received {len(graphs)}"
            )
        layer_marks = 0
        first_sample = None
        miss_sets = tuple(itertools.combinations(range(layer.order), 2))
        for encoded, base in graphs:
            catalogue_hash.update(f"{layer.order}:{encoded}\n".encode("ascii"))
            for first_index, first_miss in enumerate(miss_sets):
                for second_miss in miss_sets[first_index:]:
                    layer_marks += 1
                    adjacency = augment(base, first_miss, second_miss)
                    model = find_k7_model(adjacency)
                    if model is None:
                        print(
                            "FAIL no model "
                            f"order={layer.order} F={encoded} "
                            f"misses={first_miss},{second_miss}"
                        )
                        return 1
                    verify_model(adjacency, model)
                    record = (
                        f"{layer.order}:{encoded}:{first_miss}:{second_miss}:"
                        f"{serialize_model(model)}\n"
                    )
                    witness_hash.update(record.encode("ascii"))
                    if emit_all:
                        print("witness " + record.rstrip())
                    if first_sample is None:
                        first_sample = record.rstrip()
        if layer_marks != layer.expected_marks:
            raise RuntimeError(
                f"layer {layer.order} expected {layer.expected_marks} marks, "
                f"received {layer_marks}"
            )
        total_marks += layer_marks
        print(
            f"layer h={layer.order} e={layer.edges} "
            f"graphs={len(graphs)} marks={layer_marks} residues=0"
        )
        print(f"certificate {first_sample}")
    print(f"total_marks={total_marks} residues=0")
    catalogue_digest = catalogue_hash.hexdigest()
    witness_digest = witness_hash.hexdigest()
    print(f"catalogue_sha256={catalogue_digest}")
    print(f"witness_sha256={witness_digest}")
    if catalogue_digest != EXPECTED_CATALOGUE_SHA256:
        raise RuntimeError("catalogue hash differs from the audited run")
    if witness_digest != EXPECTED_WITNESS_SHA256:
        raise RuntimeError("witness hash differs from the audited run")
    print("PASS component-exchange five-core classification")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--geng", help="path or command name for nauty geng")
    parser.add_argument("--emit-all", action="store_true")
    arguments = parser.parse_args()
    return run(locate_geng(arguments.geng), arguments.emit_all)


if __name__ == "__main__":
    raise SystemExit(main())
