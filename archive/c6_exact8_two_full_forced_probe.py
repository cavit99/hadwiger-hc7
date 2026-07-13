#!/usr/bin/env python3
"""Exact K7-minor probe for the forced two-full-shore exact-8 quotient."""

from __future__ import annotations

import itertools

from contact_order7_sixedge_web_probe import generic_minor_model


MISSING = {(0, 4), (0, 5), (1, 3), (1, 5), (2, 3), (2, 4)}
BOUNDARY = set(itertools.combinations(range(7), 2)) - MISSING
ANTIPODAL = ({0, 3}, {1, 4}, {2, 5})
F_NEIGHBOURS = {
    v: {w for w in range(6) if tuple(sorted((v, w))) in MISSING}
    for v in range(6)
}


def quotient(a: set[int]):
    b = sorted(set(range(7)) - a)
    # Relabel B as 0..4, T as 5..7 and the two full shores as 8,9.
    old_to_new = {old: new for new, old in enumerate(b)}
    edges = {
        tuple(sorted((old_to_new[x], old_to_new[y])))
        for x, y in BOUNDARY if x in old_to_new and y in old_to_new
    }
    for h in (8, 9):
        edges.update((h, x) for x in range(8))
    return {tuple(sorted(e)) for e in edges}, b


def main():
    rows = [(f"N_F({v})", F_NEIGHBOURS[v]) for v in range(6)]
    rows += [(f"M({i})", set(a)) for i, a in enumerate(ANTIPODAL)]
    for name, a in rows:
        edges, b = quotient(a)
        model = generic_minor_model(10, edges, 7)
        print(name, "B", b, "positive" if model else "negative", model or "")
        optional = list(itertools.combinations(range(5, 8), 2))
        optional += [(t, x) for t in range(5, 8) for x in range(5)]
        positive_one = []
        for edge in optional:
            repaired = set(edges)
            repaired.add(tuple(sorted(edge)))
            if generic_minor_model(10, repaired, 7):
                positive_one.append(edge)
        print("  single repairs", positive_one)


if __name__ == "__main__":
    main()
