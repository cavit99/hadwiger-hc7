#!/usr/bin/env python3
"""Test the full exact-block Property-B obstruction on seven-edge gates."""

from __future__ import annotations

from boundary_partition_hypergraph_probe import canonical, partitions, property_b
from equality_gate_seven_edge_packet_atlas import seven_edge_types


S = tuple(range(7))
RAW = sorted({canonical(pi) for pi in partitions(S)})


def clique(block: tuple[int, ...], missing_edges: set[tuple[int, int]]) -> bool:
    return all(tuple(sorted((u, v))) in missing_edges
               for i, u in enumerate(block) for v in block[i + 1:])


def test(missing) -> tuple[int, int, bool, bool]:
    edges = {tuple(sorted(e)) for e in missing.edges()}
    states = [pi for pi in RAW if len(pi) <= 6 and all(clique(b, edges) for b in pi)]
    index = {pi: i for i, pi in enumerate(states)}
    independent_blocks = [
        tuple(v for v in S if mask >> v & 1)
        for mask in range(1, 1 << 7)
    ]
    independent_blocks = [b for b in independent_blocks if clique(b, edges)]
    hyperedges = []
    for block in independent_blocks:
        edge = tuple(index[pi] for pi in states if block in pi)
        assert edge
        hyperedges.append(edge)
    singleton = any(len(e) == 1 for e in hyperedges)
    pb = False if singleton else property_b(hyperedges, len(states))
    return len(states), len(hyperedges), singleton, pb


def main() -> None:
    counts = {}
    for i, missing in enumerate(seven_edge_types()):
        result = test(missing)
        counts[result] = counts.get(result, 0) + 1
        print(i, result)
    print("summary", counts)


if __name__ == "__main__":
    main()
