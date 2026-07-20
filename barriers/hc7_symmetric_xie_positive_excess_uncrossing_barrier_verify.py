#!/usr/bin/env python3
"""Verify the symmetric positive-excess neighbourhood-uncrossing barrier.

Run from the repository root with::

    PYTHONPATH=active/runtime/deps python3 \
      barriers/hc7_symmetric_xie_positive_excess_uncrossing_barrier_verify.py

The construction is a join of an edge with a planar triangulation.  The
script verifies the literal order-eight separation, the two terminal-free
small cuts in the selected Xie completions, and the three full-neighbourhood
orders used by the barrier.
"""

from __future__ import annotations

from itertools import combinations

import networkx as nx


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
    return graph


def planar_factor() -> nx.Graph:
    """Apply five planar diagonal flips to the base triangulation."""

    graph = dual_truncated_icosahedron()
    flips = (
        ((17, 18), (1, 2)),
        ((13, 15), (0, 8)),
        ((27, 28), (11, 4)),
        ((23, 26), (4, 6)),
        ((12, 14), (0, 5)),
    )
    for old_edge, new_edge in flips:
        assert graph.has_edge(*old_edge)
        assert not graph.has_edge(*new_edge)
        graph.remove_edge(*old_edge)
        graph.add_edge(*new_edge)
        assert nx.check_planarity(graph)[0]
    return graph


def host_graph() -> tuple[nx.Graph, nx.Graph]:
    """Return the planar factor H and G=K2 join H."""

    planar = planar_factor()
    host = planar.copy()
    host.add_edge("p", "q")
    for vertex in planar:
        host.add_edge("p", vertex)
        host.add_edge("q", vertex)
    return planar, host


def full_neighbourhood(graph: nx.Graph, vertices: set) -> set:
    """Return the open full neighbourhood of a nonempty vertex set."""

    return set().union(*(set(graph[vertex]) for vertex in vertices)) - vertices


def xie_completion(
    graph: nx.Graph,
    vertices: set[int],
    triple: tuple[int, int, int],
    pair: tuple[int, int],
) -> nx.Graph:
    """Add the virtual edge and the six triple-to-pair edges."""

    completion = graph.subgraph(vertices).copy()
    completion.add_edge(*pair)
    completion.add_edges_from((a, b) for a in triple for b in pair)
    return completion


def components_after(graph: nx.Graph, cut: set[int]) -> list[set[int]]:
    """Return components after deleting ``cut``, deterministically ordered."""

    parts = [set(part) for part in nx.connected_components(graph.subgraph(set(graph) - cut))]
    return sorted(parts, key=lambda part: (len(part), tuple(sorted(part))))


def main() -> None:
    planar, graph = host_graph()

    assert (len(planar), planar.number_of_edges()) == (32, 90)
    assert nx.check_planarity(planar)[0]
    assert nx.node_connectivity(planar) == 5
    assert planar.degree(0) == planar.degree(4) == 7
    assert not planar.has_edge(0, 4)
    assert set(planar[0]).isdisjoint(planar[4])

    assert (len(graph), graph.number_of_edges()) == (34, 155)
    assert nx.node_connectivity(graph) == 7

    boundary = {"p", "q", 2, 12, 13, 17, 18, 19}
    outside = set(graph) - boundary
    outside_components = [set(part) for part in nx.connected_components(graph.subgraph(outside))]
    outside_components = sorted(outside_components, key=lambda part: (len(part), tuple(map(str, sorted(part)))))
    assert [len(part) for part in outside_components] == [1, 25]
    right = {1}
    left = outside - right
    assert right in outside_components and left in outside_components
    assert full_neighbourhood(graph, right) == boundary

    east = {0, 5, 6, 7, 8, 9, 14, 15, 21, 22, 25, 26, 27, 28, 31}
    west = {3, 4, 10, 11, 16, 20, 23, 24, 29, 30}
    assert east.isdisjoint(west) and east | west == left
    assert nx.is_connected(graph.subgraph(east))
    assert nx.is_connected(graph.subgraph(west))
    assert any(graph.has_edge(u, v) for u in east for v in west)

    east_vertices = east | {12}
    east_triple = (6, 7, 12)
    east_pair = (9, 21)
    east_cut = {5, 8, 12, 14, 15}
    east_completion = xie_completion(graph, east_vertices, east_triple, east_pair)
    east_parts = components_after(east_completion, east_cut)
    assert len(east_cut) == 5
    assert {0} in east_parts and len(east_parts) >= 2
    assert not ({0} & (set(east_triple) | set(east_pair)))
    assert set(graph[0]) & east == {5, 8, 14, 15}

    west_vertices = west | {2}
    west_triple = (3, 10, 2)
    west_pair = (16, 20)
    west_cut = {11, 23, 24}
    west_completion = xie_completion(graph, west_vertices, west_triple, west_pair)
    west_parts = components_after(west_completion, west_cut)
    assert len(west_cut) == 3
    assert {4} in west_parts and len(west_parts) >= 2
    assert not ({4} & (set(west_triple) | set(west_pair)))
    assert set(graph[4]) & west == {11, 23, 24}

    neighbourhood_zero = full_neighbourhood(graph, {0})
    neighbourhood_four = full_neighbourhood(graph, {4})
    neighbourhood_both = full_neighbourhood(graph, {0, 4})
    assert len(neighbourhood_zero) == 9
    assert len(neighbourhood_four) == 9
    assert len(neighbourhood_both) == 16
    assert neighbourhood_zero & neighbourhood_four == {"p", "q"}

    # Each singleton neighbourhood is an actual separator: after deleting
    # it, the other selected singleton remains outside the isolated vertex.
    assert 4 not in neighbourhood_zero and 0 not in neighbourhood_four
    assert len(set(graph) - neighbourhood_zero - {0}) > 0
    assert len(set(graph) - neighbourhood_four - {4}) > 0

    print("GREEN symmetric Xie positive-excess uncrossing barrier")
    print("H: vertices=32 edges=90 connectivity=5 degrees(0,4)=(7,7)")
    print(
        "G: vertices=34 edges=155 connectivity=7; "
        "exact order-8 separator with component sizes 1,25"
    )
    print("Xie cuts: east=5 terminal-free {0}; west=3 terminal-free {4}")
    print("full boundaries: b(0)=9 b(4)=9 b({0,4})=16 common={p,q}")
    print("scope: no proper-minor response or two-full-subgraph claim")


if __name__ == "__main__":
    main()
