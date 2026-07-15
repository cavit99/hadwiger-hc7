#!/usr/bin/env python3
"""Exhaustive certificate for the nine-vertex support-six theorem.

The script expects Brendan McKay's ``geng`` on PATH.  It generates every
unlabelled graph on nine vertices with at least nineteen edges, tests the
exact six-vertex K5-support condition, and then tests for a K7 minor by
enumerating all branch-set partitions.  The only K7-minor-free graph whose
exact six-supports have transversal number greater than two is complement
C9, graph6 string ``HUzvvx}``.

Run:

    python3 active/hc7_support_six_nine_vertex_classifier.py

The lower edge bound nineteen is proved in the accompanying result note.
No graph library or SAT solver is used here.
"""

from __future__ import annotations

import itertools
import shutil
import subprocess
import sys
from collections.abc import Iterable, Iterator, Sequence


N = 9
VERTICES = tuple(range(N))
FULL_MASK = (1 << N) - 1
PAIRS = tuple(itertools.combinations(VERTICES, 2))
SIX_SETS = tuple(sum(1 << v for v in six) for six in itertools.combinations(VERTICES, 6))


def parse_graph6(line: bytes) -> tuple[int, ...]:
    """Parse the short graph6 format used for nine-vertex geng output."""

    data = line.strip()
    if not data or data[0] - 63 != N:
        raise ValueError(f"expected a short graph6 encoding on {N} vertices")
    bits: list[int] = []
    for byte in data[1:]:
        value = byte - 63
        if not 0 <= value < 64:
            raise ValueError("invalid graph6 byte")
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))

    adjacency = [0] * N
    cursor = 0
    for high in range(1, N):
        for low in range(high):
            if bits[cursor]:
                adjacency[low] |= 1 << high
                adjacency[high] |= 1 << low
            cursor += 1
    return tuple(adjacency)


def set_partitions(items: Sequence[int], blocks: int) -> Iterator[tuple[int, ...]]:
    """Yield each partition of ``items`` into ``blocks`` nonempty bitmasks."""

    bags: list[int] = []

    def visit(index: int) -> Iterator[tuple[int, ...]]:
        if index == len(items):
            if len(bags) == blocks:
                yield tuple(bags)
            return
        vertex_bit = 1 << items[index]
        for position in range(len(bags)):
            bags[position] |= vertex_bit
            yield from visit(index + 1)
            bags[position] ^= vertex_bit
        if len(bags) < blocks:
            bags.append(vertex_bit)
            yield from visit(index + 1)
            bags.pop()

    yield from visit(0)


def model_partitions(order: int) -> tuple[tuple[int, ...], ...]:
    partitions: list[tuple[int, ...]] = []
    for used_order in range(order, N + 1):
        for used in itertools.combinations(VERTICES, used_order):
            partitions.extend(set_partitions(used, order))
    return tuple(partitions)


K7_PARTITIONS = model_partitions(7)
K6_PARTITIONS = model_partitions(6)


def is_connected(mask: int, adjacency: Sequence[int]) -> bool:
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


def bags_touch(first: int, second: int, adjacency: Sequence[int]) -> bool:
    scan = first
    neighbours = 0
    while scan:
        bit = scan & -scan
        scan ^= bit
        neighbours |= adjacency[bit.bit_length() - 1]
    return bool(neighbours & second)


def is_model(partition: Sequence[int], adjacency: Sequence[int]) -> bool:
    if not all(is_connected(bag, adjacency) for bag in partition):
        return False
    return all(
        bags_touch(first, second, adjacency)
        for first, second in itertools.combinations(partition, 2)
    )


def has_k7_minor(adjacency: Sequence[int]) -> bool:
    return any(is_model(partition, adjacency) for partition in K7_PARTITIONS)


def is_exact_six_support(mask: int, adjacency: Sequence[int]) -> bool:
    """Test for a spanning K5 model with bag sizes (2,1,1,1,1)."""

    vertices = tuple(v for v in VERTICES if mask & (1 << v))
    for left, right in itertools.combinations(vertices, 2):
        if not adjacency[left] & (1 << right):
            continue
        pair = (1 << left) | (1 << right)
        singleton_mask = mask ^ pair
        singletons = tuple(v for v in vertices if singleton_mask & (1 << v))
        if any(not adjacency[u] & (1 << v) for u, v in itertools.combinations(singletons, 2)):
            continue
        if all((adjacency[left] | adjacency[right]) & (1 << vertex) for vertex in singletons):
            return True
    return False


