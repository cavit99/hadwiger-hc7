#!/usr/bin/env python3
"""Bounded falsifier for an adaptive peel-or-six-cut principle.

The thin shore consists of two clique lobes behind a literal three-gate.
Boundary contacts have the exact capacity-triangle normal form from the
audited support-four transition.  Z3 chooses every allowed portal edge.

The forbidden "peel" is deliberately stronger than a fixed two-duty split:
for no connected bipartition X|Y of the entire thin shore may there be a
partition S=I+J+U with I,J nonempty independent, U a clique, X contacting I,
and Y contacting J (in either orientation).  This is exactly the hypothesis
of the adaptive clique-reservoir return theorem.

The script then separates three questions:

* can the portal assignment defeat every adaptive peel?
* can it do so while the literal host is seven-connected?
* if a candidate survives, does it also satisfy Dirac's local inequality?

This is a bounded experiment, not a proof for arbitrary lobe interiors.
"""

from __future__ import annotations

import itertools
import random
import sys
from pathlib import Path


DEPS = Path(__file__).resolve().parent / "runtime" / "deps"
if DEPS.exists():
    sys.path.insert(0, str(DEPS))

import networkx as nx
import z3


S = tuple(range(7))
H_EDGES = ((0, 2), (0, 3), (0, 6), (1, 4), (1, 5), (3, 5))
A = frozenset((0, 1, 4, 6))
C = frozenset((0, 1, 2, 5))
EXCEPTIONAL = frozenset((3,))
COMMON = A & C

STAR_H_EDGES = ((0, 2), (2, 3), (3, 1), (0, 4), (4, 5), (0, 6))
STAR_A = frozenset((0, 1, 2, 3))
STAR_C = frozenset((0, 4, 5, 6))


def alpha(graph: nx.Graph) -> int:
    return max(
        (len(clique) for clique in nx.find_cliques(nx.complement(graph))),
        default=0,
    )


def boundary_states(boundary: nx.Graph):
    """All ordered I,J,U accepted by the adaptive return theorem."""
    answer = []
    for mask_u in range(1 << len(S)):
        u = frozenset(v for v in S if mask_u >> v & 1)
        if any(not boundary.has_edge(x, y) for x, y in itertools.combinations(u, 2)):
            continue
        rest = tuple(v for v in S if v not in u)
        for mask_i in range(1, (1 << len(rest)) - 1):
            i = frozenset(rest[j] for j in range(len(rest)) if mask_i >> j & 1)
            j = frozenset(rest) - i
            if any(boundary.has_edge(x, y) for x, y in itertools.combinations(i, 2)):
                continue
            if any(boundary.has_edge(x, y) for x, y in itertools.combinations(j, 2)):
                continue
            answer.append((i, j, u))
    return answer


def internal_graph(lobe_order: int):
    d = tuple(f"d{i}" for i in range(lobe_order))
    e = tuple(f"e{i}" for i in range(lobe_order))
    gates = ("z0", "z1", "z2")
    l = d + e + gates
    graph = nx.Graph()
    graph.add_nodes_from(l)
    graph.add_edges_from(itertools.combinations(d, 2))
    graph.add_edges_from(itertools.combinations(e, 2))
    graph.add_edges_from((z, x) for z in gates for x in d + e)
    return graph, d, e, gates, l


def connected_bipartitions(graph: nx.Graph, vertices):
    root = vertices[0]
    answer = []
    for mask in range(1, 1 << len(vertices)):
        left = frozenset(
            vertices[index] for index in range(len(vertices)) if mask >> index & 1
        )
        if root not in left or len(left) == len(vertices):
            continue
        right = frozenset(vertices) - left
        if nx.is_connected(graph.subgraph(left)) and nx.is_connected(graph.subgraph(right)):
            answer.append((left, right))
    return answer


