#!/usr/bin/env python3
"""Dependency-free verifier for the palette-wall ear architecture."""

from __future__ import annotations

import itertools


MOSER = (
    (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
    (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
)
P = ("p0", "p1", "p2")
A = tuple(f"a{i}" for i in range(4))
B = tuple(f"b{i}" for i in range(4))
C = P + A + B
CORE = C
CONTACTS = {
    0: {"a0", "a1", "a2", "p0"},
    1: {"a0", "a2", "a3", "p0"},
    2: {"a0", "a1", "a2", "b1", "b2", "p2"},
    3: {"b1", "b2", "b3", "p2"},
    4: {"a0", "a3", "b2", "p0"},
    5: {"b0", "b1", "b2", "b3", "p2"},
    6: {"a0", "a2", "a3", "b0", "b1", "b3", "p0"},
}


class Graph:
    def __init__(self) -> None:
        self.adj: dict[object, set[object]] = {}

    def add(self, x: object, y: object) -> None:
        self.adj.setdefault(x, set()).add(y)
        self.adj.setdefault(y, set()).add(x)

    def has(self, x: object, y: object) -> bool:
        return y in self.adj.get(x, ())

    @property
    def vertices(self) -> tuple[object, ...]:
        return tuple(self.adj)


def build() -> Graph:
    g = Graph()
    for x in range(7):
        g.adj[x] = set()
    for edge in MOSER:
        g.add(*edge)
    g.adj["v"] = set()
    for x in range(7):
        g.add("v", x)
    g.add("p0", "p1")
    g.add("p1", "p2")
    for edge in itertools.combinations(A, 2):
        g.add(*edge)
    for x in A:
        g.add("p0", x)
        g.add("p1", x)
    for edge in itertools.combinations(B, 2):
        g.add(*edge)
    for x in B:
        g.add("p1", x)
        g.add("p2", x)
    g.add("p2", "a1")
    g.add("p0", "b0")
    for s, neighbours in CONTACTS.items():
        for x in neighbours:
            g.add(s, x)
    return g


def components(g: Graph, vertices: set[object]) -> list[set[object]]:
    unseen = set(vertices)
    answer = []
    while unseen:
        start = unseen.pop()
        reached = {start}
        stack = [start]
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


def core_edges(g: Graph) -> tuple[frozenset[object], ...]:
    return tuple(
        frozenset((x, y))
        for i, x in enumerate(CORE)
        for y in CORE[i + 1:]
        if g.has(x, y)
    )


def canonical_core_maps(
    g: Graph, deleted_edge: frozenset[object] | None = None
) -> list[dict[object, int]]:
    edges = set(core_edges(g))
    adjacency = {x: set() for x in CORE}
    for edge in edges:
        x, y = tuple(edge)
        if edge != deleted_edge:
            adjacency[x].add(y)
            adjacency[y].add(x)

    assignment: dict[object, int] = {"p1": 0}
    answers: set[tuple[int, ...]] = set()

    def search() -> None:
        if len(assignment) == len(CORE):
            if deleted_edge is not None:
                x, y = tuple(deleted_edge)
                if assignment[x] != assignment[y]:
                    return
            renaming = {0: 0}
            next_colour = 1
            canonical = []
            for x in CORE:
                colour = assignment[x]
                if colour not in renaming:
                    renaming[colour] = next_colour
                    next_colour += 1
                canonical.append(renaming[colour])
            answers.add(tuple(canonical))
            return

        x = max(
            (z for z in CORE if z not in assignment),
            key=lambda z: (
                len({assignment[n] for n in adjacency[z] if n in assignment}),
                len(adjacency[z]),
            ),
        )
        values: object = range(6)
        if deleted_edge is not None and x in deleted_edge:
            mate = next(iter(deleted_edge - {x}))
            if mate in assignment:
                values = (assignment[mate],)
        forbidden = {assignment[n] for n in adjacency[x] if n in assignment}
        for colour in values:  # type: ignore[assignment]
            if colour in forbidden:
                continue
            assignment[x] = colour
            search()
            del assignment[x]

    search()
    return [dict(zip(CORE, values)) for values in answers]


BOUNDARY_ADJ = {x: set() for x in range(7)}
for x, y in MOSER:
    BOUNDARY_ADJ[x].add(y)
    BOUNDARY_ADJ[y].add(x)


def boundary_colouring(
    core_map: dict[object, int], at_most_five: bool
) -> dict[int, int] | None:
    lists = {
        s: set(range(6)) - {core_map[x] for x in CONTACTS[s]}
        for s in range(7)
    }
    if any(not colours for colours in lists.values()):
        return None
    assignment: dict[int, int] = {}

    def search() -> dict[int, int] | None:
        if len(assignment) == 7:
            condition = len(set(assignment.values())) <= 5
            return dict(assignment) if condition == at_most_five else None
        x = min(
            (z for z in range(7) if z not in assignment),
            key=lambda z: len(
                lists[z] - {assignment[n] for n in BOUNDARY_ADJ[z]
                            if n in assignment}
            ),
        )
        forbidden = {
            assignment[n] for n in BOUNDARY_ADJ[x] if n in assignment
        }
        for colour in lists[x] - forbidden:
            assignment[x] = colour
            answer = search()
            if answer is not None:
                return answer
            del assignment[x]
        return None

    return search()


def exact_trace_extends(g: Graph, pair: tuple[int, int]) -> bool:
    remaining = [x for x in range(7) if x not in pair]
    boundary = {pair[0]: 0, pair[1]: 0}
    boundary.update({x: i + 1 for i, x in enumerate(remaining)})
    vertices = tuple(x for x in g.vertices if x != "v")
    assignment: dict[object, int] = dict(boundary)

    def search() -> bool:
        if len(assignment) == len(vertices):
            return True
        x = max(
            (z for z in vertices if z not in assignment),
            key=lambda z: (
                len({assignment[n] for n in g.adj[z] if n in assignment}),
                len(g.adj[z]),
            ),
        )
        forbidden = {assignment[n] for n in g.adj[x] if n in assignment}
        for colour in range(6):
            if colour in forbidden:
                continue
            assignment[x] = colour
            if search():
                return True
            del assignment[x]
        return False

    return search()


def main() -> None:
    g = build()
    vertices = set(g.vertices)

    for size in range(7):
        for deleted in itertools.combinations(g.vertices, size):
            assert connected(g, vertices - set(deleted))
    cuts = []
    for deleted in itertools.combinations(g.vertices, 7):
        deleted_set = set(deleted)
        if not connected(g, vertices - deleted_set):
            cuts.append(deleted_set)
    assert cuts == [set(range(7))]

    minimum = None
    for size in range(1, len(C) + 1):
        for candidate in itertools.combinations(C, size):
            candidate_set = set(candidate)
            if (
                connected(g, candidate_set)
                and any(g.has(1, x) for x in candidate_set)
                and any(g.has(3, x) for x in candidate_set)
            ):
                minimum = size
                break
        if minimum is not None:
            break
    assert minimum == 3

    pieces = components(g, set(C) - set(P))
    assert {frozenset(x) for x in pieces} == {frozenset(A), frozenset(B)}
    rows = []
    for piece in pieces:
        row = {
            s for s in range(7) if any(g.has(s, x) for x in piece)
        }
        neighbourhood = set().union(*(g.adj[x] for x in piece)) - piece
        assert len(neighbourhood) == 8
        rows.append(row)
    assert {frozenset(x) for x in rows} == {
        frozenset((0, 1, 2, 4, 6)),
        frozenset((2, 3, 4, 5, 6)),
    }

    original_maps = canonical_core_maps(g)
    assert any(boundary_colouring(m, False) for m in original_maps)
    assert not any(boundary_colouring(m, True) for m in original_maps)

    transitions = {}
    p_target = {
        frozenset((0, 6)), frozenset((1, 3)),
        frozenset((2, 5)), frozenset((4,)),
    }
    for edge in core_edges(g):
        witnesses = []
        for core_map in canonical_core_maps(g, edge):
            boundary = boundary_colouring(core_map, True)
            if boundary is not None:
                witnesses.append(boundary)
        assert witnesses
        transitions[edge] = witnesses
    p_edge = frozenset(("p0", "p1"))
    assert any(
        {
            frozenset(x for x in range(7) if state[x] == colour)
            for colour in set(state.values())
        } == p_target
        for state in transitions[p_edge]
    )

    nonedges = tuple(
        pair for pair in itertools.combinations(range(7), 2)
        if not g.has(*pair)
    )
    traces = {pair for pair in nonedges if exact_trace_extends(g, pair)}
    assert traces == {(1, 5)}

    clique = ("p0", "p1", "a0", "a1", "a2", "a3")
    assert all(g.has(x, y) for x, y in itertools.combinations(clique, 2))
    seventh = {"b0", 6, 2}
    assert connected(g, seventh)
    assert all(any(g.has(x, y) for y in seventh) for x in clique)

    print("verified: kappa=7 and the Moser boundary is the only 7-cut")
    print("verified: minimum 13-connector order three; blocker rows have order 8")
    print("verified: palette wall on the original shore")
    print("verified: every internal edge deletion/contraction unlocks <=5 blocks")
    print("verified: p0p1 unlocks 06|13|25|4")
    print("verified: only exact trace 15 extends")
    print("verified: explicit K7 model")


if __name__ == "__main__":
    main()
