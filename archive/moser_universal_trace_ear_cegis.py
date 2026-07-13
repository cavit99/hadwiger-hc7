#!/usr/bin/env python3
"""CEGIS for a universal-trace long-ear Moser boundary gadget.

The exterior graph is the two-overlapping-palette template from
``moser_palette_wall_ear_probe.py``; only its boundary contacts vary.
We require all ten exact star traces, a genuine palette wall, minimum
degree seven, seven-connectivity, and a minimum 1--3 connector of order
at least three.  The template has a fixed K6, so any seven-connected
solution deliberately violates only K7-minor exclusion.  Finding one
isolates the force of that final hypothesis; UNSAT would isolate a
universal-trace ear exchange inside the template.
"""

from __future__ import annotations

import itertools

from z3 import And, Bool, If, Implies, Int, Not, Or, Solver, Sum, is_true

import moser_palette_wall_ear_probe as base


S = tuple(range(7))
C = base.C
V = ("v",) + S + C
G0 = base.build()
INTERNAL = tuple(
    (x, y) for x, y in itertools.combinations(C, 2) if G0.has(x, y)
)
NONEDGES = tuple(
    pair for pair in itertools.combinations(S, 2) if not G0.has(*pair)
)
CORE_MAPS = tuple(base.canonical_core_maps(G0))


def contact_vars() -> dict[tuple[int, object], object]:
    return {(s, x): Bool(f"c_{s}_{x}") for s in S for x in C}


def add_static_constraints(solver: Solver, contact: dict):
    # Every boundary root sees the sole exterior.
    for s in S:
        solver.add(Or([contact[s, x] for x in C]))

    # Minimum degree seven at exterior and boundary vertices.  The apex has
    # degree exactly seven already.
    internal_degree = {
        x: sum(x in edge for edge in INTERNAL) for x in C
    }
    for x in C:
        solver.add(
            internal_degree[x]
            + Sum([If(contact[s, x], 1, 0) for s in S])
            >= 7
        )
    boundary_degree = {
        s: 1 + len(base.BOUNDARY_ADJ[s]) for s in S
    }
    for s in S:
        solver.add(
            boundary_degree[s]
            + Sum([If(contact[s, x], 1, 0) for x in C])
            >= 7
        )

    # No order-one or order-two connected 1--3 carrier in C.
    for x in C:
        solver.add(Not(And(contact[1, x], contact[3, x])))
    for x, y in INTERNAL:
        solver.add(Not(And(contact[1, x], contact[3, y])))
        solver.add(Not(And(contact[1, y], contact[3, x])))

    # All ten exact star-contraction traces.  The boundary colors are fixed
    # canonically for each trace; the exterior colors are existential.
    trace_acts = []
    for trace_index, pair in enumerate(NONEDGES):
        active = Bool(f"trace_{pair[0]}_{pair[1]}")
        trace_acts.append(active)
        remaining = [s for s in S if s not in pair]
        boundary = {pair[0]: 0, pair[1]: 0}
        boundary.update({s: i + 1 for i, s in enumerate(remaining)})
        colour = {
            x: Int(f"t_{trace_index}_{x}") for x in C
        }
        for x in C:
            solver.add(Implies(active, And(colour[x] >= 0, colour[x] < 6)))
        for x, y in INTERNAL:
            solver.add(Implies(active, colour[x] != colour[y]))
        for s in S:
            for x in C:
                solver.add(
                    Implies(And(active, contact[s, x]),
                            colour[x] != boundary[s])
                )
    return tuple(trace_acts)


def rows(model, contact: dict) -> dict[int, set[object]]:
    return {
        s: {
            x for x in C
            if is_true(model.eval(contact[s, x], model_completion=True))
        }
        for s in S
    }


def candidate_adjacency(contact_rows: dict[int, set[object]]):
    adjacency = {x: set() for x in V}
    for x, y in base.MOSER:
        adjacency[x].add(y)
        adjacency[y].add(x)
    for s in S:
        adjacency["v"].add(s)
        adjacency[s].add("v")
    for x, y in INTERNAL:
        adjacency[x].add(y)
        adjacency[y].add(x)
    for s, row in contact_rows.items():
        for x in row:
            adjacency[s].add(x)
            adjacency[x].add(s)
    return adjacency


