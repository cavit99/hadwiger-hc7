#!/usr/bin/env python3
"""Verify the global cutvertex anchor lemma for the pure Moser boundary."""

from itertools import combinations, permutations

N = set(range(7))
EDGES = {
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 2), (1, 6), (2, 6),
    (3, 4), (3, 5), (4, 5), (5, 6),
}


def adjacent(a, b):
    return tuple(sorted((a, b))) in EDGES


TRIANGLES = [
    set(t) for t in combinations(sorted(N), 3)
    if all(tuple(sorted(e)) in EDGES for e in combinations(t, 2))
]
assert TRIANGLES == [
    {0, 1, 2}, {0, 3, 4}, {1, 2, 6}, {3, 4, 5}
]


def witness(d_1, d_2):
    """Return triangle and anchors for two one-defect adjacent shores.

    ``None`` denotes no boundary defect.  The third shore has no defect.
    """
    for triangle in TRIANGLES:
        outside = N - triangle
        for a_1, a_2, a_3 in permutations(outside, 3):
            if a_1 == d_1 or a_2 == d_2:
                continue
            if d_1 in triangle and not adjacent(a_1, d_1):
                continue
            if d_2 in triangle and not adjacent(a_2, d_2):
                continue
            return tuple(sorted(triangle)), (a_1, a_2, a_3)
    return None


defects = [None] + sorted(N)
checked = 0
for d_1 in defects:
    for d_2 in defects:
        # Full attachment of the union forbids a common nonempty defect.
        if d_1 is not None and d_1 == d_2:
            continue
        assert witness(d_1, d_2) is not None, (d_1, d_2)
        checked += 1

assert checked == 57
print("verified 57 global cutvertex defect pairs")

