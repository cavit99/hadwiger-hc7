#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Verify the eight cross-arc-connector K7 certificates."""

from __future__ import annotations

import itertools


S = tuple(range(7))
C = tuple(range(6))
Z = 6
A, B, P, Q, H = 7, 8, 9, 10, 11

MODELS = {
    ("O", (1, 5)): ((0,), (1,), (6,), (7,), (8,), (2, 9), (5, 10, 11)),
    ("O", (2, 4)): ((0,), (1,), (6,), (7,), (8,), (3, 9), (2, 4, 5, 11)),
    ("O", (1, 4)): ((0,), (1,), (6,), (7,), (8,), (2, 9), (4, 10, 11)),
    ("O", (2, 5)): ((0,), (1,), (6,), (7,), (8,), (3, 9), (2, 5, 11)),
    ("A", (1, 5)): ((0,), (1,), (6,), (7,), (2, 8), (3, 9), (4, 5, 11)),
    ("A", (2, 4)): ((0,), (1,), (6,), (7,), (5, 8), (3, 9), (2, 4, 10, 11)),
    ("A", (1, 4)): ((0,), (1,), (6,), (7,), (2, 8), (3, 9), (4, 5, 11)),
    ("A", (2, 5)): ((0,), (1,), (6,), (7,), (3, 8), (4, 9, 10), (2, 5, 11)),
    ("O", (0, 2)): ((0, 5), (6,), (7,), (8,), (1, 9), (4, 10), (2, 3, 11)),
    ("O", (0, 4)): ((5,), (6,), (7,), (8,), (0, 1, 2, 9), (3, 10), (4, 11)),
    ("O", (1, 3)): ((0, 1, 5), (6,), (7,), (8,), (2, 9), (4, 10), (3, 11)),
    ("O", (3, 5)): ((5,), (6,), (7,), (8,), (0, 1, 2, 9), (4, 10), (3, 11)),
    ("A", (0, 2)): ((0, 5), (6,), (1, 7), (8,), (9,), (4, 10), (2, 3, 11)),
    ("A", (0, 4)): ((4,), (5,), (6,), (3, 7), (8, 9), (10,), (0, 1, 2, 11)),
    ("A", (1, 3)): ((0, 1, 5), (6,), (2, 7), (8,), (9,), (4, 10), (3, 11)),
    ("A", (3, 5)): ((4,), (5,), (6,), (0, 1, 2, 7), (8, 9), (10,), (3, 11)),
}


def graph(mode: str, pair: tuple[int, int]) -> set[tuple[int, int]]:
    edges = {
        tuple(sorted((i, (i + 1) % 6))) for i in C
    } | {(i, Z) for i in C}
    edges.add((P, Q))
    if mode == "O":
        edges.add((A, B))
    else:
        edges.add((B, P))
    for s in S:
        edges.add(tuple(sorted((s, A))))
        edges.add(tuple(sorted((s, B))))
    for s in (0, 1, 2, 3, 6):
        edges.add(tuple(sorted((s, P))))
    for s in (0, 3, 4, 5, 6):
        edges.add(tuple(sorted((s, Q))))
    for s in pair:
        edges.add(tuple(sorted((s, H))))
    return edges


def connected(
    bag: tuple[int, ...],
    edges: set[tuple[int, int]],
) -> bool:
    reached = {bag[0]}
    while True:
        expanded = reached | {
            y
            for edge in edges
            for x, y in (edge, edge[::-1])
            if x in reached and y in bag
        }
        if expanded == reached:
            return reached == set(bag)
        reached = expanded


def main() -> None:
    assert len(MODELS) == 16
    for key, bags in MODELS.items():
        edges = graph(*key)
        assert len(bags) == 7
        assert sum(map(len, bags)) == len(set().union(*map(set, bags)))
        assert all(connected(bag, edges) for bag in bags)
        for first, second in itertools.combinations(bags, 2):
            assert any(
                tuple(sorted((x, y))) in edges
                for x in first for y in second
            )
    print("verified 16 arc-connector K7 certificates")


if __name__ == "__main__":
    main()
