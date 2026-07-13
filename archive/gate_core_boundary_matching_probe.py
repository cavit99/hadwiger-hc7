#!/usr/bin/env python3
"""Classify pure-core six-boundary nonedge matchings.

X={0,1,2,3} induces 2K2 with graph edges 01 and 23, so its nonedges
form C4.  Vertices p=4,q=5 have prescribed core-colour mates a,b and
therefore are nonadjacent to those mates.  When a=b, p,q are also
nonadjacent.  Optional nonedges are otherwise unrestricted.

The script prints inclusion-maximal nonedge graphs having no perfect
matching, modulo automorphisms of 2K2 and interchange of p,q.
"""

from __future__ import annotations

import itertools


X = range(4)
P, Q = 4, 5
X_NONEDGES = {
    frozenset(edge)
    for edge in ((0, 2), (0, 3), (1, 2), (1, 3))
}
ALL_OPTIONAL = {
    frozenset((u, v))
    for u in (P, Q)
    for v in X
} | {frozenset((P, Q))}


def has_perfect_matching(edges: set[frozenset[int]]) -> bool:
    vertices = set(range(6))
    first = min(vertices)
    for mate in vertices - {first}:
        if frozenset((first, mate)) not in edges:
            continue
        rem = vertices - {first, mate}
        u = min(rem)
        for w in rem - {u}:
            if frozenset((u, w)) not in edges:
                continue
            last = rem - {u, w}
            if frozenset(last) in edges:
                return True
    return False


def x_automorphisms() -> list[tuple[int, ...]]:
    graph_edges = {frozenset((0, 1)), frozenset((2, 3))}
    return [
        perm
        for perm in itertools.permutations(X)
        if {
            frozenset((perm[u], perm[v])) for u, v in ((0, 1), (2, 3))
        } == graph_edges
    ]


AUT = x_automorphisms()


def canonical(
    a: int, b: int, edges: set[frozenset[int]]
) -> tuple[int, int, tuple[tuple[int, int], ...]]:
    values = []
    for perm in AUT:
        for swap in (False, True):
            image = {i: perm[i] for i in X}
            image[P], image[Q] = ((Q, P) if swap else (P, Q))
            aa, bb = ((b, a) if swap else (a, b))
            transformed = tuple(sorted(
                tuple(sorted((image[u], image[v])))
                for u, v in (tuple(edge) for edge in edges)
            ))
            values.append((perm[aa], perm[bb], transformed))
    return min(values)


def main() -> None:
    representatives = set()
    for a in X:
        for b in X:
            forced = {
                frozenset((P, a)),
                frozenset((Q, b)),
            }
            if a == b:
                forced.add(frozenset((P, Q)))
            optional = sorted(ALL_OPTIONAL - forced, key=lambda e: tuple(sorted(e)))
            bad = []
            for mask in range(1 << len(optional)):
                edges = X_NONEDGES | forced | {
                    optional[i] for i in range(len(optional)) if mask >> i & 1
                }
                if not has_perfect_matching(edges):
                    bad.append(edges)
            for edges in bad:
                if any(edges < other for other in bad):
                    continue
                representatives.add(canonical(a, b, edges))

    print(f"maximal obstruction orbits: {len(representatives)}")
    for a, b, edges in sorted(representatives):
        print("mates", a, b, "nonedges", edges)


if __name__ == "__main__":
    main()

