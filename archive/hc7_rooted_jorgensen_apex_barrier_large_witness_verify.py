#!/usr/bin/env python3
"""Verify the explicit cofacial-neighbour rooted-Jorgensen barrier."""

from __future__ import annotations

from itertools import combinations

import networkx as nx


def frequency_two_icosahedron() -> nx.Graph:
    base = nx.icosahedral_graph()
    planar, embedding = nx.check_planarity(base)
    assert planar

    seen: set[tuple[int, int]] = set()
    faces: list[list[int]] = []
    for u, v in embedding.edges():
        if (u, v) not in seen:
            faces.append(embedding.traverse_face(u, v, seen))
    assert len(faces) == 20
    assert {len(face) for face in faces} == {3}

    graph = base.copy()
    midpoint: dict[tuple[int, int], int] = {}
    for u, v in list(base.edges):
        edge = tuple(sorted((u, v)))
        middle = 12 + len(midpoint)
        midpoint[edge] = middle
        graph.remove_edge(u, v)
        graph.add_edges_from(((u, middle), (middle, v)))

    for a, b, c in faces:
        middle_vertices = [
            midpoint[tuple(sorted(edge))]
            for edge in ((a, b), (b, c), (c, a))
        ]
        graph.add_edges_from(combinations(middle_vertices, 2))
    return graph


def witness() -> tuple[nx.Graph, nx.Graph, nx.Graph, int, int, int]:
    triangulation = frequency_two_icosahedron()
    assert triangulation.has_edge(12, 15)
    assert set(nx.common_neighbors(triangulation, 12, 15)) == {0, 20}
    assert not triangulation.has_edge(0, 20)
    triangulation.remove_edge(12, 15)
    triangulation.add_edge(0, 20)
    assert nx.check_planarity(triangulation, counterexample=False)[0]

    z = 20
    remainder = triangulation.copy()
    remainder.remove_node(z)

    a, b = 42, 43
    host = remainder.copy()
    host.add_edge(a, b)
    for apex in (a, b):
        host.add_edges_from((apex, vertex) for vertex in remainder)
    return triangulation, remainder, host, z, a, b


def facial_walks(graph: nx.Graph) -> list[list[int]]:
    planar, embedding = nx.check_planarity(graph)
    assert planar
    seen: set[tuple[int, int]] = set()
    walks = []
    for u, v in embedding.edges():
        if (u, v) not in seen:
            walks.append(embedding.traverse_face(u, v, seen))
    return walks


def main() -> None:
    triangulation, remainder, host, z, a, b = witness()
    boundary = set(triangulation[z])

    assert (len(triangulation), triangulation.number_of_edges()) == (42, 120)
    assert nx.node_connectivity(triangulation) == 5
    assert triangulation.degree(z) == 7
    assert sorted(boundary) == [0, 1, 8, 12, 15, 17, 23]

    assert (len(remainder), remainder.number_of_edges()) == (41, 113)
    assert nx.node_connectivity(remainder) == 4
    containing_faces = [
        walk for walk in facial_walks(remainder) if boundary <= set(walk)
    ]
    assert containing_faces == [[0, 15, 8, 23, 17, 1, 12]]

    assert (len(host), host.number_of_edges()) == (43, 196)
    assert nx.node_connectivity(host) == 6

    # Exact apex and two-apex checks.  The unique planarizing pair is the
    # literal universal pair.
    assert not any(
        nx.check_planarity(host.subgraph(set(host) - {vertex}))[0]
        for vertex in host
    )
    planarizing_pairs = [
        pair
        for pair in combinations(host, 2)
        if nx.check_planarity(host.subgraph(set(host) - set(pair)))[0]
    ]
    assert planarizing_pairs == [(a, b)]

    # The robustness proof reduces to these exact local facts; it does not
    # require enumerating C(43,6) deletion sets.
    assert len(boundary) == 7
    assert nx.node_connectivity(triangulation) == 5
    assert set(triangulation[z]) == boundary

    print("GREEN: explicit rooted-Jorgensen apex barrier verified")
    print("T: n=42, m=120, kappa=5, degree(z)=7")
    print("R: n=41, m=113, kappa=4, X is cofacial")
    print("H: n=43, m=196, kappa=6, nonapex")
    print("unique planarizing pair:", planarizing_pairs)


if __name__ == "__main__":
    main()
