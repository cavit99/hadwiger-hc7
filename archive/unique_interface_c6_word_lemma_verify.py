#!/usr/bin/env python3
"""Verify the finite hand table in hadwiger_c6_double_overlap_arc_lock.md."""

from __future__ import annotations

import itertools

from contact_order7_five_edge_verify import verify_model
from unique_interface_c6_arc_rows_probe import arcs, edges_for


TABLE = {
    ((1, 2, 3), (1, 2, 4, 5, 6)): ((1,), (2,), (3, 7), (4, 8)),
    ((1, 2, 3, 4), (1, 2, 5, 6)): ((1,), (2,), (3, 7), (5, 8)),
    ((1, 2, 3, 4), (1, 3, 5, 6)): ((1,), (2,), (4, 7), (3, 8)),
    ((1, 2, 3, 4), (2, 3, 5, 6)): ((1,), (2,), (3, 7), (6, 8)),
    ((1, 2, 3, 4, 5), (1, 3, 6)): ((1,), (2,), (4, 7), (3, 8)),
    ((1, 2, 3, 4, 5), (1, 4, 6)): ((1,), (6,), (5, 7), (4, 8)),
    ((1, 2, 3, 4, 5), (2, 3, 6)): ((1,), (2,), (3, 7), (6, 8)),
    ((1, 2, 3, 4, 5), (2, 4, 6)): ((1,), (2,), (3, 7), (6, 8)),
    ((1, 2, 3, 4, 5, 6), (1, 3)): ((1,), (2,), (4, 7), (3, 8)),
    ((1, 2, 3, 5), (1, 2, 4, 6)): ((1,), (2,), (3, 7), (4, 8)),
    ((1, 2, 3, 5), (1, 3, 4, 6)): ((1,), (2,), (5, 7), (3, 8)),
    ((1, 2, 3, 5), (2, 4, 5, 6)): ((1,), (2,), (3, 7), (6, 8)),
    ((1, 2, 4, 5), (1, 3, 4, 6)): ((1,), (2,), (4, 7), (3, 8)),
}


def dihedral_maps():
    for reflection in (False, True):
        for shift in range(6):
            yield {
                i + 1: (((-i if reflection else i) + shift) % 6) + 1
                for i in range(6)
            }


def canonical(left: set[int], right: set[int]):
    encodings = []
    for permutation in dihedral_maps():
        for first, second in ((left, right), (right, left)):
            encodings.append((
                tuple(sorted(permutation[x] for x in first)),
                tuple(sorted(permutation[x] for x in second)),
            ))
    return min(encodings)


def table_models_are_valid() -> None:
    def verify_k4(edges, bags):
        adjacency = {x: set() for x in range(1, 9)}
        for x, y in edges:
            adjacency[x].add(y)
            adjacency[y].add(x)
        assert len(bags) == 4
        assert len(set().union(*(set(bag) for bag in bags))) == sum(
            len(bag) for bag in bags
        )
        for bag in bags:
            reached = {bag[0]}
            while True:
                expanded = reached | {
                    y for x in reached for y in adjacency[x] if y in bag
                }
                if expanded == reached:
                    break
                reached = expanded
            assert reached == set(bag)
        for i, first in enumerate(bags):
            for second in bags[:i]:
                assert any(y in adjacency[x] for x in first for y in second)

    for (left, right), bags in TABLE.items():
        # The local graph has cycle vertices 1..6 and helpers P=7,Q=8.
        edges = {(i, i % 6 + 1) for i in range(1, 7)}
        edges.add((7, 8))
        edges.update((7, x) for x in left)
        edges.update((8, x) for x in right)
        verify_k4(edges, bags)


def classify_words() -> tuple[int, int, int]:
    table_count = arc_count = antipodal_count = 0
    for roots in itertools.combinations(range(1, 7), 2):
        free = tuple(x for x in range(1, 7) if x not in roots)
        first_arc, second_arc = arcs(*roots)
        for bits in range(16):
            left, right = set(roots), set(roots)
            for index, x in enumerate(free):
                (left if bits >> index & 1 else right).add(x)
            if (left, right) in ((first_arc, second_arc),
                                 (second_arc, first_arc)):
                arc_count += 1
                continue
            distance = min((roots[1] - roots[0]) % 6,
                           (roots[0] - roots[1]) % 6)
            if distance == 3 and (len(left) == 2 or len(right) == 2):
                antipodal_count += 1
                continue
            assert canonical(left, right) in TABLE, (roots, bits, left, right)
            table_count += 1
    return table_count, antipodal_count, arc_count


def special_models_are_valid() -> None:
    # P is small, Q full; neither zP nor zQ is used.
    left, right = {1, 4}, set(range(1, 7))
    bags = ((0,), (4, 5), (6,), (2, 7), (8,), (1, 9), (3, 10))
    for split_opposite in (False, True):
        verify_model(edges_for(left, right, split_opposite), bags)

    # P is full, Q small.
    left, right = set(range(1, 7)), {1, 4}
    bags = ((0,), (4, 5), (6,), (2, 7), (8,), (3, 9), (1, 10))
    for split_opposite in (False, True):
        verify_model(edges_for(left, right, split_opposite), bags)


def main() -> None:
    table_models_are_valid()
    special_models_are_valid()
    table_count, antipodal_count, arc_count = classify_words()
    print("binary words", table_count + antipodal_count + arc_count)
    print("covered by 13-row K4 table", table_count)
    print("antipodal full-row K7 certificates", antipodal_count)
    print("complementary-arc residuals", arc_count)


if __name__ == "__main__":
    main()
