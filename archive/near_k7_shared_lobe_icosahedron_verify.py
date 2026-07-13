#!/usr/bin/env python3
"""Replay the coherent-2-apex shared-singleton-lobe witness.

This verifies the finite graph assertions in Proposition 4.1 of
hadwiger_near_k7_shared_lobe_exchange.md.  K7-minor exclusion is proved
there from the two-apex planar argument; the script verifies planarity.
"""

from __future__ import annotations

import networkx as nx


def main() -> None:
    ico = nx.icosahedral_graph()
    assert nx.check_planarity(ico)[0]
    assert nx.node_connectivity(ico) == 5

    graph = ico.copy()
    u, v = 12, 13
    graph.add_edge(u, v)
    for x in ico:
        graph.add_edge(u, x)
        graph.add_edge(v, x)
    assert nx.node_connectivity(graph) == 7

    a, b, c, r1, r2, r3 = 4, 0, 1, u, v, 5
    labels = (a, b, c, r1, r2, r3)
    missing = {
        tuple(sorted((x, y)))
        for i, x in enumerate(labels)
        for y in labels[i + 1:]
        if not graph.has_edge(x, y)
    }
    assert missing == {tuple(sorted((a, b))), tuple(sorted((a, c)))}

    body = {2, 3, 6, 7, 8, 9, 10, 11}
    assert set(graph) == set(labels) | body
    assert nx.is_connected(graph.subgraph(body))
    assert all(set(graph[x]) & body for x in labels)

    lobe = 11
    poles = {7, 10}
    assert set(graph[lobe]) & body == poles
    assert set(graph[lobe]) & set(labels) == {a, b, r1, r2, r3}
    assert set(graph[lobe]) == poles | {a, b, r1, r2, r3}
    assert graph.degree(lobe) == 7
    assert nx.is_connected(graph.subgraph(body - poles - {lobe}))

    print("icosahedron planar and 5-connected")
    print("join graph connectivity", nx.node_connectivity(graph))
    print("literal missing edges", sorted(missing))
    print("complex bag connected", sorted(body))
    print("dark singleton exact boundary", sorted(graph[lobe]))


if __name__ == "__main__":
    main()
