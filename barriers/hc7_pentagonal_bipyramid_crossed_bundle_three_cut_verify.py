#!/usr/bin/env python3
"""Verify the crossed-bundle three-cut barrier."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "active" / "runtime" / "deps"))

import networkx as nx


# This order is retained so that the displayed graph6 certificate is stable.
VERTICES = ("q", "c1", "c2", "c3", "c4", "p0", "p1", "c00", "c01")
EDGES = {
    ("p0", "p1"),
    ("c00", "c01"),
    ("p0", "c01"),
    ("p1", "c00"),
    ("p0", "c1"),
    ("p0", "c2"),
    ("p0", "c3"),
    ("p1", "c4"),
    ("c00", "c1"),
    ("c00", "q"),
    ("c01", "c4"),
    ("c1", "c2"),
    ("c2", "c3"),
    ("c3", "c4"),
    ("q", "c1"),
    ("q", "c2"),
    ("q", "c3"),
    ("q", "c4"),
}


def exact_k5_minor(graph: nx.Graph):
    """Return five exact branch-set masks, or None."""
    vertices = tuple(graph)
    n = len(vertices)
    index = {vertex: i for i, vertex in enumerate(vertices)}
    adjacency = [0] * n
    for left, right in graph.edges():
        i, j = index[left], index[right]
        adjacency[i] |= 1 << j
        adjacency[j] |= 1 << i

    connected: list[int] = []
    external: dict[int, int] = {}
    for mask in range(1, 1 << n):
        reached = mask & -mask
        while True:
            enlarged = reached
            work = reached
            while work:
                bit = work & -work
                work -= bit
                enlarged |= adjacency[bit.bit_length() - 1] & mask
            if enlarged == reached:
                break
            reached = enlarged
        if reached != mask:
            continue
        connected.append(mask)
        neighbours = 0
        work = mask
        while work:
            bit = work & -work
            work -= bit
            neighbours |= adjacency[bit.bit_length() - 1]
        external[mask] = neighbours

    connected.sort(key=lambda mask: (mask.bit_count(), mask))

    def extend(chosen: list[int], start: int):
        if len(chosen) == 5:
            return chosen
        for position in range(start, len(connected)):
            mask = connected[position]
            if any(mask & old for old in chosen):
                continue
            if any(not (external[mask] & old) for old in chosen):
                continue
            result = extend(chosen + [mask], position + 1)
            if result is not None:
                return result
        return None

    return extend([], 0)


def main() -> None:
    graph = nx.Graph()
    graph.add_nodes_from(VERTICES)
    graph.add_edges_from(EDGES)

    assert not nx.check_planarity(graph)[0]
    assert exact_k5_minor(graph) is None
    assert nx.node_connectivity(graph) == 3
    assert nx.to_graph6_bytes(graph, header=False).strip() == b"H|do]CL"

    cut = {"p0", "c4", "c00"}
    remainder = graph.copy()
    remainder.remove_nodes_from(cut)
    components = {frozenset(component) for component in nx.connected_components(remainder)}
    assert components == {
        frozenset(("c1", "c2", "c3", "q")),
        frozenset(("p1",)),
        frozenset(("c01",)),
    }

    print("GREEN crossed PB bundle: nonplanar K5-free connectivity=3")


if __name__ == "__main__":
    main()
