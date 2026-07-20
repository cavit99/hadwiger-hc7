#!/usr/bin/env python3
"""Verify the nonplanar nonsplit pentagonal-bipyramid expansion."""

from __future__ import annotations

import itertools

import networkx as nx


RIM = tuple(f"R{i}" for i in range(5))
COLUMNS = {
    "A0": {2},
    "A1": {4},
    "R0": {6},
    "R1": {3},
    "R2": {9, 10},
    "R3": {7, 8, 11},
    "R4": {0, 1, 5},
}


def cyclic_neighbours(label: str) -> tuple[str, ...]:
    if label in ("A0", "A1"):
        return RIM
    index = int(label[1])
    return (
        f"R{(index - 1) % 5}",
        "A0",
        f"R{(index + 1) % 5}",
        "A1",
    )


def contacted_labels(graph: nx.Graph, vertices: set[int], owner: str) -> set[str]:
    return {
        label
        for label, column in COLUMNS.items()
        if label != owner
        and any(graph.has_edge(x, y) for x in vertices for y in column)
    }


def alternating(order: tuple[str, ...], left: set[str], right: set[str]) -> bool:
    for indices in itertools.combinations(range(len(order)), 4):
        labels = tuple(order[index] for index in indices)
        if all(labels[i] in (left if i % 2 == 0 else right) for i in range(4)):
            return True
        if all(labels[i] in (right if i % 2 == 0 else left) for i in range(4)):
            return True
    return False


def connected_bipartitions(graph: nx.Graph, vertices: set[int]):
    anchor = min(vertices)
    others = sorted(vertices - {anchor})
    for size in range(1, len(vertices)):
        for rest in itertools.combinations(others, size - 1):
            left = {anchor, *rest}
            right = vertices - left
            if nx.is_connected(graph.subgraph(left)) and nx.is_connected(
                graph.subgraph(right)
            ):
                yield left, right


def verify_model(graph: nx.Graph, bags: tuple[set[int], ...]) -> None:
    assert all(bags)
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
    assert all(
        bags[i].isdisjoint(bags[j])
        for i, j in itertools.combinations(range(len(bags)), 2)
    )
    assert all(
        any(graph.has_edge(x, y) for x in bags[i] for y in bags[j])
        for i, j in itertools.combinations(range(len(bags)), 2)
    )


def main() -> None:
    graph = nx.icosahedral_graph()
    assert not graph.has_edge(1, 7)
    graph.add_edge(1, 7)

    assert nx.node_connectivity(graph) == 5
    assert not nx.check_planarity(graph)[0]
    assert set().union(*COLUMNS.values()) == set(graph)
    assert sum(map(len, COLUMNS.values())) == len(graph)
    assert all(nx.is_connected(graph.subgraph(column)) for column in COLUMNS.values())

    contact = nx.Graph()
    contact.add_nodes_from(COLUMNS)
    for left, right in itertools.combinations(COLUMNS, 2):
        if any(
            graph.has_edge(x, y)
            for x in COLUMNS[left]
            for y in COLUMNS[right]
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

    tested = 0
    for owner, column in COLUMNS.items():
        for left, right in connected_bipartitions(graph, column):
            tested += 1
            assert not alternating(
                cyclic_neighbours(owner),
                contacted_labels(graph, left, owner),
                contacted_labels(graph, right, owner),
            ), (owner, left, right)
    assert tested == 6

    verify_model(
        graph,
        ({4}, {6}, {2, 3, 8}, {0, 5, 11}, {1, 7, 10}),
    )
    verify_model(
        graph,
        ({3, 9}, {2, 6}, {4, 5}, {0, 8, 11}, {1, 7, 10}),
    )

    print(
        "GREEN nonplanar nonsplit PB expansion: "
        f"connectivity=5 connected_splits={tested}"
    )


if __name__ == "__main__":
    main()