def make_solver(lobe_order: int):
    thin, d, e, gates, l = internal_graph(lobe_order)
    boundary = nx.Graph()
    boundary.add_nodes_from(S)
    boundary.add_edges_from(H_EDGES)
    states = boundary_states(boundary)
    partitions = connected_bipartitions(thin, l)

    allowed = (
        {(x, s) for x in d for s in A}
        | {(x, s) for x in e for s in C}
        | {("z0", s) for s in EXCEPTIONAL}
        | {(x, s) for x in gates[1:] for s in COMMON}
    )
    var = {edge: z3.Bool(f"p_{edge[0]}_{edge[1]}") for edge in sorted(allowed)}
    solver = z3.Solver()

    # Exact lobe supports and nonempty gate supports.
    for s in A:
        solver.add(z3.Or(*(var[x, s] for x in d)))
    for s in C:
        solver.add(z3.Or(*(var[x, s] for x in e)))
    solver.add(var["z0", 3])

    def contacts(vertices, labels):
        terms = []
        for s in labels:
            incidences = [
                value
                for (x, literal), value in var.items()
                if x in vertices and literal == s
            ]
            terms.append(z3.Or(*incidences) if incidences else z3.BoolVal(False))
        return z3.And(*terms)

    # Forbid every adaptive seed allocation on every connected carrier split.
    for left, right in partitions:
        for i, j, _u in states:
            solver.add(z3.Not(z3.And(contacts(left, i), contacts(right, j))))
            solver.add(z3.Not(z3.And(contacts(left, j), contacts(right, i))))

    return solver, var, thin, boundary, d, e, gates, l, states, partitions


def make_skeleton_solver(thin: nx.Graph, d, e, gates):
    """The same portal problem on an arbitrary labelled two-lobe skeleton."""
    d, e, gates = tuple(d), tuple(e), tuple(gates)
    l = tuple(thin)
    boundary = nx.Graph()
    boundary.add_nodes_from(S)
    boundary.add_edges_from(H_EDGES)
    states = boundary_states(boundary)
    partitions = connected_bipartitions(thin, l)
    exceptional = gates[0]

    allowed = (
        {(x, s) for x in d for s in A}
        | {(x, s) for x in e for s in C}
        | {(exceptional, s) for s in EXCEPTIONAL}
        | {(x, s) for x in gates[1:] for s in COMMON}
    )
    var = {edge: z3.Bool(f"p_{edge[0]}_{edge[1]}") for edge in sorted(allowed)}
    solver = z3.Solver()
    for s in A:
        solver.add(z3.Or(*(var[x, s] for x in d)))
    for s in C:
        solver.add(z3.Or(*(var[x, s] for x in e)))
    solver.add(var[exceptional, 3])

    def contacts(vertices, labels):
        return z3.And(
            *(
                z3.Or(
                    *(
                        value
                        for (x, literal), value in var.items()
                        if x in vertices and literal == s
                    )
                )
                for s in labels
            )
        )

    for left, right in partitions:
        for i, j, _u in states:
            solver.add(z3.Not(z3.And(contacts(left, i), contacts(right, j))))
            solver.add(z3.Not(z3.And(contacts(left, j), contacts(right, i))))
    return solver, var, boundary, l, states, partitions


def make_star_solver(
    thin: nx.Graph,
    d,
    e,
    gates,
    *,
    only_reservoir_zero=False,
    every_vertex_portal=False,
):
    """Portal solver for the lobe-centred star support obstruction."""
    d, e, gates = tuple(d), tuple(e), tuple(gates)
    l = tuple(thin)
    boundary = nx.Graph()
    boundary.add_nodes_from(S)
    boundary.add_edges_from(STAR_H_EDGES)
    states = boundary_states(boundary)
    partitions = connected_bipartitions(thin, l)
    allowed = (
        {(x, s) for x in d for s in STAR_A}
        | {(x, s) for x in e + gates for s in STAR_C}
    )
    var = {edge: z3.Bool(f"p_{edge[0]}_{edge[1]}") for edge in sorted(allowed)}
    solver = z3.Solver()
    for s in STAR_A:
        solver.add(z3.Or(*(var[x, s] for x in d)))
    for s in STAR_C:
        solver.add(z3.Or(*(var[x, s] for x in e)))
    if every_vertex_portal:
        for x in d + e + gates:
            solver.add(
                z3.Or(*(value for (left, _), value in var.items() if left == x))
            )

    def contacts(vertices, labels):
        clauses = []
        for s in labels:
            terms = [
                value
                for (x, literal), value in var.items()
                if x in vertices and literal == s
            ]
            clauses.append(z3.Or(*terms) if terms else z3.BoolVal(False))
        return z3.And(*clauses)

    selected_states = [
        state for state in states if not only_reservoir_zero or state[2] == frozenset((0,))
    ]
    for left, right in partitions:
        for i, j, _u in selected_states:
            solver.add(z3.Not(z3.And(contacts(left, i), contacts(right, j))))
            solver.add(z3.Not(z3.And(contacts(left, j), contacts(right, i))))
    return solver, var, boundary, l, states, partitions


