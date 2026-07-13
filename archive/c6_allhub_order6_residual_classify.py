#!/usr/bin/env python3
"""Classify exact residuals for six all-deletion carriers.

This independently checks the finite lemma used in Corollary 4.4 of
hadwiger_full_deletion_propagation.md.  The matching is deleted from K6.
A certificate assigns six distinct boundary representatives.  Every
missing K6 edge must be repaired simultaneously by a boundary edge or a
cross contact.
"""

from __future__ import annotations

import itertools

from z3 import And, Bool, Not, Or, Solver, Sum, unsat


S = tuple(range(7))
MISSING_BOUNDARY = {
    (0, 4), (0, 5), (1, 3), (1, 5), (2, 3), (2, 4)
}


def base_solver(q: int):
    matching = tuple((2*i, 2*i+1) for i in range(q))
    x = [[Bool(f"q{q}_{i}_{s}") for s in S] for i in range(6)]
    solver = Solver()
    low = [3] * 6
    for a, b in matching:
        low[a] = low[b] = 4
    for i in range(6):
        solver.add(Sum(x[i]) >= low[i], Sum(x[i]) <= 4)
    for s in S:
        solver.add(Sum([x[i][s] for i in range(6)]) >= 2)

    for reps in itertools.permutations(S, 6):
        conditions = [x[i][reps[i]] for i in range(6)]
        for a, b in matching:
            sa, sb = reps[a], reps[b]
            if tuple(sorted((sa, sb))) in MISSING_BOUNDARY:
                conditions.append(Or(x[a][sb], x[b][sa]))
        solver.add(Not(And(*conditions)))
    return solver, x


def exact_q1_profiles(x):
    profiles = []
    # Vertices 0,1 are the ends of the sole missing D-edge.  In the
    # residual they both see the four-set S-A; vertices 2..5 all see A.
    for A_tuple in itertools.combinations(S, 3):
        A = set(A_tuple)
        conditions = []
        for i in range(6):
            row = set(S)-A if i < 2 else A
            conditions.extend(x[i][s] if s in row else Not(x[i][s])
                              for s in S)
        profiles.append(And(*conditions))
    return Or(*profiles)


def main():
    q1, x1 = base_solver(1)
    q1.add(Not(exact_q1_profiles(x1)))
    print("q=1 outside exact 2+4 profiles", q1.check())
    assert q1.check() == unsat

    for q in (2, 3):
        solver, _ = base_solver(q)
        print(f"q={q} repaired-SDR residual", solver.check())
        assert solver.check() == unsat


if __name__ == "__main__":
    main()
