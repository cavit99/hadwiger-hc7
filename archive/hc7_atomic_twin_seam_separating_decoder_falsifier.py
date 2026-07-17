#!/usr/bin/env python3
"""Narrow falsifier for the literal twin-seam separating-edge decoder.

This is deliberately not an atlas or boundary census.  It fixes the first
minimum-degree-three twin seam: two two-vertex lobes joined through two
gates, the canonical paired width-two tree on the old seven-boundary, and
the symmetric five/five contact pattern.  Z3 searches only the literal
contact placement.

The constraints are added in the order in which they occur in the audited
HC7 kernel:

* exact twin supports and the unique ``z-u`` edge;
* every relative seven-cut inequality inside the atomic shore;
* failure of every adaptive two-carrier return;
* absence of an old-boundary-rooted K5 (checked exactly and lazily);
* two full rich packets, seven-connectivity, Dirac's neighbourhood bound,
  and K7-minor-freeness (checked on each surviving literal host);
* a six-colouring of ``G/zu`` possessing a lobe--gate edge which separates
  the corresponding bichromatic z--u lock and supplies the two literal
  twin-view mismatch-path geometries.

The search is a bounded guardrail only.  SAT would refute a geometry-only
decoder, not HC7; UNSAT identifies the earliest hypothesis killing this
specific sharp shell and is not an unbounded theorem.
"""

from __future__ import annotations

import itertools
import os
import sys
from pathlib import Path


DEPS = Path(__file__).resolve().parent / "runtime" / "deps"
if DEPS.exists():
    sys.path.insert(0, str(DEPS))

import networkx as nx
import z3


S = tuple(range(7))
U = 0
PROFILE = os.environ.get("HC7_TWIN_PROFILE", "double_conflict")
if PROFILE == "star_shell":
    I = frozenset((1, 2, 3))
    A0 = frozenset((4, 5))
    B0 = frozenset((0, 6))
elif PROFILE == "double_conflict":
    B0 = frozenset((0, 4))
    A0 = frozenset((1, 2))
    I = frozenset((3, 5, 6))
else:
    assert PROFILE == "standard_tree"
    I = frozenset((1, 2, 3))
    A0 = frozenset((4, 5))
    B0 = frozenset((0, 6))
TD = I | A0
TE = I | B0
Z = ("p", "q")
SHAPE = os.environ.get("HC7_TWIN_SHAPE", "order6")
if SHAPE == "order11_c4bow":
    D = ("d0", "d1", "d2", "d3")
    E = ("z", "e1", "e2", "e3", "e4")
elif SHAPE == "order10_c44":
    D = ("d0", "d1", "d2", "d3")
    E = ("z", "e1", "e2", "e3")
elif SHAPE == "order8_33":
    D = ("d0", "d1", "d2")
    E = ("z", "e1", "e2")
elif SHAPE == "order7_e3":
    D = ("d0", "d1")
    E = ("z", "e1", "e2")
elif SHAPE == "order7_d3":
    D = ("d0", "d1", "d2")
    E = ("z", "e1")
else:
    assert SHAPE == "order6"
    D = ("d0", "d1")
    E = ("z", "e1")
A = Z + D + E
ROOT = "z"
R = ("r0", "r1")
GATE_EDGE = os.environ.get("HC7_GATE_EDGE", "0") == "1"
CUT_LEVEL = int(os.environ.get("HC7_CUT_LEVEL", "2"))
ROOT_FULL = os.environ.get("HC7_ROOT_FULL", "1") == "1"

# A paired width-two tree.  The default profile has one literal edge inside
# each two-vertex defect and is the sharp symmetric two-list obstruction.
if PROFILE == "star_shell":
    H_EDGES = tuple((1, literal) for literal in S if literal != 1)
elif PROFILE == "double_conflict":
    H_EDGES = ((0, 4), (1, 2), (1, 6), (3, 5), (3, 6), (4, 6))
