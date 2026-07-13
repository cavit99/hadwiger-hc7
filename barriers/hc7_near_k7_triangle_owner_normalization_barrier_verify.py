#!/usr/bin/env python3
"""Verify the triangle-owner P1 normalization barrier."""

from __future__ import annotations

import itertools

import networkx as nx


def build() -> nx.Graph:
    u = ("u0", "u1", "u2")
    labels = ("A", "B", "C", "D2", "D3", "D4")
    g = nx.Graph()
    g.add_edges_from(itertools.combinations(u, 2))
    for x, y in itertools.combinations(labels, 2):
        if frozenset((x, y)) not in {
            frozenset(("A", "B")),
            frozenset(("A", "C")),
        }:
            g.add_edge(x, y)
    for x, pair in zip(u, (("A", "B"), ("C", "D2"), ("D3", "D4"))):
        g.add_edges_from((x, y) for y in pair)
    return g


def main() -> None:
    g = build()
    assert nx.node_connectivity(g) == 4

    five_cliques = [
        frozenset(c) for c in nx.enumerate_all_cliques(g) if len(c) == 5
    ]
    assert five_cliques == [frozenset(("B", "C", "D2", "D3", "D4"))]

    q = set(next(iter(five_cliques)))
    r = set(g) - q
    full = []
    for size in range(1, len(r) + 1):
        for subset in itertools.combinations(r, size):
            if all(any(g.has_edge(x, y) for x in subset) for y in q):
                full.append(set(subset))
    assert full
    assert all({"u0", "u1"} <= subset for subset in full)
    assert not any(a.isdisjoint(b) for a, b in itertools.combinations(full, 2))

    planarizing = []
    for pair in itertools.combinations(g, 2):
        h = nx.Graph(g)
        h.remove_nodes_from(pair)
        if nx.check_planarity(h)[0]:
            planarizing.append(pair)
    assert planarizing

    print("GREEN: K7 excluded by unique-K5 count; bipartite carrier loses roles")
    print("planarizing pairs", planarizing)


if __name__ == "__main__":
    main()
