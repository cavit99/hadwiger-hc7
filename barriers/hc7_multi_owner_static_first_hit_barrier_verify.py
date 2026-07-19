#!/usr/bin/env python3
"""Verify the static two-owner first-hit barrier.

Run from the repository root with

    PYTHONPATH=active/runtime/deps python3 \
        barriers/hc7_multi_owner_static_first_hit_barrier_verify.py
"""

from __future__ import annotations

from itertools import combinations, product

import networkx as nx


LABELS = ("X", "Y", "D", "U", "F", "P", "Q")
INDEX = {label: index for index, label in enumerate(LABELS)}


def dual_truncated_icosahedron() -> nx.Graph:
    """Return the deterministic 32-vertex planar triangulation."""

    icosahedron = nx.icosahedral_graph()
    faces = sorted(
        tuple(sorted(clique))
        for clique in nx.enumerate_all_cliques(icosahedron)
        if len(clique) == 3
    )
    assert len(faces) == 20

    graph = nx.Graph()
    graph.add_nodes_from(range(32))
    for face_vertex, face in enumerate(faces, 12):
        graph.add_edges_from((face_vertex, vertex) for vertex in face)
    for (left, face_left), (right, face_right) in combinations(
        list(enumerate(faces, 12)), 2
    ):
        if len(set(face_left) & set(face_right)) == 2:
            graph.add_edge(left, right)

    return graph


def host_graph() -> tuple[nx.Graph, nx.Graph]:
    """Return the planar factor and its join with an edge."""

    planar = dual_truncated_icosahedron()
    host = planar.copy()
    host.add_edge("p", "q")
    for vertex in planar:
        host.add_edge("p", vertex)
        host.add_edge("q", vertex)
    return planar, host


def adjacent(graph: nx.Graph, left: set, right: set) -> bool:
    """Return whether two disjoint vertex sets have a host edge."""

    return any(graph.has_edge(u, v) for u in left for v in right)


def model_is_compatible(graph: nx.Graph, bags: list[set]) -> bool:
    """Check the labelled model with only X--Y allowed to be absent."""

    if any(not bag or not nx.is_connected(graph.subgraph(bag)) for bag in bags):
        return False
    if set().union(*bags) != set(graph):
        return False
    if sum(len(bag) for bag in bags) != len(graph):
        return False
    for left, right in combinations(range(7), 2):
        if (left, right) == (INDEX["X"], INDEX["Y"]):
            continue
        if not adjacent(graph, bags[left], bags[right]):
            return False
    return True


def four_colouring(graph: nx.Graph) -> dict | None:
    """Find a deterministic proper four-colouring by DSATUR backtracking."""

    colours: dict = {}

    def search() -> bool:
        if len(colours) == len(graph):
            return True
        uncoloured = [vertex for vertex in graph if vertex not in colours]
        vertex = max(
            uncoloured,
            key=lambda item: (
                len({colours[n] for n in graph[item] if n in colours}),
                graph.degree(item),
                -int(item),
            ),
        )
        forbidden = {colours[n] for n in graph[vertex] if n in colours}
        for colour in range(4):
            if colour in forbidden:
                continue
            colours[vertex] = colour
            if search():
                return True
            del colours[vertex]
        return False

    return colours if search() else None


def full_neighbourhood(graph: nx.Graph, vertices: set) -> set:
    """Return the open full neighbourhood of a vertex set."""

    return set().union(*(set(graph[vertex]) for vertex in vertices)) - vertices


def main() -> None:
    planar, graph = host_graph()

    assert (len(planar), planar.number_of_edges()) == (32, 90)
    assert nx.check_planarity(planar)[0]
    assert nx.node_connectivity(planar) == 5
    assert (len(graph), graph.number_of_edges()) == (34, 155)
    assert nx.node_connectivity(graph) == 7

    colouring = four_colouring(planar)
    assert colouring is not None
    assert all(colouring[u] != colouring[v] for u, v in planar.edges())

    fixed = {0, 11, 12, 13, 14, 16}
    bags = [
        {11},
        {0},
        set(planar) - fixed,
        {12, 13, 14},
        {16},
        {"p"},
        {"q"},
    ]
    assert model_is_compatible(graph, bags)
    assert not adjacent(graph, bags[INDEX["X"]], bags[INDEX["Y"]])

    response = bags[INDEX["D"]]
    assert nx.is_connected(graph.subgraph(response))
    assert graph.has_edge(8, 13)
    assert graph.has_edge(19, 12)

    side = {12, 14}
    remainder = {13}
    assert nx.is_connected(graph.subgraph(side))
    assert nx.is_connected(graph.subgraph(remainder))
    assert 13 not in side
    assert 12 in side and 13 in remainder
    owners = {
        label
        for label in ("X", "Y", "F", "P", "Q")
        if not adjacent(graph, remainder, bags[INDEX[label]])
    }
    assert owners == {"X", "F"}
    assert adjacent(graph, side, bags[INDEX["X"]])
    assert adjacent(graph, side, bags[INDEX["F"]])

    rank_witness = {
        "X": (27, 11),
        "Y": (15, 0),
        "U": (1, 12),
        "F": (7, 16),
        "P": (2, "p"),
        "Q": (3, "q"),
    }
    assert len({edge[0] for edge in rank_witness.values()}) == 6
    assert len({edge[1] for edge in rank_witness.values()}) == 6
    for label, (port, terminal) in rank_witness.items():
        assert port in response
        assert terminal in bags[INDEX[label]]
        assert graph.has_edge(port, terminal)
    relaxed_rank = len(rank_witness)
    assert relaxed_rank == 6 == len(rank_witness)

    # The fixed response subgraph and the six prescribed roots leave only
    # vertices 12 and 14 free to change labels.  Check every assignment.
    compatible_assignments = []
    for assignment in product(range(7), repeat=2):
        candidate = [set(bag) - {12, 14} for bag in bags]
        for vertex, label_index in zip((12, 14), assignment):
            candidate[label_index].add(vertex)
        if model_is_compatible(graph, candidate):
            compatible_assignments.append(assignment)
    assert compatible_assignments == [(INDEX["U"], INDEX["U"])]

    neighbourhood_orders = {}
    branch_u = bags[INDEX["U"]]
    for size in range(1, len(branch_u) + 1):
        for choice in combinations(sorted(branch_u), size):
            connected_set = set(choice)
            if nx.is_connected(graph.subgraph(connected_set)):
                neighbourhood_orders[tuple(choice)] = len(
                    full_neighbourhood(graph, connected_set)
                )
    assert neighbourhood_orders == {
        (12,): 8,
        (13,): 8,
        (14,): 8,
        (12, 13): 10,
        (12, 14): 10,
        (12, 13, 14): 12,
    }
    assert 7 not in neighbourhood_orders.values()

    # The example is six-colourable and has unrelated order-seven cuts.
    host_colouring = dict(colouring)
    host_colouring.update({"p": 4, "q": 5})
    assert all(host_colouring[u] != host_colouring[v] for u, v in graph.edges())
    assert planar.degree(0) == 5 and graph.degree(0) == 7
    separator = set(graph[0])
    remainder_graph = graph.copy()
    remainder_graph.remove_nodes_from(separator)
    assert nx.number_connected_components(remainder_graph) >= 2

    print(
        "GREEN multi-owner static first-hit barrier: "
        "kappa=7, lambda=6, minimum U and local boundary orders verified"
    )


if __name__ == "__main__":
    main()
