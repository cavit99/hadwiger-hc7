#!/usr/bin/env python3
"""Classify the common-face order after the three rooted-K4 failures.

Contract the six facial arcs between selected portal roots to a root cycle.
Keep only the six literal portal edges, the C6+K1 boundary, and one opposite
full-shore helper.  A positive K7 model in this quotient lifts.  Negative
orders are candidate coherent annular orders.
"""

from __future__ import annotations

import itertools

from contact_order7_sixedge_web_probe import generic_minor_model


S = tuple(range(7))
R = tuple(range(7, 13))
H = 13
MISSING = {(0, 4), (0, 5), (1, 3), (1, 5), (2, 3), (2, 4)}
BOUNDARY = set(itertools.combinations(S, 2)) - MISSING


def host(order):
    edges = set(BOUNDARY)
    edges.update((s, H) for s in S)
    edges.update((i, R[i]) for i in range(6))
    for i in range(6):
        edges.add((R[order[i]], R[order[(i+1) % 6]]))
    return {tuple(sorted(e)) for e in edges}


def canonical(order):
    order = tuple(order)
    variants = []
    for seq in (order, tuple(reversed(order))):
        for k in range(6):
            variants.append(seq[k:]+seq[:k])
    return min(variants)


def main():
    seen = set()
    negative = []
    for perm in itertools.permutations(range(6)):
        order = canonical(perm)
        if order in seen:
            continue
        seen.add(order)
        model = generic_minor_model(14, host(order), 7)
        if model is None:
            negative.append(order)
    print("orders", len(seen), "negative", len(negative))
    for order in negative:
        print(order)
    expected = {
        (0, 1, 2, 5, 4, 3),
        (0, 1, 4, 3, 5, 2),
        (0, 2, 1, 4, 5, 3),
    }
    assert len(seen) == 60
    assert set(negative) == expected


if __name__ == "__main__":
    main()
