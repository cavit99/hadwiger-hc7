#!/usr/bin/env python3
"""Certify the strict four-vertex full-gate cell.

The boundary is K_{2,2,2,1}, the near shore is a K4 with arbitrary
boundary contacts, and the far shore is contracted to one full vertex.
Z3 ranges over every contact matrix satisfying the strict relative
boundary inequalities.  Every proposed matrix is either returned as a
K7-free counterarchitecture or excluded by an independently checked
explicit K7 model.  The exclusion clause uses only the contact edges of
that model, so an UNSAT result is an exhaustive monotone certificate.
"""

from __future__ import annotations

import itertools

import z3

from sharp_core_order4_shore_sat import (
    k_minor_model,
    model_witness,
    verify_model,
)


S = tuple(range(7))
D = tuple(range(7, 11))
R = 11
VARIABLE = tuple((s, d) for s in S for d in D)
MISSING = {(0, 1), (2, 3), (4, 5)}
FIXED = (
    (set(itertools.combinations(S, 2)) - MISSING)
    | set(itertools.combinations(D, 2))
    | {(s, R) for s in S}
)
FIXED = {tuple(sorted(edge)) for edge in FIXED}


def solve(limit: int = 100_000) -> dict[str, object]:
    variables = {
        edge: z3.Bool(f"e_{edge[0]}_{edge[1]}") for edge in VARIABLE
    }
    solver = z3.Solver()

    # Fullness of the near shore.  (The triple inequalities below already
    # imply this, but retaining it makes the exact gate hypothesis visible.)
    for s in S:
        solver.add(z3.Or(*(variables[(s, d)] for d in D)))

    # For nonempty proper X subset K4, its internal external neighbourhood
    # has order 4-|X|.  Strict relative boundary eight is therefore exactly
    # |N_S(X)| >= 4+|X|.
    for size in (1, 2, 3):
        for shore_subset in itertools.combinations(D, size):
            seen = [
                z3.Or(*(variables[(s, d)] for d in shore_subset))
                for s in S
            ]
            solver.add(z3.Sum(*(z3.If(term, 1, 0) for term in seen))
                       >= 4 + size)

    for iteration in range(limit):
        if solver.check() != z3.sat:
            return {"status": "unsat", "iterations": iteration}
        assignment = solver.model()
        chosen = {
            edge
            for edge, variable in variables.items()
            if z3.is_true(assignment.eval(variable, model_completion=True))
        }
        edges = FIXED | chosen
        model = k_minor_model(edges)
        if model is None:
            return {
                "status": "counterarchitecture",
                "iterations": iteration,
                "connectivity": vertex_connectivity(edges),
                "chosen": tuple(sorted(chosen)),
            }
        verify_model(edges, model)
        witness = model_witness(edges, FIXED, model)
        if not witness:
            return {
                "status": "unsat",
                "iterations": iteration + 1,
                "fixed_model": True,
            }
        solver.add(z3.Or(*(z3.Not(variables[edge]) for edge in witness)))
    return {"status": "limit", "iterations": limit}


def components_after(edges: set[tuple[int, int]], deleted: set[int]) -> int:
    remaining = set(range(12)) - deleted
    if not remaining:
        return 0
    adjacency = {vertex: set() for vertex in remaining}
    for left, right in edges:
        if left in remaining and right in remaining:
            adjacency[left].add(right)
            adjacency[right].add(left)
    count = 0
    while remaining:
        count += 1
        stack = [remaining.pop()]
        while stack:
            vertex = stack.pop()
            reached = adjacency[vertex] & remaining
            remaining.difference_update(reached)
            stack.extend(reached)
    return count


def minimum_cuts(edges: set[tuple[int, int]]) -> tuple[int, list[set[int]]]:
    for size in range(12):
        cuts = [
            set(raw)
            for raw in itertools.combinations(range(12), size)
            if components_after(edges, set(raw)) > 1
        ]
        if cuts:
            return size, cuts
    return 11, []


def vertex_connectivity(edges: set[tuple[int, int]]) -> int:
    return minimum_cuts(edges)[0]


def displayed_assignment() -> None:
    rows = {
        0: {0, 1},
        1: {2, 3},
        2: {0, 1, 2, 3},
        3: {0, 1, 2, 3},
        4: {1, 3},
        5: {0, 2},
        6: {0, 1, 2, 3},
    }
    chosen = {(s, 7 + d) for s, vertices in rows.items() for d in vertices}
    edges = FIXED | chosen

    # Replay strict relative boundary eight on every proper shore subset.
    for size in (1, 2, 3):
        for raw in itertools.combinations(range(4), size):
            boundary = {
                s for s, vertices in rows.items() if vertices & set(raw)
            }
            assert (4 - size) + len(boundary) >= 8

    # Replay all three pair packets and the absence of a triple packet.
    demands = ((0, 1), (2, 3), (4, 5))
    carriers: list[list[set[int]]] = []
    for left, right in demands:
        carriers.append([
            set(raw)
            for size in range(1, 5)
            for raw in itertools.combinations(range(4), size)
            if any(vertex in rows[left] for vertex in raw)
            and any(vertex in rows[right] for vertex in raw)
        ])
    for first, second in itertools.combinations(range(3), 2):
        assert any(
            left.isdisjoint(right)
            for left in carriers[first]
            for right in carriers[second]
        )
    assert not any(
        first.isdisjoint(second | third)
        and second.isdisjoint(third)
        for first in carriers[0]
        for second in carriers[1]
        for third in carriers[2]
    )

    connectivity, cuts = minimum_cuts(edges)
    assert connectivity == 7
    assert cuts == [set(S)]

    # This is the spanning model produced by the hand proof: match the four
    # shore vertices to 3,4,5,1, leave the cross-part edge 02, and use the
    # universal singleton 6 plus the full far shore.
    bags = ({7, 3}, {8, 4}, {9, 5}, {10, 1}, {11}, {6}, {0, 2})
    masks = tuple(sum(1 << vertex for vertex in bag) for bag in bags)
    verify_model(edges, masks)
    print("displayed connectivity 7; unique minimum cut", tuple(S))
    print("displayed K7 bags", tuple(tuple(sorted(bag)) for bag in bags))


def main() -> None:
    displayed_assignment()
    result = solve()
    print("all strict K4 contact matrices", result)
    assert result["status"] == "unsat"


if __name__ == "__main__":
    main()
