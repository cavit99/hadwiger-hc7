"""Falsification search for adaptive matching-linked elimination flags.

The full independent-trace property is automatic for X=V(G) when G is
vertex-critical: delete one vertex of a nonempty independent trace and then
colour the rest with k-1 colours.  Hence vertex-critical graphs are a clean
test family.  This program is only a discovery tool; any hit needs a hand
proof.
"""

from __future__ import annotations

import itertools

import networkx as nx

import search_colourful_flags as cf


def k_colourable(g: nx.Graph, k: int) -> bool:
    colours = {}

    def rec() -> bool:
        if len(colours) == len(g):
            return True
        uncoloured = [v for v in g if v not in colours]
        v = max(
            uncoloured,
            key=lambda x: (
                len({colours[y] for y in g[x] if y in colours}),
                g.degree[x],
            ),
        )
        forbidden = {colours[y] for y in g[v] if y in colours}
        for c in range(k):
            if c not in forbidden:
                colours[v] = c
                if rec():
                    return True
                del colours[v]
        return False

    return rec()


def two_linkage(g: nx.Graph, roots, pair1, pair2) -> bool:
    a, b = pair1
    c, d = pair2
    h = g.copy()
    h.remove_nodes_from(set(roots) - {a, b, c, d})
    first = h.copy()
    first.remove_nodes_from([c, d])
    if a not in first or b not in first:
        return False
    for path in nx.all_simple_paths(first, a, b):
        rest = h.copy()
        rest.remove_nodes_from(path)
        if c in rest and d in rest and nx.has_path(rest, c, d):
            return True
    return False


def matching_linked_four(g: nx.Graph, roots) -> bool:
    a, b, c, d = roots
    pairings = [
        ((a, b), (c, d)),
        ((a, c), (b, d)),
        ((a, d), (b, c)),
    ]
    return all(two_linkage(g, roots, p, q) for p, q in pairings)


def has_adaptive_flag(g: nx.Graph) -> bool:
    vertices = tuple(g)
    cf._COLOUR_CACHE.clear()
    cf._COLOURFUL_CACHE.clear()
    seen = set()
    for roots in cf.flags(g, vertices, vertices, 4):
        if roots in seen:
            continue
        seen.add(roots)
        if matching_linked_four(g, roots):
            return True
    return False


def critical_extensions_to_eight():
    """Generate (with duplicates) all 8-vertex 4-critical graphs."""
    for base in nx.graph_atlas_g():
        if len(base) != 7:
            continue
        base = nx.convert_node_labels_to_integers(base)
        for mask in range(1 << 7):
            g = base.copy()
            g.add_node(7)
            g.add_edges_from((7, v) for v in range(7) if mask & (1 << v))
            if min(dict(g.degree()).values()) < 3:
                continue
            if k_colourable(g, 3):
                continue
            if all(k_colourable(g.copy().subgraph(set(g) - {v}), 3) for v in g):
                yield g


def main():
    representatives: dict[str, list[nx.Graph]] = {}
    count = 0
    for g in critical_extensions_to_eight():
        key = nx.weisfeiler_lehman_graph_hash(g)
        if any(nx.is_isomorphic(g, old) for old in representatives.get(key, [])):
            continue
        representatives.setdefault(key, []).append(g.copy())
        count += 1
        if not has_adaptive_flag(g):
            print("NO ADAPTIVE FLAG")
            print("edges", sorted(g.edges()))
            return
        if count % 10 == 0:
            print("critical representatives", count, flush=True)
    print("No counterexample; representatives", count)


if __name__ == "__main__":
    main()
