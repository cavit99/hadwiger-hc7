#!/usr/bin/env python3
"""Independent replay of six-vertex tricyclic shore certificates."""

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
        if len(graph) != 6 or graph.number_of_edges() != 8 or not nx.is_connected(graph):
            continue
        code = nx.to_graph6_bytes(graph, header=False).decode().strip()
        edges = tuple(sorted(tuple(sorted(e)) for e in graph.edges()))
        assert code not in result
        result[code] = edges
    assert len(result) == 22
    return result


with open("moser_tricyclic_shore_certificate.json", encoding="utf-8") as source:
    archive = json.load(source)

assert archive["format"] == 1 and archive["edge_count"] == 8
assert archive["cut_constraints"] is True and len(archive["cases"]) == 22
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
    assert case["status"] == "unsat" and case["cut_constraints"] is True

    fixed_shores = {
        tuple(sorted((SHORES[a], SHORES[b]))) for a, b in shore_edges
    }
    variables = {edge: z3.Bool(f"e_{code}_{edge[0]}_{edge[1]}") for edge in VARIABLE}
    solver = z3.Solver()
    for i, shore in enumerate(SHORES):
        solver.add(z3.Sum([variables[(n, shore)] for n in N]) >= 7 - degrees[i])
    for n in N:
        solver.add(z3.Or([variables[(n, shore)] for shore in SHORES]))
    for mask in range(1, (1 << 6) - 1):
        side = {i for i in range(6) if mask >> i & 1}
        cut_size = sum((a in side) != (b in side) for a, b in shore_edges)
        lower_bound = max(0, 7 - cut_size)
        if lower_bound:
            solver.add(z3.Sum([
                z3.If(z3.Or([variables[(n, SHORES[i])] for i in side]), 1, 0)
                for n in N
            ]) >= lower_bound)

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
assert total_models == 64044
print(f"verified 22 tricyclic quotient types and {total_models} K6 model clauses")
print("all six-shore tricyclic counterexample formulas: UNSAT")

