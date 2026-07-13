#!/usr/bin/env python3
"""Probe literal bipartite singleton shells inside K2 join icosahedron."""

from __future__ import annotations

import itertools
import networkx as nx


I = nx.icosahedral_graph()
G = nx.Graph(I)
G.add_nodes_from(("p", "q"))
G.add_edge("p", "q")
for x in I:
    G.add_edge("p", x)
    G.add_edge("q", x)

found = 0
for a, d in I.edges():
    C = {"p", "q", a, d}
    candidates = [
        x for x in I if x not in C and all(G.has_edge(x, c) for c in C)
    ]
    for v, b in itertools.permutations(candidates, 2):
        if G.has_edge(v, b):
            continue
        B = set(G) - C - {v, b}
        J = G.subgraph(B)
        if not nx.is_connected(J) or not nx.is_bipartite(J):
            continue
        found += 1
        print("C", sorted(map(str, C)), "v,b", v, b)
        print("B", sorted(B), "edges", sorted(J.edges()))
        print("delete-poles-planar", nx.check_planarity(G.subgraph(set(G)-{v,b}))[0])

print("found", found)
