#!/usr/bin/env python3
"""Exact symbolic audit of the all-pair-intersection-two three-K5 case.

The guaranteed cliques are
  L1={z,a,b,p1,p2}, L2={z,a,c,q1,q2}, L3={z,b,c,r1,r2}.
For any chosen core vertex x in {z,a,b,c}, deleting the other three core
vertices leaves a 4-connected graph. Häggkvist--Thomassen gives a cycle
through the three independent private edges P,Q,R.  Contract each interval
between the four special objects x,P,Q,R, retaining all possible cyclic
orders and orientations.  Add only the guaranteed clique edges and ask
whether the resulting symbolic graph has a K7-minus minor.

If one core choice succeeds for every order/orientation, the hard triple is
closed without any extra host hypothesis beyond seven-connectivity.
"""

from __future__ import annotations

from itertools import permutations, product
import json
import networkx as nx

from hc7_degree8_alpha3_virtual_edge_census import k7minus_model


CORE = ("z", "a", "b", "c")
PAIRS = {
    "P": ("p1", "p2"),
    "Q": ("q1", "q2"),
    "R": ("r1", "r2"),
}
CLIQUES = [
    ("z", "a", "b", "p1", "p2"),
    ("z", "a", "c", "q1", "q2"),
    ("z", "b", "c", "r1", "r2"),
]


def symbolic_graph(kept: str, order: tuple[str, ...], flips: tuple[int, int, int]) -> nx.Graph:
    G = nx.Graph()
    for clique in CLIQUES:
        for i, u in enumerate(clique):
            for v in clique[i + 1 :]:
                G.add_edge(u, v)

    oriented = {}
    for label, flip in zip(("P", "Q", "R"), flips):
        u, v = PAIRS[label]
        oriented[label] = (v, u) if flip else (u, v)

    # Each object has an entry and exit along the cycle.  A private-edge object
    # traverses its guaranteed edge; the singleton core object has entry=exit.
    entry = {kept: kept}
    exit_ = {kept: kept}
    for label in ("P", "Q", "R"):
        entry[label], exit_[label] = oriented[label]
        G.add_edge(*oriented[label])

    for i, obj in enumerate(order):
        nxt = order[(i + 1) % len(order)]
        G.add_edge(exit_[obj], entry[nxt])
    return G


def decode(G: nx.Graph, model: tuple[int, ...] | None) -> list[list[str]] | None:
    if model is None:
        return None
    labels = nx.get_node_attributes(G, "name")
    return [[labels[v] for v in range(G.number_of_nodes()) if mask & (1 << v)] for mask in model]


def canonical_orders(kept: str):
    # Fix the singleton first; reversal is left in deliberately as an
    # independent audit rather than quotiented out.
    for tail in permutations(("P", "Q", "R")):
        yield (kept,) + tail


def main() -> None:
    result = {}
    for kept in CORE:
        failures = []
        examples = []
        tested = 0
        for order in canonical_orders(kept):
            for flips in product((0, 1), repeat=3):
                tested += 1
                named = symbolic_graph(kept, order, flips)
                G = nx.convert_node_labels_to_integers(named, ordering="sorted", label_attribute="name")
                model = k7minus_model(G)
                if model is None:
                    failures.append({"order": order, "flips": flips, "graph6": nx.to_graph6_bytes(G, header=False).decode().strip()})
                elif len(examples) < 4:
                    examples.append({"order": order, "flips": flips, "model": decode(G, model)})
        result[kept] = {"tested": tested, "failures": failures, "examples": examples}

    print(json.dumps(result, sort_keys=True))
    assert any(not data["failures"] for data in result.values()), result


if __name__ == "__main__":
    main()
