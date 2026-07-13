#!/usr/bin/env python3
"""Independent certificate for the ten-vertex sharpness graph in Section 2."""

from __future__ import annotations

from itertools import combinations

import networkx as nx

from contact_order7_sixedge_web_probe import generic_minor_model


def build_graph() -> tuple[nx.Graph, nx.Graph]:
    # Seven-vertex 2-tree T.
    tree = nx.Graph()
    tree.add_edges_from(
        (
            ("b", "x2"), ("b", "x3"), ("x2", "x3"),
            ("u", "b"), ("u", "x2"),
            ("a", "u"), ("a", "x2"),
            ("v", "u"), ("v", "x2"),
            ("c", "b"), ("c", "x3"),
        )
    )
    graph = tree.copy()
    neutral = ("q1", "q2", "q3")
    graph.add_edges_from(combinations(neutral, 2))
    graph.add_edges_from((q, vertex) for q in neutral for vertex in tree)
    return graph, tree


def edge_set(graph: nx.Graph) -> set[tuple[int, int]]:
    index = {vertex: i for i, vertex in enumerate(graph)}
    return {tuple(sorted((index[u], index[v]))) for u, v in graph.edges()}


def main() -> None:
    graph, tree = build_graph()
    assert len(tree) == 7 and tree.number_of_edges() == 11
    assert nx.node_connectivity(tree) == 2
    assert len(graph) == 10 and graph.number_of_edges() == 35
    assert nx.node_connectivity(graph) == 5
    assert generic_minor_model(len(graph), edge_set(graph), 7) is None

    planar_deletions = []
    for pair in combinations(graph, 2):
        remainder = graph.copy()
        remainder.remove_nodes_from(pair)
        if nx.check_planarity(remainder)[0]:
            planar_deletions.append(pair)
    assert not planar_deletions

    print("sharpness graph vertices", len(graph), "edges", graph.number_of_edges())
    print("connectivity", nx.node_connectivity(graph), "K7 minor", False)
    print("planar two-vertex deletions", tuple(planar_deletions))
    print("nested-triangle sharpness obstruction verified")


if __name__ == "__main__":
    main()
