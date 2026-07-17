#!/usr/bin/env python3
"""Verify the nested-interval attachment-count barrier.

The script uses only the standard library.  A displayed tree decomposition
of width five is the negative K7-minor certificate.
"""

from __future__ import annotations

import itertools


NAMES = (
    "a0", "a1", "a2", "a3", "x", "y",
    "b0", "b1", "b2", "r", "p", "q",
    *(f"s{i}" for i in range(12)),
    "c", "d",
)

A0, A1, A2, A3, X, Y = range(6)
B0, B1, B2, R, P, Q = range(6, 12)
MIDS = tuple(range(12, 24))
C, D = 24, 25


def edge(left: int, right: int) -> tuple[int, int]:
    return tuple(sorted((left, right)))


def graph_edges() -> set[tuple[int, int]]:
    edges = {
        *map(lambda pair: edge(*pair), itertools.combinations((A0, A1, A2, A3), 2)),
        edge(X, Y), edge(X, A0), edge(X, A1), edge(X, A2), edge(Y, A3),
        *(
            edge(*pair)
            for pair in itertools.combinations((B0, B1, B2, R, P, Q), 2)
            if pair != (P, Q)
        ),
        edge(A0, B0), edge(A1, B1), edge(A2, B2),
        edge(A3, P), edge(X, Q),
    }
    p5 = (Y, *MIDS, R)
    edges.update(edge(left, right) for left, right in zip(p5, p5[1:]))
    edges.update(edge(C, vertex) for vertex in (A3, X, *MIDS[:6]))
    edges.update(edge(D, vertex) for vertex in (Y, R, *MIDS[6:]))
    return edges


BAGS = (
    (3, 4, 9, 24),
    (5, 9, 18, 24),
    (5, 9, 18, 25),
    (5, 12, 17, 24),
    (5, 17, 18, 24),
    (9, 18, 23, 25),
    (12, 13, 14, 24),
    (12, 14, 15, 24),
    (12, 15, 16, 24),
    (12, 16, 17, 24),
    (18, 19, 20, 25),
    (18, 20, 21, 25),
    (18, 21, 22, 25),
    (18, 22, 23, 25),
    (3, 4, 5, 9, 24),
    (0, 1, 2, 3, 4, 6),
    (1, 2, 3, 4, 6, 7),
    (2, 3, 4, 6, 7, 8),
    (3, 4, 6, 7, 8, 9),
    (3, 6, 7, 8, 9, 10),
    (4, 6, 7, 8, 9, 11),
)

TREE_EDGES = (
    (0, 14), (0, 18), (1, 2), (1, 4), (1, 14), (2, 5),
    (3, 4), (3, 9), (5, 13), (6, 7), (7, 8), (8, 9),
    (10, 11), (11, 12), (12, 13), (15, 16), (16, 17),
    (17, 18), (18, 19), (18, 20),
)


def connected(vertices: set[int], edges: set[tuple[int, int]]) -> bool:
    if not vertices:
        return False
    reached = {next(iter(vertices))}
    while True:
        old = set(reached)
        for left, right in edges:
            if left in reached and right in vertices:
                reached.add(right)
            if right in reached and left in vertices:
                reached.add(left)
        if reached == old:
            return reached == vertices


def verify_tree_decomposition(edges: set[tuple[int, int]]) -> None:
    tree_vertices = set(range(len(BAGS)))
    tree_edges = {edge(*pair) for pair in TREE_EDGES}
    assert len(tree_edges) == len(BAGS) - 1
    assert connected(tree_vertices, tree_edges)
    assert max(map(len, BAGS)) == 6
    assert set().union(*map(set, BAGS)) == set(range(26))

    for graph_edge in edges:
        assert any(set(graph_edge) <= set(bag) for bag in BAGS)

    for vertex in range(26):
        containing = {index for index, bag in enumerate(BAGS) if vertex in bag}
        induced = {
            pair for pair in tree_edges if pair[0] in containing and pair[1] in containing
        }
        assert connected(containing, induced)


def verify_connectivity_three(edges: set[tuple[int, int]]) -> None:
    vertices = set(range(26))
    for size in range(3):
        for deleted in itertools.combinations(vertices, size):
            remaining = vertices - set(deleted)
            remaining_edges = {
                pair for pair in edges if pair[0] in remaining and pair[1] in remaining
            }
            assert connected(remaining, remaining_edges)
    deleted = {A3, X, R}
    remaining = vertices - deleted
    remaining_edges = {
        pair for pair in edges if pair[0] in remaining and pair[1] in remaining
    }
    assert not connected(remaining, remaining_edges)


def main() -> None:
    edges = graph_edges()
    sigma = set(range(24))
    assert set(range(26)) - sigma == {C, D}
    assert edge(C, D) not in edges

    c_neighbours = {other for pair in edges if C in pair for other in pair if other != C}
    d_neighbours = {other for pair in edges if D in pair for other in pair if other != D}
    assert c_neighbours == {A3, X, *MIDS[:6]}
    assert d_neighbours == {Y, R, *MIDS[6:]}
    assert len(c_neighbours) == len(d_neighbours) == 8

    verify_tree_decomposition(edges)
    verify_connectivity_three(edges)
    print("vertices", 26)
    print("edges", len(edges))
    print("component_attachment_counts", len(c_neighbours), len(d_neighbours))
    print("treewidth_upper_bound", 5)
    print("vertex_connectivity", 3)
    print("GREEN: nested-interval attachment-count barrier verified")


if __name__ == "__main__":
    main()
