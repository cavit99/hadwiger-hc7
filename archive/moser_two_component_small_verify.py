#!/usr/bin/env python3
"""Independent verifier for the K2/K3/K4 exterior shore certificates."""

import itertools
import json

import networkx as nx
import z3


N = tuple(range(7))
M = {
    tuple(sorted(e))
    for e in (
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 6), (2, 6),
        (3, 4), (3, 5), (4, 5), (5, 6),
    )
}


def verify(order):
    with open(f"moser_two_component_k{order}_certificate.json",
              encoding="utf-8") as source:
        archive = json.load(source)
    assert archive["format"] == 1 and archive["order"] == order

    small = tuple(range(7, 7 + order))
    full = 7 + order
    vertices = set(range(full + 1))
    variable_edges = {(n, x) for x in small for n in N}
    variables = {edge: z3.Bool(f"e_{order}_{edge[0]}_{edge[1]}")
                 for edge in variable_edges}
    fixed = set(M)
    fixed.update(tuple(sorted(e)) for e in itertools.combinations(small, 2))
    fixed.update((n, full) for n in N)

    solver = z3.Solver()
    for size in range(1, order + 1):
        for subset in itertools.combinations(small, size):
            contacts = [
                z3.If(z3.Or(*(variables[(n, x)] for x in subset)), 1, 0)
                for n in N
            ]
            solver.add(z3.Sum(contacts) + order - size >= 7)

    for bags_json, required_json in archive["models"]:
        bags = [set(bag) for bag in bags_json]
        required = {tuple(edge) for edge in required_json}
        assert len(bags) == 6 and all(bags)
        assert all(bag <= vertices and bag & set(N) for bag in bags)
        assert all(bags[i].isdisjoint(bags[j])
                   for i, j in itertools.combinations(range(6), 2))
        assert required and required <= variable_edges

        graph = nx.Graph()
        graph.add_nodes_from(vertices)
        graph.add_edges_from(fixed | required)
        assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
        assert all(any(graph.has_edge(x, y) for x in bags[i] for y in bags[j])
                   for i, j in itertools.combinations(range(6), 2))

        solver.add(z3.Or(*(z3.Not(variables[edge]) for edge in required)))

    assert solver.check() == z3.unsat
    print(f"verified K{order} exterior with {len(archive['models'])} model clauses")


if __name__ == "__main__":
    verify(2)
    verify(3)
    verify(4)
