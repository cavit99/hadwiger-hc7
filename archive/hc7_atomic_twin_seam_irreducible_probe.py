#!/usr/bin/env python3
"""Lazy search for a genuinely static-return-irreducible twin seam.

Unlike the older separating-decoder falsifier, this probe does not encode
all carrier blockers eagerly and does not ask for any lock before the
static kernel survives.  Each SAT contact map is inspected literally; if
it has an adaptive carrier return, only that return is blocked.  A printed
survivor is therefore a suitable substrate for the later response search.
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


def load_base():
    path = HERE / "hc7_atomic_twin_seam_separating_decoder_falsifier.py"
    spec = importlib.util.spec_from_file_location("twin_base", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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
        for literal in allowed[vertex]
    }

    def edge(vertex, literal):
        if literal == base.U:
            return z3.BoolVal(vertex == base.ROOT)
        return contact.get((vertex, literal), z3.BoolVal(False))

    solver = z3.Solver()
    for literal in base.TD:
        solver.add(z3.Or(*(edge(vertex, literal) for vertex in base.D)))
    for literal in base.TE:
        solver.add(z3.Or(*(edge(vertex, literal) for vertex in base.E)))
    for literal in base.I:
        solver.add(z3.Or(*(edge(vertex, literal) for vertex in base.Z)))
    for literal in set(base.S) - {base.U}:
        solver.add(
            z3.Or(*(edge(vertex, literal) for vertex in base.A if vertex != base.ROOT))
        )

    connected = base.connected_subsets(thin, base.A)
    for chosen in connected:
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
        solver.add(z3.PbGe([(term, 1) for term in terms], 7 - len(internal)))

    boundary = nx.Graph()
    boundary.add_nodes_from(base.S)
    boundary.add_edges_from(base.H_EDGES)
    partitions = base.adaptive_partitions(boundary)
    pairs = [
        (left, right)
        for left in connected
        for right in connected
        if left.isdisjoint(right)
        and any(thin.has_edge(x, y) for x in left for y in right)
    ]
    # Root-containing allocations are the narrowest live mechanism and are
    # checked first; the uniform theorem permits the remaining pairs too.
    pairs.sort(key=lambda pair: base.ROOT not in pair[0] and base.ROOT not in pair[1])

    def support(model, carrier):
        answer = set()
        for literal in base.S:
            if any(
                z3.is_true(model.eval(edge(vertex, literal), model_completion=True))
                for vertex in carrier
            ):
                answer.add(literal)
        return frozenset(answer)

    cap = int(os.environ.get("HC7_LAZY_CAP", "5000"))
    for iteration in range(1, cap + 1):
        status = solver.check()
        if status != z3.sat:
            print(
                "NO_STATIC_SURVIVOR",
                "status",
                status,
                "blocked_returns",
                iteration - 1,
                "shape",
                base.SHAPE,
                "profile",
                base.PROFILE,
            )
            return
        model = solver.model()
        supports = {carrier: support(model, carrier) for carrier in connected}
        witness = None
        for left, right in pairs:
            left_support = supports[left]
            right_support = supports[right]
            for first, second, reservoir in partitions:
                if first <= left_support and second <= right_support:
                    witness = (left, right, first, second, reservoir)
                    break
                if second <= left_support and first <= right_support:
                    witness = (left, right, second, first, reservoir)
                    break
            if witness is not None:
                break

        if witness is None:
            print(
                "STATIC_IRREDUCIBLE_SURVIVOR",
                "iteration",
                iteration,
                "shape",
                base.SHAPE,
                "profile",
                base.PROFILE,
            )
            print(
                "contacts",
                {
                    vertex: tuple(
                        literal
                        for literal in base.S
                        if z3.is_true(
                            model.eval(edge(vertex, literal), model_completion=True)
                        )
                    )
                    for vertex in base.A
                },
            )
            return

        left, right, first, second, _ = witness

        def hits(carrier, literal):
            return z3.Or(*(edge(vertex, literal) for vertex in carrier))

        solver.add(
            z3.Not(
                z3.And(
                    *(hits(left, literal) for literal in first),
                    *(hits(right, literal) for literal in second),
                )
            )
        )

    print("LAZY_CAP_REACHED", cap, "shape", base.SHAPE, "profile", base.PROFILE)


if __name__ == "__main__":
    main()
