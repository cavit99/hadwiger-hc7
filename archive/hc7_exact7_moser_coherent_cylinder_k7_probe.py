#!/usr/bin/env python3
"""Exact K7-minor probe for the coherent two-cycle Moser cylinder.

Vertices 0,...,6 are the standard Moser boundary, 7,...,12 and 13,...,18
are the two six-cycles, and 19 is the thin full packet contracted to one
boundary-universal vertex.  The six literal portal labels around each cycle
are 2,4,5,3,1,0.  Optional edges from boundary vertex 6 choose one cycle
location on each side.  A rung mask adds the homologous edges

    (7+i)(13+i),  0 <= i < 6.

The SMT encoding is exact: each of seven nonempty branch sets is connected
by a decreasing-depth arborescence, branch sets are disjoint, and every pair
has a literal graph edge.  It is a computational certificate, not a
replacement for displaying any positive model that it returns.
"""

from __future__ import annotations

from itertools import combinations

from z3 import And, Bool, If, Implies, Int, Not, Or, Solver, Sum, is_true, sat


MOSER = {
    (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
    (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
}
PORTAL_ORDER = (2, 4, 5, 3, 1, 0)
P = tuple(range(7, 13))
Q = tuple(range(13, 19))
THIN = 19


def edge(u: int, v: int) -> tuple[int, int]:
    return tuple(sorted((u, v)))


def cylinder(
    rungs: tuple[int, ...],
    six_port_p: int | None = None,
    six_port_q: int | None = None,
) -> set[tuple[int, int]]:
    edges = {edge(*item) for item in MOSER}
    for cycle in (P, Q):
        edges |= {edge(cycle[i], cycle[(i + 1) % 6]) for i in range(6)}
        edges |= {
            edge(literal, cycle[i])
            for i, literal in enumerate(PORTAL_ORDER)
        }
    edges |= {edge(literal, THIN) for literal in range(7)}
    edges |= {edge(P[i], Q[i]) for i in rungs}
    if six_port_p is not None:
        edges.add(edge(6, P[six_port_p]))
    if six_port_q is not None:
        edges.add(edge(6, Q[six_port_q]))
    return edges


def k7_model(
    edges: set[tuple[int, int]],
    same_bag: tuple[int, int] | None = None,
) -> list[list[int]] | None:
    order = 7
    vertex_count = 20
    neighbours = [[] for _ in range(vertex_count)]
    for u, v in edges:
        neighbours[u].append(v)
        neighbours[v].append(u)

    belongs = [
        [Bool(f"x_{vertex}_{bag}") for bag in range(order)]
        for vertex in range(vertex_count)
    ]
    root = [
        [Bool(f"r_{vertex}_{bag}") for bag in range(order)]
        for vertex in range(vertex_count)
    ]
    depth = [
        [Int(f"d_{vertex}_{bag}") for bag in range(order)]
        for vertex in range(vertex_count)
    ]

    solver = Solver()
    for vertex in range(vertex_count):
        solver.add(
            Sum([If(belongs[vertex][bag], 1, 0) for bag in range(order)]) <= 1
        )

    if same_bag is not None:
        left, right = same_bag
        solver.add(
            Or(
                [
                    And(belongs[left][bag], belongs[right][bag])
                    for bag in range(order)
                ]
            )
        )

    for bag in range(order):
        solver.add(
            Sum([If(root[vertex][bag], 1, 0) for vertex in range(vertex_count)])
            == 1
        )
        for vertex in range(vertex_count):
            solver.add(depth[vertex][bag] >= 0, depth[vertex][bag] < vertex_count)
            solver.add(
                Implies(
                    root[vertex][bag],
                    And(belongs[vertex][bag], depth[vertex][bag] == 0),
                )
            )
            solver.add(
                Implies(
                    And(belongs[vertex][bag], Not(root[vertex][bag])),
                    And(
                        depth[vertex][bag] >= 1,
                        Or(
                            [
                                And(
                                    belongs[other][bag],
                                    depth[other][bag] < depth[vertex][bag],
                                )
                                for other in neighbours[vertex]
                            ]
                        ),
                    ),
                )
            )

    for left in range(order):
        for right in range(left + 1, order):
            solver.add(
                Or(
                    [
                        Or(
                            And(belongs[u][left], belongs[v][right]),
                            And(belongs[u][right], belongs[v][left]),
                        )
                        for u, v in edges
                    ]
                )
            )

    if solver.check() != sat:
        return None
    model = solver.model()
    return [
        [
            vertex
            for vertex in range(vertex_count)
            if is_true(model.eval(belongs[vertex][bag]))
        ]
        for bag in range(order)
    ]


def main() -> None:
    # First ask for models which do not use either optional vertex-6 portal.
    # Every returned model is therefore uniform over all 36 choices.
    for size in range(7):
        good = []
        for rungs in combinations(range(6), size):
            model = k7_model(cylinder(rungs))
            if model is not None:
                good.append((rungs, model))
        print(f"port-free rung_size={size} good={len(good)}", flush=True)
        if good:
            for rungs, model in good:
                print(f"UNIFORM_MODEL rungs={rungs} bags={model}", flush=True)
            break

    # The rung-free graph is the smallest coherent cylinder.  Test every
    # optional vertex-6 portal placement to determine whether it is a genuine
    # local barrier to the proposed universal cylinder implication.
    rung_free = []
    for port_p in range(6):
        for port_q in range(6):
            model = k7_model(cylinder((), port_p, port_q))
            if model is not None:
                rung_free.append((port_p, port_q, model))
    print(f"rung_free_port_pairs_with_K7={len(rung_free)}/36", flush=True)
    for port_p, port_q, model in rung_free:
        print(
            f"RUNG_FREE_MODEL ports=({port_p},{port_q}) bags={model}",
            flush=True,
        )


if __name__ == "__main__":
    main()
