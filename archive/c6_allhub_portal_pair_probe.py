#!/usr/bin/env python3
"""Exact probes for the all-full-deletion portal-pair core.

Boundary labels are 0..6, D is a K5, and h is an opposite full helper.
Each boundary portal class is a displayed pair in D.  The main example is
an odd C5 incidence obstruction to two disjoint full transversals.
"""

from __future__ import annotations

import itertools

from contact_order7_sixedge_web_probe import generic_minor_model
from z3 import Bool, Or, PbEq, Solver, sat


S = tuple(range(7))
D = tuple(range(7, 12))
H = 12
MISSING = {(0, 4), (0, 5), (1, 3), (1, 5), (2, 3), (2, 4)}
BOUNDARY = set(itertools.combinations(S, 2)) - MISSING


def host(portal_pairs: tuple[tuple[int, int], ...]):
    edges = set(BOUNDARY)
    edges.update(itertools.combinations(D, 2))
    edges.update((s, H) for s in S)
    for s, (i, j) in enumerate(portal_pairs):
        edges.add((s, D[i]))
        edges.add((s, D[j]))
    return {tuple(sorted(e)) for e in edges}


def decode(model):
    return tuple(tuple(i for i in range(13) if bag >> i & 1)
                 for bag in model)


def main():
    pairs = ((0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 1), (2, 3))
    model = generic_minor_model(13, host(pairs), 7)
    print("odd portal cycle model", decode(model) if model else None)
    assert model is not None

    # Test the canonical five K5 bags + one boundary singleton + full helper
    # certificate against every 5x7 contact matrix with row sum four and
    # column sum at least two.
    x = [[Bool(f"x_{i}_{s}") for s in S] for i in range(5)]
    solver = Solver()
    for i in range(5):
        solver.add(PbEq([(x[i][s], 1) for s in S], 4))
    for s in S:
        solver.add(sum(x[i][s] for i in range(5)) >= 2)

    boundary = {tuple(sorted(e)) for e in BOUNDARY}
    templates = 0
    for y in S:
        choices = tuple(s for s in S if s != y)
        for assigned in itertools.permutations(choices, 5):
            required = []
            valid = True
            for i, s in enumerate(assigned):
                required.append(x[i][s])
                if tuple(sorted((s, y))) not in boundary:
                    required.append(x[i][y])
            if valid:
                solver.add(Or(*(~literal for literal in required)))
                templates += 1
    print("canonical templates", templates, "residual", solver.check())
    if solver.check() == sat:
        m = solver.model()
        rows = tuple(tuple(s for s in S if m.eval(x[i][s])) for i in range(5))
        print("canonical residual rows", rows)
        edges = set(BOUNDARY) | set(itertools.combinations(D, 2))
        edges.update((s, H) for s in S)
        for i, row in enumerate(rows):
            edges.update((s, D[i]) for s in row)
        residual_model = generic_minor_model(13, {tuple(sorted(e)) for e in edges}, 7)
        print("residual arbitrary K7", decode(residual_model) if residual_model else None)


if __name__ == "__main__":
    main()
