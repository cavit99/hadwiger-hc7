#!/usr/bin/env python3
"""Exact complement-connected block census for the degree-eight alpha=3 case.

Let x be a degree-eight vertex of a 7-contraction-critical graph, H=G[N(x)],
and S an independent triple.  Rolek--Song Lemma 1.7 applies to every set M
of missing edges in H-S.  If B is a subset of N(x)-S for which the complement
of H[B] is connected, choose a spanning tree T_B of that complement.  The
paths supplied for T_B have union connected with B, so that union is one
valid branch set.  For pairwise disjoint blocks B, the chosen trees have
disjoint endpoint sets; hence all path unions for different blocks are
vertex-disjoint.  Thus any partition into complement-connected blocks lifts
exactly, without assuming paths sharing an endpoint are internally disjoint.

This census asks whether every order-eight graph H with alpha(H)=3 and no K4
has an independent triple S such that H-S admits six nonempty pairwise
adjacent blocks, with at most one missing block adjacency, and each
non-singleton block complement-connected.  Adding singleton {x} then gives a
K7-minus model in the host.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
from itertools import combinations
import json
import sys

import networkx as nx

from hc7_degree8_alpha3_virtual_edge_census import graph6, has_k4, independent


@lru_cache(maxsize=None)
def partitions_with_unused(vertices: tuple[int, ...], k: int) -> tuple[tuple[tuple[int, ...], ...], ...]:
    """All unordered partitions of an arbitrary subset into exactly k blocks."""
    n = len(vertices)
    labels = [-2] * n
    output: list[tuple[tuple[int, ...], ...]] = []

    def rec(i: int, used: int) -> None:
        if used > k or used + (n - i) < k:
            return
        if i == n:
            if used != k:
                return
            blocks = [[] for _ in range(k)]
            for pos, label in enumerate(labels):
                if label >= 0:
                    blocks[label].append(vertices[pos])
            output.append(tuple(tuple(block) for block in blocks))
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
    output.sort(key=lambda p: (sum(len(b) for b in p), p))
    return tuple(output)


def complement_connected(H: nx.Graph, block: tuple[int, ...]) -> bool:
    if len(block) == 1:
        return True
    return nx.is_connected(nx.complement(H.subgraph(block)))


def blocks_adjacent(H: nx.Graph, left: tuple[int, ...], right: tuple[int, ...]) -> bool:
    return any(H.has_edge(u, v) for u in left for v in right)


def find_model(H: nx.Graph, S: tuple[int, int, int]) -> tuple[tuple[int, ...], ...] | None:
    R = tuple(sorted(set(H.nodes()) - set(S)))
    # The Rolek--Song paths are guaranteed only for endpoints in R=H-S.
    # Vertices of S may still be used as singleton branch sets.
    universe = tuple(sorted(H.nodes()))
    for blocks in partitions_with_unused(universe, 6):
        if any(len(block) > 1 and any(v in S for v in block) for block in blocks):
            continue
        if any(not complement_connected(H, block) for block in blocks):
            continue
        missing = 0
        for i, j in combinations(range(6), 2):
            if not blocks_adjacent(H, blocks[i], blocks[j]):
                missing += 1
                if missing > 1:
                    break
        if missing <= 1:
            return blocks
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--survivor-limit", type=int, default=3000)
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

        triples = [S for S in combinations(range(8), 3) if independent(H, S)]
        if not triples:
            continue
        if any(independent(H, Q) for Q in combinations(range(8), 4)):
            continue
        counts["alpha3"] += 1
        if has_k4(H):
            counts["k4_positive"] += 1
            continue
        counts["alpha3_k4free"] += 1

        found = None
        for S in triples:
            counts["tested_triples"] += 1
            model = find_model(H, S)
            if model is not None:
                found = {
                    "H": graph6(H),
                    "S": list(S),
                    "blocks": [list(block) for block in model],
                }
                break

        if found is None:
            counts["survivors"] += 1
            if len(survivors) < args.survivor_limit:
                survivors.append(
                    {
                        "H": graph6(H),
                        "independent_triples": [list(S) for S in triples],
                        "edges": H.number_of_edges(),
                        "degree_sequence": sorted(dict(H.degree()).values()),
                        "complement_components": sorted(
                            len(C) for C in nx.connected_components(nx.complement(H))
                        ),
                    }
                )
        else:
            counts["positive"] += 1
            if len(certificates) < 30:
                certificates.append(found)

    print(json.dumps({
        "counts": dict(sorted(counts.items())),
        "survivors_truncated": counts["survivors"] > len(survivors),
        "survivors": survivors,
        "sample_certificates": certificates,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
