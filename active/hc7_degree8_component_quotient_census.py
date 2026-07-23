#!/usr/bin/env python3
"""Exact component-quotient census for degree-eight alpha=3 survivors.

In the promoted low-degree reduction, a degree-eight vertex v has at most two
components outside N[v].  Seven-connectivity makes every such component
adjacent to at least seven of the eight neighbours.  Contract each literal
component to one vertex; component vertices are pairwise nonadjacent and are
nonadjacent to v.

For every alpha=3, K4-free neighbourhood H not already closed by the
almost-dominating rooted-K5 criterion, test all one-component and two-component
quotients, allowing each component to miss zero or one boundary vertex.  The
K7-minus test is exact.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations, product
import json
import sys

import networkx as nx

from hc7_almost_dominating_rooted_k5_census import degree8_exit
from hc7_degree8_alpha3_virtual_edge_census import graph6, has_k4, independent, k7minus_model, encode_model


def quotient(H: nx.Graph, missed: tuple[int | None, ...]) -> nx.Graph:
    J = H.copy()
    v = 8
    J.add_node(v)
    J.add_edges_from((v, x) for x in range(8))
    for i, miss in enumerate(missed):
        c = 9 + i
        J.add_node(c)
        J.add_edges_from((c, x) for x in range(8) if x != miss)
    return J


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--survivor-limit", type=int, default=5000)
    args = parser.parse_args()

    counts = Counter()
    survivors = []
    certificates = []
    miss_options = (None,) + tuple(range(8))

    for raw in sys.stdin:
        raw = raw.strip()
        if not raw or raw.startswith(">>"):
            continue
        H = nx.from_graph6_bytes(raw.encode())
        H = nx.convert_node_labels_to_integers(H, ordering="sorted")
        if H.number_of_nodes() != 8:
            raise ValueError("expected order-eight catalogue")
        counts["graphs"] += 1

        triples = [S for S in combinations(H.nodes(), 3) if independent(H, S)]
        if not triples or any(independent(H, Q) for Q in combinations(H.nodes(), 4)):
            continue
        counts["alpha_three"] += 1
        if has_k4(H) or degree8_exit(H) is not None:
            continue
        counts["rooted_k5_survivors"] += 1

        one_bad = []
        one_cert = None
        for miss in miss_options:
            counts["one_component_states"] += 1
            model = k7minus_model(quotient(H, (miss,)))
            if model is None:
                one_bad.append(miss)
            elif one_cert is None:
                one_cert = {"missed": miss, "model": encode_model(model, 10)}
        if not one_bad:
            counts["one_component_closed_graphs"] += 1
        else:
            counts["one_component_surviving_graphs"] += 1

        two_bad = []
        two_cert = None
        for misses in product(miss_options, repeat=2):
            counts["two_component_states"] += 1
            model = k7minus_model(quotient(H, misses))
            if model is None:
                two_bad.append(list(misses))
            elif two_cert is None:
                two_cert = {"missed": list(misses), "model": encode_model(model, 11)}
        if not two_bad:
            counts["two_component_closed_graphs"] += 1
        else:
            counts["two_component_surviving_graphs"] += 1

        if one_bad or two_bad:
            counts["survivors"] += 1
            if len(survivors) < args.survivor_limit:
                survivors.append({
                    "H": graph6(H),
                    "edges": H.number_of_edges(),
                    "degree_sequence": sorted(dict(H.degree()).values()),
                    "one_bad": one_bad,
                    "two_bad_count": len(two_bad),
                    "two_bad_sample": two_bad[:100],
                })
        else:
            counts["fully_closed"] += 1
            if len(certificates) < 30:
                certificates.append({"H": graph6(H), "one": one_cert, "two": two_cert})

    print(json.dumps({
        "counts": dict(sorted(counts.items())),
        "survivors_truncated": counts["survivors"] > len(survivors),
        "survivors": survivors,
        "sample_certificates": certificates,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
