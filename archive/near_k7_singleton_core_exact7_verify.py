#!/usr/bin/env python3
"""Verify the sharp singleton-K4-core icosahedral counterarchitecture."""

import networkx as nx


def build():
    g = nx.Graph()
    t, b = "t", "b"
    us = [f"u{i}" for i in range(5)]
    ws = [f"w{i}" for i in range(5)]
    old = [t, b, *us, *ws]
    g.add_nodes_from([*old, "p", "q"])
    for i in range(5):
        g.add_edge(t, us[i])
        g.add_edge(b, ws[i])
        g.add_edge(us[i], us[(i + 1) % 5])
        g.add_edge(ws[i], ws[(i + 1) % 5])
        g.add_edge(us[i], ws[i])
        g.add_edge(us[i], ws[(i - 1) % 5])
    for z in old:
        g.add_edge("p", z)
        g.add_edge("q", z)
    g.add_edge("p", "q")
    return g, set(old)


def sees(g, bag, vertex):
    return any(g.has_edge(z, vertex) for z in bag)


def main():
    g, old = build()
    qcore = {"p", "q", "t", "u0"}
    x, y = "u1", "u4"
    d = set(g) - qcore - {x, y}

    assert nx.node_connectivity(g) == 7
    assert nx.check_planarity(g.subgraph(old))[0]
    assert all(g.has_edge(a, b) for a in qcore for b in qcore if a != b)
    assert not g.has_edge(x, y)
    assert all(g.has_edge(x, z) and g.has_edge(y, z) for z in qcore)
    assert nx.is_connected(g.subgraph(d))
    assert nx.node_connectivity(g.subgraph(d)) == 3
    assert all(sees(g, d, z) for z in qcore | {x, y})
    assert all(g.has_edge(z, v) for z in {"p", "q"} for v in set(g) - {z})

    # A literal K6 model in G: p,q and a facial triangle of I plus the
    # connected remainder of I.  Planarity of I rules out K5 in I, so
    # the two universal vertices also certify eta(G) <= 6.
    face = {"t", "u0", "u1"}
    rest = old - face
    assert all(g.has_edge(a, b) for a in face for b in face if a != b)
    assert nx.is_connected(g.subgraph(rest))
    assert all(sees(g, rest, z) for z in face)

    common = set.intersection(*(set(g.neighbors(z)) - qcore for z in qcore))
    assert common == {"u1", "u4"}
    assert not g.has_edge(*sorted(common))

    print("verified: kappa(G)=7, planar I, eta(G)=6 certificate")
    print("Q =", sorted(qcore), "x,y =", x, y)
    print("D =", sorted(d), "kappa(D)=", nx.node_connectivity(g.subgraph(d)))
    print("common Q-portals =", sorted(common), "(independent)")


if __name__ == "__main__":
    main()
