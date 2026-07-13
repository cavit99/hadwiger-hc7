#!/usr/bin/env python3
"""Probe a three-linkage split 2+1 over the two C6 exterior shores."""

import itertools

from k331_two_piece_contact_atlas import fast_k7_model


P = (0, 1, 2)
Q = (3, 4, 5)
PIECES = (7, 8, 9)
S = tuple(range(7))
MISSING = {(0, 4), (0, 5), (1, 3), (1, 5), (2, 3), (2, 4)}
BOUNDARY = set(itertools.combinations(S, 2)) - MISSING


def edges_for(permutation, alone):
    edges = {tuple(sorted(e)) for e in BOUNDARY}
    for p, q, piece in zip(P, permutation, PIECES):
        edges.add(tuple(sorted((p, piece))))
        edges.add(tuple(sorted((q, piece))))
    together = [piece for piece in PIECES if piece != alone]
    edges.add(tuple(sorted(together)))
    return edges


def main():
    for permutation in itertools.permutations(Q):
        print("pairs", tuple(zip(P, permutation)))
        for alone in PIECES:
            model = fast_k7_model(edges_for(permutation, alone))
            print(" alone", alone, "model", model)


if __name__ == "__main__":
    main()
