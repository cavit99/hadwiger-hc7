#!/usr/bin/env python3
"""Finite audit for the warehouse deficiency lemmas and icosahedral data."""

from __future__ import annotations

import itertools

import networkx as nx


def has_clique_pairing(m: int, missing: frozenset[tuple[int, int]]) -> bool:
    for permutation in itertools.permutations(range(m)):
        if any((i, permutation[i]) in missing for i in range(m)):
            continue
        if all(
            not (
                (i, permutation[j]) in missing
                and (j, permutation[i]) in missing
            )
            for i in range(m)
            for j in range(i + 1, m)
        ):
            return True
    return False


def equality_type(m: int, missing: frozenset[tuple[int, int]]) -> bool:
    row_degrees = [sum((i, j) in missing for j in range(m)) for i in range(m)]
    column_degrees = [
        sum((i, j) in missing for i in range(m)) for j in range(m)
    ]
    row_star = all(d == 1 for d in column_degrees) and sum(
        d > 0 for d in row_degrees
    ) <= 2
    column_star = all(d == 1 for d in row_degrees) and sum(
        d > 0 for d in column_degrees
    ) <= 2
    return row_star or column_star


def verify_square_lemmas() -> None:
    for m in range(1, 6):
        pairs = tuple(itertools.product(range(m), repeat=2))
        for q in range(m + 1):
            for defect_tuple in itertools.combinations(pairs, q):
                missing = frozenset(defect_tuple)
                good = has_clique_pairing(m, missing)
                if q < m:
                    assert good
                elif not good:
                    assert equality_type(m, missing)
        print(f"square order {m}: all deficiencies through equality verified")


def verify_icosahedron() -> None:
    graph = nx.icosahedral_graph()
    carrier = set(graph.neighbors(0))
    assert carrier == {1, 5, 7, 8, 11}
    expected = {
        0: {1, 5, 7, 8, 11},
        2: {1, 8},
        4: {5, 11},
        6: {1, 5},
        9: {7, 8},
        10: {7, 11},
    }
    for target, profile in expected.items():
        assert carrier & set(graph.neighbors(target)) == profile

    joined = graph.copy()
    joined.add_edge("u", "v")
    for apex in ("u", "v"):
        for vertex in graph:
            joined.add_edge(apex, vertex)
    assert nx.node_connectivity(joined) == 7
    assert nx.check_planarity(graph)[0]

    # An explicit K4 model in the icosahedron.
    bags = ({0}, {1}, {5}, {2, 6, 8})
    for bag in bags:
        assert nx.is_connected(graph.subgraph(bag))
    for i, left in enumerate(bags):
        for right in bags[i + 1 :]:
            assert any(graph.has_edge(x, y) for x in left for y in right)
    print("icosahedral profiles, connectivity, planarity, and K4 model verified")


if __name__ == "__main__":
    verify_square_lemmas()
    verify_icosahedron()
