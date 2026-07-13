#!/usr/bin/env python3
"""Exact small counterexamples for the uniform three-demand exchange."""

from __future__ import annotations

from itertools import combinations

import networkx as nx


def carriers(graph: nx.Graph, left: set[int], right: set[int]):
    answer = set()
    for a in left:
        for b in right:
            for path in nx.all_simple_paths(graph, a, b):
                answer.add(frozenset(path))
    return tuple(answer)


def linkable(families):
    def rec(index, used):
        if index == len(families):
            return True
        return any(
            not carrier & used and rec(index + 1, used | carrier)
            for carrier in families[index]
        )

    return rec(0, frozenset())


def capacity_two_example():
    graph = nx.Graph()
    x, y = 0, 1
    portal_sets = []
    next_vertex = 2
    for _ in range(6):
        portal = {next_vertex, next_vertex + 1}
        next_vertex += 2
        portal_sets.append(portal)
        graph.add_edges_from((hub, leaf) for hub in (x, y) for leaf in portal)
    demands = tuple(
        carriers(graph, portal_sets[2 * i], portal_sets[2 * i + 1])
        for i in range(3)
    )
    assert all(linkable((demands[i], demands[j])) for i, j in combinations(range(3), 2))
    assert not linkable(demands)
    assert all(len(portal) == 2 for portal in portal_sets)
    assert nx.minimum_node_cut(graph) == {x, y}
    return graph, portal_sets


def prism_capture_example():
    graph = nx.Graph()
    graph.add_edges_from(
        (
            (0, 2), (2, 3), (3, 0),
            (1, 4), (4, 5), (5, 1),
            (0, 1), (2, 5), (3, 4),
        )
    )
    pairs = ((0, 2), (1, 3), (4, 5))
    demands = tuple(carriers(graph, {a}, {b}) for a, b in pairs)
    assert all(linkable((demands[i], demands[j])) for i, j in combinations(range(3), 2))
    assert not linkable(demands)
    assert nx.node_connectivity(graph) == 3

    # Transparent pair-linkages.  In each linkage involving demand 1--3,
    # the displayed route captures a terminal of the omitted demand.
    witnesses = (
        ((0, 2), (1, 4, 3)),  # demands 02 and 13, captures terminal 4
        ((0, 2), (4, 5)),     # demands 02 and 45
        ((1, 0, 3), (4, 5)),  # demands 13 and 45, captures terminal 0
    )
    for first, second in witnesses:
        assert all(graph.has_edge(first[i], first[i + 1]) for i in range(len(first) - 1))
        assert all(graph.has_edge(second[i], second[i + 1]) for i in range(len(second) - 1))
        assert set(first).isdisjoint(second)
        assert any(graph.has_edge(a, b) for a in first for b in second)
    # The two packets using demand 1--3 capture one singleton portal of
    # their omitted demand.  The middle packet is instead a clean web row.
    assert 4 in set(witnesses[0][0]) | set(witnesses[0][1])
    assert 0 in set(witnesses[2][0]) | set(witnesses[2][1])
    middle_rails = set(witnesses[1][0]) | set(witnesses[1][1])
    assert {1, 3}.isdisjoint(middle_rails)
    assert not nx.has_path(graph.subgraph(set(graph) - middle_rails), 1, 3)
    return graph, pairs, witnesses


def three_connected_clean_web_example():
    """A 3-connected pairwise-but-not-triple example with clean packets."""
    graph = nx.Graph()
    graph.add_edges_from(
        (
            (0, 1), (0, 2), (0, 5), (0, 6),
            (1, 3), (1, 6), (1, 7),
            (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
            (3, 7),
            (4, 5), (4, 6),
            (5, 6), (5, 7),
            (6, 7),
        )
    )
    pairs = ((0, 4), (1, 2), (3, 5))
    demands = tuple(carriers(graph, {a}, {b}) for a, b in pairs)
    assert all(linkable((demands[i], demands[j])) for i, j in combinations(range(3), 2))
    assert not linkable(demands)
    assert nx.node_connectivity(graph) == 3
    witnesses = (
        ((0, 6, 4), (1, 7, 2)),
        ((0, 6, 4), (3, 7, 5)),
        ((1, 6, 2), (3, 7, 5)),
    )
    all_terminals = set(range(6))
    for packet_index, (first, second) in enumerate(witnesses):
        assert all(graph.has_edge(first[i], first[i + 1]) for i in range(len(first) - 1))
        assert all(graph.has_edge(second[i], second[i + 1]) for i in range(len(second) - 1))
        assert set(first).isdisjoint(second)
        assert any(graph.has_edge(a, b) for a in first for b in second)
        endpoints = {first[0], first[-1], second[0], second[-1]}
        assert not ((set(first[1:-1]) | set(second[1:-1])) & (all_terminals - endpoints))
        used_demands = ((0, 1), (0, 2), (1, 2))[packet_index]
        omitted = ({0, 1, 2} - set(used_demands)).pop()
        omitted_terminals = set(pairs[omitted])
        rails = set(first) | set(second)
        assert omitted_terminals.isdisjoint(rails)
        residual = graph.subgraph(set(graph) - rails)
        a, b = pairs[omitted]
        assert not nx.has_path(residual, a, b)
    return graph, pairs, witnesses


def main():
    graph, portals = capacity_two_example()
    print("capacity-two example", len(graph), "vertices", graph.number_of_edges(), "edges")
    print("portal sets", tuple(tuple(sorted(portal)) for portal in portals))
    prism, pairs, witnesses = prism_capture_example()
    print("prism capture example", sorted(prism.edges()))
    print("demands", pairs, "pair-linkages", witnesses)
    clean, pairs, witnesses = three_connected_clean_web_example()
    print("3-connected clean-web example", sorted(clean.edges()))
    print("demands", pairs, "clean pair-linkages", witnesses)
    print("all three-demand counterexample assertions verified")


if __name__ == "__main__":
    main()
