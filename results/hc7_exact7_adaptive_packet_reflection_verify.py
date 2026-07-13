#!/usr/bin/env python3
"""Exhaustively verify the seven-vertex demand bound in Lemma 5.1.

Run from the repository root with

  PYTHONPATH=active/runtime/deps python3 \
      results/hc7_exact7_adaptive_packet_reflection_verify.py
"""

from __future__ import annotations

from itertools import combinations

import networkx as nx


def set_partitions(vertices: tuple[int, ...]):
    if not vertices:
        yield ()
        return
    first, *rest = vertices
    for partition in set_partitions(tuple(rest)):
        yield (frozenset({first}),) + partition
        for index in range(len(partition)):
            enlarged = list(partition)
            enlarged[index] = enlarged[index] | {first}
            yield tuple(enlarged)


PARTITIONS = tuple(set_partitions(tuple(range(7))))
assert len(PARTITIONS) == 877


def independent(graph: nx.Graph, vertices: frozenset[int]) -> bool:
    return graph.subgraph(vertices).number_of_edges() == 0


def clique_number(graph: nx.Graph, vertices: frozenset[int]) -> int:
    if not vertices:
        return 0
    return max(map(len, nx.find_cliques(graph.subgraph(vertices))))


def main() -> None:
    graphs = [
        graph
        for graph in nx.graph_atlas_g()
        if len(graph) == 7 and not any(nx.triangles(graph).values())
    ]
    assert len(graphs) == 107

    independent_sets_checked = 0
    returned_partitions_checked = 0
    maximum_three_graphs = 0
    at_least_four_graphs = 0

    for graph in graphs:
        alpha = max(map(len, nx.find_cliques(nx.complement(graph))))
        if alpha >= 4:
            size = 4
            at_least_four_graphs += 1
        else:
            assert alpha == 3
            size = 3
            maximum_three_graphs += 1

        for choice in combinations(range(7), size):
            block = frozenset(choice)
            if not independent(graph, block):
                continue
            independent_sets_checked += 1
            for partition in PARTITIONS:
                if block not in partition:
                    continue
                if not all(independent(graph, part) for part in partition):
                    continue
                returned_partitions_checked += 1
                singletons = frozenset(
                    next(iter(part)) for part in partition if len(part) == 1
                )
                demand = len(partition) - clique_number(graph, singletons)
                assert demand <= 3, (graph.edges(), block, partition, demand)

    print("VERIFIED")
    print(f"triangle_free_graphs={len(graphs)}")
    print(f"alpha_exactly_three_graphs={maximum_three_graphs}")
    print(f"alpha_at_least_four_graphs={at_least_four_graphs}")
    print(f"independent_sets_checked={independent_sets_checked}")
    print(f"returned_partitions_checked={returned_partitions_checked}")
    print("maximum_packet_demand=3")


if __name__ == "__main__":
    main()
