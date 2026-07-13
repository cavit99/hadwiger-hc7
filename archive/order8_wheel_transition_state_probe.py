#!/usr/bin/env python3
"""Enumerate boundary partitions forced by critical wheel-edge deletions.

This is an invariant finder, not a proof.  It uses the conservative quotient
from the atomic-wheel note, adds the apex adjacent to the old C6+z boundary,
deletes one internal wheel edge, and imposes the critical-edge condition that
its endpoints have equal colour in a six-colouring.
"""

from collections import defaultdict
from itertools import combinations

import networkx as nx
import z3

from order8_atomic_wheel_counterarchitecture_verify import (
    KVERTICES,
    quotient,
    wheel_and_contacts,
)


GATE = ("x", "p", "q", "c0", "c2", "c4", "c5", "z")


def canonical_partition(values):
    relabel = {}
    answer = []
    for value in values:
        if value not in relabel:
            relabel[value] = len(relabel)
        answer.append(relabel[value])
    return tuple(answer)


def states_for(edge):
    wheel, contacts = wheel_and_contacts()
    graph = quotient(wheel, contacts)
    graph.add_node("v")
    graph.add_edges_from(("v", f"c{i}") for i in range(6))
    graph.add_edge("v", "z")
    graph.remove_edge(*edge)

    vertices = list(graph)
    colours = {u: z3.Int(f"col_{u}") for u in vertices}
    solver = z3.Solver()
    for u in vertices:
        solver.add(colours[u] >= 0, colours[u] < 6)
    for u, w in graph.edges():
        solver.add(colours[u] != colours[w])
    solver.add(colours[edge[0]] == colours[edge[1]])
    # In a critical graph, either endpoint could otherwise be recoloured to
    # repair the deleted edge.  Hence each endpoint sees all five other
    # colours in its retained neighbourhood.
    for endpoint in edge:
        for colour in range(6):
            solver.add(
                z3.Implies(
                    colours[endpoint] != colour,
                    z3.Or([colours[u] == colour for u in graph[endpoint]]),
                )
            )
    # Palette normalization at the apex.
    solver.add(colours["v"] == 0)

    states = set()
    codes = set()
    while solver.check() == z3.sat:
        model = solver.model()
        values = tuple(model.eval(colours[u]).as_long() for u in GATE)
        state = canonical_partition(values)
        states.add(state)
        apex_colour = model.eval(colours["v"]).as_long()
        edge_colour = model.eval(colours[edge[0]]).as_long()
        pin = tuple(u for u, value in zip(GATE, values) if value == apex_colour)
        edge_block = tuple(u for u, value in zip(GATE, values) if value == edge_colour)
        old_values = [values[GATE.index(u)] for u in ("c0", "c2", "c4", "c5", "z")]
        codes.add((pin, edge_block, len(set(old_values))))
        # Block exactly this equality partition rather than one literal palette.
        clauses = []
        for i, j in combinations(range(len(GATE)), 2):
            if state[i] == state[j]:
                clauses.append(colours[GATE[i]] != colours[GATE[j]])
            else:
                clauses.append(colours[GATE[i]] == colours[GATE[j]])
        solver.add(z3.Or(clauses))
    return states, codes


def main():
    wheel, _ = wheel_and_contacts()
    families = {}
    for edge in sorted(tuple(sorted(e)) for e in wheel.edges()):
        states, codes = states_for(edge)
        families[edge] = states
        block_histogram = defaultdict(int)
        for state in states:
            block_histogram[len(set(state))] += 1
        print(edge, len(states), "block histogram", dict(sorted(block_histogram.items())))
        print(" codes", len(codes), sorted(codes))

    print("pairwise intersections")
    edges = list(families)
    for i, e in enumerate(edges):
        for f in edges[i + 1 :]:
            common = families[e] & families[f]
            if common:
                print(e, f, len(common))


if __name__ == "__main__":
    main()
