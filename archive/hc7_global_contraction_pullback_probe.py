#!/usr/bin/env python3
"""Exact counterexample to the naive global-mu contraction pullback.

For a pair R, mu(R) is the minimum support of a K5-model in G-R.  The
proposed rule was:

* if H=G/xy is seven-connected, z is not in R, and mu_H(R)>=6, then
  mu_G(R)>=7;
* if R={z,r} and mu_H(R)>=6, then one of mu_G({x,r}), mu_G({y,r}) is at
  least seven.

The deterministic counterexample is G = independent-K2 join P, where P
is the 32-vertex dual of the truncated icosahedron.  It is seven-connected
and K7-minor-free.  Contracting the displayed base edge preserves seven
connectivity, but both proposed conclusions fail at exact value six.

The support census is exhaustive through order seven.  A five-bag model
on at most seven vertices has one of the four bag-size patterns enumerated
below, so a returned value 6 is exact.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
import sys

sys.path.insert(0, "active/runtime/deps")
import networkx as nx  # noqa: E402


APEX_A = 32
APEX_B = 33


def dual_truncated_icosahedron() -> nx.Graph:
    icosahedron = nx.icosahedral_graph()
    faces = [
        tuple(clique)
        for clique in nx.enumerate_all_cliques(icosahedron)
        if len(clique) == 3
    ]
    assert len(faces) == 20

    graph = nx.Graph()
    graph.add_nodes_from(range(32))
    for face_vertex, face in enumerate(faces, 12):
        for vertex in face:
            graph.add_edge(vertex, face_vertex)
    for (left, face_left), (right, face_right) in combinations(
        list(enumerate(faces, 12)), 2
    ):
        if len(set(face_left) & set(face_right)) == 2:
            graph.add_edge(left, right)

    assert graph.number_of_edges() == 90
    assert nx.check_planarity(graph)[0]
    assert nx.node_connectivity(graph) == 5
    return graph


def add_two_apices(base: nx.Graph, *, adjacent: bool) -> nx.Graph:
    graph = base.copy()
    if adjacent:
        graph.add_edge(APEX_A, APEX_B)
    for vertex in base:
        graph.add_edge(APEX_A, vertex)
        graph.add_edge(APEX_B, vertex)
    return graph


def contract(graph: nx.Graph, edge: tuple[int, int]) -> tuple[nx.Graph, int]:
    x, y = edge
    return nx.Graph(nx.contracted_nodes(graph, x, y, self_loops=False)), x


def model_supports_through_seven(graph: nx.Graph) -> dict[int, set[int]]:
    vertices = list(graph)
    index = {vertex: offset for offset, vertex in enumerate(vertices)}
    adjacency = {vertex: set(graph[vertex]) for vertex in vertices}

    def mask(items: set[int] | tuple[int, ...]) -> int:
        return sum(1 << index[vertex] for vertex in items)

    cliques: dict[int, list[tuple[int, ...]]] = {3: [], 4: [], 5: []}
    for clique in nx.enumerate_all_cliques(graph):
        if len(clique) in cliques:
            cliques[len(clique)].append(tuple(clique))
        elif len(clique) > 5:
            break

    edges = [tuple(edge) for edge in graph.edges]
    supports: dict[int, set[int]] = {5: set(), 6: set(), 7: set()}

    # Bag sizes (1,1,1,1,1).
    for clique in cliques[5]:
        supports[5].add(mask(clique))

    # Bag sizes (2,1,1,1,1).
    for clique in cliques[4]:
        singletons = set(clique)
        for left, right in edges:
            edge_bag = {left, right}
            if singletons & edge_bag:
                continue
            if all(adjacency[q] & edge_bag for q in clique):
                supports[6].add(mask(singletons | edge_bag))

    # Bag sizes (3,1,1,1,1).
    connected_triples = []
    for triple in combinations(vertices, 3):
        left, middle, right = triple
        if sum(
            (
                middle in adjacency[left],
                right in adjacency[left],
                right in adjacency[middle],
            )
        ) >= 2:
            connected_triples.append(set(triple))
    for clique in cliques[4]:
        singletons = set(clique)
        for triple_bag in connected_triples:
            if singletons & triple_bag:
                continue
            if all(adjacency[q] & triple_bag for q in clique):
                supports[7].add(mask(singletons | triple_bag))

    # Bag sizes (2,2,1,1,1).
    for clique in cliques[3]:
        singletons = set(clique)
        eligible_edges = []
        for left, right in edges:
            edge_bag = {left, right}
            if singletons & edge_bag:
                continue
            if all(adjacency[q] & edge_bag for q in clique):
                eligible_edges.append(edge_bag)
        for first, second in combinations(eligible_edges, 2):
            if first & second:
                continue
            if any(y in adjacency[x] for x in first for y in second):
                supports[7].add(mask(singletons | first | second))

    return supports


def support_values_through_seven(graph: nx.Graph) -> dict[tuple[int, int], int | None]:
    vertices = list(graph)
    index = {vertex: offset for offset, vertex in enumerate(vertices)}
    supports = model_supports_through_seven(graph)
    values = {}
    for left, right in combinations(vertices, 2):
        forbidden = (1 << index[left]) | (1 << index[right])
        value = None
        for order in (5, 6, 7):
            if any(support & forbidden == 0 for support in supports[order]):
                value = order
                break
        values[tuple(sorted((left, right)))] = value
    return values


def order_six_witness(
    graph: nx.Graph, pair: tuple[int, int]
) -> tuple[tuple[int, ...], tuple[int, int]]:
    adjacency = {vertex: set(graph[vertex]) for vertex in graph}
    for clique in nx.enumerate_all_cliques(graph):
        if len(clique) != 4:
            continue
        if set(clique) & set(pair):
            continue
        for edge in graph.edges:
            edge_bag = set(edge)
            if edge_bag & set(clique) or edge_bag & set(pair):
                continue
            if all(adjacency[q] & edge_bag for q in clique):
                return tuple(clique), tuple(edge)
    raise AssertionError("no order-six witness")


def main() -> None:
    # The requested K2 join icosahedron guardrail is vacuous: every edge
    # contraction lowers its connectivity to six.
    icosahedral_host = add_two_apices(nx.icosahedral_graph(), adjacent=True)
    histogram = Counter(
        nx.node_connectivity(contract(icosahedral_host, tuple(edge))[0])
        for edge in icosahedral_host.edges
    )
    assert histogram == Counter({6: 55})
    print("K2-join-icosahedron contraction connectivity", dict(histogram))

    base = dual_truncated_icosahedron()
    graph = add_two_apices(base, adjacent=False)
    edge = (0, 16)
    contracted, z = contract(graph, edge)

    # Connectivity is checked exactly.  K7-minor-freeness is structural:
    # a K7 model would leave at least five branch sets wholly in the planar
    # base after removing the at most two apex-containing bags, giving a
    # forbidden K5 minor of the base.
    assert nx.node_connectivity(graph) == 7
    assert nx.node_connectivity(contracted) == 7
    assert nx.check_planarity(base)[0]
    assert nx.check_planarity(contract(base, edge)[0])[0]

    values_g = support_values_through_seven(graph)
    values_h = support_values_through_seven(contracted)
    print("G support distribution", dict(Counter(values_g.values())))
    print("H support distribution", dict(Counter(values_h.values())))

    # First clause: z is outside R.
    outside_pair = (1, 2)
    assert z not in outside_pair
    assert values_h[outside_pair] == 6
    assert values_g[outside_pair] == 6

    # Second clause: R contains z, but both literal pullbacks stay at six.
    inside_pair = tuple(sorted((z, 1)))
    first_pullback = tuple(sorted((edge[0], 1)))
    second_pullback = tuple(sorted((edge[1], 1)))
    assert values_h[inside_pair] == 6
    assert values_g[first_pullback] == 6
    assert values_g[second_pullback] == 6

    print(
        "z-outside counterexample",
        outside_pair,
        "mu_H=6 mu_G=6",
        "witness_G",
        order_six_witness(graph, outside_pair),
        "witness_H",
        order_six_witness(contracted, outside_pair),
    )
    print(
        "z-inside counterexample",
        inside_pair,
        "mu_H=6",
        "witness_H",
        order_six_witness(contracted, inside_pair),
        first_pullback,
        "mu_G=6",
        "witness_Gx",
        order_six_witness(graph, first_pullback),
        second_pullback,
        "mu_G=6",
        "witness_Gy",
        order_six_witness(graph, second_pullback),
    )
    print("RED: both naive contraction-pullback clauses are false")


if __name__ == "__main__":
    main()
