"""Verify a small barrier to the connectivity-only thin-split principle.

The graph has a literal exact-seven separation with a valid paired-state
tree boundary, packet vector (1,2), thirty-nine surplus packet contacts,
minimum degree seven, and all Dirac neighbourhood inequalities at parameter
seven.  Its thin shore nevertheless has no disjoint carriers for the two
boundary bipartition duties.

It deliberately contains a literal K7 and is not claimed contraction-
critical.  It therefore falsifies only an implication from the static and
connectivity hypotheses.
"""

from __future__ import annotations

import itertools

import networkx as nx


S = ("c", "a1", "t1", "a2", "t2", "a3", "t3")
A = frozenset(("c", "t1", "t2", "t3"))
B = frozenset(("a1", "a2", "a3"))
L = tuple(("l", i) for i in range(5))
R = tuple(("r", i) for i in range(6))


def alpha(graph: nx.Graph) -> int:
    return max(
        (len(clique) for clique in nx.find_cliques(nx.complement(graph))),
        default=0,
    )


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
        any(graph.has_edge(vertex, boundary) for vertex in carrier)
        for boundary in duty
    )


def packet_number(graph: nx.Graph, shore) -> int:
    packets = [
        carrier
        for carrier in connected_subsets(graph, shore)
        if funds(graph, carrier, S)
    ]

    def search(start: int, used: frozenset) -> int:
        best = 0
        for index in range(start, len(packets)):
            if packets[index].isdisjoint(used):
                best = max(
                    best,
                    1 + search(index + 1, used | packets[index]),
                )
        return best

    return search(0, frozenset())


def build():
    graph = nx.Graph()
    graph.add_nodes_from(S)

    # The six mandatory paired-state edges form a subdivided claw.  The
    # paired blocks are {a_i,t_i}; the centre c sees a_i in every block,
    # and the last three edges join every pair of distinct blocks.
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

    # The thin shore is W_5: an outer 4-cycle and its universal centre.
    graph.add_nodes_from(L)
    graph.add_edges_from((L[i], L[(i + 1) % 4]) for i in range(4))
    graph.add_edges_from((L[4], L[i]) for i in range(4))

    # Every thin vertex sees c,a1,t1.  The first four outer vertices then
    # receive alternating A,B,A,B contacts, followed by three extra contacts
    # selected by the finite falsifier.  These extras make all Dirac
    # inequalities hold without creating the desired duty split.
    for vertex in L:
        graph.add_edges_from((vertex, boundary) for boundary in ("c", "a1", "t1"))
    graph.add_edges_from(
        (
            (L[0], "t2"),
            (L[1], "a2"),
            (L[2], "t3"),
            (L[3], "a3"),
            (L[0], "a2"),
            (L[1], "t3"),
            (L[2], "a3"),
        )
    )

    # A rich K6 with exactly two disjoint full packets.  The other four
    # vertices all miss c, so every full packet contains r0 or r1.
    graph.add_nodes_from(R)
    graph.add_edges_from(itertools.combinations(R, 2))
    for index, vertex in enumerate(R):
        contacts = S if index < 2 else S[1:]
        graph.add_edges_from((vertex, boundary) for boundary in contacts)

    return graph


def main():
    graph = build()

    # S is a literal cut separating the two nonempty open shores.
    assert not any(graph.has_edge(left, right) for left in L for right in R)
    assert nx.number_connected_components(graph.subgraph(set(graph) - set(S))) == 2
    assert nx.node_connectivity(graph) == 7
    assert min(dict(graph.degree()).values()) == 7

    # The literal paired-state and frontier assertions.
    boundary = graph.subgraph(S)
    assert nx.is_tree(boundary)
    assert nx.is_bipartite(boundary)
    assert all(not graph.has_edge(f"a{i}", f"t{i}") for i in range(1, 4))
    assert all(any(graph.has_edge("c", x) for x in (f"a{i}", f"t{i}")) for i in range(1, 4))
    assert all(
        any(graph.has_edge(x, y) for x in (f"a{i}", f"t{i}") for y in (f"a{j}", f"t{j}"))
        for i, j in ((1, 2), (1, 3), (2, 3))
    )
    colouring = nx.bipartite.color(boundary)
    assert {x for x in S if colouring[x] == colouring["c"]} == set(A)
    assert set(S) - set(A) == set(B)

    assert packet_number(graph, L) == 1
    assert packet_number(graph, R) == 2

    # Explicit adjacent full cover P,Q of the rich shore.
    p = frozenset((R[0], R[2], R[3]))
    q = frozenset((R[1], R[4], R[5]))
    assert p.isdisjoint(q) and p | q == frozenset(R)
    assert nx.is_connected(graph.subgraph(p))
    assert nx.is_connected(graph.subgraph(q))
    assert funds(graph, p, S) and funds(graph, q, S)
    assert any(graph.has_edge(x, y) for x in p for y in q)

    contact_count = lambda shore: sum(
        graph.has_edge(vertex, boundary) for vertex in shore for boundary in S
    )
    counts = (contact_count(L), contact_count(p), contact_count(q))
    surplus = sum(counts) - 3 * len(S)
    assert counts == (22, 19, 19)
    assert surplus == 39 >= 14

    # Exhaust all 31 nonempty vertex subsets of the thin W5.  No A-carrier
    # is even vertex-disjoint from a B-carrier, so in particular no adjacent
    # connected split satisfies Lemma 5.2.
    carriers = list(connected_subsets(graph, L))
    a_carriers = [carrier for carrier in carriers if funds(graph, carrier, A)]
    b_carriers = [carrier for carrier in carriers if funds(graph, carrier, B)]
    assert not any(
        left.isdisjoint(right) for left in a_carriers for right in b_carriers
    )

    # The static graph even satisfies every local Dirac inequality forced by
    # strong seven-contraction-criticality.
    for vertex in graph:
        neighbourhood = graph.subgraph(graph[vertex])
        assert alpha(neighbourhood) <= graph.degree(vertex) - 5

    # Trust boundary: the rich K6 together with a1 is a literal K7.
    literal_k7 = frozenset(R) | {"a1"}
    assert len(literal_k7) == 7
    assert graph.subgraph(literal_k7).number_of_edges() == 21

    print("VERIFIED")
    print("vertices", len(graph), "edges", graph.number_of_edges())
    print("node_connectivity", nx.node_connectivity(graph))
    print("minimum_degree", min(dict(graph.degree()).values()))
    print("packet_vector", (packet_number(graph, L), packet_number(graph, R)))
    print("packet_contacts", counts, "surplus", surplus)
    print("A_carriers", len(a_carriers), "B_carriers", len(b_carriers))
    print("literal_K7", sorted(literal_k7, key=str))


if __name__ == "__main__":
    main()
