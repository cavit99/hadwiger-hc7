#!/usr/bin/env python3
"""Verify the K_{3,3,3} local-rural gluing barrier."""

from __future__ import annotations

import itertools

import networkx as nx


def main() -> None:
    g = nx.complete_multipartite_graph(3, 3, 3)
    parts = (set(range(3)), set(range(3, 6)), set(range(6, 9)))
    assert nx.node_connectivity(g) == 6

    # The proof note gives the exact K7-minor exclusion count.  Here we
    # check the two-apex and page assertions computationally.
    for deleted in itertools.combinations(g, 2):
        h = nx.Graph(g)
        h.remove_nodes_from(deleted)
        assert not nx.check_planarity(h)[0]

    a, b = 0, 3
    for i, j in ((0, 1), (1, 2), (2, 0)):
        page = g.subgraph(parts[i] | parts[j]).copy()
        page.remove_nodes_from({a, b})
        assert nx.check_planarity(page)[0]

    print("GREEN: kappa=6, no two-apex pair, three commonly planarized pages")


if __name__ == "__main__":
    main()
