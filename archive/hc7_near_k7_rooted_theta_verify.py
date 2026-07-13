#!/usr/bin/env python3
"""Small-graph falsifier for the rooted-neighbour theta lemma.

The proof is in hc7_near_k7_unique_shadow_rooted_theta.md.  This script
exhaustively checks every 3-connected graph in NetworkX's graph atlas
(therefore every graph through seven vertices), every ordered nonadjacent
pole pair, and every prescribed neighbour of the first pole.
"""

from __future__ import annotations

import itertools

import networkx as nx


def has_rooted_theta(g: nx.Graph, u: int, w: int, x: int) -> bool:
    h = nx.Graph(g)
    h.remove_node(u)
    for tail in nx.all_simple_paths(h, x, w):
        internal = set(tail[:-1])
        remainder = nx.Graph(g)
        remainder.remove_nodes_from(internal)
        if nx.node_connectivity(remainder, u, w) >= 2:
            return True
    return False


def main() -> None:
    checked_graphs = 0
    checked_roots = 0
    for raw in nx.graph_atlas_g():
        if len(raw) < 4 or not nx.is_connected(raw):
            continue
        if nx.node_connectivity(raw) < 3:
            continue
        g = nx.convert_node_labels_to_integers(raw)
        checked_graphs += 1
        for u, w, x in itertools.permutations(g, 3):
            if g.has_edge(u, w) or not g.has_edge(u, x):
                continue
            checked_roots += 1
            if not has_rooted_theta(g, u, w, x):
                raise AssertionError(
                    (len(g), sorted(g.edges()), (u, w, x))
                )
    print("GREEN", checked_graphs, "graphs", checked_roots, "rooted triples")


if __name__ == "__main__":
    main()
