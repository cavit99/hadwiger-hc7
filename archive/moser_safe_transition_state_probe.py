#!/usr/bin/env python3
"""Classify possible N-states in a six-colouring of a proper HC7 minor.

The neighbourhood is the labelled pure Moser spindle, a=1, b=3 and
U={0,2,4,5,6}.  Because alpha(N)=2 and v's colour is absent from N,
the nonsingleton classes form a matching of size two or three in the
complement.
"""

from __future__ import annotations

import itertools
from collections import Counter


N = tuple(range(7))
A, B = 1, 3
U = frozenset({0, 2, 4, 5, 6})
M_EDGES = {
    (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
    (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
}
NONEDGES = tuple(
    p for p in itertools.combinations(N, 2) if p not in M_EDGES
)


def matching(edges: tuple[tuple[int, int], ...]) -> bool:
    return len({x for e in edges for x in e}) == 2 * len(edges)


def classes(edges: tuple[tuple[int, int], ...]):
    paired = {x for e in edges for x in e}
    return [frozenset(e) for e in edges] + [
        frozenset({x}) for x in N if x not in paired
    ]


def kind(edges):
    cs = classes(edges)
    u_colors = sum(bool(c & U) for c in cs)
    a_shares_u = any(A in c and bool((c - {A}) & U) for c in cs)
    if u_colors == 3 and not a_shares_u:
        return "decorated-T trace"
    if a_shares_u:
        return f"a-shares-U / U uses {u_colors}"
    return f"a-separate / U uses {u_colors}"


def main() -> None:
    states = [
        es for q in (2, 3)
        for es in itertools.combinations(NONEDGES, q)
        if matching(es)
    ]
    counts = Counter(kind(es) for es in states)
    print("nonedges", NONEDGES)
    print("matching states", len(states), dict(sorted(counts.items())))
    for k in sorted(counts):
        print(k)
        for es in states:
            if kind(es) == k:
                print(" ", es)
    assert len(states) == 42
    assert counts == Counter({
        "decorated-T trace": 12,
        "a-shares-U / U uses 3": 2,
        "a-shares-U / U uses 4": 13,
        "a-shares-U / U uses 5": 4,
        "a-separate / U uses 4": 11,
    })


if __name__ == "__main__":
    main()
