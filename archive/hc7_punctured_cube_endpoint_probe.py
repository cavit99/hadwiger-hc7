#!/usr/bin/env python3
"""Classify the endpoint obstruction in the punctured-cube 5-colour branch.

The six vertices are partitioned into three deleted matching pairs.  A
cross-edge forbids the independent transversal assignments containing both
of its ends.  We enumerate the inclusion-minimal cross-edge sets meeting
all eight transversals, quotient by pair permutations and pair flips, and
record clique/minor data after restoring the three matching edges.

This is a finite discovery aid.  The intended reusable language is a
minimal unsatisfiable two-CNF, not a new labelled HC7 case census.
"""

from __future__ import annotations

import itertools


VERTICES = tuple(range(6))
PAIRS = ((0, 1), (2, 3), (4, 5))
CROSS_EDGES = tuple(
    (u, v)
    for left, right in itertools.combinations(PAIRS, 2)
    for u in left
    for v in right
)
MATCHING = frozenset(tuple(sorted(edge)) for edge in PAIRS)
TRANSVERSALS = tuple(itertools.product(*PAIRS))


def edge_set(mask: int) -> frozenset[tuple[int, int]]:
    return frozenset(
        edge for index, edge in enumerate(CROSS_EDGES) if mask >> index & 1
    )


def covers(edges: frozenset[tuple[int, int]]) -> bool:
    return all(
        any(tuple(sorted(edge)) in edges for edge in itertools.combinations(t, 2))
        for t in TRANSVERSALS
    )


def minimal_masks() -> tuple[int, ...]:
    answer = []
    for mask in range(1 << len(CROSS_EDGES)):
        edges = edge_set(mask)
        if not covers(edges):
            continue
        if any(covers(edges - {edge}) for edge in edges):
            continue
        answer.append(mask)
    return tuple(answer)


def symmetries():
    for pair_order in itertools.permutations(range(3)):
        for flips in itertools.product((0, 1), repeat=3):
            image = [None] * 6
            for old_pair, new_pair in enumerate(pair_order):
                for side in range(2):
                    image[2 * old_pair + side] = 2 * new_pair + (side ^ flips[old_pair])
            yield tuple(image)


SYMMETRIES = tuple(symmetries())


def transform(mask: int, image: tuple[int, ...]) -> int:
    result = 0
    index = {edge: i for i, edge in enumerate(CROSS_EDGES)}
    for edge in edge_set(mask):
        mapped = tuple(sorted((image[edge[0]], image[edge[1]])))
        result |= 1 << index[mapped]
    return result


def connected(vertices: frozenset[int], edges) -> bool:
    if not vertices:
        return False
    reached = {next(iter(vertices))}
    while True:
        old = len(reached)
        reached |= {
            v
            for u in tuple(reached)
            for v in vertices
            if tuple(sorted((u, v))) in edges
        }
        if len(reached) == old:
            return len(reached) == len(vertices)


def partitions(items: tuple[int, ...], count: int):
    blocks: list[list[int]] = []

    def visit(position: int):
        if position == len(items):
            if len(blocks) == count:
                yield tuple(frozenset(block) for block in blocks)
            return
        item = items[position]
        for block in blocks:
            block.append(item)
            yield from visit(position + 1)
            block.pop()
        if len(blocks) < count:
            blocks.append([item])
            yield from visit(position + 1)
            blocks.pop()

    yield from visit(0)


def has_clique_minor(edges, order: int) -> bool:
    for support_size in range(order, len(VERTICES) + 1):
        for support in itertools.combinations(VERTICES, support_size):
            for bags in partitions(support, order):
                if not all(connected(bag, edges) for bag in bags):
                    continue
                if all(
                    any(
                        tuple(sorted((u, v))) in edges
                        for u in left
                        for v in right
                    )
                    for left, right in itertools.combinations(bags, 2)
                ):
                    return True
    return False


def main() -> None:
    minima = minimal_masks()
    representatives = {}
    for mask in minima:
        canonical = min(transform(mask, image) for image in SYMMETRIES)
        representatives[canonical] = representatives.get(canonical, 0) + 1

    print("minimal_masks", len(minima))
    print("minimal_orbits", len(representatives))
    for index, (mask, weight) in enumerate(sorted(representatives.items())):
        cross = edge_set(mask)
        restored = cross | MATCHING
        triangles = tuple(
            t
            for t in TRANSVERSALS
            if all(tuple(sorted(edge)) in cross for edge in itertools.combinations(t, 2))
        )
        print(
            "ORBIT",
            index,
            "weight",
            weight,
            "cross_edges",
            tuple(sorted(cross)),
            "transversal_triangles",
            triangles,
            "K4_minor",
            has_clique_minor(restored, 4),
            "K5_minor",
            has_clique_minor(restored, 5),
        )


if __name__ == "__main__":
    main()