else:
    H_EDGES = ((1, 2), (1, 3), (1, 4), (2, 5), (0, 4), (3, 6))


def atomic_graph() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(A)
    if SHAPE == "order11_c4bow":
        graph.add_edges_from(
            (
                ("d0", "d1"),
                ("d1", "d2"),
                ("d2", "d3"),
                ("d3", "d0"),
                ("z", "e1"),
                ("e1", "e2"),
                ("e2", "z"),
                ("z", "e3"),
                ("e3", "e4"),
                ("e4", "z"),
            )
        )
        for gate in Z:
            graph.add_edges_from((gate, vertex) for vertex in D + E)
    elif SHAPE == "order10_c44":
        graph.add_edges_from(
            (
                ("d0", "d1"),
                ("d1", "d2"),
                ("d2", "d3"),
                ("d3", "d0"),
                ("z", "e1"),
                ("e1", "e2"),
                ("e2", "e3"),
                ("e3", "z"),
            )
        )
        for gate in Z:
            graph.add_edges_from((gate, vertex) for vertex in D + E)
    elif SHAPE == "order8_33":
        graph.add_edges_from(
            (
                ("d0", "d1"),
                ("d1", "d2"),
                ("d2", "d0"),
                ("p", "d0"),
                ("p", "d1"),
                ("q", "d1"),
                ("q", "d2"),
                ("z", "e1"),
                ("e1", "e2"),
                ("e2", "z"),
                ("p", "z"),
                ("p", "e1"),
                ("q", "e1"),
                ("q", "e2"),
            )
        )
    elif SHAPE == "order7_e3":
        graph.add_edges_from(
            (
                ("d0", "d1"),
                ("p", "d0"),
                ("p", "d1"),
                ("q", "d0"),
                ("q", "d1"),
                ("z", "e1"),
                ("e1", "e2"),
                ("e2", "z"),
                ("p", "z"),
                ("p", "e1"),
                ("q", "e1"),
                ("q", "e2"),
            )
        )
    elif SHAPE == "order7_d3":
        graph.add_edges_from(
            (
                ("d0", "d1"),
                ("d1", "d2"),
                ("d2", "d0"),
                ("p", "d0"),
                ("p", "d1"),
                ("q", "d1"),
                ("q", "d2"),
                ("z", "e1"),
                ("p", "z"),
                ("p", "e1"),
                ("q", "z"),
                ("q", "e1"),
            )
        )
    else:
        graph.add_edges_from(
            (
                ("d0", "d1"),
                ("p", "d0"),
                ("p", "d1"),
                ("q", "d0"),
                ("q", "d1"),
                ("z", "e1"),
                ("p", "z"),
                ("p", "e1"),
                ("q", "z"),
                ("q", "e1"),
            )
        )
    if GATE_EDGE:
        graph.add_edge("p", "q")
    assert nx.is_biconnected(graph)
    assert min(dict(graph.degree()).values()) >= 3
    return graph


def connected_subsets(graph: nx.Graph, vertices) -> list[frozenset]:
    vertices = tuple(vertices)
    answer = []
    for mask in range(1, 1 << len(vertices)):
        chosen = frozenset(
            vertices[index]
            for index in range(len(vertices))
            if mask >> index & 1
        )
        if nx.is_connected(graph.subgraph(chosen)):
            answer.append(chosen)
    return answer


def adaptive_partitions(boundary: nx.Graph):
    answer = []
    for reservoir_size in range(len(S) + 1):
        for reservoir_tuple in itertools.combinations(S, reservoir_size):
            reservoir = frozenset(reservoir_tuple)
            if any(
                not boundary.has_edge(x, y)
                for x, y in itertools.combinations(reservoir, 2)
            ):
                continue
            free = tuple(x for x in S if x not in reservoir)
            if len(free) < 2:
                continue
            for mask in range(1, 1 << (len(free) - 1)):
                first = frozenset(
                    free[index]
                    for index in range(len(free))
                    if mask >> index & 1
                )
                second = frozenset(free) - first
                if not second:
                    continue
                if any(boundary.has_edge(x, y) for x, y in itertools.combinations(first, 2)):
                    continue
                if any(boundary.has_edge(x, y) for x, y in itertools.combinations(second, 2)):
                    continue
                answer.append((first, second, reservoir))
    return answer


