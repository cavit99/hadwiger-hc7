#!/usr/bin/env python3
"""Probe the first all-full-deletion atom of order six.

For D=K6 the only obstruction to matching all six carrier vertices to
distinct boundary portals is the exact 4+2 incidence split A|B with
|A|=3.  We test all 35 labelled splits for a K7 model.  We then probe the
analogous minimum rows for K6 minus a matching of size 1,2,3.
"""

from __future__ import annotations

import itertools

from contact_order7_sixedge_web_probe import generic_minor_model
from z3 import Bool, Or, PbEq, PbGe, Solver, sat


S = tuple(range(7))
D = tuple(range(7, 13))
H = 13
MISSING = {(0, 4), (0, 5), (1, 3), (1, 5), (2, 3), (2, 4)}
BOUNDARY = set(itertools.combinations(S, 2)) - MISSING


def host(d_missing, rows):
    edges = set(BOUNDARY)
    edges.update(e for e in itertools.combinations(D, 2)
                 if tuple(sorted((e[0]-7, e[1]-7))) not in d_missing)
    edges.update((s, H) for s in S)
    for i, row in enumerate(rows):
        edges.update((s, D[i]) for s in row)
    return {tuple(sorted(e)) for e in edges}


def decode(model):
    return tuple(tuple(i for i in range(14) if bag >> i & 1)
                 for bag in model)


def main():
    failures = []
    for A in itertools.combinations(S, 3):
        A = set(A)
        B = set(S)-A
        rows = (A, A, A, A, B, B)
        model = generic_minor_model(14, host(set(), rows), 7)
        if model is None:
            failures.append((tuple(sorted(A)), tuple(sorted(B))))
        else:
            print("split", tuple(sorted(A)), "model", decode(model))
    print("K6 split failures", failures)
    assert not failures

    boundary = {tuple(sorted(e)) for e in BOUNDARY}
    for q in (1, 2, 3):
        missing = {(2*i, 2*i+1) for i in range(q)}
        x = [[Bool(f"q{q}_{i}_{s}") for s in S] for i in range(6)]
        solver = Solver()
        for i in range(6):
            lower = 4 if i < 2*q else 3
            solver.add(PbGe([(x[i][s], 1) for s in S], lower))
            solver.add(sum(x[i][s] for s in S) <= 4)
        for s in S:
            solver.add(sum(x[i][s] for i in range(6)) >= 2)

        templates = 0
        for assigned in itertools.permutations(S, 6):
            terms = [x[i][assigned[i]] for i in range(6)]
            repairs = []
            for i, j in missing:
                a, b = assigned[i], assigned[j]
                if tuple(sorted((a, b))) in boundary:
                    repairs.append(((),))
                else:
                    repairs.append(((x[i][b],), (x[j][a],)))
            for selected in itertools.product(*repairs):
                required = terms + [literal for choice in selected for literal in choice]
                solver.add(Or(*(~t for t in required)))
                templates += 1

        verdict = solver.check()
        print("q", q, "six-carrier templates", templates, "residual", verdict)
        if verdict == sat:
            m = solver.model()
            rows = tuple(tuple(s for s in S if m.eval(x[i][s])) for i in range(6))
            print(" q", q, "residual rows", rows)
            model = generic_minor_model(14, host(missing, rows), 7)
            print(" q", q, "arbitrary model", decode(model) if model else None)


if __name__ == "__main__":
    main()
