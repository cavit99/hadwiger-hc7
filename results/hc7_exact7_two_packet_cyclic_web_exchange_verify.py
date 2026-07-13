#!/usr/bin/env python3
"""Finite core check for the two-packet cyclic-web exchange.

The proof note gives literal carrier paths.  This independent finite check
enumerates every connected carrier in two unsubdivided alternating six-cycles.
It verifies:

* one cross-edge p_i q_j permits three disjoint duty carriers iff i != j;
* adding any subset of the six homologous rungs p_i q_i never permits three
  disjoint duty carriers.

The script checks only the sharp twelve-vertex linkage core.  Exact-state
contraction and colour gluing are proved in the companion note.
"""

from __future__ import annotations

from itertools import combinations


VERTICES = tuple(range(12))
P = tuple(range(6))
Q = tuple(range(6, 12))
DUTIES = (
    frozenset({0, 3}),
    frozenset({1, 4}),
    frozenset({2, 5}),
)


def cycle_edges(offset: int) -> set[tuple[int, int]]:
    return {
        tuple(sorted((offset + i, offset + (i + 1) % 6)))
        for i in range(6)
    }


BASE = cycle_edges(0) | cycle_edges(6)


def connected(mask: int, edges: set[tuple[int, int]]) -> bool:
    first = (mask & -mask).bit_length() - 1
    seen = 1 << first
    frontier = [first]
    while frontier:
        x = frontier.pop()
        for a, b in edges:
            y = b if a == x else a if b == x else -1
            if y >= 0 and mask & (1 << y) and not seen & (1 << y):
                seen |= 1 << y
                frontier.append(y)
    return seen == mask


def funds(mask: int, duty: frozenset[int]) -> bool:
    """Each literal label i may be met at p_i or q_i."""

    return all(mask & ((1 << i) | (1 << (i + 6))) for i in duty)


def carrier_lists(edges: set[tuple[int, int]]) -> list[list[int]]:
    answer = [[] for _ in DUTIES]
    for mask in range(1, 1 << len(VERTICES)):
        if not connected(mask, edges):
            continue
        for index, duty in enumerate(DUTIES):
            if funds(mask, duty):
                answer[index].append(mask)
    return answer


def has_three_disjoint_carriers(edges: set[tuple[int, int]]) -> bool:
    carriers = carrier_lists(edges)
    for left in carriers[0]:
        for middle in carriers[1]:
            if left & middle:
                continue
            for right in carriers[2]:
                if not right & (left | middle):
                    return True
    return False


def adjacent(left: int, right: int, edges: set[tuple[int, int]]) -> bool:
    return any(
        left & (1 << a) and right & (1 << b)
        or left & (1 << b) and right & (1 << a)
        for a, b in edges
    )


def has_pattern(
    edges: set[tuple[int, int]],
    required_pairs: frozenset[tuple[int, int]],
) -> bool:
    carriers = carrier_lists(edges)
    for left in carriers[0]:
        for middle in carriers[1]:
            if left & middle:
                continue
            for right in carriers[2]:
                if right & (left | middle):
                    continue
                chosen = (left, middle, right)
                present = frozenset(
                    (i, j)
                    for i, j in combinations(range(3), 2)
                    if adjacent(chosen[i], chosen[j], edges)
                )
                if required_pairs <= present:
                    return True
    return False


def verify_one_cross_edge() -> None:
    for i in range(6):
        for j in range(6):
            edges = BASE | {tuple(sorted((i, j + 6)))}
            assert has_three_disjoint_carriers(edges) == (i != j), (i, j)

    # These are the two geometric representative adjacencies in the five
    # normalized rows of the proof table.  The unique omitted pair is funded
    # by the named literal boundary edge.
    expected = {
        1: frozenset({(0, 2), (1, 2)}),
        2: frozenset({(0, 1), (0, 2)}),
        3: frozenset({(0, 1), (0, 2)}),
        4: frozenset({(0, 1), (0, 2)}),
        5: frozenset({(0, 1), (1, 2)}),
    }
    for offset, pattern in expected.items():
        edges = BASE | {(0, offset + 6)}
        assert has_pattern(edges, pattern), (offset, pattern)


def verify_homologous_cylinder() -> None:
    homologous = tuple((i, i + 6) for i in range(6))
    for size in range(7):
        for chosen in combinations(homologous, size):
            edges = BASE | {tuple(sorted(edge)) for edge in chosen}
            assert not has_three_disjoint_carriers(edges), chosen


if __name__ == "__main__":
    verify_one_cross_edge()
    verify_homologous_cylinder()
    print("CERTIFIED transverse carrier core and homologous-cylinder barrier")
