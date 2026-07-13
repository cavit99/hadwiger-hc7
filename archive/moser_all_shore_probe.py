#!/usr/bin/env python3
"""Find the sparsest six-vertex shore quotient defeating row bounds alone."""

import networkx as nx

from moser_unicyclic_shore_probe import solve_case


types = []
for graph in nx.graph_atlas_g():
    if len(graph) == 6 and nx.is_connected(graph):
        code = nx.to_graph6_bytes(graph, header=False).decode().strip()
        edges = tuple(sorted(tuple(sorted(e)) for e in graph.edges()))
        types.append((len(edges), code, edges))
types.sort()
print("types", len(types), flush=True)

for number, (edge_count, code, edges) in enumerate(types):
    if edge_count < 8:
        continue
    result = solve_case(code, edges)
    print(
        number, edge_count, code, result["degrees"], result["status"],
        len(result["models"]), flush=True,
    )
    if result["status"] == "counterexample":
        print("defects", result["defects"], flush=True)
        break
