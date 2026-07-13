#!/usr/bin/env python3
"""Exact six-carrier probe for an order-six all-deletion C6+K1 atom.

For a fixed matching M deleted from K6, row i is the set of all seven
boundary labels contacted by vertex i.  Atomic surplus gives row size at
least four at endpoints of M (internal degree four), and at least three
elsewhere (internal degree five); the singleton atlas gives the upper
bound four.  Full-deletion propagation gives column sum at least two.

We forbid every valid certificate made from six singleton D-bags, six
distinct boundary representatives, and the opposite full shore.  For
each missing D-edge, the corresponding two bags must be repaired either
by an edge between their representatives or by a cross contact.  All
missing pairs are checked simultaneously.
"""

from __future__ import annotations

import itertools

from z3 import And, Bool, Not, Or, Solver, Sum, sat


MISSING_BOUNDARY = {
    (0, 4), (0, 5), (1, 3), (1, 5), (2, 3), (2, 4)
}


def solve(matching: tuple[tuple[int, int], ...]):
    vertices = range(6)
    labels = range(7)
    forbidden = {tuple(sorted(e)) for e in matching}
    x = [[Bool(f"x_{i}_{s}") for s in labels] for i in vertices]
    solver = Solver()

    low = [3] * 6
    for a, b in matching:
        low[a] = low[b] = 4
    for i in vertices:
        solver.add(Sum([x[i][s] for s in labels]) >= low[i])
        solver.add(Sum([x[i][s] for s in labels]) <= 4)
    for s in labels:
        solver.add(Sum([x[i][s] for i in vertices]) >= 2)

    templates = 0
    for reps in itertools.permutations(labels, 6):
        conditions = [x[i][reps[i]] for i in vertices]
        for a, b in forbidden:
            sa, sb = reps[a], reps[b]
            if tuple(sorted((sa, sb))) in MISSING_BOUNDARY:
                conditions.append(Or(x[a][sb], x[b][sa]))
        solver.add(Not(And(*conditions)))
        templates += 1

    result = solver.check()
    print("matching", matching, "templates", templates, "residual", result)
    if result == sat:
        model = solver.model()
        rows = tuple(tuple(s for s in labels if model.eval(x[i][s]))
                     for i in vertices)
        print("rows", rows)
    return result


def main():
    for q in range(4):
        matching = tuple((2 * i, 2 * i + 1) for i in range(q))
        solve(matching)


if __name__ == "__main__":
    main()
