#!/usr/bin/env python3
"""Independent replay of the six cyclic two-defect shore certificate."""

import itertools
import json

import networkx as nx
import z3


N = set(range(7))
SHORES = tuple(range(7, 13))
V = set(range(13))
M = {
    tuple(sorted(e))
    for e in (
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 6), (2, 6),
        (3, 4), (3, 5), (4, 5), (5, 6),
    )
}
CYCLE = {
    tuple(sorted((SHORES[i], SHORES[(i + 1) % 6])))
    for i in range(6)
}
VARIABLE = {(n, shore) for shore in SHORES for n in N}


with open("moser_cycle_shore_certificate.json", encoding="utf-8") as source:
    archive = json.load(source)

assert archive["format"] == 1
records = archive["models"]
assert len(records) == 1797

variables = {edge: z3.Bool(f"e_{edge[0]}_{edge[1]}") for edge in VARIABLE}
solver = z3.Solver()
for shore in SHORES:
    solver.add(z3.Sum([variables[(n, shore)] for n in N]) >= 5)
for n in N:
    solver.add(z3.Or([variables[(n, shore)] for shore in SHORES]))

for number, record in enumerate(records):
    bags = [set(bag) for bag in record["bags"]]
    required = {tuple(edge) for edge in record["edges"]}
    assert len(bags) == 6
    assert all(bags)
    assert all(bag <= V for bag in bags)
    assert all(bags[i].isdisjoint(bags[j]) for i, j in itertools.combinations(range(6), 2))
    assert all(bag & N for bag in bags)
    assert required <= VARIABLE

    graph = nx.Graph()
    graph.add_nodes_from(V)
    graph.add_edges_from(M | CYCLE | required)
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
    assert all(
        any(graph.has_edge(x, y) for x in bags[i] for y in bags[j])
        for i, j in itertools.combinations(range(6), 2)
    )
    assert required
    solver.add(z3.Or([z3.Not(variables[edge]) for edge in required]))

assert solver.check() == z3.unsat
print(f"verified {len(records)} cyclic-shore K6 model clauses")
print("cyclic two-defect counterexample formula: UNSAT")

