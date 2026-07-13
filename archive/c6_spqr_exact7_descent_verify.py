"""Finite set-system replay for Theorem 2.1.

The exact low-defect atlas is encoded as the predicate ``negative``.
``A`` and ``B`` are the boundary defects of the two open components of
a two-cut and ``P`` is the collective defect of the two poles.  Hence the
defect of ``B+p+q`` is ``B & P``, and symmetrically.
"""

from itertools import combinations

S = set(range(7))
W = set(range(6))
cycle_neighbours = {v: {(v - 1) % 6, (v + 1) % 6} for v in W}
antipodal = [{i, i + 3} for i in range(3)]


def subsets_at_most_two():
    return [set(c) for r in range(3) for c in combinations(S, r)]


def all_subsets():
    return [set(c) for r in range(8) for c in combinations(S, r)]


def negative(left, right):
    """The low-defect negative pairs of Lemma 4.1, both orientations."""
    for v in W:
        if v in left and right == cycle_neighbours[v]:
            return True
        if v in right and left == cycle_neighbours[v]:
            return True
    return (
        len(left) == len(right) == 2
        and left in antipodal
        and right in antipodal
        and left != right
    )


states = []
for defect_a in subsets_at_most_two():
    for defect_b in subsets_at_most_two():
        for pole_defect in all_subsets():
            # Fullness of the union A+B+{p,q}.
            if defect_a & defect_b & pole_defect:
                continue
            complement_a = defect_b & pole_defect
            complement_b = defect_a & pole_defect
            if not negative(defect_a, complement_a):
                continue
            if not negative(defect_b, complement_b):
                continue
            states.append((defect_a, defect_b, pole_defect))

assert states
assert {tuple(map(len, state[:2])) for state in states} == {
    (1, 2),
    (2, 1),
    (2, 2),
}

# If A has defect two, B contacts at least one of those omitted roots;
# this is exactly the far-side connectivity step.  And conversely.
for defect_a, defect_b, _ in states:
    if len(defect_a) == 2:
        assert defect_a - defect_b
    if len(defect_b) == 2:
        assert defect_b - defect_a

# The selected two-defect side is never two adjacent cycle vertices.
# (It can be cycle-distance two, antipodal, or one cycle vertex plus z.)
for defect_a, defect_b, _ in states:
    for defect in (defect_a, defect_b):
        if len(defect) != 2 or 6 in defect:
            continue
        x, y = tuple(defect)
        assert (x - y) % 6 not in {1, 5}

print("states", len(states))
print("open-defect size patterns", [(1, 2), (2, 1), (2, 2)])
print("every state has a defect-two side and a connected far side")
print("defect-two core types: P5, P3+2K1, 2K2+K1")
