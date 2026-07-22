#!/usr/bin/env python3
"""Exact local census for a degree-eight vertex in a hypothetical
7-contraction-critical K7-minus-minor-free graph.

Let x have degree eight and let H=G[N(x)].  Dirac gives alpha(H)<=3.  This
experiment treats the difficult equality case alpha(H)=3 and assumes H is
K4-free.  For every independent triple S of H, the Rolek--Song path lemma
makes every matching M of missing edges in H-S simultaneously liftable by
pairwise vertex-disjoint paths whose interiors avoid N[x].

For each H and S we therefore add every such matching M, join a new vertex x
to all of H, and run an exact K7-minus minor search.  If one model exists, it
lifts verbatim to the host by replacing the added matching edges with the
Rolek--Song paths.  A graph H survives only when no independent triple and no
matching of its remaining five vertices yields a K7-minus model.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
from itertools import combinations
import json
import sys

import networkx as nx


def graph6(graph: nx.Graph) -> str:
    return nx.to_graph6_bytes(graph, header=False).decode().strip()


def adjacency_masks(graph: nx.Graph) -> tuple[int, ...]:
    n = graph.number_of_nodes()
    assert tuple(sorted(graph.nodes())) == tuple(range(n))
    masks = [0] * n
    for u, v in graph.edges():
        masks[u] |= 1 << v
        masks[v] |= 1 << u
    return tuple(masks)


@lru_cache(maxsize=None)
def partitions_with_unused(n: int, k: int) -> tuple[tuple[int, ...], ...]:
    labels = [-2] * n
    result: list[tuple[int, ...]] = []

    def rec(i: int, used: int) -> None:
        if used > k or used + (n - i) < k:
            return
        if i == n:
            if used == k:
                blocks = [0] * k
                for v, label in enumerate(labels):
                    if label >= 0:
                        blocks[label] |= 1 << v
                result.append(tuple(blocks))
            return
        labels[i] = -1
        rec(i + 1, used)
        for label in range(used):
            labels[i] = label
            rec(i + 1, used)
        if used < k:
            labels[i] = used
            rec(i + 1, used + 1)
        labels[i] = -2

    rec(0, 0)
    result.sort(key=lambda blocks: (sum(b.bit_count() for b in blocks), blocks))
    return tuple(result)


def connected_neighbour_tables(adj: tuple[int, ...]) -> tuple[list[bool], list[int]]:
    n = len(adj)
    connected = [False] * (1 << n)
    neighbours = [0] * (1 << n)
    for mask in range(1, 1 << n):
        seed = mask & -mask
        seen = seed
        while True:
            nxt = seen
            todo = seen
            while todo:
                bit = todo & -todo
                todo -= bit
                nxt |= adj[bit.bit_length() - 1] & mask
            if nxt == seen:
                break
            seen = nxt
        connected[mask] = seen == mask
        hood = 0
        todo = mask
        while todo:
            bit = todo & -todo
            todo -= bit
            hood |= adj[bit.bit_length() - 1]
        neighbours[mask] = hood & ~mask
    return connected, neighbours


def k7minus_model(graph: nx.Graph) -> tuple[int, ...] | None:
    n = graph.number_of_nodes()
    adj = adjacency_masks(graph)
    connected, neighbours = connected_neighbour_tables(adj)
    for blocks in partitions_with_unused(n, 7):
        if any(not connected[b] for b in blocks):
            continue
        missing = 0
        for i, j in combinations(range(7), 2):
            if not (neighbours[blocks[i]] & blocks[j]):
                missing += 1
                if missing > 1:
                    break
        if missing <= 1:
            return blocks
    return None


def independent(graph: nx.Graph, vertices: tuple[int, ...]) -> bool:
    return all(not graph.has_edge(u, v) for u, v in combinations(vertices, 2))


def has_k4(graph: nx.Graph) -> bool:
    return any(
        all(graph.has_edge(u, v) for u, v in combinations(vertices, 2))
        for vertices in combinations(graph.nodes(), 4)
    )


def matchings(edges: list[tuple[int, int]]) -> list[tuple[tuple[int, int], ...]]:
    output: list[tuple[tuple[int, int], ...]] = [tuple()]
    for size in (1, 2):
        for chosen in combinations(edges, size):
            endpoints = [v for edge in chosen for v in edge]
            if len(set(endpoints)) == 2 * size:
                output.append(chosen)
    return output


def encode_model(blocks: tuple[int, ...] | None, n: int) -> list[list[int]] | None:
    if blocks is None:
        return None
    return [[v for v in range(n) if block & (1 << v)] for block in blocks]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--survivor-limit", type=int, default=1000)
    args = parser.parse_args()

    counts = Counter()
    survivors: list[dict[str, object]] = []
    certificates: list[dict[str, object]] = []

    for raw in sys.stdin:
        raw = raw.strip()
        if not raw or raw.startswith(">>"):
            continue
        H = nx.from_graph6_bytes(raw.encode())
        H = nx.convert_node_labels_to_integers(H, ordering="sorted")
        if H.number_of_nodes() != 8:
            raise ValueError("expected order-eight graph catalogue")
        counts["graphs"] += 1

        independent_triples = [
            S for S in combinations(range(8), 3) if independent(H, S)
        ]
        if not independent_triples:
            continue
        if any(independent(H, S) for S in combinations(range(8), 4)):
            continue
        counts["alpha3"] += 1
        if has_k4(H):
            counts["k4_positive"] += 1
            continue
        counts["alpha3_k4free"] += 1

        found: dict[str, object] | None = None
        for S in independent_triples:
            R = sorted(set(range(8)) - set(S))
            missing = [
                (u, v) for u, v in combinations(R, 2) if not H.has_edge(u, v)
            ]
            for M in matchings(missing):
                counts["tested_states"] += 1
                augmented = H.copy()
                augmented.add_edges_from(M)
                augmented.add_node(8)
                augmented.add_edges_from((8, v) for v in range(8))
                model = k7minus_model(augmented)
                if model is not None:
                    found = {
                        "H": graph6(H),
                        "S": list(S),
                        "M": [list(edge) for edge in M],
                        "model": encode_model(model, 9),
                    }
                    break
            if found is not None:
                break

        if found is None:
            counts["survivors"] += 1
            if len(survivors) < args.survivor_limit:
                survivors.append(
                    {
                        "H": graph6(H),
                        "independent_triples": [list(S) for S in independent_triples],
                        "edges": H.number_of_edges(),
                        "degree_sequence": sorted(dict(H.degree()).values()),
                        "complement_components": sorted(
                            len(C) for C in nx.connected_components(nx.complement(H))
                        ),
                    }
                )
        else:
            counts["virtual_edge_positive"] += 1
            if len(certificates) < 20:
                certificates.append(found)

    print(
        json.dumps(
            {
                "counts": dict(sorted(counts.items())),
                "partition_count": len(partitions_with_unused(9, 7)),
                "survivors_truncated": counts["survivors"] > len(survivors),
                "survivors": survivors,
                "sample_certificates": certificates,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
