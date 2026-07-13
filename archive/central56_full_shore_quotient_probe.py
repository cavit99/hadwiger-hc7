#!/usr/bin/env python3
"""Exhaustive boundary probe for the central-edge exact seven-cut.

The boundary is {h,1,2,5,6,y,z} with the forced Moser edges
h1,h2,12,16,26,56.  Each helper is a contracted full shore and hence
is complete to the boundary and anticomplete to the other helpers.
"""

from itertools import combinations

import networkx as nx

from exact7_multicomponent_quotient_atlas import k7_model


BOUNDARY = ("h", "1", "2", "5", "6", "y", "z")
BASE = {
    frozenset(edge) for edge in
    (("h", "1"), ("h", "2"), ("1", "2"),
     ("1", "6"), ("2", "6"), ("5", "6"))
}
OPTIONAL = tuple(
    frozenset(edge) for edge in combinations(BOUNDARY, 2)
    if frozenset(edge) not in BASE
    and ("y" in edge or "z" in edge)
)


def build(mask: int, shores: int):
    helpers = tuple(f"C{i}" for i in range(shores))
    edges = set(BASE)
    edges.update(OPTIONAL[i] for i in range(len(OPTIONAL)) if mask >> i & 1)
    for helper in helpers:
        edges.update(frozenset((helper, x)) for x in BOUNDARY)
    return BOUNDARY + helpers, edges


def boundary_graph(mask: int):
    graph = nx.Graph()
    graph.add_nodes_from(range(7))
    index = {name: i for i, name in enumerate(BOUNDARY)}
    graph.add_edges_from((index[tuple(edge)[0]], index[tuple(edge)[1]]) for edge in BASE)
    graph.add_edges_from(
        (index[tuple(OPTIONAL[i])[0]], index[tuple(OPTIONAL[i])[1]])
        for i in range(len(OPTIONAL)) if mask >> i & 1
    )
    return graph


def main():
    print("optional", len(OPTIONAL), [tuple(e) for e in OPTIONAL])
    for shores in (2, 3, 4):
        failures = []
        for mask in range(1 << len(OPTIONAL)):
            if k7_model(boundary_graph(mask), shores) is None:
                failures.append(mask)
        print("shores", shores, "non-K7 quotients", len(failures))
        if failures:
            maximal = [m for m in failures if not any(
                m != n and (m | n) == n for n in failures
            )]
            print(" maximal", len(maximal))
            for mask in maximal[:20]:
                added = [tuple(OPTIONAL[i]) for i in range(len(OPTIONAL)) if mask >> i & 1]
                print("  ", added)


if __name__ == "__main__":
    main()
