#!/usr/bin/env python3
"""Exhaustively verify the locked two-row full-shell barrier."""

from __future__ import annotations

import itertools

import networkx as nx


FOREIGN = ("D", "E", "U1", "U2", "U3", "U4")


def shell() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(FOREIGN)
    graph.add_edges_from(itertools.combinations(FOREIGN, 2))
    graph.add_edges_from(
        [
            ("pL", "pR"),
            ("pL", "U1"),
            ("pL", "U2"),
            ("pR", "U3"),
            ("pR", "U4"),
            ("pL", "E"),
            ("pR", "E"),
            ("l", "q"),
            ("q", "r"),
            ("r", "h"),
            ("pL", "l"),
            ("pR", "r"),
            ("q", "U1"),
            ("h", "U3"),
            ("s2", "pL"),
            ("s2", "pR"),
            ("s2", "U2"),
            ("s4", "pL"),
            ("s4", "pR"),
            ("s4", "U4"),
        ]
    )
    return graph


def exact_k7_model(graph: nx.Graph) -> list[list[str]] | None:
    vertices = list(graph)
    index = {vertex: i for i, vertex in enumerate(vertices)}
    max_bag = len(vertices) - 6
    members: dict[int, list[str]] = {}
    candidates: list[int] = []

    for mask in range(1, 1 << len(vertices)):
        if mask.bit_count() > max_bag:
            continue
        subset = [
            vertices[i] for i in range(len(vertices)) if mask >> i & 1
        ]
        if nx.is_connected(graph.subgraph(subset)):
            candidates.append(mask)
            members[mask] = subset

    assert len(candidates) == 5946
    neighbourhood: dict[int, int] = {}
    for mask, subset in members.items():
        value = 0
        for vertex in subset:
            for neighbour in graph[vertex]:
                value |= 1 << index[neighbour]
        neighbourhood[mask] = value & ~mask

    # Popping tries small bags first.  Filtering the remaining prefix
    # enumerates every compatible seven-set exactly through one ordering.
    candidates.sort(key=lambda mask: -mask.bit_count())

    def search(chosen: list[int], available: list[int]) -> list[int] | None:
        if len(chosen) == 7:
            return chosen
        while len(chosen) + len(available) >= 7:
            candidate = available.pop()
            compatible = [
                other
                for other in available
                if not candidate & other
                and neighbourhood[candidate] & other
            ]
            result = search([*chosen, candidate], compatible)
            if result is not None:
                return result
        return None

    model = search([], candidates)
    return None if model is None else [members[mask] for mask in model]


def verify_labelled_model(graph: nx.Graph, augmented: bool) -> None:
    carrier = {"pL", "pR", "l", "q", "r", "h", "s2", "s4"}
    d_bag = {"D"}
    if augmented:
        d_bag |= {"a1", "a2", "b0", "b1", "b2", "c0", "c1", "c2"}
    bags = {
        "A": carrier,
        "D": d_bag,
        "E": {"E"},
        "U1": {"U1"},
        "U2": {"U2"},
        "U3": {"U3"},
        "U4": {"U4"},
    }
    assert set().union(*bags.values()) == set(graph)
    assert sum(map(len, bags.values())) == len(graph)
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags.values())
    assert all(
        any(graph.has_edge(u, v) for u in bags[x] for v in bags[y])
        for x, y in itertools.combinations(FOREIGN, 2)
    )
    assert all(
        any(graph.has_edge(u, v) for u in bags["A"] for v in bags[row])
        for row in ("E", "U1", "U2", "U3", "U4")
    )
    assert not any(
        graph.has_edge(u, v) for u in bags["A"] for v in bags["D"]
    )


def augmented() -> nx.Graph:
    graph = shell()
    parts = (
        ("D", "a1", "a2"),
        ("b0", "b1", "b2"),
        ("c0", "c1", "c2"),
    )
    graph.add_nodes_from(set().union(*map(set, parts)))
    for first, second in itertools.combinations(parts, 2):
        graph.add_edges_from(itertools.product(first, second))
    return graph


def main() -> None:
    base = shell()
    verify_labelled_model(base, augmented=False)
    assert exact_k7_model(base) is None

    # Exact Hall-deficient supports and alternating linkage failure.
    assert set(base["q"]) & set(FOREIGN) == {"U1"}
    assert set(base["h"]) & set(FOREIGN) == {"U3"}
    carrier = base.subgraph(("l", "q", "r", "h"))
    assert nx.shortest_path(carrier, "l", "h") == ["l", "q", "r", "h"]
    assert nx.shortest_path(carrier, "r", "q") == ["r", "q"]

    graph = augmented()
    verify_labelled_model(graph, augmented=True)
    assert nx.node_connectivity(graph) == 1
    assert not any(
        nx.check_planarity(graph.subgraph(set(graph) - set(pair)))[0]
        for pair in itertools.combinations(graph, 2)
    )

    print("GREEN: locked two-row shell has no K7 model")
    print("5946 connected branch-bag candidates exhausted")
    print("augmented one-sum is K7-free by proof and is non-two-apex")


if __name__ == "__main__":
    main()
