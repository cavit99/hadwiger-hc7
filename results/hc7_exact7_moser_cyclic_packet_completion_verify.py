#!/usr/bin/env python3
"""Verify the six explicit gap-avoiding Moser K7 models."""

from __future__ import annotations


MOSER = {
    (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
    (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
}
PORTAL_ORDER = (2, 4, 5, 3, 1, 0)
P = tuple(range(7, 13))
Q = tuple(range(13, 19))
T = 19

MODELS = {
    0: ((0,), (3, 16, 17), (19,), (2, 13, 14, 18),
        (1, 9, 10, 11), (5, 6, 7, 12), (4, 8)),
    1: ((1, 6, 8, 17), (4,), (5, 9, 10, 11, 12),
        (2, 13, 14, 15, 18), (3, 16), (0,), (19,)),
    2: ((1, 17), (4, 6, 8, 9), (13, 14, 15, 18),
        (3, 10, 11, 12, 16), (2, 7), (0,), (5, 19)),
    3: ((7, 8, 9, 12), (0, 3), (5, 13, 14, 15), (6, 10),
        (4, 19), (1, 11, 17, 18), (2,)),
    4: ((0, 12), (5, 7, 8, 9), (4, 13, 14, 18), (2,),
        (3, 6, 10, 11), (1, 15, 16, 17), (19,)),
    5: ((1, 16, 17), (0,), (6, 11, 12), (2, 7, 8, 13, 18),
        (4, 5, 15), (19,), (3, 9, 10)),
}


def edge(left: int, right: int) -> tuple[int, int]:
    return tuple(sorted((left, right)))


def base_graph(gap: int) -> set[tuple[int, int]]:
    edges = {edge(*item) for item in MOSER}
    for cycle in (P, Q):
        edges |= {
            edge(cycle[index], cycle[(index + 1) % 6])
            for index in range(6)
        }
        edges |= {
            edge(literal, cycle[index])
            for index, literal in enumerate(PORTAL_ORDER)
        }
    edges |= {edge(T, literal) for literal in range(7)}
    edges.add(edge(6, P[gap]))
    edges.remove(edge(P[gap], P[(gap + 1) % 6]))
    return edges


def connected(vertices: set[int], edges: set[tuple[int, int]]) -> bool:
    seen = {next(iter(vertices))}
    frontier = list(seen)
    while frontier:
        current = frontier.pop()
        for left, right in edges:
            other = right if left == current else left if right == current else -1
            if other in vertices and other not in seen:
                seen.add(other)
                frontier.append(other)
    return seen == vertices


def verify_model(gap: int) -> None:
    edges = base_graph(gap)
    bags = [set(bag) for bag in MODELS[gap]]
    assert len(bags) == 7
    assert all(bags)
    assert all(not (bags[i] & bags[j]) for i in range(7) for j in range(i))
    assert all(connected(bag, edges) for bag in bags)
    assert 6 in next(bag for bag in bags if P[gap] in bag)

    for right in range(7):
        for left in range(right):
            witnesses = [
                item
                for item in sorted(edges)
                if item[0] in bags[left] and item[1] in bags[right]
                or item[1] in bags[left] and item[0] in bags[right]
            ]
            assert witnesses, (gap, left, right)
            print(
                f"gap={gap} bags={left}-{right} witness={witnesses[0]}",
                flush=True,
            )


if __name__ == "__main__":
    for gap in range(6):
        verify_model(gap)
    print("CERTIFIED six gap-avoiding literal K7 models")
