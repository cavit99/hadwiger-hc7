#!/usr/bin/env python3
"""Exact falsification probe for the double-triangle four-carrier quotient.

The quotient contains the seven literal boundary vertices, two rich full
packets, and two adjacent near-full thin carriers X,Y.  X misses a and Y
misses b.  The exact minor solver explores at most four deletions or edge
contractions, so it is complete on these eleven-vertex hosts.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations

import networkx as nx

from hc7_exact7_adaptive_12_residue_probe import (
    S,
    has_any_safe_state,
    omega,
    robust_block,
    two_anchor_lift,
)


def has_edge_between(graph: nx.Graph, left: int, right: int) -> bool:
    return any(
        graph.has_edge(u, v)
        for u in range(len(graph))
        if left >> u & 1
        for v in range(len(graph))
        if right >> v & 1
    )


def has_k7_minor(graph: nx.Graph) -> bool:
    vertices = tuple(graph)
    assert vertices == tuple(range(len(vertices)))
    order = len(vertices)

    @lru_cache(maxsize=None)
    def search(branches: tuple[int, ...]) -> bool:
        size = len(branches)
        adjacency = [
            [False] * size for _ in range(size)
        ]
        for i, j in combinations(range(size), 2):
            adjacency[i][j] = adjacency[j][i] = has_edge_between(
                graph, branches[i], branches[j]
            )

        if size >= 7:
            for choice in combinations(range(size), 7):
                if all(adjacency[i][j] for i, j in combinations(choice, 2)):
                    return True
        if size == 7:
            return False

        next_states = set()
        # Delete one current bag.
        for index in range(size):
            next_states.add(branches[:index] + branches[index + 1 :])
        # Contract one quotient edge.
        for i, j in combinations(range(size), 2):
            if not adjacency[i][j]:
                continue
            merged = branches[i] | branches[j]
            next_branches = [
                branches[k] for k in range(size) if k not in (i, j)
            ]
            next_branches.append(merged)
            next_states.add(tuple(sorted(next_branches)))

        return any(search(state) for state in next_states)

    return search(tuple(1 << vertex for vertex in range(order)))


def hard_boundaries():
    return [
        graph
        for graph in nx.graph_atlas_g()
        if len(graph) == 7
        and omega(graph) <= 3
        and robust_block(graph) is None
        and two_anchor_lift(graph) is None
        and not has_any_safe_state(graph)
    ]


def triangle_pairs(graph: nx.Graph):
    triangles = [
        frozenset(choice)
        for choice in combinations(S, 3)
        if omega(graph.subgraph(choice)) == 3
    ]
    for left, right in combinations(triangles, 2):
        if left.isdisjoint(right):
            yield left, right


def pure_in_triangle(graph: nx.Graph, vertex: int, triangle: frozenset[int]) -> bool:
    return not any(
        graph.has_edge(vertex, other)
        for other in frozenset(S) - triangle
    )


def four_carrier_host(
    boundary: nx.Graph,
    missed_by_x: int,
    missed_by_y: int,
    rich_packets_adjacent: bool,
) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(range(11))
    graph.add_edges_from(boundary.edges())
    p1, p2, x, y = 7, 8, 9, 10
    graph.add_edges_from((p, s) for p in (p1, p2) for s in S)
    graph.add_edges_from((x, s) for s in S if s != missed_by_x)
    graph.add_edges_from((y, s) for s in S if s != missed_by_y)
    graph.add_edge(x, y)
    if rich_packets_adjacent:
        graph.add_edge(p1, p2)
    return graph


def main() -> None:
    boundaries = hard_boundaries()
    assert len(boundaries) == 10
    tested = set()
    counterexamples = []
    for index, boundary in enumerate(boundaries):
        for left, right in triangle_pairs(boundary):
            for a in left:
                if not pure_in_triangle(boundary, a, left):
                    continue
                for b in right:
                    if not pure_in_triangle(boundary, b, right):
                        continue
                    key = (
                        nx.to_graph6_bytes(boundary, header=False),
                        a,
                        b,
                    )
                    if key in tested:
                        continue
                    tested.add(key)
                    for adjacent in (False, True):
                        host = four_carrier_host(boundary, a, b, adjacent)
                        result = has_k7_minor(host)
                        print(
                            f"boundary={index} a={a} b={b} "
                            f"rich_adjacent={adjacent} K7={result}"
                        )
                        if not result:
                            counterexamples.append((index, a, b, adjacent))

    print(f"tested_hosts={2*len(tested)}")
    print(f"counterexamples={len(counterexamples)}")
    print(counterexamples)
    assert len(tested) == 28
    assert len(counterexamples) == 38

    # The first hard boundary is 2K3+K1.  Its crossed-pure quotient remains
    # K7-minor-free even after adding the rich-packet edge.
    first = boundaries[0]
    assert first.number_of_edges() == 6
    explicit = four_carrier_host(first, 0, 2, True)
    assert not has_k7_minor(explicit)
    print("VERIFIED")


if __name__ == "__main__":
    main()
