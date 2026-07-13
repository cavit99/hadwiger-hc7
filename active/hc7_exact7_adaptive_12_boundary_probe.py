#!/usr/bin/env python3
"""Finite boundary probe for adaptive exact-seven packet vector (1,2).

This script studies only the boundary combinatorics.  It does *not* assert
that every enumerated equality partition is realizable by a shore minor.

For each unlabeled K4-free graph H on seven vertices and every nonempty
independent set I, it enumerates proper equality partitions Pi of V(H)
having I as an exact block and at most six blocks, and computes

    d_H(Pi) = |Pi| - omega(H[sing(Pi)]).

The compact report is intended to falsify overly strong choices of I and
to identify the residual demand-three patterns.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations

import networkx as nx


VERTICES = tuple(range(7))


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


PARTITIONS = tuple(
    partition
    for partition in set_partitions(VERTICES)
    if len(partition) <= 6
)


def independent(graph: nx.Graph, vertices: frozenset[int]) -> bool:
    return graph.subgraph(vertices).number_of_edges() == 0


def clique_number(graph: nx.Graph, vertices: frozenset[int]) -> int:
    if not vertices:
        return 0
    return max(map(len, nx.find_cliques(graph.subgraph(vertices))))


def omega(graph: nx.Graph) -> int:
    if len(graph) == 0:
        return 0
    return max(map(len, nx.find_cliques(graph)))


def demand(graph: nx.Graph, partition: tuple[frozenset[int], ...]) -> int:
    singletons = frozenset(
        next(iter(block)) for block in partition if len(block) == 1
    )
    return len(partition) - clique_number(graph, singletons)


def graph_code(graph: nx.Graph) -> str:
    return ",".join(f"{u}{v}" for u, v in sorted(graph.edges())) or "empty"


def main() -> None:
    graphs = [
        graph
        for graph in nx.graph_atlas_g()
        if len(graph) == 7 and omega(graph) <= 3
    ]

    robust_safe = []
    robust_bad = []
    mixed = []
    maximum_set_profiles = Counter()
    graph_best_worst = Counter()
    independent_set_ranges = Counter()
    witnesses = {}
    no_safe_choice_graphs = []

    for graph_index, graph in enumerate(graphs):
        valid_partitions = [
            partition
            for partition in PARTITIONS
            if all(independent(graph, block) for block in partition)
        ]
        alpha = omega(nx.complement(graph))
        choices = []
        for size in range(1, alpha + 1):
            for choice in combinations(VERTICES, size):
                block = frozenset(choice)
                if not independent(graph, block):
                    continue
                values = [
                    (demand(graph, partition), partition)
                    for partition in valid_partitions
                    if block in partition
                ]
                assert values
                minimum = min(value for value, _ in values)
                maximum = max(value for value, _ in values)
                choices.append((block, minimum, maximum))
                independent_set_ranges[(len(block), minimum, maximum)] += 1
                key = (graph_index, tuple(sorted(block)))
                witnesses[key] = {
                    "min": next(p for d, p in values if d == minimum),
                    "max": next(p for d, p in values if d == maximum),
                }
                if maximum <= 2:
                    robust_safe.append((graph_index, block, minimum, maximum))
                elif minimum >= 3:
                    robust_bad.append((graph_index, block, minimum, maximum))
                else:
                    mixed.append((graph_index, block, minimum, maximum))

        maximum_choices = [entry for entry in choices if len(entry[0]) == alpha]
        signature = tuple(sorted((minimum, maximum) for _, minimum, maximum in maximum_choices))
        maximum_set_profiles[(alpha, signature)] += 1
        best_worst = min(maximum for _, _, maximum in choices)
        best_minimum = min(minimum for _, minimum, _ in choices)
        graph_best_worst[(alpha, best_worst, best_minimum)] += 1
        if best_minimum >= 3:
            no_safe_choice_graphs.append((graph_index, graph))

    print("BOUNDARY-ONLY PROBE")
    print(f"k4_free_unlabeled_graphs={len(graphs)}")
    print(f"partitions_at_most_six={len(PARTITIONS)}")
    print(f"independent_set_pairs={len(robust_safe)+len(robust_bad)+len(mixed)}")
    print(f"robust_safe_I_max_demand_le_2={len(robust_safe)}")
    print(f"robust_bad_I_min_demand_ge_3={len(robust_bad)}")
    print(f"mixed_I={len(mixed)}")
    print("graph_best_worst_by_alpha:")
    for key, count in sorted(graph_best_worst.items()):
        print(f"  {key}: {count}")
    print("independent_set_demand_ranges:")
    for key, count in sorted(independent_set_ranges.items()):
        print(f"  {key}: {count}")
    print(f"graphs_with_no_boundary_safe_I={len(no_safe_choice_graphs)}")
    if no_safe_choice_graphs:
        graph_index, graph = min(
            no_safe_choice_graphs,
            key=lambda item: (item[1].number_of_edges(), item[0]),
        )
        print("smallest_no_safe_choice_graph:")
        print(f"  graph_index={graph_index} edges={graph_code(graph)}")
        print(
            "  alpha="
            f"{omega(nx.complement(graph))} edge_count={graph.number_of_edges()}"
        )

    # Print one smallest-edge witness for each coarse class.
    for label, family in (
        ("robust_safe", robust_safe),
        ("robust_bad", robust_bad),
        ("mixed", mixed),
    ):
        if not family:
            continue
        graph_index, block, minimum, maximum = min(
            family,
            key=lambda item: (graphs[item[0]].number_of_edges(), len(item[1]), item[0]),
        )
        graph = graphs[graph_index]
        key = (graph_index, tuple(sorted(block)))
        print(f"{label}_example:")
        print(f"  graph_index={graph_index} edges={graph_code(graph)}")
        print(f"  I={sorted(block)} alpha={omega(nx.complement(graph))}")
        print(f"  demand_range=({minimum},{maximum})")
        print(f"  min_partition={witnesses[key]['min']}")
        print(f"  max_partition={witnesses[key]['max']}")


if __name__ == "__main__":
    main()
