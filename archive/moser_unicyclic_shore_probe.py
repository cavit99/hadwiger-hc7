#!/usr/bin/env python3
"""Explore all six-vertex unicyclic shore quotients over the Moser boundary."""

import json

import networkx as nx
import z3

from moser_cycle_shore_probe import N, SHORES, V, M, VARIABLE, k6_model, variable_witness


def unicyclic_types():
    seen = set()
    result = []
    for graph in nx.graph_atlas_g():
        if len(graph) != 6 or graph.number_of_edges() != 6 or not nx.is_connected(graph):
            continue
        code = nx.to_graph6_bytes(graph, header=False).decode().strip()
        if code in seen:
            continue
        seen.add(code)
        result.append((code, tuple(sorted(tuple(sorted(e)) for e in graph.edges()))))
    return result


def solve_case(code, quotient_edges, limit=100000, use_cut_constraints=False):
    fixed_shores = {
        tuple(sorted((SHORES[a], SHORES[b]))) for a, b in quotient_edges
    }
    fixed = M | fixed_shores
    degrees = {
        i: sum(i in edge for edge in quotient_edges) for i in range(6)
    }
    variables = {edge: z3.Bool(f"e_{edge[0]}_{edge[1]}") for edge in VARIABLE}
    solver = z3.Solver()
    certificate = []
    for i, shore in enumerate(SHORES):
        solver.add(z3.Sum([variables[(n, shore)] for n in N]) >= 7 - degrees[i])
    for n in N:
        solver.add(z3.Or([variables[(n, shore)] for shore in SHORES]))
    if use_cut_constraints:
        for mask in range(1, (1 << 6) - 1):
            side = {i for i in range(6) if mask >> i & 1}
            cut_size = sum((a in side) != (b in side) for a, b in quotient_edges)
            lower_bound = max(0, 7 - cut_size)
            if lower_bound:
                solver.add(z3.Sum([
                    z3.If(z3.Or([
                        variables[(n, SHORES[i])] for i in side
                    ]), 1, 0)
                    for n in N
                ]) >= lower_bound)

    for iteration in range(limit):
        status = solver.check()
        if status == z3.unsat:
            return {
                "code": code,
                "shore_edges": [list(e) for e in quotient_edges],
                "degrees": [degrees[i] for i in range(6)],
                "status": "unsat",
                "cut_constraints": use_cut_constraints,
                "models": certificate,
            }
        assert status == z3.sat
        assignment = solver.model()
        chosen = {
            edge for edge, variable in variables.items()
            if z3.is_true(assignment.eval(variable, model_completion=True))
        }
        graph = nx.Graph()
        graph.add_nodes_from(V)
        graph.add_edges_from(fixed | chosen)
        model = k6_model(graph)
        if model is None:
            return {
                "code": code,
                "shore_edges": [list(e) for e in quotient_edges],
                "degrees": [degrees[i] for i in range(6)],
                "status": "counterexample",
                "cut_constraints": use_cut_constraints,
                "defects": {
                    str(i): [n for n in N if (n, SHORES[i]) not in chosen]
                    for i in range(6)
                },
                "models": certificate,
            }
        witness = variable_witness(graph, model)
        if not witness:
            raise AssertionError("unexpected fixed N-meeting model")
        certificate.append({
            "bags": [[i for i in V if mask >> i & 1] for mask in model],
            "edges": [list(edge) for edge in sorted(witness)],
        })
        solver.add(z3.Or([z3.Not(variables[edge]) for edge in witness]))
    raise RuntimeError("iteration limit")


def main():
    archive = {"format": 1, "cases": []}
    for number, (code, edges) in enumerate(unicyclic_types()):
        result = solve_case(code, edges)
        archive["cases"].append(result)
        print(number, code, result["degrees"], result["status"], len(result["models"]), flush=True)
        if result["status"] == "counterexample":
            print(result["defects"], flush=True)
    with open("moser_unicyclic_shore_certificate.json", "w", encoding="utf-8") as out:
        json.dump(archive, out, indent=2)


if __name__ == "__main__":
    main()
