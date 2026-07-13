#!/usr/bin/env python3
"""Atlas probe for the order-seven three-view rooted-K4 residue.

This does not encode portal contact rows or operation states.  It asks a
clean structural question: among seven-vertex, 3-connected graphs of
minimum degree at least four, which labelings of six cycle roots make all
three antipodal-complement rooted K4 views fail?
"""

from __future__ import annotations

import itertools

import networkx as nx


def connected(mask: int, adj: list[int]) -> bool:
    if not mask:
        return False
    seen = mask & -mask
    frontier = seen
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        v = bit.bit_length() - 1
        add = adj[v] & mask & ~seen
        seen |= add
        frontier |= add
    return seen == mask


def rooted_k4(adj: list[int], roots: tuple[int, ...]) -> bool:
    n = len(adj)
    root_mask = sum(1 << r for r in roots)
    candidates: list[list[int]] = []
    full = (1 << n) - 1
    for r in roots:
        allowed = full ^ (root_mask ^ (1 << r))
        vals = [m for m in range(1, 1 << n)
                if m & (1 << r) and not m & ~allowed and connected(m, adj)]
        vals.sort(key=int.bit_count)
        candidates.append(vals)

    order = sorted(range(4), key=lambda i: len(candidates[i]))
    chosen = [0] * 4

    def touch(a: int, b: int) -> bool:
        union = 0
        z = a
        while z:
            bit = z & -z
            z ^= bit
            union |= adj[bit.bit_length() - 1]
        return bool(union & b)

    def search(pos: int, used: int) -> bool:
        if pos == 4:
            return True
        i = order[pos]
        for m in candidates[i]:
            if m & used:
                continue
            if any(chosen[j] and not touch(m, chosen[j]) for j in range(4)):
                continue
            chosen[i] = m
            if search(pos + 1, used | m):
                return True
            chosen[i] = 0
        return False

    return search(0, 0)


def main():
    total_graphs = 0
    survivor_graphs: dict[int, tuple[int, tuple[int, ...]]] = {}
    labelled = 0
    views = (
        (1, 2, 4, 5),  # omit antipodal 0,3
        (0, 2, 3, 5),  # omit 1,4
        (0, 1, 3, 4),  # omit 2,5
    )
    for index, graph in enumerate(nx.graph_atlas_g()):
        if len(graph) != 7 or min(dict(graph.degree()).values()) < 4:
            continue
        if nx.node_connectivity(graph) < 3:
            continue
        total_graphs += 1
        adj = [0] * 7
        for u, v in graph.edges:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
        good4 = {q: rooted_k4(adj, q) for q in itertools.combinations(range(7), 4)}
        for roots in itertools.permutations(range(7), 6):
            if all(not good4[tuple(sorted(roots[i] for i in view))]
                   for view in views):
                labelled += 1
                survivor_graphs.setdefault(index, (graph.number_of_edges(), roots))
                break

    print("eligible underlying graphs", total_graphs)
    print("surviving underlying graphs", len(survivor_graphs))
    for index, (m, roots) in sorted(survivor_graphs.items()):
        print("atlas", index, "edges", m, "roots", roots)
    print("first-witness count", labelled)


if __name__ == "__main__":
    main()
