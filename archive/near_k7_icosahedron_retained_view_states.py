#!/usr/bin/env python3
"""Retained-bag equality states for the K2 join icosahedron model.

The spanning K7^vee model is Proposition 1.2 of
hadwiger_near_k7_two_complex_bag_round.md.  The script contracts every bag
other than the selected one and enumerates the equality types on the six
singleton images.
"""

from __future__ import annotations

from itertools import combinations

import networkx as nx


LABELS = ("A", "B", "C", "P", "Q", "D", "E")


def ambient() -> nx.Graph:
    g = nx.Graph()
    top, bottom = "t", "b"
    us = [f"u{i}" for i in range(5)]
    ws = [f"w{i}" for i in range(5)]
    for i in range(5):
        g.add_edge(top, us[i])
        g.add_edge(bottom, ws[i])
        g.add_edge(us[i], us[(i + 1) % 5])
        g.add_edge(ws[i], ws[(i + 1) % 5])
        g.add_edge(us[i], ws[i])
        g.add_edge(us[i], ws[(i - 1) % 5])
    for apex in ("p", "q"):
        for v in tuple(g.nodes):
            g.add_edge(apex, v)
    g.add_edge("p", "q")
    return g


BAGS = {
    "A": {"b"},
    "B": {"t"},
    "C": {"u0"},
    "P": {"p"},
    "Q": {"q"},
    "D": {"u1", "w0"},
    "E": {"u2", "u3", "u4", "w1", "w2", "w3", "w4"},
}


def retained_view(retained: str) -> nx.Graph:
    g = ambient()
    image = {}
    h = nx.Graph()
    for label, bag in BAGS.items():
        if label == retained:
            for v in bag:
                image[v] = v
                h.add_node(v)
        else:
            for v in bag:
                image[v] = label
            h.add_node(label)
    for x, y in g.edges:
        ix, iy = image[x], image[y]
        if ix != iy:
            h.add_edge(ix, iy)
    return h


def equality_type(colour: dict[str, int], retained: str) -> str:
    boundary = [label for label in LABELS if label != retained]
    equal = {
        frozenset((x, y))
        for x, y in combinations(boundary, 2)
        if colour[x] == colour[y]
    }
    if not equal:
        return "R"
    if equal == {frozenset(("A", "B"))}:
        return "AB"
    if equal == {frozenset(("A", "C"))}:
        return "AC"
    return "other"


def state_set(h: nx.Graph, retained: str) -> set[str]:
    boundary = tuple(label for label in LABELS if label != retained)
    internal = tuple(v for v in h if v not in boundary)
    states = set()

    assignments = []
    # Canonical boundary assignments for the only possible types.
    assignments.append(dict(zip(boundary, range(6))))
    if "A" in boundary and "B" in boundary:
        blocks = [{"A", "B"}] + [{x} for x in boundary if x not in {"A", "B"}]
        assignments.append({v: i for i, block in enumerate(blocks) for v in block})
    if "A" in boundary and "C" in boundary:
        blocks = [{"A", "C"}] + [{x} for x in boundary if x not in {"A", "C"}]
        assignments.append({v: i for i, block in enumerate(blocks) for v in block})

    for preset in assignments:
        if any(preset[x] == preset[y] for x, y in h.edges if x in preset and y in preset):
            continue
        colour = dict(preset)
        order = sorted(internal, key=lambda v: -h.degree[v])

        def extend(pos: int) -> bool:
            if pos == len(order):
                return True
            v = order[pos]
            forbidden = {colour[w] for w in h[v] if w in colour}
            for c in range(6):
                if c not in forbidden:
                    colour[v] = c
                    if extend(pos + 1):
                        return True
                    del colour[v]
            return False

        if extend(0):
            states.add(equality_type(preset, retained))
    return states


def main() -> None:
    g = ambient()
    print("connectivity", nx.node_connectivity(g))
    print("two-apex remainder planar", nx.check_planarity(g.subgraph(set(g) - {"p", "q"}))[0])
    result = {label: state_set(retained_view(label), label) for label in LABELS}
    print(result)


if __name__ == "__main__":
    main()
