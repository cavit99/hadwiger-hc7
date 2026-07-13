#!/usr/bin/env python3
"""Verify the parity Property-B certificate for W5 disjoint-union 3K1."""

from __future__ import annotations

import itertools


def partitions(order: int, maximum_blocks: int):
    output = []

    def visit(vertex: int, blocks: list[list[int]]) -> None:
        if vertex == order:
            output.append(tuple(tuple(block) for block in blocks))
            return
        for index in range(len(blocks)):
            blocks[index].append(vertex)
            visit(vertex + 1, blocks)
            blocks[index].pop()
        if len(blocks) < maximum_blocks:
            blocks.append([vertex])
            visit(vertex + 1, blocks)
            blocks.pop()

    visit(0, [])
    return tuple(output)


def main() -> None:
    # Rim 0-1-2-3-0, hub 4, isolated vertices 5,6,7.
    edges = {
        tuple(sorted(edge))
        for edge in (
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 0), (4, 1), (4, 2), (4, 3),
        )
    }

    def independent(block) -> bool:
        return all(
            tuple(sorted(pair)) not in edges
            for pair in itertools.combinations(block, 2)
        )

    states = tuple(
        state
        for state in partitions(8, 6)
        if all(independent(block) for block in state)
    )
    assert len(states) == 573

    independent_blocks = tuple(
        tuple(vertex for vertex in range(8) if mask >> vertex & 1)
        for mask in range(1, 1 << 8)
        if independent(
            tuple(vertex for vertex in range(8) if mask >> vertex & 1)
        )
    )
    assert len(independent_blocks) == 63

    for block in independent_blocks:
        edge = tuple(state for state in states if block in state)
        assert edge
        assert {len(state) % 2 for state in edge} == {0, 1}

    print("proper states", len(states))
    print("independent exact blocks", len(independent_blocks))
    print("all exact-block edges contain both block-count parities")


if __name__ == "__main__":
    main()
