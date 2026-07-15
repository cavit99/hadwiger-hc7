#!/usr/bin/env python3
"""Verify the Hajós drop-edge barrier and its width-five decomposition."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "active"))

from hc7_boundary_join_probe import (  # noqa: E402
    colorable,
    contract_edge,
    delete_vertex,
    induced,
)


NAMES = ("a", "u", "v", "l1", "l2", "l3", "l4", "r1", "r2", "r3", "r4")
POS = {name: i for i, name in enumerate(NAMES)}


def hajos_join() -> tuple[int, ...]:
    adj = [0] * len(NAMES)

    def add(x: str, y: str) -> None:
        u, v = POS[x], POS[y]
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    left = ("a", "u", "l1", "l2", "l3", "l4")
    right = ("a", "v", "r1", "r2", "r3", "r4")
    for side, missing in ((left, {"a", "u"}), (right, {"a", "v"})):
        for i, x in enumerate(side):
            for y in side[i + 1:]:
                if {x, y} != missing:
                    add(x, y)
    add("u", "v")
    return tuple(adj)


def remove_names(adj: tuple[int, ...], names: set[str]) -> tuple[int, ...]:
    return induced(adj, tuple(i for i, name in enumerate(NAMES) if name not in names))


def verify_tree_decomposition(adj: tuple[int, ...]) -> None:
    bags = [
        {POS[x] for x in ("a", "u", "l1", "l2", "l3", "l4")},
        {POS[x] for x in ("a", "u", "v")},
        {POS[x] for x in ("a", "v", "r1", "r2", "r3", "r4")},
    ]
    assert max(map(len, bags)) == 6
    for u in range(len(adj)):
        for v in range(u + 1, len(adj)):
            if (adj[u] >> v) & 1:
                assert any(u in bag and v in bag for bag in bags)
    for vertex in range(len(adj)):
        indices = [i for i, bag in enumerate(bags) if vertex in bag]
        assert not indices or indices == list(range(min(indices), max(indices) + 1))


def main() -> None:
    graph = hajos_join()
    assert not colorable(graph, 5)
    assert colorable(graph, 6)

    # Vertex-criticality.
    for vertex in range(len(graph)):
        assert colorable(delete_vertex(graph, vertex), 5)

    u, v = POS["u"], POS["v"]
    contracted = contract_edge(graph, u, v)
    assert not colorable(contracted, 4)
    assert colorable(contracted, 5)

    for deleted in ({"u"}, {"v"}, {"u", "v"}):
        subgraph = remove_names(graph, deleted)
        assert not colorable(subgraph, 4)
        assert colorable(subgraph, 5)

    verify_tree_decomposition(graph)
    print("GREEN: all drop-edge equalities and the width-five decomposition verify")


if __name__ == "__main__":
    main()
