#!/usr/bin/env python3
"""Verify the same-vertex saturation of the shared-hub barrier graph.

The checker validates the exact base graph, its displayed automorphism,
five one-edge ``K_7`` models, the degree/non-neighbour forcing step, and the
final two-edge ``K_7`` model with one named contact edge for every pair of
branch sets.
"""

from __future__ import annotations

from itertools import combinations

import networkx as nx


CORE = tuple("abcdefg")
VERTICES = CORE + ("x", "h", "p_ac", "p_bd", "p_ad", "p_bc")
Q = "p_ad"
Q_PRIME = "p_bc"


def pair(left: str, right: str) -> frozenset[str]:
    return frozenset((left, right))


def build_host() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(VERTICES)
    graph.add_edges_from(
        (left, right)
        for left, right in combinations(CORE, 2)
        if pair(left, right) not in {pair("a", "b"), pair("c", "d")}
    )
    graph.add_edges_from(("x", vertex) for vertex in "abcd")
    for left, right, middle, anchor in (
        ("a", "c", "p_ac", "f"),
        ("b", "d", "p_bd", "f"),
        ("a", "d", "p_ad", "g"),
        ("b", "c", "p_bc", "g"),
    ):
        graph.remove_edge(left, right)
        graph.add_edges_from(((left, middle), (middle, right), (anchor, middle)))
    graph.remove_edge("f", "g")
    graph.add_edges_from((("f", "h"), ("h", "g"), ("e", "h"), ("h", "x")))
    return graph


SIGMA = {
    "a": "b",
    "b": "a",
    "c": "d",
    "d": "c",
    "e": "e",
    "f": "f",
    "g": "g",
    "x": "x",
    "h": "h",
    "p_ac": "p_bd",
    "p_bd": "p_ac",
    "p_ad": "p_bc",
    "p_bc": "p_ad",
}


ONE_EDGE_MODELS: tuple[
    tuple[tuple[str, str], tuple[frozenset[str], ...]], ...
] = (
    (
        ("b", "p_ad"),
        (
            frozenset(("a", "p_ac", "p_ad")),
            frozenset(("b",)),
            frozenset(("c", "p_bc")),
            frozenset(("e",)),
            frozenset(("f", "p_bd")),
            frozenset(("g", "h")),
            frozenset(("d", "x")),
        ),
    ),
    (
        ("c", "p_ad"),
        (
            frozenset(("a", "p_ac")),
            frozenset(("b", "p_bd", "p_bc", "x")),
            frozenset(("c",)),
            frozenset(("d", "p_ad")),
            frozenset(("e",)),
            frozenset(("g",)),
            frozenset(("f", "h")),
        ),
    ),
    (
        ("p_ac", "p_ad"),
        (
            frozenset(("b",)),
            frozenset(("d", "p_ac", "p_ad", "p_bd")),
            frozenset(("e",)),
            frozenset(("f",)),
            frozenset(("a", "g")),
            frozenset(("x", "h")),
            frozenset(("c", "p_bc")),
        ),
    ),
    (
        ("p_bd", "p_ad"),
        (
            frozenset(("b", "p_bd", "p_bc")),
            frozenset(("c",)),
            frozenset(("e",)),
            frozenset(("d", "f")),
            frozenset(("g",)),
            frozenset(("a", "p_ac", "p_ad")),
            frozenset(("x", "h")),
        ),
    ),
    (
        ("p_bc", "p_ad"),
        (
            frozenset(("d", "p_ad")),
            frozenset(("e",)),
            frozenset(("b", "f", "p_bd")),
            frozenset(("g",)),
            frozenset(("a", "p_ac")),
            frozenset(("c", "p_bc")),
            frozenset(("x", "h")),
        ),
    ),
)


FINAL_BAGS = {
    "E": frozenset(("e",)),
    "F": frozenset(("f",)),
    "A": frozenset(("a", "g", "p_ac")),
    "H": frozenset(("h", "p_ad")),
    "B": frozenset(("b", "p_bc")),
    "D": frozenset(("d", "p_bd")),
    "C": frozenset(("c", "x")),
}


