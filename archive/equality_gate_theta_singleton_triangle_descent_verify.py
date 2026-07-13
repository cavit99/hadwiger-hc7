#!/usr/bin/env python3
"""Exact certificates for the theta singleton-triangle descent.

The boundary is the complement of the seven-edge theta missing graph.
The script checks both crossed two-cut defect orientations and all sixteen
tag pairs used in the atomic-web curvature closure.
"""

from __future__ import annotations

from itertools import combinations, product

import networkx as nx


LABELS = tuple(range(7))
MISSING = {
    (0, 1), (0, 2), (0, 5), (1, 2), (1, 5), (2, 4), (4, 5)
}
P = (0, 5)
Q = (1, 2)
R = (3, 4, 6)


def boundary_edges() -> set[tuple[object, object]]:
    return set(combinations(LABELS, 2)) - MISSING


def verify_model(graph: nx.Graph, bags: tuple[frozenset[object], ...]) -> None:
    assert len(bags) == 7
    assert all(bags)
    assert all(bags[i].isdisjoint(bags[j]) for i, j in combinations(range(7), 2))
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
    assert all(
        any(graph.has_edge(x, y) for x in bags[i] for y in bags[j])
        for i, j in combinations(range(7), 2)
    )


def verify_crossed_two_cuts() -> None:
    for defects, bags in (
        (
            P,
            (
                frozenset({1}), frozenset({3}), frozenset({4}), frozenset({6}),
                frozenset({"L0"}), frozenset({2, "L5"}), frozenset({5, "E"}),
            ),
        ),
        (
            Q,
            (
                frozenset({0}), frozenset({3}), frozenset({4}), frozenset({6}),
                frozenset({"L1"}), frozenset({5, "L2"}), frozenset({2, "E"}),
            ),
        ),
    ):
        graph = nx.Graph()
        graph.add_edges_from(boundary_edges())
        left, right = (f"L{defects[0]}", f"L{defects[1]}")
        for lobe, missed in ((left, defects[0]), (right, defects[1])):
            graph.add_edges_from((lobe, label) for label in LABELS if label != missed)
            graph.add_edges_from(((lobe, "z0"), (lobe, "z1")))
        graph.add_edges_from(("E", label) for label in LABELS)
        verify_model(graph, bags)


def verify_two_tag_closure() -> None:
    for p_u, q_u, p_v, q_v in product(P, Q, P, Q):
        graph = nx.Graph()
        graph.add_edges_from(boundary_edges())
        graph.add_edges_from(("X", root) for root in P)
        graph.add_edges_from(("Y", root) for root in Q)
        graph.add_edge("A", "B")
        graph.add_edges_from(("A", root) for root in (*R, p_u, q_u))
        graph.add_edges_from(("B", root) for root in (*R, p_v, q_v))
        bags = (
            frozenset({3}), frozenset({4}), frozenset({6}),
            frozenset({0, 5, "X"}), frozenset({1, 2, "Y"}),
            frozenset({"A"}), frozenset({"B"}),
        )
        verify_model(graph, bags)


def main() -> None:
    # The five quotient blocks P,Q and the three R singletons form K5.
    blocks = (set(P), set(Q), *({root} for root in R))
    edges = boundary_edges()
    assert all(
        any(tuple(sorted((x, y))) in edges for x in blocks[i] for y in blocks[j])
        for i, j in combinations(range(5), 2)
    )
    assert all(tuple(sorted(edge)) not in edges for edge in (P, Q))
    assert all(tuple(sorted(edge)) in edges for edge in combinations(R, 2))

    verify_crossed_two_cuts()
    verify_two_tag_closure()
    print("theta five-block quotient verified")
    print("crossed two-cut K7 certificates", 2)
    print("two-tag K7 certificates", 16)
    print("theta singleton-triangle descent certificates verified")


if __name__ == "__main__":
    main()
