"""Search for a strict-surplus pairwise-but-not-triple packet shore.

This is a falsification probe for proposed portal-exchange lemmas.  The
internal graph is the eight-vertex clean-web example from
``hadwiger_uniform_three_demand_exchange.md``.  Boundary rows are varied;
the three demands are 04, 12, 35 and label 6 is the unused singleton.
"""

from __future__ import annotations

import random

import networkx as nx


EDGES = {
    (0, 1), (0, 2), (0, 5), (0, 6), (1, 3), (1, 6), (1, 7),
    (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 7), (4, 5),
    (4, 6), (5, 6), (5, 7), (6, 7),
}
DEMANDS = ((0, 4), (1, 2), (3, 5))


def connected_masks(graph: nx.Graph) -> list[bool]:
    n = graph.number_of_nodes()
    answer = [False] * (1 << n)
    for mask in range(1, 1 << n):
        vertices = [v for v in range(n) if mask & (1 << v)]
        answer[mask] = nx.is_connected(graph.subgraph(vertices))
    return answer


def packet_status(
    rows: tuple[int, ...], connected: list[bool]
) -> tuple[tuple[bool, bool, bool], bool]:
    n = len(rows)
    carriers: list[list[int]] = []
    for left, right in DEMANDS:
        left_portals = sum(1 << v for v in range(n) if rows[v] & (1 << left))
        right_portals = sum(1 << v for v in range(n) if rows[v] & (1 << right))
        carriers.append([
            mask
            for mask in range(1, 1 << n)
            if connected[mask] and mask & left_portals and mask & right_portals
        ])

    pairwise = []
    for i, j in ((0, 1), (0, 2), (1, 2)):
        pairwise.append(any(not (x & y) for x in carriers[i] for y in carriers[j]))

    triple = any(
        not (x & y) and not (x & z) and not (y & z)
        for x in carriers[0]
        for y in carriers[1]
        for z in carriers[2]
    )
    return tuple(pairwise), triple


def boundary_sizes(graph: nx.Graph) -> list[int]:
    n = graph.number_of_nodes()
    all_vertices = (1 << n) - 1
    result = [0] * (1 << n)
    for mask in range(1, all_vertices):
        boundary = set()
        for vertex in range(n):
            if mask & (1 << vertex):
                boundary.update(graph.neighbors(vertex))
        boundary.difference_update(v for v in range(n) if mask & (1 << v))
        result[mask] = len(boundary)
    return result


def strict_surplus(rows: tuple[int, ...], internal_boundary: list[int]) -> bool:
    all_vertices = (1 << len(rows)) - 1
    row_union = [0] * (1 << len(rows))
    for mask in range(1, all_vertices):
        bit = mask & -mask
        vertex = bit.bit_length() - 1
        row_union[mask] = row_union[mask ^ bit] | rows[vertex]
        if internal_boundary[mask] + row_union[mask].bit_count() < 8:
            return False
    return True


def main() -> None:
    graph = nx.Graph()
    graph.add_nodes_from(range(8))
    graph.add_edges_from(EDGES)
    connected = connected_masks(graph)
    internal_boundary = boundary_sizes(graph)
    minimum_rows = [max(1, 8 - graph.degree(vertex)) for vertex in graph]
    choices = [
        [
            row
            for row in range(1, 1 << 7)
            if minimum_rows[vertex] <= row.bit_count() <= min(7, minimum_rows[vertex] + 1)
        ]
        for vertex in graph
    ]

    print("internal degrees", dict(graph.degree()))
    print("minimum row sizes", minimum_rows)
    random.seed(20260712)
    for iteration in range(100_000):
        rows = tuple(random.choice(choices[vertex]) for vertex in graph)
        if len(set().union(*(set(i for i in range(7) if row & (1 << i)) for row in rows))) < 7:
            continue
        if not strict_surplus(rows, internal_boundary):
            continue
        pairs, triple = packet_status(rows, connected)
        if all(pairs) and not triple:
            print("strict-surplus counterexample", iteration)
            print([[i for i in range(7) if row & (1 << i)] for row in rows])
            return
    print("no witness in random sample")


if __name__ == "__main__":
    main()
