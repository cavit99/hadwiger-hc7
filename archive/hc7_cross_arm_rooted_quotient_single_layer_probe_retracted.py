#!/usr/bin/env python3
"""Retracted single-edge-layer probe for the overlap-four cross-arm cell.

Do not use this script as a rooted-model decoder.  It imposes the terminal
clique as literal original edges before checking the eleven support
relations.  A rooted exterior K4 supplies only virtual bag adjacencies, so
that order is invalid for the intended application.  The corrected
two-layer result and dependency-free verifier are:

    results/hc7_cross_arm_overlap_four_rooted_k4_decoder.md
    active/hc7_cross_arm_overlap_four_decoder_verify.py

This is a finite falsifier/discovery experiment, not a proof of the global
HC7 implication.  It uses the nine literal labels in the overlap-four
configuration:

    A = 0,1,2,3,4,5
    I = A cap X = 0,1,2,3
    X = 0,1,2,3,6
    private roots p=7, q=8.

All eleven exact-six supports supplied by the rigid cross-arm theorem are
required and are made irredundant by excluding a literal K5 in each.  The
negative side excludes both a K7 minor on the nine labels and a common
three-rooted K4 in A-{x}, for every x in I.

The expected results are:

* bare local data: SAT (so local support incidence is insufficient);
* the five outside labels 4,5,6,7,8 induce a 3-connected graph: UNSAT;
* any four of those five labels are completed to a clique, while both a
  common three-rooted K4 and a K7 avoiding the fifth label are forbidden:
  UNSAT.

The last item is valid only for an already literal clique.  It originally
motivated the corrected experiment but cannot itself lift a rooted K4.
"""

from __future__ import annotations

import itertools

from z3 import And, Bool, BoolVal, Not, Or, Solver, sat, unsat


N = 9
A = tuple(range(6))
I = tuple(range(4))
X = (0, 1, 2, 3, 6)
P, Q = 7, 8
OUTSIDE = (4, 5, 6, 7, 8)

EDGES = {(u, v): Bool(f"e_{u}_{v}") for u in range(N) for v in range(u + 1, N)}


def edge(u: int, v: int):
    return EDGES[tuple(sorted((u, v)))]


def partitions(items: tuple[int, ...], block_count: int):
    blocks: list[list[int]] = []

    def visit(index: int):
        if index == len(items):
            if len(blocks) == block_count:
                yield tuple(tuple(block) for block in blocks)
            return
        item = items[index]
        for position in range(len(blocks)):
            blocks[position].append(item)
            yield from visit(index + 1)
            blocks[position].pop()
        if len(blocks) < block_count:
            blocks.append([item])
            yield from visit(index + 1)
            blocks.pop()

    yield from visit(0)


def connected(vertices: tuple[int, ...]):
    """Cut characterization of connectivity on a fixed nonempty set."""
    if len(vertices) <= 1:
        return BoolVal(True)
    root = vertices[0]
    clauses = []
    for size in range(len(vertices) - 1):
        for chosen in itertools.combinations(vertices[1:], size):
            left = {root, *chosen}
            clauses.append(
                Or(*(edge(u, v) for u in left for v in vertices if v not in left))
            )
    return And(*clauses)


def touch(left: tuple[int, ...], right: tuple[int, ...]):
    return Or(*(edge(u, v) for u in left for v in right))


def exact_six_support(support: tuple[int, ...]):
    models = []
    for x, y in itertools.combinations(support, 2):
        core = tuple(v for v in support if v not in (x, y))
        models.append(
            And(
                edge(x, y),
                *(edge(u, v) for u, v in itertools.combinations(core, 2)),
                *(Or(edge(x, z), edge(y, z)) for z in core),
            )
        )
    return Or(*models)


def irredundant_exact_six(support: tuple[int, ...]):
    no_literal_k5 = [
        Not(And(*(edge(u, v) for u, v in itertools.combinations(five, 2))))
        for five in itertools.combinations(support, 5)
    ]
    return And(exact_six_support(support), *no_literal_k5)


def rooted_k4(common: tuple[int, ...], roots: tuple[int, ...]):
    models = []
    for support_size in (4, 5):
        for support in itertools.combinations(common, support_size):
            for bags in partitions(support, 4):
                models.append(
                    And(
                        *(connected(bag) for bag in bags),
                        *(touch(left, right) for left, right in itertools.combinations(bags, 2)),
                        *(touch((root,), bag) for root in roots for bag in bags),
                    )
                )
    return Or(*models)


def forbid_k7_models(vertices: tuple[int, ...] = tuple(range(N))):
    clauses = []
    for support_size in range(7, len(vertices) + 1):
        for support in itertools.combinations(vertices, support_size):
            for bags in partitions(support, 7):
                clauses.append(
                    Not(
                        And(
                            *(connected(bag) for bag in bags),
                            *(
                                touch(left, right)
                                for left, right in itertools.combinations(bags, 2)
                            ),
                        )
                    )
                )
    return clauses


def base_solver(k7_vertices: tuple[int, ...] = tuple(range(N))) -> Solver:
    solver = Solver()
    supports = [A, X + (P,), X + (Q,)]
    for x in I:
        common = tuple(v for v in A if v != x)
        supports.extend((common + (P,), common + (Q,)))
        solver.add(Not(rooted_k4(common, (x, P, Q))))
    solver.add(*(irredundant_exact_six(support) for support in supports))
    solver.add(*forbid_k7_models(k7_vertices))
    return solver


def require_three_connected(solver: Solver, vertices: tuple[int, ...]) -> None:
    """Require every deletion of at most two vertices to remain connected."""
    for deletion_size in range(3):
        for deleted in itertools.combinations(vertices, deletion_size):
            remaining = tuple(v for v in vertices if v not in deleted)
            solver.add(connected(remaining))


def main() -> None:
    bare = base_solver().check()
    print(f"bare={bare}")
    assert bare == sat

    terminal_connected = base_solver()
    require_three_connected(terminal_connected, OUTSIDE)
    connected_result = terminal_connected.check()
    print(f"outside_3connected={connected_result}")
    assert connected_result == unsat

    for four in itertools.combinations(OUTSIDE, 4):
        fifth = next(vertex for vertex in OUTSIDE if vertex not in four)
        surviving_vertices = tuple(vertex for vertex in range(N) if vertex != fifth)
        solver = base_solver(surviving_vertices)
        solver.add(*(edge(u, v) for u, v in itertools.combinations(four, 2)))
        result = solver.check()
        print(f"outside_k4={four} omitted={fifth} result={result}")
        assert result == unsat


if __name__ == "__main__":
    main()
