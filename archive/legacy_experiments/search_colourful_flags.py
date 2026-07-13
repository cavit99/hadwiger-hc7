"""Falsification search for the colourful-elimination flag principle.

This script is deliberately only a discovery aid.  Any returned example must
be verified and written up without relying on the computation.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations, product

import networkx as nx

_COLOUR_CACHE = {}
_COLOURFUL_CACHE = {}


def colourings(g: nx.Graph, vertices: tuple[int, ...], k: int):
    order = sorted(vertices, key=lambda v: -g.degree[v])
    assigned: dict[int, int] = {}

    def rec(pos: int):
        if pos == len(order):
            yield tuple(assigned[v] for v in vertices)
            return
        v = order[pos]
        forbidden = {assigned[w] for w in g[v] if w in assigned}
        for colour in range(k):
            if colour not in forbidden:
                assigned[v] = colour
                yield from rec(pos + 1)
                del assigned[v]

    yield from rec(0)


def colourful_sets(g: nx.Graph, vertices: tuple[int, ...], k: int):
    key = (vertices, k)
    if key in _COLOURFUL_CACHE:
        return _COLOURFUL_CACHE[key]
    if key not in _COLOUR_CACHE:
        _COLOUR_CACHE[key] = list(colourings(g, vertices, k))
    cols = _COLOUR_CACHE[key]
    if not cols:
        return []
    index = {v: i for i, v in enumerate(vertices)}
    answer = []
    for size in range(1, len(vertices) + 1):
        for subset in combinations(vertices, size):
            ss = set(subset)
            if any(set(c[index[v]] for v in ss) != set(range(k)) for c in cols):
                continue
            if any(set(old).issubset(ss) for old in answer):
                continue
            answer.append(subset)
    _COLOURFUL_CACHE[key] = answer
    return answer


def rooted_clique_model(g: nx.Graph, roots: tuple[int, ...]):
    k = len(roots)
    others = [v for v in g if v not in roots]
    root_label = {v: i for i, v in enumerate(roots)}
    for choices in product(range(-1, k), repeat=len(others)):
        bags = [{roots[i]} for i in range(k)]
        for v, label in zip(others, choices):
            if label >= 0:
                bags[label].add(v)
        if not all(nx.is_connected(g.subgraph(b)) for b in bags):
            continue
        if all(
            any(g.has_edge(x, y) for x in bags[i] for y in bags[j])
            for i in range(k)
            for j in range(i)
        ):
            return bags
    return None


def flags(g: nx.Graph, vertices: tuple[int, ...], xk: tuple[int, ...], k: int):
    """Yield root tuples (x_1,...,x_k) from every legal descent."""
    if k == 1:
        for x in xk:
            yield (x,)
        return
    key = (vertices, k)
    if key not in _COLOUR_CACHE:
        _COLOUR_CACHE[key] = list(colourings(g, vertices, k))
    cols = _COLOUR_CACHE[key]
    idx = {v: i for i, v in enumerate(vertices)}
    for x in xk:
        layers = set()
        for c in cols:
            alpha = c[idx[x]]
            if [v for v in xk if c[idx[v]] == alpha] != [x]:
                continue
            layers.add(frozenset(v for v in vertices if c[idx[v]] == alpha))
        for layer in layers:
            prev_vertices = tuple(v for v in vertices if v not in layer)
            for prev_x in colourful_sets(g, prev_vertices, k - 1):
                if not set(prev_x).issubset(set(xk) - {x}):
                    continue
                for old_roots in flags(g, prev_vertices, prev_x, k - 1):
                    yield old_roots + (x,)


def find_flag_witness(g, vertices, xk, roots, k):
    """Return explicit (X_i, c_i, A_i, x_i) records for fixed roots."""
    if k == 1:
        return [] if roots == (roots[0],) and roots[0] in xk else None
    key = (vertices, k)
    if key not in _COLOUR_CACHE:
        _COLOUR_CACHE[key] = list(colourings(g, vertices, k))
    idx = {v: i for i, v in enumerate(vertices)}
    x = roots[-1]
    for c in _COLOUR_CACHE[key]:
        alpha = c[idx[x]]
        if [v for v in xk if c[idx[v]] == alpha] != [x]:
            continue
        layer = frozenset(v for v in vertices if c[idx[v]] == alpha)
        prev_vertices = tuple(v for v in vertices if v not in layer)
        for prev_x in colourful_sets(g, prev_vertices, k - 1):
            if not set(prev_x).issubset(set(xk) - {x}):
                continue
            if not set(roots[:-1]).issubset(prev_x):
                continue
            old = find_flag_witness(g, prev_vertices, prev_x, roots[:-1], k - 1)
            if old is not None:
                assignment = {v: c[idx[v]] for v in vertices}
                return old + [(k, tuple(xk), assignment, tuple(sorted(layer)), x)]
    return None


def main():
    for count, g0 in enumerate(nx.graph_atlas_g()):
        if len(g0) < 2:
            continue
        if len(g0) > 7:
            continue
        g = nx.convert_node_labels_to_integers(g0)
        _COLOUR_CACHE.clear()
        _COLOURFUL_CACHE.clear()
        vertices = tuple(g)
        chromatic = next(
            k for k in range(1, len(g) + 1)
            if next(colourings(g, vertices, k), None) is not None
        )
        for k in [chromatic] if 2 <= chromatic <= 4 else []:
            minimal = colourful_sets(g, vertices, k)
            if not minimal:
                continue
            seen = set()
            for xk in minimal:
                for roots in flags(g, vertices, xk, k):
                    if roots in seen:
                        continue
                    seen.add(roots)
                    if rooted_clique_model(g, roots) is None:
                        print("COUNTEREXAMPLE")
                        print("n", len(g), "k", k, "edges", sorted(g.edges()))
                        print("X", xk, "roots", roots)
                        return
        if count % 100 == 0:
            print("checked", count, flush=True)
    print("No atlas counterexample")


if __name__ == "__main__":
    main()
