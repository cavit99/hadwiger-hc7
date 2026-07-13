#!/usr/bin/env python3
"""Exact adjacent-piece contact atlas for the C6+K1 boundary."""

from __future__ import annotations

import itertools

import k331_two_piece_contact_atlas as base


S = base.S
X, Y, H = base.X, base.Y, base.H
# Isolated vertex 6; the six missing edges form 0-4-2-3-1-5-0.
MISSING = {(0, 4), (0, 5), (1, 3), (1, 5), (2, 3), (2, 4)}


def quotient_edges(mask_x, mask_y):
    edges = set(itertools.combinations(S, 2)) - MISSING
    edges.add((X, Y))
    edges.update((s, H) for s in S)
    edges.update((s, X) for s in mask_x)
    edges.update((s, Y) for s in mask_y)
    return {tuple(sorted(edge)) for edge in edges}


def mask_set(mask):
    return frozenset(s for s in S if mask >> s & 1)


def main():
    failures = []
    full = (1 << 7) - 1
    for code in range(3 ** 7):
        value = code
        mask_x = mask_y = 0
        for s in S:
            choice = value % 3
            value //= 3
            if choice != 1:
                mask_x |= 1 << s
            if choice != 0:
                mask_y |= 1 << s
        mx, my = mask_set(mask_x), mask_set(mask_y)
        if base.fast_k7_model(quotient_edges(mx, my)) is None:
            failures.append((mx, my))

    maximal = [pair for pair in failures
               if not any(pair != other and pair[0] <= other[0]
                          and pair[1] <= other[1]
                          for other in failures)]
    print("candidate branch partitions", len(base.CANDIDATES))
    print("contact pairs checked", 3 ** 7)
    print("negative pairs", len(failures))
    print("maximal negative pairs", len(maximal))
    for mx, my in sorted(maximal,
                         key=lambda p: (tuple(sorted(p[0])),
                                        tuple(sorted(p[1])))):
        print("X", tuple(sorted(mx)), "Y", tuple(sorted(my)))


if __name__ == "__main__":
    main()
