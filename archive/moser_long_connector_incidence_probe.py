#!/usr/bin/env python3
"""Dependency-free probe of the sharp long-connector architecture.

Run with

    python3 moser_long_connector_incidence_probe.py

This is an incidence-only warning, not a contraction-critical example.
All connectivity and carrier assertions are exhaustively checked using
only the Python standard library.
"""

from __future__ import annotations

import itertools


MOSER = (
    (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
    (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
)
P = ("p0", "p1", "p2")
A = tuple(f"a{i}" for i in range(5))
B = tuple(f"b{i}" for i in range(5))
C = P + A + B
U = (0, 5, 2, 4, 6)
F = tuple(zip(U, U[1:] + U[:1]))


class Graph:
    def __init__(self) -> None:
        self.adj: dict[object, set[object]] = {}

    def add_node(self, x: object) -> None:
        self.adj.setdefault(x, set())

    def add_edge(self, x: object, y: object) -> None:
        self.add_node(x)
        self.add_node(y)
        self.adj[x].add(y)
        self.adj[y].add(x)

    def add_edges(self, edges: object) -> None:
        for x, y in edges:  # type: ignore[misc]
            self.add_edge(x, y)

    def has_edge(self, x: object, y: object) -> bool:
        return y in self.adj.get(x, ())

    @property
    def vertices(self) -> tuple[object, ...]:
        return tuple(self.adj)


def build() -> Graph:
    g = Graph()
    for x in range(7):
        g.add_node(x)
    g.add_edges(MOSER)
    g.add_node("v")
    g.add_edges(("v", x) for x in range(7))

    g.add_edges((("p0", "p1"), ("p1", "p2")))
    for p in P:
        for u in (0, 2, 4, 5, 6):
            g.add_edge(p, u)
    g.add_edge("p0", 1)
    g.add_edge("p2", 3)

    g.add_edges(itertools.combinations(A, 2))
    for x in A:
        for u in (2, 4, 5, 6):
            g.add_edge(x, u)
    for x in A[:3]:
        g.add_edge(x, 1)
        g.add_edge(x, "p0")
        g.add_edge(x, "p1")
    for x in A[3:]:
        g.add_edge(x, "p1")
        g.add_edge(x, "p2")

    g.add_edges(itertools.combinations(B, 2))
    for x in B:
        for u in (0, 2, 4, 6):
            g.add_edge(x, u)
    for x in B[:3]:
        g.add_edge(x, 3)
        g.add_edge(x, "p1")
        g.add_edge(x, "p2")
    for x in B[3:]:
        g.add_edge(x, "p0")
        g.add_edge(x, "p1")
    return g


def components(g: Graph, vertices: set[object]) -> list[set[object]]:
    unseen = set(vertices)
    answer: list[set[object]] = []
    while unseen:
        start = next(iter(unseen))
        reached = {start}
        stack = [start]
        unseen.remove(start)
        while stack:
            x = stack.pop()
            for y in g.adj[x] & unseen:
                unseen.remove(y)
                reached.add(y)
                stack.append(y)
        answer.append(reached)
    return answer


def connected(g: Graph, vertices: set[object]) -> bool:
    return bool(vertices) and len(components(g, vertices)) == 1


def is_carrier(g: Graph, vertices: set[object], x: int, y: int) -> bool:
    return (
        connected(g, vertices)
        and any(g.has_edge(x, z) for z in vertices)
        and any(g.has_edge(y, z) for z in vertices)
    )


def main() -> None:
    g = build()
    all_vertices = set(g.vertices)

    # Exhaust the complete cut search through order seven.
    for size in range(7):
        for deleted_tuple in itertools.combinations(g.vertices, size):
            assert connected(g, all_vertices - set(deleted_tuple))
    seven_cuts = []
    for deleted_tuple in itertools.combinations(g.vertices, 7):
        deleted = set(deleted_tuple)
        if not connected(g, all_vertices - deleted):
            seven_cuts.append(deleted)
    assert seven_cuts == [set(range(7))]

    minimum = None
    for size in range(1, len(C) + 1):
        if any(
            is_carrier(g, set(vertices), 1, 3)
            for vertices in itertools.combinations(C, size)
        ):
            minimum = size
            break
    assert minimum == 3 and is_carrier(g, set(P), 1, 3)

    pieces = components(g, set(C) - set(P))
    assert {frozenset(x) for x in pieces} == {frozenset(A), frozenset(B)}
    rows = []
    for piece in pieces:
        row = {
            s for s in range(7)
            if any(g.has_edge(s, x) for x in piece)
        }
        neighbourhood = set().union(*(g.adj[x] for x in piece)) - piece
        assert len(neighbourhood) == 8
        rows.append(row)
    assert {frozenset(x) for x in rows} == {
        frozenset((1, 2, 4, 5, 6)),
        frozenset((0, 2, 3, 4, 6)),
    }
    blocked = {
        edge for edge in F
        if not any(set(edge) <= row for row in rows)
    }
    assert blocked == {(0, 5)}

    nonedges = tuple(
        edge for edge in itertools.combinations(range(7), 2)
        if not g.has_edge(*edge)
    )
    carrier_masks: dict[tuple[int, int], list[int]] = {edge: [] for edge in nonedges}
    for mask in range(1, 1 << len(C)):
        vertices = {C[i] for i in range(len(C)) if mask & (1 << i)}
        if not connected(g, vertices):
            continue
        row = {
            s for s in range(7)
            if any(g.has_edge(s, x) for x in vertices)
        }
        for edge in nonedges:
            if set(edge) <= row:
                carrier_masks[edge].append(mask)

    for e, f in itertools.combinations(nonedges, 2):
        if set(e) & set(f):
            continue
        assert any(
            not (x & y)
            for x in carrier_masks[e]
            for y in carrier_masks[f]
        )

    print("verified: kappa=7 and the Moser boundary is the only 7-cut")
    print("verified: minimum 13-connector order is three")
    print("verified: unique blocked C5 carrier edge is 05")
    print("verified: both blockers have strict neighbourhood eight")
    print("verified: the original shore owns every matching-mode pair")


if __name__ == "__main__":
    main()
