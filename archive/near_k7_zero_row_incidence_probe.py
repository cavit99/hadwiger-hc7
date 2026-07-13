#!/usr/bin/env python3
"""Probe K7 minors in a K6 frame plus independent zero-row components.

Each outside vertex is adjacent to every frame vertex except its named
zero column.  The vertices represent distinct components of the free graph,
so they are pairwise anticomplete.  This deliberately forgets internal
portal placement; it is only an incidence-level falsification/guide.
"""

from __future__ import annotations

from itertools import combinations_with_replacement

import networkx as nx


def graph_for(zeros: tuple[int, ...]) -> nx.Graph:
    graph = nx.complete_graph(6)
    for i, zero in enumerate(zeros, 6):
        graph.add_node(i)
        graph.add_edges_from((i, j) for j in range(6) if j != zero)
    return graph


def main() -> None:
    tested = 0
    for outside_count in range(1, 9):
        profiles = tuple(combinations_with_replacement(range(6), outside_count))
        for zeros in profiles:
            graph = graph_for(zeros)
            assert nx.is_chordal(graph)
            assert max(map(len, nx.chordal_graph_cliques(graph))) == 6
            # The reverse outside-vertex order followed by the K6 is an
            # explicit perfect-elimination order: each outside vertex sees
            # exactly one K5 and no other outside vertex.
            for v, zero in zip(range(6, 6 + outside_count), zeros):
                assert set(graph[v]) == set(range(6)) - {zero}
            tested += 1
        print("outside", outside_count, "profiles", len(profiles),
              "all chordal with clique number 6")
    print("profiles checked", tested)


if __name__ == "__main__":
    main()
