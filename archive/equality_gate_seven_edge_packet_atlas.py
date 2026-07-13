#!/usr/bin/env python3
"""Certificate atlas for the nonsplit seven-missing-edge equality layer.

This is not a raw list-only search.  It verifies three structural filters:

1. full-split cyclic-hull closure;
2. the repeated-root compatibility graph; and
3. a matching-triangle packet certificate in each final residual.
"""

from __future__ import annotations

from itertools import combinations

import networkx as nx

from contact_order7_all_unlabelled_atlas import is_split, quotient_edges
from contact_order7_five_edge_verify import k_minor_model
from equality_gate_repeated_root_verify import (
    covering_rows,
    cyclic_hulls,
    k7_model,
    split_quotient,
)
from order7_induced_core_direct_atlas import split_crossing_forces


S = tuple(range(7))
PAIRS = set(combinations(S, 2))


DIRECT_WITNESSES = {
    3: (0, 3, 1, 4),
    4: (0, 1, 4, 2),
    5: (0, 2, 4, 3),
    6: (2, 3, 4, 5),
    12: (1, 3, 2, 6),
    13: (0, 1, 3, 2),
    14: (1, 3, 2, 6),
    15: (0, 1, 3, 2),
    17: (2, 5, 3, 6),
    18: (0, 2, 1, 3),
    19: (0, 2, 1, 6),
    21: (1, 2, 3, 5),
    23: (0, 3, 2, 6),
    24: (0, 2, 1, 5),
    25: (3, 4, 6, 5),
    26: (1, 2, 3, 5),
    27: (0, 2, 5, 3),
    28: (0, 5, 3, 6),
}

NONBIPARTITE_COMPATIBILITY = {1, 2, 6, 15, 20}
FINAL_RESIDUAL = {0, 7, 8, 9, 10, 11, 16, 22, 29, 30}

FULL_PACKET_TRIANGLES = {
    7: ((0, 3), (1, 2), (4, 5)),
    8: ((0, 1), (2, 3), (4, 5)),
    9: ((1, 2), (3, 6), (4, 5)),
    10: ((1, 2), (3, 6), (4, 5)),
    11: ((1, 2), (3, 4), (5, 6)),
    16: ((0, 1), (2, 3), (5, 6)),
    29: ((0, 1), (2, 3), (4, 5)),
}

CENTER_LOCKED_TRIANGLES = {
    # Value is (matching, unique carrier which may be the connector-tree centre).
    22: (((0, 1), (2, 3), (4, 5)), (4, 5)),
    30: (((0, 1), (2, 3), (5, 6)), (0, 1)),
}

EXPECTED_RESIDUAL_MANIFEST = {
    0: ("FwJG?", ((0, 1), (0, 2), (0, 5), (1, 2), (1, 5), (2, 4), (4, 5))),
    7: ("F[JG?", ((0, 2), (0, 3), (0, 5), (1, 2), (1, 5), (2, 4), (4, 5))),
    8: ("FhoW?", ((0, 1), (0, 4), (1, 2), (1, 4), (2, 3), (3, 5), (4, 5))),
    9: ("FHHGg", ((1, 2), (1, 5), (2, 3), (2, 4), (3, 6), (4, 5), (5, 6))),
    10: ("FHOgg", ((1, 2), (1, 4), (2, 3), (2, 5), (3, 6), (4, 5), (5, 6))),
    11: ("FIS`G", ((1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 4), (5, 6))),
    16: ("Fpq?G", ((0, 1), (0, 2), (0, 4), (0, 5), (1, 4), (2, 3), (5, 6))),
    22: ("Fh_gG", ((0, 1), (0, 4), (1, 2), (2, 3), (2, 5), (4, 5), (5, 6))),
    29: ("FhCKG", ((0, 1), (0, 6), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6))),
    30: ("F`o_g", ((0, 1), (0, 4), (1, 4), (2, 3), (2, 5), (3, 6), (5, 6))),
}


def seven_edge_types():
    answer = []
    for raw in nx.graph_atlas_g():
        if len(raw) != 7:
            continue
        missing = nx.convert_node_labels_to_integers(raw)
        if missing.number_of_edges() != 7 or is_split(missing):
            continue
        boundary = nx.complement(missing)
        if k_minor_model(quotient_edges(boundary)) is None:
            answer.append(missing)
    assert len(answer) == 31
    return tuple(answer)


def missing_edges(graph):
    return {tuple(sorted(edge)) for edge in graph.edges()}


def verify_model(order, edges, model):
    """Replay a returned bit-mask model independently of the search."""
    assert model is not None and len(model) == 7
    bags = [
        {vertex for vertex in range(order) if mask >> vertex & 1}
        for mask in model
    ]
    assert all(bags)
    assert all(bags[i].isdisjoint(bags[j]) for i in range(7) for j in range(i))
    edges = {tuple(sorted(edge)) for edge in edges}
    for bag in bags:
        reached = {next(iter(bag))}
        while True:
            expanded = reached | {
                y
                for x in reached
                for y in bag
                if tuple(sorted((x, y))) in edges
            }
            if expanded == reached:
                break
            reached = expanded
        assert reached == bag
    assert all(
        any(tuple(sorted((x, y))) in edges for x in bags[i] for y in bags[j])
        for i in range(7)
        for j in range(i)
    )


