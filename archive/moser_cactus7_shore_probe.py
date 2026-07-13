#!/usr/bin/env python3
"""CEGIS certificates for the two seven-shore tricyclic cactus quotients."""

import itertools
import json
import sys

import networkx as nx
import z3


N = tuple(range(7))
SHORES = tuple(range(7, 14))
V = tuple(range(14))
M = {
    tuple(sorted(e))
    for e in (
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 6), (2, 6),
        (3, 4), (3, 5), (4, 5), (5, 6),
    )
}
VARIABLE = tuple((n, shore) for shore in SHORES for n in N)


def cactus_types():
    friendship = nx.Graph()
    friendship.add_nodes_from(range(7))
    friendship.add_edges_from(
        [(0, x) for x in range(1, 7)] + [(1, 2), (3, 4), (5, 6)]
    )
    chain = nx.Graph()
    chain.add_nodes_from(range(7))
    for triangle in ((0, 1, 2), (2, 3, 4), (4, 5, 6)):
        chain.add_edges_from(itertools.combinations(triangle, 2))
    result = []
    for name, graph in (("friendship", friendship), ("chain", chain)):
        result.append((
            name,
            nx.to_graph6_bytes(graph, header=False).decode().strip(),
            tuple(sorted(tuple(sorted(e)) for e in graph.edges())),
        ))
    return tuple(result)


def k6_model(graph):
    adjacency = [sum(1 << j for j in graph.neighbors(i)) for i in V]
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

    boundary = (1 << 7) - 1
    for omitted in N:
        roots = tuple(x for x in N if x != omitted)
        selected = boundary ^ (1 << omitted)
        candidates = {
            root: [mask for mask in connected if mask & selected == 1 << root]
            for root in roots
        }
        order = tuple(sorted(roots, key=lambda r: len(candidates[r])))

        def rec(position, chosen, used):
            if position == 6:
                return chosen
            root = order[position]
            for bag in candidates[root]:
                if bag & used:
                    continue
                if any(not (neighbour_union[bag] & old) for old in chosen):
                    continue
                answer = rec(position + 1, chosen + [bag], used | bag)
                if answer is not None:
                    return answer
            return None

        answer = rec(0, [], 0)
        if answer is not None:
            return answer
    return None


def variable_witness(graph, model):
    optional = set(VARIABLE)
    required = set()
    bags = [[i for i in V if mask >> i & 1] for mask in model]
    for bag in bags:
        tree = nx.minimum_spanning_tree(graph.subgraph(bag))
        required.update(
            tuple(sorted(e)) for e in tree.edges()
            if tuple(sorted(e)) in optional
        )
    for left, right in itertools.combinations(bags, 2):
        cross = [
            tuple(sorted((x, y))) for x in left for y in right
            if graph.has_edge(x, y)
        ]
        fixed = next((e for e in cross if e not in optional), None)
        if fixed is None:
            required.add(cross[0])
    return required


def solve(index, limit=200000):
    name, code, quotient = cactus_types()[index]
    fixed_shores = {
        tuple(sorted((SHORES[a], SHORES[b]))) for a, b in quotient
    }
    fixed = M | fixed_shores
    variables = {edge: z3.Bool(f"e_{edge[0]}_{edge[1]}") for edge in VARIABLE}
    solver = z3.Solver()

    for mask in range(1, (1 << 7) - 1):
        side = {i for i in range(7) if mask >> i & 1}
        cut_size = sum((a in side) != (b in side) for a, b in quotient)
        lower = max(0, 7 - cut_size)
        if lower:
            solver.add(z3.Sum([
                z3.If(z3.Or([variables[(n, SHORES[i])] for i in side]), 1, 0)
                for n in N
            ]) >= lower)
    for n in N:
        solver.add(z3.Or([variables[(n, shore)] for shore in SHORES]))

    certificate = []
    for iteration in range(limit):
        status = solver.check()
        if status == z3.unsat:
            archive = {
                "format": 1,
                "name": name,
                "code": code,
                "shore_edges": [list(e) for e in quotient],
                "models": certificate,
            }
            with open(f"moser_cactus7_{name}_certificate.json", "w",
                      encoding="utf-8") as target:
                json.dump(archive, target, indent=2)
            print(name, "UNSAT", len(certificate), flush=True)
            return True
        assignment = solver.model()
        chosen = {
            edge for edge, var in variables.items()
            if z3.is_true(assignment.eval(var, model_completion=True))
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
            print(name, "COUNTEREXAMPLE", defects, flush=True)
            return False
        required = variable_witness(graph, model)
        if not required:
            print(name, "FIXED MODEL", model, flush=True)
            return True
        certificate.append({
            "bags": [[i for i in V if mask >> i & 1] for mask in model],
            "edges": [list(e) for e in sorted(required)],
        })
        solver.add(z3.Or([z3.Not(variables[e]) for e in required]))
        if iteration and iteration % 500 == 0:
            print(name, iteration, flush=True)
    raise RuntimeError("iteration limit")


if __name__ == "__main__":
    raise SystemExit(0 if solve(int(sys.argv[1])) else 1)
