#!/usr/bin/env python3
"""Exact star-forest closure for the degree-eight alpha-three residue.

Let x have degree eight in a 7-contraction-critical graph, let H=G[N(x)],
and let S be an independent triple.  Rolek--Song Lemma 1.7 supplies one
outside path for every selected missing edge of H-S.  Paths belonging to
edges with four distinct ends are vertex-disjoint.

Consequently every missing-edge *star forest* F in H-S is simultaneously
liftable: for each nontrivial star component, the union of its paths after
removing the leaf endpoints is connected and can be contracted onto the
star centre; different components have disjoint endpoint sets and hence
vertex-disjoint path unions.  A matching is the special case in which every
component has one edge.

For each order-eight H with alpha(H)=3 and no K4, and each independent
triple S, this script tests every inclusion-maximal liftable star forest F
of missing edges in H-S.  It adds F, adds the universal vertex x, and runs
the exact K7-minus branch-set search from the matching census.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations
import json
import sys

import networkx as nx

from hc7_degree8_alpha3_virtual_edge_census import (
    encode_model,
    graph6,
    has_k4,
    independent,
    k7minus_model,
    partitions_with_unused,
)


def is_star_forest(vertices: list[int], edges: tuple[tuple[int, int], ...]) -> bool:
    graph = nx.Graph()
    graph.add_nodes_from(vertices)
    graph.add_edges_from(edges)
    for component in nx.connected_components(graph):
        if len(component) <= 2:
            continue
        degrees = sorted((graph.degree(v) for v in component), reverse=True)
        # A connected graph on r>=3 vertices is a star iff its degree sequence
        # is (r-1,1,...,1).
        if degrees != [len(component) - 1] + [1] * (len(component) - 1):
            return False
    return True


def maximal_star_forests(vertices: list[int], missing: list[tuple[int, int]]) -> list[tuple[tuple[int, int], ...]]:
    forests: list[frozenset[tuple[int, int]]] = []
    for mask in range(1 << len(missing)):
        chosen = tuple(missing[i] for i in range(len(missing)) if mask & (1 << i))
        if is_star_forest(vertices, chosen):
            forests.append(frozenset(chosen))

    maximal = [
        forest
        for forest in forests
        if not any(forest < other for other in forests)
    ]
    return [tuple(sorted(forest)) for forest in sorted(maximal, key=lambda f: (len(f), sorted(f)))]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--survivor-limit", type=int, default=2000)
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

        independent_triples = [S for S in combinations(range(8), 3) if independent(H, S)]
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
        state_count = 0
        max_forest_size = 0
        for S in independent_triples:
            R = sorted(set(range(8)) - set(S))
            missing = [(u, v) for u, v in combinations(R, 2) if not H.has_edge(u, v)]
            forests = maximal_star_forests(R, missing)
            counts["independent_triple_states"] += 1
            counts["maximal_star_forests"] += len(forests)
            for forest in forests:
                state_count += 1
                max_forest_size = max(max_forest_size, len(forest))
                counts["tested_states"] += 1
                augmented = H.copy()
                augmented.add_edges_from(forest)
                augmented.add_node(8)
                augmented.add_edges_from((8, v) for v in range(8))
                model = k7minus_model(augmented)
                if model is not None:
                    found = {
                        "H": graph6(H),
                        "S": list(S),
                        "F": [list(edge) for edge in forest],
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
                        "tested_states": state_count,
                        "max_forest_size": max_forest_size,
                    }
                )
        else:
            counts["star_forest_positive"] += 1
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
