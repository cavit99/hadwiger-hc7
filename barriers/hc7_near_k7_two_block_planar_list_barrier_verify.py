#!/usr/bin/env python3
"""Verify the pentagonal-antiprism two-block list barrier."""

from __future__ import annotations

import networkx as nx


def carrier() -> tuple[nx.Graph, list[str], list[str]]:
    graph = nx.Graph()
    top = [f"a{i}" for i in range(5)]
    bottom = [f"b{i}" for i in range(5)]
    for i in range(5):
        graph.add_edge(top[i], top[(i + 1) % 5])
        graph.add_edge(bottom[i], bottom[(i + 1) % 5])
        graph.add_edge(top[i], bottom[i])
        graph.add_edge(top[i], bottom[(i - 1) % 5])
    return graph, top, bottom


def proper(graph: nx.Graph, colouring: dict[str, int]) -> bool:
    return all(colouring[u] != colouring[v] for u, v in graph.edges())


def main() -> None:
    graph, top, bottom = carrier()
    assert len(graph) == 10 and graph.number_of_edges() == 20
    assert nx.is_connected(graph)
    assert nx.node_connectivity(graph) == 4
    planar, embedding = nx.check_planarity(graph)
    assert planar
    assert all(graph.has_edge(top[i], top[(i + 1) % 5]) for i in range(5))
    assert not any(
        graph.has_edge(top[i], top[j])
        for i in range(5)
        for j in range(i + 1, 5)
        if (j - i) % 5 not in (1, 4)
    )
    directed_seen: set[tuple[str, str]] = set()
    faces: list[list[str]] = []
    for u, v in embedding.edges():
        if (u, v) not in directed_seen:
            faces.append(embedding.traverse_face(u, v, directed_seen))
    assert any(set(face) == set(top) and len(face) == 5 for face in faces)

    boundary = [f"s{i}" for i in range(5)]
    host = graph.copy()
    host.add_nodes_from(boundary)
    for vertex in top:
        for s in boundary:
            host.add_edge(vertex, s)

    x_side = {top[0]}
    y_side = set(graph) - x_side
    assert nx.is_connected(graph.subgraph(y_side))
    assert any(graph.has_edge(u, v) for u in x_side for v in y_side)
    assert all(any(host.has_edge(u, s) for u in x_side) for s in boundary)
    assert all(any(host.has_edge(u, s) for u in y_side) for s in boundary)

    total = nx.Graph()
    total.add_nodes_from(["z", *boundary])
    total.add_edges_from(("z", s) for s in boundary)
    total_colouring = {"z": 5, **{s: i for i, s in enumerate(boundary)}}
    assert proper(total, total_colouring)

    two_block = nx.Graph()
    two_block.add_nodes_from(["zX", "zY", *boundary])
    two_block.add_edge("zX", "zY")
    for block in ("zX", "zY"):
        two_block.add_edges_from((block, s) for s in boundary)
    block_colouring = {
        "zX": 4,
        "zY": 5,
        boundary[0]: 0,
        boundary[1]: 0,
        boundary[2]: 1,
        boundary[3]: 2,
        boundary[4]: 3,
    }
    assert proper(two_block, block_colouring)
    assert set(block_colouring[s] for s in boundary) == {0, 1, 2, 3}
    assert all({4, 5} == set(range(6)) - {block_colouring[s] for s in boundary}
               for _ in top)
    assert not nx.is_bipartite(graph.subgraph(top))

    print("GREEN: four-connected planar pentagonal-antiprism barrier")
    print("total state uses five boundary colours; two-block state uses four")
    print("common two-lists fail on the facial C5")


if __name__ == "__main__":
    main()