def dense_star_probe(
    order: int,
    *,
    only_reservoir_zero=False,
    expanded_rich=False,
    connectivity_target=7,
):
    thin, d, e, gates, l = internal_graph(order)
    solver, var, boundary, l, states, partitions = make_star_solver(
        thin, d, e, gates, only_reservoir_zero=only_reservoir_zero
    )
    static = solver.check()
    if static != z3.sat:
        return {
            "status": "UNSAT",
            "states": len(states),
            "partitions": len(partitions),
        }
    cuts = 0
    history = []
    while solver.check() == z3.sat:
        model = solver.model()
        edges = [edge for edge, value in var.items() if z3.is_true(model.eval(value))]
        host = (
            literal_host_expanded(thin, boundary, l, edges)
            if expanded_rich
            else literal_host(thin, boundary, l, edges)
        )
        if nx.node_connectivity(host) >= connectivity_target:
            return {
                "status": f"SAT{connectivity_target}",
                "host": host,
                "portals": edges,
                "dirac_bad": [
                    v
                    for v in host
                    if alpha(host.subgraph(host[v])) > host.degree(v) - 5
                ],
                "cuts": cuts,
                "states": len(states),
                "partitions": len(partitions),
            }
        cut = nx.minimum_node_cut(host)
        residual = host.copy()
        residual.remove_nodes_from(cut)
        component = min(
            nx.connected_components(residual),
            key=lambda x: (len(x), sorted(map(str, x))),
        )
        opposite = set(host) - set(cut) - set(component)
        crossing = [
            value
            for (x, s), value in var.items()
            if x not in cut
            and s not in cut
            and (
                (x in component and s in opposite)
                or (s in component and x in opposite)
            )
        ]
        history.append(
            {
                "cut": tuple(sorted(map(str, cut))),
                "component": tuple(sorted(map(str, component))),
                "crossing": tuple(
                    sorted(
                        (str(edge[0]), edge[1])
                        for edge, value in var.items()
                        if value in crossing
                    )
                ),
            }
        )
        solver.add(z3.Or(*crossing) if crossing else z3.BoolVal(False))
        cuts += 1
    return {
        "status": f"UNSAT{connectivity_target}",
        "cuts": cuts,
        "history": history,
        "states": len(states),
        "partitions": len(partitions),
    }


