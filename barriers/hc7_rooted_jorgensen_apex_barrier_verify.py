#!/usr/bin/env python3
"""Verify the 13-vertex rooted-Jorgensen cofacial barrier."""

from __future__ import annotations

from itertools import combinations

import networkx as nx


GRAPH6 = b"LhcEJKtFNo^~~~"
Z = 0
APICES = (12, 13)


def witness() -> tuple[nx.Graph, nx.Graph, nx.Graph, set[int]]:
    triangulation = nx.icosahedral_graph()
    boundary = set(triangulation[Z])
    remainder = triangulation.copy()
    remainder.remove_node(Z)

    host = remainder.copy()
    host.add_edge(*APICES)
    for apex in APICES:
        host.add_edges_from((apex, vertex) for vertex in remainder)
    return triangulation, remainder, host, boundary


def facial_walks(graph: nx.Graph) -> list[list[int]]:
    planar, embedding = nx.check_planarity(graph)
    assert planar
    seen: set[tuple[int, int]] = set()
    walks = []
    for u, v in embedding.edges():
        if (u, v) not in seen:
            walks.append(embedding.traverse_face(u, v, seen))
    return walks


def connected_and_pairwise_adjacent(
    graph: nx.Graph, bags: list[set[int]]
) -> bool:
    return (
        all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
        and all(
            not bags[i] & bags[j]
            for i in range(len(bags))
            for j in range(i)
        )
        and all(
            any(graph.has_edge(u, v) for u in bags[i] for v in bags[j])
            for i in range(len(bags))
            for j in range(i)
        )
    )


def main() -> None:
    triangulation, remainder, host, boundary = witness()
    x_set = boundary | set(APICES)

    assert nx.to_graph6_bytes(host, header=False).strip() == GRAPH6
    assert (len(triangulation), triangulation.number_of_edges()) == (12, 30)
    assert nx.node_connectivity(triangulation) == 5
    assert boundary == {1, 5, 7, 8, 11}

    assert (len(remainder), remainder.number_of_edges()) == (11, 25)
    assert nx.node_connectivity(remainder) == 4
    containing_faces = [
        walk for walk in facial_walks(remainder) if boundary <= set(walk)
    ]
    assert containing_faces == [[1, 8, 7, 11, 5]]

    assert (len(host), host.number_of_edges()) == (13, 48)
    assert nx.node_connectivity(host) == 6
    assert len(x_set) == 7

    assert not any(
        nx.check_planarity(host.subgraph(set(host) - {vertex}))[0]
        for vertex in host
    )
    planarizing_pairs = [
        pair
        for pair in combinations(host, 2)
        if nx.check_planarity(host.subgraph(set(host) - set(pair)))[0]
    ]
    assert planarizing_pairs == [APICES]

    unrooted_k6 = [
        {APICES[0]},
        {APICES[1]},
        {1},
        {2},
        {8},
        {9, 3, 6},
    ]
    assert connected_and_pairwise_adjacent(host, unrooted_k6)

    # Adding v with neighbourhood X reconstructs the planar icosahedron
    # after deleting the two universal vertices.
    lifted = host.copy()
    lifted.add_edges_from((Z, vertex) for vertex in x_set)
    after_apices = lifted.subgraph(set(lifted) - set(APICES))
    assert nx.is_isomorphic(after_apices, triangulation)
    assert nx.node_connectivity(lifted) == 7

    vee_bags = [
        {APICES[0]},
        {APICES[1]},
        {0},
        {1},
        {5},
        {8, 2, 6},
        {4},
    ]
    assert connected_and_pairwise_adjacent(lifted, vee_bags[:6])
    assert nx.is_connected(lifted.subgraph(vee_bags[6]))
    assert not any(
        vee_bags[i] & vee_bags[j] for i in range(7) for j in range(i)
    )
    last_contacts = [
        i
        for i in range(6)
        if any(
            lifted.has_edge(u, v) for u in vee_bags[6] for v in vee_bags[i]
        )
    ]
    assert last_contacts == [0, 1, 4, 5]

    print("GREEN: 13-vertex rooted-Jorgensen barrier verified")
    print("H graph6:", GRAPH6.decode())
    print("kappa(T), kappa(R), kappa(H): 5, 4, 6")
    print("X:", sorted(x_set))
    print("unique planarizing pair:", planarizing_pairs)
    print("unrooted K6 and lifted K7^vee models verified")
    print("lifted graph is seven-connected and deletes to the icosahedron")


if __name__ == "__main__":
    main()
