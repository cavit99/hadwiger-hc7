#!/usr/bin/env python3
"""Verify the exact-seven paired-block parity barrier."""

from __future__ import annotations

from itertools import combinations


S = ("j0", "b", "r", "j1", "z1", "z2", "q")
FIRST = {"j0", "b", "r"}
SECOND = {"j1", "z1", "z2"}
EDGES = {
    frozenset(edge)
    for triangle in (FIRST, SECOND)
    for edge in combinations(triangle, 2)
}


def set_partitions(items: tuple[str, ...]):
    """Yield every set partition once, in restricted-growth order."""
    blocks: list[list[str]] = []

    def visit(index: int):
        if index == len(items):
            yield frozenset(frozenset(block) for block in blocks)
            return
        item = items[index]
        for block in blocks:
            block.append(item)
            yield from visit(index + 1)
            block.pop()
        blocks.append([item])
        yield from visit(index + 1)
        blocks.pop()

    yield from visit(0)


def independent(vertices: frozenset[str]) -> bool:
    return not any(edge <= vertices for edge in EDGES)


OMEGA = {
    partition
    for partition in set_partitions(S)
    if len(partition) <= 6 and all(independent(block) for block in partition)
}
EVEN = {partition for partition in OMEGA if len(partition) % 2 == 0}
ODD = OMEGA - EVEN


def require(condition: bool, message: str) -> None:
    """Raise even when Python is run with optimization enabled."""
    if not condition:
        raise AssertionError(message)


def main() -> None:
    require(len(OMEGA) == 174, "unexpected number of proper states")
    require(len(EVEN) == 93 and len(ODD) == 81, "wrong parity counts")
    require(EVEN.isdisjoint(ODD) and EVEN | ODD == OMEGA, "parity split failed")

    target = frozenset(
        {
            frozenset({"j0", "j1", "q"}),
            frozenset({"b", "z1"}),
            frozenset({"r"}),
            frozenset({"z2"}),
        }
    )
    require(target in EVEN, "target partition is not an even proper state")

    independent_sets = {
        frozenset(x for index, x in enumerate(S) if mask & (1 << index))
        for mask in range(1, 1 << len(S))
    }
    independent_sets = {item for item in independent_sets if independent(item)}
    require(len(independent_sets) == 31, "unexpected independent-set count")

    for item in independent_sets:
        require(any(item in partition for partition in EVEN), "even language misses an exact block")
        require(any(item in partition for partition in ODD), "odd language misses an exact block")

    queries = [
        pair
        for pair in combinations(independent_sets, 2)
        if pair[0].isdisjoint(pair[1])
    ]
    require(len(queries) == 222, "unexpected disjoint-pair count")
    for first, second in queries:
        require(
            any(first in part and second in part for part in EVEN),
            "even language misses a two-block query",
        )
        require(
            any(first in part and second in part for part in ODD),
            "odd language misses a two-block query",
        )

    packet_vertices = {"pL", "pR"}
    quotient_vertices = set(S) | packet_vertices
    quotient_edges = set(EDGES)
    quotient_edges.update(
        frozenset({packet, boundary})
        for packet in packet_vertices
        for boundary in S
    )

    clique_number = 0
    for size in range(1, len(quotient_vertices) + 1):
        for candidate in combinations(quotient_vertices, size):
            if all(
                frozenset(edge) in quotient_edges
                for edge in combinations(candidate, 2)
            ):
                clique_number = max(clique_number, size)
    require(
        len(quotient_vertices) == 9 and clique_number == 4,
        "wrong quotient order or clique number",
    )

    print("GREEN: 174 proper states split into 93 even and 81 odd")
    print("GREEN: both parities answer all 31 exact-block queries")
    print("GREEN: both parities answer all 222 two-block queries")
    print("GREEN: the returned paired-block partition is even")
    print("GREEN: the two-packet quotient has order 9 and clique number 4")


if __name__ == "__main__":
    main()
