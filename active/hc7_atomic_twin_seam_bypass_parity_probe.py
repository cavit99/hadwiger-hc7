#!/usr/bin/env python3
"""Verify a literal twin-seam shell for the two-colour bypass barrier.

This is a mechanism falsifier, not an HC7 counterexample.  It realizes the
two overlapping seven-boundaries, the unique compulsory edge, two full rich
packets, a response-matched nonseparating lock and two crossed minor
responses.  The host deliberately omits seven-connectivity and criticality,
and the two packets lift a rooted five-bag core to a terminal K7.
"""

from __future__ import annotations

from pathlib import Path
import sys


DEPS = Path(__file__).resolve().parent / "runtime" / "deps"
if DEPS.exists():
    sys.path.insert(0, str(DEPS))

import networkx as nx
import z3


Z = ("t", "q")
D = ("d", "d1")
E = ("z", "e1")
I = ("i1", "i2", "i3")
A0 = ("a1", "a2")
B0 = ("u", "b")
S = I + A0 + B0
K = Z + I
OMEGA_D = frozenset(K + A0)
OMEGA_E = frozenset(K + B0)
R = ("r1", "r2")
EDGE_E = ("z", "u")
EDGE_F = ("t", "d")


PHI = {
    "z": 0,
    "u": 0,
    "t": 1,
    "d": 0,
    "q": 2,
    "d1": 3,
    "e1": 4,
    "a1": 1,
    "a2": 4,
    "b": 1,
    "i1": 3,
    "i2": 4,
    "i3": 4,
    "r1": 2,
    "r2": 5,
}

PSI = {
    "z": 0,
    "u": 1,
    "t": 2,
    "d": 2,
    "q": 3,
    "d1": 0,
    "e1": 1,
    "a1": 0,
    "a2": 0,
    "b": 3,
    "i1": 4,
    "i2": 3,
    "i3": 1,
    "r1": 2,
    "r2": 5,
}


def build() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(Z + D + E + S + R)

    # The two lobes and their two literal gates.
    graph.add_edges_from((("d", "d1"), ("z", "e1"), ("t", "q")))
    graph.add_edges_from((gate, vertex) for gate in Z for vertex in D + E)

    # Exact old-boundary supports.  The compulsory edge is the only A-u edge.
    graph.add_edges_from(("d", literal) for literal in ("i1",) + A0)
    graph.add_edges_from(("d1", literal) for literal in ("i2", "i3"))
    graph.add_edges_from(("z", literal) for literal in ("i2", "i3"))
    graph.add_edges_from(("e1", literal) for literal in ("i1", "b"))
    graph.add_edge("z", "b")
    graph.add_edge(*EDGE_E)

    # A connected bipartite old boundary.  The two displayed arms are the
    # through-f lock continuation and the f-free bypass continuation.
    graph.add_edges_from(
        (
            ("u", "a1"),
            ("u", "b"),
            ("a1", "i1"),
            ("i1", "a2"),
            ("i1", "i2"),
            ("i1", "i3"),
        )
    )

    # Two adjacent singleton S-full packets.
    graph.add_edge("r1", "r2")
    graph.add_edges_from((rich, literal) for rich in R for literal in S)
    return graph


def proper_off(graph: nx.Graph, colouring: dict[str, int], omitted) -> bool:
    omitted = frozenset((tuple(sorted(omitted)),))
    return all(
        tuple(sorted((x, y))) in omitted or colouring[x] != colouring[y]
        for x, y in graph.edges()
    )


def partition(colouring: dict[str, int], boundary) -> tuple[tuple[str, ...], ...]:
    blocks: dict[int, list[str]] = {}
    for vertex in boundary:
        blocks.setdefault(colouring[vertex], []).append(vertex)
    return tuple(sorted(tuple(sorted(block)) for block in blocks.values()))


