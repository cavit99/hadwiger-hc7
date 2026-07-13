#!/usr/bin/env python3
"""Verify the finite boundary assignment in the Moser cutvertex lemma.

For a missing C5 edge e=xy, one endpoint o is omitted from the four
root bags.  The unused boundary vertices are A={1,3,o}.  Each of the two
connected shores misses at most one boundary vertex, and their defects
are distinct.  We assign distinct vertices of A to the shores so that
each shore becomes N-meeting and any missed retained root is repaired.

This is a dependency-free exhaustive check of the table printed below.
"""

from itertools import product

N = set(range(7))
U = {0, 2, 4, 5, 6}
C5 = [(0, 5), (5, 2), (2, 4), (4, 6), (6, 0)]
M_EDGES = {
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 2), (1, 6), (2, 6),
    (3, 4), (3, 5), (4, 5), (5, 6),
}
M_EDGES |= {(b, a) for a, b in tuple(M_EDGES)}


def assignment(edge, omitted, defect_1, defect_2):
    retained = U - {omitted}
    available = (omitted, 1, 3)

    def allowed(defect, anchor):
        # A shore is adjacent to every boundary vertex except possibly
        # its defect, so the absorbed anchor must not be that defect.
        if anchor == defect:
            return False
        # If a retained root was missed, the anchor must repair it by a
        # Moser-spindle edge.
        return defect not in retained or (defect, anchor) in M_EDGES

    for a_1, a_2 in product(available, repeat=2):
        if a_1 != a_2 and allowed(defect_1, a_1) and allowed(defect_2, a_2):
            return a_1, a_2
    return None


def failures(edge, omitted):
    defects = [None, *sorted(N)]
    bad = []
    for d_1, d_2 in product(defects, repeat=2):
        # If both shores have a defect, the defects are distinct because
        # their union is the full exterior component and N(C)=N.
        if d_1 is not None and d_1 == d_2:
            continue
        if assignment(edge, omitted, d_1, d_2) is None:
            bad.append((d_1, d_2))
    return bad


expected = {
    ((0, 5), 0): [],
    ((5, 2), 5): [],
    ((2, 4), 2): [(4, 5), (5, 4)],
    ((2, 4), 4): [(2, 6), (6, 2)],
    ((4, 6), 6): [],
    ((6, 0), 0): [],
}

for key, want in expected.items():
    got = failures(*key)
    assert got == want, (key, got, want)

# In the central case 24, the two exceptional lists are disjoint, so
# choosing the omission adaptively always works.
for d_1, d_2 in product([None, *sorted(N)], repeat=2):
    if d_1 is not None and d_1 == d_2:
        continue
    assert (
        assignment((2, 4), 2, d_1, d_2) is not None
        or assignment((2, 4), 4, d_1, d_2) is not None
    ), (d_1, d_2)

print("Moser cutvertex assignment table verified")
for key in expected:
    print(f"edge={key[0]}, omit={key[1]}, failures={expected[key]}")

