#!/usr/bin/env python3
"""Verify the four-colourable combined-negative PB core."""

from __future__ import annotations

from itertools import combinations, product
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "active" / "runtime" / "deps"))

import networkx as nx


POLES = (0, 1)
RIM = (2, 3, 4, 5, 6)
COLUMNS = {label: {(label, 0), (label, 1)} for label in POLES + RIM}
CROSS_EDGES = (
    (1, 0, 2, 1),
    (0, 0, 4, 0),
    (0, 0, 4, 1),
    (0, 1, 4, 0),
    (0, 1, 4, 1),
    (3, 1, 4, 0),
    (1, 0, 5, 0),
    (0, 0, 3, 1),
    (1, 1, 4, 0),
    (1, 1, 4, 1),
    (0, 0, 6, 0),
    (2, 0, 3, 0),
    (2, 0, 3, 1),
    (2, 1, 3, 0),
    (0, 0, 2, 0),
    (4, 1, 5, 0),
    (2, 0, 6, 0),
    (2, 1, 6, 0),
    (2, 1, 6, 1),
    (5, 0, 6, 1),
    (5, 1, 6, 0),
    (5, 1, 6, 1),
    (0, 0, 5, 1),
    (0, 1, 5, 0),
    (0, 1, 5, 1),
    (1, 0, 6, 1),
    (1, 0, 3, 0),
    (1, 0, 3, 1),
    (1, 1, 3, 0),
    (1, 1, 3, 1),
)

ROTATION = {
    0: RIM,
    1: tuple(reversed(RIM)),
    2: (3, 0, 6, 1),
    3: (4, 0, 2, 1),
    4: (5, 0, 3, 1),
    5: (6, 0, 4, 1),
    6: (2, 0, 5, 1),
}


def build_graph() -> nx.Graph:
    graph = nx.Graph()
    for column in COLUMNS.values():
        graph.add_nodes_from(column)
        graph.add_edge(*column)
    graph.add_edges_from(((a, i), (b, j)) for a, i, b, j in CROSS_EDGES)
    return graph


def touches(graph: nx.Graph, vertices: set, label: int) -> bool:
    return any(graph.has_edge(x, y) for x in vertices for y in COLUMNS[label])


def alternating(order: tuple[int, ...], left: set[int], right: set[int]) -> bool:
    for indices in combinations(range(len(order)), 4):
        labels = tuple(order[index] for index in indices)
        if all(labels[i] in (left if i % 2 == 0 else right) for i in range(4)):
            return True
        if all(labels[i] in (right if i % 2 == 0 else left) for i in range(4)):
            return True
    return False


def check_no_alternating_column_cut(graph: nx.Graph) -> None:
    for owner, column in COLUMNS.items():
        left = {min(column)}
        right = column - left
        left_labels = {
            label for label in ROTATION[owner] if touches(graph, left, label)
        }
        right_labels = {
            label for label in ROTATION[owner] if touches(graph, right, label)
        }
        assert not alternating(ROTATION[owner], left_labels, right_labels), owner


def connected_nonempty_subsets(graph: nx.Graph, vertices: set):
    ordered = tuple(sorted(vertices))
    for mask in range(1, 1 << len(ordered)):
        subset = {ordered[i] for i in range(len(ordered)) if mask & (1 << i)}
        if nx.is_connected(graph.subgraph(subset)):
            yield subset


def check_adjacent_rim_linkages_negative(graph: nx.Graph) -> None:
    for position, left_label in enumerate(RIM):
        right_label = RIM[(position + 1) % 5]
        previous = RIM[(position - 1) % 5]
        following = RIM[(position + 2) % 5]
        carrier = COLUMNS[left_label] | COLUMNS[right_label]
        subsets = tuple(connected_nonempty_subsets(graph, carrier))
        for first in subsets:
            if not (touches(graph, first, 0) and touches(graph, first, 1)):
                continue
            for second in subsets:
                if first & second:
                    continue
                if touches(graph, second, previous) and touches(graph, second, following):
                    raise AssertionError((left_label, right_label, first, second))


def check_no_whole_column_anchored_k5(graph: nx.Graph) -> int:
    tested = 0
    for anchors in combinations(COLUMNS, 5):
        unchosen = set(COLUMNS) - set(anchors)
        remaining = [vertex for label in unchosen for vertex in COLUMNS[label]]
        for assignment in product(range(6), repeat=4):
            bags = [set(COLUMNS[label]) for label in anchors]
            for vertex, destination in zip(remaining, assignment):
                if destination < 5:
                    bags[destination].add(vertex)
            tested += 1
            if not all(nx.is_connected(graph.subgraph(bag)) for bag in bags):
                continue
            if all(
                any(graph.has_edge(x, y) for x in bags[i] for y in bags[j])
                for i, j in combinations(range(5), 2)
            ):
                raise AssertionError((anchors, assignment, bags))
    return tested


def main() -> None:
    graph = build_graph()
    assert len(graph) == 14
    assert graph.number_of_edges() == 37
    assert nx.node_connectivity(graph) == 5
    assert not nx.check_planarity(graph)[0]

    expected_contact = {
        frozenset((pole, rim)) for pole in POLES for rim in RIM
    } | {
        frozenset((RIM[i], RIM[(i + 1) % 5])) for i in range(5)
    }
    actual_contact = {
        frozenset((left, right))
        for left, right in combinations(COLUMNS, 2)
        if any(
            graph.has_edge(x, y) for x in COLUMNS[left] for y in COLUMNS[right]
        )
    }
    assert actual_contact == expected_contact

    colouring = {
        (0, 0): 0, (0, 1): 2, (1, 0): 3, (1, 1): 2,
        (2, 0): 2, (2, 1): 1, (3, 0): 0, (3, 1): 1,
        (4, 0): 3, (4, 1): 1, (5, 0): 0, (5, 1): 1,
        (6, 0): 3, (6, 1): 2,
    }
    assert all(colouring[x] != colouring[y] for x, y in graph.edges())
    clique = {(0, 0), (0, 1), (4, 0), (4, 1)}
    assert graph.subgraph(clique).number_of_edges() == 6

    check_no_alternating_column_cut(graph)
    check_adjacent_rim_linkages_negative(graph)
    tested = check_no_whole_column_anchored_k5(graph)
    assert tested == 27_216

    paired_rooted_bags = (
        {(0, 0), (0, 1)},
        {(2, 0), (2, 1)},
        {(1, 0), (3, 1)},
        {(5, 0), (6, 1)},
        {(1, 1), (3, 0), (4, 1)},
    )
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in paired_rooted_bags)
    assert all(
        any(graph.has_edge(x, y) for x in paired_rooted_bags[i]
            for y in paired_rooted_bags[j])
        for i, j in combinations(range(5), 2)
    )
    assert all({vertex[1] for vertex in bag} == {0, 1}
               for bag in paired_rooted_bags)

    print(
        "GREEN four-colour PB core: combined-negative paired-rooted "
        f"anchored_models_tested={tested}"
    )


if __name__ == "__main__":
    main()
