#!/usr/bin/env python3
"""Adversarial packet-escape probe for the atomic compulsory portal.

The construction keeps the exact width-two boundary and an exact rich-side
colour trace.  Its two full packets are stars: every full subpacket in a
star contains its centre.  In the two trace colours the only route between
the two named J-blocks is the edge between the two packet centres, so every
blocking path meets both packets.

The verifier distinguishes the static geometry from the HC7 kernel by
checking connectivity, Dirac's inequality, exact packet number, K7 and
K7^vee minors, and the canonical-pair K5 test independently.
"""

from __future__ import annotations

import itertools
import sys
from functools import lru_cache
from pathlib import Path


DEPS = Path(__file__).resolve().parent.parent / "active" / "runtime" / "deps"
if DEPS.exists():
    sys.path.insert(0, str(DEPS))

import networkx as nx
import z3


S = tuple(range(7))
U = 0
I = frozenset((0, 3, 5))
B = frozenset((1, 2))
C = frozenset((4, 6))
J = B | C
H_EDGES = ((0, 2), (2, 3), (3, 1), (0, 4), (4, 5), (0, 6))
THIN = "a"
P_CENTRE = "pc"
Q_CENTRE = "qb"


def build(leaves_per_packet: int = 3) -> tuple[nx.Graph, tuple[str, ...], tuple[str, ...]]:
    p_leaves = tuple(f"p{i}" for i in range(leaves_per_packet))
    q_leaves = tuple(f"q{i}" for i in range(leaves_per_packet))
    p = (P_CENTRE,) + p_leaves
    q = (Q_CENTRE,) + q_leaves

    graph = nx.Graph()
    graph.add_nodes_from(S + (THIN,) + p + q)
    graph.add_edges_from(H_EDGES)
    graph.add_edges_from((THIN, s) for s in S)

    # Packet centres carry the two blocking colours.  Each is forbidden
    # from the opposite J block by properness.
    graph.add_edges_from((P_CENTRE, s) for s in I | B)
    graph.add_edges_from((Q_CENTRE, s) for s in I | C)
    graph.add_edge(P_CENTRE, Q_CENTRE)

    # Leaves have spare colours and miss one literal each, so no leaf is a
    # singleton full packet.  All leaf-to-leaf edges are absent; hence every
    # connected full subpacket contains its star centre.
    for index, leaf in enumerate(p_leaves):
        missed = index % len(S)
        graph.add_edge(P_CENTRE, leaf)
        graph.add_edges_from((leaf, s) for s in S if s != missed)
    for index, leaf in enumerate(q_leaves):
        missed = (index + 3) % len(S)
        graph.add_edge(Q_CENTRE, leaf)
        graph.add_edges_from((leaf, s) for s in S if s != missed)

    return graph, p, q


def trace_colouring(p, q) -> dict[object, int]:
    colouring = {s: 0 if s in I else 1 if s in B else 2 for s in S}
    colouring[THIN] = 3
    colouring[P_CENTRE] = 2
    colouring[Q_CENTRE] = 1
    for index, leaf in enumerate(p[1:]):
        colouring[leaf] = 3 + index % 3
    for index, leaf in enumerate(q[1:]):
        colouring[leaf] = 4 + index % 2
    return colouring


def connected_full_packets(graph: nx.Graph, rich) -> list[frozenset]:
    rich = tuple(rich)
    answer = []
    for mask in range(1, 1 << len(rich)):
        packet = frozenset(rich[i] for i in range(len(rich)) if mask >> i & 1)
        if not nx.is_connected(graph.subgraph(packet)):
            continue
        if all(any(graph.has_edge(v, s) for v in packet) for s in S):
            answer.append(packet)
    return answer


def packing_number(packets) -> int:
    best = 0

    def search(start, used, count):
        nonlocal best
        best = max(best, count)
        for index in range(start, len(packets)):
            if packets[index].isdisjoint(used):
                search(index + 1, used | packets[index], count + 1)

    search(0, frozenset(), 0)
    return best


def alpha(graph: nx.Graph) -> int:
    return max(
        (len(clique) for clique in nx.find_cliques(nx.complement(graph))),
        default=0,
    )


