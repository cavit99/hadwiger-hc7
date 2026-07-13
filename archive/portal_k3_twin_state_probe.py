#!/usr/bin/env python3
"""Enumerate local boundary states after deleting one true twin."""

import z3

from portal_k3k1_probe import graph
from portal_oneone_small_probe import N


SURVIVORS = (
    (93, 115, 115),
    (109, 115, 115),
    (115, 115, 124),
    (115, 115, 125),
)


def normalized_state(values):
    rename = {}
    result = []
    for value in values:
        if value not in rename:
            rename[value] = len(rename)
        result.append(rename[value])
    return tuple(result)


def states(rows):
    h = graph("triangle", rows, False)
    apex = 12
    deleted = 10
    twin = 9
    h.add_node(apex)
    h.add_edges_from((apex, n) for n in N)
    h.remove_node(11)  # discard the artificial contracted opposite helper
    h.remove_node(deleted)
    vertices = tuple(h.nodes())
    colors = {x: z3.Int(f"c_{x}") for x in vertices}
    solver = z3.Solver()
    for x in vertices:
        solver.add(colors[x] >= 0, colors[x] < 6)
    for x, y in h.edges():
        solver.add(colors[x] != colors[y])
    solver.add(colors[twin] == 0)

    # In a vertex-critical graph, the deleted twin cannot be coloured:
    # its seven neighbours therefore use every one of the six colours.
    deleted_neighbours = {8, 9, 1, 0, 2, 6, 7}
    for colour in range(6):
        solver.add(z3.Or([colors[x] == colour for x in deleted_neighbours]))

    result = set()
    while solver.check() == z3.sat:
        model = solver.model()
        values = tuple(model.eval(colors[x]).as_long() for x in sorted(N))
        state = normalized_state(values)
        result.add(state)
        # Block this exact equality partition on N, not merely one naming.
        clauses = []
        ordered = sorted(N)
        for i in range(7):
            for j in range(i + 1, 7):
                same = state[i] == state[j]
                clauses.append(colors[ordered[i]] != colors[ordered[j]] if same
                               else colors[ordered[i]] == colors[ordered[j]])
        solver.add(z3.Or(clauses))
    return result


def edge_states(rows, edge):
    h = graph("triangle", rows, False)
    apex = 12
    h.add_node(apex)
    h.add_edges_from((apex, n) for n in N)
    h.remove_node(11)  # use only necessary constraints from this side
    h.remove_edge(*edge)
    vertices = tuple(h.nodes())
    colors = {x: z3.Int(f"e_{edge[0]}_{edge[1]}_{x}") for x in vertices}
    solver = z3.Solver()
    for x in vertices:
        solver.add(colors[x] >= 0, colors[x] < 6)
    for x, y in h.edges():
        solver.add(colors[x] != colors[y])
    solver.add(colors[edge[0]] == 0, colors[edge[1]] == 0)
    for endpoint in edge:
        neighbours = set(h.neighbors(endpoint))
        for colour in range(1, 6):
            solver.add(z3.Or([colors[x] == colour for x in neighbours]))
    result = set()
    while solver.check() == z3.sat:
        model = solver.model()
        values = tuple(model.eval(colors[x]).as_long() for x in sorted(N))
        state = normalized_state(values)
        result.add(state)
        ordered = sorted(N)
        clauses = []
        for i in range(7):
            for j in range(i + 1, 7):
                same = state[i] == state[j]
                clauses.append(colors[ordered[i]] != colors[ordered[j]] if same
                               else colors[ordered[i]] == colors[ordered[j]])
        solver.add(z3.Or(clauses))
    return result


def pair_blocks(state):
    ordered = sorted(N)
    groups = {}
    for x, c in zip(ordered, state):
        groups.setdefault(c, []).append(x)
    return tuple(sorted(tuple(group) for group in groups.values() if len(group) > 1))


def main():
    for rows in SURVIVORS:
        result = states(rows)
        blocks = sorted({pair_blocks(state) for state in result})
        print(rows, "states", len(result), "matching states", len(blocks))
        for item in blocks:
            print(" ", item)
        for edge in ((8, 9), (8, 10), (9, 10)):
            eresult = edge_states(rows, edge)
            eblocks = {pair_blocks(state) for state in eresult}
            print(" edge", edge, "states", len(eblocks))


if __name__ == "__main__":
    main()
