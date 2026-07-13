#!/usr/bin/env python3
"""Exact 49-state check of Lemma 7.1 in the colourful R--R exchange."""

from __future__ import annotations

import itertools


W = frozenset(range(6))
Z = 6
M = tuple(frozenset((i, i + 3)) for i in range(3))
X = tuple(W - pair for pair in M)


def compatibility(alpha: int, beta: int) -> tuple[set[int], set[tuple[int, int]]]:
    vertices = set(W - ({alpha} if alpha in W else set()))
    edges: set[tuple[int, int]] = set()
    for i, k in itertools.combinations(sorted(vertices), 2):
        if any({i, k} <= roots and beta not in roots - {i, k} for roots in X):
            edges.add((i, k))
    return vertices, edges


def components(vertices: set[int], edges: set[tuple[int, int]]) -> list[set[int]]:
    unseen = set(vertices)
    answer: list[set[int]] = []
    while unseen:
        start = unseen.pop()
        block = {start}
        stack = [start]
        while stack:
            here = stack.pop()
            for edge in edges:
                if here not in edge:
                    continue
                there = next(iter(set(edge) - {here}))
                if there in unseen:
                    unseen.remove(there)
                    block.add(there)
                    stack.append(there)
        answer.append(block)
    return answer


def main() -> None:
    disconnected = []
    for alpha in range(7):
        for beta in range(7):
            vertices, edges = compatibility(alpha, beta)
            blocks = components(vertices, edges)
            predicted = alpha == beta and alpha in W
            assert (len(blocks) > 1) == predicted
            if predicted:
                mate = (alpha + 3) % 6
                assert {mate} in blocks
                remainder = vertices - {mate}
                assert all(tuple(sorted(edge)) in edges
                           for edge in itertools.combinations(remainder, 2))
                disconnected.append((alpha, beta, sorted(map(sorted, blocks))))
    print("checked defect pairs", 49)
    print("disconnected cases", disconnected)


if __name__ == "__main__":
    main()
