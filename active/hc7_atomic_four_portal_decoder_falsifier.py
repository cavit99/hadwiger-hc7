#!/usr/bin/env python3
"""CEGAR falsifier for the atomic alternating four-portal decoder.

The search uses actual two-connected thin graphs, literal boundary contacts,
all relative seven-cut inequalities, the unique ``z-u`` portal, deleted-root
W-fullness, an explicitly verified fully crossed rooted path core, and every
clique-reservoir bipartition on every connected prefix/suffix-type split.
Rooted K5 models are checked exactly.  A discovered model is fed back as a monotone
contact-edge blocking clause, so a completed UNSAT run is exhaustive for the
declared finite thin-shape family rather than a sample of contact masks.

The rich shore, global minor-critical colouring responses and the selected
bichromatic trace are not encoded.  A survivor is therefore a barrier to the
local decoder only, not a counterexample to HC7.
"""

from __future__ import annotations

import itertools
import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

DEPS = Path(__file__).resolve().parent / "runtime" / "deps"
if DEPS.exists():
    sys.path.insert(0, str(DEPS))

import networkx as nx  # noqa: E402
import z3  # noqa: E402


S = ("c", "a1", "a2", "a3", "t1", "t2", "t3")
U = "t1"
W = tuple(s for s in S if s != U)
Z = 0


def paired_tree() -> nx.Graph:
    h = nx.Graph()
    h.add_nodes_from(S)
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


def paired_c6_leaf() -> nx.Graph:
    # The connected non-tree width-two frontier in the audited census.
    h = nx.Graph()
    h.add_nodes_from(S)
    h.add_edges_from(
        (
            ("c", "a2"),
            ("c", "t3"),
            ("a1", "a2"),
            ("a1", "t2"),
            ("a3", "t2"),
            ("a3", "t3"),
            ("t1", "t3"),
        )
    )
    assert nx.is_bipartite(h)
    assert sorted(dict(h.degree()).values()) == [1, 2, 2, 2, 2, 2, 3]
    return h


FRONTIERS = {"paired_tree": paired_tree(), "paired_c6_leaf": paired_c6_leaf()}


def all_rooted_width_two_frontiers():
    """All rooted seven-vertex trees and rooted C6-plus-leaf graphs."""

    for h0 in nx.graph_atlas_g():
        is_tree = len(h0) == 7 and nx.is_tree(h0)
        is_c6_leaf = (
            len(h0) == 7
            and nx.is_connected(h0)
            and nx.is_bipartite(h0)
            and len(h0.edges()) == 7
            and sorted(dict(h0.degree()).values()) == [1, 2, 2, 2, 2, 2, 3]
            and sorted(map(len, nx.cycle_basis(h0))) == [6]
        )
        if not (is_tree or is_c6_leaf):
            continue
        kind = "tree" if is_tree else "c6_leaf"
        graph6 = nx.to_graph6_bytes(h0, header=False).decode().strip()
        for root in h0:
            others = [v for v in h0 if v != root]
            relabel = {root: U, **dict(zip(others, W))}
            yield f"{kind}:{graph6}:u={root}", nx.relabel_nodes(h0, relabel)


def connected_masks(a: nx.Graph) -> tuple[int, ...]:
    out = []
    for mask in range(1, 1 << len(a)):
        vertices = [v for v in a if mask >> v & 1]
        if nx.is_connected(a.subgraph(vertices)):
            out.append(mask)
    return tuple(out)


def mask_adjacent(a: nx.Graph, x: int, y: int) -> bool:
    return any(((x >> v) & 1) and ((y >> w) & 1) for v, w in a.edges()) or any(
        ((x >> w) & 1) and ((y >> v) & 1) for v, w in a.edges()
    )