def atlas_static_census(*, expanded_rich=False):
    """Search every atlas skeleton (at most seven thin vertices)."""
    tested = 0
    static_sat = 0
    seven_connected = 0
    dirac_good = 0
    witness = None
    for raw in nx.graph_atlas_g():
        if len(raw) < 5 or len(raw) > 7:
            continue
        raw = nx.relabel_nodes(raw, {v: f"l{v}" for v in raw})
        if nx.node_connectivity(raw) < 3:
            continue
        if min(dict(raw.degree()).values()) < 4:
            continue
        for gates_set in itertools.combinations(raw, 3):
            remainder = raw.copy()
            remainder.remove_nodes_from(gates_set)
            components = list(nx.connected_components(remainder))
            if len(components) != 2:
                continue
            for exceptional_index in range(3):
                gates = (
                    gates_set[exceptional_index],
                    *(
                        gates_set[index]
                        for index in range(3)
                        if index != exceptional_index
                    ),
                )
                for d, e in (components, components[::-1]):
                    tested += 1
                    solver, var, boundary, l, states, partitions = make_skeleton_solver(
                        raw, d, e, gates
                    )
                    if solver.check() != z3.sat:
                        continue
                    static_sat += 1
                    while solver.check() == z3.sat:
                        model = solver.model()
                        edges = [
                            edge
                            for edge, value in var.items()
                            if z3.is_true(model.eval(value))
                        ]
                        graph = (
                            literal_host_expanded(raw, boundary, l, edges)
                            if expanded_rich
                            else literal_host(raw, boundary, l, edges)
                        )
                        if nx.node_connectivity(graph) < 7:
                            cut = nx.minimum_node_cut(graph)
                            residual = graph.copy()
                            residual.remove_nodes_from(cut)
                            component = min(
                                nx.connected_components(residual),
                                key=lambda x: (len(x), sorted(map(str, x))),
                            )
                            opposite = set(graph) - set(cut) - set(component)
                            crossing = [
                                value
                                for (x, s), value in var.items()
                                if x not in cut
                                and s not in cut
                                and (
                                    (x in component and s in opposite)
                                    or (s in component and x in opposite)
                                )
                            ]
                            solver.add(
                                z3.Or(*crossing) if crossing else z3.BoolVal(False)
                            )
                            continue
                        seven_connected += 1
                        bad = [
                            v
                            for v in graph
                            if alpha(graph.subgraph(graph[v])) > graph.degree(v) - 5
                        ]
                        if not bad:
                            dirac_good += 1
                            witness = (raw.copy(), tuple(d), tuple(e), gates, graph, edges)
                            return {
                                "tested": tested,
                                "static_sat": static_sat,
                                "seven_connected": seven_connected,
                                "dirac_good": dirac_good,
                                "witness": witness,
                            }
                        solver.add(
                            z3.Or(
                                *(
                                    z3.Not(value)
                                    if z3.is_true(model.eval(value))
                                    else value
                                    for value in var.values()
                                )
                            )
                        )
    return {
        "tested": tested,
        "static_sat": static_sat,
        "seven_connected": seven_connected,
        "dirac_good": dirac_good,
        "witness": witness,
    }


def atlas_star_census(*, only_reservoir_zero=False, expanded_rich=False):
    """Exact atlas census for the lobe-star form."""
    tested = static_sat = cut_clauses = 0
    for raw in nx.graph_atlas_g():
        if len(raw) < 5 or len(raw) > 7:
            continue
        raw = nx.relabel_nodes(raw, {v: f"l{v}" for v in raw})
        if nx.node_connectivity(raw) != 3:
            continue
        if min(dict(raw.degree()).values()) < 4:
            continue
        for gates_set in itertools.combinations(raw, 3):
            remainder = raw.copy()
            remainder.remove_nodes_from(gates_set)
            components = list(nx.connected_components(remainder))
            if len(components) != 2:
                continue
            for d, e in (components, components[::-1]):
                tested += 1
                solver, var, boundary, l, states, partitions = make_star_solver(
                    raw,
                    d,
                    e,
                    gates_set,
                    only_reservoir_zero=only_reservoir_zero,
                )
                if solver.check() != z3.sat:
                    continue
                static_sat += 1
                while solver.check() == z3.sat:
                    model = solver.model()
                    edges = [
                        edge
                        for edge, value in var.items()
                        if z3.is_true(model.eval(value))
                    ]
                    host = (
                        literal_host_expanded(raw, boundary, tuple(raw), edges)
                        if expanded_rich
                        else literal_host(raw, boundary, tuple(raw), edges)
                    )
                    if nx.node_connectivity(host) >= 7:
                        return {
                            "status": "SAT7",
                            "tested": tested,
                            "static_sat": static_sat,
                            "cut_clauses": cut_clauses,
                            "skeleton": raw.copy(),
                            "d": tuple(d),
                            "e": tuple(e),
                            "gates": tuple(gates_set),
                            "host": host,
                            "portals": edges,
                            "dirac_bad": [
                                v
                                for v in host
                                if alpha(host.subgraph(host[v])) > host.degree(v) - 5
                            ],
                        }
                    cut = nx.minimum_node_cut(host)
                    residual = host.copy()
                    residual.remove_nodes_from(cut)
                    component = min(
                        nx.connected_components(residual),
                        key=lambda x: (len(x), sorted(map(str, x))),
                    )
                    opposite = set(host) - set(cut) - set(component)
                    crossing = [
                        value
                        for (x, s), value in var.items()
                        if x not in cut
                        and s not in cut
                        and (
                            (x in component and s in opposite)
                            or (s in component and x in opposite)
                        )
                    ]
                    solver.add(
                        z3.Or(*crossing) if crossing else z3.BoolVal(False)
                    )
                    cut_clauses += 1
    return {
        "status": "UNSAT7",
        "tested": tested,
        "static_sat": static_sat,
        "cut_clauses": cut_clauses,
    }


