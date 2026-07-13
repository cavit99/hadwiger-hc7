#!/usr/bin/env python3
"""Independently replay and verify ``moser_c4_certificate.json``."""

import itertools
import json

import networkx as nx
import z3

N = tuple(range(7))
V = tuple(range(12))
v = 7
C = tuple(range(8, 12))
M = {
    tuple(sorted(e))
    for e in ((0,1),(0,2),(0,3),(0,4),(1,2),(1,6),(2,6),(3,4),(3,5),(4,5),(5,6))
}
VARIABLE = tuple((u, x) for u in N for x in C)


def adjacent(g, a, b):
    return any(g.has_edge(x, y) for x in a for y in b)


def main():
    with open("moser_c4_certificate.json", encoding="utf-8") as handle:
        archive = json.load(handle)
    assert archive["format"] == 1
    assert len(archive["cases"]) == 6
    assert {case["case"] for case in archive["cases"]} == set(range(6))

    atlas_types = [
        graph for graph in nx.graph_atlas_g()
        if len(graph) == 4 and nx.is_connected(graph)
    ]
    assert len(atlas_types) == 6
    matched_types = set()

    for case in archive["cases"]:
        assert case["status"] == "unsat"
        c_edges = {tuple(edge) for edge in case["c_edges"]}
        c_graph = nx.Graph()
        c_graph.add_nodes_from(range(4))
        c_graph.add_edges_from((x - 8, y - 8) for x, y in c_edges)
        matches = [i for i, graph in enumerate(atlas_types) if nx.is_isomorphic(c_graph, graph)]
        assert len(matches) == 1
        matched_types.add(matches[0])
        fixed = set(M) | {(v, u) for u in N} | c_edges
        variable = {e: z3.Bool(f"c{case['case']}_{e[0]}_{e[1]}") for e in VARIABLE}
        solver = z3.Solver()

        for u in N:
            fixed_degree = sum(u in e for e in fixed)
            solver.add(z3.Sum([variable[(u, x)] for x in C]) + fixed_degree >= 7)
            solver.add(z3.Or([variable[(u, x)] for x in C]))
        for x in C:
            fixed_degree = sum(x in e for e in fixed)
            solver.add(z3.Sum([variable[(u, x)] for u in N]) + fixed_degree >= 7)

        for item in case["certificate"]:
            edges = {tuple(edge) for edge in item["edges"]}
            assert edges <= set(VARIABLE)
            if item["kind"] == "connectivity":
                cut = set(item["cut"])
                components = [set(block) for block in item["components"]]
                assert cut <= set(V)
                assert len(cut) <= 6
                assert len(components) >= 2
                assert set().union(*components) == set(V) - cut
                assert sum(map(len, components)) == len(set(V) - cut)
                cross_variables = {
                    e for e in VARIABLE
                    if e[0] not in cut and e[1] not in cut
                    and any(e[0] in a and e[1] in b or e[1] in a and e[0] in b
                            for a, b in itertools.combinations(components, 2))
                }
                assert edges == cross_variables
                assert not any(
                    x not in cut and y not in cut
                    and any(x in a and y in b or y in a and x in b
                            for a, b in itertools.combinations(components, 2))
                    for x, y in fixed
                )
                solver.add(z3.Or([variable[e] for e in edges]))
            elif item["kind"] == "minor":
                bags = [set(bag) for bag in item["bags"]]
                assert len(bags) == 7
                assert all(bag and bag <= set(V) for bag in bags)
                assert edges
                assert sum(map(len, bags)) == len(set().union(*bags))
                witness_graph = nx.Graph()
                witness_graph.add_nodes_from(V)
                witness_graph.add_edges_from(fixed | edges)
                assert all(nx.is_connected(witness_graph.subgraph(bag)) for bag in bags)
                assert all(adjacent(witness_graph, a, b) for a, b in itertools.combinations(bags, 2))
                solver.add(z3.Or([z3.Not(variable[e]) for e in edges]))
            else:
                raise AssertionError(item["kind"])

        assert solver.check() == z3.unsat
        print("verified", case["case"], len(case["certificate"]), "clauses")

    assert matched_types == set(range(6))


if __name__ == "__main__":
    main()
