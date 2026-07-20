#!/usr/bin/env python3
"""Verify the seven-column K2-join-planar shadow.

Run with

    PYTHONPATH=active/runtime/deps python3 \
        barriers/hc7_seven_column_k2_planar_shadow_verify.py
"""

from __future__ import annotations

import itertools

import networkx as nx


def midpoint(i: int, j: int) -> tuple[str, int, int]:
    i, j = sorted((i, j))
    return ("m", i, j)


def refined_icosahedron() -> nx.Graph:
    old = nx.icosahedral_graph()
    graph = nx.Graph()
    graph.add_nodes_from(old)
    for i, j in old.edges():
        graph.add_edges_from(((i, midpoint(i, j)), (midpoint(i, j), j)))
    faces = [
        tuple(clique)
        for clique in nx.enumerate_all_cliques(old)
        if len(clique) == 3
    ]
    for i, j, k in faces:
        graph.add_edges_from(
            (
                (midpoint(i, j), midpoint(j, k)),
                (midpoint(j, k), midpoint(i, k)),
                (midpoint(i, k), midpoint(i, j)),
            )
        )
    return graph


def has_k5_minor(graph: nx.Graph) -> bool:
    """Exact five-bag census, used only on the seven-vertex contact graph."""
    vertices = list(graph)
    for assignment in itertools.product(range(5), repeat=len(vertices)):
        if set(assignment) != set(range(5)):
            continue
        bags = [
            {vertices[i] for i, value in enumerate(assignment) if value == label}
            for label in range(5)
        ]
        if not all(nx.is_connected(graph.subgraph(bag)) for bag in bags):
            continue
        if all(
            any(graph.has_edge(u, v) for u in bags[i] for v in bags[j])
            for i in range(5)
            for j in range(i + 1, 5)
        ):
            return True
    return False


def main() -> None:
    planar = refined_icosahedron()
    assert len(planar) == 42
    assert nx.check_planarity(planar)[0]
    assert nx.node_connectivity(planar) == 5

    graph = planar.copy()
    graph.add_edge("a", "b")
    for root in ("a", "b"):
        graph.add_edges_from((root, vertex) for vertex in planar)
    assert nx.node_connectivity(graph) == 7

    x = midpoint(0, 1)
    boundary = set(graph[x])
    assert len(boundary) == 8
    components = list(nx.connected_components(graph.subgraph(set(graph) - boundary)))
    assert len(components) == 2
    assert {x} in components
    far = next(component for component in components if x not in component)
    assert all(any(graph.has_edge(s, y) for y in far) for s in boundary)

    w = midpoint(10, 11)
    assert not planar.has_edge(x, w)
    paths = {
        1: (w, 10, midpoint(3, 10), 3, midpoint(2, 3), 2, midpoint(1, 2), 1),
        0: (w, 11, midpoint(0, 11), 0),
        midpoint(1, 5): (w, midpoint(4, 10), 4, midpoint(4, 5), 5, midpoint(1, 5)),
        midpoint(0, 5): (w, midpoint(4, 11), midpoint(5, 11), midpoint(0, 5)),
        midpoint(1, 8): (w, midpoint(7, 10), 7, midpoint(7, 8), 8, midpoint(1, 8)),
        midpoint(0, 8): (w, midpoint(7, 11), midpoint(0, 7), midpoint(0, 8)),
        "a": (w, "a"),
        "b": (w, "b"),
    }
    assert set(paths) == boundary
    used: set[object] = set()
    for target, path in paths.items():
        assert path[0] == w and path[-1] == target
        assert all(graph.has_edge(u, v) for u, v in zip(path, path[1:]))
        assert set(path[1:-1]).isdisjoint(boundary)
        assert set(path[1:-1]) <= far
        assert set(path[1:]).isdisjoint(used)
        used.update(path[1:])

    p = "a"
    columns = {
        s: {s} | set(paths[s][1:])
        for s in boundary - {p}
    }
    assert all(nx.is_connected(graph.subgraph(column)) for column in columns.values())
    assert all(
        columns[s].isdisjoint(columns[t])
        for s, t in itertools.combinations(columns, 2)
    )
    root_c = {x, p}
    root_d = {w}
    assert nx.is_connected(graph.subgraph(root_c))
    assert any(graph.has_edge(u, v) for u in root_c for v in root_d)
    assert all(any(graph.has_edge(u, v) for u in root_c for v in column) for column in columns.values())
    assert all(any(graph.has_edge(u, v) for u in root_d for v in column) for column in columns.values())

    contact = nx.Graph()
    contact.add_nodes_from(columns)
    for s, t in itertools.combinations(columns, 2):
        if any(graph.has_edge(u, v) for u in columns[s] for v in columns[t]):
            contact.add_edge(s, t)
    cycle = [0, midpoint(0, 5), midpoint(1, 5), 1, midpoint(1, 8), midpoint(0, 8)]
    expected = {frozenset(("b", s)) for s in cycle}
    expected |= {
        frozenset((cycle[i], cycle[(i + 1) % len(cycle)]))
        for i in range(len(cycle))
    }
    assert {frozenset(edge) for edge in contact.edges()} == expected
    # Deleting the universal column leaves a cycle, so the contact graph is
    # K1 join C6 and has treewidth three.  Planarity of the cycle rules out
    # a K4 minor there; hence the join has no K5 minor.
    assert set(contact["b"]) == set(cycle)
    assert nx.is_isomorphic(contact.subgraph(cycle), nx.cycle_graph(6))
    assert not has_k5_minor(contact)
    for u, v in itertools.combinations(contact, 2):
        if contact.has_edge(u, v):
            continue
        augmented = contact.copy()
        augmented.add_edge(u, v)
        assert not has_k5_minor(augmented)

    # The planar core is explicitly four-coloured.  Giving the two join
    # vertices fresh colours yields the proper/proper signature, while the
    # same colouring after deleting x and/or w verifies the planar parts of
    # the three contraction-based positive signatures.
    colouring = nx.coloring.greedy_color(
        planar, strategy="largest_first", interchange=True
    )
    assert max(colouring.values()) < 4
    assert all(colouring[u] != colouring[v] for u, v in planar.edges())
    for removed in ({x}, {w}, {x, w}):
        assert all(
            colouring[u] != colouring[v]
            for u, v in planar.edges()
            if u not in removed and v not in removed
        )

    # The old icosahedral vertices retain degree five in the planar core and
    # therefore have degree seven in the join, locating the missing minimum-
    # interface hypothesis exactly.
    assert min(dict(graph.degree()).values()) == 7
    print("GREEN seven-column K2-planar shadow")


if __name__ == "__main__":
    main()
