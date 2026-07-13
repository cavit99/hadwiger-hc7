#!/usr/bin/env python3
"""Finite quotient checks for the double-Moser outer-portal peel.

The six boundary vertices are x1,x2,x3,x4,p,q.  The guaranteed graph is
two triangles x1-x2-q and x3-x4-p joined by pq.  A shore row has one
possible missed boundary vertex.  The program verifies two statements:

* four rows always have the representative-plus-core certificate used in
  Theorem 3.1 of ``hadwiger_double_moser_outer_portal_peel.md``;
* three rows have the two-leftover-bag certificate unless their nonempty
  defects are the two ends of one literal edge, with both ends occurring.

No graph library is used.
"""

from itertools import combinations, permutations, product


X = frozenset(range(4))
W = tuple(range(6))
EDGES = {
    frozenset(edge)
    for edge in ((0, 1), (2, 3), (4, 2), (4, 3),
                 (5, 0), (5, 1), (4, 5))
}


def adjacent(left, right):
    return frozenset((left, right)) in EDGES


def connected(vertices):
    vertices = set(vertices)
    reached = {next(iter(vertices))}
    while True:
        expanded = reached | {
            y for x in reached for y in vertices if adjacent(x, y)
        }
        if expanded == reached:
            return reached == vertices
        reached = expanded


def cross_edge(left, right):
    return any(adjacent(x, y) for x in left for y in right)


def incidence_free(defects, representatives):
    if len(set(representatives)) != len(representatives):
        return False
    if any(representatives[i] == defects[i] for i in range(len(defects))):
        return False
    return not any(
        representatives[j] == defects[i]
        and representatives[i] == defects[j]
        for i, j in combinations(range(len(defects)), 2)
    )


def four_row_certificate(defects):
    for representatives in permutations(W, 4):
        if not incidence_free(defects, representatives):
            continue
        unused_core = X - set(representatives)
        for y in unused_core:
            if all(
                y != defects[i] or adjacent(y, representatives[i])
                for i in range(4)
            ):
                return representatives, y
    return None


def bipartitions(vertices):
    vertices = set(vertices)
    first = min(vertices)
    for size in range(1, len(vertices)):
        for left_tuple in combinations(vertices, size):
            left = set(left_tuple)
            if first not in left:
                continue
            yield left, vertices - left


def shore_meets_bag(row, bag, defects, representatives):
    # The shore itself meets every boundary vertex except its defect.  If
    # the whole bag is missed, the representative may still supply an edge.
    return (
        any(vertex != defects[row] for vertex in bag)
        or any(adjacent(representatives[row], vertex) for vertex in bag)
    )


def three_row_certificate(defects):
    for representatives in permutations(W, 3):
        if not incidence_free(defects, representatives):
            continue
        unused = set(W) - set(representatives)
        for left, right in bipartitions(unused):
            if not (connected(left) and connected(right)):
                continue
            if not cross_edge(left, right):
                continue
            if not (left & X and right & X):
                continue
            if all(
                shore_meets_bag(i, left, defects, representatives)
                and shore_meets_bag(i, right, defects, representatives)
                for i in range(3)
            ):
                return representatives, left, right
    return None


def exceptional_three_profile(defects):
    defect_set = set(defects)
    return defect_set in ({0, 1}, {2, 3})


def main():
    four_failures = [
        defects for defects in product(W, repeat=4)
        if four_row_certificate(defects) is None
    ]
    assert not four_failures

    three_failures = [
        defects for defects in product(W, repeat=3)
        if three_row_certificate(defects) is None
    ]
    assert len(three_failures) == 12
    assert all(exceptional_three_profile(defects) for defects in three_failures)
    assert all(len(set(defects)) == 2 for defects in three_failures)

    print("four-row profiles: 1296/1296 certified")
    print("three-row profiles: 204/216 certified")
    print("three-row residue: both ends of one literal edge, each occurring")


if __name__ == "__main__":
    main()
