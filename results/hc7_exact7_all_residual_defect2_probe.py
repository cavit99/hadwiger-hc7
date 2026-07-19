#!/usr/bin/env python3
"""Probe two full boundary carriers plus one defect-two carrier on all 129 residues.

This is boundary algebra only.  For each residual seven-vertex boundary and
each defect set of order at most two, choose one non-singleton maximal
independent boundary block before the proper-minor colouring is returned.
Every exact returned partition containing that block must either have packet
demand at most two, or have demand three with one block assignable to the
partial carrier.
"""

from __future__ import annotations

from itertools import combinations

import networkx as nx

from hc7_exact7_adaptive_12_boundary_verify import (
    PARTITIONS,
    S,
    demand,
    independent,
    omega,
)
from hc7_exact7_adaptive_12_residue_probe import robust_block, two_anchor_lift


def residual_boundaries() -> list[nx.Graph]:
    return [
        graph
        for graph in nx.graph_atlas_g()
        if len(graph) == 7
        and omega(graph) <= 3
        and robust_block(graph) is None
        and two_anchor_lift(graph) is None
    ]


def exact_states(graph: nx.Graph, block: frozenset[int]):
    return [
        partition
        for partition in PARTITIONS
        if block in partition
        and all(independent(graph, part) for part in partition)
    ]


def maximal_independent(graph: nx.Graph, block: frozenset[int]) -> bool:
    return all(
        any(graph.has_edge(vertex, member) for member in block)
        for vertex in set(S) - set(block)
    )


def candidate_blocks(graph: nx.Graph) -> list[frozenset[int]]:
    return [
        frozenset(choice)
        for size in range(2, 8)
        for choice in combinations(S, size)
        if independent(graph, frozenset(choice))
        and maximal_independent(graph, frozenset(choice))
    ]


def maximum_singleton_cliques(graph: nx.Graph, partition):
    singletons = frozenset(
        next(iter(block)) for block in partition if len(block) == 1
    )
    width = omega(graph.subgraph(singletons))
    return [
        frozenset(choice)
        for choice in combinations(singletons, width)
        if graph.subgraph(choice).number_of_edges() == width * (width - 1) // 2
    ]


def partial_carrier_funds(
    graph: nx.Graph,
    block: frozenset[int],
    clique: frozenset[int],
    defect: frozenset[int],
) -> bool:
    if block & defect:
        return False
    return all(
        any(graph.has_edge(missed, vertex) for vertex in block)
        for missed in clique & defect
    )


def returned_state_closes(graph: nx.Graph, partition, defect: frozenset[int]) -> bool:
    value = demand(graph, partition)
    if value <= 2:
        return True
    if value != 3:
        return False
    for clique in maximum_singleton_cliques(graph, partition):
        blocks = [
            block
            for block in partition
            if not (len(block) == 1 and next(iter(block)) in clique)
        ]
        if len(blocks) != 3:
            continue
        if any(partial_carrier_funds(graph, block, clique, defect) for block in blocks):
            return True
    return False


def main() -> None:
    boundaries = residual_boundaries()
    assert len(boundaries) == 129
    defects = [frozenset()]
    defects += [frozenset({vertex}) for vertex in S]
    defects += [frozenset(pair) for pair in combinations(S, 2)]

    failures = []
    witnesses = 0
    for index, graph in enumerate(boundaries):
        blocks = candidate_blocks(graph)
        for defect in defects:
            witness = next(
                (
                    block
                    for block in blocks
                    if all(
                        returned_state_closes(graph, state, defect)
                        for state in exact_states(graph, block)
                    )
                ),
                None,
            )
            if witness is None:
                failures.append((index, sorted(defect)))
            else:
                witnesses += 1

    cells = len(boundaries) * len(defects)
    print(f"boundaries={len(boundaries)}")
    print(f"cells={cells}")
    print(f"witnesses={witnesses}")
    print(f"failures={len(failures)}")
    for failure in failures[:100]:
        print("FAIL", failure)
    assert cells == 3741
    assert witnesses == cells
    assert not failures
    print("CERTIFIED full-residual defect-two carrier reflection")


if __name__ == "__main__":
    main()
