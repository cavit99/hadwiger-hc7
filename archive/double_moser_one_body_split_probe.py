#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "networkx",
#     "z3-solver",
# ]
# ///
"""Probe the one-body double-Moser portal-split obstruction.

The probe searches for a body R of order four which simultaneously has:

* the exact double-Moser boundary incidences;
* the relative seven-connectivity inequalities inside C={a,b}+R;
* the root-portal multiplicities forced by minimum degree;
* no connected a-b covering split whose ten-vertex quotient is K7-positive;
* global vertex-connectivity at least seven.

The last condition is imposed by a CEGIS loop: after each SAT model,
NetworkX returns a cut of order at most six and the solver requires an
edge across that particular residual disconnection.  The script is a
falsification probe, not a proof of unsatisfiability for unbounded R.
"""

from __future__ import annotations

from itertools import combinations, product
from typing import Iterable

import networkx as nx
import z3


MAXIMAL_BAD = (
    (0, 0, 1, 1, 3, 3),
    (0, 1, 0, 1, 3, 3),
    (0, 1, 1, 0, 3, 3),
    (0, 1, 1, 1, 2, 2),
    (1, 0, 0, 1, 3, 3),
    (1, 0, 1, 0, 3, 3),
    (1, 0, 1, 1, 2, 2),
    (1, 1, 0, 0, 3, 3),
    (1, 1, 0, 1, 1, 1),
    (1, 1, 1, 0, 1, 1),
)


def normalized_edge(left: str, right: str) -> tuple[str, str]:
    return tuple(sorted((left, right)))


def build_probe(body_order: int = 4):
    body = tuple(f"r{i}" for i in range(body_order))
    shore = ("a", "b", *body)
    boundary = ("v", "x1", "x2", "x3", "x4", "p", "q")
    all_vertices = ("u", *boundary, *shore)

    fixed_pairs = [
        ("u", "v"),
        *(("u", x) for x in ("x1", "x2", "x3", "x4", "p", "q")),
        *(("v", x) for x in ("x1", "x2", "x3", "x4", "a", "b")),
        ("x1", "x2"),
        ("x3", "x4"),
        ("a", "b"),
        ("p", "q"),
        ("a", "x1"),
        ("a", "x2"),
        ("b", "x3"),
        ("b", "x4"),
        ("p", "x3"),
        ("p", "x4"),
        ("q", "x1"),
        ("q", "x2"),
    ]
    fixed = {normalized_edge(*pair) for pair in fixed_pairs}

    optional: set[tuple[str, str]] = set()
    for left, right in combinations(shore, 2):
        pair = normalized_edge(left, right)
        if pair not in fixed:
            optional.add(pair)
    for outer in ("a", "b"):
        for exclusive in ("p", "q"):
            optional.add(normalized_edge(outer, exclusive))
    for vertex in body:
        for label in ("x1", "x2", "x3", "x4", "p", "q"):
            optional.add(normalized_edge(vertex, label))

    variables = {
        pair: z3.Bool("edge_" + "_".join(pair)) for pair in sorted(optional)
    }

    def edge(left: str, right: str):
        pair = normalized_edge(left, right)
        if pair in fixed:
            return z3.BoolVal(True)
        return variables.get(pair, z3.BoolVal(False))

    def connected(vertices: Iterable[str]):
        vertices = tuple(vertices)
        if len(vertices) <= 1:
            return z3.BoolVal(True)
        root = vertices[0]
        clauses = []
        for mask in range(1 << (len(vertices) - 1)):
            first = {root} | {
                vertices[index + 1]
                for index in range(len(vertices) - 1)
                if mask & (1 << index)
            }
            if len(first) == len(vertices):
                continue
            clauses.append(
                z3.Or(
                    [
                        edge(left, right)
                        for left in first
                        for right in vertices
                        if right not in first
                    ]
                )
            )
        return z3.And(clauses)

    def hits(vertices: Iterable[str], label: str):
        return z3.Or([edge(vertex, label) for vertex in vertices])

    def below_maximal_bad(bits, p_a, p_b, q_a, q_b, maximal):
        constraints = [
            z3.Not(bit) for bit, maximum in zip(bits, maximal[:4]) if not maximum
        ]
        for contact_a, contact_b, maximum in (
            (p_a, p_b, maximal[4]),
            (q_a, q_b, maximal[5]),
        ):
            if maximum == 1:
                constraints.extend((contact_a, z3.Not(contact_b)))
            elif maximum == 2:
                constraints.extend((z3.Not(contact_a), contact_b))
        return z3.And(constraints)

    solver = z3.Solver()
    solver.add(connected(body))
    solver.add(z3.Or([edge("a", vertex) for vertex in body]))
    solver.add(z3.Or([edge("b", vertex) for vertex in body]))

    for label in ("x1", "x2", "x3", "x4", "p", "q"):
        solver.add(z3.Or([edge(vertex, label) for vertex in body]))
    for root in ("x1", "x2", "x3", "x4"):
        solver.add(z3.PbGe([(edge(vertex, root), 1) for vertex in body], 2))

    # Relative seven-connectivity for every nonempty proper subset of C.
    for order in range(1, len(shore)):
        for subset_tuple in combinations(shore, order):
            subset = set(subset_tuple)
            terms = [
                z3.Or([edge(vertex, outside) for vertex in subset])
                for outside in shore
                if outside not in subset
            ]
            terms.extend(
                z3.Or([edge(vertex, label) for vertex in subset])
                for label in boundary
            )
            solver.add(z3.PbGe([(term, 1) for term in terms], 7))

    # Atlas A contains old outer b (fixed contacts x3,x4); atlas B contains
    # old outer a (fixed contacts x1,x2).  This orientation is essential.
    for assignment in product((0, 1), repeat=body_order):
        side_a = ["b", *(v for v, side in zip(body, assignment) if side == 0)]
        side_b = ["a", *(v for v, side in zip(body, assignment) if side == 1)]
        bits = (
            hits(side_a, "x1"),
            hits(side_a, "x2"),
            hits(side_b, "x3"),
            hits(side_b, "x4"),
        )
        p_a, p_b = hits(side_a, "p"), hits(side_b, "p")
        q_a, q_b = hits(side_a, "q"), hits(side_b, "q")
        negative = z3.Or(
            [
                below_maximal_bad(bits, p_a, p_b, q_a, q_b, maximal)
                for maximal in MAXIMAL_BAD
            ]
        )
        solver.add(
            z3.Implies(z3.And(connected(side_a), connected(side_b)), negative)
        )

    return solver, variables, fixed, all_vertices


