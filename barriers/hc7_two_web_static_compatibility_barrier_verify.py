#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["networkx==3.6.1"]
# ///
"""Verify the static two-web barriers and the direct-link census."""

from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path

import networkx as nx


ROOT = Path(__file__).resolve().parents[1]
CLASSIFIER_PATH = (
    ROOT / "results" / "hc7_disjoint_k6minus_support6_linkage_classifier.py"
)
SPEC = importlib.util.spec_from_file_location("linkage_classifier", CLASSIFIER_PATH)
assert SPEC is not None and SPEC.loader is not None
CLASSIFIER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CLASSIFIER)


def mixed_bridge_graph(order: str) -> nx.Graph:
    """Return G_34 or G_43 from Section 2 of the barrier note."""

    graph = CLASSIFIER.base_graph("3+1", (3, 4))
    graph.remove_edges_from(((5, 9), (3, 10), (4, 11)))
    graph.add_edges_from(
        (
            (5, 12),
            (12, 13),
            (13, 9),
            (3, 14),
            (14, 10),
            (4, 15),
            (15, 11),
        )
    )
    if order == "34":
        graph.add_edges_from(((12, 14), (13, 15)))
    elif order == "43":
        graph.add_edges_from(((13, 14), (12, 15)))
    else:
        raise ValueError(order)
    return graph


def has_crossing(
    graph: nx.Graph,
    first_pair: tuple[int, int],
    second_pair: tuple[int, int],
) -> bool:
    """Test two prescribed vertex-disjoint paths by direct enumeration."""

    for first in nx.all_simple_paths(graph, *first_pair):
        first_vertices = set(first)
        for second in nx.all_simple_paths(graph, *second_pair):
            if first_vertices.isdisjoint(second):
                return True
    return False


def check_mixed_graphs() -> None:
    path_5 = {5, 12, 13, 9}
    path_3 = {3, 14, 10}
    path_4 = {4, 15, 11}
    for order in ("34", "43"):
        graph = mixed_bridge_graph(order)
        clean_3 = graph.subgraph(path_5 | path_3).copy()
        clean_4 = graph.subgraph(path_5 | path_4).copy()
        assert not has_crossing(clean_3, (5, 10), (9, 3))
        assert not has_crossing(clean_4, (5, 11), (9, 4))
        has_k7 = CLASSIFIER.exact_k7_with_low_degree_reduction(graph)
        connectivity = nx.node_connectivity(graph)
        assert not has_k7
        assert connectivity == 3
        print(
            f"mixed_order_{order}",
            "vertices",
            len(graph),
            "edges",
            graph.number_of_edges(),
            "connectivity",
            connectivity,
            "k7_minor",
            has_k7,
        )


def direct_link_census() -> None:
    base = CLASSIFIER.base_graph("3+1", (3, 4))
    missing = [
        edge
        for edge in itertools.combinations(range(12), 2)
        if not base.has_edge(*edge)
    ]
    indexed_edges = dict(enumerate(missing))
    edge_index = {edge: index for index, edge in indexed_edges.items()}
    crossing_pairs = (
        (edge_index[(5, 10)], edge_index[(3, 9)]),
        (edge_index[(5, 11)], edge_index[(4, 9)]),
    )
    incident = {
        vertex: [
            index for index, edge in indexed_edges.items() if vertex in edge
        ]
        for vertex in range(12)
    }

    seen: set[int] = set()
    k7_cache: dict[int, bool] = {}
    recursive_calls = 0

    def violates_crossing(mask: int) -> bool:
        return any(
            mask >> first & 1 and mask >> second & 1
            for first, second in crossing_pairs
        )

    def graph_from_mask(mask: int) -> nx.Graph:
        graph = base.copy()
        graph.add_edges_from(
            indexed_edges[index]
            for index in range(len(missing))
            if mask >> index & 1
        )
        return graph

    def has_k7(mask: int) -> bool:
        if mask not in k7_cache:
            k7_cache[mask] = CLASSIFIER.exact_k7_at_most_twelve(
                graph_from_mask(mask)
            )
        return k7_cache[mask]

    def search(mask: int) -> int | None:
        nonlocal recursive_calls
        recursive_calls += 1
        if mask in seen:
            return None
        seen.add(mask)
        if violates_crossing(mask) or has_k7(mask):
            return None

        graph = graph_from_mask(mask)
        deficient = [
            (7 - graph.degree(vertex), vertex)
            for vertex in graph
            if graph.degree(vertex) < 7
        ]
        if not deficient:
            return mask

        deficit, vertex = max(deficient)
        available = [
            index
            for index in incident[vertex]
            if not (mask >> index & 1)
            and not violates_crossing(mask | (1 << index))
        ]
        if len(available) < deficit:
            return None

        combinations = list(itertools.combinations(available, deficit))
        combinations.sort(
            key=lambda choice: -sum(
                max(
                    0,
                    7
                    - graph.degree(
                        indexed_edges[index][0]
                        + indexed_edges[index][1]
                        - vertex
                    ),
                )
                for index in choice
            )
        )
        for choice in combinations:
            extension = mask
            for index in choice:
                extension |= 1 << index
            answer = search(extension)
            if answer is not None:
                return answer
        return None

    answer = search(0)
    assert answer is None
    assert len(seen) == 4_633
    assert recursive_calls == 4_679
    assert len(k7_cache) == len(seen)
    print("direct_link_states", len(seen))
    print("direct_link_recursive_calls", recursive_calls)
    print("direct_link_minimum_degree_seven_completion", False)


def main() -> None:
    check_mixed_graphs()
    direct_link_census()
    print("GREEN: static two-web barriers and direct-link census verified")


if __name__ == "__main__":
    main()
