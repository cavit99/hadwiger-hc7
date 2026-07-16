#!/usr/bin/env python3
"""Verify the six-terminal crossing decoder in the exceptional 3+1 quotient.

The positive cases are checked from explicit branch-set certificates.  The
three negative cases are checked by an exact, dependency-free K7-minor
search on the twelve-vertex quotient.
"""

from __future__ import annotations

import functools
import itertools


A0, A1, A2, A3, X, Y = range(6)
B0, B1, B2, R, P, Q = range(6, 12)

BASE_EDGES = {
    *map(tuple, itertools.combinations((A0, A1, A2, A3), 2)),
    (X, Y),
    (X, A0),
    (X, A1),
    (X, A2),
    (Y, A3),
    *(
        edge
        for edge in itertools.combinations((B0, B1, B2, R, P, Q), 2)
        if edge != (P, Q)
    ),
    (A0, B0),
    (A1, B1),
    (A2, B2),
    (A3, P),
    (X, Q),
    (Y, R),
}

ORDER = (A3, Y, X, Q, R, P)

# The entries are the two crossing chords followed by seven branch sets.
# Vertex names are expanded in the accompanying note.
CERTIFICATES: dict[
    tuple[tuple[int, int], tuple[int, int]], tuple[tuple[int, ...], ...]
] = {
    ((A3, Q), (Y, R)): (
        (B0,), (B1,), (B2,), (R,), (Q,), (A3, P), (A0, A1, A2, X, Y)
    ),
    ((A3, Q), (Y, P)): (
        (B0,), (B1,), (B2,), (R,), (P,), (A3, Q), (A0, A1, A2, X, Y)
    ),
    ((A3, R), (Y, P)): (
        (B0,), (B1,), (B2,), (R,), (P,), (X, Y, Q), (A0, A1, A2, A3)
    ),
    ((A3, Q), (X, R)): (
        (B0,), (B1,), (B2,), (R,), (Q,), (A3, Y, P), (A0, A1, A2, X)
    ),
    ((A3, Q), (X, P)): (
        (B0,), (B1,), (B2,), (R,), (P,), (X, Q), (A0, A1, A2, A3, Y)
    ),
    ((A3, R), (X, P)): (
        (B0,), (B1,), (B2,), (R,), (P,), (X, Y, Q), (A0, A1, A2, A3)
    ),
    ((A3, R), (Q, P)): (
        (B0,), (B1,), (B2,), (R,), (P,), (Q,), (A0, A1, A2, A3, X, Y)
    ),
    ((Y, Q), (X, R)): (
        (B0,), (B1,), (B2,), (R,), (Q,), (A3, Y, P), (A0, A1, A2, X)
    ),
    ((Y, Q), (X, P)): (
        (B0,), (B1,), (B2,), (R,), (P,), (X, Q), (A0, A1, A2, A3, Y)
    ),
    ((Y, R), (X, P)): (
        (B0,), (B1,), (B2,), (R,), (P,), (X, Q), (A0, A1, A2, A3, Y)
    ),
    ((Y, R), (Q, P)): (
        (B0,), (B1,), (B2,), (R,), (P,), (Q,), (A0, A1, A2, A3, X, Y)
    ),
    ((X, R), (Q, P)): (
        (B0,), (B1,), (B2,), (R,), (P,), (Q,), (A0, A1, A2, A3, X, Y)
    ),
}

EXPECTED_NEGATIVE = {
    ((A3, X), (Y, Q)),
    ((A3, X), (Y, R)),
    ((A3, X), (Y, P)),
}


def crossing_types() -> tuple[tuple[tuple[int, int], tuple[int, int]], ...]:
    answer = []
    for i, j, k, ell in itertools.combinations(range(6), 4):
        answer.append(((ORDER[i], ORDER[k]), (ORDER[j], ORDER[ell])))
    return tuple(answer)


def adjacency(order: int, edges: frozenset[tuple[int, int]] | set[tuple[int, int]]) -> list[int]:
    answer = [0] * order
    for left, right in edges:
        answer[left] |= 1 << right
        answer[right] |= 1 << left
    return answer


def connected(mask: int, adj: list[int]) -> bool:
    reached = mask & -mask
    while True:
        old = reached
        frontier = reached
        neighbours = 0
        while frontier:
            bit = frontier & -frontier
            frontier -= bit
            neighbours |= adj[bit.bit_length() - 1]
        reached |= neighbours & mask
        if reached == old:
            return reached == mask


def touches(left: int, right: int, adj: list[int]) -> bool:
    while left:
        bit = left & -left
        left -= bit
        if adj[bit.bit_length() - 1] & right:
            return True
    return False


def verify_certificate(
    crossing: tuple[tuple[int, int], tuple[int, int]],
    bags: tuple[tuple[int, ...], ...],
) -> None:
    edges = BASE_EDGES | set(crossing)
    adj = adjacency(12, edges)
    masks = tuple(sum(1 << vertex for vertex in bag) for bag in bags)
    assert len(masks) == 7
    assert all(masks)
    assert all(not (left & right) for left, right in itertools.combinations(masks, 2))
    assert all(connected(mask, adj) for mask in masks)
    assert all(
        touches(left, right, adj)
        for left, right in itertools.combinations(masks, 2)
    )


