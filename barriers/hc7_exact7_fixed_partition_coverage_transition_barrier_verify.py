#!/usr/bin/env python3
"""Verify the fixed-partition coverage/Kempe-path barrier.

The checker uses only the Python standard library.  It verifies the graph,
colouring, boundary two-colour components, support packing and minimum
orders, obstruction-path contacts, and the width-four elimination order.
"""

from itertools import combinations


BOUNDARY = tuple(range(7))
OPEN = ("u0", "u1", "u2", "u3", "u4", "u5", "s")


def edge(a, b):
    return frozenset((a, b))


EDGES = {
    edge(0, 1), edge(0, 2), edge(0, 3), edge(0, 4),
    edge(1, 2), edge(1, 6), edge(2, 6), edge(3, 4),
    edge(3, 5), edge(4, 5), edge(5, 6),
}

cycle = ("u0", "u1", "u2", "u3", "u4", "u5", "s")
EDGES.update(edge(cycle[i], cycle[(i + 1) % len(cycle)]) for i in range(7))
portal_labels = (2, 1, 0, 3, 4, 5)
EDGES.update(edge(portal_labels[i], f"u{i}") for i in range(6))
EDGES.add(edge(6, "u0"))

VERTICES = set(BOUNDARY) | set(OPEN)
DUTIES = {
    "A": {2, 3},
    "B": {1, 4},
    "D": {0, 5},
}

COLOUR = {
    2: 1, 3: 1,
    1: 2, 4: 2,
    0: 3, 5: 3,
    6: 4,
    "u0": 2, "s": 1, "u5": 2, "u4": 1,
    "u1": 5, "u2": 6, "u3": 5,
}


def adjacent(a, b):
    return edge(a, b) in EDGES


def connected(vertices):
    vertices = set(vertices)
    if not vertices:
        return False
    seen = {next(iter(vertices))}
    todo = list(seen)
    while todo:
        u = todo.pop()
        for v in vertices - seen:
            if adjacent(u, v):
                seen.add(v)
                todo.append(v)
    return seen == vertices


def boundary_contacts(vertices):
    return {
        s for s in BOUNDARY
        if any(adjacent(s, v) for v in vertices)
    }


def connected_open_sets():
    answer = []
    for mask in range(1, 1 << len(OPEN)):
        vertices = {OPEN[i] for i in range(len(OPEN)) if mask & (1 << i)}
        if connected(vertices):
            answer.append(vertices)
    return answer


def filled_width(order):
    graph = {v: set() for v in VERTICES}
    for e in EDGES:
        a, b = tuple(e)
        graph[a].add(b)
        graph[b].add(a)
    width = 0
    for v in order:
        neighbours = list(graph[v])
        width = max(width, len(neighbours))
        for a, b in combinations(neighbours, 2):
            graph[a].add(b)
            graph[b].add(a)
        for u in neighbours:
            graph[u].remove(v)
        del graph[v]
    assert not graph
    return width


def main():
    assert len(VERTICES) == 14
    assert len(EDGES) == 25
    assert all(COLOUR[a] != COLOUR[b] for a, b in map(tuple, EDGES))

    two_colour_boundary = {v for v in BOUNDARY if COLOUR[v] in {1, 2}}
    components = []
    unseen = set(two_colour_boundary)
    while unseen:
        component = {unseen.pop()}
        todo = list(component)
        while todo:
            u = todo.pop()
            for v in list(unseen):
                if adjacent(u, v):
                    unseen.remove(v)
                    component.add(v)
                    todo.append(v)
        components.append(frozenset(component))
    assert set(components) == {frozenset({1, 2}), frozenset({3, 4})}

    obstruction = (2, "u0", "s", "u5", "u4", 4)
    assert all(adjacent(a, b) for a, b in zip(obstruction, obstruction[1:]))
    assert all(COLOUR[v] in {1, 2} for v in obstruction)

    supports = []
    for vertices in connected_open_sets():
        contacts = boundary_contacts(vertices)
        funded = {name for name, duty in DUTIES.items() if duty <= contacts}
        if funded:
            supports.append((vertices, funded))

    minimum = {
        name: min(len(vertices) for vertices, funded in supports if name in funded)
        for name in DUTIES
    }
    assert minimum == {"A": 4, "B": 4, "D": 4}

    # Alternation is checked literally: no two disjoint connected supports
    # fund two different duties.
    for (left, left_funded), (right, right_funded) in combinations(supports, 2):
        if left.isdisjoint(right):
            assert len(left_funded | right_funded) == 1

    interior = {"u0", "s", "u5", "u4"}
    assert boundary_contacts(interior) == {2, 4, 5, 6}
    assert all(not (duty <= boundary_contacts(interior)) for duty in DUTIES.values())

    containing_minimum = {}
    for name, duty in DUTIES.items():
        containing_minimum[name] = min(
            len(vertices)
            for vertices in connected_open_sets()
            if interior <= vertices and duty <= boundary_contacts(vertices)
        )
    assert containing_minimum == {"A": 5, "B": 5, "D": 6}

    elimination_order = (
        "s", "u1", 2, 1, "u3", "u5", 4, 3,
        6, 0, 5, "u0", "u2", "u4",
    )
    assert set(elimination_order) == VERTICES
    assert filled_width(elimination_order) == 4

    print("GREEN fixed-partition coverage transition barrier")
    print("order=14 size=25 treewidth<=4 kappa_P(Pi)=1 minimum_support=4")
    print("obstruction_contacts=2,4,5,6 extension_orders=A:5,B:5,D:6")


if __name__ == "__main__":
    main()