def random_star_one(seed: int, *, only_reservoir_zero=False):
    """One exact order-eight/nine star search, suitable for fresh processes."""
    rng = random.Random(seed)
    for attempt in range(50_000):
        nd, ne = (2, 3) if rng.random() < 0.5 else (3, 3)
        d = tuple(f"d{i}" for i in range(nd))
        e = tuple(f"e{i}" for i in range(ne))
        gates = ("z0", "z1", "z2")
        graph = nx.Graph()
        graph.add_nodes_from(d + e + gates)
        for side in (d, e):
            # Connected lobe, with random extra chords.
            for index in range(1, len(side)):
                graph.add_edge(side[index - 1], side[index])
            for x, y in itertools.combinations(side, 2):
                if rng.random() < 0.45:
                    graph.add_edge(x, y)
            for gate in gates:
                for x in side:
                    if rng.random() < 0.67:
                        graph.add_edge(gate, x)
                if not any(graph.has_edge(gate, x) for x in side):
                    graph.add_edge(gate, rng.choice(side))
        for x, y in itertools.combinations(gates, 2):
            if rng.random() < 0.35:
                graph.add_edge(x, y)
        if nx.node_connectivity(graph) != 3:
            continue
        if min(dict(graph.degree()).values()) < 4:
            continue
        solver, var, boundary, l, states, partitions = make_star_solver(
            graph,
            d,
            e,
            gates,
            only_reservoir_zero=only_reservoir_zero,
        )
        if solver.check() != z3.sat:
            return {
                "status": "STATIC_UNSAT",
                "attempt": attempt,
                "skeleton": graph,
                "partitions": len(partitions),
            }
        cuts = 0
        while solver.check() == z3.sat:
            model = solver.model()
            edges = [
                edge for edge, value in var.items() if z3.is_true(model.eval(value))
            ]
            host = literal_host(graph, boundary, l, edges)
            if nx.node_connectivity(host) >= 7:
                return {
                    "status": "SAT7",
                    "attempt": attempt,
                    "skeleton": graph,
                    "host": host,
                    "portals": edges,
                    "cuts": cuts,
                    "dirac_bad": [
                        v
                        for v in host
                        if alpha(host.subgraph(host[v])) > host.degree(v) - 5
                    ],
                    "partitions": len(partitions),
                }
            cut = nx.minimum_node_cut(host)
            residual = host.copy()
            residual.remove_nodes_from(cut)
            component = min(
                nx.connected_components(residual),
                key=lambda x: (len(x), sorted(map(str, x))),
            )
            opposite = set(host) - set(cut) - set(component)
            crossing = [
                value
                for (x, s), value in var.items()
                if x not in cut
                and s not in cut
                and (
                    (x in component and s in opposite)
                    or (s in component and x in opposite)
                )
            ]
            solver.add(z3.Or(*crossing) if crossing else z3.BoolVal(False))
            cuts += 1
        return {
            "status": "UNSAT7",
            "attempt": attempt,
            "skeleton": graph,
            "cuts": cuts,
            "partitions": len(partitions),
        }
    return {"status": "NO_SKELETON"}


