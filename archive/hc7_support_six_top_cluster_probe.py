#!/usr/bin/env python3
"""Exact seven-vertex probe for the support-six top-cluster residue.

A top cluster consists of the seven six-subsets of a fixed seven-set U.
For every u in U, this probe asks whether G[U-u] supports a spanning K5
model of bag sizes (2,1,1,1,1).  It then tests whether G[U] has a K6 minor
and whether adjoining one universal exterior vertex produces a K7 minor.

The census is exhaustive over the 1,044 unlabelled seven-vertex graphs in
NetworkX's graph atlas.  It is a falsification aid, not by itself a theorem.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations
import sys

sys.path.insert(0, "active/runtime/deps")
import networkx as nx  # noqa: E402


def spanning_support_six_k5(graph: nx.Graph) -> bool:
    """Return whether a six-vertex graph has a spanning K5 model."""

    if graph.number_of_nodes() != 6:
        return False
    vertices = tuple(graph)
    for core in combinations(vertices, 4):
        if any(not graph.has_edge(x, y) for x, y in combinations(core, 2)):
            continue
        edge_bag = tuple(set(vertices) - set(core))
        if not graph.has_edge(*edge_bag):
            continue
        if all(any(graph.has_edge(q, x) for x in edge_bag) for q in core):
            return True
    return False


def has_complete_minor(graph: nx.Graph, order: int) -> bool:
    """Exact connected-branch-set search, sufficient for graphs of order <=8."""

    vertices = tuple(graph)
    index = {vertex: i for i, vertex in enumerate(vertices)}
    n = len(vertices)
    adjacency = [0] * n
    for vertex in vertices:
        i = index[vertex]
        for neighbour in graph[vertex]:
            adjacency[i] |= 1 << index[neighbour]

    connected = []
    neighbourhood = {}
    for mask in range(1, 1 << n):
        seed = mask & -mask
        seen = seed
        while True:
            nxt = seen
            todo = seen
            while todo:
                bit = todo & -todo
                todo -= bit
                nxt |= adjacency[bit.bit_length() - 1] & mask
            if nxt == seen:
                break
            seen = nxt
        if seen != mask:
            continue
        connected.append(mask)
        neighbours = 0
        todo = mask
        while todo:
            bit = todo & -todo
            todo -= bit
            neighbours |= adjacency[bit.bit_length() - 1]
        neighbourhood[mask] = neighbours & ~mask

    connected.sort(key=lambda mask: (mask.bit_count(), mask))

    @lru_cache(maxsize=None)
    def search(chosen: tuple[int, ...], used: int, start: int) -> bool:
        if len(chosen) == order:
            return True
        if n - used.bit_count() < order - len(chosen):
            return False
        for position in range(start, len(connected)):
            branch = connected[position]
            if branch & used:
                continue
            if any(not (neighbourhood[branch] & old) for old in chosen):
                continue
            if search(chosen + (branch,), used | branch, position + 1):
                return True
        return False

    return search((), 0, 0)


def graph6(graph: nx.Graph) -> str:
    return nx.to_graph6_bytes(graph, header=False).decode().strip()


def main() -> None:
    seven_vertex_graphs = [
        graph
        for graph in nx.graph_atlas_g()
        if graph.number_of_nodes() == 7
    ]
    assert len(seven_vertex_graphs) == 1044

    top_hosts = []
    no_k6 = []
    universal_no_k7 = []
    for graph in seven_vertex_graphs:
        if not all(
            spanning_support_six_k5(graph.subgraph(set(graph) - {vertex}))
            for vertex in graph
        ):
            continue
        top_hosts.append(graph)
        if not has_complete_minor(graph, 6):
            no_k6.append(graph)
        joined = graph.copy()
        apex = 7
        joined.add_node(apex)
        joined.add_edges_from((apex, vertex) for vertex in graph)
        if not has_complete_minor(joined, 7):
            universal_no_k7.append(graph)

    print("top-cluster hosts", len(top_hosts))
    print("top-cluster hosts without K6 minor", len(no_k6))
    print("universal extensions without K7 minor", len(universal_no_k7))
    print(
        "top complement signatures",
        [
            (
                graph6(graph),
                tuple(sorted(dict(nx.complement(graph).degree()).values())),
                tuple(sorted(tuple(sorted(edge)) for edge in nx.complement(graph).edges)),
            )
            for graph in top_hosts
        ],
    )
    if no_k6:
        print("no-K6 graph6", [graph6(graph) for graph in no_k6])
    if universal_no_k7:
        print(
            "universal-no-K7 graph6",
            [graph6(graph) for graph in universal_no_k7],
        )


if __name__ == "__main__":
    main()
