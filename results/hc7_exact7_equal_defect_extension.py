#!/usr/bin/env python3
"""Verify the equal-defect extension of adaptive three-carrier exchange.

The audited theorem checks distinct defects.  This companion checks all
49 ordered pairs, including the case in which both adjacent near-full
carriers miss the same literal.  It reuses the audited state predicates.

Run with

  PYTHONPATH=active/runtime/deps:results python3 \
      results/hc7_exact7_equal_defect_extension.py
"""

from __future__ import annotations

from itertools import product

import networkx as nx

from hc7_exact7_three_carrier_state_probe import (
    S,
    exact_states,
    hard_boundaries,
    state_closes,
)


FIXED_BLOCKS = {
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


def code(graph: nx.Graph) -> str:
    return nx.to_graph6_bytes(graph, header=False).decode().strip()


def maximal_independent(graph: nx.Graph, block: frozenset[int]) -> bool:
    return all(
        any(graph.has_edge(vertex, member) for member in block)
        for vertex in set(S) - set(block)
    )


def main() -> None:
    graphs = {code(graph): graph for graph in hard_boundaries()}
    assert set(graphs) == set(FIXED_BLOCKS) | {"F{cZG"}

    for graph_code, block in FIXED_BLOCKS.items():
        graph = graphs[graph_code]
        assert maximal_independent(graph, block)
        assert all(
            state_closes(graph, state, defect_x, defect_y)
            for state in exact_states(graph, block)
            for defect_x, defect_y in product(S, repeat=2)
        )

    moser = graphs["F{cZG"]
    for defect_x, defect_y in product(S, repeat=2):
        # I={1,5} has exactly the four failures with both defects in {3,4};
        # I={0,5} repairs all four at once.
        block = (
            frozenset({0, 5})
            if defect_x in {3, 4} and defect_y in {3, 4}
            else frozenset({1, 5})
        )
        assert maximal_independent(moser, block)
        assert all(
            state_closes(moser, state, defect_x, defect_y)
            for state in exact_states(moser, block)
        )

    print("CERTIFIED equal-defect adaptive three-carrier extension")


if __name__ == "__main__":
    main()
