#!/usr/bin/env python3
"""Exact K7-model check for the residual near-full Moser quotients.

Vertices 0,...,6 induce the labelled Moser spindle, 7 and 8 are
adjacent almost-full rows, and 9 is the full shore.  For every distinct
defect pair in W={1,2,3,4}, enumerate every choice of used vertices and
every canonical partition into seven nonempty branch sets.
"""

from itertools import combinations


ROOTS = frozenset(range(7))
W = (1, 2, 3, 4)
VERTICES = tuple(range(10))
X, Y, H = 7, 8, 9
MOSER = {
    (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
    (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
}


def edge(u, v):
    return (u, v) if u < v else (v, u)


def quotient_edges(a, b):
    edges = set(MOSER)
    edges.add((X, Y))
    edges.update(edge(H, s) for s in ROOTS)
    edges.update(edge(X, s) for s in ROOTS - {a})
    edges.update(edge(Y, s) for s in ROOTS - {b})
    return edges


def partitions(vertices, number):
    """Canonical unordered set partitions into exactly ``number`` blocks."""
    blocks = []

    def visit(index):
        if index == len(vertices):
            if len(blocks) == number:
                yield tuple(frozenset(block) for block in blocks)
            return
        if len(blocks) + len(vertices) - index < number:
            return
        vertex = vertices[index]
        for block in blocks:
            block.add(vertex)
            yield from visit(index + 1)
            block.remove(vertex)
        if len(blocks) < number:
            blocks.append({vertex})
            yield from visit(index + 1)
            blocks.pop()

    yield from visit(0)


def connected(block, edges):
    reached = {next(iter(block))}
    while True:
        enlarged = reached | {
            v for v in block
            if any(edge(u, v) in edges for u in reached)
        }
        if enlarged == reached:
            return len(reached) == len(block)
        reached = enlarged


def k7_model(a, b):
    edges = quotient_edges(a, b)
    for size in range(7, 11):
        for used in combinations(VERTICES, size):
            for bags in partitions(used, 7):
                if not all(connected(bag, edges) for bag in bags):
                    continue
                if all(
                    any(edge(u, v) in edges for u in left for v in right)
                    for left, right in combinations(bags, 2)
                ):
                    return bags
    return None


def main():
    answers = {}
    for a, b in combinations(W, 2):
        answers[(a, b)] = k7_model(a, b)
        print((a, b), "POSITIVE" if answers[(a, b)] else "NEGATIVE")
    assert all(model is None for model in answers.values())
    print("PASS: all six distinct W-defect quotients are K7-negative")


if __name__ == "__main__":
    main()
