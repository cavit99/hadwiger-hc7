#!/usr/bin/env python3
"""Describe the boundary residues after the two uniform `(1,2)` closures.

This is a diagnostic, not a realizability assertion.  It retains a
K4-free seven-vertex boundary H only when

* no independent block is robustly reflectable by two full packets; and
* no deletion of two boundary anchors leaves a K4 minor.

For the smallest hard core it also checks whether *any* equality state
forced by one independent block has packet demand at most two.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations

import networkx as nx


S = tuple(range(7))


def omega(graph: nx.Graph) -> int:
    if not graph:
        return 0
    return max(map(len, nx.find_cliques(graph)))


def independent(graph: nx.Graph, vertices: frozenset[int]) -> bool:
    return graph.subgraph(vertices).number_of_edges() == 0


def robust_block(graph: nx.Graph) -> frozenset[int] | None:
    """Return an independent block whose every exact state has demand <=2."""

    for size in range(3, 8):
        for choice in combinations(S, size):
            block = frozenset(choice)
            if not independent(graph, block):
                continue
            remainder = frozenset(S) - block
            if size >= 5:
                return block
            if size == 4 and graph.subgraph(remainder).number_of_edges() > 0:
                return block
            if size == 3 and omega(graph.subgraph(remainder)) >= 3:
                return block
    return None


def has_k4_minor_on_at_most_five(graph: nx.Graph) -> bool:
    """Test K4-minor containment when graph has at most five vertices."""

    if omega(graph) >= 4:
        return True
    for edge in graph.edges():
        contracted = nx.contracted_edge(graph, edge, self_loops=False)
        if omega(contracted) >= 4:
            return True
    return False


def two_anchor_lift(graph: nx.Graph) -> tuple[int, int] | None:
    for x, y in combinations(S, 2):
        if has_k4_minor_on_at_most_five(graph.subgraph(set(S) - {x, y}).copy()):
            return x, y
    return None


def set_partitions(vertices: tuple[int, ...]):
    if not vertices:
        yield ()
        return
    first, *rest = vertices
    for partition in set_partitions(tuple(rest)):
        yield (frozenset({first}),) + partition
        for index in range(len(partition)):
            enlarged = list(partition)
            enlarged[index] |= {first}
            yield tuple(enlarged)


PARTITIONS = tuple(p for p in set_partitions(S) if len(p) <= 6)


def demand(graph: nx.Graph, partition: tuple[frozenset[int], ...]) -> int:
    singletons = frozenset(
        next(iter(block)) for block in partition if len(block) == 1
    )
    return len(partition) - omega(graph.subgraph(singletons))


def has_any_safe_state(graph: nx.Graph) -> bool:
    for partition in PARTITIONS:
        if not all(independent(graph, block) for block in partition):
            continue
        if demand(graph, partition) > 2:
            continue
        if any(len(block) >= 2 for block in partition):
            return True
    return False


def disjoint_triangles(graph: nx.Graph) -> bool:
    triangles = [
        frozenset(choice)
        for choice in combinations(S, 3)
        if omega(graph.subgraph(choice)) == 3
    ]
    return any(first.isdisjoint(second) for first, second in combinations(triangles, 2))


def code(graph: nx.Graph) -> str:
    return nx.to_graph6_bytes(graph, header=False).decode().strip()


def main() -> None:
    graphs = [
        graph
        for graph in nx.graph_atlas_g()
        if len(graph) == 7 and omega(graph) <= 3
    ]
    residues = [
        graph
        for graph in graphs
        if robust_block(graph) is None and two_anchor_lift(graph) is None
    ]

    hard = [graph for graph in residues if not has_any_safe_state(graph)]
    profile = Counter(
        (
            omega(nx.complement(graph)),
            graph.number_of_edges(),
            nx.number_connected_components(graph),
            disjoint_triangles(graph),
        )
        for graph in residues
    )

    print("ADAPTIVE (1,2) RESIDUE PROBE")
    print(f"k4_free_boundaries={len(graphs)}")
    print(f"residues_after_robust_and_two_anchor={len(residues)}")
    print(f"residues_with_no_safe_state={len(hard)}")
    print("residue_profile=(alpha,edges,components,two_disjoint_triangles):")
    for key, count in sorted(profile.items()):
        print(f"  {key}: {count}")

    print("no_safe_state_residues:")
    for graph in sorted(hard, key=lambda item: (item.number_of_edges(), code(item))):
        triangles = sum(
            1
            for choice in combinations(S, 3)
            if omega(graph.subgraph(choice)) == 3
        )
        print(
            "  "
            f"g6={code(graph)} edges={sorted(graph.edges())} "
            f"degrees={sorted(dict(graph.degree()).values())} "
            f"alpha={omega(nx.complement(graph))} triangles={triangles} "
            f"disjoint_triangles={disjoint_triangles(graph)} "
            f"planar={nx.check_planarity(graph)[0]}"
        )


if __name__ == "__main__":
    main()
