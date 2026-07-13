#!/usr/bin/env python3
"""Check a Hall-tight six-adhesion obstruction to four-block realization."""

import itertools
import networkx as nx


U = (0, 2, 4, 5, 6)
W = 7
S = set(U) | {W}
A = 1
B = 3
AH = (8, 9, 10, 11, 12, 13)
BH = (14, 15, 16, 17, 18, 19)
M = {
    tuple(sorted(e))
    for e in (
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 6), (2, 6),
        (3, 4), (3, 5), (4, 5), (5, 6),
    )
}
F = {(0, 5), (2, 5), (2, 4), (4, 6), (0, 6)}


def graph():
    g = nx.Graph()
    g.add_nodes_from(range(20))
    g.add_edges_from(M)
    g.add_edges_from(itertools.combinations((A,) + AH, 2))
    g.add_edges_from(itertools.combinations((B,) + BH, 2))
    g.add_edge(A, W)
    g.add_edge(B, W)
    matched = (2, 4, 5, 6, W, W)
    g.add_edges_from(zip(AH, matched))
    g.add_edges_from((h, s) for h in BH for s in S)
    g.add_edge(0, BH[0])
    g.add_edge(W, BH[0])
    return g


def connected(g, bag):
    return bool(bag) and nx.is_connected(g.subgraph(bag))


def adjacent(g, left, right):
    return any(g.has_edge(x, y) for x in left for y in right)


def side_realizes(g, helpers, pair):
    other = [u for u in U if u not in pair]
    # The extra portal w may be assigned to any one of the four root blocks.
    traces = [set(pair)] + [{u} for u in other]
    for w_block in range(4):
        blocks = [set(trace) for trace in traces]
        blocks[w_block].add(W)
        # Assign each helper to a block or leave it unused.
        for assignment in itertools.product(range(-1, 4), repeat=len(helpers)):
            bags = [set(block) for block in blocks]
            for helper, target in zip(helpers, assignment):
                if target >= 0:
                    bags[target].add(helper)
            if not all(connected(g, bag) for bag in bags):
                continue
            if all(adjacent(g, bags[i], bags[j])
                   for i, j in itertools.combinations(range(4), 2)):
                return bags
    return None


def main():
    g = graph()
    print("connectivity", nx.node_connectivity(g))
    print("degrees", dict(g.degree()))
    print("minimum cut", sorted(nx.minimum_node_cut(g)))
    gs = g.copy()
    gs.remove_nodes_from(S)
    gu = g.copy()
    gu.remove_nodes_from(U)
    print("S deletion components", [sorted(c) for c in nx.connected_components(gs)])
    print("U deletion connected", nx.is_connected(gu))
    for pair in sorted(F):
        print(pair, side_realizes(g, AH, pair), side_realizes(g, BH, pair))
    apex = 20
    gg = g.copy()
    gg.add_node(apex)
    gg.add_edges_from((apex, n) for n in (A, B) + U)
    print("apex connectivity", nx.node_connectivity(gg))
    print("apex minimum cut", sorted(nx.minimum_node_cut(gg)))


if __name__ == "__main__":
    main()
