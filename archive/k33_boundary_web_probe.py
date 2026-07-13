#!/usr/bin/env python3
"""Explore cyclic terminal orders for the residual 2K3+K1 boundary.

The boundary graph is K1 join K3,3.  This script deliberately ignores
boundary chords while testing the shore society: it reports which cyclic
orders have every alternating crossing quotient containing K7, and it
classifies the bad crossing endpoint types for alternating six-orders.
"""

from __future__ import annotations

import itertools

import c5_core_k2_shore_verify as minor
import six_edge_web_template_search as web


A = frozenset((0, 1, 5))
B = frozenset((2, 3, 4))
C = 6
MISSING = {tuple(sorted(edge)) for edge in web.EXCEPTIONS[2]}
BOUNDARY = web.PAIRS - MISSING


def canonical_orders(vertices):
    first = min(vertices)
    for tail in itertools.permutations(v for v in vertices if v != first):
        order = (first,) + tail
        if order[1] < order[-1]:
            yield order


def crossing_model(first, second):
    edges = web.quotient_edges(BOUNDARY, first, second)
    return minor.k_minor_model(edges)


def crossing_failures(order):
    failures = []
    for i, r, j, s in itertools.combinations(range(len(order)), 4):
        first = (order[i], order[j])
        second = (order[r], order[s])
        if crossing_model(first, second) is None:
            failures.append((first, second))
    return tuple(failures)


def pair_type(pair):
    ends = frozenset(pair)
    if ends <= A:
        return "AA"
    if ends <= B:
        return "BB"
    if C in ends:
        return "cA" if len(ends & A) else "cB"
    return "AB"


def main():
    for size in range(4, 8):
        safe = []
        best = None
        for vertices in itertools.combinations(range(7), size):
            for order in canonical_orders(vertices):
                failures = crossing_failures(order)
                if not failures:
                    safe.append(order)
                score = len(failures)
                if best is None or score < best[0]:
                    best = (score, order, failures)
        print("size", size, "safe", len(safe), "examples", safe[:10])
        print(" best", best)

    order = (0, 2, 1, 3, 5, 4)
    print("alternating order", order)
    for first, second in crossing_failures(order):
        print(first, second, pair_type(first), pair_type(second))


if __name__ == "__main__":
    main()