def spanning_minor_model(graph: nx.Graph, k: int, near=False):
    """Exact Z3 search for a spanning K_k or K_k^vee model.

    Every clique-minor model in a connected graph extends to a spanning
    model.  Bag connectivity is encoded by one root and strictly decreasing
    integer depths along an in-bag neighbour relation.
    """
    vertices = tuple(graph)
    n = len(vertices)
    assigned = {
        (v, bag): z3.Bool(f"x_{index}_{bag}")
        for index, v in enumerate(vertices)
        for bag in range(k)
    }
    root = {
        (v, bag): z3.Bool(f"r_{index}_{bag}")
        for index, v in enumerate(vertices)
        for bag in range(k)
    }
    depth = {
        (v, bag): z3.Int(f"d_{index}_{bag}")
        for index, v in enumerate(vertices)
        for bag in range(k)
    }
    solver = z3.Solver()
    for v in vertices:
        solver.add(z3.PbEq([(assigned[v, bag], 1) for bag in range(k)], 1))
    for bag in range(k):
        solver.add(z3.PbEq([(root[v, bag], 1) for v in vertices], 1))
        for v in vertices:
            solver.add(z3.Implies(root[v, bag], assigned[v, bag]))
            solver.add(depth[v, bag] >= 0, depth[v, bag] < n)
            solver.add(z3.Implies(root[v, bag], depth[v, bag] == 0))
            lower_neighbour = z3.Or(
                *(
                    z3.And(assigned[w, bag], depth[w, bag] < depth[v, bag])
                    for w in graph[v]
                )
            )
            solver.add(
                z3.Implies(
                    z3.And(assigned[v, bag], z3.Not(root[v, bag])),
                    lower_neighbour,
                )
            )

    adjacent = {}
    for left, right in itertools.combinations(range(k), 2):
        adjacent[left, right] = z3.Or(
            *(
                z3.Or(
                    z3.And(assigned[u, left], assigned[v, right]),
                    z3.And(assigned[u, right], assigned[v, left]),
                )
                for u, v in graph.edges
            )
        )
    if not near:
        solver.add(*adjacent.values())
    else:
        # Bag zero is the deficient hub; bags 1,...,k-1 form a clique and
        # at most two hub spokes may be absent.
        solver.add(
            *(adjacent[i, j] for i, j in itertools.combinations(range(1, k), 2))
        )
        solver.add(z3.PbGe([(adjacent[0, j], 1) for j in range(1, k)], k - 3))

    if solver.check() != z3.sat:
        return None
    model = solver.model()
    return tuple(
        frozenset(v for v in vertices if z3.is_true(model.eval(assigned[v, bag])))
        for bag in range(k)
    )


def partition_minor_model(graph: nx.Graph, k: int, near=False):
    """Exact restricted-growth partition search, efficient through 12 vertices."""
    vertices = tuple(graph)
    n = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    rows = [0] * n
    for u, v in graph.edges:
        left, right = index[u], index[v]
        rows[left] |= 1 << right
        rows[right] |= 1 << left

    @lru_cache(maxsize=None)
    def connected(mask):
        reached = mask & -mask
        while True:
            expanded = reached
            todo = reached
            while todo:
                bit = todo & -todo
                todo ^= bit
                expanded |= rows[bit.bit_length() - 1] & mask
            if expanded == reached:
                return reached == mask
            reached = expanded

    blocks = []

    def accepted(masks):
        neighbourhoods = []
        for block in blocks:
            row = 0
            for vertex in block:
                row |= rows[vertex]
            neighbourhoods.append(row)
        adjacency = [
            [
                i == j or bool(neighbourhoods[i] & masks[j])
                for j in range(k)
            ]
            for i in range(k)
        ]
        if not near:
            return all(adjacency[i][j] for i, j in itertools.combinations(range(k), 2))
        for hub in range(k):
            rim = [i for i in range(k) if i != hub]
            if not all(adjacency[i][j] for i, j in itertools.combinations(rim, 2)):
                continue
            if sum(adjacency[hub][j] for j in rim) >= k - 3:
                return True
        return False

    def search(position):
        if position == n:
            if len(blocks) != k:
                return None
            masks = [sum(1 << v for v in block) for block in blocks]
            if not all(connected(mask) for mask in masks):
                return None
            if accepted(masks):
                return tuple(
                    frozenset(vertices[v] for v in block) for block in blocks
                )
            return None
        if len(blocks) + n - position < k:
            return None
        for block in blocks:
            block.append(position)
            witness = search(position + 1)
            block.pop()
            if witness is not None:
                return witness
        if len(blocks) < k:
            blocks.append([position])
            witness = search(position + 1)
            blocks.pop()
            if witness is not None:
                return witness
        return None

    return search(0)


def sparse_atomic_base():
    """Small K7^vee-free packet lock before optional contact repairs."""
    graph, p, q = build(1)
    pc, p_leaf = p
    qb, q_leaf = q
    graph.remove_edges_from(
        (v, s) for v in p + q for s in S if graph.has_edge(v, s)
    )
    graph.add_edge(pc, 1)
    graph.add_edges_from((p_leaf, s) for s in S if s != 1)
    graph.add_edge(qb, 4)
    graph.add_edges_from((q_leaf, s) for s in S if s != 4)
    return graph, p, q