def has_k7_minor_at_most_twelve(
    order: int, edges: frozenset[tuple[int, int]]
) -> bool:
    """Exact branch-set search on a graph of order at most twelve.

    Every seven-branch model on ``order`` vertices has at least
    ``14-order`` singleton branch sets.  The search fixes the exact
    singleton clique and enumerates all remaining connected branch sets.
    """

    assert order <= 12
    vertices = tuple(range(order))
    adj = adjacency(order, edges)
    full = (1 << order) - 1

    @functools.lru_cache(maxsize=None)
    def is_connected(mask: int) -> bool:
        return connected(mask, adj)

    @functools.lru_cache(maxsize=None)
    def are_adjacent(left: int, right: int) -> bool:
        return touches(left, right, adj)

    minimum_singletons = max(0, 14 - order)
    for singleton_count in range(7, minimum_singletons - 1, -1):
        non_singleton_count = 7 - singleton_count
        for singletons in itertools.combinations(vertices, singleton_count):
            if any(
                not (adj[left] >> right & 1)
                for left, right in itertools.combinations(singletons, 2)
            ):
                continue

            singleton_mask = sum(1 << vertex for vertex in singletons)
            remainder = full ^ singleton_mask
            if non_singleton_count == 0:
                return True

            maximum_size = remainder.bit_count() - 2 * (non_singleton_count - 1)
            candidates = []
            subset = remainder
            while subset:
                if (
                    2 <= subset.bit_count() <= maximum_size
                    and is_connected(subset)
                    and all(
                        are_adjacent(subset, 1 << vertex)
                        for vertex in singletons
                    )
                ):
                    candidates.append(subset)
                subset = (subset - 1) & remainder

            def search(start: int, chosen: tuple[int, ...], used: int) -> bool:
                if len(chosen) == non_singleton_count:
                    return True
                missing = non_singleton_count - len(chosen)
                if (remainder & ~used).bit_count() < 2 * missing:
                    return False
                for position in range(start, len(candidates)):
                    candidate = candidates[position]
                    if candidate & used:
                        continue
                    if all(are_adjacent(candidate, old) for old in chosen) and search(
                        position + 1, chosen + (candidate,), used | candidate
                    ):
                        return True
                return False

            if search(0, (), 0):
                return True
    return False


def normalize_graph(
    vertices: tuple[int, ...], edges: frozenset[tuple[int, int]]
) -> tuple[int, frozenset[tuple[int, int]]]:
    relabel = {vertex: index for index, vertex in enumerate(vertices)}
    normalized = frozenset(
        tuple(sorted((relabel[left], relabel[right])))
        for left, right in edges
        if left in relabel and right in relabel and left != right
    )
    return len(vertices), normalized


def delete_vertex(
    order: int, edges: frozenset[tuple[int, int]], vertex: int
) -> tuple[int, frozenset[tuple[int, int]]]:
    return normalize_graph(
        tuple(old for old in range(order) if old != vertex), edges
    )


def contract_edge(
    order: int,
    edges: frozenset[tuple[int, int]],
    left: int,
    right: int,
) -> tuple[int, frozenset[tuple[int, int]]]:
    merged = frozenset(
        tuple(sorted((left if u == right else u, left if v == right else v)))
        for u, v in edges
        if (left if u == right else u) != (left if v == right else v)
    )
    return normalize_graph(
        tuple(old for old in range(order) if old != right), merged
    )


@functools.lru_cache(maxsize=None)
def has_k7_minor(order: int, edges: frozenset[tuple[int, int]]) -> bool:
    """Exact detector, using deletion/contraction at degree below six."""

    if order <= 12:
        return has_k7_minor_at_most_twelve(order, edges)

    adj = adjacency(order, edges)
    vertex = min(range(order), key=lambda old: adj[old].bit_count())
    assert adj[vertex].bit_count() < 6

    if has_k7_minor(*delete_vertex(order, edges, vertex)):
        return True
    neighbours = tuple(
        old for old in range(order) if adj[vertex] >> old & 1
    )
    return any(
        has_k7_minor(*contract_edge(order, edges, vertex, neighbour))
        for neighbour in neighbours
    )


def main() -> None:
    crossings = set(crossing_types())
    assert len(crossings) == 15
    assert set(CERTIFICATES) | EXPECTED_NEGATIVE == crossings
    assert not (set(CERTIFICATES) & EXPECTED_NEGATIVE)

    for crossing, bags in CERTIFICATES.items():
        verify_certificate(crossing, bags)
        assert has_k7_minor(12, frozenset(BASE_EDGES | set(crossing)))

    for crossing in EXPECTED_NEGATIVE:
        assert not has_k7_minor(12, frozenset(BASE_EDGES | set(crossing)))
        first, second = crossing
        subdivided = frozenset(
            BASE_EDGES
            | {
                (first[0], 12),
                (12, first[1]),
                (second[0], 13),
                (13, second[1]),
            }
        )
        assert not has_k7_minor(14, subdivided)

    print("crossing_types", len(crossings))
    print("explicit_k7_certificates", len(CERTIFICATES))
    print("exact_negative_types", sorted(EXPECTED_NEGATIVE))
    print("subdivided_negative_types", len(EXPECTED_NEGATIVE))
    print("GREEN: six-terminal crossing decoder verified")


if __name__ == "__main__":
    main()
