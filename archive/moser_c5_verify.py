#!/usr/bin/env python3
"""Independently verify all 21 order-five pure-Moser certificates."""

import glob
import itertools
import json

import networkx as nx
import z3

N = tuple(range(7))
V = tuple(range(13))
v = 7
C = tuple(range(8, 13))
M = {
    tuple(sorted(e))
    for e in ((0,1),(0,2),(0,3),(0,4),(1,2),(1,6),(2,6),(3,4),(3,5),(4,5),(5,6))
}
VARIABLE = tuple((u, x) for u in N for x in C)


def adjacent(graph, a, b):
    return any(graph.has_edge(x, y) for x in a for y in b)


def main():
    paths = sorted(glob.glob("moser_c5_certificate_*.json"))
    assert len(paths) == 4, paths
    cases = []
    for path in paths:
        with open(path, encoding="utf-8") as handle:
            archive = json.load(handle)
        assert archive["format"] == 1
        assert archive["exterior_order"] == 5
        cases.extend(archive["cases"])

    assert len(cases) == 21
    assert {case["case"] for case in cases} == set(range(21))

    atlas_types = [
        graph for graph in nx.graph_atlas_g()
        if len(graph) == 5 and nx.is_connected(graph)
    ]
    assert len(atlas_types) == 21
    expected_edges = [
        {tuple(sorted((a + 8, b + 8))) for a, b in graph.edges()}
        for graph in atlas_types
    ]
    matched_types = set()

    for case in sorted(cases, key=lambda item: item["case"]):
        assert case["status"] == "unsat"
        number = case["case"]
        c_edges = {tuple(edge) for edge in case["c_edges"]}
        assert c_edges == expected_edges[number]

        c_graph = nx.Graph()
        c_graph.add_nodes_from(range(5))
        c_graph.add_edges_from((x - 8, y - 8) for x, y in c_edges)
        matches = [i for i, graph in enumerate(atlas_types) if nx.is_isomorphic(c_graph, graph)]
        assert len(matches) == 1
        matched_types.add(matches[0])

        fixed = set(M) | {(v, u) for u in N} | c_edges
        variable = {e: z3.Bool(f"c{number}_{e[0]}_{e[1]}") for e in VARIABLE}
        solver = z3.Solver()

        for u in N:
            fixed_degree = sum(u in edge for edge in fixed)
            solver.add(z3.Sum([variable[(u, x)] for x in C]) + fixed_degree >= 7)
            solver.add(z3.Or([variable[(u, x)] for x in C]))
        for x in C:
            fixed_degree = sum(x in edge for edge in fixed)
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
                    edge for edge in VARIABLE
                    if edge[0] not in cut and edge[1] not in cut
                    and any(
                        edge[0] in a and edge[1] in b
                        or edge[1] in a and edge[0] in b
                        for a, b in itertools.combinations(components, 2)
                    )
                }
                assert edges == cross_variables
                assert not any(
                    x not in cut and y not in cut
                    and any(
                        x in a and y in b or y in a and x in b
                        for a, b in itertools.combinations(components, 2)
                    )
                    for x, y in fixed
                )
                solver.add(z3.Or([variable[edge] for edge in edges]))
            elif item["kind"] == "minor":
                bags = [set(bag) for bag in item["bags"]]
                assert len(bags) == 7
                assert all(bag and bag <= set(V) for bag in bags)
                assert edges
                assert sum(map(len, bags)) == len(set().union(*bags))
                witness = nx.Graph()
                witness.add_nodes_from(V)
                witness.add_edges_from(fixed | edges)
                assert all(nx.is_connected(witness.subgraph(bag)) for bag in bags)
                assert all(adjacent(witness, a, b) for a, b in itertools.combinations(bags, 2))
                solver.add(z3.Or([z3.Not(variable[edge]) for edge in edges]))
            else:
                raise AssertionError(item["kind"])

        assert solver.check() == z3.unsat
        print("verified", number, len(case["certificate"]), "clauses")

    assert matched_types == set(range(21))


if __name__ == "__main__":
    main()
