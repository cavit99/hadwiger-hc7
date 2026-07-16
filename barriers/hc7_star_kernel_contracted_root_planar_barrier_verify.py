#!/usr/bin/env python3
"""Verify the contracted-root planar barrier in the five-support star branch."""

from __future__ import annotations

from itertools import combinations
import sys

sys.path.insert(0, "active/runtime/deps")

import networkx as nx  # noqa: E402
from z3 import Bool, If, Implies, Int, Solver, Sum, unsat  # noqa: E402


def dual_truncated_icosahedron() -> nx.Graph:
    """Return a deterministic 32-vertex planar triangulation."""

    icosahedron = nx.icosahedral_graph()
    faces = sorted(
        tuple(sorted(clique))
        for clique in nx.enumerate_all_cliques(icosahedron)
        if len(clique) == 3
    )
    assert len(faces) == 20

    graph = nx.Graph()
    graph.add_nodes_from(range(32))
    for face_vertex, face in enumerate(faces, 12):
        graph.add_edges_from((face_vertex, vertex) for vertex in face)
    for (left, face_left), (right, face_right) in combinations(
        list(enumerate(faces, 12)), 2
    ):
        if len(set(face_left) & set(face_right)) == 2:
            graph.add_edge(left, right)

    assert graph.number_of_edges() == 90
    assert nx.check_planarity(graph)[0]
    assert nx.node_connectivity(graph) == 5
    return graph


def facial_cycles(graph: nx.Graph) -> set[tuple[int, ...]]:
    """Return all facial cycles, canonically up to rotation and reversal."""

    planar, embedding = nx.check_planarity(graph)
    assert planar
    seen: set[tuple[int, int]] = set()
    faces: set[tuple[int, ...]] = set()
    for left, right in embedding.edges():
        if (left, right) in seen:
            continue
        face = embedding.traverse_face(left, right, seen)
        rotations = []
        for word in (face, list(reversed(face))):
            rotations.extend(
                tuple(word[offset:] + word[:offset])
                for offset in range(len(word))
            )
        faces.add(min(rotations))
    return faces


def expand_true_twins(
    quotient: nx.Graph, a: int, b: int
) -> tuple[nx.Graph, tuple[int, str], tuple[int, str]]:
    """Undo the two contractions while retaining the old root labels."""

    graph = quotient.copy()
    a_prime = "a_prime"
    b_prime = "b_prime"
    graph.add_node(a_prime)
    graph.add_node(b_prime)
    graph.add_edge(a, a_prime)
    graph.add_edge(b, b_prime)
    graph.add_edges_from((a_prime, vertex) for vertex in quotient[a])
    graph.add_edges_from((b_prime, vertex) for vertex in quotient[b])
    graph.add_edge(a_prime, b_prime)
    return graph, (a, a_prime), (b, b_prime)


def paired_paths_exist(
    graph: nx.Graph,
    source_a: int,
    targets_a: set[int],
    source_b: int,
    targets_b: set[int],
) -> bool:
    """Decide the exact two-path question by finite simple-flow encoding."""

    for target_a in sorted(targets_a):
        for target_b in sorted(targets_b):
            if target_a == target_b:
                continue

            solver = Solver()
            used: dict[tuple[int, object], Bool] = {}
            arc: dict[tuple[int, object, object], Bool] = {}
            order: dict[tuple[int, object], Int] = {}

            specifications = (
                (source_a, target_a, source_b),
                (source_b, target_b, source_a),
            )
            for commodity, (source, target, forbidden) in enumerate(
                specifications
            ):
                for vertex in graph:
                    if vertex == forbidden:
                        continue
                    used[commodity, vertex] = Bool(
                        f"used_{commodity}_{vertex}"
                    )
                    order[commodity, vertex] = Int(
                        f"order_{commodity}_{vertex}"
                    )
                    solver.add(order[commodity, vertex] >= 0)
                    solver.add(order[commodity, vertex] <= len(graph))

                for left, right in graph.edges():
                    if forbidden in {left, right}:
                        continue
                    arc[commodity, left, right] = Bool(
                        f"arc_{commodity}_{left}_{right}"
                    )
                    arc[commodity, right, left] = Bool(
                        f"arc_{commodity}_{right}_{left}"
                    )

                for vertex in graph:
                    if vertex == forbidden:
                        continue
                    incoming = [
                        arc[commodity, neighbour, vertex]
                        for neighbour in graph[vertex]
                        if (commodity, neighbour, vertex) in arc
                    ]
                    outgoing = [
                        arc[commodity, vertex, neighbour]
                        for neighbour in graph[vertex]
                        if (commodity, vertex, neighbour) in arc
                    ]
                    in_degree = Sum([If(value, 1, 0) for value in incoming])
                    out_degree = Sum([If(value, 1, 0) for value in outgoing])
                    if vertex == source:
                        solver.add(in_degree == 0, out_degree == 1)
                        solver.add(used[commodity, vertex])
                        solver.add(order[commodity, vertex] == 0)
                    elif vertex == target:
                        solver.add(in_degree == 1, out_degree == 0)
                        solver.add(used[commodity, vertex])
                    else:
                        solver.add(
                            in_degree == If(used[commodity, vertex], 1, 0)
                        )
                        solver.add(
                            out_degree == If(used[commodity, vertex], 1, 0)
                        )

                for (index, left, right), selected in list(arc.items()):
                    if index != commodity:
                        continue
                    solver.add(
                        Implies(
                            selected,
                            order[commodity, right]
                            == order[commodity, left] + 1,
                        )
                    )

            for vertex in graph:
                occupancies = [
                    used[commodity, vertex]
                    for commodity in range(2)
                    if (commodity, vertex) in used
                ]
                if len(occupancies) == 2:
                    solver.add(
                        Sum([If(value, 1, 0) for value in occupancies]) <= 1
                    )

            if solver.check() != unsat:
                return True
    return False


