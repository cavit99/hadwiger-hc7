#!/usr/bin/env python3
"""Verify the 8-connected path/three-portal-tree barrier."""

from __future__ import annotations

from itertools import combinations

import networkx as nx


S = ("d", "e", "x1", "x2", "x3", "y1", "y2", "y3")
X = ("x1", "x2", "x3")
Y = ("y1", "y2", "y3")
Q = tuple(f"q{i}" for i in range(5))
R = ("r0", "r1")

PORTALS = {
    "d": frozenset(("q0",)),
    "e": frozenset(("q2",)),
    "x1": frozenset(("q1",)),
    "x2": frozenset(("q3",)),
    "x3": frozenset(Q),
    "y1": frozenset(Q),
    "y2": frozenset(Q),
    "y3": frozenset(Q),
}


def build() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(S + Q + R)

    graph.add_edges_from((x, y) for x in X for y in Y)
    graph.add_edges_from((a, z) for a in ("d", "e") for z in X + Y)
    graph.add_edges_from(
        (
            ("q0", "q1"),
            ("q1", "q2"),
            ("q2", "q3"),
            ("q3", "q0"),
            ("q4", "q0"),
            ("q4", "q1"),
            ("q4", "q2"),
            ("q4", "q3"),
        )
    )
    graph.add_edges_from(
        (s, q) for s, portals in PORTALS.items() for q in portals
    )
    graph.add_edge("r0", "r1")
    graph.add_edges_from((r, s) for r in R for s in S)
    return graph


def connected(graph: nx.Graph, vertices: frozenset[str]) -> bool:
    return bool(vertices) and nx.is_connected(graph.subgraph(vertices))


def packing_witness(graph: nx.Graph):
    qset = frozenset(Q)
    checked = 0
    for root_order in range(2, len(Q) + 1):
        for root_tuple in combinations(Q, root_order):
            root_support = frozenset(root_tuple)
            if not (PORTALS["d"] & root_support and PORTALS["e"] & root_support):
                continue
            if not connected(graph, root_support):
                continue
            available = qset - root_support
            for tree_order in range(1, len(available) + 1):
                for tree_tuple in combinations(sorted(available), tree_order):
                    tree_support = frozenset(tree_tuple)
                    checked += 1
                    if not connected(graph, tree_support):
                        continue
                    if all(PORTALS[x] & tree_support for x in X):
                        return root_support, tree_support, checked
    return None, None, checked


def main() -> None:
    graph = build()
    assert len(graph) == 15
    assert graph.number_of_edges() == 70

    boundary = graph.subgraph(S)
    assert not boundary.has_edge("d", "e")
    assert boundary.subgraph(X).number_of_edges() == 0
    assert boundary.subgraph(Y).number_of_edges() == 0
    assert all(boundary.has_edge(a, z) for a in ("d", "e") for z in X + Y)
    assert all(boundary.has_edge(x, y) for x in X for y in Y)

    open_graph = graph.subgraph(set(graph) - set(S))
    open_components = {frozenset(c) for c in nx.connected_components(open_graph)}
    assert open_components == {frozenset(Q), frozenset(R)}
    assert not any(graph.has_edge(q, r) for q in Q for r in R)
    for component in open_components:
        assert all(any(graph.has_edge(s, v) for v in component) for s in S)

    qgraph = graph.subgraph(Q).copy()
    assert nx.node_connectivity(qgraph) == 3

    tested_cuts = 0
    for order in range(8):
        for deleted in combinations(tuple(graph), order):
            tested_cuts += 1
            remainder = graph.copy()
            remainder.remove_nodes_from(deleted)
            assert nx.is_connected(remainder), deleted
    assert tested_cuts == 16384
    assert nx.node_connectivity(graph) == 8

    remainder = graph.copy()
    remainder.remove_nodes_from(S)
    assert nx.number_connected_components(remainder) == 2

    root_support, tree_support, checked_pairs = packing_witness(qgraph)
    assert root_support is None and tree_support is None

    print("GREEN portal path/three-set-tree connectivity barrier")
    print("G: vertices=15 edges=70 connectivity=8 cuts_tested=16384")
    print("G-S: two connected S-full components of orders 5 and 2")
    print("Q: W5 connectivity=3; exhaustive packing witness: none")
    print(f"connected-support pairs checked={checked_pairs}")
    print("scope: no K7-minor-free or contraction-critical claim")


if __name__ == "__main__":
    main()
