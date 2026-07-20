#!/usr/bin/env python3
"""Verify the pentagonal-bipyramid target-star shadow.

Run with

    PYTHONPATH=active/runtime/deps python3 \
        barriers/hc7_pentagonal_bipyramid_target_star_shadow_verify.py
"""

from __future__ import annotations

import itertools

import networkx as nx


def build() -> tuple[nx.Graph, dict[str, set[int]]]:
    core = nx.icosahedral_graph()
    graph = core.copy()
    graph.add_edge("v", "w")
    for root in ("v", "w"):
        graph.add_edges_from((root, x) for x in core)
    columns = {
        "A0": {2},
        "A1": {4},
        "R0": {6},
        "R1": {3},
        "R2": {9, 10},
        "R3": {7, 8, 11},
        "R4": {0, 1, 5},
    }
    return graph, columns


def main() -> None:
    graph, columns = build()
    core = graph.subgraph(range(12)).copy()

    expected_core_edges = {
        (0, 1), (0, 5), (0, 7), (0, 8), (0, 11),
        (1, 2), (1, 5), (1, 6), (1, 8),
        (2, 3), (2, 6), (2, 8), (2, 9),
        (3, 4), (3, 6), (3, 9), (3, 10),
        (4, 5), (4, 6), (4, 10), (4, 11),
        (5, 6), (5, 11),
        (7, 8), (7, 9), (7, 10), (7, 11),
        (8, 9), (9, 10), (10, 11),
    }
    assert {tuple(sorted(edge)) for edge in core.edges()} == expected_core_edges
    assert nx.check_planarity(core)[0]
    assert nx.node_connectivity(core) == 5
    assert nx.node_connectivity(graph) == 7
    assert min(dict(graph.degree()).values()) == 7

    assert set().union(*columns.values()) == set(core)
    assert sum(map(len, columns.values())) == len(core)
    assert all(nx.is_connected(graph.subgraph(column)) for column in columns.values())
    assert all(
        columns[left].isdisjoint(columns[right])
        for left, right in itertools.combinations(columns, 2)
    )
    assert graph.has_edge("v", "w")
    assert all(
        any(graph.has_edge(root, x) for x in column)
        for root in ("v", "w")
        for column in columns.values()
    )

    contact = nx.Graph()
    contact.add_nodes_from(columns)
    for left, right in itertools.combinations(columns, 2):
        if any(
            graph.has_edge(x, y)
            for x in columns[left]
            for y in columns[right]
        ):
            contact.add_edge(left, right)

    expected = {
        frozenset((apex, f"R{i}"))
        for apex in ("A0", "A1")
        for i in range(5)
    }
    expected |= {
        frozenset((f"R{i}", f"R{(i + 1) % 5}")) for i in range(5)
    }
    assert {frozenset(edge) for edge in contact.edges()} == expected
    assert set(contact["A0"]) == {f"R{i}" for i in range(5)}
    assert not contact.has_edge("A0", "A1")

    # Seven distinct target/source/auxiliary spokes at v.
    spokes = [
        ("v", 2),  # target A0
        ("v", 6),
        ("v", 3),
        ("v", 9),
        ("v", 7),
        ("v", 0),  # five rim sources
        ("v", 4),  # auxiliary A1
    ]
    assert len({end for _, end in spokes}) == 7
    assert all(graph.has_edge(*edge) for edge in spokes)

    # The dirty intermediate is the whole singleton rim column.
    assert columns["R0"] == {6}
    assert graph.has_edge(2, 6) and graph.has_edge(6, 4)
    assert not graph.has_edge(2, 4)

    # Four-colourability of the planar core supplies the stated trust
    # boundary (the join then uses two fresh colours).
    colouring = nx.coloring.greedy_color(
        core, strategy="largest_first", interchange=True
    )
    assert max(colouring.values()) < 4
    assert all(colouring[x] != colouring[y] for x, y in core.edges())

    print("GREEN pentagonal-bipyramid target-star shadow")


if __name__ == "__main__":
    main()
