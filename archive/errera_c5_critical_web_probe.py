#!/usr/bin/env python3
"""Test every degree-five boundary patch of the Errera triangulation."""

from __future__ import annotations

import itertools


EDGE_DICT = {
    0: [1, 7, 14, 15, 16],
    1: [2, 9, 14, 15],
    2: [3, 8, 9, 10, 14],
    3: [4, 9, 10, 11],
    4: [5, 10, 11, 12],
    5: [6, 11, 12, 13],
    6: [7, 8, 12, 13, 16],
    7: [13, 15, 16],
    8: [10, 12, 14, 16],
    9: [11, 13, 15],
    10: [12],
    11: [13],
    13: [15],
    14: [16],
}


def edge(x: int, y: int) -> tuple[int, int]:
    return (x, y) if x < y else (y, x)


EDGES = {edge(x, y) for x, ys in EDGE_DICT.items() for y in ys}
V = tuple(range(17))


def neighbors(x: int) -> set[int]:
    return {y for y in V if edge(x, y) in EDGES}


def boundary_cycle(v: int) -> tuple[int, ...]:
    ns = neighbors(v)
    assert len(ns) == 5
    start = min(ns)
    cycle = [start]
    previous = v
    current = start
    while len(cycle) < 5:
        options = sorted(y for y in ns if edge(current, y) in EDGES and y != previous)
        if len(cycle) > 1:
            options = [y for y in options if y != cycle[-2]]
        options = [y for y in options if y not in cycle or (len(cycle) == 4 and y == start)]
        if not options:
            # Restart by the unique unused induced-cycle neighbour.
            options = sorted(y for y in ns - set(cycle) if edge(current, y) in EDGES)
        nxt = options[0]
        cycle.append(nxt)
        current = nxt
    assert edge(cycle[-1], cycle[0]) in EDGES
    assert all(sum(edge(x, y) in EDGES for y in ns) == 2 for x in ns)
    return tuple(cycle)


def normalized_words():
    out = []
    for word in itertools.product(range(4), repeat=5):
        if word[0] != 0 or any(word[i] == word[(i + 1) % 5] for i in range(5)):
            continue
        seen: list[int] = []
        normal = []
        for c in word:
            if c not in seen:
                seen.append(c)
            normal.append(seen.index(c))
        if tuple(normal) == word:
            out.append(word)
    return out


def extends(
    deleted_apex: int,
    boundary: tuple[int, ...],
    word: tuple[int, ...],
    *,
    deleted_vertex: int | None = None,
    deleted_edge: tuple[int, int] | None = None,
    contracted_edge: tuple[int, int] | None = None,
) -> bool:
    vertices = [x for x in V if x not in {deleted_apex, deleted_vertex}]
    edges = {e for e in EDGES if deleted_apex not in e and deleted_vertex not in e}
    if deleted_edge:
        edges.discard(deleted_edge)
    if contracted_edge:
        edges.discard(contracted_edge)
    color = {x: word[i] for i, x in enumerate(boundary)}

    def compatible(x: int, c: int) -> bool:
        if contracted_edge and x in contracted_edge:
            y = contracted_edge[0] if x == contracted_edge[1] else contracted_edge[1]
            if y in color and color[y] != c:
                return False
        return all(color.get(y) != c for y in vertices if edge(x, y) in edges)

    def dfs(left: list[int]) -> bool:
        if not left:
            return contracted_edge is None or color[contracted_edge[0]] == color[contracted_edge[1]]
        x = max(
            left,
            key=lambda z: (
                len({color[y] for y in vertices if y in color and edge(z, y) in edges}),
                sum(edge(z, y) in edges for y in vertices),
            ),
        )
        rest = [y for y in left if y != x]
        if contracted_edge and x in contracted_edge:
            y = contracted_edge[0] if x == contracted_edge[1] else contracted_edge[1]
            choices = [color[y]] if y in color else range(4)
        else:
            choices = range(4)
        for c in choices:
            if compatible(x, c):
                color[x] = c
                if dfs(rest):
                    return True
                del color[x]
        return False

    return dfs([x for x in vertices if x not in color])


def main() -> None:
    assert len(EDGES) == 45
    words = normalized_words()
    for v in V:
        if len(neighbors(v)) != 5:
            continue
        boundary = boundary_cycle(v)
        base = {w for w in words if extends(v, boundary, w)}
        internal = set(V) - {v} - set(boundary)
        preserving = 0
        if len(base) < len(words):
            patch_edges = {e for e in EDGES if v not in e}
            for e in patch_edges:
                if set(e) <= internal:
                    if {w for w in words if extends(v, boundary, w, deleted_edge=e)} == base:
                        preserving += 1
                    if {w for w in words if extends(v, boundary, w, contracted_edge=e)} == base:
                        preserving += 1
            for x in internal:
                if {w for w in words if extends(v, boundary, w, deleted_vertex=x)} == base:
                    preserving += 1
        print(
            "apex", v, "boundary", boundary,
            "extend", len(base), "fail", sorted(set(words) - base),
            "preserving", preserving,
        )


if __name__ == "__main__":
    main()
