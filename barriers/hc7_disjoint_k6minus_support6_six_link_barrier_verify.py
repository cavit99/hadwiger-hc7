#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["networkx==3.6.1"]
# ///
"""Verify the explicit six-link quotient and its width-five certificate."""

from __future__ import annotations

from itertools import combinations

import networkx as nx  # noqa: E402


LEFT = frozenset(range(6))
RIGHT = frozenset(range(6, 12))
Q = frozenset(range(4))
X = frozenset(range(6, 10))
SPLIT = frozenset({4, 5})
MISSING = frozenset({10, 11})
MATCHING = ((0, 6), (1, 7), (2, 8), (3, 10), (4, 11), (5, 9))

BAGS = (
    frozenset({0, 1, 2, 3, 4, 6}),
    frozenset({1, 2, 3, 4, 6, 7}),
    frozenset({2, 3, 4, 6, 7, 8}),
    frozenset({3, 4, 6, 7, 8, 9}),
    frozenset({3, 4, 5, 9}),
    frozenset({3, 6, 7, 8, 9, 10}),
    frozenset({4, 6, 7, 8, 9, 11}),
)

TREE_EDGES = ((0, 1), (1, 2), (2, 3), (3, 4), (3, 5), (3, 6))


def host() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(range(12))
    graph.add_edges_from(combinations(Q, 2))
    graph.add_edge(4, 5)
    graph.add_edges_from((q, 4) for q in (0, 1, 2))
    graph.add_edge(3, 5)
    graph.add_edges_from(
        edge for edge in combinations(RIGHT, 2) if frozenset(edge) != MISSING
    )
    graph.add_edges_from(MATCHING)
    return graph


def verify_tree_decomposition(graph: nx.Graph) -> None:
    tree = nx.Graph()
    tree.add_nodes_from(range(len(BAGS)))
    tree.add_edges_from(TREE_EDGES)
    assert nx.is_tree(tree)
    assert max(map(len, BAGS)) == 6

    assert set().union(*BAGS) == set(graph)
    for edge in graph.edges:
        assert any(set(edge) <= bag for bag in BAGS)
    for vertex in graph:
        containing = [index for index, bag in enumerate(BAGS) if vertex in bag]
        assert containing
        assert nx.is_connected(tree.subgraph(containing))


def main() -> None:
    graph = host()

    # The left side is a six-vertex K5 model: Q is its singleton K4 and
    # {4,5} is its connected fifth branch set, jointly adjacent to Q.
    assert all(graph.has_edge(*edge) for edge in combinations(Q, 2))
    assert graph.has_edge(4, 5)
    assert all(any(graph.has_edge(q, endpoint) for endpoint in SPLIT) for q in Q)

    # The right side is K6 minus one edge, and the six displayed cross-edges
    # are a perfect matching between the two sides.
    assert graph.subgraph(RIGHT).number_of_edges() == 14
    assert not graph.has_edge(*tuple(MISSING))
    assert {left for left, _ in MATCHING} == LEFT
    assert {right for _, right in MATCHING} == RIGHT
    assert all(graph.has_edge(left, right) for left, right in MATCHING)

    verify_tree_decomposition(graph)
    # A width-five graph cannot contain K7 as a minor, since treewidth is
    # minor-monotone and tw(K7)=6.
    print("GREEN: six-link quotient has a width-five tree decomposition")
    print(nx.to_graph6_bytes(graph, header=False).decode().strip())


if __name__ == "__main__":
    main()
