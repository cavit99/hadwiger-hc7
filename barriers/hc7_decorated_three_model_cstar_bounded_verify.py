#!/usr/bin/env python3
"""Bounded exact test of the surviving six-separator hypothesis C*.

The fixed core is the twelve-vertex planar 3-tree from the genuine-cell
falsifier, with one marked vertex added complete to each of its three
disjoint K4s.  All 27 still-optional edges incident with a marked vertex
are symbolic.  For every possible optional edge count, a cutting-plane
search returns one of:

* a separator of order below six;
* a six-separator not containing all three marks; or
* an explicit K7 branch-set model.

Exhaustion proves that no graph in this finite family satisfies C* and is
K7-minor-free.  This is evidence for C*, not a proof of C* in general.
"""

from __future__ import annotations

from itertools import combinations

from z3 import Bool, Not, Or, PbEq, PbGe, Solver, is_true, sat

from hc7_decorated_hwege_genuine_cell_falsifier_verify import (
    CLIQUES,
    MARKS,
    N,
    adjacency,
    components_after_deletion,
    depth_minor_model,
)


PLANAR_CORE = frozenset(
    {
        (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 9), (0, 10),
        (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 10), (1, 11),
        (2, 3), (2, 5), (2, 6), (2, 7), (2, 8),
        (3, 4), (3, 9),
        (4, 9),
        (5, 6), (5, 7), (5, 10), (5, 11),
        (6, 7), (6, 8),
        (7, 8),
        (10, 11),
    }
)

FIXED = frozenset(
    set(PLANAR_CORE)
    | {
        tuple(sorted((mark, vertex)))
        for mark, clique in zip(sorted(MARKS), CLIQUES)
        for vertex in clique - {mark}
    }
)

OPTIONAL = tuple(
    sorted(
        edge
        for edge in set(combinations(range(N), 2)) - set(FIXED)
        if set(edge) & MARKS
    )
)


def first_bad_cut(
    edges: frozenset[tuple[int, int]],
) -> tuple[frozenset[int], frozenset[int], frozenset[int]] | None:
    for order in range(6):
        for raw in combinations(range(N), order):
            deleted = frozenset(raw)
            components = components_after_deletion(edges, deleted)
            if len(components) > 1:
                left = components[0]
                right = frozenset(set(range(N)) - set(deleted) - set(left))
                return deleted, left, right
    for raw in combinations(range(N), 6):
        deleted = frozenset(raw)
        components = components_after_deletion(edges, deleted)
        if len(components) > 1 and not MARKS <= deleted:
            left = components[0]
            right = frozenset(set(range(N)) - set(deleted) - set(left))
            return deleted, left, right
    return None


def witness_optional_edges(
    edges: frozenset[tuple[int, int]], bags: tuple[tuple[int, ...], ...]
) -> frozenset[tuple[int, int]]:
    """Choose one literal edge for every connectivity/adjacency duty."""

    rows = adjacency(edges)
    witness = set()
    for raw_bag in bags:
        bag = set(raw_bag)
        reached = {raw_bag[0]}
        stack = [raw_bag[0]]
        while stack:
            vertex = stack.pop()
            for neighbour in rows[vertex]:
                if neighbour in bag - reached:
                    reached.add(neighbour)
                    stack.append(neighbour)
                    witness.add(tuple(sorted((vertex, neighbour))))
        assert reached == bag
    for left, right in combinations(bags, 2):
        edge = next(
            tuple(sorted((u, v)))
            for u in left
            for v in right
            if tuple(sorted((u, v))) in edges
        )
        witness.add(edge)
    return frozenset(witness & set(OPTIONAL))


def check_layer(optional_count: int) -> tuple[int, int, int]:
    variables = {edge: Bool(f"layer_{optional_count}_{edge[0]}_{edge[1]}") for edge in OPTIONAL}
    solver = Solver()
    solver.add(PbEq([(variables[edge], 1) for edge in OPTIONAL], optional_count))

    # Six-connectivity implies minimum degree six.  Adding this necessary
    # condition accelerates the symbolic exhaustion without narrowing C*.
    for vertex in range(N):
        fixed_degree = sum(vertex in edge for edge in FIXED)
        solver.add(
            PbGe(
                [(variables[edge], 1) for edge in OPTIONAL if vertex in edge],
                max(0, 6 - fixed_degree),
            )
        )

    candidates = separator_clauses = model_clauses = 0
    while solver.check() == sat:
        assignment = solver.model()
        edges = frozenset(
            set(FIXED)
            | {edge for edge in OPTIONAL if is_true(assignment[variables[edge]])}
        )
        candidates += 1

        bad = first_bad_cut(edges)
        if bad is not None:
            _, left, right = bad
            repairs = [
                variables[edge]
                for edge in OPTIONAL
                if (edge[0] in left and edge[1] in right)
                or (edge[1] in left and edge[0] in right)
            ]
            solver.add(Or(repairs) if repairs else False)
            separator_clauses += 1
            continue

        model = depth_minor_model(edges, f"cstar_{optional_count}_{candidates}")
        assert model is not None
        witness = witness_optional_edges(edges, model)
        assert witness
        solver.add(Or([Not(variables[edge]) for edge in witness]))
        model_clauses += 1

    return candidates, separator_clauses, model_clauses


def main() -> None:
    assert len(PLANAR_CORE) == 30
    assert len(FIXED) == 42
    assert len(OPTIONAL) == 27
    totals = [0, 0, 0]
    for optional_count in range(len(OPTIONAL) + 1):
        row = check_layer(optional_count)
        totals = [left + right for left, right in zip(totals, row)]
        print(optional_count, *row)
    print("family_size", 1 << len(OPTIONAL))
    print("symbolic_candidates", totals[0])
    print("separator_certificates", totals[1])
    print("K7_certificates", totals[2])
    print("Cstar_K7_free_survivors", 0)


if __name__ == "__main__":
    main()
