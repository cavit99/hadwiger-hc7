#!/usr/bin/env python3
"""Probe the literal three-packet quotient in the adaptive `(1,2)` cell.

The quotient has the seven literal boundary vertices and three independent
vertices, one for each available full packet.  Every packet vertex is
adjacent to every boundary vertex.  A K7 model in this quotient lifts
literally to the original graph.

This is a falsification/classification aid, not a theorem by itself.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations

import networkx as nx

from hc7_exact7_adaptive_12_boundary_probe import (
    PARTITIONS,
    demand,
    independent,
    omega,
)
def has_clique_minor(graph: nx.Graph, order: int) -> bool:
    vertices = tuple(graph)
    connected = []
    for mask in range(1, 1 << len(vertices)):
        subset = [vertices[index] for index in range(len(vertices)) if mask >> index & 1]
        if nx.is_connected(graph.subgraph(subset)):
            connected.append(frozenset(subset))

    def search(chosen: tuple[frozenset[int], ...], used: frozenset[int]) -> bool:
        if len(chosen) == order:
            return True
        for branch in connected:
            if branch & used:
                continue
            if all(
                any(graph.has_edge(x, y) for x in branch for y in old)
                for old in chosen
            ) and search(chosen + (branch,), used | branch):
                return True
        return False

    return search((), frozenset())


def certified_packet_k7(graph: nx.Graph) -> bool:
    """Two anchors plus three packets and a K4 model on the remainder."""
    for x in range(7):
        for y in range(x + 1, 7):
            remainder = graph.subgraph(set(range(7)) - {x, y})
            if has_clique_minor(remainder, 4):
                return True
    return False


def certified_connected_rich_k7(graph: nx.Graph) -> bool:
    """One anchor, adjacent rich packets, and a K4 model after deletion."""
    for x in range(7):
        remainder = graph.subgraph(set(range(7)) - {x})
        if has_clique_minor(remainder, 4):
            return True
    return False


def robust_independent_block(graph: nx.Graph) -> frozenset[int] | None:
    for size in range(3, 8):
        for choice in combinations(range(7), size):
            block = frozenset(choice)
            if not independent(graph, block):
                continue
            complement = set(range(7)) - block
            if size >= 5:
                return block
            if size == 4 and graph.subgraph(complement).number_of_edges() >= 1:
                return block
            if size == 3 and omega(graph.subgraph(complement)) >= 3:
                return block
    return None


def has_disjoint_triangles(graph: nx.Graph) -> bool:
    triangles = [
        frozenset(choice)
        for choice in combinations(range(7), 3)
        if graph.subgraph(choice).number_of_edges() == 3
    ]
    return any(not (left & right) for left in triangles for right in triangles)


def main() -> None:
    graphs = [
        graph
        for graph in nx.graph_atlas_g()
        if len(graph) == 7 and omega(graph) <= 3
    ]
    census: Counter[tuple[int, bool]] = Counter()
    survivors = []
    structural_failures = []
    combined_residual = []
    robust_count = 0
    quotient_count = 0
    overlap_count = 0
    residual_minimum_demand: Counter[int] = Counter()
    connected_rich_extra = 0
    connected_rich_residual: Counter[tuple[int, int]] = Counter()
    for index, graph in enumerate(graphs):
        valid = [
            partition
            for partition in PARTITIONS
            if all(independent(graph, block) for block in partition)
            and any(len(block) >= 2 for block in partition)
        ]
        minimum_demand = min(demand(graph, partition) for partition in valid)
        model = certified_packet_k7(graph)
        robust = robust_independent_block(graph) is not None
        robust_count += int(robust)
        quotient_count += int(model)
        overlap_count += int(robust and model)
        census[(minimum_demand, model)] += 1
        if minimum_demand >= 3 and not model:
            survivors.append(
                (
                    index,
                    graph.number_of_edges(),
                    omega(nx.complement(graph)),
                    min(len(partition) for partition in valid),
                    tuple(sorted(graph.edges())),
                )
            )
        if not robust and not model:
            combined_residual.append((index, tuple(sorted(graph.edges()))))
            residual_minimum_demand[minimum_demand] += 1
            one_anchor = certified_connected_rich_k7(graph)
            connected_rich_extra += int(one_anchor)
            if not one_anchor:
                connected_rich_residual[(omega(nx.complement(graph)), minimum_demand)] += 1
            if not has_disjoint_triangles(graph):
                structural_failures.append((index, tuple(sorted(graph.edges()))))

    print("THREE-PACKET QUOTIENT PROBE")
    print(f"graphs={len(graphs)}")
    for key, count in sorted(census.items()):
        print(f"minimum_demand={key[0]} quotient_k7={key[1]} count={count}")
    print(f"demand_ge_3_without_quotient_k7={len(survivors)}")
    print(f"robust_independent_block={robust_count}")
    print(f"two_anchor_k4_lift={quotient_count}")
    print(f"overlap={overlap_count}")
    print(
        "no_robust_I_no_packet_k7="
        f"{len(combined_residual)}"
    )
    print(
        "of_these_without_disjoint_triangles="
        f"{len(structural_failures)}"
    )
    print(f"combined_residual_by_minimum_demand={dict(residual_minimum_demand)}")
    print(f"connected_rich_one_anchor_extra={connected_rich_extra}")
    print(f"connected_rich_residual_by_alpha_demand={dict(connected_rich_residual)}")
    for survivor in survivors:
        index, edges, alpha, chromatic_number, edge_set = survivor
        print(
            f"index={index} edges={edges} alpha={alpha} "
            f"chromatic_number={chromatic_number} edge_set={edge_set}"
        )


if __name__ == "__main__":
    main()
