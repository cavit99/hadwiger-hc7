#!/usr/bin/env python3
"""Extract a small static UNSAT core from the twin-seam contact shell.

This is a diagnostic companion to the separating-decoder falsifier.  It
deliberately omits every cut, colouring, minor and lock constraint.  The
only positive constraints are the literal twin supports and the
root-deletion fullness condition.  The negative constraints forbid each
legal adaptive two-carrier return.  An UNSAT core therefore identifies a
pure support allocation and must not be credited to the double-lock
decoder.
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
DEPS = HERE / "runtime" / "deps"
if DEPS.exists():
    sys.path.insert(0, str(DEPS))

import networkx as nx
import z3
from z3.z3util import get_vars


def load_base():
    path = HERE / "hc7_atomic_twin_seam_separating_decoder_falsifier.py"
    spec = importlib.util.spec_from_file_location("twin_base", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fmt_set(vertices) -> str:
    return "{" + ",".join(map(str, sorted(vertices, key=str))) + "}"


def main() -> None:
    base = load_base()
    thin = base.atomic_graph()
    allowed = {
        **{vertex: base.TD for vertex in base.D},
        **{vertex: base.TE - {base.U} for vertex in base.E},
        **{vertex: base.I for vertex in base.Z},
    }
    contact = {
        (vertex, literal): z3.Bool(f"x_{vertex}_{literal}")
        for vertex in base.A
        for literal in base.S
        if literal != base.U
    }

    def edge(vertex, literal):
        if literal == base.U:
            return z3.BoolVal(vertex == base.ROOT)
        if literal not in allowed[vertex]:
            return z3.BoolVal(False)
        return contact[vertex, literal]

    records: list[tuple[str, z3.BoolRef, str]] = []

    def record(name: str, formula, description: str) -> None:
        records.append((name, formula, description))

    for (vertex, literal), variable in contact.items():
        if literal not in allowed[vertex]:
            record(
                f"forbid_{vertex}_{literal}",
                z3.Not(variable),
                f"forbid contact {vertex}-{literal}",
            )

    for literal in base.TD:
        record(
            f"Dfull_{literal}",
            z3.Or(*(edge(vertex, literal) for vertex in base.D)),
            f"D contacts {literal}",
        )
    for literal in base.TE:
        record(
            f"Efull_{literal}",
            z3.Or(*(edge(vertex, literal) for vertex in base.E)),
            f"E contacts {literal}",
        )
    for literal in base.I:
        record(
            f"Zfull_{literal}",
            z3.Or(*(edge(vertex, literal) for vertex in base.Z)),
            f"Z contacts {literal}",
        )
    if base.ROOT_FULL:
        for literal in set(base.S) - {base.U}:
            record(
                f"rootfull_{literal}",
                z3.Or(
                    *(edge(vertex, literal) for vertex in base.A if vertex != base.ROOT)
                ),
                f"A-z contacts {literal}",
            )

    if os.environ.get("HC7_CORE_CUTS", "0") == "1":
        for number, chosen in enumerate(base.connected_subsets(thin, base.A), 1):
            internal = {
                vertex
                for vertex in base.A
                if vertex not in chosen
                and any(thin.has_edge(vertex, old) for old in chosen)
            }
            terms = [
                z3.Or(*(edge(vertex, literal) for vertex in chosen))
                for literal in base.S
            ]
            record(
                f"cut_{number}",
                z3.PbGe([(term, 1) for term in terms], 7 - len(internal)),
                (
                    f"relative cut X={fmt_set(chosen)} "
                    f"internal={fmt_set(internal)} needs={7-len(internal)}"
                ),
            )

    boundary = nx.Graph()
    boundary.add_nodes_from(base.S)
    boundary.add_edges_from(base.H_EDGES)
    connected = base.connected_subsets(thin, base.A)
    carrier_pairs = [
        (left, right)
        for left in connected
        for right in connected
        if base.ROOT in left
        and left.isdisjoint(right)
        and any(thin.has_edge(x, y) for x in left for y in right)
    ]
    partitions = base.adaptive_partitions(boundary)

    def hits(carrier, literal):
        return z3.Or(*(edge(vertex, literal) for vertex in carrier))

    index = 0
    for left, right in carrier_pairs:
        for first, second, reservoir in partitions:
            for orientation, seed_left, seed_right in (
                ("ab", first, second),
                ("ba", second, first),
            ):
                index += 1
                record(
                    f"block_{index}",
                    z3.Not(
                        z3.And(
                            *(hits(left, literal) for literal in seed_left),
                            *(hits(right, literal) for literal in seed_right),
                        )
                    ),
                    (
                        f"forbid return L={fmt_set(left)} R={fmt_set(right)} "
                        f"I={fmt_set(seed_left)} J={fmt_set(seed_right)} "
                        f"U={fmt_set(reservoir)} orientation={orientation}"
                    ),
                )

    by_name = {name: (formula, description) for name, formula, description in records}

    def solve(active_names):
        solver = z3.Solver()
        for name in active_names:
            formula, _ = by_name[name]
            solver.assert_and_track(formula, z3.Bool(name))
        return solver

    names = [name for name, _, _ in records]
    solver = solve(names)
    status = solver.check()
    print(
        "STATIC_CORE_STATUS",
        status,
        "shape",
        base.SHAPE,
        "profile",
        base.PROFILE,
        "constraints",
        len(names),
    )
    if status == z3.sat:
        model = solver.model()
        print(
            "SAT_CONTACTS",
            {
                vertex: tuple(
                    literal
                    for literal in base.S
                    if literal != base.U
                    and (vertex, literal) in contact
                    and z3.is_true(
                        model.eval(contact[vertex, literal], model_completion=True)
                    )
                )
                for vertex in base.A
            },
        )
        return
    if status != z3.unsat:
        return

    core = [str(atom) for atom in solver.unsat_core()]
    # Deletion-minimize the solver core.  The core is normally tiny, so a
    # linear pass is enough and keeps this probe transparent.
    changed = True
    while changed:
        changed = False
        for name in tuple(core):
            trial = [other for other in core if other != name]
            if solve(trial).check() == z3.unsat:
                core = trial
                changed = True
                break

    print("MINIMAL_CORE_SIZE", len(core))
    for name in core:
        print(name, by_name[name][1])

    relevant = sorted(
        {
            str(variable): variable
            for name in core
            for variable in get_vars(by_name[name][0])
        }.values(),
        key=str,
    )
    print("CORE_VARIABLES", len(relevant), *(str(variable) for variable in relevant))



if __name__ == "__main__":
    main()
