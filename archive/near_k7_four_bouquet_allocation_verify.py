"""Allocation census for the (2,2,0) four-bouquet.

Labels 0,1,2 are a,b,c and 3,4,5 are the neutral clique labels.
The first two miss entries belong to pq-lobes and the last two to
pr-lobes.  ``spent_pair`` is the three-pole construction which absorbs
two boundary labels and leaves a literal K4.
"""

from itertools import combinations, permutations, product


L = tuple(range(6))
A, B, C = 0, 1, 2
NONEDGES = {frozenset((A, B)), frozenset((A, C))}


def adjacent(x, y):
    return x != y and frozenset((x, y)) not in NONEDGES


def spent_pair(misses):
    left = misses[:2]
    right = misses[2:]
    for i, j in product(range(2), repeat=2):
        common_miss = left[i] if left[i] == right[j] else None
        q_miss = left[1 - i]
        r_miss = right[1 - j]
        for x, y in permutations(L, 2):
            if not adjacent(x, y):
                continue
            core = set(L) - {x, y}
            if any(not adjacent(u, v) for u, v in combinations(core, 2)):
                continue
            # Q=q+left_other+x and R=r+right_other+y must be connected.
            if x == q_miss or y == r_miss:
                continue
            # P=p+left_i+right_j must see every remaining singleton.
            if common_miss is not None and common_miss in core:
                continue
            # The absorbed labels repair a sole missed core label.
            if q_miss in core and not adjacent(x, q_miss):
                continue
            if r_miss in core and not adjacent(y, r_miss):
                continue
            return i, j, x, y
    return None


bad = [m for m in product(L, repeat=4) if spent_pair(m) is None]
deficient = [m for m in bad if set(m) <= {A, B, C}]
uniform_neutral = [m for m in bad if len(set(m)) == 1 and m[0] >= 3]

assert len(bad) == 46
assert len(deficient) == 43
assert uniform_neutral == [(3, 3, 3, 3), (4, 4, 4, 4), (5, 5, 5, 5)]
assert set(bad) == set(deficient) | set(uniform_neutral)

print("profiles", 6**4)
print("spent-pair positive", 6**4 - len(bad))
print("deficient-triangle residue", len(deficient))
print("uniform-neutral residue", uniform_neutral)
