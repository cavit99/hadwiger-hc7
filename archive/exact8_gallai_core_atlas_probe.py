#!/usr/bin/env python3
"""Atlas probe for the seven-vertex 4-critical core in the Gallai branch."""

from __future__ import annotations

import itertools

import networkx as nx

from contact_order7_sixedge_web_probe import generic_minor_model


def colourable(g, k):
    order = sorted(g.nodes(), key=lambda v: -g.degree(v))
    colour = {}

    def rec(i):
        if i == len(order):
            return True
        v = order[i]
        used = {colour[w] for w in g.neighbors(v) if w in colour}
        for c in range(k):
            if c not in used:
                colour[v] = c
                if rec(i + 1):
                    return True
                del colour[v]
        return False

    return rec(0)


def critical4(g):
    if colourable(g, 3) or not colourable(g, 4):
        return False
    return all(colourable(nx.subgraph(g, [w for w in g if w != v]).copy(), 3)
               for v in g)


def has_k5(g):
    mapping = {v: i for i, v in enumerate(g.nodes())}
    edges = {(mapping[x], mapping[y]) for x, y in g.edges()}
    return generic_minor_model(len(mapping), edges, 5) is not None


def minor_model(g, k):
    vertices = tuple(g.nodes())
    mapping = {v: i for i, v in enumerate(vertices)}
    edges = {(mapping[x], mapping[y]) for x, y in g.edges()}
    model = generic_minor_model(len(mapping), edges, k)
    if model is None:
        return None
    return tuple(
        tuple(vertices[i] for i in range(len(vertices)) if mask >> i & 1)
        for mask in model
    )


def joined(g):
    x = nx.convert_node_labels_to_integers(g)
    u = 7
    x.add_node(u)
    x.add_edges_from((u, v) for v in range(7))
    return x


def boundary_type(h):
    missing = nx.complement(h)
    degrees = sorted(dict(missing.degree()).values())
    if degrees == [0, 1, 1, 2, 2]:
        return "adjacent-misses"
    if degrees == [0, 1, 1, 1, 1]:
        return "independent-misses"
    return None


def main():
    atlas = nx.graph_atlas_g()
    order_seven = [g for g in atlas if len(g) == 7]
    assert len(atlas) == 1253
    assert len(order_seven) == 1044
    print("atlas/order7", len(atlas), len(order_seven))
    cores = [g.copy() for g in order_seven if critical4(g)]
    print("4critical cores", len(cores))
    assert len(cores) == 7
    survivors = []
    for i, y in enumerate(cores):
        x = joined(y)
        deletion_ok = all(not has_k5(nx.subgraph(x, [w for w in x if w != v]).copy())
                          for v in x)
        types = set()
        for five in itertools.combinations(x.nodes(), 5):
            kind = boundary_type(nx.subgraph(x, five).copy())
            if kind:
                types.add(kind)
        certificate = None
        for v in y:
            model = minor_model(nx.subgraph(y, [w for w in y if w != v]).copy(), 4)
            if model is not None:
                certificate = (v, model)
                break
        assert certificate is not None
        print(i, "Yedges", y.number_of_edges(), "degree", sorted(dict(y.degree()).values()),
              "all deletions K5-free", deletion_ok, "Btypes", sorted(types))
        print(" edges", sorted(tuple(sorted(edge)) for edge in y.edges()))
        print(" delete/K4", certificate)
        if deletion_ok and types:
            survivors.append((i, y, types))
    print("survivors", [(i, sorted(types)) for i, _, types in survivors])
    assert not survivors
    for i, y, _ in survivors:
        print("rep", i, sorted(tuple(sorted(e)) for e in y.edges()))


if __name__ == "__main__":
    main()
