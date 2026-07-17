#!/usr/bin/env python3
"""Probe the two-transversal pullback across a split apex.

Start with H = K2 join I, where I is the icosahedron.  Split one universal
vertex z into adjacent vertices x,y whose neighbourhoods cover I, retaining
the other universal vertex b.  The pair {z,b} is terminal in H.  This probe
looks for a seven-connected split G in which no pair meets every K5-model
supported on at most six vertices.

This is a falsifier only.  A survivor would still need an independent K7
minor check; the script records the exact small-model family and connectivity.
"""

from __future__ import annotations

import argparse
import random
import subprocess
import sys
from itertools import combinations

sys.path.insert(0, "active/runtime/deps")
import networkx as nx


def icosahedron() -> nx.Graph:
    return nx.icosahedral_graph()


def split_apex(left: set[int], right: set[int]) -> nx.Graph:
    base = icosahedron()
    graph = nx.Graph(base)
    x, y, b = 12, 13, 14
    graph.add_edges_from((b, vertex) for vertex in range(12))
    graph.add_edges_from(((b, x), (b, y), (x, y)))
    graph.add_edges_from((x, vertex) for vertex in left)
    graph.add_edges_from((y, vertex) for vertex in right)
    return graph


def small_k5_supports(graph: nx.Graph) -> set[frozenset[int]]:
    """All supports of K5-models of order five or six.

    At order five the support is a literal K5.  At order six the bag sizes
    are (2,1,1,1,1), so four singleton vertices form a K4 and the remaining
    adjacent pair jointly contacts every singleton.
    """

    vertices = tuple(graph)
    supports: set[frozenset[int]] = set()
    for five in combinations(vertices, 5):
        if graph.subgraph(five).number_of_edges() == 10:
            supports.add(frozenset(five))
    for six in combinations(vertices, 6):
        support = set(six)
        for u, v in combinations(six, 2):
            if not graph.has_edge(u, v):
                continue
            clique = support - {u, v}
            if graph.subgraph(clique).number_of_edges() != 6:
                continue
            if all(graph.has_edge(u, q) or graph.has_edge(v, q) for q in clique):
                supports.add(frozenset(support))
                break
    return supports


def transversal_pair(
    vertices: tuple[int, ...], supports: set[frozenset[int]]
) -> tuple[int, int] | None:
    for pair in combinations(vertices, 2):
        if all(set(pair) & support for support in supports):
            return pair
    return None


def has_k7_minor_at_most_eight(graph: nx.Graph) -> bool:
    """Exact for graphs of order at most eight."""

    vertices = tuple(graph)
    for seven in combinations(vertices, 7):
        if graph.subgraph(seven).number_of_edges() == 21:
            return True
    if len(vertices) < 8:
        return False
    for u, v in combinations(vertices, 2):
        if not graph.has_edge(u, v):
            continue
        clique = set(vertices) - {u, v}
        if graph.subgraph(clique).number_of_edges() != 15:
            continue
        if all(graph.has_edge(u, q) or graph.has_edge(v, q) for q in clique):
            return True
    return False


def random_cover(rng: random.Random) -> tuple[set[int], set[int]]:
    left: set[int] = set()
    right: set[int] = set()
    for vertex in range(12):
        state = rng.randrange(3)
        if state != 1:
            left.add(vertex)
        if state != 0:
            right.add(vertex)
    return left, right


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=20_000)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--atlas", action="store_true")
    parser.add_argument("--geng", type=int)
    args = parser.parse_args()
    if args.geng is not None:
        if args.geng > 8:
            raise SystemExit("the current exact K7-minor test is only valid through order 8")
        process = subprocess.Popen(
            ["geng", "-cq", str(args.geng)],
            stdout=subprocess.PIPE,
            text=True,
        )
        assert process.stdout is not None
        tested = positive = excluded = 0
        for line in process.stdout:
            if line.startswith(">"):
                continue
            graph = nx.from_graph6_bytes(line.strip().encode())
            tested += 1
            supports = small_k5_supports(graph)
            if not supports or transversal_pair(tuple(graph), supports) is not None:
                continue
            positive += 1
            if has_k7_minor_at_most_eight(graph):
                excluded += 1
                continue
            print(
                "COUNTERARCHITECTURE",
                "order=", len(graph),
                "edges=", graph.number_of_edges(),
                "supports=", len(supports),
                "connectivity=", nx.node_connectivity(graph),
                "graph6=", line.strip(),
            )
            return
        if process.wait() != 0:
            raise SystemExit("geng failed")
        print(
            "GENG_GREEN",
            "tested=", tested,
            "tau_gt_2=", positive,
            "all_with_K7=", excluded,
        )
        return
    if args.atlas:
        records = []
        for graph in nx.graph_atlas_g():
            if len(graph) != 7 or not nx.is_connected(graph):
                continue
            supports = small_k5_supports(graph)
            if not supports:
                continue
            minimum = None
            for size in range(1, 8):
                if any(
                    all(set(choice) & support for support in supports)
                    for choice in combinations(graph, size)
                ):
                    minimum = size
                    break
            records.append((minimum, len(supports), graph.number_of_edges(), graph))
        records.sort(key=lambda record: record[:3], reverse=True)
        for minimum, count, edges, graph in records[:20]:
            print(
                "ATLAS",
                "tau=", minimum,
                "supports=", count,
                "edges=", edges,
                "graph6=", nx.to_graph6_bytes(graph, header=False).decode().strip(),
            )
        return
    rng = random.Random(args.seed)

    tested = connected = unhit = 0
    canonical_failures = 0
    best: tuple[int, set[int], set[int], int, int] | None = None
    for _ in range(args.trials):
        left, right = random_cover(rng)
        if min(len(left), len(right)) < 5:
            continue
        tested += 1
        graph = split_apex(left, right)
        connectivity = nx.node_connectivity(graph)
        if connectivity < 7:
            continue
        connected += 1
        supports = small_k5_supports(graph)
        pair = transversal_pair(tuple(graph), supports)
        canonical = ((12, 14), (13, 14), (12, 13))
        if all(any(not (set(candidate) & support) for support in supports) for candidate in canonical):
            canonical_failures += 1
            print(
                "CANONICAL_LIFTS_FAIL",
                "left=", sorted(left),
                "right=", sorted(right),
                "global_pair=", pair,
                "supports=", len(supports),
                "connectivity=", connectivity,
            )
            return
        if pair is None:
            unhit += 1
            print(
                "SURVIVOR",
                "left=", sorted(left),
                "right=", sorted(right),
                "supports=", len(supports),
                "connectivity=", connectivity,
            )
            return
        score = min(
            sum(bool(set(pair0) & support) for support in supports)
            for pair0 in combinations(graph, 2)
        )
        record = (score, left, right, len(supports), connectivity)
        if best is None or score < best[0]:
            best = record

    print(
        "NO_SURVIVOR",
        "tested=", tested,
        "seven_connected=", connected,
        "unhit=", unhit,
        "canonical_failures=", canonical_failures,
        "best=", best,
    )


if __name__ == "__main__":
    main()
