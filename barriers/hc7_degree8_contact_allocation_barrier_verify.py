#!/usr/bin/env python3
"""Verify the finite degree-eight contact-allocation barrier."""

from __future__ import annotations

from itertools import combinations


VERTICES = tuple(range(9))
V, B0, B1, B2, C0, C1, C2, C3, C4 = VERTICES
B = (B0, B1, B2)
C = (C0, C1, C2, C3, C4)
S = frozenset((*B, C0, C1, C3, C4))


def make_edges() -> set[frozenset[int]]:
    edges = {frozenset((V, vertex)) for vertex in (*B, *C)}
    edges.update(
        frozenset((b, c))
        for b in B
        for c in C
        if (b, c) != (B2, C0)
    )
    edges.update((frozenset((C0, C1)), frozenset((C2, C3))))
    return edges


EDGES = make_edges()


def adjacent(x: int, y: int) -> bool:
    return frozenset((x, y)) in EDGES


def connected(vertices: frozenset[int]) -> bool:
    seen = {next(iter(vertices))}
    frontier = list(seen)
    while frontier:
        vertex = frontier.pop()
        for other in vertices - seen:
            if adjacent(vertex, other):
                seen.add(other)
                frontier.append(other)
    return seen == set(vertices)


def branch_sets() -> list[frozenset[int]]:
    values = []
    for mask in range(1, 1 << len(VERTICES)):
        vertices = frozenset(i for i in VERTICES if mask & (1 << i))
        if vertices & S and connected(vertices):
            values.append(vertices)
    return values


def sets_adjacent(left: frozenset[int], right: frozenset[int]) -> bool:
    return any(adjacent(x, y) for x in left for y in right)


def has_s_meeting_k6() -> bool:
    candidates = branch_sets()

    def search(start: int, chosen: tuple[frozenset[int], ...]) -> bool:
        if len(chosen) == 6:
            return True
        if len(candidates) - start < 6 - len(chosen):
            return False
        used = frozenset().union(*chosen) if chosen else frozenset()
        for index in range(start, len(candidates)):
            candidate = candidates[index]
            if candidate & used:
                continue
            if not all(sets_adjacent(candidate, old) for old in chosen):
                continue
            if search(index + 1, (*chosen, candidate)):
                return True
        return False

    return search(0, ())


def independence_number_without_v() -> int:
    vertices = (*B, *C)
    for size in range(len(vertices), 0, -1):
        for subset in combinations(vertices, size):
            if all(not adjacent(x, y) for x, y in combinations(subset, 2)):
                return size
    raise AssertionError("the graph is nonempty")


def main() -> None:
    assert len(S) == 7
    assert independence_number_without_v() == 3
    assert all(adjacent(b, c) for b in B for c in C if (b, c) != (B2, C0))
    assert not adjacent(B2, C0)
    assert not has_s_meeting_k6()
    print("GREEN: degree-eight contact-allocation barrier verified")


if __name__ == "__main__":
    main()
