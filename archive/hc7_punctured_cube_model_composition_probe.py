#!/usr/bin/env python3
"""Test whether endpoint obstruction plus three split models forces K7.

This deliberately omits ambient seven-connectivity and colouring-state
geometry.  A negative instance is therefore a barrier to a *static*
punctured-cube composition claim, not to the HC7 programme.
"""

from __future__ import annotations

import itertools

import z3

import hc7_punctured_cube_endpoint_probe as endpoint


def build_graph(endpoint_mask: int, defect_sizes=((1, 1),) * 3):
    edges = set(endpoint.edge_set(endpoint_mask)) | set(endpoint.MATCHING)
    for index, (left_size, right_size) in enumerate(defect_sizes):
        left, right = endpoint.PAIRS[index]
        core = tuple(range(6 + 4 * index, 10 + 4 * index))
        edges.update(tuple(sorted(edge)) for edge in itertools.combinations(core, 2))
        for position, vertex in enumerate(core):
            if position < left_size:
                edges.add(tuple(sorted((right, vertex))))
            elif position < left_size + right_size:
                edges.add(tuple(sorted((left, vertex))))
            else:
                edges.add(tuple(sorted((left, vertex))))
                edges.add(tuple(sorted((right, vertex))))
    return 18, frozenset(edges)


def k7_model(order: int, edges, timeout_ms=30_000):
    adjacency = [set() for _ in range(order)]
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)

    solver = z3.Solver()
    solver.set(timeout=timeout_ms)
    member = [[z3.Bool(f"m_{v}_{b}") for b in range(7)] for v in range(order)]
    root = [[z3.Bool(f"r_{v}_{b}") for b in range(7)] for v in range(order)]
    rank = [[z3.Int(f"d_{v}_{b}") for b in range(7)] for v in range(order)]

    for vertex in range(order):
        solver.add(z3.PbLe([(member[vertex][bag], 1) for bag in range(7)], 1))

    root_values = []
    for bag in range(7):
        solver.add(z3.PbEq([(root[v][bag], 1) for v in range(order)], 1))
        root_values.append(
            z3.Sum([v * z3.If(root[v][bag], 1, 0) for v in range(order)])
        )
        for vertex in range(order):
            solver.add(z3.Implies(root[vertex][bag], member[vertex][bag]))
            solver.add(
                z3.Implies(
                    root[vertex][bag],
                    z3.And(
                        rank[vertex][bag] == 0,
                        *[z3.Not(member[old][bag]) for old in range(vertex)],
                    ),
                )
            )
            solver.add(
                z3.Implies(
                    member[vertex][bag],
                    z3.And(rank[vertex][bag] >= 0, rank[vertex][bag] < order),
                )
            )
            solver.add(
                z3.Implies(
                    z3.And(member[vertex][bag], z3.Not(root[vertex][bag])),
                    z3.Or(
                        *[
                            z3.And(
                                member[old][bag],
                                rank[old][bag] < rank[vertex][bag],
                            )
                            for old in adjacency[vertex]
                        ]
                    ),
                )
            )
    for bag in range(6):
        solver.add(root_values[bag] < root_values[bag + 1])
    for first, second in itertools.combinations(range(7), 2):
        solver.add(
            z3.Or(
                *[
                    z3.And(member[u][first], member[v][second])
                    for u, v in edges
                ],
                *[
                    z3.And(member[v][first], member[u][second])
                    for u, v in edges
                ],
            )
        )

    status = solver.check()
    if status != z3.sat:
        return str(status), None
    model = solver.model()
    bags = tuple(
        tuple(v for v in range(order) if model.evaluate(member[v][bag]))
        for bag in range(7)
    )
    return "sat", bags


def main() -> None:
    minima = endpoint.minimal_masks()
    representatives = sorted(
        {min(endpoint.transform(mask, image) for image in endpoint.SYMMETRIES) for mask in minima}
    )
    defect_types = ((1, 1), (1, 2), (2, 1), (1, 3), (3, 1), (2, 2))
    for orbit, mask in enumerate(representatives):
        for defects in itertools.product(defect_types, repeat=3):
            order, edges = build_graph(mask, defects)
            status, bags = k7_model(order, edges)
            print("CASE", orbit, defects, len(edges), status, bags, flush=True)
            if status != "sat":
                return


if __name__ == "__main__":
    main()
