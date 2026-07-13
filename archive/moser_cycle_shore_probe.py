#!/usr/bin/env python3
"""Lazy certificate for the six two-defect shores on a cycle."""

import itertools
import json

import networkx as nx
import z3


N = tuple(range(7))
SHORES = tuple(range(7, 13))
V = tuple(range(13))
M = {
    tuple(sorted(e))
    for e in (
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 6), (2, 6),
        (3, 4), (3, 5), (4, 5), (5, 6),
    )
}
CYCLE = {
    tuple(sorted((SHORES[i], SHORES[(i + 1) % 6])))
    for i in range(6)
}
VARIABLE = tuple((n, shore) for shore in SHORES for n in N)


def k6_model(g):
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
    connected.sort(key=lambda mask: (mask.bit_count(), mask))

    boundary_mask = (1 << 7) - 1
    for omitted_root in N:
        roots = tuple(x for x in N if x != omitted_root)
        root_mask = boundary_mask ^ (1 << omitted_root)
        candidates = {
            root: [
                mask for mask in connected
                if mask & root_mask == 1 << root
            ]
            for root in roots
        }
        order = tuple(sorted(roots, key=lambda root: len(candidates[root])))

        def rec(index, chosen, used):
            if index == len(order):
                return chosen
            root = order[index]
            for bag in candidates[root]:
                if bag & used:
                    continue
                if any(not neighbour_union[bag] & old for old in chosen):
                    continue
                result = rec(index + 1, chosen + [bag], used | bag)
                if result is not None:
                    return result
            return None

        result = rec(0, [], 0)
        if result is not None:
            return result
    return None


def variable_witness(g, model):
    variable = set(VARIABLE)
    required = set()
    bags = [[i for i in V if mask >> i & 1] for mask in model]
    for bag in bags:
        tree = nx.minimum_spanning_tree(g.subgraph(bag))
        required.update(
            tuple(sorted(edge)) for edge in tree.edges()
            if tuple(sorted(edge)) in variable
        )
    for left, right in itertools.combinations(bags, 2):
        edges = [
            tuple(sorted((x, y))) for x in left for y in right
            if g.has_edge(x, y)
        ]
        fixed = next((edge for edge in edges if edge not in variable), None)
        required.add(fixed if fixed is not None else edges[0])
    return required & variable


def main():
    fixed = M | CYCLE
    variables = {edge: z3.Bool(f"e_{edge[0]}_{edge[1]}") for edge in VARIABLE}
    solver = z3.Solver()
    certificate = []
    for shore in SHORES:
        solver.add(z3.Sum([variables[(n, shore)] for n in N]) >= 5)
    for n in N:
        solver.add(z3.Or([variables[(n, shore)] for shore in SHORES]))

    for iteration in range(100000):
        if iteration and iteration % 100 == 0:
            print("iteration", iteration, flush=True)
        status = solver.check()
        if status == z3.unsat:
            print("unsat", iteration)
            with open("moser_cycle_shore_certificate.json", "w", encoding="utf-8") as out:
                json.dump({"format": 1, "models": certificate}, out, indent=2)
            return
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
            defects = {
                shore: [n for n in N if (n, shore) not in chosen]
                for shore in SHORES
            }
            print("counterexample", defects)
            return
        witness = variable_witness(graph, model)
        bags = [[i for i in V if mask >> i & 1] for mask in model]
        if not witness:
            print("fixed model", bags)
            return
        certificate.append({
            "bags": bags,
            "edges": [list(edge) for edge in sorted(witness)],
        })
        solver.add(z3.Or([z3.Not(variables[edge]) for edge in witness]))

    print("iteration limit")


if __name__ == "__main__":
    main()