def graph_from_model(model, variables, fixed, vertices):
    graph = nx.Graph()
    graph.add_nodes_from(vertices)
    graph.add_edges_from(fixed)
    graph.add_edges_from(
        pair
        for pair, variable in variables.items()
        if z3.is_true(model.eval(variable))
    )
    return graph


def main() -> None:
    solver, variables, fixed, vertices = build_probe(body_order=4)
    for iteration in range(500):
        result = solver.check()
        if result != z3.sat:
            print(f"probe result: {result} after {iteration} connectivity cuts")
            return

        graph = graph_from_model(solver.model(), variables, fixed, vertices)
        connectivity = nx.node_connectivity(graph)
        if connectivity >= 7:
            print(f"found globally 7-connected atlas-negative architecture at {iteration=}")
            print(f"vertices={len(graph)} edges={graph.number_of_edges()}")
            for vertex in ("a", "b", "r0", "r1", "r2", "r3"):
                print(vertex, " ".join(sorted(graph.neighbors(vertex))))
            return

        cut = nx.minimum_node_cut(graph)
        residual = graph.copy()
        residual.remove_nodes_from(cut)
        components = list(nx.connected_components(residual))
        first = components[0]
        rest = set().union(*components[1:])
        repairs = [
            variables[normalized_edge(left, right)]
            for left in first
            for right in rest
            if normalized_edge(left, right) in variables
        ]
        if not repairs:
            solver.add(z3.BoolVal(False))
        else:
            solver.add(z3.Or(repairs))

    raise RuntimeError("CEGIS iteration limit reached")


if __name__ == "__main__":
    main()
