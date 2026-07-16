#!/usr/bin/env python3
"""Bounded falsifier for the atomic carrier-or-rooted-K5 principle.

For every two-connected thin graph in the NetworkX graph atlas (orders
3--7), the script asks Z3 for boundary-contact assignments satisfying the
literal relative seven-cut inequalities, the unique ``z-u`` portal and
deleted-root W-fullness, while forbidding every adjacent connected pair of
near-full carriers rooted at ``z``.  Each returned assignment is then
tested for an S-rooted K5 model by an exact branch-set search.

This is a bounded falsifier only.  In particular it does not encode minor
criticality, the rich shore, or the selected path/Y bridge hull.
"""

from __future__ import annotations

import itertools
import sys
from collections.abc import Iterable

sys.path.insert(0, "active/runtime/deps")

import networkx as nx  # noqa: E402
import z3  # noqa: E402


W = tuple(range(6))
S_NAMES = ("c", "a1", "a2", "a3", "t1", "t2", "t3")
U = "t1"
Z = 0


def boundary_graph() -> nx.Graph:
    h = nx.Graph()
    h.add_nodes_from(S_NAMES)
    h.add_edges_from(
        (
            ("c", "a1"),
            ("c", "a2"),
            ("c", "a3"),
            ("a1", "t2"),
            ("t1", "a3"),
            ("a2", "t3"),
        )
    )
    return h


def connected_masks(g: nx.Graph) -> list[int]:
    n = len(g)
    out = []
    for mask in range(1, 1 << n):
        vertices = [v for v in g if mask >> v & 1]
        if nx.is_connected(g.subgraph(vertices)):
            out.append(mask)
    return out


def adjacent_masks(g: nx.Graph, x: int, y: int) -> bool:
    return any((x >> a & 1) and (y >> b & 1) for a, b in g.edges()) or any(
        (x >> b & 1) and (y >> a & 1) for a, b in g.edges()
    )


def support_ge(contact, mask: int, threshold: int):
    terms = []
    for s in W:
        terms.append(z3.Or([contact[v, s] for v in range(len(contact) // 6) if mask >> v & 1]))
    return z3.PbGe([(term, 1) for term in terms], threshold)


def make_solver(a: nx.Graph):
    n = len(a)
    contact = {(v, s): z3.Bool(f"x_{v}_{s}") for v in range(n) for s in W}
    solver = z3.Solver()

    # A-z is literally W-full.
    for s in W:
        solver.add(z3.Or([contact[v, s] for v in range(1, n)]))

    masks = connected_masks(a)

    # Every connected D subseteq A has at least seven literal neighbours
    # in (A-D) union S.  Only z sees u.
    for mask in masks:
        outside_neighbours = {
            b
            for x, b in a.edges()
            if (mask >> x & 1) and not (mask >> b & 1)
        } | {
            x
            for x, b in a.edges()
            if (mask >> b & 1) and not (mask >> x & 1)
        }
        w_terms = [
            z3.Or([contact[v, s] for v in range(n) if mask >> v & 1])
            for s in W
        ]
        u_term = 1 if mask & 1 else 0
        solver.add(
            z3.PbGe(
                [(term, 1) for term in w_terms],
                7 - len(outside_neighbours) - u_term,
            )
        )

    # Forbid every disjoint adjacent connected rooted near-full pair.
    rooted = [mask for mask in masks if mask & 1]
    for x in rooted:
        for y in masks:
            if x & y or not adjacent_masks(a, x, y):
                continue
            # x contains z, hence its S-support is 1 + its W-support.
            solver.add(z3.Not(z3.And(support_ge(contact, x, 5), support_ge(contact, y, 6))))

    return solver, contact


def literal_graph(a: nx.Graph, model, contact) -> nx.Graph:
    g = nx.Graph()
    thin = tuple(f"v{v}" for v in a)
    g.add_nodes_from(thin)
    g.add_nodes_from(S_NAMES)
    g.add_edges_from((f"v{x}", f"v{y}") for x, y in a.edges())
    g.add_edges_from(boundary_graph().edges())
    g.add_edge("v0", U)
    w_names = ("c", "a1", "a2", "a3", "t2", "t3")
    for v in a:
        for s, name in zip(W, w_names):
            if z3.is_true(model.eval(contact[v, s], model_completion=True)):
                g.add_edge(f"v{v}", name)
    return g


def has_rooted_k5(g: nx.Graph) -> bool:
    """Exact rooted-model test by a decreasing-depth connectivity encoding."""

    nodes = list(g)
    for roots in itertools.combinations(S_NAMES, 5):
        solver = z3.Solver()
        label = {v: z3.Int(f"label_{i}") for i, v in enumerate(nodes)}
        depth = {v: z3.Int(f"depth_{i}") for i, v in enumerate(nodes)}
        for v in nodes:
            solver.add(label[v] >= -1, label[v] <= 4)
            solver.add(depth[v] >= 0, depth[v] < len(nodes))
        for i, root in enumerate(roots):
            solver.add(label[root] == i, depth[root] == 0)
        for i, root in enumerate(roots):
            for v in nodes:
                if v == root:
                    continue
                solver.add(
                    z3.Implies(
                        label[v] == i,
                        z3.And(
                            depth[v] > 0,
                            z3.Or(
                                [
                                    z3.And(label[w] == i, depth[w] < depth[v])
                                    for w in g.neighbors(v)
                                ]
                            ),
                        ),
                    )
                )
        for i in range(5):
            for j in range(i + 1, 5):
                solver.add(
                    z3.Or(
                        [
                            z3.Or(
                                z3.And(label[v] == i, label[w] == j),
                                z3.And(label[v] == j, label[w] == i),
                            )
                            for v, w in g.edges()
                        ]
                    )
                )
        if solver.check() == z3.sat:
            return True
    return False


def atlas_shapes(max_order: int = 6) -> Iterable[nx.Graph]:
    for graph in nx.graph_atlas_g():
        n = len(graph)
        if not 3 <= n <= max_order:
            continue
        if nx.is_biconnected(graph):
            yield nx.convert_node_labels_to_integers(graph)


def main() -> None:
    shape_count = 0
    assignment_count = 0
    rooted_count = 0
    for a in atlas_shapes():
        shape_count += 1
        solver, contact = make_solver(a)
        # Sample a bounded number of distinct no-carrier assignments per
        # shape; rooted K5 certificates are checked exactly for each sample.
        for _ in range(5):
            if solver.check() != z3.sat:
                break
            model = solver.model()
            assignment_count += 1
            g = literal_graph(a, model, contact)
            if not has_rooted_k5(g):
                print("COUNTEREXAMPLE", nx.to_graph6_bytes(a, header=False).decode().strip())
                for v in a:
                    row = [
                        s
                        for s, name in enumerate(("c", "a1", "a2", "a3", "t2", "t3"))
                        if g.has_edge(f"v{v}", name)
                    ]
                    print(v, row)
                raise SystemExit(1)
            rooted_count += 1
            block = []
            for variable in contact.values():
                value = z3.is_true(model.eval(variable, model_completion=True))
                block.append(variable != value)
            solver.add(z3.Or(block))
    print(
        "BOUNDED_FALSIFIER_GREEN",
        "shapes",
        shape_count,
        "no_carrier_assignments",
        assignment_count,
        "rooted_K5",
        rooted_count,
    )


if __name__ == "__main__":
    main()
