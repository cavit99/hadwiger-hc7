"""Verify the K7-minor-free static width-two split barrier."""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations

import networkx as nx


S = ("c", "a1", "t1", "a2", "t2", "a3", "t3")
A = frozenset(("c", "t1", "t2", "t3"))
B = frozenset(("a1", "a2", "a3"))
L = ("l0", "l1", "l2")
P, Q = "p", "q"


def build() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(S + L + (P, Q))
    graph.add_edges_from(
        (
            ("c", "a1"),
            ("c", "a2"),
            ("c", "a3"),
            ("a1", "t2"),
            ("t1", "a3"),
            ("a2", "t3"),
        )
    )
    graph.add_edges_from(combinations(L, 2))
    rows = {
        "l0": ("c", "a1", "t1", "t2", "a3"),
        "l1": ("c", "a1", "a2", "t2", "t3"),
        "l2": ("c", "t1", "a2", "a3", "t3"),
    }
    for vertex, contacts in rows.items():
        graph.add_edges_from((vertex, literal) for literal in contacts)
    graph.add_edge(P, Q)
    for packet in (P, Q):
        graph.add_edges_from((packet, literal) for literal in S)
    return graph


def connected_subsets(graph: nx.Graph, vertices):
    vertices = tuple(vertices)
    for mask in range(1, 1 << len(vertices)):
        subset = frozenset(
            vertices[i] for i in range(len(vertices)) if mask >> i & 1
        )
        if nx.is_connected(graph.subgraph(subset)):
            yield subset


def funds(graph: nx.Graph, carrier, duty) -> bool:
    return all(
        any(graph.has_edge(vertex, literal) for vertex in carrier)
        for literal in duty
    )


def alpha(graph: nx.Graph) -> int:
    return max(
        (len(clique) for clique in nx.find_cliques(nx.complement(graph))),
        default=0,
    )


def exact_k7_model(graph: nx.Graph):
    """Exhaust connected spanning seven-block partitions.

    Any clique-minor model in a connected graph can be extended to a
    spanning model by attaching every unused component to an adjacent bag.
    Hence this restricted-growth partition search is exact.
    """

    vertices = tuple(graph)
    index = {vertex: i for i, vertex in enumerate(vertices)}
    rows = [0] * len(vertices)
    for left, right in graph.edges:
        i, j = index[left], index[right]
        rows[i] |= 1 << j
        rows[j] |= 1 << i

    @lru_cache(maxsize=None)
    def connected(mask: int) -> bool:
        reached = mask & -mask
        while True:
            expanded = reached
            todo = reached
            while todo:
                bit = todo & -todo
                todo ^= bit
                expanded |= rows[bit.bit_length() - 1] & mask
            if expanded == reached:
                return reached == mask
            reached = expanded

    blocks: list[list[int]] = []
    checked = 0

    def search(position: int):
        nonlocal checked
        if position == len(vertices):
            if len(blocks) != 7:
                return None
            masks = [sum(1 << vertex for vertex in block) for block in blocks]
            if not all(connected(mask) for mask in masks):
                return None
            checked += 1
            neighbourhoods = []
            for block in blocks:
                row = 0
                for vertex in block:
                    row |= rows[vertex]
                neighbourhoods.append(row)
            if all(
                neighbourhoods[i] & masks[j]
                for i, j in combinations(range(7), 2)
            ):
                return tuple(
                    tuple(vertices[vertex] for vertex in block) for block in blocks
                )
            return None

        if len(blocks) + len(vertices) - position < 7:
            return None
        for block in blocks:
            block.append(position)
            witness = search(position + 1)
            block.pop()
            if witness is not None:
                return witness
        if len(blocks) < 7:
            blocks.append([position])
            witness = search(position + 1)
            blocks.pop()
            if witness is not None:
                return witness
        return None

    witness = search(0)
    return witness, checked


