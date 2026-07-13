#!/usr/bin/env python3
"""Replay the sharp four-common-owner reserve zero row.

The quotient is the first inclusion-maximal negative row for profile
``(c,c,a)`` with the first path piece split.  This script checks the
literal rooted K4, both pool contacts, the free-component zero rows, and
absence of a K7 minor using the independent spanning-partition search in
``near_k7_exceptional_cross_split_atlas``.
"""

from __future__ import annotations

import networkx as nx

from near_k7_exceptional_cross_split_atlas import (
    A,
    B,
    C,
    Q1,
    Q2,
    Q3,
    X,
    has_k7,
    split_adjacency,
)


def main() -> None:
    profile = (C, C, A)
    target = 0
    pool_0 = 9
    pool_1 = X[target]
    common = {Q1, Q2, Q3, X[1]}
    side_0 = {A, B, Q1, Q2, Q3, X[1]}
    side_1 = set(common)
    adjacency = split_adjacency(profile, target, side_0, side_1)

    graph = nx.Graph()
    graph.add_nodes_from(range(10))
    graph.add_edges_from(
        (u, v)
        for u in range(10)
        for v in range(u + 1, 10)
        if adjacency[u] >> v & 1
    )

    assert graph.has_edge(pool_0, pool_1)
    assert all(graph.has_edge(u, v) for u in common for v in common if u < v)
    assert all(graph.has_edge(root, pool) for root in common for pool in (pool_0, pool_1))

    protected = common | {pool_0, pool_1}
    free = graph.subgraph(set(graph) - protected)
    components = [set(component) for component in nx.connected_components(free)]
    assert {frozenset(component) for component in components} == {
        frozenset({A}),
        frozenset({B, C, X[2]}),
    }

    columns = (pool_0, pool_1, Q1, Q2, Q3, X[1])
    rows = []
    for component in components:
        row = tuple(any(graph.has_edge(x, column) for x in component) for column in columns)
        assert not all(row)
        assert not row[1]
        rows.append((tuple(sorted(component)), row))

    assert not has_k7(adjacency)
    print("four-common rooted K4 verified", tuple(sorted(common)))
    print("free-component incidence rows", sorted(rows))
    print("K7 minor", False)


if __name__ == "__main__":
    main()
