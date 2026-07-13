#!/usr/bin/env python3
"""Verify finite members of the spanning-minimal deficient-tree barrier."""

from __future__ import annotations

import itertools

import networkx as nx


def build(height: int) -> tuple[nx.Graph, set[object]]:
    tree = nx.balanced_tree(3, height)
    tree = nx.relabel_nodes(tree, lambda x: ('t', x))
    root = ('t', 0)
    labels = ('B', 'C', 'U1', 'U2', 'U3', 'U4')
    graph = nx.Graph(tree)
    graph.add_edges_from(itertools.combinations(labels, 2))
    graph.add_edges_from((root, label) for label in labels[2:])
    return graph, set(tree)


def main() -> None:
    for height in range(1, 6):
        graph, tree = build(height)
        root = ('t', 0)
        labels = ('B', 'C', 'U1', 'U2', 'U3', 'U4')
        assert nx.is_tree(graph.subgraph(tree))
        assert set(graph.neighbors(root)) & set(labels) == set(labels[2:])
        assert all(
            not (set(graph.neighbors(x)) - tree)
            for x in tree - {root}
        )
        assert nx.node_connectivity(graph) == 1
        print(height, len(graph), 'forced_tree_vertices', len(tree))
    print('GREEN')


if __name__ == '__main__':
    main()