def search_canonical_pair_failure():
    """Add the fewest trace-legal contacts seeking K5 after {a,u} deletion."""
    base, p, q = sparse_atomic_base()
    pc, p_leaf = p
    qb, q_leaf = q
    optional = (
        tuple((pc, s) for s in sorted((I | B) - {1}))
        + tuple((qb, s) for s in sorted((I | C) - {4}))
        + (
            (p_leaf, 1),
            (q_leaf, 4),
            (p_leaf, qb),
            (pc, q_leaf),
            (p_leaf, q_leaf),
        )
    )
    checked = 0
    with_k5 = 0
    near_triggers = []
    for edge in optional:
        graph = base.copy()
        graph.add_edge(*edge)
        if partition_minor_model(graph, 7, near=True) is not None:
            near_triggers.append(frozenset((edge,)))
    for size in range(len(optional) + 1):
        for chosen in itertools.combinations(optional, size):
            checked += 1
            chosen_set = frozenset(chosen)
            if any(trigger <= chosen_set for trigger in near_triggers):
                continue
            graph = base.copy()
            graph.add_edges_from(chosen)
            if packing_number(connected_full_packets(graph, p + q)) != 2:
                continue
            remainder = graph.copy()
            remainder.remove_nodes_from((THIN, U))
            k5 = partition_minor_model(remainder, 5)
            if k5 is None:
                continue
            with_k5 += 1
            near = partition_minor_model(graph, 7, near=True)
            if near is None:
                return {
                    "graph": graph,
                    "p": p,
                    "q": q,
                    "chosen": chosen,
                    "k5": k5,
                    "checked": checked,
                    "with_k5": with_k5,
                    "near_triggers": near_triggers,
                }
            near_triggers.append(chosen_set)
    return {
        "graph": None,
        "checked": checked,
        "with_k5": with_k5,
        "near_triggers": near_triggers,
    }


def first_k5_contact_sets(limit=20):
    base, p, q = sparse_atomic_base()
    pc, p_leaf = p
    qb, q_leaf = q
    optional = (
        tuple((pc, s) for s in sorted((I | B) - {1}))
        + tuple((qb, s) for s in sorted((I | C) - {4}))
        + (
            (p_leaf, 1),
            (q_leaf, 4),
            (p_leaf, qb),
            (pc, q_leaf),
            (p_leaf, q_leaf),
        )
    )
    answer = []
    checked = 0
    for size in range(len(optional) + 1):
        for chosen in itertools.combinations(optional, size):
            checked += 1
            graph = base.copy()
            graph.add_edges_from(chosen)
            remainder = graph.copy()
            remainder.remove_nodes_from((THIN, U))
            witness = partition_minor_model(remainder, 5)
            if witness is not None:
                answer.append((chosen, witness))
                if len(answer) >= limit:
                    return optional, answer, checked
    return optional, answer, checked


def main() -> None:
    graph, p, q = sparse_atomic_base()
    colouring = trace_colouring(p, q)
    assert all(colouring[u] != colouring[v] for u, v in graph.edges)
    assert nx.is_tree(graph.subgraph(S))
    assert nx.is_bipartite(graph.subgraph(S))
    assert I | J == frozenset(S) and I.isdisjoint(J)
    assert all(not graph.has_edge(x, y) for x, y in itertools.combinations(I, 2))
    assert all(not graph.has_edge(x, y) for x, y in itertools.combinations(J, 2))
    assert set(graph[THIN]) == set(S)
    assert graph.has_edge(THIN, U)

    packets = connected_full_packets(graph, p + q)
    assert frozenset(p) in packets and frozenset(q) in packets
    assert packing_number(packets) == 2

    two_colour = graph.subgraph(
        [v for v in graph if colouring[v] in {1, 2}]
    )
    component = nx.node_connected_component(two_colour, next(iter(B)))
    assert C & component
    assert P_CENTRE in component and Q_CENTRE in component
    assert all(
        P_CENTRE in path and Q_CENTRE in path
        for b in B
        for c in C
        for path in nx.all_simple_paths(two_colour, b, c)
    )

    kappa = nx.node_connectivity(graph)
    dirac_bad = {
        v: (graph.degree(v), alpha(graph.subgraph(graph[v])))
        for v in graph
        if alpha(graph.subgraph(graph[v])) > graph.degree(v) - 5
    }
    k7 = partition_minor_model(graph, 7)
    k7vee = partition_minor_model(graph, 7, near=True)
    canonical = graph.copy()
    canonical.remove_nodes_from((THIN, U))
    k5_after_pair = partition_minor_model(canonical, 5)

    classification = search_canonical_pair_failure()
    assert classification["graph"] is None
    assert classification["with_k5"] == 0
    singleton_triggers = {
        next(iter(trigger))
        for trigger in classification["near_triggers"]
        if len(trigger) == 1
    }
    expected_triggers = {
        (P_CENTRE, s) for s in (0, 2, 3, 5)
    } | {
        (Q_CENTRE, s) for s in (0, 3, 5, 6)
    } | {("p0", "q0")}
    assert singleton_triggers == expected_triggers

    print("vertices", len(graph), "edges", graph.number_of_edges())
    print("connectivity", kappa)
    print("packet_number", 2, "full_packets", len(packets))
    print("blocking_path_uses_both_packet_centres", True)
    print("dirac_bad", dirac_bad)
    print("K7_model", k7)
    print("K7vee_model", k7vee)
    print("K5_after_canonical_pair", k5_after_pair)
    print("trace_legal_extensions", classification["checked"])
    print("singleton_K7vee_triggers", sorted(map(str, singleton_triggers)))
    print("near_free_extension_with_canonical_K5", False)


if __name__ == "__main__":
    main()
