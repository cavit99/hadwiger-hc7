#!/usr/bin/env python3
"""Probe K2/K3 exterior components opposite one full Moser shore."""

import itertools
import json
import sys

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


def k6_model(graph, vertices):
    adjacency = [sum(1 << j for j in graph.neighbors(i)) for i in vertices]
    neighbour_union = [0] * (1 << len(vertices))
    connected = []
    for mask in range(1, 1 << len(vertices)):
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

    boundary = (1 << 7) - 1
    for omitted in N:
        roots = tuple(x for x in N if x != omitted)
        root_mask = boundary ^ (1 << omitted)
        candidates = {
            root: [mask for mask in connected if mask & root_mask == 1 << root]
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
                if any(not (neighbour_union[bag] & old) for old in chosen):
                    continue
                answer = rec(index + 1, chosen + [bag], used | bag)
                if answer is not None:
                    return answer
            return None

        answer = rec(0, [], 0)
        if answer is not None:
            return answer
    return None


def solve(order):
    small = tuple(range(7, 7 + order))
    full = 7 + order
    vertices = tuple(range(full + 1))
    variable_edges = tuple((n, x) for x in small for n in N)
    variables = {edge: z3.Bool(f"e_{edge[0]}_{edge[1]}") for edge in variable_edges}

    fixed = set(M)
    fixed.update(itertools.combinations(small, 2))
    fixed.update((n, full) for n in N)

    solver = z3.Solver()
    # For every nonempty vertex set S in the clique component, seven-
    # connectivity gives |N_N(S)| + |C-S| >= 7.
    for size in range(1, order + 1):
        for subset in itertools.combinations(small, size):
            contacts = []
            for n in N:
                contact = z3.Or(*(variables[(n, x)] for x in subset))
                contacts.append(z3.If(contact, 1, 0))
            solver.add(z3.Sum(contacts) + order - size >= 7)

    certificate = []
    for iteration in range(100000):
        if solver.check() == z3.unsat:
            with open(f"moser_two_component_k{order}_certificate.json", "w",
                      encoding="utf-8") as target:
                json.dump({"format": 1, "order": order,
                           "models": certificate}, target, indent=2)
            print("UNSAT", order, "models", len(certificate))
            return True
        assignment = solver.model()
        chosen = {
            edge for edge, var in variables.items()
            if z3.is_true(assignment.eval(var, model_completion=True))
        }
        graph = nx.Graph()
        graph.add_nodes_from(vertices)
        graph.add_edges_from(fixed | chosen)
        model = k6_model(graph, vertices)
        if model is None:
            defects = {
                x: [n for n in N if (n, x) not in chosen] for x in small
            }
            print("COUNTEREXAMPLE", order, defects)
            return False

        bags = [[i for i in vertices if mask >> i & 1] for mask in model]
        required = set()
        for bag in bags:
            tree = nx.minimum_spanning_tree(graph.subgraph(bag))
            required.update(tuple(sorted(e)) for e in tree.edges()
                            if tuple(sorted(e)) in variables)
        for left, right in itertools.combinations(bags, 2):
            cross = [tuple(sorted((x, y))) for x in left for y in right
                     if graph.has_edge(x, y)]
            fixed_cross = next((e for e in cross if e not in variables), None)
            if fixed_cross is None:
                required.add(cross[0])
        if not required:
            print("FIXED MODEL", order, bags)
            return True
        certificate.append((bags, sorted(required)))
        solver.add(z3.Or(*(z3.Not(variables[e]) for e in required)))
    raise RuntimeError("iteration limit")


if __name__ == "__main__":
    raise SystemExit(0 if solve(int(sys.argv[1])) else 1)
