#!/usr/bin/env python3
"""Experimental lazy SAT search for a one-component pure-Moser |C|=4 cell."""

import itertools
import json
import sys
import networkx as nx
import z3

N = tuple(range(7))
v = 7
NC = int(sys.argv[1]) if len(sys.argv) > 1 else 4
C = tuple(range(8, 8 + NC))
V = tuple(range(8 + NC))
M = {
    tuple(sorted(e))
    for e in ((0,1),(0,2),(0,3),(0,4),(1,2),(1,6),(2,6),(3,4),(3,5),(4,5),(5,6))
}
VARIABLE = tuple((u, x) for u in N for x in C)


def k_minor_model(g, k=7):
    adjacency = [sum(1 << j for j in g.neighbors(i)) for i in V]
    neighbour_union = [0] * (1 << len(V))
    connected = []
    for mask in range(1, 1 << len(V)):
        low = mask & -mask
        i = low.bit_length() - 1
        neighbour_union[mask] = neighbour_union[mask ^ low] | adjacency[i]
        reached = low
        while True:
            expanded = reached | (neighbour_union[reached] & mask)
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            connected.append(mask)
    connected.sort(key=lambda m: (m.bit_count(), m))

    def adjacent(a, b):
        return not (a & b) and bool(neighbour_union[a] & b)

    def rec(chosen, candidates, used):
        if len(chosen) == k:
            return chosen
        needed = k - len(chosen)
        if len(candidates) < needed:
            return None
        for pos, a in enumerate(candidates):
            if a & used:
                continue
            nxt = [
                b for b in candidates[pos + 1:]
                if not b & (used | a) and adjacent(a, b)
            ]
            if len(nxt) >= needed - 1:
                result = rec(chosen + [a], nxt, used | a)
                if result:
                    return result
        return None

    return rec([], connected, 0)


def model_variable_witness(g, model):
    required = set()
    variable = set(VARIABLE)
    bags = [[i for i in V if mask >> i & 1] for mask in model]
    for bag in bags:
        tree = nx.minimum_spanning_tree(g.subgraph(bag))
        required.update(tuple(sorted(e)) for e in tree.edges() if tuple(sorted(e)) in variable)
    for a, b in itertools.combinations(bags, 2):
        edges = [tuple(sorted((x, y))) for x in a for y in b if g.has_edge(x, y)]
        fixed = next((e for e in edges if e not in variable), None)
        required.add(fixed if fixed is not None else edges[0])
    return required & variable


def solve_for_c(c_edges, limit=20000):
    fixed = set(M) | {(v, u) for u in N} | {tuple(sorted(e)) for e in c_edges}
    variables = {e: z3.Bool(f"x_{e[0]}_{e[1]}") for e in VARIABLE}
    solver = z3.Solver()
    certificate = []

    # Minimum degree seven and full boundary attachment.
    for u in N:
        fixed_degree = sum(u in e for e in fixed)
        solver.add(z3.Sum([variables[(u, x)] for x in C]) + fixed_degree >= 7)
        solver.add(z3.Or([variables[(u, x)] for x in C]))
    for x in C:
        fixed_degree = sum(x in e for e in fixed)
        solver.add(z3.Sum([variables[(u, x)] for u in N]) + fixed_degree >= 7)

    for iteration in range(limit):
        if solver.check() != z3.sat:
            return {"status": "unsat", "iterations": iteration, "certificate": certificate}
        model = solver.model()
        chosen = {e for e, q in variables.items() if z3.is_true(model.eval(q, model_completion=True))}
        g = nx.Graph()
        g.add_nodes_from(V)
        g.add_edges_from(fixed | chosen)

        connectivity = nx.node_connectivity(g)
        if connectivity < 7:
            cut = nx.minimum_node_cut(g)
            components = list(nx.connected_components(nx.subgraph_view(g, filter_node=lambda x: x not in cut)))
            optional = set()
            for a, b in itertools.combinations(components, 2):
                optional.update(
                    e for e in VARIABLE
                    if (e[0] in a and e[1] in b) or (e[1] in a and e[0] in b)
                )
            optional -= chosen
            if not optional:
                return {"status": "connectivity-impossible", "iterations": iteration, "cut": sorted(cut), "certificate": certificate}
            certificate.append({
                "kind": "connectivity",
                "cut": sorted(cut),
                "components": [sorted(component) for component in components],
                "edges": [list(e) for e in sorted(optional)],
            })
            solver.add(z3.Or([variables[e] for e in optional]))
            continue

        km = k_minor_model(g)
        if km is None:
            return {
                "status": "counterarchitecture",
                "iterations": iteration,
                "edges": sorted(chosen),
                "connectivity": connectivity,
                "certificate": certificate,
            }
        witness = model_variable_witness(g, km)
        if not witness:
            return {"status": "fixed-model", "iterations": iteration, "certificate": certificate}
        certificate.append({
            "kind": "minor",
            "bags": [[i for i in V if mask >> i & 1] for mask in km],
            "edges": [list(e) for e in sorted(witness)],
        })
        solver.add(z3.Or([z3.Not(variables[e]) for e in witness]))
    return {"status": "limit", "iterations": limit, "certificate": certificate}


def main():
    types = []
    for graph in nx.graph_atlas_g():
        if len(graph) == NC and nx.is_connected(graph):
            edges = tuple(sorted((a + 8, b + 8) for a, b in graph.edges()))
            if edges not in types:
                types.append(edges)
    assert len(types) == {4: 6, 5: 21}.get(NC, len(types))
    selected = set(map(int, sys.argv[2:])) if len(sys.argv) > 2 else set(range(len(types)))
    assert selected <= set(range(len(types)))
    archive = {"format": 1, "exterior_order": NC, "cases": []}
    for number, edges in enumerate(types):
        if number not in selected:
            continue
        result = solve_for_c(edges)
        archive["cases"].append({
            "case": number,
            "c_edges": [list(e) for e in edges],
            **result,
        })
        summary = {key: value for key, value in result.items() if key != "certificate"}
        print(number, edges, summary)
        if result["status"] == "counterarchitecture":
            break
    suffix = "" if selected == set(range(len(types))) else "_" + "-".join(map(str, sorted(selected)))
    with open(f"moser_c{NC}_certificate{suffix}.json", "w", encoding="utf-8") as handle:
        json.dump(archive, handle, indent=2, sort_keys=True)


if __name__ == "__main__":
    main()