def main() -> None:
    graph = build()
    boundary = graph.subgraph(S)

    assert nx.is_tree(boundary)
    assert nx.is_bipartite(boundary)
    colouring = nx.bipartite.color(boundary)
    assert {x for x in S if colouring[x] == colouring["c"]} == set(A)
    assert set(S) - set(A) == set(B)
    assert all(not graph.has_edge(f"a{i}", f"t{i}") for i in range(1, 4))
    assert all(
        any(graph.has_edge("c", x) for x in (f"a{i}", f"t{i}"))
        for i in range(1, 4)
    )
    assert all(
        any(
            graph.has_edge(x, y)
            for x in (f"a{i}", f"t{i}")
            for y in (f"a{j}", f"t{j}")
        )
        for i, j in ((1, 2), (1, 3), (2, 3))
    )

    assert nx.is_connected(graph.subgraph(L))
    assert list(nx.articulation_points(graph.subgraph(L))) == []
    assert not any(graph.has_edge(x, y) for x in L for y in (P, Q))
    assert graph.has_edge(P, Q)
    assert all(graph.has_edge(packet, literal) for packet in (P, Q) for literal in S)

    carriers = list(connected_subsets(graph, L))
    full = [carrier for carrier in carriers if funds(graph, carrier, S)]
    a_carriers = [carrier for carrier in carriers if funds(graph, carrier, A)]
    b_carriers = [carrier for carrier in carriers if funds(graph, carrier, B)]
    assert len(full) == 4
    assert {len(packet) for packet in full} == {2, 3}
    assert not any(
        left.isdisjoint(right) for left, right in combinations(full, 2)
    )
    assert not any(
        left.isdisjoint(right) for left in a_carriers for right in b_carriers
    )

    planar_core = graph.copy()
    planar_core.remove_nodes_from((P, Q))
    planar, embedding = nx.check_planarity(planar_core)
    assert planar
    embedding.check_structure()
    assert len(planar_core) == 10
    assert planar_core.number_of_edges() == 3 * len(planar_core) - 6
    assert all(graph.subgraph(L).degree(vertex) + len(set(graph[vertex]) & set(S)) == 7
               for vertex in L)
    thin_expansion = {}
    for size in range(1, len(L) + 1):
        for subset_tuple in combinations(L, size):
            subset = set(subset_tuple)
            neighbourhood = set().union(*(set(graph[x]) for x in subset)) - subset
            thin_expansion[subset_tuple] = len(neighbourhood)
            assert len(neighbourhood) >= 7
    thin_neighbourhood_alpha = {
        vertex: alpha(graph.subgraph(graph[vertex])) for vertex in L
    }
    assert thin_neighbourhood_alpha == {vertex: 3 for vertex in L}

    # A literal common low state, showing why state attainment without
    # minimal incompatibility is insufficient.
    colouring = {vertex: 0 if vertex in A else 1 for vertex in S}
    colouring.update({"l0": 2, "l1": 3, "l2": 4, P: 2, Q: 3})
    assert all(colouring[left] != colouring[right] for left, right in graph.edges)

    witness, checked = exact_k7_model(graph)
    assert witness is None
    assert nx.node_connectivity(graph) == 5

    print("VERIFIED")
    print("vertices", len(graph), "edges", graph.number_of_edges())
    print("thin_full_packets", full)
    print("A_carriers", a_carriers)
    print("B_carriers", b_carriers)
    print("planar_core", planar)
    print("connected_spanning_seven_partitions", checked)
    print("K7_minor", witness)
    print("thin_local_degrees", {
        vertex: graph.subgraph(L).degree(vertex) + len(set(graph[vertex]) & set(S))
        for vertex in L
    })
    print("thin_neighbourhood_alpha", thin_neighbourhood_alpha)
    print("thin_expansion", thin_expansion)
    print("explicit_colours", colouring)
    print("node_connectivity", nx.node_connectivity(graph))


if __name__ == "__main__":
    main()
