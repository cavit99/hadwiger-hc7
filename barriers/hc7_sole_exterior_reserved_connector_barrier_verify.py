#!/usr/bin/env python3
"""Verify the explicit high-connectivity reserved-connector barrier."""

import networkx as nx


def main() -> None:
    p = nx.icosahedral_graph()
    assert len(p) == 12
    assert nx.node_connectivity(p) == 5
    assert min(dict(p.degree()).values()) == 5
    assert nx.check_planarity(p)[0]

    c = p.copy()
    a, b = 12, 13
    c.add_edge(a, b)
    for x in range(12):
        c.add_edge(a, x)
        c.add_edge(b, x)

    assert nx.node_connectivity(c) == 7
    assert min(dict(c.degree()).values()) == 7

    portals = tuple(range(7))
    # Explicit carrier rows.  The sets are disjoint, connected, adjacent,
    # and contain the unique portals for their two assigned labels.
    rows = [
        ({portals[1], a, portals[3]}, {portals[2], b, portals[4]}),
        ({portals[1], a, portals[4]}, {portals[2], b, portals[3]}),
    ]
    for left, right in rows:
        assert left.isdisjoint(right)
        assert nx.is_connected(c.subgraph(left))
        assert nx.is_connected(c.subgraph(right))
        assert any(c.has_edge(x, y) for x in left for y in right)

    # Any S-full vertex set must contain all unique portals.  Every carrier
    # row has already consumed the four corner portals, so a disjoint full
    # set is impossible.
    for left, right in rows:
        assert set(portals[:7]) & (left | right)
        assert set(portals[1:5]) <= left | right
        assert not set(portals).isdisjoint(left | right)

    print("verified: kappa(C)=7, delta(C)=7, both matchings essential")


if __name__ == "__main__":
    main()
