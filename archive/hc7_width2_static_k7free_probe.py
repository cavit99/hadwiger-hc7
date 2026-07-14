#!/usr/bin/env python3
"""Archived finite probe for a K7-minor-free width-two split obstruction.

This was a falsification probe, not a proof artifact.  The boundary is the
paired-state subdivided claw from the audited width-two frontier.  The rich
shore consists of two adjacent boundary-universal vertices.  Random portal
sets are put on a five-wheel thin shore.  Candidates must be exactly
7-connected, satisfy the packet vector (1,2), and have no disjoint carriers
for the two bipartition duties.  Z3 then tests the K7-minor condition exactly.
"""

from __future__ import annotations

from itertools import combinations
import random

import networkx as nx
from z3 import And, Bool, If, Implies, Int, Not, Or, Solver, Sum, is_true, sat


S = ("c", "a1", "t1", "a2", "t2", "a3", "t3")
A = frozenset(("c", "t1", "t2", "t3"))
B = frozenset(("a1", "a2", "a3"))
L = tuple(("l", i) for i in range(5))
R = (("p",), ("q",))


def connected_subsets(graph: nx.Graph, vertices):
    vertices = tuple(vertices)
    for mask in range(1, 1 << len(vertices)):
        subset = frozenset(vertices[i] for i in range(len(vertices)) if mask >> i & 1)
        if nx.is_connected(graph.subgraph(subset)):
            yield subset


def funds(graph: nx.Graph, carrier, duty) -> bool:
    return all(any(graph.has_edge(x, s) for x in carrier) for s in duty)


def packet_number(graph: nx.Graph, shore) -> int:
    packets = [x for x in connected_subsets(graph, shore) if funds(graph, x, S)]
    if not packets:
        return 0
    if not any(x.isdisjoint(y) for x, y in combinations(packets, 2)):
        return 1
    # The probe only asks whether the thin packet number is one.  Returning
    # two is sufficient once a disjoint pair exists.
    return 2


def k7_model(graph: nx.Graph):
    vertices = tuple(graph)
    index = {v: i for i, v in enumerate(vertices)}
    edges = tuple((index[u], index[v]) for u, v in graph.edges)
    neighbours = [[] for _ in vertices]
    for u, v in edges:
        neighbours[u].append(v)
        neighbours[v].append(u)
    belongs = [[Bool(f"x_{v}_{b}") for b in range(7)] for v in range(len(vertices))]
    root = [[Bool(f"r_{v}_{b}") for b in range(7)] for v in range(len(vertices))]
    depth = [[Int(f"d_{v}_{b}") for b in range(7)] for v in range(len(vertices))]
    solver = Solver()
    solver.set(timeout=15_000)
    for v in range(len(vertices)):
        solver.add(Sum([If(belongs[v][b], 1, 0) for b in range(7)]) <= 1)
    for b in range(7):
        solver.add(Sum([If(root[v][b], 1, 0) for v in range(len(vertices))]) == 1)
        for v in range(len(vertices)):
            solver.add(depth[v][b] >= 0, depth[v][b] < len(vertices))
            solver.add(Implies(root[v][b], And(belongs[v][b], depth[v][b] == 0)))
            solver.add(Implies(
                And(belongs[v][b], Not(root[v][b])),
                And(depth[v][b] >= 1, Or([
                    And(belongs[w][b], depth[w][b] < depth[v][b])
                    for w in neighbours[v]
                ])),
            ))
    for b1, b2 in combinations(range(7), 2):
        solver.add(Or([
            Or(And(belongs[u][b1], belongs[v][b2]),
               And(belongs[u][b2], belongs[v][b1]))
            for u, v in edges
        ]))
    if solver.check() != sat:
        return None
    model = solver.model()
    return [[vertices[v] for v in range(len(vertices))
             if is_true(model.eval(belongs[v][b]))] for b in range(7)]


def build(rows):
    graph = nx.Graph()
    graph.add_nodes_from(S + L + R)
    graph.add_edges_from((
        ("c", "a1"), ("c", "a2"), ("c", "a3"),
        ("a1", "t2"), ("t1", "a3"), ("a2", "t3"),
    ))
    graph.add_edges_from((L[i], L[(i + 1) % 4]) for i in range(4))
    graph.add_edges_from((L[4], L[i]) for i in range(4))
    for vertex, row in zip(L, rows):
        graph.add_edges_from((vertex, s) for s in row)
    graph.add_edge(*R)
    for r in R:
        graph.add_edges_from((r, s) for s in S)
    return graph


def main():
    # Start from the verified connectivity-only barrier and exhaust all of
    # its portal supergraphs after replacing the rich K6 by p-q.  This is a
    # monotone 13-edge cube, small enough to check without sampling.
    base_rows = [
        frozenset(("c", "a1", "t1", "t2", "a2")),
        frozenset(("c", "a1", "t1", "a2", "t3")),
        frozenset(("c", "a1", "t1", "t3", "a3")),
        frozenset(("c", "a1", "t1", "a3")),
        frozenset(("c", "a1", "t1")),
    ]
    optional = [(i, s) for i, row in enumerate(base_rows) for s in S if s not in row]
    static = kappa7 = k7free = 0
    for mask in range(1 << len(optional)):
        rows = [set(row) for row in base_rows]
        for bit, (i, s) in enumerate(optional):
            if mask >> bit & 1:
                rows[i].add(s)
        rows = tuple(frozenset(row) for row in rows)
        graph = build(rows)
        carriers = list(connected_subsets(graph, L))
        if packet_number(graph, L) != 1:
            continue
        a_carriers = [x for x in carriers if funds(graph, x, A)]
        b_carriers = [x for x in carriers if funds(graph, x, B)]
        if any(x.isdisjoint(y) for x in a_carriers for y in b_carriers):
            continue
        static += 1
        if min(dict(graph.degree()).values()) < 7 or nx.node_connectivity(graph) != 7:
            continue
        kappa7 += 1
        model = k7_model(graph)
        if model is None:
            k7free += 1
            print("K7_FREE", rows)
            print("edges", graph.number_of_edges(), "kappa", nx.node_connectivity(graph))
            return
        if kappa7 <= 10:
            print("K7", rows, model)
    print("DONE", "cube", 1 << len(optional), "static", static,
          "kappa7", kappa7, "k7free", k7free)


if __name__ == "__main__":
    main()
