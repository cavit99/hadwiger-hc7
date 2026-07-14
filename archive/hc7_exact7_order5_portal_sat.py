#!/usr/bin/env python3
"""Search the exact five-vertex paired-duty portal residue.

This is a discovery probe.  For every labelled three-connected graph C on
five vertices it asks whether six nonempty portal sets can satisfy the host
minimum-degree lower bound while no two duties have disjoint connected
carriers.  The singleton c is allowed to contact every C-vertex, so the
degree constraint used here is the weakest one implied by delta(G) >= 7.
"""

from __future__ import annotations

from itertools import combinations

import z3


N = 5
LABELS = range(6)
DUTIES = ((0, 1), (2, 3), (4, 5))
ALL_EDGES = tuple(combinations(range(N), 2))


def adjacency(edge_mask: int) -> tuple[int, ...]:
    answer = [0] * N
    for bit, (u, v) in enumerate(ALL_EDGES):
        if edge_mask >> bit & 1:
            answer[u] |= 1 << v
            answer[v] |= 1 << u
    return tuple(answer)


def connected(mask: int, adj: tuple[int, ...]) -> bool:
    if not mask:
        return False
    seen = mask & -mask
    while True:
        larger = seen
        for v in range(N):
            if seen >> v & 1:
                larger |= adj[v] & mask
        if larger == seen:
            return seen == mask
        seen = larger


def three_connected(adj: tuple[int, ...]) -> bool:
    full = (1 << N) - 1
    for size in range(3):
        for deleted in combinations(range(N), size):
            deleted_mask = sum(1 << v for v in deleted)
            if not connected(full ^ deleted_mask, adj):
                return False
    return True


def solve(adj: tuple[int, ...]):
    solver = z3.Solver()
    portal = [[z3.Bool(f"p_{label}_{v}") for v in range(N)] for label in LABELS]

    for label in LABELS:
        solver.add(z3.Or(portal[label]))

    # At most one further boundary neighbour c is available at each vertex.
    for v in range(N):
        degree_c = adj[v].bit_count()
        solver.add(z3.Sum([z3.If(portal[label][v], 1, 0) for label in LABELS]) >= 6 - degree_c)

    connected_sets = [mask for mask in range(1, 1 << N) if connected(mask, adj)]

    def meets(label: int, mask: int):
        return z3.Or([portal[label][v] for v in range(N) if mask >> v & 1])

    def funds(duty: int, mask: int):
        left, right = DUTIES[duty]
        return z3.And(meets(left, mask), meets(right, mask))

    for duty_left, duty_right in combinations(range(3), 2):
        for left in connected_sets:
            for right in connected_sets:
                if left & right:
                    continue
                solver.add(z3.Not(z3.And(funds(duty_left, left), funds(duty_right, right))))
                solver.add(z3.Not(z3.And(funds(duty_right, left), funds(duty_left, right))))

    if solver.check() != z3.sat:
        return None
    model = solver.model()
    return tuple(
        tuple(v for v in range(N) if z3.is_true(model.eval(portal[label][v])))
        for label in LABELS
    )


def main() -> None:
    checked = 0
    for edge_mask in range(1 << len(ALL_EDGES)):
        adj = adjacency(edge_mask)
        if not three_connected(adj):
            continue
        checked += 1
        model = solve(adj)
        if model is not None:
            edges = [edge for bit, edge in enumerate(ALL_EDGES) if edge_mask >> bit & 1]
            print("SAT", edges, model)
            return
    print("UNSAT: no five-vertex three-connected portal system", checked)


if __name__ == "__main__":
    main()
