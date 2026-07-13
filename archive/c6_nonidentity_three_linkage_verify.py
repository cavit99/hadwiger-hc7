#!/usr/bin/env python3
"""Verify the nonidentity three-linkage certificates for C6 + K1.

The boundary W={0,...,5} induces the triangular prism with triangles
P={0,1,2}, Q={3,4,5} and matching 03,14,25; vertex 6 is universal on
the boundary.  Vertices 7,8,9 represent three disjoint linkage pieces,
and 10 represents the contracted opposite full shore.  For each
permutation linking P to Q and each of the three connector trees on the
pieces, search only for the transparent certificate form with singleton
bags 0,1,2,6,10 and two bags partitioning {3,4,5,7,8,9}.
"""

from __future__ import annotations

import itertools


P = (0, 1, 2)
Q = (3, 4, 5)
PIECES = (7, 8, 9)
H = 10
SINGLETONS = (0, 1, 2, 6, H)
REST = (3, 4, 5, 7, 8, 9)

# Missing cycle 0-4-2-3-1-5-0.
MISSING = {(0, 4), (0, 5), (1, 3), (1, 5), (2, 3), (2, 4)}
BOUNDARY = set(itertools.combinations(range(7), 2)) - MISSING

# The three labelled trees on pieces A=7,B=8,C=9.
TREES = {
    "A-centre": ((7, 8), (7, 9)),
    "B-centre": ((7, 8), (8, 9)),
    "C-centre": ((7, 9), (8, 9)),
}


def edges_for(permutation: tuple[int, int, int], tree):
    edges = {tuple(sorted(e)) for e in BOUNDARY}
    edges.update((s, H) for s in range(7))
    for p, q, piece in zip(P, permutation, PIECES):
        edges.add(tuple(sorted((p, piece))))
        edges.add(tuple(sorted((q, piece))))
    edges.update(tuple(sorted(e)) for e in tree)
    return edges


def connected(vertices, edges):
    vertices = set(vertices)
    reached = {next(iter(vertices))}
    while True:
        expanded = reached | {
            y for x, y in edges if x in reached and y in vertices
        } | {
            x for x, y in edges if y in reached and x in vertices
        }
        if expanded == reached:
            return reached == vertices
        reached = expanded


def adjacent(left, right, edges):
    return any(tuple(sorted((x, y))) in edges for x in left for y in right)


def certificate(permutation, tree):
    edges = edges_for(permutation, tree)
    for size in range(1, len(REST)):
        for left_tuple in itertools.combinations(REST, size):
            # Quotient by swapping the final two bags.
            if REST[0] not in left_tuple:
                continue
            left = frozenset(left_tuple)
            right = frozenset(REST) - left
            bags = tuple(frozenset((x,)) for x in SINGLETONS) + (left, right)
            if not all(connected(bag, edges) for bag in bags):
                continue
            if all(adjacent(bags[i], bags[j], edges)
                   for i in range(7) for j in range(i)):
                return bags
    return None


def label(permutation):
    return " ".join(f"{p}{q}" for p, q in zip(P, permutation))


def main():
    identity = (3, 4, 5)
    for permutation in itertools.permutations(Q):
        row = []
        for name, tree in TREES.items():
            model = certificate(permutation, tree)
            if permutation == identity:
                assert model is None
            else:
                assert model is not None
            row.append((name, model))
        print(label(permutation))
        for name, model in row:
            print(" ", name, model)


if __name__ == "__main__":
    main()
