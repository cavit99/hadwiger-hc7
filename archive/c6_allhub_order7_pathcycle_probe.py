#!/usr/bin/env python3
"""Probe the uniform repaired-representative principle at |D|=7.

The missing graph F=overline(D) has maximum degree two.  Atomic surplus
gives boundary-row lower bound 2+d_F(i), the singleton atlas gives upper
bound four, and full-deletion propagation gives boundary-column sum at
least two.  A certificate omits one D vertex, assigns distinct boundary
representatives to the other six, and repairs every retained F-edge by a
boundary edge or a cross contact.
"""

from __future__ import annotations

import itertools

from z3 import And, Bool, Not, Or, Solver, Sum, sat
from contact_order7_sixedge_web_probe import generic_minor_model


S = tuple(range(7))
V = tuple(range(7))
MISSING_BOUNDARY = {
    (0, 4), (0, 5), (1, 3), (1, 5), (2, 3), (2, 4)
}


def path(vertices):
    return {(vertices[i], vertices[i+1]) for i in range(len(vertices)-1)}


def cycle(vertices):
    return path(vertices) | {(vertices[-1], vertices[0])}


FAMILIES = {
    "C7": cycle((0,1,2,3,4,5,6)),
    "C6+I": cycle((0,1,2,3,4,5)),
    "C5+P2": cycle((0,1,2,3,4)) | {(5,6)},
    "C4+P3": cycle((0,1,2,3)) | path((4,5,6)),
    "C3+C4": cycle((0,1,2)) | cycle((3,4,5,6)),
    "C3+P4": cycle((0,1,2)) | path((3,4,5,6)),
    "P7": path((0,1,2,3,4,5,6)),
    "P5+P2": path((0,1,2,3,4)) | {(5,6)},
    "P4+P3": path((0,1,2,3)) | path((4,5,6)),
    "3P2+I": {(0,1),(2,3),(4,5)},
}


def solve(name, f_edges):
    f_edges = {tuple(sorted(e)) for e in f_edges}
    degree = [sum(i in e for e in f_edges) for i in V]
    x = [[Bool(f"{name}_{i}_{s}") for s in S] for i in V]
    solver = Solver()
    for i in V:
        solver.add(Sum(x[i]) >= 2 + degree[i], Sum(x[i]) <= 4)
    for s in S:
        solver.add(Sum([x[i][s] for i in V]) >= 2)

    templates = 0
    for omitted in V:
        kept = tuple(i for i in V if i != omitted)
        for reps in itertools.permutations(S, 6):
            assigned = dict(zip(kept, reps))
            conditions = [x[i][assigned[i]] for i in kept]
            for i, j in f_edges:
                if omitted in (i, j):
                    continue
                a, b = assigned[i], assigned[j]
                if tuple(sorted((a,b))) in MISSING_BOUNDARY:
                    conditions.append(Or(x[i][b], x[j][a]))
            solver.add(Not(And(*conditions)))
            templates += 1
    verdict = solver.check()
    print(name, "edges", len(f_edges), "templates", templates, "residual", verdict)
    if verdict == sat:
        model = solver.model()
        rows = tuple(tuple(s for s in S if model.eval(x[i][s])) for i in V)
        print(" rows", rows)
        # Exact arbitrary minor check for the first repaired-SDR residual.
        boundary = set(itertools.combinations(S, 2))-MISSING_BOUNDARY
        dverts = tuple(range(7, 14))
        helper = 14
        edges = set(boundary)
        edges.update((s, helper) for s in S)
        for i, row in enumerate(rows):
            edges.update((s, dverts[i]) for s in row)
        for i, j in itertools.combinations(V, 2):
            if tuple(sorted((i, j))) not in f_edges:
                edges.add((dverts[i], dverts[j]))
        minor = generic_minor_model(15, {tuple(sorted(e)) for e in edges}, 7)
        print(" arbitrary K7", minor)
    return verdict


def main():
    for name, edges in FAMILIES.items():
        solve(name, edges)


if __name__ == "__main__":
    main()
