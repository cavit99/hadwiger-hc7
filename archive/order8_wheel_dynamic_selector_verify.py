#!/usr/bin/env python3
"""SAT verification of the dynamic atomic-wheel selector construction."""

from itertools import combinations

import networkx as nx
import z3


RIM = ("v0", "v1", "v2", "v3")
WHEEL = RIM + ("h",)
S = tuple(f"c{i}" for i in range(6)) + ("z",)


def add_equality_gadget(graph, a, b, tag):
    """Add K7-ab with five private clique vertices."""
    internal = tuple(f"eq_{tag}_{i}" for i in range(5))
    graph.add_edges_from(combinations(internal, 2))
    graph.add_edges_from((a, u) for u in internal)
    graph.add_edges_from((b, u) for u in internal)


def construction():
    graph = nx.Graph()
    graph.add_nodes_from(S + ("x", "p", "q", "v") + WHEEL)

    # K7-(C6+K1) boundary.
    for i in range(6):
        for j in range(i + 1, 6):
            if (i - j) % 6 not in (1, 5):
                graph.add_edge(f"c{i}", f"c{j}")
    graph.add_edges_from(("z", f"c{i}") for i in range(6))
    graph.add_edge("x", "c0")

    # Atomic wheel and contacts.
    graph.add_edges_from((RIM[i], RIM[(i + 1) % 4]) for i in range(4))
    graph.add_edges_from(("h", u) for u in RIM)
    contacts = {
        "v0": ("x", "c5", "c0", "z", "p"),
        "v1": ("c5", "c2", "c0", "z", "p"),
        "v2": ("c2", "c4", "c0", "z", "q"),
        "v3": ("c4", "x", "c0", "z", "q"),
        "h": ("c0", "z", "p", "q"),
    }
    for u, row in contacts.items():
        graph.add_edges_from((u, b) for b in row)

    # Opposite selector.
    proxies = tuple(f"y{i}" for i in range(5))
    graph.add_edges_from(combinations(proxies, 2))
    for tag, (a, b) in enumerate(
        (
            ("c0", "y0"),
            ("c2", "y1"),
            ("c4", "y2"),
            ("c5", "y3"),
            ("z", "y4"),
            ("p", "c0"),
            ("q", "c0"),
            ("c1", "c0"),
        )
    ):
        add_equality_gadget(graph, a, b, tag)
    for u in ("x", "c3"):
        graph.add_edges_from((u, f"y{i}") for i in (0, 2, 3, 4))
    graph.add_edge("x", "c3")

    # Apex.
    graph.add_edges_from(("v", u) for u in S)
    return graph


def six_colourable(graph):
    colour = {u: z3.Int(f"col_{i}") for i, u in enumerate(graph)}
    solver = z3.Solver()
    for u in graph:
        solver.add(colour[u] >= 0, colour[u] < 6)
    for u, w in graph.edges():
        solver.add(colour[u] != colour[w])
    # The proxy K5 is present in every tested minor.  Fix its palette to
    # remove the 6! global colour symmetry.
    if all(f"y{i}" in graph for i in range(5)):
        for i in range(5):
            solver.add(colour[f"y{i}"] == i)
    return solver.check() == z3.sat


def contract(graph, u, w):
    answer = nx.contracted_nodes(graph, u, w, self_loops=False)
    return nx.Graph(answer)


def main():
    graph = construction()
    assert not six_colourable(graph)

    star = contract(graph, "v", "c0")
    star = contract(star, "v", "c1")
    assert six_colourable(star)

    wheel_edges = sorted(
        tuple(sorted(edge))
        for edge in graph.edges()
        if edge[0] in WHEEL and edge[1] in WHEEL
    )
    for edge in wheel_edges:
        deleted = graph.copy()
        deleted.remove_edge(*edge)
        assert six_colourable(deleted), edge
        assert six_colourable(contract(graph, *edge)), edge

    selector = ("x", "c3")
    deleted = graph.copy()
    deleted.remove_edge(*selector)
    assert six_colourable(deleted)
    assert six_colourable(contract(graph, *selector))

    print("vertices", graph.number_of_nodes(), "edges", graph.number_of_edges())
    print("G* is not six-colourable")
    print("star contraction is six-colourable")
    print("wheel deletion/contraction pairs checked", len(wheel_edges))
    print("selector deletion and contraction checked")
    print("vertex connectivity", nx.node_connectivity(graph))


if __name__ == "__main__":
    main()
