#!/usr/bin/env python3
"""Sharp local obstruction to adding the omitted fifth-colour bag."""

from __future__ import annotations

from itertools import combinations

import networkx as nx

from contact_order7_sixedge_web_probe import generic_minor_model


def build_graph() -> nx.Graph:
    # Society S={0,1}; four-colour K4 roots 2,...,5; beta portals 6,...,9.
    graph = nx.Graph()
    graph.add_edge(0, 1)
    graph.add_edges_from(
        (i, j) for i in range(2, 6) for j in range(i + 1, 6)
    )
    for vertex in range(2, 10):
        graph.add_edge(0, vertex)
        graph.add_edge(1, vertex)
    for i in range(4):
        graph.add_edge(2 + i, 6 + i)
    return graph


def edge_set(graph: nx.Graph) -> set[tuple[int, int]]:
    return {tuple(sorted(edge)) for edge in graph.edges()}


def main() -> None:
    graph = build_graph()
    society = {0, 1}
    roots = {2, 3, 4, 5}
    beta = {6, 7, 8, 9}

    assert nx.is_connected(graph.subgraph(society))
    assert nx.is_bipartite(graph.subgraph(society))
    # Every outside vertex completes a triangle with the society edge, so
    # no proper superset induces a bipartite graph.
    assert all(graph.has_edge(0, v) and graph.has_edge(1, v) for v in graph if v not in society)
    assert all(
        not nx.is_bipartite(graph.subgraph(society | set(extra)))
        for size in range(1, 9)
        for extra in combinations(set(graph) - society, size)
    )

    quotient = nx.contracted_nodes(graph, 0, 1, self_loops=False, copy=True)
    colour = {0: 0, **{2 + i: 1 + i for i in range(4)}, **{6 + i: 5 for i in range(4)}}
    assert all(colour[u] != colour[v] for u, v in quotient.edges())
    assert set(colour) == set(quotient)

    assert nx.is_isomorphic(graph.subgraph(roots), nx.complete_graph(4))

    # For each gamma colour, the unique mixed beta/gamma portal component
    # is the edge y_i x_i.  No beta portal is mixed with two gamma colours.
    for i in range(4):
        gamma_root = 2 + i
        two_colour = quotient.subgraph(beta | {gamma_root})
        mixed = [
            component
            for component in nx.connected_components(two_colour)
            if component & beta and gamma_root in component
        ]
        assert mixed == [{gamma_root, 6 + i}]
    assert all(
        sum(graph.has_edge(y, x) for x in roots) == 1 for y in beta
    )

    outside = nx.convert_node_labels_to_integers(graph.subgraph(set(graph) - society))
    assert generic_minor_model(len(outside), edge_set(outside), 5) is None
    assert generic_minor_model(len(graph), edge_set(graph), 7) is None

    # The singleton K4 bags are the rooted model.  Every component outside
    # their union is one beta vertex and attaches to exactly one bag.
    remainder = graph.subgraph(set(graph) - society - roots)
    assert all(len(component) == 1 for component in nx.connected_components(remainder))
    for component in nx.connected_components(remainder):
        vertex = next(iter(component))
        assert sum(graph.has_edge(vertex, root) for root in roots) == 1

    # The example deliberately is six-colourable; it falsifies the local
    # fifth-bag inference, not the additional minor-critical HC7 hypothesis.
    six_colour = {
        0: 0,
        1: 1,
        **{2 + i: 2 + i for i in range(4)},
        **{6 + i: 2 + ((i + 1) % 4) for i in range(4)},
    }
    assert all(six_colour[u] != six_colour[v] for u, v in graph.edges())

    print("maximal society local obstruction verified")
    print("vertices", len(graph), "edges", graph.number_of_edges())
    print("K7 minor", False, "outside K5 minor", False)
    print("beta-to-root attachments", tuple((6 + i, 2 + i) for i in range(4)))


if __name__ == "__main__":
    main()
