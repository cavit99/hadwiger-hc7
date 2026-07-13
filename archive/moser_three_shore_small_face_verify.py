#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["networkx>=3.4"]
# ///
"""Transparent facial certificate for terminal Moser shores of order 4--6.

A non-owner partition supplies three faces F12,F13,F23.  The two roots
of block Ai can contact only vertices in the corresponding intersection
of two faces.  Thus every shore vertex v has at most

    1 + 2 * number_of_pairwise_intersections_containing(v)

boundary neighbours: one omitted singleton root, plus two roots for
each pair block.  The script checks the resulting degree upper bound on
the complete atlas of planar 3-connected graphs of orders four to six.
It contains no SAT solver and no minor-model search.
"""

from __future__ import annotations

import itertools

import networkx as nx


EXPECTED = {
    "C~": (4, 20, 0),
    "Dl{": (5, 35, 0),
    "Dn{": (6, 56, 0),
    "EtTg": (5, 30, 0),
    "Ehfw": (6, 56, 0),
    "EzNG": (6, 50, 0),
    "ER~g": (7, 77, 0),
    "Ep~o": (7, 70, 0),
    "Ep~w": (8, 104, 0),
    "EznW": (8, 88, 0),
}


def facial_cycles(graph: nx.Graph) -> tuple[frozenset[int], ...]:
    planar, embedding = nx.check_planarity(graph)
    assert planar
    visited: set[tuple[int, int]] = set()
    answer = []
    for u, v in embedding.edges():
        if (u, v) not in visited:
            answer.append(
                frozenset(embedding.traverse_face(u, v, visited))
            )
    return tuple(answer)


def triple_counts(
    graph: nx.Graph, faces: tuple[frozenset[int], ...]
) -> tuple[int, int]:
    nonempty_intersections = 0
    degree_compatible = 0
    for i, j, k in itertools.combinations_with_replacement(
        range(len(faces)), 3
    ):
        intersections = (
            faces[i] & faces[j],
            faces[i] & faces[k],
            faces[j] & faces[k],
        )
        if any(not intersection for intersection in intersections):
            continue
        nonempty_intersections += 1
        if all(
            graph.degree(vertex)
            + 1
            + 2
            * sum(vertex in intersection for intersection in intersections)
            >= 7
            for vertex in graph
        ):
            degree_compatible += 1
    return nonempty_intersections, degree_compatible


def main() -> None:
    records = {}
    for graph in nx.graph_atlas_g():
        if not 4 <= len(graph) <= 6:
            continue
        if nx.node_connectivity(graph) < 3:
            continue
        planar, _ = nx.check_planarity(graph)
        if not planar:
            continue
        graph = nx.convert_node_labels_to_integers(graph)
        graph6 = nx.to_graph6_bytes(graph, header=False).strip().decode()
        faces = facial_cycles(graph)
        nonempty, compatible = triple_counts(graph, faces)
        records[graph6] = (len(faces), nonempty, compatible)

    assert records == EXPECTED
    for graph6, record in records.items():
        print(graph6, *record)


if __name__ == "__main__":
    main()
