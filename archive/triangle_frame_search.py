#!/usr/bin/env python3
"""Search relaxed cyclic frames in the singleton triangle boundary.

For each K7-free optional-edge orbit, test whether bilateral web gluing
closes the boundary: the omitted set must be bipartite and every
alternating crossing quotient must contain a K7 minor.
"""

from __future__ import annotations

import itertools


B = ("h", "1", "2", "r", "a", "b", "c")
S = ("h", "1", "2", "r")
W = ("a", "b", "c")


def edge(x: str, y: str) -> tuple[str, str]:
    return tuple(sorted((x, y)))


BASE = {edge(x, y) for x, y in itertools.combinations(S, 2)}
BASE |= {edge(x, y) for x, y in itertools.combinations(W, 2)}
BASE |= {edge(x, y) for x, y in (("h", "a"), ("1", "b"), ("2", "b"), ("r", "c"))}


def connected(block: tuple[str, ...], edges: set[tuple[str, str]]) -> bool:
    reached = {block[0]}
    while True:
        more = {v for v in block if any(edge(v, u) in edges for u in reached)}
        if more <= reached:
            return len(reached) == len(block)
        reached |= more


def partitions(vertices: tuple[str, ...], k: int):
    blocks: list[list[str]] = []

    def rec(i: int):
        if i == len(vertices):
            if len(blocks) == k:
                yield tuple(tuple(x) for x in blocks)
            return
        if len(blocks) + len(vertices) - i < k:
            return
        v = vertices[i]
        for block in blocks:
            block.append(v)
            yield from rec(i + 1)
            block.pop()
        if len(blocks) < k:
            blocks.append([v])
            yield from rec(i + 1)
            blocks.pop()

    yield from rec(0)


def has_k7(vertices: tuple[str, ...], edges: set[tuple[str, str]]) -> bool:
    for size in range(7, len(vertices) + 1):
        for used in itertools.combinations(vertices, size):
            for blocks in partitions(used, 7):
                if not all(connected(block, edges) for block in blocks):
                    continue
                if all(
                    any(edge(x, y) in edges for x in left for y in right)
                    for left, right in itertools.combinations(blocks, 2)
                ):
                    return True
    return False


def bipartite(vertices: set[str], edges: set[tuple[str, str]]) -> bool:
    colour: dict[str, int] = {}
    for root in vertices:
        if root in colour:
            continue
        colour[root] = 0
        stack = [root]
        while stack:
            x = stack.pop()
            for y in vertices:
                if edge(x, y) not in edges:
                    continue
                if y not in colour:
                    colour[y] = 1 - colour[x]
                    stack.append(y)
                elif colour[y] == colour[x]:
                    return False
    return True


def canonical_cycles(items: tuple[str, ...]):
    first = min(items)
    rest = tuple(x for x in items if x != first)
    for tail in itertools.permutations(rest):
        cycle = (first,) + tail
        if cycle[1] < cycle[-1]:
            yield cycle


def frame_ok(cycle: tuple[str, ...], edges: set[tuple[str, str]]) -> bool:
    frame = {
        edge(cycle[i], cycle[(i + 1) % len(cycle)])
        for i in range(len(cycle))
    }
    return all(edge(x, y) in frame for x, y in itertools.combinations(cycle, 2) if edge(x, y) in edges)


def crossings(cycle: tuple[str, ...]):
    m = len(cycle)
    for indices in itertools.combinations(range(m), 4):
        i, r, j, s = indices
        yield (cycle[i], cycle[j]), (cycle[r], cycle[s])


def crossing_forces(
    pair1: tuple[str, str], pair2: tuple[str, str], edges: set[tuple[str, str]]
) -> bool:
    vertices = B + ("E", "X", "Y")
    qedges = set(edges)
    qedges |= {edge("E", z) for z in B}
    qedges.add(edge("X", "Y"))
    qedges |= {edge("X", z) for z in pair1}
    qedges |= {edge("Y", z) for z in pair2}
    return has_k7(vertices, qedges)


def main() -> None:
    patterns = {
        "none": set(),
        "one": {edge("1", "a")},
        "star": {edge("1", "a"), edge("1", "c")},
    }
    for name, optional in patterns.items():
        edges = BASE | optional
        solutions = []
        for size in range(4, 8):
            for chosen in itertools.combinations(B, size):
                z = set(B) - set(chosen)
                if not bipartite(z, edges):
                    continue
                for cycle in canonical_cycles(chosen):
                    if not frame_ok(cycle, edges):
                        continue
                    demands = tuple(crossings(cycle))
                    if demands and all(crossing_forces(p, q, edges) for p, q in demands):
                        solutions.append((cycle, tuple(sorted(z)), demands))
        print(name, len(solutions))
        for solution in solutions[:20]:
            print(" ", solution)


if __name__ == "__main__":
    main()
