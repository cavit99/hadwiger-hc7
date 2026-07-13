#!/usr/bin/env python3
"""Test degree-five boundary patches of the Poussin triangulation."""

from __future__ import annotations

import itertools

from errera_c5_critical_web_probe import edge, normalized_words


V = tuple(range(15))
EDGES: set[tuple[int, int]] = set()
base = {2: [7, 8, 3, 4], 1: [7, 6], 0: [6, 5, 4], 3: [5]}
EDGES |= {edge(x, y) for x, ys in base.items() for y in ys}
for cycle in [list(range(3)), list(range(3, 9)), list(range(9, 14))]:
    EDGES |= {edge(cycle[i], cycle[(i + 1) % len(cycle)]) for i in range(len(cycle))}
path = [8, 12, 7, 11, 6, 10, 5, 9, 3, 13, 8, 12]
EDGES |= {edge(path[i], path[i + 1]) for i in range(len(path) - 1)}
EDGES |= {edge(14, i) for i in range(9, 14)}


def nbrs(x: int) -> set[int]:
    return {y for y in V if edge(x, y) in EDGES}


def cycle_order(ns: set[int]) -> tuple[int, ...] | None:
    if any(sum(edge(x, y) in EDGES for y in ns) != 2 for x in ns):
        return None
    start = min(ns)
    order = [start]
    prev = None
    cur = start
    while len(order) < len(ns):
        nxts = [y for y in ns if edge(cur, y) in EDGES and y != prev and y not in order]
        if not nxts:
            return None
        nxt = min(nxts)
        order.append(nxt)
        prev, cur = cur, nxt
    return tuple(order) if edge(order[-1], order[0]) in EDGES else None


def extends(apex: int, boundary: tuple[int, ...], word: tuple[int, ...]) -> bool:
    vertices = [x for x in V if x != apex]
    edges = {e for e in EDGES if apex not in e}
    color = {x: word[i] for i, x in enumerate(boundary)}

    def dfs(left: list[int]) -> bool:
        if not left:
            return True
        x = max(left, key=lambda z: (len({color[y] for y in color if edge(z, y) in edges}), len(nbrs(z))))
        rest = [y for y in left if y != x]
        forbidden = {color[y] for y in color if edge(x, y) in edges}
        for c in range(4):
            if c not in forbidden:
                color[x] = c
                if dfs(rest):
                    return True
                del color[x]
        return False

    return dfs([x for x in vertices if x not in color])


def main() -> None:
    print("order", len(V), "edges", len(EDGES), "degrees", sorted(map(lambda x: len(nbrs(x)), V)))
    words = normalized_words()
    for v in V:
        if len(nbrs(v)) != 5:
            continue
        boundary = cycle_order(nbrs(v))
        if boundary is None:
            continue
        base_states = {w for w in words if extends(v, boundary, w)}
        print("apex", v, "boundary", boundary, "extend", len(base_states), "fail", sorted(set(words)-base_states))


if __name__ == "__main__":
    main()
