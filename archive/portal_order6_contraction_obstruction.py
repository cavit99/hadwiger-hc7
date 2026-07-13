#!/usr/bin/env python3
"""Test whether every edge of an admissible order-six shore can be blocked.

For each of the 112 connected unlabelled graphs F on six vertices, build the
exact attachment formula from the reserved-connector cell.  For every edge e
of F, form the five-vertex row system obtained by contracting e.  ``safe(e)``
means that the contracted system still satisfies every hypothesis of the
certified order-five theorem (full attachment is automatic).  We ask whether
all edges can simultaneously be unsafe.

UNSAT for every F proves that every admissible six-shore has a safe contraction
to the already-closed order-five cell; SAT records the exact tight obstruction
for further analysis.
"""

from __future__ import annotations

import json

import z3

from portal_k6k1_probe import ORDER, TYPES


def base_constraints(solver, x, aw, fedges):
    degrees = [sum(i in edge for edge in fedges) for i in range(ORDER)]
    for i in range(ORDER):
        solver.add(z3.PbGe([(x[i][j], 1) for j in range(7)], 7 - degrees[i]))
    for j in range(7):
        solver.add(z3.Or(*(x[i][j] for i in range(ORDER))))
    solver.add(z3.PbGe([(aw, 1)] + [(x[i][6], 1) for i in range(ORDER)], 3))
    for subset in range(1, (1 << ORDER) - 1):
        outside = {
            y
            for i in range(ORDER) if subset >> i & 1
            for y in range(ORDER) if not (subset >> y & 1)
            if tuple(sorted((i, y))) in fedges
        }
        unions = [
            z3.Or(*(x[i][j] for i in range(ORDER) if subset >> i & 1))
            for j in range(7)
        ]
        solver.add(z3.PbGe([(term, 1) for term in unions], 7 - len(outside)))


def contraction_groups(edge):
    a, b = edge
    return [(a, b)] + [(i,) for i in range(ORDER) if i not in edge]


def safe_contraction(x, aw, fedges, edge):
    groups = contraction_groups(edge)
    assert len(groups) == 5
    group_rows = [
        [z3.Or(*(x[i][j] for i in group)) for j in range(7)]
        for group in groups
    ]
    group_edges = {
        tuple(sorted((p, q)))
        for p in range(5) for q in range(p + 1, 5)
        if any(tuple(sorted((i, j))) in fedges for i in groups[p] for j in groups[q])
    }
    conditions = [
        z3.PbGe([(aw, 1)] + [(group_rows[i][6], 1) for i in range(5)], 3)
    ]
    for subset in range(1, 31):
        outside = {
            q
            for p in range(5) if subset >> p & 1
            for q in range(5) if not (subset >> q & 1)
            if tuple(sorted((p, q))) in group_edges
        }
        unions = [
            z3.Or(*(group_rows[i][j] for i in range(5) if subset >> i & 1))
            for j in range(7)
        ]
        conditions.append(
            z3.PbGe([(term, 1) for term in unions], 7 - len(outside))
        )
    return z3.And(*conditions)


def diagnose(model, rows, aw_value, fedges):
    """Return tight original sets and the failed conditions after each edge."""
    tight = []
    for subset in range(1, (1 << ORDER) - 1):
        outside = {
            y
            for i in range(ORDER) if subset >> i & 1
            for y in range(ORDER) if not (subset >> y & 1)
            if tuple(sorted((i, y))) in fedges
        }
        union = 0
        for i in range(ORDER):
            if subset >> i & 1:
                union |= rows[i]
        phi = len(outside) + union.bit_count()
        if phi == 7:
            tight.append({
                "set": [i for i in range(ORDER) if subset >> i & 1],
                "outside": sorted(outside),
                "boundary_mask": union,
            })
    failures = {}
    for edge in sorted(fedges):
        groups = contraction_groups(edge)
        crows = [0] * 5
        for p, group in enumerate(groups):
            for i in group:
                crows[p] |= rows[i]
        gedges = {
            tuple(sorted((p, q)))
            for p in range(5) for q in range(p + 1, 5)
            if any(tuple(sorted((i, j))) in fedges for i in groups[p] for j in groups[q])
        }
        bad = []
        terminal = int(aw_value) + sum(bool(row & 64) for row in crows)
        if terminal < 3:
            bad.append({"terminal": terminal})
        for subset in range(1, 31):
            outside = {
                q
                for p in range(5) if subset >> p & 1
                for q in range(5) if not (subset >> q & 1)
                if tuple(sorted((p, q))) in gedges
            }
            union = 0
            for p, row in enumerate(crows):
                if subset >> p & 1:
                    union |= row
            phi = len(outside) + union.bit_count()
            if phi < 7:
                bad.append({
                    "groups": [list(groups[p]) for p in range(5) if subset >> p & 1],
                    "phi": phi,
                })
        failures[f"{edge[0]}-{edge[1]}"] = bad
    return tight, failures


def main():
    records = []
    for index, (name, fedges) in enumerate(TYPES.items()):
        solver = z3.Solver()
        x = [[z3.Bool(f"{name}_{i}_{j}") for j in range(7)] for i in range(ORDER)]
        aw = z3.Bool(f"{name}_aw")
        base_constraints(solver, x, aw, fedges)
        for edge in fedges:
            solver.add(z3.Not(safe_contraction(x, aw, fedges, edge)))
        outcome = solver.check()
        if outcome == z3.unsat:
            records.append({"type": name, "status": "unsat"})
            print(index, name, "UNSAT", flush=True)
            continue
        assert outcome == z3.sat
        model = solver.model()
        rows = [
            sum(1 << j for j in range(7) if z3.is_true(model.eval(x[i][j])))
            for i in range(ORDER)
        ]
        aw_value = z3.is_true(model.eval(aw))
        tight, failures = diagnose(model, rows, aw_value, fedges)
        records.append({
            "type": name,
            "status": "sat",
            "internal_edges": [list(edge) for edge in sorted(fedges)],
            "aw": aw_value,
            "rows": rows,
            "tight_sets": tight,
            "contraction_failures": failures,
        })
        print(index, name, "SAT", rows, "aw", aw_value, flush=True)
    with open("portal_order6_contraction_obstruction.json", "w", encoding="utf-8") as target:
        json.dump({"format": 1, "records": records}, target, indent=2)


if __name__ == "__main__":
    main()
