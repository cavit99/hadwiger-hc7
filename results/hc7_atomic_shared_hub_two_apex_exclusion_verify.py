#!/usr/bin/env python3
"""Verify the two-apex exclusion for the shared-hub graph G_*."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

import networkx as nx


def build_graph() -> nx.Graph:
    graph = nx.Graph()
    branches = tuple("abcdefg")
    defects = {frozenset("ab"), frozenset("cd")}
    for left, right in combinations(branches, 2):
        if frozenset((left, right)) not in defects:
            graph.add_edge(left, right)
    graph.add_edges_from((("x", v) for v in "abcd"))
    substitutions = {
        ("a", "c"): "p_ac",
        ("b", "d"): "p_bd",
        ("a", "d"): "p_ad",
        ("b", "c"): "p_bc",
        ("f", "g"): "h",
    }
    for (left, right), middle in substitutions.items():
        graph.remove_edge(left, right)
        graph.add_edges_from(((left, middle), (middle, right)))
    graph.add_edges_from(
        (
            ("f", "p_ac"),
            ("f", "p_bd"),
            ("g", "p_ad"),
            ("g", "p_bc"),
            ("e", "h"),
            ("x", "h"),
        )
    )
    assert (len(graph), graph.number_of_edges()) == (13, 34)
    assert {vertex: graph.degree(vertex) for vertex in ("f", "g")} == {
        "f": 8,
        "g": 8,
    }
    return graph


def validate_kuratowski(graph: nx.Graph, certificate: nx.Graph) -> str:
    """Check that a returned certificate is a TK5 or TK3,3."""

    assert set(certificate) <= set(graph)
    assert all(graph.has_edge(left, right) for left, right in certificate.edges())
    assert nx.is_connected(certificate)
    branch = {v for v, degree in certificate.degree() if degree != 2}
    assert branch
    connections = []
    for start in branch:
        for neighbour in certificate[start]:
            previous, current = start, neighbour
            while current not in branch:
                options = [v for v in certificate[current] if v != previous]
                assert len(options) == 1
                previous, current = current, options[0]
            if str(start) < str(current):
                connections.append((start, current))
    core = nx.Graph()
    core.add_nodes_from(branch)
    core.add_edges_from(connections)
    assert core.number_of_edges() == len(connections)
    if len(branch) == 5:
        assert all(core.degree(v) == 4 for v in core)
        return "TK5"
    assert len(branch) == 6
    assert all(core.degree(v) == 3 for v in core)
    assert nx.is_bipartite(core)
    return "TK3,3"


def delete_objects(graph: nx.Graph, objects: tuple[tuple[str, object], ...]) -> nx.Graph:
    remainder = graph.copy()
    for kind, item in objects:
        if kind == "vertex":
            if remainder.has_node(item):
                remainder.remove_node(item)
        else:
            assert kind == "edge"
            left, right = item
            if remainder.has_edge(left, right):
                remainder.remove_edge(left, right)
    return remainder


def validate_icosahedral_sharpening(graph: nx.Graph) -> None:
    """Check the displayed TK5 in G_*-{f,g}."""

    remainder = graph.copy()
    remainder.remove_nodes_from(("f", "g"))
    roots = ("b", "c", "d", "e", "x")
    routes = {
        frozenset(("b", "c")): ("b", "p_bc", "c"),
        frozenset(("b", "d")): ("b", "p_bd", "d"),
        frozenset(("c", "d")): ("c", "p_ac", "a", "p_ad", "d"),
        frozenset(("e", "x")): ("e", "h", "x"),
    }
    for left, right in combinations(roots, 2):
        route = routes.get(frozenset((left, right)), (left, right))
        if route[0] != left:
            route = tuple(reversed(route))
        assert route[0] == left and route[-1] == right
        assert all(remainder.has_edge(u, v) for u, v in zip(route, route[1:]))
    interiors = [
        set(route[1:-1]) for route in routes.values()
    ]
    assert not (set(roots) & set().union(*interiors))
    assert sum(map(len, interiors)) == len(set().union(*interiors))


def main() -> None:
    graph = build_graph()
    validate_icosahedral_sharpening(graph)
    universe = tuple(("vertex", v) for v in graph) + tuple(
        ("edge", tuple(sorted(edge))) for edge in graph.edges()
    )
    counts = Counter()
    certificates = Counter()
    for size in range(3):
        for deleted in combinations(universe, size):
            kinds = "".join(sorted(kind[0] for kind, _ in deleted)) or "none"
            counts[kinds] += 1
            remainder = delete_objects(graph, deleted)
            planar, certificate = nx.check_planarity(
                remainder, counterexample=True
            )
            assert not planar
            certificates[validate_kuratowski(remainder, certificate)] += 1
    assert counts == {
        "none": 1,
        "v": 13,
        "e": 34,
        "vv": 78,
        "ev": 442,
        "ee": 561,
    }
    assert sum(counts.values()) == 1129
    assert sum(certificates.values()) == 1129
    print("GREEN shared-hub two-apex exclusion")
    print("deletion_cases=1129 none=1 v=13 e=34 vv=78 ve=442 ee=561")
    print(f"kuratowski_certificates={dict(sorted(certificates.items()))}")
    print("icosahedral_sharpening=G_*-{f,g} contains the displayed TK5")
    print("consequence=no subdivision of G_* embeds in a two-apex graph")


if __name__ == "__main__":
    main()
