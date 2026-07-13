#!/usr/bin/env python3
"""Exact quotient atlas for a split full shore behind a Moser 7-boundary.

The graph has the seven Moser boundary vertices, two adjacent pieces X,Y
whose boundary rows cover the boundary, and two further full helpers.  It
classifies row pairs forced to share two low-boundary-degree Moser roots.
"""

from __future__ import annotations

import itertools

S = tuple(range(7))
X, Y, H1, H2 = 7, 8, 9, 10
V = tuple(range(11))
FULL = (1 << 7) - 1
MOSER = {tuple(map(int, e)) for e in "01 02 03 04 12 16 26 34 35 45 56".split()}
MOSER = {tuple(sorted(e)) for e in MOSER}


def k_minor_model(edges: set[tuple[int, int]], k: int = 7):
    n = len(V)
    adjacency = [0] * n
    for i, j in edges:
        adjacency[i] |= 1 << j
        adjacency[j] |= 1 << i
    neighbour_union = [0] * (1 << n)
    connected: list[int] = []
    for mask in range(1, 1 << n):
        low = mask & -mask
        i = low.bit_length() - 1
        neighbour_union[mask] = neighbour_union[mask ^ low] | adjacency[i]
        reached = low
        while True:
            expanded = reached | (neighbour_union[reached] & mask)
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            connected.append(mask)
    connected.sort(key=lambda mask: (mask.bit_count(), mask))

    def adjacent(a: int, b: int) -> bool:
        return not (a & b) and bool(neighbour_union[a] & b)

    def rec(chosen: list[int], candidates: list[int], used: int):
        if len(chosen) == k:
            return tuple(chosen)
        needed = k - len(chosen)
        if len(candidates) < needed:
            return None
        for pos, a in enumerate(candidates):
            if a & used:
                continue
            nxt = [
                b
                for b in candidates[pos + 1 :]
                if not b & (used | a) and adjacent(a, b)
            ]
            if len(nxt) >= needed - 1:
                answer = rec(chosen + [a], nxt, used | a)
                if answer is not None:
                    return answer
        return None

    return rec([], connected, 0)


def edges_for(p: int, q: int) -> set[tuple[int, int]]:
    edges = set(MOSER)
    edges.add((X, Y))
    edges.update((s, h) for h in (H1, H2) for s in S)
    edges.update((s, X) for s in S if p >> s & 1)
    edges.update((s, Y) for s in S if q >> s & 1)
    return {tuple(sorted(e)) for e in edges}


def fmt(mask: int) -> str:
    return "".join(str(s) for s in S if mask >> s & 1) or "-"


def main() -> None:
    negatives: dict[tuple[int, int], list[tuple[int, int]]] = {}
    checked = positive = 0
    for a, b in itertools.combinations(range(1, 7), 2):
        common = (1 << a) | (1 << b)
        pairs: list[tuple[int, int]] = []
        for p in range(1, 1 << 7):
            if p & common != common:
                continue
            for q in range(p, 1 << 7):
                if q & common != common or p | q != FULL:
                    continue
                checked += 1
                if k_minor_model(edges_for(p, q)):
                    positive += 1
                else:
                    pairs.append((p, q))
        negatives[a, b] = pairs
        print(a, b, "negative", len(pairs))
        maximal = [
            (p, q)
            for p, q in pairs
            if not any(
                (p != pp or q != qq)
                and (p & ~pp) == 0
                and (q & ~qq) == 0
                for pp, qq in pairs
            )
        ]
        print(" maximal", [(fmt(p), fmt(q)) for p, q in maximal])
    print("checked", checked, "positive", positive, "negative", checked - positive)


if __name__ == "__main__":
    main()
