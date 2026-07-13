#!/usr/bin/env python3
"""Test the quotient forced by a direct L-to-R st-numbering jump."""

from __future__ import annotations

import itertools


W = tuple(range(6))
Z = 6
A, U, B, H = 7, 8, 9, 10
V = tuple(range(11))


def set_partitions(values: tuple[int, ...], blocks: int):
    if not values:
        if blocks == 0:
            yield ()
        return

    def rec(index: int, current: list[list[int]]):
        if index == len(values):
            if len(current) == blocks:
                yield tuple(tuple(block) for block in current)
            return
        value = values[index]
        for position in range(len(current)):
            current[position].append(value)
            yield from rec(index + 1, current)
            current[position].pop()
        if len(current) < blocks:
            current.append([value])
            yield from rec(index + 1, current)
            current.pop()

    yield from rec(1, [[values[0]]])


def candidates():
    for order in range(7, 12):
        for support in itertools.combinations(V, order):
            for partition in set_partitions(support, 7):
                yield tuple(sum(1 << vertex for vertex in block)
                            for block in partition)


def quotient(optional_u: frozenset[int]) -> set[tuple[int, int]]:
    boundary = set(itertools.combinations((*W, Z), 2))
    boundary -= {tuple(sorted((i, (i + 1) % 6))) for i in W}
    edges = boundary
    edges |= {(A, U), (U, B)}
    edges |= {(s, H) for s in (*W, Z)}
    edges |= {(s, A) for s in (*W, Z) if s not in {5, 1}}
    edges |= {(s, B) for s in (*W, Z) if s not in {0, 2}}
    edges |= {(s, U) for s in ({2, 5} | set(optional_u))}
    return {tuple(sorted(edge)) for edge in edges}


def model(edges: set[tuple[int, int]], all_candidates):
    adjacency = [0] * len(V)
    for first, second in edges:
        adjacency[first] |= 1 << second
        adjacency[second] |= 1 << first

    connected_cache: dict[int, bool] = {}
    neighbour_cache: dict[int, int] = {}

    def connected(mask: int) -> bool:
        if mask not in connected_cache:
            reached = mask & -mask
            while True:
                expanded = reached
                bits = reached
                while bits:
                    low = bits & -bits
                    expanded |= adjacency[low.bit_length() - 1] & mask
                    bits ^= low
                if expanded == reached:
                    connected_cache[mask] = reached == mask
                    break
                reached = expanded
        return connected_cache[mask]

    def neighbours(mask: int) -> int:
        if mask not in neighbour_cache:
            union = 0
            bits = mask
            while bits:
                low = bits & -bits
                union |= adjacency[low.bit_length() - 1]
                bits ^= low
            neighbour_cache[mask] = union
        return neighbour_cache[mask]

    for bags in all_candidates:
        if all(connected(bag) for bag in bags) and all(
            neighbours(bags[i]) & bags[j]
            for i in range(7) for j in range(i)
        ):
            return bags
    return None


def display(bags):
    names = (*map(str, W), "z", "A", "u", "B", "H")
    return [tuple(names[v] for v in V if mask >> v & 1) for mask in bags]


def main() -> None:
    all_candidates = tuple(candidates())
    print("candidate partitions", len(all_candidates))
    for transition, removed, expected_trigger in (
        ("L-M", 5, 3),
        ("M-R", 2, 4),
        ("L-R", None, None),
    ):
        optional = (3, 4, Z)
        for add_bridge in (False, True):
            for size in range(4):
                for subset in itertools.combinations(optional, size):
                    edges = quotient(frozenset(subset))
                    if removed is not None:
                        edges.discard(tuple(sorted((removed, U))))
                    if add_bridge:
                        edges.add(tuple(sorted((A, B))))
                    bags = model(edges, all_candidates)
                    positive = bags is not None
                    if not add_bridge:
                        expected = False
                    elif transition == "L-R":
                        expected = 3 in subset or 4 in subset
                    else:
                        expected = expected_trigger in subset
                    assert positive == expected
                    print(transition, "AB", add_bridge, "optional", subset,
                          "K7", positive)
                    if positive and subset in ((3,), (4,)):
                        print(display(bags))


if __name__ == "__main__":
    main()
