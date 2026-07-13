#!/usr/bin/env python3
"""Verify the coloured two-cycle crossing and rooted-model facts."""

from __future__ import annotations

from itertools import combinations, product

import networkx as nx


CYCLE_C = (0, 1, 2, 3, 4, 5, 6)
CYCLE_D = (0, 1, 4, 6, 5, 2, 3)
COLOUR = dict(zip(range(7), "AABBCCD", strict=True))


def cycle_edges(order: tuple[int, ...]) -> list[tuple[int, int]]:
    return [(order[i], order[(i + 1) % len(order)]) for i in range(len(order))]


def alternates(first: tuple[int, int], second: tuple[int, int]) -> bool:
    if set(first) & set(second):
        return False
    position = {vertex: i for i, vertex in enumerate(CYCLE_C)}
    a, b = sorted((position[first[0]], position[first[1]]))
    c, d = position[second[0]], position[second[1]]
    return (a < c < b) != (a < d < b)


def rooted_k4(graph: nx.Graph, roots: tuple[int, ...]) -> bool:
    root_set = set(roots)
    free = tuple(set(graph) - root_set)
    candidates: dict[int, list[set[int]]] = {}
    for root in roots:
        values = []
        for choice in range(1 << len(free)):
            bag = {root} | {
                free[i] for i in range(len(free)) if choice >> i & 1
            }
            if nx.is_connected(graph.subgraph(bag)):
                values.append(bag)
        candidates[root] = values

    def search(position: int, chosen: list[set[int]]) -> bool:
        if position == 4:
            return True
        root = roots[position]
        for bag in candidates[root]:
            if any(bag & old for old in chosen):
                continue
            if not all(
                any(graph.has_edge(u, v) for u in bag for v in old)
                for old in chosen
            ):
                continue
            if search(position + 1, [*chosen, bag]):
                return True
        return False

    return search(0, [])


def main() -> None:
    d_edges = cycle_edges(CYCLE_D)
    crossing = [
        (first, second)
        for first, second in combinations(d_edges, 2)
        if alternates(first, second)
    ]
    expected = [
        ((1, 4), (5, 2)),
        ((1, 4), (3, 0)),
        ((4, 6), (5, 2)),
        ((5, 2), (3, 0)),
    ]
    assert crossing == expected
    assert all(
        len({COLOUR[v] for edge in pair for v in edge}) < 4
        for pair in crossing
    )

    graph = nx.Graph()
    graph.add_edges_from(cycle_edges(CYCLE_C))
    graph.add_edges_from(cycle_edges(CYCLE_D))
    transversals = list(product((0, 1), (2, 3), (4, 5), (6,)))
    rootability = {roots: rooted_k4(graph, roots) for roots in transversals}
    assert [roots for roots, value in rootability.items() if not value] == [
        (0, 2, 5, 6)
    ]

    print("GREEN: coloured two-cycle barrier verified")
    print("crossing D-edge pairs:", crossing)
    print("unique nonrootable rainbow transversal: (0,2,5,6)")


if __name__ == "__main__":
    main()
