#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Audit the triangle/repair choice in Lemma 3.1 for K1 join C6."""

from __future__ import annotations

import itertools


S = tuple(range(7))
Z = 0
C = tuple(range(1, 7))
J = {tuple(sorted((Z, c))) for c in C}
J.update(tuple(sorted((C[i], C[(i + 1) % 6]))) for i in range(6))


def adjacent(a, b):
    return tuple(sorted((a, b))) in J


triangles = [
    set(t) for t in itertools.combinations(S, 3)
    if all(adjacent(a, b) for a, b in itertools.combinations(t, 2))
]
assert len(triangles) == 6

for defect in (None,) + S:
    witness = None
    for triangle in triangles:
        for root in set(S) - triangle:
            if root == defect:
                continue
            if defect not in triangle or adjacent(root, defect):
                witness = (triangle, root)
                break
        if witness is not None:
            break
    assert witness is not None, defect
    print("defect", defect, "triangle", sorted(witness[0]), "repair", witness[1])

print("verified all seven defect labels and the full case")