def support_family(adjacency: Sequence[int]) -> tuple[int, ...]:
    return tuple(mask for mask in SIX_SETS if is_exact_six_support(mask, adjacency))


def has_transversal_number_above_two(supports: Sequence[int]) -> bool:
    if not supports:
        return False
    return all(
        any(not support & ((1 << left) | (1 << right)) for support in supports)
        for left, right in PAIRS
    )


def has_meeting_k6(boundary: int, adjacency: Sequence[int]) -> bool:
    return any(
        all(bag & boundary for bag in partition) and is_model(partition, adjacency)
        for partition in K6_PARTITIONS
    )


def edge_count(adjacency: Sequence[int]) -> int:
    return sum(mask.bit_count() for mask in adjacency) // 2


def verify_exception() -> None:
    encoded = b"HUzvvx}"
    adjacency = parse_graph6(encoded)
    complement_cycle = tuple(
        FULL_MASK ^ (1 << vertex) ^ (1 << ((vertex - 1) % N)) ^ (1 << ((vertex + 1) % N))
        for vertex in VERTICES
    )
    assert adjacency == complement_cycle
    supports = support_family(adjacency)
    assert edge_count(adjacency) == 27
    assert len(supports) == 27
    assert has_transversal_number_above_two(supports)
    assert not has_k7_minor(adjacency)
    displayed = {
        (0, 1): ((0, 1, 5), (2,), (3, 7), (4,), (6,), (8,)),
        (0, 2): ((0, 2, 5), (1,), (3, 7), (4,), (6,), (8,)),
        (0, 3): ((0, 1, 5), (2,), (3, 7), (4,), (6,), (8,)),
        (0, 4): ((0, 2, 5), (1,), (3,), (4, 7), (6,), (8,)),
    }
    for missing, bags in displayed.items():
        partition = tuple(sum(1 << vertex for vertex in bag) for bag in bags)
        boundary = FULL_MASK ^ (1 << missing[0]) ^ (1 << missing[1])
        assert is_model(partition, adjacency), missing
        assert all(bag & boundary for bag in partition), missing
    for missing in PAIRS:
        boundary = FULL_MASK ^ (1 << missing[0]) ^ (1 << missing[1])
        assert has_meeting_k6(boundary, adjacency), missing


def geng_graphs() -> Iterable[bytes]:
    executable = shutil.which("geng")
    if executable is None:
        raise SystemExit("geng was not found on PATH (install nauty/Traces)")
    process = subprocess.Popen(
        [executable, "-q", str(N), "19:36"],
        stdout=subprocess.PIPE,
    )
    assert process.stdout is not None
    yield from process.stdout
    return_code = process.wait()
    if return_code:
        raise SystemExit(f"geng exited with status {return_code}")


def classify() -> None:
    verify_exception()
    total = 0
    high_transversal = 0
    survivors: list[tuple[str, int, int]] = []
    for line in geng_graphs():
        total += 1
        adjacency = parse_graph6(line)
        supports = support_family(adjacency)
        if not has_transversal_number_above_two(supports):
            continue
        high_transversal += 1
        if not has_k7_minor(adjacency):
            survivors.append((line.strip().decode("ascii"), edge_count(adjacency), len(supports)))

    expected = [("HUzvvx}", 27, 27)]
    assert total == 120_314, total
    assert high_transversal == 614, high_transversal
    assert survivors == expected, survivors
    print(f"unlabelled graphs tested: {total}")
    print(f"graphs with support transversal > 2: {high_transversal}")
    print(f"K7-minor-free survivors: {survivors}")
    print("all 36 seven-sets meet an explicit K6 model in the survivor")


if __name__ == "__main__":
    try:
        classify()
    except AssertionError as error:
        print(f"verification failed: {error}", file=sys.stderr)
        raise
