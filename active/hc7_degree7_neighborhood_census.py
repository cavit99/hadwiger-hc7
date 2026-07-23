#!/usr/bin/env python3
"""Exact degree-seven neighbourhood census for a K7-minus-free host.

For every unlabelled graph H on seven vertices:
  * retain alpha(H)<=2, as forced by 7-contraction-criticality;
  * add a universal vertex v;
  * retain only graphs H+v with no K7-minus minor;
  * count the K4 subgraphs of H, equivalently the K5 subgraphs through v.

The minor search is exact over all partitions of arbitrary vertex subsets into
seven connected branch sets.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
import json
import sys

import networkx as nx

from hc7_degree8_alpha3_virtual_edge_census import graph6, independent, k7minus_model


def alpha_at_most_two(H: nx.Graph) -> bool:
    return not any(independent(H, triple) for triple in combinations(H.nodes(), 3))


def k4s(H: nx.Graph) -> list[tuple[int, int, int, int]]:
    return [Q for Q in combinations(H.nodes(), 4) if all(H.has_edge(x, y) for x, y in combinations(Q, 2))]


def main() -> None:
    counts = Counter()
    survivors = []
    signatures = Counter()

    for raw in sys.stdin:
        raw = raw.strip()
        if not raw or raw.startswith(">>"):
            continue
        H = nx.from_graph6_bytes(raw.encode())
        H = nx.convert_node_labels_to_integers(H, ordering="sorted")
        if H.number_of_nodes() != 7:
            raise ValueError("expected order-seven catalogue")
        counts["graphs"] += 1
        if not alpha_at_most_two(H):
            continue
        counts["alpha_at_most_two"] += 1

        J = H.copy()
        J.add_node(7)
        J.add_edges_from((7, x) for x in range(7))
        if k7minus_model(J) is not None:
            counts["local_k7minus_positive"] += 1
            continue

        cliques = k4s(H)
        counts["local_survivors"] += 1
        counts[f"k4_count_{len(cliques)}"] += 1
        signature = (
            len(cliques),
            H.number_of_edges(),
            tuple(sorted(dict(H.degree()).values())),
            tuple(sorted(len(C) for C in nx.connected_components(nx.complement(H)))),
        )
        signatures[signature] += 1
        survivors.append({
            "H": graph6(H),
            "k4s": [list(Q) for Q in cliques],
            "edges": H.number_of_edges(),
            "degree_sequence": sorted(dict(H.degree()).values()),
            "complement_components": sorted(len(C) for C in nx.connected_components(nx.complement(H))),
        })

    print(json.dumps({
        "counts": dict(sorted(counts.items())),
        "signature_counts": [
            {"signature": [sig[0], sig[1], list(sig[2]), list(sig[3])], "count": count}
            for sig, count in sorted(signatures.items())
        ],
        "survivors": survivors,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
