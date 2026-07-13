#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Audit duplicated-portal covering splits over the two C6+K1 conventions.

The quotient has a seven-vertex boundary, two full anticomplete helper
vertices, and two adjacent split helpers.  Their boundary rows cover the
boundary and share a prescribed duplicated label.  We enumerate all rows
and search exactly for a K7 minor.
"""

from __future__ import annotations

import itertools
from collections import Counter


S = tuple(range(7))
A, B, H1, H2 = 7, 8, 9, 10
V = tuple(range(11))
FULL = (1 << 7) - 1


def connected_masks(adjacency: list[int]) -> tuple[int, ...]:
    answer = []
    for mask in range(1, 1 << len(V)):
        reached = mask & -mask
        while True:
            expanded = reached
            bits = reached
            while bits:
                bit = bits & -bits
                expanded |= adjacency[bit.bit_length() - 1] & mask
                bits ^= bit
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            answer.append(mask)
    answer.sort(key=lambda item: (item.bit_count(), item))
    return tuple(answer)


def k7_model(edges: set[tuple[int, int]]) -> tuple[int, ...] | None:
    adjacency = [0] * len(V)
    for x, y in edges:
        adjacency[x] |= 1 << y
        adjacency[y] |= 1 << x
    connected = connected_masks(adjacency)
    neighbourhood = [0] * (1 << len(V))
    for mask in range(1, 1 << len(V)):
        bit = mask & -mask
        neighbourhood[mask] = (
            neighbourhood[mask ^ bit] | adjacency[bit.bit_length() - 1]
        )

    def rec(chosen: tuple[int, ...], candidates: tuple[int, ...], used: int):
        needed = 7 - len(chosen)
        if needed == 0:
            return chosen
        if len(candidates) < needed:
            return None
        for position, bag in enumerate(candidates):
            if bag & used:
                continue
            nxt = tuple(
                other for other in candidates[position + 1 :]
                if not other & (used | bag) and neighbourhood[bag] & other
            )
            if len(nxt) >= needed - 1:
                result = rec(chosen + (bag,), nxt, used | bag)
                if result is not None:
                    return result
        return None

    return rec((), connected, 0)


def boundary_edges(kind: str) -> set[tuple[int, int]]:
    rim = {(i, (i + 1) % 6) for i in range(6)}
    rim = {tuple(sorted(edge)) for edge in rim}
    if kind == "cycle":
        edges = set(rim)
    elif kind == "co-cycle":
        edges = set(itertools.combinations(range(6), 2)) - rim
    else:
        raise ValueError(kind)
    edges.update((i, 6) for i in range(6))
    return edges


def quotient(kind: str, row_a: int, row_b: int) -> set[tuple[int, int]]:
    edges = boundary_edges(kind)
    edges.add((A, B))
    edges.update((s, helper) for s in S for helper in (H1, H2))
    edges.update((s, A) for s in S if row_a >> s & 1)
    edges.update((s, B) for s in S if row_b >> s & 1)
    return {tuple(sorted(edge)) for edge in edges}


def maximal(pairs: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return [
        pair for pair in pairs
        if not any(
            pair != other
            and pair[0] | other[0] == other[0]
            and pair[1] | other[1] == other[1]
            for other in pairs
        )
    ]


def main() -> None:
    for kind in ("cycle", "co-cycle"):
        for duplicated in (0, 6):
            failures = []
            counts = Counter()
            for code in range(3**7):
                value = code
                row_a = row_b = 0
                for s in S:
                    choice = value % 3
                    value //= 3
                    if choice != 1:
                        row_a |= 1 << s
                    if choice != 0:
                        row_b |= 1 << s
                assert row_a | row_b == FULL
                if not (row_a >> duplicated & 1 and row_b >> duplicated & 1):
                    continue
                counts["checked"] += 1
                if k7_model(quotient(kind, row_a, row_b)) is None:
                    failures.append((row_a, row_b))
            maxima = maximal(failures)
            print(kind, "duplicated", duplicated, dict(counts),
                  "negative", len(failures), "maximal", len(maxima))
            for row_a, row_b in maxima:
                defect_a = tuple(s for s in S if not row_a >> s & 1)
                defect_b = tuple(s for s in S if not row_b >> s & 1)
                print(" defects", defect_a, "|", defect_b)


if __name__ == "__main__":
    main()