def compatibility_graph(missing):
    edges = missing_edges(missing)
    labels = tuple(vertex for vertex in S if missing.degree(vertex) >= 2)
    graph = nx.Graph()
    graph.add_nodes_from(labels)
    for pair in combinations(labels, 2):
        if all(
            k7_model(10, split_quotient(edges, *rows)) is not None
            for rows in covering_rows(pair)
        ):
            graph.add_edge(*pair)
    return graph


def packet_demands(missing):
    answer = set()
    for order in cyclic_hulls(missing):
        for i, r, j, s in combinations(range(len(order)), 4):
            first = tuple(sorted((order[i], order[j])))
            second = tuple(sorted((order[r], order[s])))
            answer.add(tuple(sorted((first, second))))
    return answer


TREES = (
    ((7, 8), (8, 9)),  # centre carrier 8
    ((7, 8), (7, 9)),  # centre carrier 7
    ((7, 9), (8, 9)),  # centre carrier 9
)


def packet_tree_models(missing, matching):
    boundary = PAIRS - missing
    results = []
    for tree in TREES:
        edges = set(boundary) | {(10, root) for root in S} | set(tree)
        for carrier, pair in zip((7, 8, 9), matching):
            edges.add((carrier, pair[0]))
            edges.add((carrier, pair[1]))
        edges = {tuple(sorted(edge)) for edge in edges}
        model = k7_model(11, edges)
        if model is not None:
            verify_model(11, edges, model)
        results.append(model)
    return tuple(results)


def verify_packet_triangle(index, missing, matching, *, locked_centre=None):
    demands = packet_demands(missing)
    triangle = tuple(tuple(sorted(pair)) for pair in combinations(matching, 2))
    assert all(demand in demands for demand in triangle)
    models = packet_tree_models(missing, matching)
    centres = (matching[1], matching[0], matching[2])
    positive_centres = {centres[i] for i, model in enumerate(models) if model is not None}
    if locked_centre is None:
        assert all(model is not None for model in models)
    else:
        assert positive_centres == set(matching) - {locked_centre}
    print(
        "packet", index,
        "matching", matching,
        "positive_centres", tuple(sorted(positive_centres)),
        "model_bags", tuple(
            None if model is None else tuple(
                tuple(vertex for vertex in range(11) if bag >> vertex & 1)
                for bag in model
            )
            for model in models
        ),
    )


def main():
    types = seven_edge_types()

    for index, order in DIRECT_WITNESSES.items():
        missing = types[index]
        assert order in cyclic_hulls(missing_edges(missing))
        boundary_edges = PAIRS - missing_edges(missing)
        certificates = split_crossing_forces(boundary_edges, order)
        assert certificates is not None
        for _, _, assignments in certificates:
            for row_x, model in assignments:
                row_x = set(row_x)
                row_y = set(S) - row_x
                edges = set(boundary_edges) | {(7, 8)}
                edges.update((9, root) for root in S)
                edges.update((7, root) for root in row_x)
                edges.update((8, root) for root in row_y)
                verify_model(10, edges, model)
    print("direct cyclic-hull closures", len(DIRECT_WITNESSES))

    nonbipartite = set()
    for index, missing in enumerate(types):
        graph = compatibility_graph(missing)
        if not nx.is_bipartite(graph):
            nonbipartite.add(index)
    assert nonbipartite == NONBIPARTITE_COMPATIBILITY
    print("nonbipartite compatibility types", tuple(sorted(nonbipartite)))

    closed = set(DIRECT_WITNESSES) | nonbipartite
    residual = set(range(len(types))) - closed
    assert residual == FINAL_RESIDUAL
    assert residual == set(EXPECTED_RESIDUAL_MANIFEST)
    assert residual == (
        {0} | set(FULL_PACKET_TRIANGLES) | set(CENTER_LOCKED_TRIANGLES)
    )
    assert set(FULL_PACKET_TRIANGLES).isdisjoint(CENTER_LOCKED_TRIANGLES)
    print("residual types", tuple(sorted(residual)))
    for index in sorted(residual):
        graph = types[index]
        code = nx.to_graph6_bytes(graph, header=False).strip().decode()
        expected_code, expected_edges = EXPECTED_RESIDUAL_MANIFEST[index]
        assert code == expected_code
        assert tuple(sorted(missing_edges(graph))) == expected_edges
        print(
            " residual", index,
            code,
            "edges", tuple(sorted(missing_edges(graph))),
        )

    for index, matching in FULL_PACKET_TRIANGLES.items():
        verify_packet_triangle(index, missing_edges(types[index]), matching)
    for index, (matching, locked) in CENTER_LOCKED_TRIANGLES.items():
        verify_packet_triangle(
            index, missing_edges(types[index]), matching, locked_centre=locked
        )

    # The last type has matching number two and a theta packet-demand graph.
    theta = types[0]
    assert len(nx.max_weight_matching(theta, maxcardinality=True)) == 2
    packet_graph = nx.Graph()
    packet_graph.add_edges_from(packet_demands(missing_edges(theta)))
    assert len(packet_graph) == 7 and packet_graph.number_of_edges() == 8
    assert sorted(dict(packet_graph.degree()).values()) == [2, 2, 2, 2, 2, 3, 3]
    assert len(nx.cycle_basis(packet_graph)) == 2
    print("rank-two theta packet graph", tuple(sorted(packet_graph.edges())))
    print("all seven-edge packet-atlas assertions verified")


if __name__ == "__main__":
    main()
