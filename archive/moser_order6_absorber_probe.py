#!/usr/bin/env python3
"""Probe singleton-w absorbers in archived order-six shore witnesses.

This is a conservative test: optional w--U edges are omitted.  A positive
certificate therefore uses only the internal shore, its archived attachment
rows, the fixed Moser boundary, and the archived optional edge aw.
"""

from __future__ import annotations

import json
from itertools import combinations


ROOTS = (0, 2, 4, 5, 6)
W = "w"
A = 1
L = (0, 2, 4, 5, 6, W, A)
MISSING = ((0, 5), (5, 2), (2, 4), (4, 6), (6, 0))
FRAMES = ((0, 2), (0, 3), (1, 3), (1, 4), (2, 4))
MOSER = {
    frozenset(edge)
    for edge in (
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 6), (2, 6),
        (3, 4), (3, 5), (4, 5), (5, 6),
    )
}


def d(i: int) -> tuple[str, int]:
    return ("d", i)


def b(x: int | str) -> tuple[str, int | str]:
    return ("b", x)


def graph_edges(record: dict) -> set[frozenset]:
    edges = {
        frozenset((d(i), d(j))) for i, j in record["internal_edges"]
    }
    for i, row in enumerate(record["rows"]):
        for bit, label in enumerate(L):
            if row & (1 << bit):
                edges.add(frozenset((d(i), b(label))))
    edges |= {frozenset((b(x), b(y))) for x, y in MOSER}
    if record["aw"]:
        edges.add(frozenset((b(A), b(W))))
    return edges


def connected(vertices: set, edges: set[frozenset]) -> bool:
    if not vertices:
        return False
    seen = {next(iter(vertices))}
    while True:
        more = {
            y
            for x in seen
            for y in vertices - seen
            if frozenset((x, y)) in edges
        }
        if not more:
            return seen == vertices
        seen |= more


def adjacent(first: set, second: set, edges: set[frozenset]) -> bool:
    return any(frozenset((x, y)) in edges for x in first for y in second)


def masks() -> range:
    return range(1, 1 << 6)


def vertices(mask: int) -> set:
    return {d(i) for i in range(6) if mask & (1 << i)}


def w_region(remaining: set, edges: set[frozenset]) -> set:
    """All remaining D-components adjacent to w, together with w."""
    unseen = set(remaining)
    region = {b(W)}
    while unseen:
        seed = next(iter(unseen))
        comp = {seed}
        while True:
            more = {
                y
                for x in comp
                for y in unseen - comp
                if frozenset((x, y)) in edges
            }
            if not more:
                break
            comp |= more
        unseen -= comp
        if adjacent(comp, {b(W)}, edges):
            region |= comp
    return region


def find_absorber_masks(
    record: dict, frame: tuple[int, int]
) -> tuple[bool, tuple[int, int, int] | None]:
    edges = graph_edges(record)
    i, j = frame
    e, f = MISSING[i], MISSING[j]
    leftover = next(root for root in ROOTS if root not in e + f)
    crossed = False

    for mask_e in masks():
        block_e = vertices(mask_e) | {b(e[0]), b(e[1])}
        if not connected(block_e, edges):
            continue
        for mask_f in masks():
            if mask_e & mask_f:
                continue
            block_f = vertices(mask_f) | {b(f[0]), b(f[1])}
            if not connected(block_f, edges):
                continue
            crossed = True
            if not adjacent(block_e, block_f, edges):
                # Enlarging along a connector is represented by another
                # assignment of the unused shore vertices to the blocks.
                continue
            remaining = vertices(((1 << 6) - 1) ^ (mask_e | mask_f))
            absorber = w_region(remaining, edges)
            targets = (block_e, block_f, {b(leftover)}, {b(A)})
            if all(adjacent(absorber, target, edges) for target in targets):
                mask_w = sum(1 << node[1] for node in absorber if node[0] == "d")
                return True, (mask_e, mask_f, mask_w)
    return crossed, None


def frame_status(record: dict, frame: tuple[int, int]) -> tuple[bool, bool]:
    crossed, certificate = find_absorber_masks(record, frame)
    return crossed, certificate is not None


def main() -> None:
    with open("portal_order6_contraction_obstruction.json", encoding="utf-8") as f:
        records = [
            record for record in json.load(f)["records"]
            if record["status"] == "sat"
        ]

    summary = {"no_cross": 0, "cross_absorbed": 0, "cross_unabsorbed": 0}
    unabsorbed = []
    for record in records:
        for frame in FRAMES:
            crossed, absorbed = frame_status(record, frame)
            if not crossed:
                summary["no_cross"] += 1
            elif absorbed:
                summary["cross_absorbed"] += 1
            else:
                summary["cross_unabsorbed"] += 1
                unabsorbed.append((record["type"], frame))

    assert sum(summary.values()) == 65 * 5
    print(summary)
    print("first unabsorbed crossed frames:", unabsorbed[:20])


if __name__ == "__main__":
    main()