def random_skeleton_census(samples: int = 200, seed: int = 7):
    """Seek a larger static obstruction before spending kernel hypotheses."""
    rng = random.Random(seed)
    tested = 0
    for attempt in range(samples * 200):
        if tested >= samples:
            break
        nd = rng.randint(2, 5)
        ne = rng.randint(2, 5)
        d = tuple(f"d{i}" for i in range(nd))
        e = tuple(f"e{i}" for i in range(ne))
        gates = ("z0", "z1", "z2")
        graph = nx.Graph()
        graph.add_nodes_from(d + e + gates)
        for side in (d, e):
            # Start with a random tree, then add internal and gate edges.
            order = list(side)
            rng.shuffle(order)
            for index in range(1, len(order)):
                graph.add_edge(order[index], order[rng.randrange(index)])
            for x, y in itertools.combinations(side, 2):
                if rng.random() < 0.45:
                    graph.add_edge(x, y)
            for gate in gates:
                chosen = [x for x in side if rng.random() < 0.62]
                if not chosen:
                    chosen = [rng.choice(side)]
                graph.add_edges_from((gate, x) for x in chosen)
        for x, y in itertools.combinations(gates, 2):
            if rng.random() < 0.35:
                graph.add_edge(x, y)
        if nx.node_connectivity(graph) != 3:
            continue
        if min(dict(graph.degree()).values()) < 4:
            continue
        remainder = graph.copy()
        remainder.remove_nodes_from(gates)
        if len(list(nx.connected_components(remainder))) != 2:
            continue
        tested += 1
        solver, var, boundary, l, states, partitions = make_skeleton_solver(
            graph, d, e, gates
        )
        if solver.check() != z3.sat:
            continue
        model = solver.model()
        edges = [
            edge for edge, value in var.items() if z3.is_true(model.eval(value))
        ]
        host = literal_host(graph, boundary, l, edges)
        return {
            "tested": tested,
            "attempt": attempt,
            "skeleton": graph,
            "d": d,
            "e": e,
            "gates": gates,
            "host": host,
            "portals": edges,
            "connectivity": nx.node_connectivity(host),
            "dirac_bad": [
                v
                for v in host
                if alpha(host.subgraph(host[v])) > host.degree(v) - 5
            ],
            "partitions": len(partitions),
        }
    return {"tested": tested, "witness": None}


