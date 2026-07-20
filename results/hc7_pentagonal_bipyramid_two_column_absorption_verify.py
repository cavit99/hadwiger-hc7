#!/usr/bin/env python3
"""Verify the fourteen-vertex two-column absorption certificate."""

from __future__ import annotations

from itertools import combinations
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "active" / "runtime" / "deps"))

import networkx as nx


COLUMNS = {label: {(label, 0), (label, 1)} for label in range(7)}
CROSS_EDGES = (
    (1, 0, 2, 1),
    (0, 0, 4, 1),
    (3, 0, 4, 0),
    (3, 1, 4, 0),
    (3, 1, 4, 1),
    (1, 0, 5, 0),
    (1, 1, 5, 0),
    (1, 1, 5, 1),
    (0, 0, 3, 1),
    (1, 0, 4, 0),
    (0, 1, 6, 0),
    (0, 1, 6, 1),
    (2, 0, 3, 0),
    (2, 0, 3, 1),
    (2, 1, 3, 0),
    (0, 0, 2, 0),
    (0, 0, 2, 1),
    (0, 1, 2, 0),
    (0, 1, 2, 1),
    (4, 0, 5, 0),
    (4, 1, 5, 0),
    (4, 1, 5, 1),
    (2, 1, 6, 0),
    (5, 1, 6, 1),
    (0, 1, 5, 1),
    (1, 0, 6, 0),
    (1, 0, 6, 1),
    (1, 1, 6, 0),
    (1, 1, 6, 1),
    (1, 0, 3, 0),
)


def has_edge_between(graph: nx.Graph, left: set, right: set) -> bool:
    return any(graph.has_edge(x, y) for x in left for y in right)


def main() -> None:
    graph = nx.Graph()
    for column in COLUMNS.values():
        graph.add_nodes_from(column)
        graph.add_edge(*column)
    graph.add_edges_from(((a, i), (b, j)) for a, i, b, j in CROSS_EDGES)

    assert len(graph) == 14
    assert graph.number_of_edges() == 37
    assert nx.node_connectivity(graph) == 5
    assert not nx.check_planarity(graph)[0]

    x_1 = {(0, 1), (2, 0)}
    x_2 = {(0, 0), (2, 1)}
    bags = (
        COLUMNS[1],
        COLUMNS[3] | x_1,
        COLUMNS[4] | x_2,
        COLUMNS[5],
        COLUMNS[6],
    )

    assert set().union(*bags) == set(graph)
    assert sum(map(len, bags)) == len(graph)
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
    assert all(
        bags[i].isdisjoint(bags[j])
        for i, j in combinations(range(5), 2)
    )
    assert all(
        has_edge_between(graph, bags[i], bags[j])
        for i, j in combinations(range(5), 2)
    )

    print("GREEN combined-negative PB core: distributed K5 certificate")


if __name__ == "__main__":
    main()
