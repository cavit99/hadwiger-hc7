"""Independent replay of the explicit strict-surplus packet circuits."""

from __future__ import annotations

from itertools import combinations

import networkx as nx

from atomic_three_packet_actual_gate_search import CIRCUITS


DEMANDS = ((0, 1), (2, 3), (4, 5))


def carriers(graph: nx.Graph, rows, demand):
    left, right = demand
    left_portals = {vertex for vertex, row in enumerate(rows) if left in row}
    right_portals = {vertex for vertex, row in enumerate(rows) if right in row}
    answer = []
    for size in range(1, len(rows) + 1):
        for raw in combinations(range(len(rows)), size):
            bag = set(raw)
            if bag & left_portals and bag & right_portals and nx.is_connected(graph.subgraph(bag)):
                answer.append(bag)
    return answer


def verify_circuit(order: int) -> None:
    edges, rows = CIRCUITS[order]
    graph = nx.Graph()
    graph.add_nodes_from(range(order))
    graph.add_edges_from(edges)

    for size in range(1, order):
        for raw in combinations(range(order), size):
            subset = set(raw)
            internal = set().union(*(set(graph.neighbors(vertex)) for vertex in subset)) - subset
            boundary = set().union(*(set(rows[vertex]) for vertex in subset))
            assert len(internal) + len(boundary) >= 8

    families = [carriers(graph, rows, demand) for demand in DEMANDS]
    assert all(
        any(left.isdisjoint(right) for left in families[i] for right in families[j])
        for i, j in combinations(range(3), 2)
    )
    assert not any(
        first.isdisjoint(second)
        and first.isdisjoint(third)
        and second.isdisjoint(third)
        for first in families[0]
        for second in families[1]
        for third in families[2]
    )


def main() -> None:
    for order in CIRCUITS:
        verify_circuit(order)
    print("strict-surplus packet circuits verified", tuple(CIRCUITS))


if __name__ == "__main__":
    main()
