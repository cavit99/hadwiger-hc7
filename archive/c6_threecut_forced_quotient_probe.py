#!/usr/bin/env python3
"""Probe the literal quotient forced by a 3-cut in the minimum C6+K1 atom.

The two components of D-T are contracted to x,y.  Each of the three cut
vertices is adjacent to both x and y.  We deliberately give T no boundary
edges and no internal edges, so a positive model uses only forced edges.
"""

from __future__ import annotations

import itertools

from contact_order7_sixedge_web_probe import generic_minor_model


S = tuple(range(7))
H, X, Y = 7, 8, 9
T = (10, 11, 12)
MISSING = {(0, 4), (0, 5), (1, 3), (1, 5), (2, 3), (2, 4)}
BOUNDARY = set(itertools.combinations(S, 2)) - MISSING
F_NEIGHBOURS = {
    v: {w for w in range(6) if tuple(sorted((v, w))) in MISSING}
    for v in range(6)
}
ANTIPODAL = ({0, 3}, {1, 4}, {2, 5})


def host(dx: set[int], dy: set[int]):
    edges = set(BOUNDARY)
    edges.update((s, H) for s in S)
    edges.update((X, s) for s in S if s not in dx)
    edges.update((Y, s) for s in S if s not in dy)
    for t in T:
        edges.add((X, t))
        edges.add((Y, t))
    return {tuple(sorted(e)) for e in edges}


def main():
    # The four canonical polarities of Theorem 2.5, translated from the
    # cyclic order (0,4,2,3,1,5) used by this verifier.
    rows = [
        ("singleton", {0}, {4, 5}),
        ("crossed one-hole", {0, 2}, {4, 3}),
        ("opposite one-hole", {0, 2}, {4, 1}),
        ("antipodal", {0, 3}, {4, 1}),
    ]

    for name, dx, dy in rows:
        model = generic_minor_model(13, host(dx, dy), 7)
        print(name, "positive" if model else "negative", model or "")


if __name__ == "__main__":
    main()
