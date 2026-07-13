#!/usr/bin/env python3
"""Exact quotient atlas for the unique-owner triangle residue.

X carries (h,c), Y carries (r,a), X-Y is an edge, and E is the
opposite full shore.  Each of 1,2,b has support X, Y, or both.  The
script prints the K7-free support words and a branch-set certificate for
every other word.
"""

from __future__ import annotations

import itertools

import triangle_frame_search as core


VERTICES = core.B + ("E", "X", "Y")
HELPERS = ("1", "2", "b")


def graph(word: tuple[int, int, int]):
    edges = set(core.BASE)
    edges |= {core.edge("E", z) for z in core.B}
    edges |= {core.edge("X", "Y")}
    edges |= {core.edge("X", z) for z in ("h", "c")}
    edges |= {core.edge("Y", z) for z in ("r", "a")}
    for z, support in zip(HELPERS, word):
        if support & 1:
            edges.add(core.edge("X", z))
        if support & 2:
            edges.add(core.edge("Y", z))
    return edges


def find_model(edges: set[tuple[str, str]]):
    for size in range(7, len(VERTICES) + 1):
        for used in itertools.combinations(VERTICES, size):
            for blocks in core.partitions(used, 7):
                if not all(core.connected(block, edges) for block in blocks):
                    continue
                if all(
                    any(core.edge(x, y) in edges for x in left for y in right)
                    for left, right in itertools.combinations(blocks, 2)
                ):
                    return blocks
    return None


def main() -> None:
    survivors = []
    for word in itertools.product((1, 2, 3), repeat=3):
        model = find_model(graph(word))
        if model is None:
            survivors.append(word)
        else:
            print(word, "|".join("".join(block) for block in model))
    print("survivors", survivors)


if __name__ == "__main__":
    main()
