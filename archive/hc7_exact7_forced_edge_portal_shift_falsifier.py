#!/usr/bin/env python3
"""Adversarial probe for the forced-edge portal-shift mechanism.

The probe has two parts.

1.  It verifies one literal expanded lobe-star whose every connected
    two-carrier partition fails the width-two bipartition duty.  The thin
    shore is 3-connected and has internal minimum degree seven, and the
    resulting host satisfies every Dirac neighbourhood inequality.  Its
    first kernel failures are exhibited exactly: connectivity is six and
    the contracted quotient has the displayed K7^vee model.

2.  On the natural lobe-saturated expansion with two K5 lobes, three
    independent gates complete to both lobes, and two adjacent K4 rich
    packets of exact packing number two, Z3 exhausts *all* literal contact
    assignments in the D0-star support pattern.  It proves that no
    assignment can simultaneously be seven-connected and defeat every
    legal two-carrier duty split.

This is a bounded falsification/certification experiment, not a proof for
arbitrary expanded lobes.
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path


DEPS = Path(__file__).resolve().parent / "runtime" / "deps"
if DEPS.exists():
    sys.path.insert(0, str(DEPS))

import networkx as nx
import z3


S = ("c", "a1", "t1", "a2", "t2", "a3", "t3")
H_EDGES = (
    ("c", "a1"),
    ("c", "a2"),
    ("c", "a3"),
    ("a1", "t2"),
    ("t1", "a3"),
    ("a2", "t3"),
)
B_DUTY = frozenset(("a1", "a2", "a3"))
W_DUTY = frozenset(S) - B_DUTY
A_SUPPORT = frozenset(("c", "t2", "a1", "a2"))
C_SUPPORT = frozenset(("c", "t1", "t3", "a3"))
D = tuple(f"d{i}" for i in range(5))
E = tuple(f"e{i}" for i in range(5))
T = ("z0", "z1", "z2")
L = D + E + T
P_PACKET = tuple(f"p{i}" for i in range(4))
Q_PACKET = tuple(f"q{i}" for i in range(4))
R = P_PACKET + Q_PACKET
V = S + L + R


def base_graph() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(V)
    graph.add_edges_from(H_EDGES)
    graph.add_edges_from(itertools.combinations(D, 2))
    graph.add_edges_from(itertools.combinations(E, 2))
    graph.add_edges_from((gate, vertex) for gate in T for vertex in D + E)
    graph.add_edges_from(itertools.combinations(P_PACKET, 2))
    graph.add_edges_from(itertools.combinations(Q_PACKET, 2))
    graph.add_edge("p0", "q0")
    for packet in (P_PACKET, Q_PACKET):
        for index, vertex in enumerate(packet):
            missed = "t3" if index == 3 else "c"
            graph.add_edges_from(
                (vertex, literal) for literal in S if literal != missed
            )
    return graph


def legal_partitions(graph: nx.Graph):
    answer = []
    for mask in range(1, 1 << (len(L) - 1)):
        left = frozenset(L[index] for index in range(len(L)) if mask >> index & 1)
        right = frozenset(L) - left
        if nx.is_connected(graph.subgraph(left)) and nx.is_connected(
            graph.subgraph(right)
        ):
            answer.append((left, right))
    return answer


def support(rows, vertices):
    return frozenset().union(*(rows[vertex] for vertex in vertices))


def is_duty_split(rows, left, right) -> bool:
    left_support = support(rows, left)
    right_support = support(rows, right)
    return (
        B_DUTY <= left_support and W_DUTY <= right_support
    ) or (
        W_DUTY <= left_support and B_DUTY <= right_support
    )


def independence_number(graph: nx.Graph) -> int:
    return max(
        (len(clique) for clique in nx.find_cliques(nx.complement(graph))),
        default=0,
    )


def rich_full_packets(graph: nx.Graph):
    packets = []
    for mask in range(1, 1 << len(R)):
        candidate = frozenset(
            R[index] for index in range(len(R)) if mask >> index & 1
        )
        if nx.is_connected(graph.subgraph(candidate)) and all(
            any(graph.has_edge(vertex, literal) for vertex in candidate)
            for literal in S
        ):
            packets.append(candidate)
    return packets


def packet_packing_number(packets):
    best = 0

    def search(index, used, count):
        nonlocal best
        best = max(best, count)
        for next_index in range(index, len(packets)):
            if packets[next_index].isdisjoint(used):
                search(next_index + 1, used | packets[next_index], count + 1)

    search(0, frozenset(), 0)
    return best


def explicit_obstruction():
    graph = base_graph()
    rows = {
        "d0": frozenset(("c", "t2", "a1")),
        "d1": frozenset(("c", "t2", "a2")),
        "d2": frozenset(("c",)),
        "d3": frozenset(("c",)),
        "d4": frozenset(("c",)),
        "e0": frozenset(("t3", "t1", "a3")),
        "e1": frozenset(("c", "t3", "t1")),
        "e2": frozenset(("t3",)),
        "e3": frozenset(("t3",)),
        "e4": frozenset(("t3",)),
        "z0": frozenset(("t3", "t1", "a3")),
        "z1": frozenset(("t3", "t1", "a3")),
        "z2": frozenset(("c", "t3", "t1")),
    }
    graph.add_edges_from(
        (vertex, literal) for vertex, row in rows.items() for literal in row
    )

    thin = graph.subgraph(L)
    assert nx.node_connectivity(thin) == 3
    assert min(dict(thin.degree()).values()) == 7
    assert support(rows, D) == A_SUPPORT
    assert support(rows, E) == C_SUPPORT
    assert all(rows[gate] <= C_SUPPORT for gate in T)
    partitions = legal_partitions(thin)
    assert len(partitions) == 3_131
    assert not any(is_duty_split(rows, left, right) for left, right in partitions)

    assert nx.node_connectivity(graph) == 6
    cut = nx.minimum_node_cut(graph)
    assert len(cut) == 6
    dirac = {
        vertex: (
            graph.degree(vertex),
            independence_number(graph.subgraph(graph[vertex])),
        )
        for vertex in graph
    }
    assert all(alpha <= degree - 5 for degree, alpha in dirac.values())
    packets = rich_full_packets(graph)
    assert frozenset(P_PACKET) in packets
    assert frozenset(Q_PACKET) in packets
    assert packet_packing_number(packets) == 2

    quotient = nx.Graph()
    quotient.add_nodes_from(S + ("D", "E") + T + ("P", "Q"))
    quotient.add_edges_from(H_EDGES)
    quotient.add_edges_from(("D", literal) for literal in A_SUPPORT)
    quotient.add_edges_from(("E", literal) for literal in C_SUPPORT)
    quotient.add_edges_from(
        (gate, literal) for gate in T for literal in rows[gate]
    )
    quotient.add_edges_from((lobe, gate) for lobe in ("D", "E") for gate in T)
    quotient.add_edge("P", "Q")
    quotient.add_edges_from(
        (packet, literal) for packet in ("P", "Q") for literal in S
    )
    bags = (
        frozenset(("c",)),
        frozenset(("a1", "Q")),
        frozenset(("z1", "t1", "D")),
        frozenset(("z2", "a2", "t3", "z0")),
        frozenset(("t2", "P")),
        frozenset(("a3",)),
        frozenset(("E",)),
    )
    assert all(nx.is_connected(quotient.subgraph(bag)) for bag in bags)
    missing = [
        (left_index, right_index)
        for left_index, right_index in itertools.combinations(range(7), 2)
        if not any(
            quotient.has_edge(left, right)
            for left in bags[left_index]
            for right in bags[right_index]
        )
    ]
    assert missing == [(1, 6), (4, 6)]
    return cut, dirac, bags, missing, len(packets)


def exact_saturated_search():
    graph = base_graph()
    partitions = legal_partitions(graph.subgraph(L))
    allowed = sorted(
        {(vertex, literal) for vertex in D for literal in A_SUPPORT}
        | {(vertex, literal) for vertex in E + T for literal in C_SUPPORT}
    )
    variables = {
        edge: z3.Bool(f"edge_{edge[0]}_{edge[1]}") for edge in allowed
    }
    solver = z3.Solver()

    for literal in A_SUPPORT:
        solver.add(z3.Or(*(variables[vertex, literal] for vertex in D)))
    for literal in C_SUPPORT:
        solver.add(z3.Or(*(variables[vertex, literal] for vertex in E)))
    for vertex in L:
        solver.add(
            z3.Or(
                *(value for (left, _), value in variables.items() if left == vertex)
            )
        )

    def covers(vertices, duty):
        return z3.And(
            *(
                z3.Or(
                    *(
                        variables[vertex, literal]
                        for vertex in vertices
                        if (vertex, literal) in variables
                    )
                )
                for literal in duty
            )
        )

    for left, right in partitions:
        solver.add(z3.Not(z3.And(covers(left, B_DUTY), covers(right, W_DUTY))))
        solver.add(z3.Not(z3.And(covers(left, W_DUTY), covers(right, B_DUTY))))

    cut_clauses = 0
    while solver.check() == z3.sat:
        model = solver.model()
        candidate = graph.copy()
        candidate.add_edges_from(
            edge
            for edge, variable in variables.items()
            if z3.is_true(model.eval(variable))
        )
        connectivity = nx.node_connectivity(candidate)
        if connectivity >= 7:
            return False, cut_clauses, candidate

        cut = nx.minimum_node_cut(candidate)
        remainder = candidate.copy()
        remainder.remove_nodes_from(cut)
        components = list(nx.connected_components(remainder))
        assert len(components) >= 2
        component = min(components, key=lambda item: (len(item), sorted(item)))
        opposite = set(V) - set(cut) - set(component)
        crossing = [
            variable
            for (left, right), variable in variables.items()
            if left not in cut
            and right not in cut
            and (
                (left in component and right in opposite)
                or (right in component and left in opposite)
            )
        ]
        solver.add(z3.Or(*crossing) if crossing else z3.BoolVal(False))
        cut_clauses += 1

    return True, cut_clauses, None


def main() -> None:
    cut, dirac, bags, missing, packet_count = explicit_obstruction()
    unsat, cut_clauses, witness = exact_saturated_search()
    assert unsat and witness is None
    print("VERIFIED explicit parity-locked expansion")
    print("thin_order", len(L), "thin_connectivity", 3, "thin_min_degree", 7)
    print("host_connectivity", 6, "minimum_cut", sorted(cut))
    print("all_Dirac_inequalities", True)
    print("rich_full_packets", packet_count, "rich_packet_packing", 2)
    print("quotient_K7vee_bags", tuple(tuple(sorted(bag)) for bag in bags))
    print("quotient_missing_pairs", missing)
    print("EXACT bounded saturated search")
    print("contact_variables", 52)
    print("legal_connected_partitions", 3_131)
    print("connectivity_cut_clauses", cut_clauses)
    print("seven_connected_and_parity_locked", False)


if __name__ == "__main__":
    main()
