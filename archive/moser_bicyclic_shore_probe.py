#!/usr/bin/env python3
"""Explore all six-vertex, seven-edge shore quotients over the Moser boundary."""

import json

import networkx as nx

from moser_unicyclic_shore_probe import solve_case


types = []
for graph in nx.graph_atlas_g():
    if len(graph) == 6 and graph.number_of_edges() == 7 and nx.is_connected(graph):
        code = nx.to_graph6_bytes(graph, header=False).decode().strip()
        edges = tuple(sorted(tuple(sorted(e)) for e in graph.edges()))
        types.append((code, edges))

print("types", len(types), flush=True)
archive = {"format": 1, "edge_count": 7, "cases": []}
for number, (code, edges) in enumerate(types):
    result = solve_case(code, edges)
    archive["cases"].append(result)
    print(number, code, result["degrees"], result["status"], len(result["models"]), flush=True)
    if result["status"] == "counterexample":
        print(result["defects"], flush=True)
with open("moser_bicyclic_shore_certificate.json", "w", encoding="utf-8") as out:
    json.dump(archive, out, indent=2)

