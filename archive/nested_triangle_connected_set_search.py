#!/usr/bin/env python3
"""Search the icosahedral shell for a connected-set triangle counterexample.

The three shell roots a,b,c are literal common neighbours of Q, with
ab,ac absent and bc present.  Every other icosahedron vertex is adjacent
to exactly two members of Q.  We enumerate all 3^9 missing-label maps and
all spanning K4 branch partitions of the icosahedron.
"""

from itertools import product

import networkx as nx


def connected_mask(graph: nx.Graph, mask: int) -> bool:
    if not mask:
        return False
    start = (mask & -mask).bit_length() - 1
    seen = 1 << start
    todo = [start]
    while todo:
        u = todo.pop()
        for v in graph[u]:
            bit = 1 << v
            if mask & bit and not seen & bit:
                seen |= bit
                todo.append(v)
    return seen == mask


def adjacent_masks(graph: nx.Graph, left: int, right: int) -> bool:
    for u in range(len(graph)):
        if left >> u & 1:
            if any(right >> v & 1 for v in graph[u]):
                return True
    return False


def spanning_k4_models(graph: nx.Graph) -> list[tuple[int, int, int, int]]:
    n = len(graph)
    models: list[tuple[int, int, int, int]] = []
    labels = [0] * n

    def rec(pos: int, maximum: int) -> None:
        if pos == n:
            if maximum != 3:
                return
            bags = [0, 0, 0, 0]
            for vertex, label in enumerate(labels):
                bags[label] |= 1 << vertex
            if not all(connected_mask(graph, bag) for bag in bags):
                return
            if not all(
                adjacent_masks(graph, bags[i], bags[j])
                for i in range(4)
                for j in range(i + 1, 4)
            ):
                return
            models.append(tuple(bags))
            return
        for label in range(min(maximum + 1, 3) + 1):
            labels[pos] = label
            rec(pos + 1, max(maximum, label))

    labels[0] = 0
    rec(1, 0)
    return models


def build_augmented(
    h: nx.Graph, common: tuple[int, int, int], rest: list[int], missing: tuple[int, ...]
) -> nx.Graph:
    g = h.copy()
    q = [12, 13, 14]
    g.add_edges_from([(q[0], q[1]), (q[0], q[2]), (q[1], q[2])])
    for x in common:
        for qi in q:
            g.add_edge(x, qi)
    for x, miss in zip(rest, missing):
        for i, qi in enumerate(q):
            if i != miss:
                g.add_edge(x, qi)
    return g


def main() -> None:
    h = nx.icosahedral_graph()
    common = None
    for a in h:
        non = [v for v in h if v != a and not h.has_edge(a, v)]
        for i, b in enumerate(non):
            for c in non[i + 1 :]:
                if h.has_edge(b, c):
                    common = (a, b, c)
                    break
            if common:
                break
        if common:
            break
    assert common is not None
    a, b, c = common
    assert not h.has_edge(a, b) and not h.has_edge(a, c) and h.has_edge(b, c)
    rest = sorted(set(h) - set(common))
    assert nx.is_connected(h.subgraph(rest))
    assert all(any(h.has_edge(x, y) for y in rest) for x in common)

    models = spanning_k4_models(h)
    print("common", common, "rest", rest, "models", len(models))

    common_mask = sum(1 << x for x in common)
    survivors = []
    seven_connected = 0
    for missing in product(range(3), repeat=len(rest)):
        g = build_augmented(h, common, rest, missing)
        if nx.node_connectivity(g) < 7:
            continue
        seven_connected += 1

        seen = [0] * len(h)
        for x in common:
            seen[x] = 0b111
        for x, miss in zip(rest, missing):
            seen[x] = 0b111 ^ (1 << miss)

        found = False
        for model in models:
            if all(
                any(seen[v] & (1 << i) for v in range(len(h)) if bag >> v & 1)
                for bag in model
                for i in range(3)
            ):
                found = True
                break
        if not found:
            survivors.append((missing, nx.to_graph6_bytes(g, header=False).decode().strip()))
            print("SURVIVOR", missing, survivors[-1][1])
            break

    print("seven_connected", seven_connected, "survivors", len(survivors))


if __name__ == "__main__":
    main()
