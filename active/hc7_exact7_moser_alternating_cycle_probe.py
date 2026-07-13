#!/usr/bin/env python3
"""Probe the literal alternating-cycle residue in the normalized Moser state.

The host consists of the seven literal Moser vertices and a six-cycle with
one private portal for each member of duties {2,3}, {1,4}, {0,5}.  For each
of the eight within-duty orientations, search exhaustively for five pairwise
adjacent disjoint connected branch sets, each meeting the literal boundary,
after reserving one boundary vertex as the anchor of a second full packet.
Such a rooted K5 plus the two full packets lifts literally to K7.
"""

from __future__ import annotations

from itertools import product


S_MASK = (1 << 7) - 1
MOSER_EDGES = (
    (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
    (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
)
DUTIES = ((2, 3), (1, 4), (0, 5))


def host(order: tuple[int, ...]) -> list[int]:
    adjacency = [0] * 13

    def edge(x: int, y: int) -> None:
        adjacency[x] |= 1 << y
        adjacency[y] |= 1 << x

    for x, y in MOSER_EDGES:
        edge(x, y)
    for index in range(6):
        edge(7 + index, 7 + (index + 1) % 6)
        edge(order[index], 7 + index)
    return adjacency


def connected_masks(adjacency: list[int], forbidden: int) -> list[int]:
    answer = []
    for mask in range(1, 1 << len(adjacency)):
        if mask & forbidden or not mask & S_MASK:
            continue
        seed = mask & -mask
        reached = seed
        while True:
            expanded = reached
            work = reached
            while work:
                bit = work & -work
                work -= bit
                expanded |= adjacency[bit.bit_length() - 1] & mask
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            answer.append(mask)
    return answer


def neighbourhood(adjacency: list[int], mask: int) -> int:
    answer = 0
    work = mask
    while work:
        bit = work & -work
        work -= bit
        answer |= adjacency[bit.bit_length() - 1]
    return answer


def rooted_k5(adjacency: list[int], anchor: int) -> tuple[int, ...] | None:
    candidates = connected_masks(adjacency, 1 << anchor)
    neighbours = {mask: neighbourhood(adjacency, mask) for mask in candidates}

    def search(chosen: tuple[int, ...], used: int, start: int):
        if len(chosen) == 5:
            return chosen
        if 13 - used.bit_count() < 5 - len(chosen):
            return None
        for index in range(start, len(candidates)):
            mask = candidates[index]
            if mask & used:
                continue
            if any(not neighbours[mask] & other for other in chosen):
                continue
            result = search(chosen + (mask,), used | mask, index + 1)
            if result is not None:
                return result
        return None

    return search((), 0, 0)


def vertices(mask: int) -> list[int]:
    return [vertex for vertex in range(13) if mask >> vertex & 1]


def main() -> None:
    failures = set()
    for flips in product((0, 1), repeat=3):
        order = tuple(
            DUTIES[duty][copy ^ flips[duty]]
            for copy in range(2)
            for duty in range(3)
        )
        adjacency = host(order)
        certificate = None
        for anchor in range(7):
            model = rooted_k5(adjacency, anchor)
            if model is not None:
                certificate = (anchor, tuple(vertices(mask) for mask in model))
                break
        print(flips, order, certificate)
        if certificate is None:
            failures.add(flips)

    assert failures == {(0, 1, 1), (1, 0, 0)}
    print("CERTIFIED six cyclic Moser orientations lift through two packets")


if __name__ == "__main__":
    main()
