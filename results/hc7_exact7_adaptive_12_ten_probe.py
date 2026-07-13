#!/usr/bin/env python3
"""Inspect the ten absolute-demand-three boundaries after the two closures."""

from __future__ import annotations

from itertools import combinations, permutations

import networkx as nx

from hc7_exact7_adaptive_12_residue_probe import (
    S,
    code,
    has_any_safe_state,
    omega,
    robust_block,
    two_anchor_lift,
)


def triangle_sets(graph: nx.Graph):
    return [
        frozenset(choice)
        for choice in combinations(S, 3)
        if omega(graph.subgraph(choice)) == 3
    ]


def marked_signature(graph: nx.Graph):
    signatures = []
    triangles = triangle_sets(graph)
    for left, right in combinations(triangles, 2):
        if not left.isdisjoint(right):
            continue
        extra = next(iter(frozenset(S) - left - right))
        for first, second in ((left, right), (right, left)):
            for a in permutations(first):
                for b in permutations(second):
                    bits = tuple(
                        int(graph.has_edge(x, y)) for x in a for y in b
                    ) + tuple(
                        int(graph.has_edge(extra, x)) for x in a + b
                    )
                    signatures.append((bits, a, b, extra))
    if not signatures:
        return None
    return min(signatures)


def main() -> None:
    graphs = [
        graph
        for graph in nx.graph_atlas_g()
        if len(graph) == 7 and omega(graph) <= 3
    ]
    hard = [
        graph
        for graph in graphs
        if robust_block(graph) is None
        and two_anchor_lift(graph) is None
        and not has_any_safe_state(graph)
    ]
    assert len(hard) == 10

    for graph in sorted(hard, key=lambda item: (item.number_of_edges(), code(item))):
        signature = marked_signature(graph)
        print(
            f"g6={code(graph)} m={graph.number_of_edges()} "
            f"degree={sorted(dict(graph.degree()).values())} "
            f"alpha={omega(nx.complement(graph))}"
        )
        if signature is None:
            print("  no_disjoint_triangle_marking")
            continue
        bits, left, right, extra = signature
        cross = bits[:9]
        extra_bits = bits[9:]
        cross_degrees_left = tuple(sum(cross[3*i:3*i+3]) for i in range(3))
        cross_degrees_right = tuple(sum(cross[i+3*j] for i in range(3)) for j in range(3))
        print(
            f"  A={left} B={right} z={extra} signature={''.join(map(str,bits))}"
        )
        print(
            f"  cross_edges={sum(cross)} cross_degrees="
            f"{cross_degrees_left}/{cross_degrees_right} "
            f"z_support={sum(extra_bits[:3])}/{sum(extra_bits[3:])}"
        )


if __name__ == "__main__":
    main()
