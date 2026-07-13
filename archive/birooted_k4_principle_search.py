#!/usr/bin/env python3
"""Small-order falsification search for a birooted K4 principle.

For each 4-connected 4-chromatic graph in the NetworkX graph atlas, find
all inclusion-minimal sets which use all four colours in every proper
4-colouring.  Test every pair X,Y for a K4 minor model whose four bags each
meet both X and Y.  This is a conjecture probe, not a proof certificate.
"""

from __future__ import annotations

import itertools
import sys

import networkx as nx


def colourings4(g: nx.Graph):
    order = sorted(g, key=lambda v: -g.degree(v))
    col = {}

    def rec(i):
        if i == len(order):
            yield tuple(col[v] for v in g)
            return
        v = order[i]
        forbidden = {col[w] for w in g[v] if w in col}
        for c in range(4):
            if c not in forbidden:
                col[v] = c
                yield from rec(i + 1)
                del col[v]

    yield from rec(0)


def minimal_colourful_sets(g: nx.Graph, colourings):
    vs = list(g)
    good = []
    for mask in range(1 << len(vs)):
        x = {vs[i] for i in range(len(vs)) if mask >> i & 1}
        if len(x) < 4:
            continue
        if all({c[vs.index(v)] for v in x} == {0, 1, 2, 3}
               for c in colourings):
            if not any(y < x for y in good):
                good = [y for y in good if not x < y]
                good.append(x)
    return good


def connected(g: nx.Graph, s: set[int]):
    return bool(s) and nx.is_connected(g.subgraph(s))


def has_birooted_k4(g: nx.Graph, x: set[int], y: set[int]):
    vs = list(g)
    # The connected-subset compatibility search is already substantially
    # faster at order eight; the assignment fallback is retained only for
    # the tiny atlas cases.
    if len(vs) > 7:
        candidates = []
        for mask in range(1, 1 << len(vs)):
            bag = {vs[i] for i in range(len(vs)) if mask >> i & 1}
            if bag & x and bag & y and connected(g, bag):
                candidates.append((mask, bag))
        compat = {}
        for i, (mi, bi) in enumerate(candidates):
            compat[i] = {
                j for j, (mj, bj) in enumerate(candidates)
                if i < j and not (mi & mj)
                and any(g.has_edge(u, v) for u in bi for v in bj)
            }

        def search(chosen, allowed):
            if len(chosen) == 4:
                return True
            if len(chosen) + len(allowed) < 4:
                return False
            while allowed:
                i = min(allowed)
                allowed = allowed - {i}
                nxt = {j for j in allowed if j in compat[i]}
                if search(chosen + [i], nxt):
                    return True
            return False

        return search([], set(range(len(candidates))))
    # A model is an assignment to four nonempty bags or to the unused set.
    # Break colour symmetry by requiring the least used vertex labels to
    # encounter bag labels in canonical order.
    for assn in itertools.product(range(5), repeat=len(vs)):
        bags = [{vs[i] for i, a in enumerate(assn) if a == b}
                for b in range(4)]
        if any(not b or not (b & x) or not (b & y) for b in bags):
            continue
        mins = [min(vs.index(v) for v in b) for b in bags]
        if mins != sorted(mins):
            continue
        if any(not connected(g, b) for b in bags):
            continue
        if all(any(g.has_edge(u, v) for u in bags[i] for v in bags[j])
               for i in range(4) for j in range(i + 1, 4)):
            return True
    return False


def chromatic_at_most(g: nx.Graph, k: int):
    order = sorted(g, key=lambda v: -g.degree(v))
    col = {}

    def rec(i):
        if i == len(order):
            return True
        v = order[i]
        forbidden = {col[w] for w in g[v] if w in col}
        for c in range(k):
            if c not in forbidden:
                col[v] = c
                if rec(i + 1):
                    return True
                del col[v]
        return False

    return rec(0)


def main():
    connectivity = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    tested = 0
    pairs = 0
    for idx, g0 in enumerate(nx.graph_atlas_g()):
        if len(g0) < 5 or not nx.is_connected(g0):
            continue
        if nx.node_connectivity(g0) < connectivity:
            continue
        if chromatic_at_most(g0, 3) or not chromatic_at_most(g0, 4):
            continue
        g = nx.convert_node_labels_to_integers(g0)
        cs = list(colourings4(g))
        xs = minimal_colourful_sets(g, cs)
        tested += 1
        for x in xs:
            for y in xs:
                pairs += 1
                if not has_birooted_k4(g, x, y):
                    print("COUNTEREXAMPLE", idx, len(g), sorted(g.edges()),
                          sorted(x), sorted(y), "colourings", len(cs))
                    return
    print("NO_COUNTEREXAMPLE", "connectivity", connectivity,
          "graphs", tested, "pairs", pairs)


if __name__ == "__main__":
    main()
