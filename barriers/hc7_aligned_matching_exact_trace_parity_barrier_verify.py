#!/usr/bin/env python3
"""Verify the finite boundary claims in the aligned exact-trace barrier.

This checker does not construct the Dvořák--Swart realizers.  It verifies
the explicit boundary, the aligned perfect matching, the width-five tree
decomposition of its two-apex join, and the parity-cylinder calculation.
"""

from __future__ import annotations

from itertools import combinations


VERTICES = tuple(range(8))
R = frozenset((0, 1, 2))
A = frozenset((3, 4))
B = frozenset((5, 6))
X = 7
EDGES = {
    tuple(sorted(edge))
    for edge in (
        (0, 1),
        (0, 2),
        (0, 4),
        (0, 6),
        (1, 2),
        (1, 3),
        (1, 5),
        (2, 3),
        (2, 5),
        (3, 4),
        (5, 6),
    )
}
MATCHING = {(0, 3), (1, 6), (2, 7), (4, 5)}


def edge(left: int, right: int) -> bool:
    return tuple(sorted((left, right))) in EDGES


def independent(block: frozenset[int]) -> bool:
    return all(not edge(left, right) for left, right in combinations(block, 2))


def partitions(items: tuple[int, ...]):
    """Generate set partitions canonically as tuples of frozensets."""

    if not items:
        yield ()
        return
    first, *rest = items
    for partition in partitions(tuple(rest)):
        yield (frozenset((first,)),) + partition
        for index in range(len(partition)):
            yield (
                partition[:index]
                + (partition[index] | frozenset((first,)),)
                + partition[index + 1 :]
            )


def verify_tree_decomposition() -> None:
    # Add two nonadjacent universal vertices 8,9 to every bag.
    base_bags = (
        frozenset((0, 1, 2, 5)),
        frozenset((0, 1, 2, 3)),
        frozenset((0, 3, 4)),
        frozenset((0, 5, 6)),
        frozenset((7,)),
    )
    bags = tuple(bag | frozenset((8, 9)) for bag in base_bags)
    tree_edges = ((0, 1), (1, 2), (0, 3), (0, 4))
    assert max(map(len, bags)) == 6

    join_edges = set(EDGES)
    for apex in (8, 9):
        join_edges.update(tuple(sorted((apex, vertex))) for vertex in VERTICES)
    assert all(any({left, right} <= bag for bag in bags) for left, right in join_edges)

    tree_adj = [set() for _ in bags]
    for left, right in tree_edges:
        tree_adj[left].add(right)
        tree_adj[right].add(left)
    for vertex in range(10):
        containing = {index for index, bag in enumerate(bags) if vertex in bag}
        reached = set()
        if containing:
            stack = [next(iter(containing))]
            while stack:
                current = stack.pop()
                if current in reached:
                    continue
                reached.add(current)
                stack.extend(tree_adj[current] & containing)
        assert reached == containing


def main() -> None:
    assert all(independent(frozenset(pair)) for pair in MATCHING)
    assert set().union(*(set(pair) for pair in MATCHING)) == set(VERTICES)
    assert (2, 7) in MATCHING
    assert (4, 5) in MATCHING

    for defect in (A, B):
        left, right = sorted(defect)
        left_misses = {root for root in R if not edge(left, root)}
        right_misses = {root for root in R if not edge(right, root)}
        assert left_misses
        assert right_misses
        assert left_misses.isdisjoint(right_misses)

    assert independent(frozenset((0, 3, 5, 7)))
    verify_tree_decomposition()

    legal = []
    for partition in partitions(VERTICES):
        if len(partition) <= 6 and all(independent(block) for block in partition):
            legal.append(partition)

    independent_sets = [
        frozenset(mask_vertices)
        for size in range(1, 9)
        for mask_vertices in combinations(VERTICES, size)
        if independent(frozenset(mask_vertices))
    ]
    for target in independent_sets:
        parities = {
            len(partition) % 2
            for partition in legal
            if target in partition
        }
        assert parities == {0, 1}

    pi_zero = (
        frozenset((0, 1)),
        frozenset((2, 7)),
        frozenset((3,)),
        frozenset((4,)),
        frozenset((5,)),
        frozenset((6,)),
    )
    assert all(
        independent(block) or block == frozenset((0, 1))
        for block in pi_zero
    )
    assert edge(0, 1)

    print("aligned perfect matching verified")
    print("endpoint-contact rigidity verified")
    print("width-five join decomposition verified")
    print(f"legal boundary partitions: {len(legal)}")
    print(f"nonempty independent sets: {len(independent_sets)}")
    print("every exact-trace cylinder has both block-count parities")


if __name__ == "__main__":
    main()