def heuristic_static_search(samples: int = 200, assignments: int = 2000, seed: int = 11):
    """Fast randomized search using the exact finite support predicate."""
    rng = random.Random(seed)
    boundary = nx.Graph()
    boundary.add_nodes_from(S)
    boundary.add_edges_from(H_EDGES)
    states = boundary_states(boundary)
    good = [[False] * 128 for _ in range(128)]
    for left_mask in range(128):
        for right_mask in range(128):
            good[left_mask][right_mask] = any(
                all(left_mask >> x & 1 for x in i)
                and all(right_mask >> x & 1 for x in j)
                or all(left_mask >> x & 1 for x in j)
                and all(right_mask >> x & 1 for x in i)
                for i, j, _u in states
            )

    best = None
    tested = 0
    for _ in range(samples * 300):
        if tested >= samples:
            break
        nd, ne = rng.randint(2, 5), rng.randint(2, 5)
        d = tuple(f"d{i}" for i in range(nd))
        e = tuple(f"e{i}" for i in range(ne))
        gates = ("z0", "z1", "z2")
        graph = nx.Graph()
        graph.add_nodes_from(d + e + gates)
        for side in (d, e):
            order = list(side)
            rng.shuffle(order)
            for index in range(1, len(order)):
                graph.add_edge(order[index], order[rng.randrange(index)])
            for x, y in itertools.combinations(side, 2):
                if rng.random() < 0.5:
                    graph.add_edge(x, y)
            for gate in gates:
                chosen = [x for x in side if rng.random() < 0.65]
                if not chosen:
                    chosen = [rng.choice(side)]
                graph.add_edges_from((gate, x) for x in chosen)
        for x, y in itertools.combinations(gates, 2):
            if rng.random() < 0.25:
                graph.add_edge(x, y)
        if nx.node_connectivity(graph) != 3 or min(dict(graph.degree()).values()) < 4:
            continue
        tested += 1
        partitions = connected_bipartitions(graph, tuple(graph))
        part_masks = []
        vertices = tuple(graph)
        for left, right in partitions:
            part_masks.append((tuple(left), tuple(right)))

        allowed_masks = {
            **{x: sum(1 << s for s in A) for x in d},
            **{x: sum(1 << s for s in C) for x in e},
            "z0": 1 << 3,
            "z1": sum(1 << s for s in COMMON),
            "z2": sum(1 << s for s in COMMON),
        }

        def random_rows():
            while True:
                rows = {
                    x: rng.randint(1, allowed_masks[x]) & allowed_masks[x]
                    for x in vertices
                }
                rows["z0"] = 1 << 3
                if all(rows[x] for x in vertices) and (
                    (sum((rows[x] for x in d), 0) | 0) >= 0
                ):
                    da = 0
                    ec = 0
                    for x in d:
                        da |= rows[x]
                    for x in e:
                        ec |= rows[x]
                    if da == sum(1 << s for s in A) and ec == sum(1 << s for s in C):
                        return rows

        def score(rows):
            count = 0
            for left, right in part_masks:
                lm = rm = 0
                for x in left:
                    lm |= rows[x]
                for x in right:
                    rm |= rows[x]
                count += bool(good[lm][rm])
            return count

        for _assignment in range(assignments):
            rows = random_rows()
            value = score(rows)
            if best is None or value < best[0]:
                best = (value, graph.copy(), d, e, gates, dict(rows), len(partitions))
            if value == 0:
                edges = [
                    (x, s)
                    for x, mask in rows.items()
                    for s in S
                    if mask >> s & 1
                ]
                host = literal_host(graph, boundary, tuple(graph), edges)
                return {
                    "tested": tested,
                    "score": 0,
                    "skeleton": graph,
                    "rows": rows,
                    "host": host,
                    "connectivity": nx.node_connectivity(host),
                    "dirac_bad": [
                        v
                        for v in host
                        if alpha(host.subgraph(host[v])) > host.degree(v) - 5
                    ],
                    "partitions": len(partitions),
                }
    return {
        "tested": tested,
        "best_score": None if best is None else best[0],
        "best": best,
    }


def literal_host(thin, boundary, l, true_edges):
    # Two singleton rich packets suffice for the connectivity experiment.
    graph = nx.Graph()
    graph.add_nodes_from(S + tuple(l) + ("p", "q"))
    graph.add_edges_from(boundary.edges)
    graph.add_edges_from(thin.edges)
    graph.add_edges_from(true_edges)
    graph.add_edge("p", "q")
    graph.add_edges_from((packet, s) for packet in ("p", "q") for s in S)
    return graph


def literal_host_expanded(thin, boundary, l, true_edges):
    """Use two four-vertex full packets, each of packing number one."""
    p = tuple(f"p{i}" for i in range(4))
    q = tuple(f"q{i}" for i in range(4))
    graph = nx.Graph()
    graph.add_nodes_from(S + tuple(l) + p + q)
    graph.add_edges_from(boundary.edges)
    graph.add_edges_from(thin.edges)
    graph.add_edges_from(true_edges)
    graph.add_edges_from(itertools.combinations(p, 2))
    graph.add_edges_from(itertools.combinations(q, 2))
    graph.add_edge("p0", "q0")

    # P has scarce literals 1 and 3; Q has scarce literals 4 and 5.
    for index, vertex in enumerate(p):
        contacts = set(S) - {1, 3}
        if index == 0:
            contacts.add(1)
        if index == 1:
            contacts.add(3)
        graph.add_edges_from((vertex, s) for s in contacts)
    for index, vertex in enumerate(q):
        contacts = set(S) - {4, 5}
        if index == 0:
            contacts.add(4)
        if index == 1:
            contacts.add(5)
        graph.add_edges_from((vertex, s) for s in contacts)
    return graph


