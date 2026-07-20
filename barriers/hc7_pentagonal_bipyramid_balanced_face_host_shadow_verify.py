#!/usr/bin/env python3
"""Verify the seven-connected balanced-face PB shadow.

Run with

    PYTHONPATH=active/runtime/deps python3 \
        barriers/hc7_pentagonal_bipyramid_balanced_face_host_shadow_verify.py
"""

from __future__ import annotations

import itertools

import networkx as nx


RIM = tuple(f"R{i}" for i in range(5))
COLUMNS = {
    "A0": {1, 5, 11},
    "A1": {9},
    "R0": {7},
    "R1": {8},
    "R2": {2, 6},
    "R3": {3, 4},
    "R4": {10},
}


def build() -> tuple[nx.Graph, nx.Graph]:
    core = nx.icosahedral_graph()
    graph = core.copy()
    for root in ("v", "w"):
        graph.add_edges_from((root, x) for x in core)
    return graph, core


def contact_graph(graph: nx.Graph) -> nx.Graph:
    contact = nx.Graph()
    contact.add_nodes_from(COLUMNS)
    for left, right in itertools.combinations(COLUMNS, 2):
        if any(
            graph.has_edge(x, y)
            for x in COLUMNS[left]
            for y in COLUMNS[right]
        ):
            contact.add_edge(left, right)
    return contact


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


def has_alternating_quadruple(
    order: tuple[str, ...], left: set[str], right: set[str]
) -> bool:
    for indices in itertools.combinations(range(len(order)), 4):
        labels = tuple(order[index] for index in indices)
        if (
            labels[0] in left
            and labels[1] in right
            and labels[2] in left
            and labels[3] in right
        ) or (
            labels[0] in right
            and labels[1] in left
            and labels[2] in right
            and labels[3] in left
        ):
            return True
    return False


def connected_bipartitions(graph: nx.Graph, vertices: set[int]):
    anchor = min(vertices)
    others = sorted(vertices - {anchor})
    for size in range(1, len(vertices)):
        for left_rest in itertools.combinations(others, size - 1):
            left = {anchor, *left_rest}
            right = vertices - left
            if nx.is_connected(graph.subgraph(left)) and nx.is_connected(
                graph.subgraph(right)
            ):
                yield left, right


def main() -> None:
    graph, core = build()
    p = 0

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
    assert graph.has_edge("v", p) and graph.has_edge(p, "w")
    assert not graph.has_edge("v", "w")

    assert set().union(*COLUMNS.values()) == set(core) - {p}
    assert sum(map(len, COLUMNS.values())) == len(core) - 1
    assert all(nx.is_connected(core.subgraph(column)) for column in COLUMNS.values())
    assert all(
        COLUMNS[left].isdisjoint(COLUMNS[right])
        for left, right in itertools.combinations(COLUMNS, 2)
    )
    assert all(
        any(graph.has_edge(root, x) for x in column)
        for root in ("v", "w")
        for column in COLUMNS.values()
    )

    contact = contact_graph(graph)
    expected_contact = {
        frozenset((apex, f"R{i}"))
        for apex in ("A0", "A1")
        for i in range(5)
    }
    expected_contact |= {
        frozenset((f"R{i}", f"R{(i + 1) % 5}")) for i in range(5)
    }
    assert {frozenset(edge) for edge in contact.edges()} == expected_contact

    p_labels = {
        label
        for label, column in COLUMNS.items()
        if any(graph.has_edge(p, x) for x in column)
    }
    assert p_labels == {"A0", "R0", "R1"}
    assert contact.subgraph(p_labels).number_of_edges() == 3

    tested = 0
    for owner, column in COLUMNS.items():
        for left, right in connected_bipartitions(core, column):
            tested += 1
            left_labels = contacted_labels(core, left, owner)
            right_labels = contacted_labels(core, right, owner)
            assert not has_alternating_quadruple(
                cyclic_neighbours(owner), left_labels, right_labels
            ), (owner, left, right, left_labels, right_labels)
    assert tested > 0

    boundary = set(graph.neighbors(p))
    assert len(boundary) == 7
    assert {"v", "w"} <= boundary
    assert graph.number_of_nodes() - len(boundary) - 1 > 0

    # One global proper five-colouring restricts to compatible colourings of
    # both closed shores of every separation, including N(p).
    core_colouring = nx.coloring.greedy_color(
        core, strategy="largest_first", interchange=True
    )
    assert max(core_colouring.values()) < 4
    colouring = {**core_colouring, "v": 4, "w": 4}
    assert all(colouring[x] != colouring[y] for x, y in graph.edges())

    print(
        "GREEN balanced-face PB host shadow: "
        f"connected_splits={tested} boundary={len(boundary)}"
    )


if __name__ == "__main__":
    main()