def main() -> None:
    triangulation = dual_truncated_icosahedron()
    u, a, v, b, p = 12, 13, 0, 1, 18

    assert triangulation.has_edge(u, a)
    assert set(nx.common_neighbors(triangulation, u, a)) == {v, b}
    assert p in set(nx.common_neighbors(triangulation, a, b)) - {u}

    quotient = triangulation.copy()
    quotient.remove_edge(u, a)
    assert nx.node_connectivity(quotient) == 5
    assert not quotient.has_edge(u, a)
    assert not quotient.has_edge(v, b)

    cycle = (u, v, a, b)
    rotations = {
        tuple(word[offset:] + word[:offset])
        for word in (list(cycle), list(reversed(cycle)))
        for offset in range(4)
    }
    assert facial_cycles(quotient) & rotations

    graph, edge_a, edge_b = expand_true_twins(quotient, a, b)
    exterior = graph.copy()
    exterior.remove_nodes_from({u, v})

    assert nx.node_connectivity(graph) == 5
    assert nx.node_connectivity(exterior) == 4
    assert all(not graph.has_edge(u, vertex) for vertex in edge_a)
    assert all(graph.has_edge(v, vertex) for vertex in edge_a)
    assert all(not graph.has_edge(v, vertex) for vertex in edge_b)
    assert all(graph.has_edge(u, vertex) for vertex in edge_b)

    literal_k5 = set(edge_a) | set(edge_b) | {p}
    assert all(
        graph.has_edge(left, right)
        for left, right in combinations(literal_k5, 2)
    )

    recovered = nx.contracted_nodes(
        graph, edge_a[0], edge_a[1], self_loops=False
    )
    recovered = nx.contracted_nodes(
        recovered, edge_b[0], edge_b[1], self_loops=False
    )
    recovered = nx.Graph(recovered)
    assert set(recovered) == set(quotient)
    assert set(map(frozenset, recovered.edges())) == set(
        map(frozenset, quotient.edges())
    )

    path_graph = quotient.copy()
    path_graph.remove_nodes_from({u, v})
    targets_a = set(quotient[u]) - {v, b}
    targets_b = set(quotient[v]) - {u, a}
    assert not paired_paths_exist(path_graph, a, targets_a, b, targets_b)

    # Extend the same exterior to the full five-edge normalized incidence
    # pattern.  This graph is intentionally not K7-minor-free.
    a_prime = edge_a[1]
    b_prime = edge_b[1]
    leaves = (u, v, "r", "s", "t")
    defect_edges = (
        edge_a,
        edge_b,
        (a, b),
        (a, b_prime),
        (a_prime, b),
    )
    host = exterior.copy()
    host.add_nodes_from(leaves)
    host.add_edges_from(combinations(leaves, 2))
    for leaf in (u, v):
        host.add_edges_from(
            (leaf, vertex) for vertex in graph[leaf] if vertex in exterior
        )
    for leaf, defect_edge in zip(leaves[2:], defect_edges[2:]):
        host.add_edges_from(
            (leaf, vertex)
            for vertex in exterior
            if vertex not in defect_edge
        )

    assert nx.node_connectivity(host) == 8
    assert len({frozenset(edge) for edge in defect_edges}) == 5
    for index, (leaf, defect_edge) in enumerate(zip(leaves, defect_edges)):
        assert all(not host.has_edge(leaf, end) for end in defect_edge)
        assert all(
            any(host.has_edge(other_leaf, end) for end in defect_edge)
            for other_index, other_leaf in enumerate(leaves)
            if other_index != index
        )
    assert all(
        host.has_edge(left, right)
        for left, right in combinations(literal_k5, 2)
    )

    carrier_s = {8, a, b_prime}
    carrier_t = {b, a_prime, 15}
    assert carrier_s.isdisjoint(carrier_t)
    assert nx.is_connected(host.subgraph(carrier_s))
    assert nx.is_connected(host.subgraph(carrier_t))
    assert any(host.has_edge("s", vertex) for vertex in carrier_s)
    assert any(host.has_edge("t", vertex) for vertex in carrier_t)
    assert any(
        host.has_edge(left, right)
        for left in carrier_s
        for right in carrier_t
    )
    assert all(
        any(host.has_edge(leaf, vertex) for vertex in carrier)
        for carrier in (carrier_s, carrier_t)
        for leaf in leaves
    )

    print("GREEN: contracted-root planar star-kernel barrier verified")
    print("connectivity T,Q,J,H,G0", 5, 5, 5, 4, 8)
    print("facial roots", cycle)
    print("repair target sets", sorted(targets_a), sorted(targets_b))


if __name__ == "__main__":
    main()
