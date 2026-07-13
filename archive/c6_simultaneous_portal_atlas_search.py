#!/usr/bin/env python3
"""Adversarial atlas search for the simultaneous C6 portal theorem.

Unlike the singleton search, portal classes may overlap arbitrarily.  Each
fixed two-connected atlas host is decorated with six nonempty portal sets
and a seventh z-contact set.  We impose an SDR, all three antipodal
nonlinkages, two owned opposite frame pairs, and the optimistic local
minimum-degree-seven inequalities.  A satisfying host shows which further
criticality hypothesis a uniform theorem must retain.
"""

from __future__ import annotations

import itertools

import networkx as nx
import z3


def connected_masks(graph: nx.Graph) -> tuple[int, ...]:
    vertices = tuple(graph)
    return tuple(
        mask
        for mask in range(1, 1 << len(vertices))
        if nx.is_connected(
            graph.subgraph(vertices[i] for i in range(len(vertices)) if mask >> i & 1)
        )
    )


def solve_host(graph: nx.Graph, owned_pairs: tuple[int, int]):
    vertices = tuple(graph)
    n = len(vertices)
    masks = connected_masks(graph)
    disjoint = tuple((a, b) for a in masks for b in masks if not a & b)
    p = [[z3.Bool(f"p_{i}_{x}") for x in range(n)] for i in range(6)]
    z = [z3.Bool(f"z_{x}") for x in range(n)]
    representatives = [z3.Int(f"r_{i}") for i in range(6)]
    solver = z3.Solver()
    for i in range(6):
        solver.add(representatives[i] >= 0, representatives[i] < n)
        solver.add(
            z3.Or(
                *[z3.And(representatives[i] == x, p[i][x]) for x in range(n)]
            )
        )
    solver.add(z3.Distinct(*representatives))
    solver.add(z3.Or(*z))

    for x, vertex in enumerate(vertices):
        boundary_degree = z3.Sum(
            *[z3.If(p[i][x], 1, 0) for i in range(6)],
            z3.If(z[x], 1, 0),
        )
        solver.add(graph.degree(vertex) + boundary_degree >= 7)

    meets_cache = {}
    carries_cache = {}
    linkage_cache = {}

    def meets(label: int, mask: int):
        key = (label, mask)
        if key not in meets_cache:
            meets_cache[key] = z3.Or(
                *[p[label][x] for x in range(n) if mask >> x & 1]
            )
        return meets_cache[key]

    def carries(edge: tuple[int, int], mask: int):
        key = (edge[0], mask)
        if key not in carries_cache:
            carries_cache[key] = z3.And(
                meets(edge[0], mask), meets(edge[1], mask)
            )
        return carries_cache[key]

    def linkage(first: int, second: int):
        key = tuple(sorted((first, second)))
        if key in linkage_cache:
            return linkage_cache[key]
        e1 = (first, (first + 1) % 6)
        e2 = (second, (second + 1) % 6)
        linkage_cache[key] = z3.Or(
            *[
                z3.And(carries(e1, a), carries(e2, b))
                for a, b in disjoint
            ]
        )
        return linkage_cache[key]

    for i in range(3):
        solver.add(z3.Not(linkage(i, i + 3)))
    for pair in owned_pairs:
        for frame in (pair, pair + 3):
            solver.add(linkage((frame - 2) % 6, (frame + 2) % 6))

    if solver.check() != z3.sat:
        return None
    model = solver.model()
    rows = {
        i: tuple(vertices[x] for x in range(n) if z3.is_true(model.eval(p[i][x])))
        for i in range(6)
    }
    zrow = tuple(vertices[x] for x in range(n) if z3.is_true(model.eval(z[x])))
    return rows, zrow


def main() -> None:
    tested = 0
    for graph in nx.graph_atlas_g():
        if len(graph) != 7 or nx.node_connectivity(graph) < 2:
            continue
        for owned_pairs in itertools.combinations(range(3), 2):
            tested += 1
            result = solve_host(graph, owned_pairs)
            if result is not None:
                print("SAT host order", len(graph), "owned", owned_pairs)
                print("edges", sorted(graph.edges()))
                print("portals", result[0])
                print("z", result[1])
                return
    print("UNSAT on atlas order 7; host/pair instances", tested)


if __name__ == "__main__":
    main()
