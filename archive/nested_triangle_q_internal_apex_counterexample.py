#!/usr/bin/env python3
"""Verify the sharp K2-join-icosahedron neutral-triangle warning."""

import networkx as nx


def main() -> None:
    ico = nx.icosahedral_graph()
    u, v = next(iter(ico.edges()))
    common = sorted(set(ico[u]) & set(ico[v]))
    assert len(common) == 2
    r, s = common

    p, q = "p", "q"
    graph = ico.copy()
    graph.add_edge(p, q)
    for x in ico:
        graph.add_edge(p, x)
        graph.add_edge(q, x)

    neutral = {p, u, v}
    literal_common = {q, r, s}
    h = graph.copy()
    h.remove_nodes_from(neutral)
    piece = set(h) - literal_common

    assert nx.node_connectivity(ico) == 5
    assert nx.node_connectivity(graph) == 7
    assert nx.node_connectivity(h) >= 4
    assert all(all(graph.has_edge(x, z) for z in neutral) for x in literal_common)
    assert nx.is_connected(h.subgraph(piece))
    assert all(any(graph.has_edge(x, z) for x in piece) for z in neutral)
    assert all(any(graph.has_edge(x, z) for x in piece) for z in literal_common)

    # No pair internal to the selected neutral triangle is an apex pair.
    for pair in ((p, u), (p, v), (u, v)):
        remainder = graph.copy()
        remainder.remove_nodes_from(pair)
        assert not nx.check_planarity(remainder)[0]

    coherent = graph.copy()
    coherent.remove_nodes_from((p, q))
    assert nx.is_isomorphic(coherent, ico)
    assert nx.check_planarity(coherent)[0]

    print(
        {
            "order": len(graph),
            "connectivity": nx.node_connectivity(graph),
            "neutral_Q": sorted(map(str, neutral)),
            "literal_common": sorted(map(str, literal_common)),
            "piece_order": len(piece),
            "H_connectivity": nx.node_connectivity(h),
            "Q_internal_apex_pair": False,
            "global_apex_pair": (p, q),
        }
    )


if __name__ == "__main__":
    main()
