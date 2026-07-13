#!/usr/bin/env python3
"""Exact N-meeting K6 search in the order-six one-one portal quotient."""

import itertools
import networkx as nx


N = tuple(range(7))
U = (0, 2, 4, 5, 6)
A, B, W = 1, 3, 7
M = {
    tuple(sorted(e))
    for e in (
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 6), (2, 6),
        (3, 4), (3, 5), (4, 5), (5, 6),
    )
}


def nmeeting_k6(g):
    vertices = tuple(g.nodes())
    index = {v: i for i, v in enumerate(vertices)}
    adjacency = [sum(1 << index[y] for y in g.neighbors(x)) for x in vertices]
    count = len(vertices)
    neighbour_union = [0] * (1 << count)
    connected = []
    for mask in range(1, 1 << count):
        low = mask & -mask
        i = low.bit_length() - 1
        neighbour_union[mask] = neighbour_union[mask ^ low] | adjacency[i]
        reached = low
        while True:
            expanded = reached | (neighbour_union[reached] & mask)
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            connected.append(mask)
    nmask = sum(1 << index[x] for x in N)
    for omitted in N:
        roots = [x for x in N if x != omitted]
        rootmask = nmask ^ (1 << index[omitted])
        candidates = {
            root: [m for m in connected if m & rootmask == 1 << index[root]]
            for root in roots
        }
        order = sorted(roots, key=lambda r: len(candidates[r]))

        def rec(i, bags, used):
            if i == 6:
                return bags
            for bag in candidates[order[i]]:
                if bag & used:
                    continue
                if all(neighbour_union[bag] & old for old in bags):
                    result = rec(i + 1, bags + [bag], used | bag)
                    if result is not None:
                        return result
            return None

        result = rec(0, [], 0)
        if result is not None:
            return [[vertices[i] for i in range(count) if mask >> i & 1]
                    for mask in result]
    return None


def singleton_graph(w_edges=()):
    da, db = 8, 9
    g = nx.Graph()
    g.add_nodes_from(range(10))
    g.add_edges_from(M)
    g.add_edges_from((W, x) for x in w_edges)
    g.add_edges_from((da, x) for x in set(U) | {W, A})
    g.add_edges_from((db, x) for x in set(U) | {W, B})
    return g


def pair_graph(defects):
    da = (8, 9)
    db = (10, 11)
    g = nx.Graph()
    g.add_nodes_from(range(12))
    g.add_edges_from(M)
    g.add_edge(A, W)
    g.add_edge(B, W)
    g.add_edge(*da)
    g.add_edge(*db)
    for x in da:
        g.add_edge(A, x)
    for x in db:
        g.add_edge(B, x)
    portals = set(U) | {W}
    for x, missed in zip(da + db, defects):
        g.add_edges_from((x, s) for s in portals if s != missed)
    return g


def pair_single_graph(defects):
    da = (8, 9)
    db = 10
    g = nx.Graph()
    g.add_nodes_from(range(11))
    g.add_edges_from(M)
    g.add_edge(A, W)
    g.add_edge(*da)
    for x in da:
        g.add_edge(A, x)
    portals = set(U) | {W}
    for x, missed in zip(da, defects):
        g.add_edges_from((x, s) for s in portals if s != missed)
    g.add_edges_from((db, s) for s in portals | {B})
    return g


def main():
    g = singleton_graph()
    print("minimal singleton/singleton", nmeeting_k6(g))
    failures = 0
    feasible = 0
    for mask in range(1 << 7):
        edges = [x for i, x in enumerate(N) if mask >> i & 1]
        h = singleton_graph(edges)
        gg = h.copy()
        gg.add_node(10)
        gg.add_edges_from((10, x) for x in N)
        if nx.node_connectivity(gg) < 7:
            continue
        feasible += 1
        model = nmeeting_k6(h)
        if model is None:
            failures += 1
            print("7-connected failure", edges)
            break
    print("7-connected patterns", feasible, "failures", failures)

    options = (None,) + U + (W,)
    pair_failures = []
    for index, defects in enumerate(itertools.product(options, repeat=4)):
        model = nmeeting_k6(pair_graph(defects))
        if model is None:
            pair_failures.append(defects)
            print("pair failure", defects)
            if len(pair_failures) == 10:
                break
    print("pair failures", len(pair_failures))

    ps_failures = []
    for defects in itertools.product(options, repeat=2):
        model = nmeeting_k6(pair_single_graph(defects))
        if model is None:
            ps_failures.append(defects)
            print("pair/single failure", defects)
    print("pair/single failures", len(ps_failures))


if __name__ == "__main__":
    main()
