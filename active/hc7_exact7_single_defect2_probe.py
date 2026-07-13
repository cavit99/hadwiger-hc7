#!/usr/bin/env python3
"""Test two full packets plus one carrier with boundary defect at most two."""

from __future__ import annotations

from itertools import combinations

from hc7_exact7_three_carrier_state_probe import (
    S,
    exact_states,
    hard_boundaries,
    maximum_singleton_cliques,
    normalized_blocks,
)


def state_closes(graph, partition, defect):
    for clique in maximum_singleton_cliques(graph, partition):
        blocks = [
            block
            for block in partition
            if not (len(block) == 1 and next(iter(block)) in clique)
        ]
        assert len(blocks) == 3
        for block in blocks:
            if block & defect:
                continue
            if all(
                any(graph.has_edge(c, vertex) for vertex in block)
                for c in clique & defect
            ):
                return True
    return False


def maximal_independent(graph, block):
    """Whether the independent block is inclusion-maximal in the boundary."""

    return all(
        any(graph.has_edge(vertex, member) for member in block)
        for vertex in set(S) - set(block)
    )


def main():
    failures = []
    cells = 0
    for index, graph in enumerate(hard_boundaries()):
        defects = [frozenset()]
        defects += [frozenset({a}) for a in S]
        defects += [frozenset(pair) for pair in combinations(S, 2)]
        bad = []
        for defect in defects:
            cells += 1
            witnesses = [
                block
                for block in normalized_blocks(graph)
                if maximal_independent(graph, block)
                if all(
                    state_closes(graph, state, defect)
                    for state in exact_states(graph, block)
                )
            ]
            if not witnesses:
                bad.append(sorted(defect))
        print(f"boundary={index} failures={bad}")
        failures.extend((index, defect) for defect in bad)
    print(f"total_failures={len(failures)}")
    print(f"total_cells={cells}")
    assert cells == 290
    assert not failures
    print("CERTIFIED single defect-two carrier exchange")


if __name__ == "__main__":
    main()