def contact_solver():
    thin = atomic_graph()
    allowed = {
        **{vertex: TD for vertex in D},
        **{vertex: TE - {U} for vertex in E},
        **{vertex: I for vertex in Z},
    }
    contact = {
        (vertex, literal): z3.Bool(f"x_{vertex}_{literal}")
        for vertex in A
        for literal in S
        if literal != U
    }
    solver = z3.Solver()

    # Variables are kept rectangular for simple model blocking, but contacts
    # outside the literal twin supports are forbidden rather than left as
    # unconstrained bookkeeping bits.
    for (vertex, literal), variable in contact.items():
        if literal not in allowed[vertex]:
            solver.add(z3.Not(variable))

    def edge(vertex, literal):
        if literal == U:
            return z3.BoolVal(vertex == ROOT)
        if literal not in allowed[vertex]:
            return z3.BoolVal(False)
        return contact[vertex, literal]

    # Exact five/five lobe supports and exact gate-support containment.
    for literal in TD:
        solver.add(z3.Or(*(edge(vertex, literal) for vertex in D)))
    for literal in TE:
        solver.add(z3.Or(*(edge(vertex, literal) for vertex in E)))
    for literal in I:
        solver.add(z3.Or(*(edge(vertex, literal) for vertex in Z)))
    # Root-deletion normalization: A-z is W-full.
    if ROOT_FULL:
        for literal in set(S) - {U}:
            solver.add(z3.Or(*(edge(vertex, literal) for vertex in A if vertex != ROOT)))

    subsets = connected_subsets(thin, A)
    for chosen in subsets:
        if CUT_LEVEL == 0 or (CUT_LEVEL == 1 and len(chosen) != 1):
            continue
        internal = {
            vertex
            for vertex in A
            if vertex not in chosen
            and any(thin.has_edge(vertex, old) for old in chosen)
        }
        terms = [
            z3.Or(*(edge(vertex, literal) for vertex in chosen))
            for literal in S
        ]
        solver.add(z3.PbGe([(term, 1) for term in terms], 7 - len(internal)))

    boundary = nx.Graph()
    boundary.add_nodes_from(S)
    boundary.add_edges_from(H_EDGES)
    connected = connected_subsets(thin, A)
    carrier_pairs = [
        (left, right)
        for left in connected
        for right in connected
        if ROOT in left
        and left.isdisjoint(right)
        and any(thin.has_edge(x, y) for x in left for y in right)
    ]
    partitions = adaptive_partitions(boundary)

    def hits(carrier, literal):
        return z3.Or(*(edge(vertex, literal) for vertex in carrier))

    for left, right in carrier_pairs:
        for first, second, _ in partitions:
            solver.add(
                z3.Not(
                    z3.And(
                        *(hits(left, literal) for literal in first),
                        *(hits(right, literal) for literal in second),
                    )
                )
            )
            solver.add(
                z3.Not(
                    z3.And(
                        *(hits(left, literal) for literal in second),
                        *(hits(right, literal) for literal in first),
                    )
                )
            )

    return solver, contact, edge, len(subsets), len(carrier_pairs), len(partitions)


def literal_host(model, contact) -> tuple[nx.Graph, nx.Graph]:
    graph = atomic_graph()
    graph.add_nodes_from(S + R)
    graph.add_edges_from(H_EDGES)
    graph.add_edge(ROOT, U)
    for (vertex, literal), variable in contact.items():
        if z3.is_true(model.eval(variable, model_completion=True)):
            graph.add_edge(vertex, literal)
    graph.add_edge(*R)
    for rich in R:
        graph.add_edges_from((rich, literal) for literal in S)
    return graph, graph.subgraph(set(A) | set(S)).copy()