def exact_rich_packet_number(graph: nx.Graph) -> int:
    rich = tuple(
        v
        for v in graph
        if isinstance(v, str) and v[:1] in {"p", "q"}
    )
    packets = []
    for mask in range(1, 1 << len(rich)):
        candidate = frozenset(
            rich[index] for index in range(len(rich)) if mask >> index & 1
        )
        if not nx.is_connected(graph.subgraph(candidate)):
            continue
        if all(any(graph.has_edge(v, s) for v in candidate) for s in S):
            packets.append(candidate)
    best = 0

    def search(index, used, count):
        nonlocal best
        best = max(best, count)
        for next_index in range(index, len(packets)):
            if packets[next_index].isdisjoint(used):
                search(next_index + 1, used | packets[next_index], count + 1)

    search(0, frozenset(), 0)
    return best


def solve(lobe_order: int):
    solver, var, thin, boundary, d, e, gates, l, states, partitions = make_solver(
        lobe_order
    )
    cuts = 0
    dirac_blocks = 0
    while solver.check() == z3.sat:
        model = solver.model()
        true_edges = [edge for edge, value in var.items() if z3.is_true(model.eval(value))]
        graph = literal_host(thin, boundary, l, true_edges)
        if nx.node_connectivity(graph) < 7:
            cut = nx.minimum_node_cut(graph)
            remainder = graph.copy()
            remainder.remove_nodes_from(cut)
            component = min(nx.connected_components(remainder), key=lambda x: (len(x), sorted(map(str, x))))
            opposite = set(graph) - set(cut) - set(component)
            crossing = [
                value
                for (x, s), value in var.items()
                if x not in cut
                and s not in cut
                and ((x in component and s in opposite) or (s in component and x in opposite))
            ]
            solver.add(z3.Or(*crossing) if crossing else z3.BoolVal(False))
            cuts += 1
            continue

        bad = [
            v
            for v in graph
            if alpha(graph.subgraph(graph[v])) > graph.degree(v) - 5
        ]
        if bad:
            # Block this complete portal assignment.  This is deliberately
            # coarse: the experiment reports whether any exact assignment
            # survives, not a minimal Dirac core.
            solver.add(
                z3.Or(
                    *(
                        z3.Not(value) if z3.is_true(model.eval(value)) else value
                        for value in var.values()
                    )
                )
            )
            dirac_blocks += 1
            continue

        return {
            "status": "SAT",
            "graph": graph,
            "portals": true_edges,
            "cuts": cuts,
            "dirac_blocks": dirac_blocks,
            "states": len(states),
            "partitions": len(partitions),
        }

    return {
        "status": "UNSAT",
        "cuts": cuts,
        "dirac_blocks": dirac_blocks,
        "states": len(states),
        "partitions": len(partitions),
    }


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "dense-star"
    if mode == "dense-star":
        result = dense_star_probe(4, expanded_rich=True)
        assert result["status"] == "UNSAT7"
        print(
            "DENSE_STAR_K4",
            result["status"],
            "connected_splits",
            result["partitions"],
            "cut_clauses",
            result["cuts"],
        )
    elif mode == "dense-cross":
        result = dense_star_probe(
            5,
            only_reservoir_zero=True,
            expanded_rich=True,
        )
        assert result["status"] == "UNSAT7"
        print(
            "DENSE_STAR_K5_RESERVOIR_ZERO",
            result["status"],
            "connected_splits",
            result["partitions"],
            "cut_clauses",
            result["cuts"],
        )
    elif mode == "star-atlas":
        result = atlas_star_census(expanded_rich=True)
        assert result["status"] == "UNSAT7"
        print("STAR_ATLAS", result)
    elif mode == "triangle-atlas":
        result = atlas_static_census(expanded_rich=True)
        assert result["witness"] is None
        print("TRIANGLE_ATLAS", result)
    elif mode == "packet":
        thin, _d, _e, _gates, l = internal_graph(2)
        boundary = nx.Graph()
        boundary.add_nodes_from(S)
        boundary.add_edges_from(STAR_H_EDGES)
        packet_host = literal_host_expanded(thin, boundary, l, [])
        assert exact_rich_packet_number(packet_host) == 2
        print("EXPANDED_RICH_PACKET_NUMBER", 2)
    else:
        raise SystemExit(f"unknown mode: {mode}")


if __name__ == "__main__":
    main()
