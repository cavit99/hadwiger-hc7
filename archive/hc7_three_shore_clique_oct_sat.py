#!/usr/bin/env python3
"""Certified finite lemma for the three-full-shore HC7 interface.

For n=7,8,9, search for a graph F such that

* F is not 3-colourable;
* F-Z has no K4 minor for every two-set Z; and
* no clique K has bipartite complement F-K.

The K4-minor clauses are exact: since K4 is subcubic, a graph contains a
K4 minor iff it contains a subdivision of K4.  Every labelled subdivision
on each (n-2)-set is generated explicitly and its edge set is forbidden.

Expected result: n=8 and n=9 are UNSAT.  At n=7 every solution is the
Moser spindle; a labelled Moser spindle is supplied as a positive witness.
The latter uniqueness is checked separately with the complete NetworkX
seven-vertex graph atlas in ``check_order_seven``.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
import sys

import networkx as nx

# The workspace venv carries NetworkX, while the locally installed Z3 wheel
# is in Homebrew's matching Python 3.14 site-packages.
sys.path.append("/opt/homebrew/lib/python3.14/site-packages")
import z3


def edge(u: int, v: int) -> tuple[int, int]:
    return (u, v) if u < v else (v, u)


def subdivision_edge_sets(vertices: tuple[int, ...]) -> set[frozenset[tuple[int, int]]]:
    """All edge-minimal labelled subdivisions of K4 inside ``vertices``."""
    out: set[frozenset[tuple[int, int]]] = set()
    for branch in combinations(vertices, 4):
        branch_edges = tuple(combinations(branch, 2))
        internal = tuple(v for v in vertices if v not in branch)
        # A witness may omit vertices.  A permutation gives the order of all
        # used internal vertices; assigning them to one of the six K4 edges
        # gives the six internally disjoint paths.  Every family of six
        # ordered lists has an interleaving, so this generates every witness.
        for used_count in range(len(internal) + 1):
            for ordered in permutations(internal, used_count):
                for labels in product(range(6), repeat=used_count):
                    paths: list[list[int]] = [[] for _ in range(6)]
                    for v, label in zip(ordered, labels):
                        paths[label].append(v)
                    witness: set[tuple[int, int]] = set()
                    for (a, b), middle in zip(branch_edges, paths):
                        route = [a, *middle, b]
                        witness.update(edge(x, y) for x, y in zip(route, route[1:]))
                    out.add(frozenset(witness))
    return out


def solver_for_order(
    n: int,
    critical_core_order: int,
    degree_case: str | None = None,
    forbid_moser_labelling: bool = False,
) -> tuple[z3.Solver, dict[tuple[int, int], z3.BoolRef], dict[str, int]]:
    vertices = tuple(range(n))
    e = {uv: z3.Bool(f"e_{uv[0]}_{uv[1]}") for uv in combinations(vertices, 2)}
    solver = z3.Solver()

    # A non-3-colourable graph has a 4-critical subgraph.  The support
    # condition forces that core to have n or n-1 vertices.  We solve those
    # two cases separately.  In the n-1 case relabelling lets the sole vertex
    # outside the core be n-1.
    assert critical_core_order in (n - 1, n)
    core = tuple(range(critical_core_order))

    # The core is not 3-colourable.  Each of its 3^q maps must have a
    # monochromatic edge.
    colour_clauses = 0
    for colouring in product(range(3), repeat=critical_core_order):
        mono = [e[uv] for uv in combinations(core, 2)
                if colouring[uv[0]] == colouring[uv[1]]]
        solver.add(z3.Or(mono))
        colour_clauses += 1

    # Explicit consequences used only as SAT propagation aids.
    for v in core:
        solver.add(z3.PbGe([(e[edge(v, u)], 1) for u in core if u != v], 3))

    # Symmetry breaking for the only expensive order-nine cases.  If the
    # core has order eight, its edge bound gives a degree-three vertex.  If
    # it has order nine, either it has a degree-three vertex or the global
    # induced-seven edge bound makes it exactly 4-regular.  Relabel that
    # vertex as 0 and its neighbourhood as an initial segment.
    if degree_case == "three":
        assert critical_core_order >= 4
        for u in core[1:]:
            solver.add(e[edge(0, u)] if u <= 3 else z3.Not(e[edge(0, u)]))
    elif degree_case == "four_regular":
        assert critical_core_order == 9
        for v in core:
            solver.add(z3.PbEq([(e[edge(v, u)], 1) for u in core if u != v], 4))
        for u in core[1:]:
            solver.add(e[edge(0, u)] if u <= 4 else z3.Not(e[edge(0, u)]))
    else:
        assert degree_case is None
    for deleted in combinations(vertices, 2):
        remain = tuple(v for v in vertices if v not in deleted)
        # K4-minor-free graphs on r vertices have at most 2r-3 edges.
        solver.add(z3.PbLe([(e[uv], 1) for uv in combinations(remain, 2)],
                           2 * len(remain) - 3))

    # Every deletion of two vertices is K4-minor-free.  Generate the union
    # of all labelled subdivisions supported on at most n-2 vertices and
    # forbid every corresponding edge conjunction.  Deduplication across
    # the deletion pairs is substantial at orders eight and nine.
    witnesses: set[frozenset[tuple[int, int]]] = set()
    for deleted in combinations(vertices, 2):
        remain = tuple(v for v in vertices if v not in deleted)
        witnesses.update(subdivision_edge_sets(remain))
    for witness in witnesses:
        solver.add(z3.Or([z3.Not(e[uv]) for uv in witness]))

    colouring_constraints = 0

    def add_colouring(subset: tuple[int, ...], colours: int, tag: str) -> None:
        nonlocal colouring_constraints
        cv = {(v, a): z3.Bool(f"c_{tag}_{v}_{a}")
              for v in subset for a in range(colours)}
        for v in subset:
            solver.add(z3.PbEq([(cv[v, a], 1) for a in range(colours)], 1))
            colouring_constraints += 1
        for u, v in combinations(subset, 2):
            for a in range(colours):
                solver.add(z3.Or(z3.Not(e[edge(u, v)]),
                                 z3.Not(cv[u, a]), z3.Not(cv[v, a])))
                colouring_constraints += 1

    # The whole boundary is known to be four-colourable.
    add_colouring(vertices, 4, "all4")
    for v in core:
        add_colouring(tuple(x for x in core if x != v), 3, f"crit{v}")

    # There is no clique odd-cycle transversal K.  It is enough to consider
    # |K|<=4: a larger K contains a literal K4, already forbidden above.
    # For every candidate K and every bipartition A,B of V-K, forbid the
    # conjunction "K is a clique and A,B are independent".
    oct_clauses = 0
    for k_size in range(5):
        for K in combinations(vertices, k_size):
            rest = tuple(v for v in vertices if v not in K)
            # Fix the first remaining vertex in A to quotient A/B symmetry.
            for bits_tail in product((0, 1), repeat=max(0, len(rest) - 1)):
                bits = (0, *bits_tail) if rest else ()
                clause = [z3.Not(e[edge(x, y)]) for x, y in combinations(K, 2)]
                for side in (0, 1):
                    part = [v for v, bit in zip(rest, bits) if bit == side]
                    clause.extend(e[edge(x, y)] for x, y in combinations(part, 2))
                solver.add(z3.Or(clause))
                oct_clauses += 1

    if forbid_moser_labelling:
        moser = {
            edge(*uv)
            for uv in ((0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
                       (2, 6), (3, 4), (3, 5), (4, 5), (5, 6))
        }
        # Forbids this one labelling only.  Atlas is used for isomorphism
        # uniqueness at order seven; this switch is merely a smoke test.
        solver.add(z3.Or([z3.Not(e[uv]) if uv in moser else e[uv] for uv in e]))

    stats = {
        "colour_clauses": colour_clauses,
        "minor_clauses": len(witnesses),
        "colouring_constraints": colouring_constraints,
        "oct_clauses": oct_clauses,
    }
    return solver, e, stats


def chromatic_at_most(g: nx.Graph, k: int) -> bool:
    order = sorted(g, key=lambda v: -g.degree(v))
    colour: dict[int, int] = {}

    def rec(pos: int) -> bool:
        if pos == len(order):
            return True
        v = order[pos]
        used = {colour[w] for w in g[v] if w in colour}
        for value in range(k):
            if value not in used:
                colour[v] = value
                if rec(pos + 1):
                    return True
                del colour[v]
        return False

    return rec(0)


def has_k4_minor(g: nx.Graph) -> bool:
    vertices = tuple(g)
    for witness in subdivision_edge_sets(vertices):
        if all(g.has_edge(*uv) for uv in witness):
            return True
    return False


def has_clique_oct(g: nx.Graph) -> bool:
    for k_size in range(5):
        for K in combinations(g, k_size):
            if all(g.has_edge(x, y) for x, y in combinations(K, 2)):
                if nx.is_bipartite(g.subgraph(set(g) - set(K))):
                    return True
    return False


def check_order_seven() -> None:
    candidates = []
    for g in nx.graph_atlas_g():
        if len(g) != 7 or chromatic_at_most(g, 3):
            continue
        if any(has_k4_minor(g.subgraph(set(g) - set(z)).copy())
               for z in combinations(g, 2)):
            continue
        if not has_clique_oct(g):
            candidates.append(g)
    print("order7 atlas exceptional count", len(candidates))
    for g in candidates:
        print(" order7 exception edges", sorted(edge(x, y) for x, y in g.edges()))
        print(" degree sequence", sorted(dict(g.degree()).values()))
    assert len(candidates) == 1
    assert g.number_of_edges() == 11
    assert sorted(dict(g.degree()).values()) == [3, 3, 3, 3, 3, 3, 4]


def main() -> None:
    check_order_seven()
    for n in (8,):
        for core_order in (n - 1, n):
            solver, _, stats = solver_for_order(n, core_order)
            result = solver.check()
            print("order", n, "critical core", core_order, stats, "result", result)
            assert result == z3.unsat
    cases = ((8, "three"), (9, "three"), (9, "four_regular"))
    for core_order, degree_case in cases:
        solver, _, stats = solver_for_order(9, core_order, degree_case)
        result = solver.check()
        print("order 9 critical core", core_order, "degree case", degree_case,
              stats, "result", result)
        assert result == z3.unsat


if __name__ == "__main__":
    main()