def exact_rooted_k5(graph: nx.Graph) -> bool:
    vertices = tuple(graph)
    for roots in itertools.combinations(S, 5):
        solver = z3.Solver()
        label = {v: z3.Int(f"l_{i}") for i, v in enumerate(vertices)}
        depth = {v: z3.Int(f"d_{i}") for i, v in enumerate(vertices)}
        for v in vertices:
            solver.add(-1 <= label[v], label[v] < 5)
            solver.add(0 <= depth[v], depth[v] < len(vertices))
        for index, root in enumerate(roots):
            solver.add(label[root] == index, depth[root] == 0)
            for v in vertices:
                if v == root:
                    continue
                predecessors = [
                    z3.And(label[w] == index, depth[w] < depth[v])
                    for w in graph[v]
                ]
                solver.add(
                    z3.Implies(
                        label[v] == index,
                        z3.And(depth[v] > 0, z3.Or(*predecessors)),
                    )
                )
        for left, right in itertools.combinations(range(5), 2):
            solver.add(
                z3.Or(
                    *(
                        z3.Or(
                            z3.And(label[x] == left, label[y] == right),
                            z3.And(label[x] == right, label[y] == left),
                        )
                        for x, y in graph.edges()
                    )
                )
            )
        if solver.check() == z3.sat:
            return True
    return False


def has_clique_minor(graph: nx.Graph, order: int) -> bool:
    vertices = tuple(graph)
    solver = z3.Solver()
    label = {v: z3.Int(f"m_l_{i}") for i, v in enumerate(vertices)}
    depth = {v: z3.Int(f"m_d_{i}") for i, v in enumerate(vertices)}
    root = {
        (v, bag): z3.Bool(f"m_r_{i}_{bag}")
        for i, v in enumerate(vertices)
        for bag in range(order)
    }
    for v in vertices:
        solver.add(-1 <= label[v], label[v] < order)
        solver.add(0 <= depth[v], depth[v] < len(vertices))
    for bag in range(order):
        solver.add(z3.PbEq([(root[v, bag], 1) for v in vertices], 1))
        for v in vertices:
            solver.add(z3.Implies(root[v, bag], z3.And(label[v] == bag, depth[v] == 0)))
            predecessors = [
                z3.And(label[w] == bag, depth[w] < depth[v]) for w in graph[v]
            ]
            solver.add(
                z3.Implies(
                    z3.And(label[v] == bag, z3.Not(root[v, bag])),
                    z3.And(depth[v] > 0, z3.Or(*predecessors)),
                )
            )
    for left, right in itertools.combinations(range(order), 2):
        solver.add(
            z3.Or(
                *(
                    z3.Or(
                        z3.And(label[x] == left, label[y] == right),
                        z3.And(label[x] == right, label[y] == left),
                    )
                    for x, y in graph.edges()
                )
            )
        )
    return solver.check() == z3.sat


def independence_number(graph: nx.Graph) -> int:
    return max((len(clique) for clique in nx.find_cliques(nx.complement(graph))), default=0)


def dirac_ok(graph: nx.Graph) -> bool:
    return all(
        independence_number(graph.subgraph(graph[vertex])) <= graph.degree(vertex) - 5
        for vertex in graph
    )


def contract(graph: nx.Graph, keep, drop) -> nx.Graph:
    return nx.contracted_nodes(graph, keep, drop, self_loops=False, copy=True)