FINAL_CONTACTS = {
    ("E", "F"): ("e", "f"),
    ("E", "A"): ("e", "a"),
    ("E", "H"): ("e", "h"),
    ("E", "B"): ("e", "b"),
    ("E", "D"): ("e", "d"),
    ("E", "C"): ("e", "c"),
    ("F", "A"): ("f", "a"),
    ("F", "H"): ("f", "h"),
    ("F", "B"): ("f", "b"),
    ("F", "D"): ("f", "d"),
    ("F", "C"): ("f", "c"),
    ("A", "H"): ("a", "p_ad"),
    ("A", "B"): ("g", "b"),
    ("A", "D"): ("g", "d"),
    ("A", "C"): ("a", "x"),
    ("H", "B"): ("h", "p_bc"),
    ("H", "D"): ("p_ad", "d"),
    ("H", "C"): ("h", "x"),
    ("B", "D"): ("b", "p_bd"),
    ("B", "C"): ("b", "x"),
    ("D", "C"): ("d", "x"),
}


def validate_k7_model(
    graph: nx.Graph, branch_sets: tuple[frozenset[str], ...]
) -> None:
    assert len(branch_sets) == 7 and all(branch_sets)
    assert set().union(*branch_sets) == set(graph)
    assert sum(map(len, branch_sets)) == len(graph)
    assert all(nx.is_connected(graph.subgraph(branch)) for branch in branch_sets)
    assert all(
        any(graph.has_edge(left, right) for left in first for right in second)
        for first, second in combinations(branch_sets, 2)
    )


def validate_automorphism(graph: nx.Graph) -> None:
    assert set(SIGMA) == set(graph) == set(SIGMA.values())
    assert all(SIGMA[SIGMA[vertex]] == vertex for vertex in graph)
    original = {pair(left, right) for left, right in graph.edges}
    image = {pair(SIGMA[left], SIGMA[right]) for left, right in graph.edges}
    assert image == original
    assert SIGMA[Q] == Q_PRIME and SIGMA[Q_PRIME] == Q


def validate_final_contacts(graph: nx.Graph) -> None:
    labels = tuple(FINAL_BAGS)
    assert set(FINAL_CONTACTS) == set(combinations(labels, 2))
    for (first, second), (left, right) in FINAL_CONTACTS.items():
        assert graph.has_edge(left, right)
        assert (
            left in FINAL_BAGS[first] and right in FINAL_BAGS[second]
        ) or (
            right in FINAL_BAGS[first] and left in FINAL_BAGS[second]
        )


def main() -> None:
    graph = build_host()
    assert tuple(graph) == VERTICES
    assert len(graph) == 13 and graph.number_of_edges() == 34
    validate_automorphism(graph)

    assert set(graph[Q]) == {"a", "d", "g"}
    assert set(graph[Q_PRIME]) == {"b", "c", "g"}
    terminal = {other for edge, _ in ONE_EDGE_MODELS for other in edge if other != Q}
    remaining = {"e", "f", "h", "x"}
    nonneighbours = set(graph) - {Q} - set(graph[Q])
    assert terminal == {"b", "c", "p_ac", "p_bd", "p_bc"}
    assert nonneighbours == terminal | remaining
    assert graph.degree(Q) == 3 and 7 - graph.degree(Q) == len(remaining) == 4

    for added_edge, branch_sets in ONE_EDGE_MODELS:
        assert Q in added_edge and not graph.has_edge(*added_edge)
        augmented = graph.copy()
        augmented.add_edge(*added_edge)
        validate_k7_model(augmented, branch_sets)

    sigma_terminal = {SIGMA[vertex] for vertex in terminal}
    q_prime_nonneighbours = set(graph) - {Q_PRIME} - set(graph[Q_PRIME])
    assert q_prime_nonneighbours == sigma_terminal | remaining
    assert graph.degree(Q_PRIME) == 3 and 7 - graph.degree(Q_PRIME) == 4

    forced = (("h", Q), ("h", Q_PRIME))
    augmented = graph.copy()
    augmented.add_edges_from(forced)
    final_model = tuple(FINAL_BAGS.values())
    validate_k7_model(augmented, final_model)
    validate_final_contacts(augmented)

    print("GREEN atomic shared-hub same-vertex saturation")
    print("host: vertices=13 edges=34 degree(p_ad)=3 degree(p_bc)=3")
    print("automorphism: p_ad<->p_bc verified")
    print(
        "one_edge_K7_models:",
        "p_ad-b,p_ad-c,p_ad-p_ac,p_ad-p_bd,p_ad-p_bc",
    )
    print("remaining_incident_edges: p_ad-e,p_ad-f,p_ad-h,p_ad-x")
    print("forced_edges: h-p_ad,h-p_bc")
    print("two_edge_K7_model: branch_sets=7 contact_edges=21 verified")
    print("conclusion: same_vertex_minimum_degree_7_K7_free_supergraph=no")


if __name__ == "__main__":
    main()
