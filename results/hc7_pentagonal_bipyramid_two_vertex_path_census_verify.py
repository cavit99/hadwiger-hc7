#!/usr/bin/env python3
"""Exact CEGAR census for two-vertex PB path-column expansions."""

from itertools import combinations, permutations
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "active" / "runtime" / "deps"))

import networkx as nx
import z3


LABELS = tuple(range(7))
RIM = tuple(range(2, 7))
PB = {tuple(sorted((p, r))) for p in (0, 1) for r in RIM}
PB.update(tuple(sorted((2+i, 2+((i+1) % 5)))) for i in range(5))
ORDER = {0: (2,3,4,5,6), 1: (2,6,5,4,3)}
for i in range(5):
    ORDER[2+i] = (0, 2+((i+1) % 5), 1, 2+((i-1) % 5))

VERTICES = tuple((x, i) for x in LABELS for i in range(2))
solver = z3.Solver()
edge = {}
for x, y in PB:
    bundle = []
    for i in range(2):
        for j in range(2):
            variable = z3.Bool(f"e_{x}_{i}_{y}_{j}")
            edge[x,i,y,j] = variable
            bundle.append(variable)
    solver.add(z3.Or(*bundle))


def edge_variable(u, v):
    x, i = u
    y, j = v
    if x == y:
        return z3.BoolVal(i != j)
    if x < y:
        return edge[x,i,y,j]
    return edge[y,j,x,i]


def portal(u, outside_label):
    if tuple(sorted((u[0], outside_label))) not in PB:
        return z3.BoolVal(False)
    return z3.Or(edge_variable(u, (outside_label,0)),
                 edge_variable(u, (outside_label,1)))


def path_condition(path, first_label, second_label):
    terms = [portal(path[0], first_label), portal(path[-1], second_label)]
    terms.extend(edge_variable(path[i], path[i+1]) for i in range(len(path)-1))
    return z3.And(*terms)


# Minimum degree at least five.
for x in LABELS:
    for i in range(2):
        incident = []
        for y in ORDER[x]:
            for j in range(2):
                incident.append((edge_variable((x,i), (y,j)), 1))
        # The fixed internal path edge supplies the fifth incident edge.
        solver.add(z3.PbGe(incident, 4))

# Exclude every four-distinct-label alternating internal cut.
for x in LABELS:
    cyclic = ORDER[x]
    for positions in combinations(range(len(cyclic)), 4):
        q = tuple(cyclic[i] for i in positions)
        for first_side in (0, 1):
            second_side = 1-first_side
            solver.add(z3.Not(z3.And(
                portal((x,first_side),q[0]), portal((x,second_side),q[1]),
                portal((x,first_side),q[2]), portal((x,second_side),q[3]),
            )))

# Exclude every adjacent-rim linkage.  Each union has only four vertices,
# so all two disjoint internal simple paths can be listed exactly.
for index in range(5):
    ci, cj = 2+index, 2+((index+1) % 5)
    left, right = 2+((index-1) % 5), 2+((index+2) % 5)
    vertices = ((ci,0),(ci,1),(cj,0),(cj,1))
    paths = []
    for length in range(1, 5):
        paths.extend(permutations(vertices, length))
    for first in paths:
        remaining = tuple(v for v in vertices if v not in first)
        for length in range(1, len(remaining)+1):
            for second in permutations(remaining, length):
                solver.add(z3.Not(z3.And(
                    path_condition(first, 0, 1),
                    path_condition(second, left, right),
                )))


def graph_from_model(model):
    graph = nx.Graph()
    for x in LABELS:
        graph.add_edge((x,0),(x,1))
    for key, variable in edge.items():
        if z3.is_true(model.eval(variable)):
            x,i,y,j = key
            graph.add_edge((x,i),(y,j))
    return graph


def four_colouring(graph):
    check = z3.Solver()
    colour = {v:z3.Int(f"c_{v[0]}_{v[1]}") for v in graph}
    for v in graph:
        check.add(0 <= colour[v], colour[v] < 4)
    for u, v in graph.edges():
        check.add(colour[u] != colour[v])
    if check.check() != z3.sat:
        return None
    model = check.model()
    return {v:model.eval(colour[v]).as_long() for v in graph}


while True:
    status = solver.check()
    if status == z3.unsat:
        print("pentagonal-bipyramid two-vertex path census: PASS")
        break
    if status != z3.sat:
        raise RuntimeError(f"solver returned {status}, not an exact verdict")

    model = solver.model()
    graph = graph_from_model(model)
    if nx.node_connectivity(graph) < 5:
        cut = set(nx.minimum_node_cut(graph))
        remainder = graph.subgraph(set(VERTICES)-cut)
        for component_tuple in nx.connected_components(remainder):
            component = set(component_tuple)
            outside = set(VERTICES)-cut-component
            possible = []
            for u in component:
                for v in outside:
                    if u >= v or u[0] == v[0]:
                        continue
                    if tuple(sorted((u[0],v[0]))) in PB:
                        possible.append(edge_variable(u,v))
            # A five-connected graph must cross this exact bipartition.
            solver.add(z3.Or(*possible) if possible else z3.BoolVal(False))
        continue

    colouring = four_colouring(graph)
    if colouring is None:
        raise AssertionError("five-connected non-four-colourable survivor")

    same_colour_edges = []
    for (x,i,y,j), variable in edge.items():
        if colouring[(x,i)] == colouring[(y,j)]:
            same_colour_edges.append(variable)
    assert same_colour_edges
    # Every graph not coloured by this colouring must select one such edge.
    solver.add(z3.Or(*same_colour_edges))
