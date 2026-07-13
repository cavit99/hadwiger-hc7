#!/usr/bin/env python3
"""Independent replay of all six-vertex unicyclic shore certificates."""

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
VARIABLE = {(n, shore) for shore in SHORES for n in N}


def atlas_types():
    result = {}
    for graph in nx.graph_atlas_g():
        if len(graph) != 6 or graph.number_of_edges() != 6 or not nx.is_connected(graph):
            continue
        code = nx.to_graph6_bytes(graph, header=False).decode().strip()
        edges = tuple(sorted(tuple(sorted(e)) for e in graph.edges()))
        assert code not in result
        result[code] = edges
    assert len(result) == 13
    return result


with open("moser_unicyclic_shore_certificate.json", encoding="utf-8") as source:
    archive = json.load(source)

assert archive["format"] == 1
assert len(archive["cases"]) == 13
expected = atlas_types()
seen = set()
total_models = 0

for case in archive["cases"]:
    code = case["code"]
    assert code in expected and code not in seen
    seen.add(code)
    shore_edges = tuple(tuple(edge) for edge in case["shore_edges"])
    assert shore_edges == expected[code]
    degrees = [sum(i in edge for edge in shore_edges) for i in range(6)]
    assert degrees == case["degrees"]
    assert case["status"] == "unsat"

    fixed_shores = {
        tuple(sorted((SHORES[a], SHORES[b]))) for a, b in shore_edges
    }
    variables = {edge: z3.Bool(f"e_{code}_{edge[0]}_{edge[1]}") for edge in VARIABLE}
    solver = z3.Solver()
    for i, shore in enumerate(SHORES):
        solver.add(z3.Sum([variables[(n, shore)] for n in N]) >= 7 - degrees[i])
    for n in N:
        solver.add(z3.Or([variables[(n, shore)] for shore in SHORES]))

    for record in case["models"]:
        bags = [set(bag) for bag in record["bags"]]
        required = {tuple(edge) for edge in record["edges"]}
        assert len(bags) == 6 and all(bags)
        assert all(bag <= V and bag & N for bag in bags)
        assert all(
            bags[i].isdisjoint(bags[j])
            for i, j in itertools.combinations(range(6), 2)
        )
        assert required and required <= VARIABLE

        graph = nx.Graph()
        graph.add_nodes_from(V)
        graph.add_edges_from(M | fixed_shores | required)
        assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
        assert all(
            any(graph.has_edge(x, y) for x in bags[i] for y in bags[j])
            for i, j in itertools.combinations(range(6), 2)
        )
        solver.add(z3.Or([z3.Not(variables[edge]) for edge in required]))
        total_models += 1

    assert solver.check() == z3.unsat

assert seen == set(expected)
assert total_models == 8447
print(f"verified 13 unicyclic quotient types and {total_models} K6 model clauses")
print("all unicyclic-shore counterexample formulas: UNSAT")

