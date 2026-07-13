#!/usr/bin/env python3
"""Independent verifier for the two seven-shore cactus certificates."""

import itertools
import json

import networkx as nx
import z3


N = set(range(7))
SHORES = tuple(range(7, 14))
V = set(range(14))
M = {
    tuple(sorted(e))
    for e in (
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 6), (2, 6),
        (3, 4), (3, 5), (4, 5), (5, 6),
    )
}
VARIABLE = {(n, shore) for shore in SHORES for n in N}

CASES = {
    "friendship": {
        (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
        (1, 2), (3, 4), (5, 6),
    },
    "chain": {
        (0, 1), (0, 2), (1, 2),
        (2, 3), (2, 4), (3, 4),
        (4, 5), (4, 6), (5, 6),
    },
}


def verify(name):
    with open(f"moser_cactus7_{name}_certificate.json", encoding="utf-8") as source:
        archive = json.load(source)
    assert archive["format"] == 1 and archive["name"] == name
    quotient = {tuple(edge) for edge in archive["shore_edges"]}
    assert quotient == CASES[name]

    fixed_shores = {
        tuple(sorted((SHORES[a], SHORES[b]))) for a, b in quotient
    }
    variables = {edge: z3.Bool(f"e_{name}_{edge[0]}_{edge[1]}")
                 for edge in VARIABLE}
    solver = z3.Solver()
    for mask in range(1, (1 << 7) - 1):
        side = {i for i in range(7) if mask >> i & 1}
        cut_size = sum((a in side) != (b in side) for a, b in quotient)
        lower = max(0, 7 - cut_size)
        if lower:
            solver.add(z3.Sum([
                z3.If(z3.Or([variables[(n, SHORES[i])] for i in side]), 1, 0)
                for n in N
            ]) >= lower)
    for n in N:
        solver.add(z3.Or([variables[(n, shore)] for shore in SHORES]))

    for record in archive["models"]:
        bags = [set(bag) for bag in record["bags"]]
        required = {tuple(edge) for edge in record["edges"]}
        assert len(bags) == 6 and all(bags)
        assert all(bag <= V and bag & N for bag in bags)
        assert all(bags[i].isdisjoint(bags[j])
                   for i, j in itertools.combinations(range(6), 2))
        assert required and required <= VARIABLE

        graph = nx.Graph()
        graph.add_nodes_from(V)
        graph.add_edges_from(M | fixed_shores | required)
        assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
        assert all(any(graph.has_edge(x, y) for x in bags[i] for y in bags[j])
                   for i, j in itertools.combinations(range(6), 2))
        solver.add(z3.Or([z3.Not(variables[e]) for e in required]))

    assert solver.check() == z3.unsat
    print(name, "verified", len(archive["models"]), "K6 model clauses")


if __name__ == "__main__":
    verify("friendship")
    verify("chain")
