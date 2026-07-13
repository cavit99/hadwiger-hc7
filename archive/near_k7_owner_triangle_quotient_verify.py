#!/usr/bin/env python3
"""Exact 3-by-4 owner-triangle quotient check.

Boundary vertices 0,1,2,3 induce K4 minus 01.  Vertices 4,5,6 form
a triangle.  Vertices 7,8,9 represent three pairwise anticomplete full
components and are complete to the seven boundary vertices.  The twelve
triangle-to-owner contacts are enumerated.  Every contact matrix with at
least five entries has a K7 minor.
"""

from __future__ import annotations

import itertools


VERTICES = tuple(range(10))


def set_partitions(values: tuple[int, ...], blocks: int):
    current = [[values[0]]]

    def recurse(index: int):
        if index == len(values):
            if len(current) == blocks:
                yield tuple(sum(1 << x for x in block) for block in current)
            return
        vertex = values[index]
        for block in current:
            block.append(vertex)
            yield from recurse(index + 1)
            block.pop()
        if len(current) < blocks:
            current.append([vertex])
            yield from recurse(index + 1)
            current.pop()

    yield from recurse(1)


PARTITIONS = tuple(
    partition
    for support_order in range(7, 11)
    for support in itertools.combinations(VERTICES, support_order)
    for partition in set_partitions(support, 7)
)


BASE_EDGES: set[tuple[int, int]] = set()
for first, second in itertools.combinations(range(4), 2):
    if (first, second) != (0, 1):
        BASE_EDGES.add((first, second))
for first, second in itertools.combinations(range(4, 7), 2):
    BASE_EDGES.add((first, second))
for helper in range(7, 10):
    for boundary in range(7):
        BASE_EDGES.add((boundary, helper))


def quotient_adjacency(contact_mask: int) -> list[int]:
    adjacency = [0] * 10
    edges = set(BASE_EDGES)
    bit = 0
    for triangle in range(4, 7):
        for owner in range(4):
            if contact_mask & (1 << bit):
                edges.add((owner, triangle))
            bit += 1
    for first, second in edges:
        adjacency[first] |= 1 << second
        adjacency[second] |= 1 << first
    return adjacency


def k7_model(contact_mask: int) -> tuple[int, ...] | None:
    adjacency = quotient_adjacency(contact_mask)
    connected_cache: dict[int, bool] = {}
    neighbour_cache: dict[int, int] = {}

    def connected(mask: int) -> bool:
        if mask not in connected_cache:
            reached = mask & -mask
            while True:
                expanded = reached
                bits = reached
                while bits:
                    vertex = bits & -bits
                    bits ^= vertex
                    expanded |= adjacency[vertex.bit_length() - 1] & mask
                if expanded == reached:
                    break
                reached = expanded
            connected_cache[mask] = reached == mask
        return connected_cache[mask]

    def neighbours(mask: int) -> int:
        if mask not in neighbour_cache:
            result = 0
            bits = mask
            while bits:
                vertex = bits & -bits
                bits ^= vertex
                result |= adjacency[vertex.bit_length() - 1]
            neighbour_cache[mask] = result
        return neighbour_cache[mask]

    for bags in PARTITIONS:
        if not all(connected(bag) for bag in bags):
            continue
        if all(
            neighbours(bags[first]) & bags[second]
            for first in range(7)
            for second in range(first + 1, 7)
        ):
            return bags
    return None


def main() -> None:
    negative = []
    certificates = 0
    for contact_mask in range(1 << 12):
        model = k7_model(contact_mask)
        if contact_mask.bit_count() >= 5:
            assert model is not None
            certificates += 1
        if model is None:
            negative.append(contact_mask)

    maximal_negative = [
        mask
        for mask in negative
        if not any(mask != other and mask | other == other for other in negative)
    ]
    assert len(negative) == 226
    assert len(maximal_negative) == 60
    assert max(mask.bit_count() for mask in maximal_negative) == 4

    owner_permutations = []
    for swap_deficient in (False, True):
        for swap_neutral in (False, True):
            permutation = list(range(4))
            if swap_deficient:
                permutation[0], permutation[1] = 1, 0
            if swap_neutral:
                permutation[2], permutation[3] = 3, 2
            owner_permutations.append(permutation)

    def relabel(mask: int, owner_permutation, triangle_permutation) -> int:
        result = 0
        for triangle in range(3):
            for owner in range(4):
                if mask & (1 << (4 * triangle + owner)):
                    result |= 1 << (
                        4 * triangle_permutation[triangle]
                        + owner_permutation[owner]
                    )
        return result

    maximal_set = set(maximal_negative)
    unseen = set(maximal_negative)
    orbit_representatives = []
    while unseen:
        seed = min(unseen)
        orbit = {
            relabel(seed, owner_permutation, triangle_permutation)
            for owner_permutation in owner_permutations
            for triangle_permutation in itertools.permutations(range(3))
        } & maximal_set
        unseen -= orbit
        orbit_representatives.append(min(orbit))

    representative_rows = [
        tuple(
            tuple(
                owner
                for owner in range(4)
                if mask & (1 << (4 * triangle + owner))
            )
            for triangle in range(3)
        )
        for mask in orbit_representatives
    ]
    expected = {
        ((2, 3), (2,), ()),
        ((1, 2), (0, 2), ()),
        ((0, 2), (1,), (0,)),
        ((3,), (2,), (0,)),
    }
    assert set(representative_rows) == expected
    print(
        {
            "partitions_checked_per_matrix": len(PARTITIONS),
            "five_or_more_contact_matrices_certified": certificates,
            "negative_matrices": len(negative),
            "maximal_negative_matrices": len(maximal_negative),
            "maximum_negative_contacts": 4,
            "maximal_negative_orbits": representative_rows,
        }
    )


if __name__ == "__main__":
    main()