def has_clique_minor(graph: nx.Graph, order: int) -> bool:
    vertices = tuple(graph)
    solver = z3.Solver()
    label = {v: z3.Int(f"l_{i}") for i, v in enumerate(vertices)}
    depth = {v: z3.Int(f"d_{i}") for i, v in enumerate(vertices)}
    root = {
        (v, bag): z3.Bool(f"r_{i}_{bag}")
        for i, v in enumerate(vertices)
        for bag in range(order)
    }
    for vertex in vertices:
        solver.add(-1 <= label[vertex], label[vertex] < order)
        solver.add(0 <= depth[vertex], depth[vertex] < len(vertices))
    for bag in range(order):
        solver.add(z3.PbEq([(root[v, bag], 1) for v in vertices], 1))
        for vertex in vertices:
            solver.add(
                z3.Implies(
                    root[vertex, bag],
                    z3.And(label[vertex] == bag, depth[vertex] == 0),
                )
            )
            predecessors = [
                z3.And(label[neighbour] == bag, depth[neighbour] < depth[vertex])
                for neighbour in graph[vertex]
            ]
            solver.add(
                z3.Implies(
                    z3.And(label[vertex] == bag, z3.Not(root[vertex, bag])),
                    z3.And(depth[vertex] > 0, z3.Or(*predecessors)),
                )
            )
    for left in range(order):
        for right in range(left + 1, order):
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


def main() -> None:
    graph = build()
    assert proper_off(graph, PHI, EDGE_E)
    assert proper_off(graph, PSI, EDGE_F)
    assert PHI["z"] == PHI["u"]
    assert PSI["d"] == PSI["t"]
    assert PSI["z"] != PSI["u"]

    alpha, beta = PHI["z"], PHI["t"]
    lock_vertices = {v for v in graph if PHI[v] in (alpha, beta)}
    lock = graph.subgraph(lock_vertices).copy()
    lock.remove_edge(*EDGE_E)
    assert nx.has_path(lock, "z", "u")
    assert all(
        lock.has_edge(x, y)
        for x, y in zip(("z", "t", "d", "a1", "u"), ("t", "d", "a1", "u"))
    )
    assert all(
        lock.has_edge(x, y)
        for x, y in zip(("z", "b", "u"), ("b", "u"))
    )
    lock_without_f = lock.copy()
    lock_without_f.remove_edge(*EDGE_F)
    assert nx.has_path(lock_without_f, "z", "u")
    assert nx.has_path(lock_without_f, "d", "t")
    assert nx.has_path(lock_without_f, "z", "d")

    assert set(nx.node_connected_component(graph.subgraph(Z + D + E), "d")) == set(Z + D + E)
    assert nx.is_biconnected(graph.subgraph(Z + D + E))
    assert nx.is_connected(graph.subgraph(set(Z + D + E) - {"z"}))
    assert set(nx.node_connected_component(graph.subgraph(D), "d")) == set(D)
    assert set(nx.node_connected_component(graph.subgraph(E), "z")) == set(E)
    assert set().union(*(set(graph.neighbors(v)) & set(S) for v in D)) == set(I + A0)
    assert set().union(*(set(graph.neighbors(v)) & set(S) for v in E)) == set(I + B0)
    assert set(graph.neighbors("t")) & set(S) <= set(I)
    assert set(graph.neighbors("q")) & set(S) <= set(I)
    assert [x for x in Z + D + E if graph.has_edge(x, "u")] == ["z"]
    assert all(
        any(graph.has_edge(vertex, literal) for vertex in set(Z + D + E) - {"z"})
        for literal in set(S) - {"u"}
    )

    assert nx.is_connected(graph.subgraph(S))
    assert nx.is_bipartite(graph.subgraph(S))
    for rich in R:
        assert set(S) <= set(graph.neighbors(rich))
    assert graph.has_edge(*R)

    pi_d_phi = partition(PHI, OMEGA_D)
    pi_d_psi = partition(PSI, OMEGA_D)
    pi_e_phi = partition(PHI, OMEGA_E)
    pi_e_psi = partition(PSI, OMEGA_E)
    assert pi_d_phi != pi_d_psi
    assert pi_e_phi != pi_e_psi
    assert has_clique_minor(graph, 7)

    print("GREEN bypass_parity_shell")
    print("orders", graph.number_of_nodes(), graph.number_of_edges())
    print("connectivity", nx.node_connectivity(graph))
    print("Pi_D", pi_d_phi, "->", pi_d_psi)
    print("Pi_E", pi_e_phi, "->", pi_e_psi)


if __name__ == "__main__":
    main()
