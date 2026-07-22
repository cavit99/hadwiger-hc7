#!/usr/bin/env python3
"""Verify the independent two-defect four-bag barrier."""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations, permutations


BOUNDARY_ORDER = 8
TARGET_ORDER = 7
BOUNDARY = tuple(range(BOUNDARY_ORDER))
U, E0, E1, F0, F1 = range(8, 13)
MISSED = (
    frozenset({3, 7}),
    frozenset({0, 5}),
    frozenset({1, 7}),
    frozenset({1, 6}),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def add_edge(adjacency: list[int], left: int, right: int) -> None:
    adjacency[left] |= 1 << right
    adjacency[right] |= 1 << left


def edge(adjacency: tuple[int, ...], left: int, right: int) -> bool:
    return bool((adjacency[left] >> right) & 1)


def boundary_graph() -> tuple[int, ...]:
    adjacency = [0] * BOUNDARY_ORDER
    for component in ((0, 3, 6), (1, 4, 7)):
        for left, right in combinations(component, 2):
            add_edge(adjacency, left, right)
    add_edge(adjacency, 2, 5)
    return tuple(adjacency)


def graph6_code(adjacency: tuple[int, ...]) -> str:
    bits = [
        (adjacency[left] >> right) & 1
        for right in range(1, len(adjacency))
        for left in range(right)
    ]
    while len(bits) % 6:
        bits.append(0)
    values = [len(adjacency)]
    for start in range(0, len(bits), 6):
        value = 0
        for bit in bits[start : start + 6]:
            value = (value << 1) | bit
        values.append(value)
    return "".join(chr(value + 63) for value in values)


def build_host() -> tuple[int, ...]:
    boundary = boundary_graph()
    adjacency = [0] * 13
    for left, right in combinations(BOUNDARY, 2):
        if edge(boundary, left, right):
            add_edge(adjacency, left, right)
    for vertex in BOUNDARY:
        add_edge(adjacency, U, vertex)
    for bag, missed in zip((E0, E1, F0, F1), MISSED, strict=True):
        for vertex in BOUNDARY:
            if vertex not in missed:
                add_edge(adjacency, bag, vertex)
    add_edge(adjacency, E0, E1)
    add_edge(adjacency, F0, F1)
    return tuple(adjacency)


def connected(adjacency: tuple[int, ...]) -> bool:
    seen = 1
    frontier = 1
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        vertex = bit.bit_length() - 1
        frontier |= adjacency[vertex] & ~seen
        seen |= frontier
    return seen == (1 << len(adjacency)) - 1


def component_masks(
    adjacency: tuple[int, ...], allowed: int | None = None
) -> tuple[int, ...]:
    if allowed is None:
        allowed = (1 << len(adjacency)) - 1
    components: list[int] = []
    unseen = allowed
    while unseen:
        seed = unseen & -unseen
        component = 0
        frontier = seed
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            vertex = bit.bit_length() - 1
            component |= bit
            frontier |= adjacency[vertex] & allowed & ~component
        components.append(component)
        unseen &= ~component
    return tuple(components)


def contract_edge(
    adjacency: tuple[int, ...], left: int, right: int
) -> tuple[int, ...]:
    """Contract ``right`` into ``left`` and relabel the remaining graph."""

    keep = tuple(vertex for vertex in range(len(adjacency)) if vertex != right)
    position = {vertex: index for index, vertex in enumerate(keep)}
    answer = [0] * len(keep)
    merged_neighbours = (adjacency[left] | adjacency[right]) & ~(
        (1 << left) | (1 << right)
    )

    for old_left, old_right in combinations(keep, 2):
        if old_left == left:
            present = bool((merged_neighbours >> old_right) & 1)
        elif old_right == left:
            present = bool((merged_neighbours >> old_left) & 1)
        else:
            present = bool((adjacency[old_left] >> old_right) & 1)
        if present:
            add_edge(answer, position[old_left], position[old_right])
    return tuple(answer)


def has_k7_minor(adjacency: tuple[int, ...]) -> tuple[bool, int]:
    """Exact contraction search for a connected host.

    A clique-minor model in a connected graph can be enlarged to cover all
    host vertices.  Above target order, one spanning branch set then contains
    an edge, whose contraction preserves the model.  It is therefore enough
    to try every edge contraction until seven vertices remain.
    """

    require(connected(adjacency), "contraction-only search needs a connected host")
    calls = 0

    @lru_cache(maxsize=None)
    def search(graph: tuple[int, ...]) -> bool:
        nonlocal calls
        calls += 1
        if len(graph) < TARGET_ORDER:
            return False
        if len(graph) == TARGET_ORDER:
            return all(
                graph[vertex].bit_count() == TARGET_ORDER - 1
                for vertex in range(TARGET_ORDER)
            )
        for left in range(len(graph)):
            for right in range(left + 1, len(graph)):
                if edge(graph, left, right) and search(
                    contract_edge(graph, left, right)
                ):
                    return True
        return False

    return search(adjacency), calls


def anchor_certificate_count(boundary: tuple[int, ...]) -> int:
    count = 0
    for first, second in combinations(BOUNDARY, 2):
        if not edge(boundary, first, second):
            continue
        available = tuple(
            vertex for vertex in BOUNDARY if vertex not in {first, second}
        )
        for anchors in permutations(available, 4):
            if any(anchors[index] in MISSED[index] for index in range(4)):
                continue
            if any(
                singleton in MISSED[index]
                and not edge(boundary, anchors[index], singleton)
                for index in range(4)
                for singleton in (first, second)
            ):
                continue
            if any(
                anchors[right] in MISSED[left]
                and anchors[left] in MISSED[right]
                and not edge(boundary, anchors[left], anchors[right])
                for left in (0, 1)
                for right in (2, 3)
            ):
                continue
            count += 1
    return count


def main() -> None:
    boundary = boundary_graph()
    host = build_host()

    require(graph6_code(boundary) == "GCOcaO", "unexpected graph6 code")
    require(
        not any(
            all(not edge(boundary, left, right) for left, right in combinations(group, 2))
            for group in combinations(BOUNDARY, 4)
        ),
        "boundary has an independent four-set",
    )
    require(
        sorted(component.bit_count() for component in component_masks(boundary))
        == [2, 3, 3],
        "unexpected boundary component orders",
    )
    for deleted in combinations(BOUNDARY, 2):
        allowed = ((1 << BOUNDARY_ORDER) - 1) & ~sum(1 << vertex for vertex in deleted)
        require(
            all(
                component.bit_count() <= 3
                for component in component_masks(boundary, allowed)
            ),
            f"two-vertex deletion {deleted} can contain a K4 minor",
        )
    require(all(len(missed) == 2 for missed in MISSED), "defect is not two")
    require(edge(host, E0, E1) and edge(host, F0, F1), "same-shore edge missing")
    require(
        all(
            edge(host, bag, vertex) == (vertex not in missed)
            for bag, missed in zip((E0, E1, F0, F1), MISSED, strict=True)
            for vertex in BOUNDARY
        ),
        "bag contacts do not match the displayed defects",
    )

    certificates = anchor_certificate_count(boundary)
    require(certificates == 0, "unexpected four-anchor certificate")

    k7 = tuple(
        ((1 << TARGET_ORDER) - 1) & ~(1 << vertex)
        for vertex in range(TARGET_ORDER)
    )
    subdivided = [0] * (TARGET_ORDER + 1)
    for left, right in combinations(range(TARGET_ORDER), 2):
        if (left, right) != (0, 1):
            add_edge(subdivided, left, right)
    add_edge(subdivided, 0, TARGET_ORDER)
    add_edge(subdivided, 1, TARGET_ORDER)
    k6 = tuple(
        ((1 << 6) - 1) & ~(1 << vertex)
        for vertex in range(6)
    )
    positive_control, _ = has_k7_minor(k7)
    subdivision_control, _ = has_k7_minor(tuple(subdivided))
    negative_control, _ = has_k7_minor(k6)
    require(positive_control, "K7 positive control failed")
    require(subdivision_control, "subdivided-K7 positive control failed")
    require(not negative_control, "K6 negative control failed")

    has_minor, states = has_k7_minor(host)
    require(not has_minor, "the displayed host has a K7 minor")

    print("boundary GCOcaO: K3 + K3 + K2; alpha=3; compact")
    print("missed_sets E0=37 E1=05 F0=17 F1=16")
    print(f"anchor_certificates {certificates}")
    print("solver_controls K7=True subdivided_K7=True K6=False")
    print(
        "host vertices=13 edges="
        f"{sum(mask.bit_count() for mask in host) // 2} "
        f"contraction_states={states} K7_minor={has_minor}"
    )
    print("PASS independent_two_defect_four_bag_barrier")


if __name__ == "__main__":
    main()
