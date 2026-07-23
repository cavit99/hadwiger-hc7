#!/usr/bin/env python3
"""Exact symbolic probe for the triple-intersection-one three-K5 cycle case.

The guaranteed clique structure is
  L1={z,a,b,p1,p2}, L2={z,a,c,q1,q2}, L3={z,b,c,r1,r2}.
After deleting z,a,b, a prescribed-edge theorem gives a cycle through
p1p2,q1q2,r1r2. Up to reversal there are two positions for c relative to
the three edge blocks. We contract each empty gap to one edge and search the
resulting guaranteed graph exactly for a K7-minus model.
"""

from __future__ import annotations

import json
import networkx as nx

from hc7_degree8_alpha3_virtual_edge_census import encode_model, k7minus_model


def make_graph(order: list[str]) -> nx.Graph:
    G = nx.Graph()
    cliques = [
        ["z", "a", "b", "p1", "p2"],
        ["z", "a", "c", "q1", "q2"],
        ["z", "b", "c", "r1", "r2"],
    ]
    for clique in cliques:
        for i, u in enumerate(clique):
            for v in clique[i + 1 :]:
                G.add_edge(u, v)
    for i, u in enumerate(order):
        G.add_edge(u, order[(i + 1) % len(order)])
    return nx.convert_node_labels_to_integers(G, label_attribute="name")


def decode(G: nx.Graph, model: tuple[int, ...] | None) -> list[list[str]] | None:
    if model is None:
        return None
    return [[G.nodes[v]["name"] for v in range(G.number_of_nodes()) if mask & (1 << v)] for mask in model]


def main() -> None:
    cases = {
        "opposite-gap": ["p1", "p2", "c", "q1", "q2", "r1", "r2"],
        "adjacent-gap": ["p1", "p2", "q1", "q2", "c", "r1", "r2"],
    }
    result = {}
    for name, order in cases.items():
        G = make_graph(order)
        model = k7minus_model(G)
        result[name] = {
            "nodes": G.number_of_nodes(),
            "edges": G.number_of_edges(),
            "model": decode(G, model),
            "graph6": nx.to_graph6_bytes(G, header=False).decode().strip(),
        }
    print(json.dumps(result, sort_keys=True))
    assert all(data["model"] is not None for data in result.values())


if __name__ == "__main__":
    main()
