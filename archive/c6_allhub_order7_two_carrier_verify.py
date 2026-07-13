#!/usr/bin/env python3
"""Certified finite closure attempt for the saturated |D|=7 atom.

Variables encode the missing graph F=overline(D) (maximum degree two) and
the seven boundary contact rows.  We forbid two explicit K7 templates:

1. six D singleton bags with distinct representatives plus the full shore;
2. the fixed boundary K4 {0,1,2,z}, the full shore, and two disjoint
   connected D carriers appended to distinct labels of the opposite prism
   triangle {3,4,5}.

UNSAT would prove that these two uniform templates close every order-seven
all-full-deletion atom; SAT prints the exact residual architecture.
"""

from __future__ import annotations

import itertools

from z3 import And, Bool, Not, Or, Solver, Sum, sat


V = tuple(range(7))
S = tuple(range(7))
PAIRS = tuple(itertools.combinations(V, 2))
MISSING_BOUNDARY = {
    (0, 4), (0, 5), (1, 3), (1, 5), (2, 3), (2, 4)
}
R = (3, 4, 5)
DEMANDS = {3: (1, 2), 4: (0, 2), 5: (0, 1)}


def connected_conditions(vertices, f):
    vertices = tuple(sorted(vertices))
    if len(vertices) <= 1:
        return []
    root = vertices[0]
    conditions = []
    rest = vertices[1:]
    # One orientation of every nontrivial cut, fixed by putting root left.
    for mask in range(1 << len(rest)):
        left = {root} | {rest[i] for i in range(len(rest)) if mask >> i & 1}
        if len(left) == len(vertices):
            continue
        right = set(vertices)-left
        conditions.append(Or(*(Not(f[tuple(sorted((i, j)))])
                               for i in left for j in right)))
    return conditions


def main():
    solver = Solver()
    f = {e: Bool(f"f_{e[0]}_{e[1]}") for e in PAIRS}
    x = [[Bool(f"x_{i}_{s}") for s in S] for i in V]

    for i in V:
        degree_f = Sum([f[tuple(sorted((i, j)))] for j in V if j != i])
        solver.add(degree_f <= 2)
        solver.add(Sum(x[i]) >= 2 + degree_f, Sum(x[i]) <= 4)
    for s in S:
        solver.add(Sum([x[i][s] for i in V]) >= 2)

    type_a = 0
    for omitted in V:
        kept = tuple(i for i in V if i != omitted)
        for reps in itertools.permutations(S, 6):
            assigned = dict(zip(kept, reps))
            conditions = [x[i][assigned[i]] for i in kept]
            for i, j in itertools.combinations(kept, 2):
                a, b = assigned[i], assigned[j]
                if tuple(sorted((a, b))) in MISSING_BOUNDARY:
                    conditions.append(Or(Not(f[tuple(sorted((i, j)))]),
                                         x[i][b], x[j][a]))
            solver.add(Not(And(*conditions)))
            type_a += 1

    # All ordered disjoint supports; order matters because their appended
    # triangle labels have different two-label demand pairs.
    supports = [set(i for i in V if mask >> i & 1)
                for mask in range(1, 1 << 7)]
    type_b = 0
    for r_a, r_b in itertools.permutations(R, 2):
        for A in supports:
            for B in supports:
                if A & B:
                    continue
                conditions = []
                conditions.extend(connected_conditions(A, f))
                conditions.extend(connected_conditions(B, f))
                conditions.append(Or(*(x[i][r_a] for i in A)))
                conditions.append(Or(*(x[i][r_b] for i in B)))
                for q in DEMANDS[r_a]:
                    conditions.append(Or(*(x[i][q] for i in A)))
                for q in DEMANDS[r_b]:
                    conditions.append(Or(*(x[i][q] for i in B)))
                solver.add(Not(And(*conditions)))
                type_b += 1

    verdict = solver.check()
    print("type-A", type_a, "type-B", type_b, "residual", verdict)
    if verdict == sat:
        model = solver.model()
        missing = tuple(e for e in PAIRS if model.eval(f[e]))
        rows = tuple(tuple(s for s in S if model.eval(x[i][s])) for i in V)
        print("missing D edges", missing)
        print("rows", rows)


if __name__ == "__main__":
    main()
