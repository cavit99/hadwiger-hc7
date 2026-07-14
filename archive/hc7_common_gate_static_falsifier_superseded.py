#!/usr/bin/env python3
"""Probe common-gate width-two locks for an exact K7^vee obstruction.

This is an adversarial search script.  It is not a theorem certificate.
"""

from __future__ import annotations

from itertools import combinations
import random

import networkx as nx
from z3 import And, Bool, If, Implies, Int, Not, Or, Solver, Sum, is_true, sat


S = ("c", "a1", "t1", "a2", "t2", "a3", "t3")
A = frozenset(("c", "t1", "t2", "t3"))
B = frozenset(("a1", "a2", "a3"))
H_EDGES = (
    ("c", "a1"), ("c", "a2"), ("c", "a3"),
    ("a1", "t2"), ("t1", "a3"), ("a2", "t3"),
)


def alpha(graph: nx.Graph) -> int:
    return max((len(c) for c in nx.find_cliques(nx.complement(graph))), default=0)


def connected_subsets(graph: nx.Graph, vertices):
    vertices = tuple(vertices)
    for mask in range(1, 1 << len(vertices)):
        subset = frozenset(vertices[i] for i in range(len(vertices)) if mask >> i & 1)
        if nx.is_connected(graph.subgraph(subset)):
            yield subset


def funds(graph: nx.Graph, carrier, duty) -> bool:
    return all(any(graph.has_edge(x, s) for x in carrier) for s in duty)


def build(thin: nx.Graph, rows) -> tuple[nx.Graph, tuple]:
    names = tuple(("l", i) for i in range(len(thin)))
    relabelled = nx.relabel_nodes(thin, {i: names[i] for i in range(len(thin))})
    p, q = ("p",), ("q",)
    graph = nx.Graph()
    graph.add_nodes_from(S + names + (p, q))
    graph.add_edges_from(H_EDGES)
    graph.add_edges_from(relabelled.edges)
    for x, row in zip(names, rows):
        graph.add_edges_from((x, s) for s in row)
    graph.add_edge(p, q)
    for packet in (p, q):
        graph.add_edges_from((packet, s) for s in S)
    return graph, names


def k7vee_model(graph: nx.Graph):
    """Exact Z3 model: bags 1..6 form K6; bag 0 meets at least four."""
    vertices = tuple(graph)
    index = {v: i for i, v in enumerate(vertices)}
    edges = tuple((index[u], index[v]) for u, v in graph.edges)
    neighbours = [[] for _ in vertices]
    for u, v in edges:
        neighbours[u].append(v)
        neighbours[v].append(u)

    belongs = [[Bool(f"x_{v}_{b}") for b in range(7)] for v in range(len(vertices))]
    roots = [[Bool(f"r_{v}_{b}") for b in range(7)] for v in range(len(vertices))]
    depth = [[Int(f"d_{v}_{b}") for b in range(7)] for v in range(len(vertices))]
    solver = Solver()
    solver.set(timeout=30_000)
    for v in range(len(vertices)):
        solver.add(Sum([If(belongs[v][b], 1, 0) for b in range(7)]) <= 1)
    for b in range(7):
        solver.add(Sum([If(roots[v][b], 1, 0) for v in range(len(vertices))]) == 1)
        for v in range(len(vertices)):
            solver.add(depth[v][b] >= 0, depth[v][b] < len(vertices))
            solver.add(Implies(roots[v][b], And(belongs[v][b], depth[v][b] == 0)))
            solver.add(Implies(
                And(belongs[v][b], Not(roots[v][b])),
                And(depth[v][b] >= 1, Or([
                    And(belongs[w][b], depth[w][b] < depth[v][b])
                    for w in neighbours[v]
                ])),
            ))

    def adjacent(left, right):
        return Or([
            Or(And(belongs[u][left], belongs[v][right]),
               And(belongs[u][right], belongs[v][left]))
            for u, v in edges
        ])

    for left, right in combinations(range(1, 7), 2):
        solver.add(adjacent(left, right))
    solver.add(Sum([If(adjacent(0, b), 1, 0) for b in range(1, 7)]) >= 4)
    if solver.check() != sat:
        return None
    model = solver.model()
    return [[vertices[v] for v in range(len(vertices))
             if is_true(model.eval(belongs[v][b]))] for b in range(7)]


def candidate_graphs():
    for n in range(5, 13):
        cycle = nx.cycle_graph(n)
        square = nx.Graph(cycle)
        square.add_edges_from((i, (i + 2) % n) for i in range(n))
        if min(dict(square.degree()).values()) >= 4:
            yield f"cycle_square_{n}", square
    yield "octahedron", nx.complete_multipartite_graph(2, 2, 2)
    yield "K44", nx.complete_bipartite_graph(4, 4)
    yield "icosahedron", nx.icosahedral_graph()
    rng = random.Random(934)
    for n in (8, 9, 10, 11, 12):
        if n % 2:
            continue
        for i in range(8):
            yield f"regular4_{n}_{i}", nx.random_regular_graph(4, n, seed=rng.randrange(1 << 30))


def main():
    common = frozenset(("c", "a1", "a2"))
    for name, thin in candidate_graphs():
        if nx.node_connectivity(thin) < 3 or min(dict(thin.degree()).values()) < 4:
            continue
        rows = (frozenset(S),) + (common,) * (len(thin) - 1)
        graph, L = build(thin, rows)
        if any(alpha(graph.subgraph(graph[x])) > graph.degree(x) - 5 for x in L):
            continue
        carriers = list(connected_subsets(graph, L))
        a_carriers = [x for x in carriers if funds(graph, x, A)]
        b_carriers = [x for x in carriers if funds(graph, x, B)]
        assert not any(x.isdisjoint(y) for x in a_carriers for y in b_carriers)
        model = k7vee_model(graph)
        print(name, "order", len(L), "model", model, flush=True)
        if model is None:
            print("COUNTEREXAMPLE", name, rows)
            return


if __name__ == "__main__":
    main()
