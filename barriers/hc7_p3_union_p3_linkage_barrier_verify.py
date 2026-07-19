"""Verify the finite core of the ordered-P3-pair barrier.

The topological no-linkage argument and the join-minor argument are written
in the adjacent Markdown proof.  This script checks the explicit planar
core, including all possible vertex cuts of order at most four.
"""

from itertools import combinations
from math import comb

import networkx as nx


FACES = (
    (0, 1, 5),
    (0, 1, 8),
    (0, 5, 11),
    (0, 7, 8),
    (0, 7, 11),
    (1, 2, 6),
    (1, 2, 8),
    (1, 5, 6),
    (2, 3, 6),
    (2, 3, 9),
    (2, 8, 9),
    (3, 4, 6),
    (3, 4, 10),
    (3, 9, 10),
    (4, 5, 6),
    (4, 5, 11),
    (4, 10, 11),
    (7, 8, 9),
    (7, 9, 10),
    (7, 10, 11),
)


def build_core() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(f"p{vertex}" for vertex in range(12))
    graph.add_nodes_from(f"h{index}" for index in range(20))

    for index, face in enumerate(FACES):
        for vertex in face:
            graph.add_edge(f"p{vertex}", f"h{index}")

    for index, face in enumerate(FACES):
        for earlier, other_face in enumerate(FACES[:index]):
            if len(set(face) & set(other_face)) == 2:
                graph.add_edge(f"h{index}", f"h{earlier}")

    assert graph.has_edge("h0", "h1")
    graph.remove_edge("h0", "h1")
    return graph


def facial_walks(graph: nx.Graph) -> list[tuple[str, ...]]:
    planar, embedding = nx.check_planarity(graph)
    assert planar
    marked: set[tuple[str, str]] = set()
    walks: list[tuple[str, ...]] = []
    for left, right in embedding.edges():
        if (left, right) not in marked:
            walks.append(tuple(embedding.traverse_face(left, right, marked)))
    return walks


def main() -> None:
    graph = build_core()
    assert graph.number_of_nodes() == 32
    assert graph.number_of_edges() == 89
    assert min(dict(graph.degree()).values()) == 5

    checked = 0
    vertices = tuple(graph.nodes())
    for order in range(5):
        for deleted in combinations(vertices, order):
            remainder = graph.copy()
            remainder.remove_nodes_from(deleted)
            assert nx.is_connected(remainder), deleted
            checked += 1
    assert checked == sum(comb(32, order) for order in range(5)) == 41_449

    nontriangular = [walk for walk in facial_walks(graph) if len(walk) != 3]
    assert len(nontriangular) == 1
    quadrilateral = nontriangular[0]
    target = ("p0", "h1", "p1", "h0")
    rotations = [quadrilateral[i:] + quadrilateral[:i] for i in range(4)]
    reversed_walk = tuple(reversed(quadrilateral))
    rotations += [reversed_walk[i:] + reversed_walk[:i] for i in range(4)]
    assert target in rotations

    print("vertices=32 edges=89 minimum_degree=5")
    print(f"small_vertex_cut_deletions_checked={checked}")
    print("quadrilateral=p0,h1,p1,h0")
    print("alternating_pairs=p0-p1,h1-h0")
    print("certificate=PASS")


if __name__ == "__main__":
    main()
