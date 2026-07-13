"""Search small graphs for failures of simultaneous two-set rooted clique models.

For a graph H and sets X,Y, call them q-colourful when every proper
q-colouring of H uses every colour on each set.  We test whether H has a
K_q-model all of whose branch sets meet both X and Y.
"""

from __future__ import annotations

import itertools
import networkx as nx


def proper_q_colourings(g: nx.Graph, q: int):
    vertices = sorted(g, key=lambda v: -g.degree(v))
    colour: dict[int, int] = {}

    def rec(i: int):
        if i == len(vertices):
            yield dict(colour)
            return
        v = vertices[i]
        forbidden = {colour[w] for w in g[v] if w in colour}
        for c in range(q):
            if c not in forbidden:
                colour[v] = c
                yield from rec(i + 1)
                del colour[v]

    yield from rec(0)


def chromatic_number(g: nx.Graph) -> int:
    for q in range(1, len(g) + 1):
        if next(proper_q_colourings(g, q), None) is not None:
            return q
    return 0


def colourful_sets(g: nx.Graph, q: int):
    cols = list(proper_q_colourings(g, q))
    vertices = list(g)
    ans = []
    for mask in range(1, 1 << len(vertices)):
        s = {vertices[i] for i in range(len(vertices)) if mask >> i & 1}
        if all(len({c[v] for v in s}) == q for c in cols):
            ans.append(frozenset(s))
    return ans


def connected_subsets(g: nx.Graph):
    vertices = list(g)
    ans = []
    for mask in range(1, 1 << len(vertices)):
        s = frozenset(vertices[i] for i in range(len(vertices)) if mask >> i & 1)
        if len(s) == 1 or nx.is_connected(g.subgraph(s)):
            ans.append(s)
    return ans


def has_birooted_model(g: nx.Graph, q: int, x: frozenset, y: frozenset) -> bool:
    candidates = [s for s in connected_subsets(g) if s & x and s & y]
    compatible: dict[frozenset, list[frozenset]] = {}
    for a in candidates:
        compatible[a] = [
            b
            for b in candidates
            if a.isdisjoint(b) and any(g.has_edge(u, v) for u in a for v in b)
        ]

    def rec(chosen: list[frozenset], pool: list[frozenset]) -> bool:
        if len(chosen) == q:
            return True
        for i, bag in enumerate(pool):
            if all(bag in compatible[old] for old in chosen):
                if rec(chosen + [bag], pool[i + 1 :]):
                    return True
        return False

    return rec([], candidates)


def main():
    for g in nx.graph_atlas_g():
        if len(g) < 2 or not nx.is_connected(g):
            continue
        q = chromatic_number(g)
        if q < 2 or q > 4:
            continue
        sets = colourful_sets(g, q)
        for x, y in itertools.combinations_with_replacement(sets, 2):
            if x & y:
                continue
            if not has_birooted_model(g, q, x, y):
                print("COUNTEREXAMPLE", len(g), g.number_of_edges(), q)
                print("edges", sorted(tuple(sorted(e)) for e in g.edges()))
                print("X", sorted(x), "Y", sorted(y))
                return
    print("No counterexample in graph atlas")


if __name__ == "__main__":
    main()
