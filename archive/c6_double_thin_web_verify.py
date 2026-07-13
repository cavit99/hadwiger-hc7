#!/usr/bin/env python3
"""Kuratowski certificate for the double-thin one-ear web.

If the four Two-Paths terminals are cofacial, adjoining r to all four
preserves planarity.  Contracting the connected body to b leaves the
displayed subdivision of K_3,3.
"""

from __future__ import annotations

import networkx as nx


LEFT = ("x", "b", "c3")
RIGHT = ("p", "q", "c4")


def graph() -> nx.Graph:
    answer = nx.Graph()
    answer.add_edges_from(
        (
            ("x", "p"), ("x", "q"), ("x", "c4"),
            ("b", "p"), ("b", "q"), ("b", "c4"),
            ("c3", "p"), ("c3", "q"),
            ("c3", "r"), ("r", "c4"),
            # The remaining terminal/body edges from the actual quotient.
            ("x", "c0"), ("b", "c1"), ("p", "q"),
            ("r", "c0"), ("r", "c1"),
        )
    )
    return answer


def main() -> None:
    answer = graph()
    assert not nx.check_planarity(answer)[0]

    # Suppressing r turns its c3-r-c4 path into the ninth K3,3 edge.
    subdivision = answer.edge_subgraph(
        (
            ("x", "p"), ("x", "q"), ("x", "c4"),
            ("b", "p"), ("b", "q"), ("b", "c4"),
            ("c3", "p"), ("c3", "q"),
            ("c3", "r"), ("r", "c4"),
        )
    ).copy()
    assert subdivision.degree("r") == 2
    subdivision.remove_node("r")
    subdivision.add_edge("c3", "c4")
    assert nx.is_isomorphic(
        subdivision,
        nx.complete_bipartite_graph(LEFT, RIGHT),
    )
    print("K3,3 left", LEFT)
    print("K3,3 right", RIGHT)
    print("subdivided edge c3-r-c4")
    print("cofacial-apex quotient planar", nx.check_planarity(answer)[0])


if __name__ == "__main__":
    main()
