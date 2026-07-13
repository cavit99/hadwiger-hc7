#!/usr/bin/env python3
"""Independent replay of the theta nonowner K7 certificates.

The script uses only the theta boundary edge list.  It verifies both
two-cut defect orientations and all tag choices in the curvature closure.
"""

from __future__ import annotations

from itertools import combinations, product

import networkx as nx


MISSING = {
    tuple(sorted(edge))
    for edge in ((0, 1), (0, 2), (0, 5), (1, 2), (1, 5), (2, 4), (4, 5))
}
S = tuple(range(7))
P = (0, 5)
Q = (1, 2)
R = (3, 4, 6)


def base_graph() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(S)
    for x, y in combinations(S, 2):
        if (x, y) not in MISSING:
            graph.add_edge(x, y)
    graph.add_nodes_from(("xp", "xq"))
    graph.add_edges_from(("xp", x) for x in P)
    graph.add_edges_from(("xq", x) for x in Q)
    return graph


def check_model(graph: nx.Graph, bags: tuple[frozenset[object], ...]) -> None:
    assert len(bags) == 7
    assert all(bags[i].isdisjoint(bags[j]) for i, j in combinations(range(7), 2))
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
    assert all(
        any(graph.has_edge(x, y) for x in bags[i] for y in bags[j])
        for i, j in combinations(range(7), 2)
    )


def two_cut_certificate(active: tuple[int, int], other: tuple[int, int]) -> None:
    graph = base_graph()
    if active == Q:
        # Relabel carrier roles for the symmetric Q-defect certificate.
        graph.remove_nodes_from(("xp", "xq"))
        graph.add_nodes_from(("xp", "xq"))
        graph.add_edges_from(("xp", x) for x in active)
        graph.add_edges_from(("xq", x) for x in other)
    a, b = active
    graph.add_nodes_from(("la", "lb", "z"))
    graph.add_edges_from(("la", x) for x in S if x != b)
    graph.add_edges_from(("lb", x) for x in S if x != a)
    graph.add_edges_from((("z", "la"), ("z", "lb")))
    bags = (
        frozenset((*active, "xp")),
        frozenset((*other, "xq")),
        *(frozenset((x,)) for x in R),
        frozenset(("la", "z")),
        frozenset(("lb",)),
    )
    check_model(graph, bags)


def tagged_certificate(tags: tuple[tuple[int, int], tuple[int, int]]) -> None:
    graph = base_graph()
    graph.add_edge("w0", "w1")
    for index, (p, q) in enumerate(tags):
        w = f"w{index}"
        graph.add_edges_from((w, x) for x in (*R, p, q))
    bags = (
        frozenset((*P, "xp")),
        frozenset((*Q, "xq")),
        *(frozenset((x,)) for x in R),
        frozenset(("w0",)),
        frozenset(("w1",)),
    )
    check_model(graph, bags)


def main() -> None:
    two_cut_certificate(P, Q)
    two_cut_certificate(Q, P)
    tag_types = tuple(product(P, Q))
    checked = 0
    for first in tag_types:
        for second in tag_types:
            tagged_certificate((first, second))
            checked += 1
    print("two-cut certificates 2")
    print("tagged certificates", checked)


if __name__ == "__main__":
    main()
