#!/usr/bin/env python3
"""Probe the adaptive state exchange with one full and two near-full carriers.

For each of the ten audited absolute-demand-three boundary orbits, choose an
independent exact block I whose every proper equality state has demand three.
For every such state and every ordered pair of distinct carrier defects a,b,
test whether one full carrier Q and adjacent carriers X,Y missing a,b can fund
the three blocks outside a maximum singleton clique.

This is boundary algebra only.  A positive result becomes geometric only when
the three carriers really are disjoint, connected, and X,Y are adjacent.

Run from the repository root with

  PYTHONPATH=active/runtime/deps:active python3 \
      results/hc7_exact7_three_carrier_state_probe.py
"""

from __future__ import annotations

from itertools import combinations, permutations

import networkx as nx

from hc7_exact7_adaptive_12_boundary_verify import (
    PARTITIONS,
    S,
    demand,
    independent,
    omega,
)
from hc7_exact7_adaptive_12_residue_probe import (
    has_any_safe_state,
    robust_block,
    two_anchor_lift,
)


def hard_boundaries() -> list[nx.Graph]:
    return [
        graph
        for graph in nx.graph_atlas_g()
        if len(graph) == 7
        and omega(graph) <= 3
        and robust_block(graph) is None
        and two_anchor_lift(graph) is None
        and not has_any_safe_state(graph)
    ]


def exact_states(graph: nx.Graph, block: frozenset[int]):
    return [
        partition
        for partition in PARTITIONS
        if block in partition
        and all(independent(graph, part) for part in partition)
    ]


def normalized_blocks(graph: nx.Graph) -> list[frozenset[int]]:
    answer = []
    for size in range(2, 4):
        for choice in combinations(S, size):
            block = frozenset(choice)
            if not independent(graph, block):
                continue
            states = exact_states(graph, block)
            if states and all(demand(graph, state) == 3 for state in states):
                answer.append(block)
    return answer


def maximum_singleton_cliques(
    graph: nx.Graph,
    partition: tuple[frozenset[int], ...],
) -> list[frozenset[int]]:
    singletons = frozenset(
        next(iter(block)) for block in partition if len(block) == 1
    )
    width = omega(graph.subgraph(singletons))
    return [
        frozenset(choice)
        for choice in combinations(singletons, width)
        if graph.subgraph(choice).number_of_edges() == width * (width - 1) // 2
    ]


def carrier_funds(
    graph: nx.Graph,
    block: frozenset[int],
    clique: frozenset[int],
    defect: int | None,
) -> bool:
    """Whether a carrier complete to S-defect can represent this block."""

    if defect is None:
        return True

    # The carrier-block union must be connected.  Equality blocks are
    # independent, so if the missed literal lies in the assigned block it
    # has no edge either to the carrier or to another block vertex.
    if defect in block:
        return False

    # Only the missed literal can fail carrier adjacency to the retained
    # singleton clique; a boundary edge from the represented block repairs it.
    if defect in clique and not any(graph.has_edge(defect, x) for x in block):
        return False
    return True


def state_closes(
    graph: nx.Graph,
    partition: tuple[frozenset[int], ...],
    defect_x: int,
    defect_y: int,
) -> bool:
    for clique in maximum_singleton_cliques(graph, partition):
        blocks = [
            block
            for block in partition
            if not (len(block) == 1 and next(iter(block)) in clique)
        ]
        assert len(blocks) == 3
        for q_block, x_block, y_block in permutations(blocks):
            if not carrier_funds(graph, q_block, clique, None):
                continue
            if not carrier_funds(graph, x_block, clique, defect_x):
                continue
            if not carrier_funds(graph, y_block, clique, defect_y):
                continue
            return True
    return False


def main() -> None:
    boundaries = hard_boundaries()
    assert len(boundaries) == 10
    total_states = 0
    failures = []

    for index, graph in enumerate(boundaries):
        candidates = normalized_blocks(graph)
        assert candidates
        best = None
        best_failures = None
        for block in candidates:
            states = exact_states(graph, block)
            current = []
            for partition in states:
                for defect_x, defect_y in permutations(S, 2):
                    if not state_closes(
                        graph, partition, defect_x, defect_y
                    ):
                        current.append((partition, defect_x, defect_y))
            if best_failures is None or len(current) < len(best_failures):
                best = block
                best_failures = current
        assert best is not None and best_failures is not None
        total_states += len(exact_states(graph, best))
        print(
            f"boundary={index} block={sorted(best)} "
            f"states={len(exact_states(graph, best))} "
            f"failures={len(best_failures)}"
        )
        failures.extend((index, best, *failure) for failure in best_failures)

        # The star-contraction block may be chosen after the two geometric
        # defects are known, but before the returned state is known.
        adaptive_failures = []
        for defect_x, defect_y in permutations(S, 2):
            if not any(
                all(
                    state_closes(graph, state, defect_x, defect_y)
                    for state in exact_states(graph, block)
                )
                for block in candidates
            ):
                adaptive_failures.append((defect_x, defect_y))
        print(f"  adaptive_defect_failures={adaptive_failures}")

    print(f"total_states={total_states}")
    print(f"total_failures={len(failures)}")
    for failure in failures[:40]:
        print("FAIL", failure)

    # Compact independently checkable certificate used in the companion
    # theorem note.  Codes are graph6 strings in graph-atlas labeling.
    fixed_blocks = {
        "FCc`G": frozenset({0, 1, 2}),
        "FKc`G": frozenset({0, 1, 5}),
        "F`ooo": frozenset({0, 2, 6}),
        "Feo`G": frozenset({2, 3, 4}),
        "FMs`G": frozenset({0, 1, 5}),
        "F`NBW": frozenset({0, 3, 6}),
        "FhMMG": frozenset({1, 3, 5}),
        "FlBHo": frozenset({0, 2, 4}),
        "FBjN_": frozenset({0, 1, 2}),
    }
    codes = {
        nx.to_graph6_bytes(graph, header=False).decode().strip(): graph
        for graph in boundaries
    }
    assert set(codes) == set(fixed_blocks) | {"F{cZG"}
    for code, block in fixed_blocks.items():
        graph = codes[code]
        assert all(
            state_closes(graph, state, defect_x, defect_y)
            for state in exact_states(graph, block)
            for defect_x, defect_y in permutations(S, 2)
        )

    moser = codes["F{cZG"]
    for defect_x, defect_y in permutations(S, 2):
        block = (
            frozenset({0, 5})
            if frozenset({defect_x, defect_y}) == frozenset({3, 4})
            else frozenset({1, 5})
        )
        assert all(
            state_closes(moser, state, defect_x, defect_y)
            for state in exact_states(moser, block)
        )
    print("CERTIFIED adaptive three-carrier exchange")


if __name__ == "__main__":
    main()
