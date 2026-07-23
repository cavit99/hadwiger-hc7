#!/usr/bin/env python3
"""Exact liftable-block census for the degree-eight alpha=3 residue.

Let x be a degree-eight vertex of a 7-contraction-critical graph, H=G[N(x)],
and S an independent triple.  Put R=N(x)-S, so |R|=5.  Every nonempty block
B contained in R is a valid connected branch set in the host:

* choose any spanning tree of the complete graph on B;
* retain its edges that already belong to H;
* for every missing tree edge use the path supplied by Rolek--Song Lemma 1.7;
* paths for missing edges inside one block may overlap, but their union with B
  is connected;
* missing-edge trees belonging to distinct blocks have disjoint endpoint sets,
  so all of their path systems are vertex-disjoint.

Thus six blocks on N(x), with every nonsingleton block contained in R and at
most one missing cross-block adjacency in H, lift to a K6-minus model in
G-x.  Adding singleton {x} gives a K7-minus model.

The census checks whether every eight-vertex H with alpha(H)=3 and no K4 has
such a partition for at least one independent triple S.
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


def adjacent(H: nx.Graph, left: tuple[int, ...], right: tuple[int, ...]) -> bool:
    return any(H.has_edge(u, v) for u in left for v in right)


def find_model(H: nx.Graph, S: tuple[int, int, int]) -> tuple[tuple[int, ...], ...] | None:
    for blocks in partitions_with_unused(tuple(range(8)), 6):
        # Virtual paths are guaranteed only for endpoints in R=N(x)-S.
        if any(len(block) > 1 and any(v in S for v in block) for block in blocks):
            continue
        missing = 0
        for i, j in combinations(range(6), 2):
            if not adjacent(H, blocks[i], blocks[j]):
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
                found = {"H": graph6(H), "S": list(S), "blocks": [list(b) for b in model]}
                break

        if found is None:
            counts["survivors"] += 1
            if len(survivors) < args.survivor_limit:
                survivors.append({
                    "H": graph6(H),
                    "independent_triples": [list(S) for S in triples],
                    "edges": H.number_of_edges(),
                    "degree_sequence": sorted(dict(H.degree()).values()),
                    "complement_components": sorted(
                        len(C) for C in nx.connected_components(nx.complement(H))
                    ),
                })
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
