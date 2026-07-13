#!/usr/bin/env python3
"""Classify one cut vertex's boundary contacts that root a K5 in B+t."""

from __future__ import annotations

import itertools

from contact_order7_sixedge_web_probe import generic_minor_model


def minimal_positive(missing: set[tuple[int, int]]):
    # B={0,...,4}; t=5.  `missing` contains missing pairs inside B.
    base = set(itertools.combinations(range(5), 2)) - missing
    positives = []
    for size in range(6):
        for row in itertools.combinations(range(5), size):
            edges = set(base)
            edges.update((5, x) for x in row)
            if generic_minor_model(6, edges, 5):
                positives.append(frozenset(row))
    return sorted(
        [r for r in positives if not any(q < r for q in positives)],
        key=lambda r: (len(r), tuple(r)),
    )


def main():
    # Type I: K5 minus two adjacent edges 1-3 and 2-3.
    print("one-hole", minimal_positive({(1, 3), (2, 3)}))
    # Type II: K5 minus two disjoint edges 0-1 and 2-3.
    print("antipodal", minimal_positive({(0, 1), (2, 3)}))


if __name__ == "__main__":
    main()
