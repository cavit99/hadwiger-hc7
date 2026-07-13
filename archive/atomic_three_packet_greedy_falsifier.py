"""Greedy falsification search for an atomic three-packet theorem.

Starting from the clean pairwise-but-not-triple eight-vertex shore, add
internal edges and boundary incidences while preserving absence of a
triple linkage.  The objective is the minimum relative boundary order
over every nonempty proper shore subset.  Reaching eight would refute the
proposed strict-surplus packet theorem.
"""

from __future__ import annotations

import random
from itertools import combinations

import networkx as nx


BASE_EDGES = {
    (0, 1), (0, 2), (0, 5), (0, 6), (1, 3), (1, 6), (1, 7),
    (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 7), (4, 5),
    (4, 6), (5, 6), (5, 7), (6, 7),
}
DEMANDS = ((0, 4), (1, 2), (3, 5))


def carrier_masks(graph: nx.Graph, rows: tuple[int, ...], demand: tuple[int, int]) -> list[int]:
    left, right = demand
    left_portals = sum(1 << v for v, row in enumerate(rows) if row & (1 << left))
    right_portals = sum(1 << v for v, row in enumerate(rows) if row & (1 << right))
    answer = []
    for mask in range(1, 1 << len(rows)):
        if not (mask & left_portals and mask & right_portals):
            continue
        vertices = [v for v in range(len(rows)) if mask & (1 << v)]
        if nx.is_connected(graph.subgraph(vertices)):
            answer.append(mask)
    # Every connected carrier contains an inclusion-minimal carrier, and
    # replacing a carrier by a subset preserves disjointness.  Keeping only
    # minimal masks makes the three-way search several orders faster.
    return [
        mask
        for mask in answer
        if not any(other != mask and other & mask == other for other in answer)
    ]


def linkage_status(graph: nx.Graph, rows: tuple[int, ...]) -> tuple[bool, bool]:
    carriers = [carrier_masks(graph, rows, demand) for demand in DEMANDS]
    pairwise = all(
        any(not (left & right) for left in carriers[i] for right in carriers[j])
        for i, j in combinations(range(3), 2)
    )
    triple = any(
        not (first & second) and not (first & third) and not (second & third)
        for first in carriers[0]
        for second in carriers[1]
        for third in carriers[2]
    )
    return pairwise, triple


def surplus_profile(graph: nx.Graph, rows: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    scores = []
    full = (1 << len(rows)) - 1
    for mask in range(1, full):
        vertices = {v for v in range(len(rows)) if mask & (1 << v)}
        internal = set().union(*(set(graph.neighbors(v)) for v in vertices)) - vertices
        boundary = 0
        for vertex in vertices:
            boundary |= rows[vertex]
        scores.append((len(internal) + boundary.bit_count(), mask))
    minimum = min(score for score, _ in scores)
    histogram = tuple(sorted(score for score, _ in scores))
    return minimum, histogram


def state_graph(edges: set[tuple[int, int]]) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(range(8))
    graph.add_edges_from(edges)
    return graph


def main() -> None:
    all_edges = set(combinations(range(8), 2))
    rng = random.Random(20260712)
    best = None
    for restart in range(20):
        edges = set(BASE_EDGES)
        # The first six vertices are the initial distinct portals; give the
        # singleton label 6 one random portal.
        rows = [1 << vertex if vertex < 6 else 0 for vertex in range(8)]
        rows[rng.randrange(8)] |= 1 << 6
        rows = tuple(rows)

        while True:
            graph = state_graph(edges)
            candidates = []
            for edge in all_edges - edges:
                new_edges = edges | {edge}
                new_graph = state_graph(new_edges)
                pairwise, triple = linkage_status(new_graph, rows)
                if pairwise and not triple:
                    score = surplus_profile(new_graph, rows)
                    candidates.append((score, "edge", edge, new_edges, rows))
            for vertex in range(8):
                for label in range(7):
                    if rows[vertex] & (1 << label):
                        continue
                    new_rows = list(rows)
                    new_rows[vertex] |= 1 << label
                    new_rows = tuple(new_rows)
                    pairwise, triple = linkage_status(graph, new_rows)
                    if pairwise and not triple:
                        score = surplus_profile(graph, new_rows)
                        candidates.append((score, "portal", (vertex, label), edges, new_rows))
            if not candidates:
                break
            candidates.sort(key=lambda item: item[0], reverse=True)
            top_score = candidates[0][0]
            elite = [item for item in candidates if item[0] == top_score]
            _, _, _, edges, rows = rng.choice(elite)
            if top_score[0] >= 8:
                print("STRICT COUNTEREXAMPLE", restart)
                print("edges", sorted(edges))
                print("rows", [[label for label in range(7) if row & (1 << label)] for row in rows])
                return

        graph = state_graph(edges)
        score = surplus_profile(graph, rows)
        if best is None or score > best[0]:
            best = (score, edges, rows)
            print("best", restart, score[0], score[1][:12])
    assert best is not None
    print("best edges", sorted(best[1]))
    print("best rows", [[label for label in range(7) if row & (1 << label)] for row in best[2]])


if __name__ == "__main__":
    main()