def bridge_lock_witness(graph: nx.Graph):
    contracted = contract(graph, ROOT, U)
    vertices = tuple(contracted)
    solver = z3.Solver()
    colour = {v: z3.Int(f"c_{i}") for i, v in enumerate(vertices)}
    for variable in colour.values():
        solver.add(0 <= variable, variable < 6)
    solver.add(colour[ROOT] == 0)
    for x, y in contracted.edges():
        solver.add(colour[x] != colour[y])

    attempts = 0
    while solver.check() == z3.sat and attempts < 2000:
        attempts += 1
        model = solver.model()
        assignment = {v: model.eval(colour[v]).as_long() for v in vertices}
        expanded = assignment | {U: assignment[ROOT]}
        minus_e = graph.copy()
        minus_e.remove_edge(ROOT, U)
        for beta in range(1, 6):
            lock_vertices = {v for v in minus_e if expanded[v] in (0, beta)}
            lock = minus_e.subgraph(lock_vertices).copy()
            if ROOT not in lock or U not in lock or not nx.has_path(lock, ROOT, U):
                continue
            for d in D:
                for t in Z:
                    f = (d, t)
                    if not lock.has_edge(*f):
                        continue
                    cut_lock = lock.copy()
                    cut_lock.remove_edge(*f)
                    if nx.has_path(cut_lock, ROOT, U):
                        continue
                    # Literal twin-view path geometries.  P_D stays in D+Omega_D;
                    # P_E stays outside E, with endpoints on Omega_E.
                    omega_d = set(Z) | set(TD)
                    omega_e = set(Z) | set(TE)
                    d_view = lock.subgraph(set(D) | omega_d)
                    e_view = lock.subgraph((set(graph) - set(E)) | omega_e)
                    other_d = [x for x in omega_d - {t} if x in d_view and nx.has_path(d_view, t, x)]
                    other_e = [x for x in omega_e - {t} if x in e_view and nx.has_path(e_view, t, x)]
                    if other_d and other_e:
                        return {
                            "colouring": expanded,
                            "beta": beta,
                            "f": f,
                            "P_D_end": other_d[0],
                            "P_E_end": other_e[0],
                            "attempts": attempts,
                        }
        solver.add(z3.Or(*(colour[v] != assignment[v] for v in vertices)))
    return None


def main() -> None:
    solver, contact, _edge, thin_sets, carrier_pairs, partitions = contact_solver()
    local_survivors = rooted_free = static_survivors = lock_survivors = 0
    while solver.check() == z3.sat:
        model = solver.model()
        local_survivors += 1
        graph, thin_closed = literal_host(model, contact)
        if not exact_rooted_k5(thin_closed):
            rooted_free += 1
            static = (
                nx.node_connectivity(graph) >= 7
                and dirac_ok(graph)
                and not has_clique_minor(graph, 7)
            )
            if static:
                static_survivors += 1
                lock = bridge_lock_witness(graph)
                if lock is not None:
                    lock_survivors += 1
                    print("SURVIVOR", lock)
                    print(
                        "contacts",
                        {
                            vertex: tuple(
                                literal
                                for literal in S
                                if literal != U
                                and (vertex, literal) in contact
                                and z3.is_true(model.eval(contact[vertex, literal], model_completion=True))
                            )
                            for vertex in A
                        },
                    )
                    return
        solver.add(
            z3.Or(
                *(
                    variable != z3.is_true(model.eval(variable, model_completion=True))
                    for variable in contact.values()
                )
            )
        )
        # This fixed shell has few literal placements; retain an explicit
        # hard ceiling so it remains a falsifier rather than a census.
        if local_survivors >= 5000:
            break

    print(
        "NO_BOUNDED_SURVIVOR",
        "local_no_carrier",
        local_survivors,
        "rooted_free",
        rooted_free,
        "seven_conn_dirac_k7free",
        static_survivors,
        "bridge_lock",
        lock_survivors,
        "thin_sets",
        thin_sets,
        "carrier_pairs",
        carrier_pairs,
        "adaptive_partitions",
        partitions,
        "gate_edge",
        GATE_EDGE,
        "shape",
        SHAPE,
        "profile",
        PROFILE,
        "cut_level",
        CUT_LEVEL,
        "root_full",
        ROOT_FULL,
    )


if __name__ == "__main__":
    main()