def st_prefix_masks(a: nx.Graph) -> tuple[int, ...]:
    """All literal cuts occurring in an st-order with first vertex z."""

    cuts = set()
    remaining = tuple(v for v in a if v != Z)
    for tail in itertools.permutations(remaining):
        order = (Z, *tail)
        # A standard st-numbering is taken relative to an actual edge zt.
        if not a.has_edge(Z, order[-1]):
            continue
        if any(
            index > 0
            and not any(a.has_edge(v, order[j]) for j in range(index))
            for index, v in enumerate(order)
        ):
            continue
        if any(
            index < len(order) - 1
            and not any(a.has_edge(v, order[j]) for j in range(index + 1, len(order)))
            for index, v in enumerate(order)
        ):
            continue
        mask = 0
        for v in order[:-1]:
            mask |= 1 << v
            cuts.add(mask)
    return tuple(sorted(cuts))


def contact_term(contact, mask: int, s: str):
    if s == U:
        return z3.BoolVal(bool(mask & 1))
    return z3.Or([contact[v, s] for v in range(len(contact) // len(W)) if mask >> v & 1])


def proper_two_colourings(h: nx.Graph, retained: str | None):
    f_vertices = tuple(v for v in S if v != retained)
    for bits in itertools.product((0, 1), repeat=len(f_vertices)):
        colour = dict(zip(f_vertices, bits))
        if set(bits) != {0, 1}:
            continue
        if any(colour[v] == colour[w] for v, w in h.edges() if retained not in (v, w)):
            continue
        yield colour


def carrier_success_formula(contact, h: nx.Graph, left: int, right: int, retained):
    formulas = []
    carriers = (left, right)
    for colour in proper_two_colourings(h, retained):
        required = []
        for s, i in colour.items():
            required.append(contact_term(contact, carriers[i], s))
        # This is the corrected adaptive clique-reservoir criterion.  No
        # carrier-to-reservoir contact is imposed: the proper-minor response
        # may absorb the retained singleton into either seed block.
        formulas.append(z3.And(required))
    return z3.Or(formulas)


def make_solver(a: nx.Graph, h: nx.Graph):
    n = len(a)
    contact = {(v, s): z3.Bool(f"x_{v}_{s}") for v in a for s in W}
    solver = z3.Solver()
    masks = connected_masks(a)

    for s in W:
        solver.add(z3.Or([contact[v, s] for v in a if v != Z]))

    for mask in masks:
        outside = {
            w
            for v, w in a.edges()
            if (mask >> v & 1) and not (mask >> w & 1)
        } | {
            v
            for v, w in a.edges()
            if (mask >> w & 1) and not (mask >> v & 1)
        }
        support = [contact_term(contact, mask, s) for s in W]
        u_count = 1 if mask & 1 else 0
        solver.add(z3.PbGe([(term, 1) for term in support], 7 - len(outside) - u_count))

    full_mask = (1 << n) - 1
    carrier_pairs = 0
    return_states = 0
    mask_set = set(masks)
    for left in st_prefix_masks(a):
        right = full_mask ^ left
        if not right or right not in mask_set or not mask_adjacent(a, left, right):
            continue
        # The cuts are generated from literal st-orders, rather than inferred
        # merely from connectedness.  Boundary labels are still not silently
        # treated as distinct portal vertices.
        carrier_pairs += 1
        for retained in (None, *S):
            formula = carrier_success_formula(contact, h, left, right, retained)
            if not z3.is_false(formula):
                solver.add(z3.Not(formula))
                return_states += 1
    return solver, contact, carrier_pairs, return_states


def literal_closed_graph(a: nx.Graph, h: nx.Graph, model, contact) -> nx.Graph:
    g = nx.Graph()
    g.add_nodes_from(f"v{v}" for v in a)
    g.add_nodes_from(S)
    g.add_edges_from((f"v{v}", f"v{w}") for v, w in a.edges())
    g.add_edges_from(h.edges())
    g.add_edge("v0", U)
    for (v, s), variable in contact.items():
        if z3.is_true(model.eval(variable, model_completion=True)):
            g.add_edge(f"v{v}", s)
    return g


def exact_rooted_k5(g: nx.Graph):
    nodes = tuple(g)
    for roots in itertools.combinations(S, 5):
        solver = z3.Solver()
        label = {v: z3.Int(f"lab_{i}") for i, v in enumerate(nodes)}
        depth = {v: z3.Int(f"dep_{i}") for i, v in enumerate(nodes)}
        for v in nodes:
            solver.add(-1 <= label[v], label[v] <= 4, 0 <= depth[v], depth[v] < len(nodes))
        for i, root in enumerate(roots):
            solver.add(label[root] == i, depth[root] == 0)
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
            model = solver.model()
            bags = tuple(
                frozenset(v for v in nodes if model.eval(label[v]).as_long() == i)
                for i in range(5)
            )
            return roots, bags
    return None


def contact_witness_edges(g: nx.Graph, a: nx.Graph, h: nx.Graph, bags):
    fixed = {frozenset((f"v{v}", f"v{w}")) for v, w in a.edges()}
    fixed |= {frozenset(edge) for edge in h.edges()}
    fixed.add(frozenset(("v0", U)))

    def variable(edge):
        edge = frozenset(edge)
        if edge in fixed:
            return None
        x, y = tuple(edge)
        if x.startswith("v"):
            x, y = y, x
        assert y.startswith("v") and x in W
        return int(y[1:]), x

    used = set()
    for bag in bags:
        subgraph = g.subgraph(bag).copy()
        for v, w in subgraph.edges():
            subgraph[v][w]["weight"] = 0 if frozenset((v, w)) in fixed else 1
        tree = nx.minimum_spanning_tree(subgraph, weight="weight")
        for edge in tree.edges():
            item = variable(edge)
            if item is not None:
                used.add(item)
    for i in range(5):
        for j in range(i + 1, 5):
            choices = [
                (0 if frozenset((v, w)) in fixed else 1, v, w)
                for v in bags[i]
                for w in bags[j]
                if g.has_edge(v, w)
            ]
            _, v, w = min(choices)
            item = variable((v, w))
            if item is not None:
                used.add(item)
    return frozenset(used)


def crossing_bridges(a: nx.Graph, path: tuple[int, ...]):
    t_vertices = set(path)
    t_edges = {frozenset(edge) for edge in zip(path, path[1:])}
    attachments = []
    for v, w in a.subgraph(t_vertices).edges():
        if frozenset((v, w)) not in t_edges:
            attachments.append(frozenset((v, w)))
    for component in nx.connected_components(a.subgraph(set(a) - t_vertices)):
        attach = {w for v in component for w in a.neighbors(v) if w in t_vertices}
        attachments.append(frozenset(attach))
    for index in range(len(path) - 1):
        left = set(path[: index + 1])
        right = set(path[index + 1 :])
        if not any(bridge & left and bridge & right for bridge in attachments):
            return False
    return True


def find_fully_crossed_path(a: nx.Graph):
    for target in a:
        if target == Z:
            continue
        for path in nx.all_simple_paths(a, Z, target):
            if len(path) >= 3 and crossing_bridges(a, tuple(path)):
                return tuple(path)
    return None


def exact_k_minor(g: nx.Graph, k: int) -> bool:
    nodes = tuple(g)
    solver = z3.Solver()
    label = {v: z3.Int(f"Klab_{i}") for i, v in enumerate(nodes)}
    depth = {v: z3.Int(f"Kdep_{i}") for i, v in enumerate(nodes)}
    root = {(v, i): z3.Bool(f"root_{j}_{i}") for j, v in enumerate(nodes) for i in range(k)}
    for v in nodes:
        solver.add(-1 <= label[v], label[v] < k, 0 <= depth[v], depth[v] < len(nodes))
    for i in range(k):
        solver.add(z3.PbEq([(root[v, i], 1) for v in nodes], 1))
        for v in nodes:
            solver.add(z3.Implies(root[v, i], z3.And(label[v] == i, depth[v] == 0)))
            solver.add(
                z3.Implies(
                    z3.And(label[v] == i, z3.Not(root[v, i])),
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
    for i in range(k):
        for j in range(i + 1, k):
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
    return solver.check() == z3.sat


@dataclass
class SearchResult:
    status: str
    iterations: int
    rooted_blocks: int
    graph: nx.Graph | None = None
    core: tuple[int, ...] | None = None


def search_shape(a: nx.Graph, h: nx.Graph, iteration_limit=5000) -> SearchResult:
    core = find_fully_crossed_path(a)
    if core is None:
        return SearchResult("no_fully_crossed_core", 0, 0)
    solver, contact, _, _ = make_solver(a, h)
    rooted_blocks = 0
    for iteration in range(1, iteration_limit + 1):
        if solver.check() != z3.sat:
            return SearchResult("unsat", iteration - 1, rooted_blocks)
        model = solver.model()
        g = literal_closed_graph(a, h, model, contact)
        certificate = exact_rooted_k5(g)
        if certificate is None:
            return SearchResult("survivor", iteration, rooted_blocks, g, core)
        _, bags = certificate
        witness = contact_witness_edges(g, a, h, bags)
        rooted_blocks += 1
        if not witness:
            solver.add(z3.BoolVal(False))
        else:
            solver.add(z3.Or([z3.Not(contact[item]) for item in witness]))
    return SearchResult("limit", iteration_limit, rooted_blocks)


def atlas_shapes(max_order=6):
    for a in nx.graph_atlas_g():
        if 3 <= len(a) <= max_order and nx.is_biconnected(a):
            yield nx.convert_node_labels_to_integers(a)


def print_survivor(a: nx.Graph, h: nx.Graph, result: SearchResult):
    g = result.graph
    assert g is not None
    print("SURVIVOR", "A", nx.to_graph6_bytes(a, header=False).decode().strip())
    print("frontier", nx.to_graph6_bytes(h, header=False).decode().strip())
    print("core", result.core)
    for v in a:
        print("row", v, sorted(s for s in W if g.has_edge(f"v{v}", s)))
    full = g.copy()
    full.add_nodes_from(("r0", "r1"))
    full.add_edge("r0", "r1")
    for r in ("r0", "r1"):
        full.add_edges_from((r, s) for s in S)
    print("global_connectivity_with_two_packets", nx.node_connectivity(full))
    print("contains_K7_minor", exact_k_minor(full, 7))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--all-rooted-frontiers",
        action="store_true",
        help="enumerate all rooted trees and rooted C6-plus-leaf frontiers",
    )
    parser.add_argument("--max-thin-order", type=int, default=None)
    parser.add_argument("--frontier-modulus", type=int, default=1)
    parser.add_argument("--frontier-residue", type=int, default=0)
    args = parser.parse_args()

    if args.all_rooted_frontiers:
        frontiers = tuple(all_rooted_width_two_frontiers())
        max_order = args.max_thin_order or 5
    else:
        frontiers = tuple(FRONTIERS.items())
        max_order = args.max_thin_order or 6
    if not 0 <= args.frontier_residue < args.frontier_modulus:
        parser.error("frontier residue must lie in [0, modulus)")
    frontiers = tuple(
        item
        for index, item in enumerate(frontiers)
        if index % args.frontier_modulus == args.frontier_residue
    )
    totals = {"frontiers": len(frontiers), "shapes": 0, "unsat": 0, "iterations": 0}
    for frontier_name, h in frontiers:
        for a in atlas_shapes(max_order):
            totals["shapes"] += 1
            result = search_shape(a, h)
            totals["iterations"] += result.iterations
            if result.status == "survivor":
                print_survivor(a, h, result)
                return
            if result.status != "unsat":
                print("INCOMPLETE", frontier_name, len(a), result.status, result.iterations)
                return
            totals["unsat"] += 1
    print("FINITE_CEGAR_GREEN", totals)


if __name__ == "__main__":
    main()
