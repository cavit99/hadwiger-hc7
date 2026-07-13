#!/usr/bin/env python3
"""Audit the finite boundary counts in the Moser three-shore descent.

This is not a minor search.  It enumerates the optimal 4-colour partitions
of the labelled Moser spindle and checks the sharp circular fact used in
the hand proof: any cyclic order makes at most seven of the sixteen
three-pair matchings pairwise alternating.
"""

from __future__ import annotations

import itertools
from collections import Counter

V = tuple(range(7))
MOSER = {
    tuple(sorted(map(int, edge)))
    for edge in "01 02 03 04 12 16 26 34 35 45 56".split()
}
NONEDGES = set(itertools.combinations(V, 2)) - MOSER


def optimal_partitions():
    result = []
    for singleton in V:
        for matching in itertools.combinations(NONEDGES, 3):
            ends = [x for edge in matching for x in edge]
            if len(set(ends)) == 6 and set(ends) == set(V) - {singleton}:
                result.append((singleton, tuple(sorted(matching))))
    return tuple(sorted(set(result)))


def alternating(order, edge_1, edge_2):
    pos = {vertex: index for index, vertex in enumerate(order)}
    a, b = sorted((pos[edge_1[0]], pos[edge_1[1]]))
    c, d = sorted((pos[edge_2[0]], pos[edge_2[1]]))
    return a < c < b < d or c < a < d < b


def main() -> None:
    partitions = optimal_partitions()
    assert len(partitions) == 16
    singleton_counts = Counter(singleton for singleton, _ in partitions)
    assert sorted(singleton_counts.values()) == [2, 2, 2, 2, 2, 2, 4]

    maximum = 0
    witnesses = []
    for tail in itertools.permutations(V[1:]):
        order = (0,) + tail
        if order[1] > order[-1]:
            continue  # reversal
        count = sum(
            all(alternating(order, e, f) for e, f in itertools.combinations(matching, 2))
            for _, matching in partitions
        )
        if count > maximum:
            maximum = count
            witnesses = [order]
        elif count == maximum:
            witnesses.append(order)

    assert maximum == 7
    print("optimal partitions", len(partitions))
    print("counts by singleton", dict(sorted(singleton_counts.items())))
    print("maximum pairwise-alternating matchings in one circular order", maximum)
    print("number of maximizing orders modulo rotation/reversal", len(witnesses))


if __name__ == "__main__":
    main()
