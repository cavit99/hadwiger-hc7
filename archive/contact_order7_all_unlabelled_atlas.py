#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["networkx"]
# ///
"""Atlas the unlabelled order-seven boundaries surviving two full shores.

For each seven-vertex graph J, add two nonadjacent vertices complete to J
and test for a K7 minor using the existing exact nine-vertex verifier.  The
report groups the quotient-negative boundaries by their missing graph and
marks the split graphs already excluded by the exact-block theorem.
"""

from __future__ import annotations

from collections import Counter, defaultdict

import networkx as nx

from contact_order7_five_edge_verify import as_sets, k_minor_model, verify_model


def quotient_edges(boundary: nx.Graph) -> set[tuple[int, int]]:
    edges = {tuple(sorted(edge)) for edge in boundary.edges()}
    edges.update((root, helper) for root in range(7) for helper in (7, 8))
    return {tuple(sorted(edge)) for edge in edges}


def is_split(graph: nx.Graph) -> bool:
    forbidden_edges = {
        (4, (1, 1, 1, 1)),  # 2K2 or C4 distinguished below by edge count.
        (5, (2, 2, 2, 2, 2)),
    }
    for size in (4, 5):
        for vertices in __import__("itertools").combinations(graph.nodes(), size):
            subgraph = graph.subgraph(vertices)
            degrees = tuple(sorted(dict(subgraph.degree()).values()))
            edges = subgraph.number_of_edges()
            if size == 4 and ((edges == 2 and degrees == (1, 1, 1, 1)) or
                              (edges == 4 and degrees == (2, 2, 2, 2))):
                return False
            if (size, degrees) in forbidden_edges and size == 5 and edges == 5:
                return False
    return True


def signature(graph: nx.Graph) -> tuple[object, ...]:
    components = sorted((len(component) for component in nx.connected_components(graph)), reverse=True)
    return (
        graph.number_of_edges(),
        tuple(sorted(dict(graph.degree()).values(), reverse=True)),
        tuple(components),
        nx.node_connectivity(graph) if nx.is_connected(graph) and len(graph) > 1 else 0,
        nx.is_bipartite(graph),
    )


def main() -> None:
    failures: list[tuple[nx.Graph, nx.Graph]] = []
    for raw in nx.graph_atlas_g():
        if raw.number_of_nodes() != 7:
            continue
        boundary = nx.convert_node_labels_to_integers(raw)
        edges = quotient_edges(boundary)
        model = k_minor_model(edges)
        if model is not None:
            verify_model(edges, as_sets(model))
            continue
        missing = nx.complement(boundary)
        failures.append((boundary, missing))

    by_missing_edges = Counter(missing.number_of_edges() for _, missing in failures)
    nonsplit = [(boundary, missing) for boundary, missing in failures if not is_split(missing)]
    nonsplit_by_edges = Counter(missing.number_of_edges() for _, missing in nonsplit)
    nonsplit_signatures: dict[int, Counter[tuple[object, ...]]] = defaultdict(Counter)
    for _, missing in nonsplit:
        nonsplit_signatures[missing.number_of_edges()][signature(missing)] += 1

    print("quotient_negative_unlabelled", len(failures))
    print("by_missing_edges", sorted(by_missing_edges.items()))
    print("nonsplit_negative", len(nonsplit))
    print("nonsplit_by_missing_edges", sorted(nonsplit_by_edges.items()))
    for edge_count in sorted(nonsplit_signatures):
        print("EDGE_COUNT", edge_count, "types", sum(nonsplit_signatures[edge_count].values()))
        for item, multiplicity in sorted(nonsplit_signatures[edge_count].items()):
            print(" ", multiplicity, item)


if __name__ == "__main__":
    main()