def components(adjacency, remaining: set[object]):
    unseen = set(remaining)
    answer = []
    while unseen:
        root = unseen.pop()
        reached = {root}
        stack = [root]
        while stack:
            x = stack.pop()
            for y in adjacency[x] & unseen:
                unseen.remove(y)
                reached.add(y)
                stack.append(y)
        answer.append(reached)
    return answer


def small_cut(adjacency):
    vertex_set = set(V)
    for size in range(7):
        for cut_tuple in itertools.combinations(V, size):
            cut = set(cut_tuple)
            pieces = components(adjacency, vertex_set - cut)
            if len(pieces) > 1:
                return cut, pieces
    return None


def boundary_violations(contact_rows: dict[int, set[object]]):
    # The fixed exterior contains K6, so its proper six-colourings are the
    # 78 color-permutation orbits already enumerated by the base verifier.
    answer = []
    for core_map in CORE_MAPS:
        lists = {
            s: set(range(6)) - {core_map[x] for x in contact_rows[s]}
            for s in S
        }
        if any(not allowed for allowed in lists.values()):
            continue
        assignment: dict[int, int] = {}

        def search():
            if len(assignment) == 7:
                if len(set(assignment.values())) <= 5:
                    return dict(assignment)
                return None
            s = min(
                (z for z in S if z not in assignment),
                key=lambda z: len(
                    lists[z]
                    - {assignment[n] for n in base.BOUNDARY_ADJ[z]
                       if n in assignment}
                ),
            )
            forbidden = {
                assignment[n] for n in base.BOUNDARY_ADJ[s]
                if n in assignment
            }
            for value in lists[s] - forbidden:
                assignment[s] = value
                result = search()
                if result is not None:
                    return result
                del assignment[s]
            return None

        boundary = search()
        if boundary is not None:
            answer.append((core_map, boundary))
    return answer


def main() -> None:
    solver = Solver()
    contact = contact_vars()
    trace_acts = add_static_constraints(solver, contact)
    palette_blocks = 0
    cut_blocks = 0
    seen_palette_blocks = set()

    while True:
        status = solver.check(*trace_acts)
        if status.r != 1:
            if status.r == -1:
                print(
                    "UNSAT", "palette_blocks", palette_blocks,
                    "cut_blocks", cut_blocks,
                    "trace_core", [str(x) for x in solver.unsat_core()],
                )
            else:
                print("UNKNOWN", solver.reason_unknown())
            return
        model = solver.model()
        contact_rows = rows(model, contact)

        violations = boundary_violations(contact_rows)
        if violations:
            added = 0
            for core_map, boundary in violations:
                key = frozenset(
                    (s, x) for s in S for x in C
                    if boundary[s] == core_map[x]
                )
                if not key:
                    raise AssertionError(
                        "fixed palette violation cannot be blocked"
                    )
                if key in seen_palette_blocks:
                    continue
                seen_palette_blocks.add(key)
                solver.add(Or([contact[s, x] for s, x in key]))
                palette_blocks += 1
                added += 1
            if not added:
                raise AssertionError("palette blocker loop")
            if palette_blocks // 1000 != (palette_blocks - added) // 1000:
                print("palette_blocks", palette_blocks, flush=True)
            continue

        adjacency = candidate_adjacency(contact_rows)
        cut_witness = small_cut(adjacency)
        if cut_witness is not None:
            cut, pieces = cut_witness
            first = pieces[0]
            rest = set(V) - cut - first
            blockers = []
            for s in S:
                for x in C:
                    if ((s in first and x in rest)
                            or (x in first and s in rest)):
                        blockers.append(contact[s, x])
            if not blockers:
                raise AssertionError(("unrepairable cut", cut, pieces))
            solver.add(Or(blockers))
            cut_blocks += 1
            continue

        print("SURVIVOR")
        print("palette_blocks", palette_blocks, "cut_blocks", cut_blocks)
        for s in S:
            print(s, *contact_rows[s])
        return


if __name__ == "__main__":
    main()
