#!/usr/bin/env python3
"""Exact Rolek--Song matching census at a degree-seven vertex.

Let v have degree seven in a 7-contraction-critical graph and H=G[N(v)].
Dirac gives alpha(H)<=2.  For every independent pair S in H, Rolek--Song
Lemma 1.7 supplies outside paths for any matching M of missing edges in H-S,
with the paths pairwise vertex-disjoint.  Therefore every K7-minus model in
H+v+M lifts exactly to the host.

The census retains H with fewer than two K4 subgraphs and asks whether some
independent pair and missing-edge matching already yields K7-minus.  Graphs
with alpha(H)=1 are complete and have many K4s, so every relevant graph has
an independent pair.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
import json
import sys

import networkx as nx

from hc7_degree8_alpha3_virtual_edge_census import (
    encode_model,
    graph6,
    independent,
    k7minus_model,
    matchings,
)


def k4s(H: nx.Graph) -> list[tuple[int, int, int, int]]:
    return [Q for Q in combinations(H.nodes(), 4) if all(H.has_edge(x, y) for x, y in combinations(Q, 2))]


def main() -> None:
    counts = Counter()
    survivors = []
    certificates = []

    for raw in sys.stdin:
        raw = raw.strip()
        if not raw or raw.startswith(">>"):
            continue
        H = nx.from_graph6_bytes(raw.encode())
        H = nx.convert_node_labels_to_integers(H, ordering="sorted")
        if H.number_of_nodes() != 7:
            raise ValueError("expected order-seven catalogue")
        counts["graphs"] += 1

        if any(independent(H, triple) for triple in combinations(range(7), 3)):
            continue
        counts["alpha_at_most_two"] += 1
        cliques = k4s(H)
        if len(cliques) >= 2:
            counts["two_k4_positive"] += 1
            continue
        counts[f"input_k4_{len(cliques)}"] += 1

        found = None
        pairs = [S for S in combinations(range(7), 2) if independent(H, S)]
        for S in pairs:
            R = sorted(set(range(7)) - set(S))
            missing = [(x, y) for x, y in combinations(R, 2) if not H.has_edge(x, y)]
            for M in matchings(missing):
                counts["tested_states"] += 1
                J = H.copy()
                J.add_edges_from(M)
                J.add_node(7)
                J.add_edges_from((7, x) for x in range(7))
                model = k7minus_model(J)
                if model is not None:
                    found = {
                        "H": graph6(H),
                        "S": list(S),
                        "M": [list(e) for e in M],
                        "model": encode_model(model, 8),
                        "input_k4_count": len(cliques),
                    }
                    break
            if found is not None:
                break

        if found is None:
            counts["survivors"] += 1
            counts[f"survivor_k4_{len(cliques)}"] += 1
            survivors.append({
                "H": graph6(H),
                "k4s": [list(Q) for Q in cliques],
                "independent_pairs": [list(S) for S in pairs],
                "edges": H.number_of_edges(),
                "degree_sequence": sorted(dict(H.degree()).values()),
                "complement_components": sorted(len(C) for C in nx.connected_components(nx.complement(H))),
            })
        else:
            counts["virtual_matching_positive"] += 1
            if len(certificates) < 50:
                certificates.append(found)

    print(json.dumps({
        "counts": dict(sorted(counts.items())),
        "survivors": survivors,
        "sample_certificates": certificates,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
