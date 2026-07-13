#!/usr/bin/env python3
"""Exact portal atlas for the unique bad C6-frame crossing.

Boundary missing cycle: 0-4-2-3-1-5-0, with 6 isolated.  The bad frame
crossing has an X path for 05 and a Y path for 13; X,Y are adjacent and H
is the opposite full shore.  Enumerate all additional X/Y boundary
contacts, replay every K7 certificate exactly, and list the inclusion-
maximal negative contact pairs.
"""

from __future__ import annotations

import itertools

from k331_two_piece_contact_atlas import fast_k7_model


S = tuple(range(7))
F = {(0, 4), (0, 5), (1, 3), (1, 5), (2, 3), (2, 4)}
J = set(itertools.combinations(S, 2)) - F
X, Y, H = 7, 8, 9

BASE_X = frozenset((0, 5))
BASE_Y = frozenset((1, 3))
OPTIONAL = tuple((p, s) for p, base in ((X, BASE_X), (Y, BASE_Y))
                 for s in S if s not in base)


def quotient_edges(bits):
    edges = set(J)
    edges.add((X, Y))
    edges.update((s, H) for s in S)
    edges.update((s, X) for s in BASE_X)
    edges.update((s, Y) for s in BASE_Y)
    edges.update(tuple(sorted(OPTIONAL[i])) for i in range(len(OPTIONAL))
                 if bits >> i & 1)
    return edges


def contacts(bits, piece, base):
    answer = set(base)
    for i, (p, s) in enumerate(OPTIONAL):
        if p == piece and bits >> i & 1:
            answer.add(s)
    return tuple(sorted(answer))


def main():
    failures = []
    witnesses = {}
    for bits in range(1 << len(OPTIONAL)):
        model = fast_k7_model(quotient_edges(bits))
        if model is None:
            failures.append(bits)
        else:
            witnesses[bits] = model

    failure_set = set(failures)
    maximal = [
        bits for bits in failures
        if not any(not (bits >> i & 1) and
                   (bits | (1 << i)) in failure_set
                   for i in range(len(OPTIONAL)))
    ]

    # The two outward contacts are individually sufficient.
    x4 = next(i for i, edge in enumerate(OPTIONAL) if edge == (X, 4))
    y2 = next(i for i, edge in enumerate(OPTIONAL) if edge == (Y, 2))
    assert fast_k7_model(quotient_edges(1 << x4)) is not None
    assert fast_k7_model(quotient_edges(1 << y2)) is not None
    assert all(not (bits >> x4 & 1) and not (bits >> y2 & 1)
               for bits in failures)

    print("contact patterns", 1 << len(OPTIONAL))
    print("negative patterns", len(failures))
    print("maximal negative patterns", len(maximal))
    for bits in maximal:
        print("X", contacts(bits, X, BASE_X),
              "Y", contacts(bits, Y, BASE_Y))
    print("X4 witness", witnesses[1 << x4])
    print("Y2 witness", witnesses[1 << y2])


if __name__ == "__main__":
    main()
