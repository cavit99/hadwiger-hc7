#!/usr/bin/env python3
"""Exact local probe for the two-unused-colour XOR interface lock.

This graph is not asserted to be contraction-critical.  It tests whether
the atomic inequalities, seven-connectivity, almost-full portal rows, and
the four-anchor conclusion alone exclude the XOR relation.
"""

from __future__ import annotations

from itertools import combinations


S = tuple(range(7))
X1, Z, X2, Y1, Y2 = range(7, 12)
HELPERS = tuple(range(12, 17))
V = tuple(range(17))


def graph_edges() -> set[tuple[int, int]]:
    edges = {
        tuple(sorted(edge))
        for edge in {
            (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
            (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
        }
    }
    for helper in HELPERS:
        edges.update((min(helper, s), max(helper, s)) for s in S)
    edges.update((HELPERS[0], HELPERS[i]) for i in range(1, len(HELPERS)))
    for vertex in (X1, Z, X2):
        edges.update((min(vertex, s), max(vertex, s)) for s in S if s != 1)
    for vertex in (Y1, Y2):
        edges.update((min(vertex, s), max(vertex, s)) for s in S if s != 2)
    edges.update(tuple(sorted(edge)) for edge in {
        (X1, Z), (Z, X2), (Y1, Y2), (X1, Y1), (X2, Y2),
    })
    return edges


EDGES = graph_edges()
ADJ = [0] * len(V)
for first, second in EDGES:
    ADJ[first] |= 1 << second
    ADJ[second] |= 1 << first


def connected_after(deleted: set[int]) -> bool:
    remaining = ((1 << len(V)) - 1) & ~sum(1 << x for x in deleted)
    if not remaining:
        return True
    reached = remaining & -remaining
    while True:
        expanded = reached
        bits = reached
        while bits:
            bit = bits & -bits
            bits ^= bit
            expanded |= ADJ[bit.bit_length() - 1] & remaining
        if expanded == reached:
            return reached == remaining
        reached = expanded


def verify_connectivity() -> None:
    for size in range(7):
        assert all(connected_after(set(cut)) for cut in combinations(V, size))
    assert not connected_after(set(S))


def verify_minimum_fragment() -> None:
    # D itself is a five-vertex fragment behind S.  No connected set of
    # order below five has an external neighbourhood of order seven.
    for size in range(1, 5):
        for subset in combinations(V, size):
            mask = sum(1 << x for x in subset)
            reached = mask & -mask
            while True:
                expanded = reached
                bits = reached
                while bits:
                    bit = bits & -bits
                    bits ^= bit
                    expanded |= ADJ[bit.bit_length() - 1] & mask
                if expanded == reached:
                    break
                reached = expanded
            if reached != mask:
                continue
            neighbourhood = 0
            for x in subset:
                neighbourhood |= ADJ[x]
            neighbourhood &= ~mask
            assert neighbourhood.bit_count() != 7


def proper(colour: dict[int, int], omitted: tuple[int, int] | None = None) -> bool:
    for edge in EDGES:
        if omitted is not None and edge == tuple(sorted(omitted)):
            continue
        first, second = edge
        if colour[first] == colour[second]:
            return False
    return True


def verify_xor_and_anchors() -> None:
    # Boundary state 13|05|24|6 uses colours 0,1,2,3; 4,5 are unused.
    boundary = {1: 0, 3: 0, 0: 1, 5: 1, 2: 2, 4: 2, 6: 3}

    # X is the diagonal relation and Y the off-diagonal relation on {4,5}.
    for deleted, values in (
        ((X1, Y1), (4, 5, 4, 4, 5)),
        ((X2, Y2), (4, 5, 4, 5, 4)),
    ):
        colour = dict(boundary)
        colour.update({X1: values[0], Z: values[1], X2: values[2],
                       Y1: values[3], Y2: values[4]})
        colour[HELPERS[0]] = 4
        for helper in HELPERS[1:]:
            colour[helper] = 5
        # The opposite helper shore is irrelevant to the local side.
        local_edges = {e for e in EDGES if not (set(e) & set(HELPERS))}
        for first, second in local_edges:
            if (first, second) == tuple(sorted(deleted)):
                continue
            assert colour[first] != colour[second]

        alpha = colour[deleted[0]]
        assert alpha == colour[deleted[1]]
        other_interface = (X2, Y2) if deleted == (X1, Y1) else (X1, Y1)
        assert colour[other_interface[0]] != colour[other_interface[1]]

        # For each of the four boundary colours, the alpha/gamma components
        # at the two ends are distinct and anchored directly at the boundary.
        for gamma in range(4):
            allowed = {alpha, gamma}
            shore = {X1, Z, X2, Y1, Y2}
            kept = {x for x in shore if colour[x] in allowed}
            adjacency = {x: set() for x in kept}
            for first, second in local_edges:
                if (first, second) == tuple(sorted(deleted)):
                    continue
                if first in kept and second in kept:
                    adjacency[first].add(second)
                    adjacency[second].add(first)

            def component(start: int) -> set[int]:
                seen = {start}
                stack = [start]
                while stack:
                    x = stack.pop()
                    for y in adjacency[x] - seen:
                        seen.add(y)
                        stack.append(y)
                return seen

            left = component(deleted[0])
            right = component(deleted[1])
            assert left.isdisjoint(right)
            for part in (left, right):
                assert any(
                    colour[s] in allowed and tuple(sorted((x, s))) in EDGES
                    for x in part for s in S
                )


def verify_k7_certificate() -> list[list[int]]:
    bags = [
        [0, 15], [1, 10], [2, 4, 12], [3], [5, 16],
        [6, 7, 8, 9, 11, 14], [13],
    ]
    used: set[int] = set()
    for bag in bags:
        assert not (used & set(bag))
        used.update(bag)
        mask = sum(1 << x for x in bag)
        reached = mask & -mask
        while True:
            expanded = reached
            bits = reached
            while bits:
                bit = bits & -bits
                bits ^= bit
                expanded |= ADJ[bit.bit_length() - 1] & mask
            if expanded == reached:
                break
            reached = expanded
        assert reached == mask
    assert all(
        any(tuple(sorted((x, y))) in EDGES for x in bags[i] for y in bags[j])
        for i in range(7) for j in range(i)
    )
    return bags


def main() -> None:
    verify_connectivity()
    verify_minimum_fragment()
    verify_xor_and_anchors()
    print("verified seven-connectivity, minimum-fragment order, and the saturated local XOR lock")
    print("explicit_K7_model", verify_k7_certificate())


if __name__ == "__main__":
    main()
