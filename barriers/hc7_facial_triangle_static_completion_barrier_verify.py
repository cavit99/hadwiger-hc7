#!/usr/bin/env python3
"""Verify the static facial-triangle completion barrier.

Requires NetworkX and z3-solver.  The exact minor solver is reused from the
adjacent audited quotient-barrier verifier.
"""

from __future__ import annotations

from itertools import combinations
import sys

sys.path.insert(0, "active/runtime/deps")

import networkx as nx
from z3 import Int, Solver, sat

from hc7_balanced_order8_two_missing_colour_paths_verify import (
    has_k7_minor,
    has_linkage,
)


R = ("r0", "r1", "r2")
E = ("e0", "e1")
F = ("f0", "f1")
S = R + E + F + ("x",)
C = ("a", "b", "w")
D = tuple(f"y{i}" for i in range(5))


def build_host() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(S + C + D)
    graph.add_edges_from(combinations(R, 2))
    graph.add_edge(*E)
    graph.add_edge(*F)
    graph.add_edges_from(combinations(C, 2))
    graph.add_edges_from(combinations(D, 2))

    misses = {
        "e0": {"r2"},
        "e1": {"r0", "r1"},
        "f0": {"r2"},
        "f1": {"r0", "r1"},
    }
    for endpoint, missed in misses.items():
        for vertex in R:
            if vertex not in missed:
                graph.add_edge(endpoint, vertex)

    for vertex in R:
        graph.add_edge("a", vertex)
        graph.add_edge("b", vertex)
    graph.add_edges_from((("a", "f0"), ("a", "f1"), ("b", "e0")))

    for vertex in set(S) - {"r1", "f0"}:
        graph.add_edge("w", vertex)

    for vertex in S:
        graph.add_edge("y0", vertex)
    graph.add_edges_from((("y1", "e0"), ("y2", "x")))
    return graph


def contracted_quotient(graph: nx.Graph) -> nx.Graph:
    quotient = graph.copy()
    quotient.remove_nodes_from(R)
    quotient = nx.contracted_nodes(quotient, "e0", "e1", self_loops=False)
    nx.relabel_nodes(quotient, {"e0": "ze"}, copy=False)
    quotient = nx.contracted_nodes(quotient, "f0", "f1", self_loops=False)
    nx.relabel_nodes(quotient, {"f0": "zf"}, copy=False)
    return quotient


def is_six_colourable(graph: nx.Graph) -> bool:
    colours = {vertex: Int(f"colour_{vertex}") for vertex in graph}
    solver = Solver()
    for vertex in graph:
        solver.add(colours[vertex] >= 0, colours[vertex] < 6)
    for left, right in graph.edges():
        solver.add(colours[left] != colours[right])
    return solver.check() == sat


def main() -> None:
    graph = build_host()
    boundary = set(S)
    first_shore = set(C)
    second_shore = set(D)

    assert graph.number_of_nodes() == 16
    assert graph.number_of_edges() == 49
    assert nx.node_connectivity(graph) == 3
    assert set(graph) - boundary == first_shore | second_shore
    assert not any(graph.has_edge(left, right) for left in C for right in D)
    assert nx.is_connected(graph.subgraph(C))
    assert nx.is_connected(graph.subgraph(D))
    for shore in (first_shore, second_shore):
        assert all(
            any(graph.has_edge(vertex, boundary_vertex) for vertex in shore)
            for boundary_vertex in boundary
        )

    assert all(graph.has_edge(left, right) for left, right in combinations(R, 2))
    assert graph.has_edge(*E) and graph.has_edge(*F)
    assert not any(graph.has_edge(left, right) for left in E for right in F)
    assert all(not graph.has_edge("a", endpoint) for endpoint in E)
    assert all(not graph.has_edge("b", endpoint) for endpoint in F)
    assert all(
        any(graph.has_edge(endpoint, vertex) for endpoint in E)
        for vertex in R + ("b",)
    )
    assert all(
        any(graph.has_edge(endpoint, vertex) for endpoint in F)
        for vertex in R + ("a",)
    )

    for edge in (E, F):
        missed = [
            {vertex for vertex in R if not graph.has_edge(endpoint, vertex)}
            for endpoint in edge
        ]
        assert all(missed) and missed[0].isdisjoint(missed[1])

    assert all(
        graph.has_edge(left, right)
        for left, right in combinations(set(R) | {"a", "b"}, 2)
    )
    assert all(graph.has_edge(left, right) for left, right in combinations(D, 2))

    complement = nx.complement(graph.subgraph(S))
    matching = nx.max_weight_matching(complement, maxcardinality=True)
    assert len(matching) == 4
    stated_matching = {
        frozenset(pair)
        for pair in (("f1", "r1"), ("r2", "e0"), ("x", "r0"), ("f0", "e1"))
    }
    assert all(complement.has_edge(*tuple(pair)) for pair in stated_matching)

    colour_classes = {
        0: {"a", "b", "y0"},
        1: {"w", "y1"},
        2: {"r0", "e1", "y2"},
        3: {"r1", "f1", "y3"},
        4: {"r2", "x", "y4"},
        5: {"e0", "f0"},
    }
    colour = {
        vertex: value
        for value, vertices in colour_classes.items()
        for vertex in vertices
    }
    assert set(colour) == set(graph)
    deleted = graph.copy()
    deleted.remove_edge("a", "b")
    assert all(colour[left] != colour[right] for left, right in deleted.edges())
    assert colour["a"] == colour["b"] == 0 and colour["w"] == 1
    for vertex in C:
        seen = {
            colour[neighbour]
            for neighbour in graph.neighbors(vertex)
            if neighbour in boundary
        }
        assert seen == {2, 3, 4, 5}
    assert all(
        {0, 1} != {colour[left], colour[right]}
        or graph.has_edge(left, right)
        for left, right in combinations(C, 2)
    )
    # K3 with the common two-list {0,1} is not list-colourable; every
    # proper induced subgraph is.
    assert all(graph.has_edge(left, right) for left, right in combinations(C, 2))
    assert set(S) - set(graph.neighbors("w")) == {"r1", "f0"}

    quotient = contracted_quotient(graph)
    assert nx.node_connectivity(quotient) == 3
    assert has_linkage(quotient, ("a", "b"), ("ze", "zf"))
    assert has_linkage(quotient, ("a", "zf"), ("b", "ze"))
    assert not has_linkage(quotient, ("a", "ze"), ("b", "zf"))
    assert nx.is_connected(quotient.subgraph(set(quotient) - {"a", "b", "w"}))
    assert all(quotient.has_edge("w", root) for root in ("a", "b", "ze", "zf"))

    witness_cut = {"y0", "y1", "x"}
    assert not {"ze", "zf"}.issubset(witness_cut)
    assert not nx.is_connected(quotient.subgraph(set(quotient) - witness_cut))

    assert not has_k7_minor(graph)
    assert is_six_colourable(graph)

    print("VERIFIED")
    print("vertices", graph.number_of_nodes(), "edges", graph.number_of_edges())
    print("host connectivity", nx.node_connectivity(graph))
    print("quotient connectivity", nx.node_connectivity(quotient))
    print("K7 minor", False)


if __name__ == "__main__":
    main()
