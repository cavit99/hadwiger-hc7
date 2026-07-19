#!/usr/bin/env python3
"""Verify the exact seven-vertex boundary census in the singleton mode.

Run with the repository's pinned NetworkX runtime, for example

    PYTHONPATH=active/runtime/deps python3 \
        results/hc7_singleton_exact7_boundary_census.py

The test is finite.  It does not assert that any listed boundary is
realizable in a hypothetical counterexample.
"""

from __future__ import annotations

import networkx as nx


EXPECTED = (
    "FKdbG", "Fms`G", "Fm{`G", "FhNHo", "F{cZG",
    "FhffG", "FQT|o", "FpLYw", "FL~Cg", "Ffwhg",
    "F`urg", "FK|ko", "FN^Sg", "FJe~O", "Floxw",
    "Fb]lg", "Feg~w", "F{e}o", "FzM]W", "FtTnw",
)


def adjacency_tuple(graph: nx.Graph) -> tuple[int, ...]:
    return tuple(
        sum(1 << neighbour for neighbour in graph.neighbors(vertex))
        for vertex in range(len(graph))
    )


def induced(adjacency: tuple[int, ...], keep: tuple[int, ...]) -> tuple[int, ...]:
    position = {vertex: index for index, vertex in enumerate(keep)}
    result = [0] * len(keep)
    for index, vertex in enumerate(keep):
        for neighbour in keep:
            if adjacency[vertex] >> neighbour & 1:
                result[index] |= 1 << position[neighbour]
    return tuple(result)


def contract(adjacency: tuple[int, ...], left: int, right: int) -> tuple[int, ...]:
    if left > right:
        left, right = right, left
    keep = [vertex for vertex in range(len(adjacency)) if vertex != right]
    position = {vertex: index for index, vertex in enumerate(keep)}
    result = [0] * len(keep)
    for old_i, first in enumerate(keep):
        for old_j in range(old_i + 1, len(keep)):
            second = keep[old_j]
            edge = bool(adjacency[first] >> second & 1)
            if first == left:
                edge |= bool(adjacency[right] >> second & 1)
            if second == left:
                edge |= bool(adjacency[first] >> right & 1)
            if edge:
                new_i, new_j = position[first], position[second]
                result[new_i] |= 1 << new_j
                result[new_j] |= 1 << new_i
    return tuple(result)


def has_clique_minor(graph: nx.Graph, target: int) -> bool:
    seen: set[tuple[int, ...]] = set()

    def search(adjacency: tuple[int, ...]) -> bool:
        order = len(adjacency)
        if order < target:
            return False
        if order == target:
            return all(mask.bit_count() == target - 1 for mask in adjacency)
        if adjacency in seen:
            return False
        seen.add(adjacency)
        for vertex in range(order):
            keep = tuple(x for x in range(order) if x != vertex)
            if search(induced(adjacency, keep)):
                return True
        for left in range(order):
            for right in range(left + 1, order):
                if adjacency[left] >> right & 1:
                    if search(contract(adjacency, left, right)):
                        return True
        return False

    return search(adjacency_tuple(graph))


def join_independent_pair(boundary: nx.Graph) -> nx.Graph:
    graph = boundary.copy()
    p, q = 7, 8
    graph.add_nodes_from((p, q))
    graph.add_edges_from((x, s) for x in (p, q) for s in range(7))
    return graph


def independence_number(graph: nx.Graph) -> int:
    return max(len(clique) for clique in nx.find_cliques(nx.complement(graph)))


def eligible(boundary: nx.Graph) -> bool:
    complement = nx.complement(boundary)
    nonisolated = [v for v in complement if complement.degree(v)]
    core = complement.subgraph(nonisolated)
    return (
        independence_number(boundary) <= 2
        and len(nx.max_weight_matching(complement, maxcardinality=True)) >= 3
        and not has_clique_minor(join_independent_pair(boundary), 7)
        and len(nonisolated) >= 6
        and nx.is_connected(core)
        and nx.is_biconnected(core)
        and min(dict(core.degree()).values()) >= 2
    )


def standard_moser() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(range(7))
    graph.add_edges_from(
        ((0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
         (2, 6), (3, 4), (3, 5), (4, 5), (5, 6))
    )
    return graph


def main() -> None:
    survivors = [
        nx.convert_node_labels_to_integers(graph)
        for graph in nx.graph_atlas_g()
        if len(graph) == 7
        and eligible(nx.convert_node_labels_to_integers(graph))
    ]
    codes = tuple(
        nx.to_graph6_bytes(graph, header=False).decode().strip()
        for graph in survivors
    )
    assert codes == EXPECTED, (codes, EXPECTED)

    exceptional = []
    degree_two = []
    for boundary in survivors:
        complement = nx.complement(boundary)
        core = complement.subgraph(
            [v for v in complement if complement.degree(v)]
        )
        if min(dict(core.degree()).values()) == 2:
            degree_two.append(boundary)
        else:
            exceptional.append(complement)

    assert len(degree_two) == 18
    assert len(exceptional) == 2
    assert any(nx.is_isomorphic(graph, nx.complete_bipartite_graph(3, 4))
               for graph in exceptional)
    k33_plus_isolate = nx.disjoint_union(
        nx.complete_bipartite_graph(3, 3), nx.empty_graph(1)
    )
    assert any(nx.is_isomorphic(graph, k33_plus_isolate)
               for graph in exceptional)

    moser = standard_moser()
    moser_plus = moser.copy()
    moser_plus.add_edge(1, 3)
    assert any(nx.is_isomorphic(graph, moser) for graph in survivors)
    assert any(nx.is_isomorphic(graph, moser_plus) for graph in survivors)

    print(
        "VERIFIED singleton_exact7_boundary_types=20 "
        "degree_two_complement=18 exceptional=2 "
        "moser_types=2_not_exhaustive"
    )


if __name__ == "__main__":
    main()
