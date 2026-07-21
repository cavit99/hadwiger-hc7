#!/usr/bin/env python3
"""Verify the exact two-path atomic-core seven-fan certificates."""

from __future__ import annotations

from itertools import combinations

import networkx as nx


CORE = tuple("abcdefg")
VERTICES = CORE + ("x", "h", "p", "q", "r", "s")


def pair(left: str, right: str) -> frozenset[str]:
    return frozenset((left, right))


def build_core() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(VERTICES)
    graph.add_edges_from(
        (left, right)
        for left, right in combinations(CORE, 2)
        if pair(left, right) not in {pair("a", "b"), pair("c", "d")}
    )
    graph.add_edges_from(("x", vertex) for vertex in "abcd")
    for left, right, route in (
        ("f", "a", ("f", "p", "a")),
        ("g", "a", ("g", "q", "a")),
        ("a", "c", ("a", "r", "s", "c")),
        ("f", "g", ("f", "h", "g")),
    ):
        graph.remove_edge(left, right)
        graph.add_edges_from(zip(route, route[1:]))
    graph.add_edges_from((("e", "h"), ("h", "x"), ("p", "r"), ("s", "q")))
    return graph


TERMINAL_MODELS = {
    "b": (("a", "p", "q", "r"), ("b",), ("c", "f", "s"), ("d",), ("e",), ("g",), ("x", "h")),
    "d": (("a", "x", "p", "r"), ("b",), ("c", "s"), ("d", "q"), ("e",), ("f",), ("g", "h")),
    "f": (("a", "d", "p", "r"), ("b",), ("c", "s"), ("e",), ("f", "q"), ("g",), ("x", "h")),
    "h": (("a", "p", "r"), ("b", "x"), ("c", "s"), ("d", "g"), ("e",), ("f",), ("h", "q")),
    "p": (("a", "d", "r"), ("b",), ("c", "s"), ("e",), ("f", "p"), ("g", "q"), ("x", "h")),
}


FINAL_BAGS = {
    "X": frozenset(("q", "x", "u_x", "u_e")),
    "A": frozenset(("a", "p", "r", "s", "c")),
    "B": frozenset(("b",)),
    "D": frozenset(("d",)),
    "E": frozenset(("e",)),
    "F": frozenset(("f", "h")),
    "G": frozenset(("g",)),
}


FINAL_CONTACTS = {
    ("X", "A"): ("q", "s"),
    ("X", "B"): ("x", "b"),
    ("X", "D"): ("x", "d"),
    ("X", "E"): ("u_e", "e"),
    ("X", "F"): ("x", "h"),
    ("X", "G"): ("q", "g"),
    ("A", "B"): ("c", "b"),
    ("A", "D"): ("a", "d"),
    ("A", "E"): ("a", "e"),
    ("A", "F"): ("p", "f"),
    ("A", "G"): ("c", "g"),
    ("B", "D"): ("b", "d"),
    ("B", "E"): ("b", "e"),
    ("B", "F"): ("b", "f"),
    ("B", "G"): ("b", "g"),
    ("D", "E"): ("d", "e"),
    ("D", "F"): ("d", "f"),
    ("D", "G"): ("d", "g"),
    ("E", "F"): ("e", "f"),
    ("E", "G"): ("e", "g"),
    ("F", "G"): ("h", "g"),
}


def validate_model(graph: nx.Graph, raw_bags: tuple[tuple[str, ...], ...]) -> None:
    bags = tuple(frozenset(bag) for bag in raw_bags)
    assert len(bags) == 7 and all(bags)
    assert set().union(*bags) == set(graph)
    assert sum(map(len, bags)) == len(graph)
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
    assert all(
        any(graph.has_edge(left, right) for left in first for right in second)
        for first, second in combinations(bags, 2)
    )


def validate_final_model(graph: nx.Graph) -> None:
    labels = tuple(FINAL_BAGS)
    bags = tuple(FINAL_BAGS.values())
    assert set(FINAL_CONTACTS) == set(combinations(labels, 2))
    assert set().union(*bags) == set(graph)
    assert sum(map(len, bags)) == len(graph)
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
    for (first, second), (left, right) in FINAL_CONTACTS.items():
        assert graph.has_edge(left, right)
        assert (
            left in FINAL_BAGS[first] and right in FINAL_BAGS[second]
        ) or (
            right in FINAL_BAGS[first] and left in FINAL_BAGS[second]
        )


def main() -> None:
    core = build_core()
    assert tuple(core) == VERTICES
    assert len(core) == 13 and core.number_of_edges() == 32
    assert set(core["q"]) == {"a", "g", "s"}
    assert set(TERMINAL_MODELS) == {"b", "d", "f", "h", "p"}

    for endpoint, bags in TERMINAL_MODELS.items():
        assert not core.has_edge("q", endpoint)
        augmented = core.copy()
        augmented.add_edge("q", endpoint)
        validate_model(augmented, bags)

    fan_graph = core.copy()
    fan_graph.add_edges_from(
        (("q", "u_x"), ("u_x", "x"), ("q", "u_e"), ("u_e", "e"))
    )
    validate_final_model(fan_graph)

    print("GREEN exact two-path atomic-core seven-fan closure")
    print("core: vertices=13 edges=32 q_neighbours=a,g,s")
    print("terminal_endpoints: b,d,f,h,p; five K7 models verified")
    print("forced_fan_endpoints: a,c,e,g,r,s,x")
    print("final_model: seven branch sets and 21 named contacts verified")


if __name__ == "__main__":
    main()
