#!/usr/bin/env python3
"""Verify the width-five adjacent-defect-one order-eight barrier."""

from __future__ import annotations


N = 12
A, B, Q0, Q1 = 8, 9, 10, 11
ORDER = (0, 6, 7, 1, 2, 3, 4, 5, 8, 9, 10, 11)
EXPECTED = (
    (1, 2, 9, 10, 11),
    (8, 9, 10, 11),
    (8, 9, 10, 11),
    (2, 8, 9, 10, 11),
    (8, 9, 10, 11),
    (4, 5, 8, 10, 11),
    (5, 8, 9, 10, 11),
    (8, 9, 10, 11),
    (9, 10, 11),
    (10, 11),
    (11,),
    (),
)


def build() -> list[set[int]]:
    graph = [set() for _ in range(N)]

    def edge(x: int, y: int) -> None:
        graph[x].add(y)
        graph[y].add(x)

    for triangle in ((0, 1, 2), (3, 4, 5)):
        for index, x in enumerate(triangle):
            for y in triangle[:index]:
                edge(x, y)
    for carrier, missed in ((A, 0), (B, 3), (Q0, None), (Q1, None)):
        for boundary in range(8):
            if boundary != missed:
                edge(carrier, boundary)
    edge(A, B)
    return graph


def main() -> None:
    graph = build()
    boundary = set(range(8))
    assert graph[A] & boundary == boundary - {0}
    assert graph[B] & boundary == boundary - {3}
    assert graph[Q0] & boundary == boundary
    assert graph[Q1] & boundary == boundary
    assert B in graph[A]

    alive = set(range(N))
    actual = []
    width = 0
    for vertex in ORDER:
        later = tuple(sorted(graph[vertex] & alive))
        actual.append(later)
        width = max(width, len(later))
        for x in later:
            for y in later:
                if x != y:
                    graph[x].add(y)
        alive.remove(vertex)

    assert tuple(actual) == EXPECTED
    assert width == 5
    print("vertices=12")
    print("defects=A:{0} B:{3} full=Q0,Q1 edge=AB")
    print("elimination_order=0,6,7,1,2,3,4,5,8,9,10,11")
    print("elimination_width=5")
    print("K7_minor=no (treewidth at most 5)")


if __name__ == "__main__":
    main()
