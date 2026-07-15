#!/usr/bin/env python3
"""Dependency-free verifier for the icosahedral singleton-K6 barrier."""

from __future__ import annotations

from itertools import combinations


ICO_NEIGHBOURS = {
    0: {1, 5, 7, 8, 11},
    1: {0, 2, 5, 6, 8},
    2: {1, 3, 6, 8, 9},
    3: {2, 4, 6, 9, 10},
    4: {3, 5, 6, 10, 11},
    5: {0, 1, 4, 6, 11},
    6: {1, 2, 3, 4, 5},
    7: {0, 8, 9, 10, 11},
    8: {0, 1, 2, 7, 9},
    9: {2, 3, 7, 8, 10},
    10: {3, 4, 7, 9, 11},
    11: {0, 4, 5, 7, 10},
}


def joined_host() -> dict[object, set[object]]:
    graph: dict[object, set[object]] = {
        vertex: set(neighbours) for vertex, neighbours in ICO_NEIGHBOURS.items()
    }
    graph["a"] = set(ICO_NEIGHBOURS)
    graph["b"] = set(ICO_NEIGHBOURS)
    for vertex in ICO_NEIGHBOURS:
        graph[vertex].update(("a", "b"))
    return graph


def connected(graph: dict[object, set[object]], vertices: set[object]) -> bool:
    if not vertices:
        return False
    reached = {next(iter(vertices))}
    frontier = list(reached)
    while frontier:
        vertex = frontier.pop()
        for neighbour in graph[vertex] & vertices - reached:
            reached.add(neighbour)
            frontier.append(neighbour)
    return reached == vertices


def vertex_connectivity_at_least(graph: dict[object, set[object]], k: int) -> bool:
    vertices = tuple(graph)
    for size in range(k):
        for deleted in combinations(vertices, size):
            remainder = set(vertices) - set(deleted)
            if len(remainder) > 1 and not connected(graph, remainder):
                return False
    return True


def bags_form_clique_model(
    graph: dict[object, set[object]], bags: list[set[object]]
) -> bool:
    if any(not connected(graph, bag) for bag in bags):
        return False
    if sum(map(len, bags)) != len(set().union(*bags)):
        return False
    return all(
        any(y in graph[x] for x in left for y in right)
        for index, left in enumerate(bags)
        for right in bags[index + 1 :]
    )


def main() -> None:
    ico = {vertex: set(neighbours) for vertex, neighbours in ICO_NEIGHBOURS.items()}
    host = joined_host()
    s0 = {0, 1, 2, 3, 4, 11}
    shore_a = {5, 6}
    shore_b = {7, 8, 9, 10}
    boundary = s0 | {"a", "b"}

    assert vertex_connectivity_at_least(ico, 5)
    assert not connected(ico, set(ico) - ICO_NEIGHBOURS[0])
    assert vertex_connectivity_at_least(host, 7)
    seven_cut = {"a", "b"} | ICO_NEIGHBOURS[0]
    assert len(seven_cut) == 7
    assert not connected(host, set(host) - seven_cut)

    assert connected(ico, shore_a) and connected(ico, shore_b)
    assert set(ico) - s0 == shore_a | shore_b
    assert not any(y in ico[x] for x in shore_a for y in shore_b)
    for shore in (shore_a, shore_b):
        assert all(any(x in host[s] for x in shore) for s in boundary)

    expected_cycle = {
        frozenset(edge)
        for edge in ((0, 1), (1, 2), (2, 3), (3, 4), (4, 11), (11, 0))
    }
    actual_cycle = {
        frozenset((x, y)) for x in s0 for y in ico[x] & s0 if x < y
    }
    assert actual_cycle == expected_cycle

    # Explicit proper three-colouring of the boundary join.
    cycle_order = (0, 1, 2, 3, 4, 11)
    colour = {vertex: index % 2 for index, vertex in enumerate(cycle_order)}
    colour.update({"a": 2, "b": 2})
    assert all(
        colour[x] != colour[y]
        for x in boundary
        for y in host[x] & boundary
    )

    bags = [{5}, {6}, {1}, {2, 3, 4}, {"a", 0}, {"b"}]
    assert bags_form_clique_model(host, bags)

    print("GREEN: seven-connectivity, full shores, boundary and singleton K6 verify")


if __name__ == "__main__":
    main()
