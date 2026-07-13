#!/usr/bin/env python3
"""Verify the single-portal and block-cut labelled barriers."""

from __future__ import annotations

import itertools

import networkx as nx


FOREIGN = ("D", "E", "U1", "U2", "U3", "U4")


def shell(two_portals: bool) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(FOREIGN)
    graph.add_edges_from(itertools.combinations(FOREIGN, 2))
    graph.add_edges_from(
        [
            ("pL", "pR"),
            ("pL", "g"),
            ("pR", "g"),
            ("g", "z"),
            ("z", "w"),
            ("w", "x"),
            ("pL", "U1"),
            ("pL", "U2"),
            ("pR", "U3"),
            ("pR", "U4"),
            ("x", "E"),
        ]
    )
    for row in ("U1", "U2", "U3", "U4"):
        graph.add_edge("g", row)
    if two_portals:
        graph.add_edges_from([("w", "y"), ("y", "E")])
    return graph


def carrier(two_portals: bool) -> set[str]:
    return {"g", "z", "w", "x"} | ({"y"} if two_portals else set())


def validate_tree_decomposition(
    graph: nx.Graph,
    bags: list[frozenset[str]],
    tree_edges: list[tuple[int, int]],
) -> None:
    tree = nx.Graph()
    tree.add_nodes_from(range(len(bags)))
    tree.add_edges_from(tree_edges)
    assert nx.is_tree(tree)
    assert max(map(len, bags)) <= 6
    assert all(any({u, v} <= bag for bag in bags) for u, v in graph.edges())
    for vertex in graph:
        indices = [index for index, bag in enumerate(bags) if vertex in bag]
        assert indices
        assert nx.is_connected(tree.subgraph(indices))


def width_five_certificate(graph: nx.Graph, two_portals: bool) -> None:
    bags = [
        frozenset(("D", "E", "U1", "U2", "U3", "U4")),
        frozenset(("E", "U1", "U2", "U3", "U4", "g")),
        frozenset(("U1", "U2", "U3", "U4", "g", "pR")),
        frozenset(("U1", "U2", "g", "pL", "pR")),
    ]
    edges = [(0, 1), (1, 2), (2, 3)]
    if two_portals:
        bags.extend(
            [
                frozenset(("E", "g", "w")),
                frozenset(("E", "w", "x")),
                frozenset(("E", "w", "y")),
                frozenset(("g", "w", "z")),
            ]
        )
        edges.extend([(1, 4), (4, 5), (4, 6), (4, 7)])
    else:
        bags.extend(
            [
                frozenset(("E", "g", "x")),
                frozenset(("g", "w", "x")),
                frozenset(("g", "w", "z")),
            ]
        )
        edges.extend([(1, 4), (4, 5), (5, 6)])
    validate_tree_decomposition(graph, bags, edges)


def sees_all_retained(graph: nx.Graph, subset: frozenset[str]) -> bool:
    return all(
        any(graph.has_edge(vertex, row) for vertex in subset)
        for row in ("E", "U1", "U2", "U3", "U4")
    )


def verify_no_shore_completion(graph: nx.Graph, two_portals: bool) -> None:
    vertices = frozenset({"pL", "pR"} | carrier(two_portals))
    connected = [
        frozenset(choice)
        for size in range(1, len(vertices) + 1)
        for choice in itertools.combinations(vertices, size)
        if nx.is_connected(graph.subgraph(choice))
        and sees_all_retained(graph, frozenset(choice))
    ]
    for left, right in itertools.combinations(connected, 2):
        assert left & right or not any(
            graph.has_edge(u, v) for u in left for v in right
        )


def augmented(two_portals: bool) -> nx.Graph:
    graph = shell(two_portals)
    parts = (
        ("D", "a1", "a2"),
        ("b0", "b1", "b2"),
        ("c0", "c1", "c2"),
    )
    graph.add_nodes_from(set().union(*map(set, parts)))
    for first, second in itertools.combinations(parts, 2):
        graph.add_edges_from(itertools.product(first, second))
    return graph


def verify_model(graph: nx.Graph, two_portals: bool) -> None:
    tripartite = {"D", "a1", "a2", "b0", "b1", "b2", "c0", "c1", "c2"}
    bags = {
        "A": {"pL", "pR"} | carrier(two_portals),
        "D": tripartite,
        "E": {"E"},
        "U1": {"U1"},
        "U2": {"U2"},
        "U3": {"U3"},
        "U4": {"U4"},
    }
    assert set().union(*bags.values()) == set(graph)
    assert sum(map(len, bags.values())) == len(graph)
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags.values())
    foreign = ("D", "E", "U1", "U2", "U3", "U4")
    assert all(
        any(graph.has_edge(u, v) for u in bags[x] for v in bags[y])
        for x, y in itertools.combinations(foreign, 2)
    )
    assert all(
        any(graph.has_edge(u, v) for u in bags["A"] for v in bags[row])
        for row in ("E", "U1", "U2", "U3", "U4")
    )
    assert not any(
        graph.has_edge(u, v) for u in bags["A"] for v in bags["D"]
    )


def main() -> None:
    for two_portals in (False, True):
        base = shell(two_portals)
        width_five_certificate(base, two_portals)
        verify_no_shore_completion(base, two_portals)

        graph = augmented(two_portals)
        verify_model(graph, two_portals)
        assert nx.node_connectivity(graph) == 1
        assert not any(
            nx.check_planarity(graph.subgraph(set(graph) - set(pair)))[0]
            for pair in itertools.combinations(graph, 2)
        )

        if two_portals:
            k = graph.subgraph(carrier(True))
            assert nx.is_connected(k)
            components = list(nx.connected_components(nx.subgraph_view(k, filter_node=lambda v: v != "z")))
            assert {"w", "x", "y"} in components
            assert {"g"} in components
        else:
            assert {v for v in carrier(False) if graph.has_edge(v, "E")} == {"x"}

    print("GREEN: unique portal and cutvertex arm barriers verified")
    print("shell treewidth <=5; augmented hosts K7-free by one-sum proof")
    print("augmented hosts non-two-apex and have connectivity exactly 1")


if __name__ == "__main__":
    main()
