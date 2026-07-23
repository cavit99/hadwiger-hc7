#!/usr/bin/env python3
"""Finite check for the almost-dominating rooted-K5 exit.

Degree seven.  If H=G[N(v)] has alpha(H)<=2 and no K4, choose a nonedge ab,
put U=V(H)-{a,b}, and use the promoted degree-seven rooted-K5 theorem on U.
If a is nonadjacent to at most one vertex of U, then the seven bags

    {v}, {a}, (B_u : u in U)

form K7-minus.  This census checks that every order-seven alpha<=2 K4-free
H has such an oriented nonedge.

Degree eight, alpha three.  For every independent triple S and U=V(H)-S,
Rolek--Song supplies all missing-edge paths on U.  If the missing graph on U
has at most six edges, Kriesell--Mohr Theorem 7 packages a U-rooted K5.  If
some a in S is nonadjacent to at most one vertex of U, then {v},{a}, and the
five rooted bags form K7-minus.  This census records the exact survivors.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations
import json
import sys

import networkx as nx

from hc7_degree8_alpha3_virtual_edge_census import graph6, has_k4, independent


def degree7_exit(H: nx.Graph) -> dict[str, object] | None:
    for a, b in combinations(H.nodes(), 2):
        if H.has_edge(a, b):
            continue
        U = sorted(set(H.nodes()) - {a, b})
        misses = [u for u in U if not H.has_edge(a, u)]
        if len(misses) <= 1:
            return {"a": a, "b": b, "U": U, "misses": misses}
        misses = [u for u in U if not H.has_edge(b, u)]
        if len(misses) <= 1:
            return {"a": b, "b": a, "U": U, "misses": misses}
    return None


def degree8_exit(H: nx.Graph) -> dict[str, object] | None:
    for S in combinations(H.nodes(), 3):
        if not independent(H, S):
            continue
        U = sorted(set(H.nodes()) - set(S))
        missing_edges = [e for e in combinations(U, 2) if not H.has_edge(*e)]
        if len(missing_edges) > 6:
            continue
        for a in S:
            misses = [u for u in U if not H.has_edge(a, u)]
            if len(misses) <= 1:
                return {
                    "S": list(S),
                    "a": a,
                    "U": U,
                    "root_missing_edges": [list(e) for e in missing_edges],
                    "misses": misses,
                }
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, choices=(7, 8), required=True)
    args = parser.parse_args()
    n = args.order

    counts = Counter()
    survivors = []
    certificates = []

    for raw in sys.stdin:
        raw = raw.strip()
        if not raw or raw.startswith(">>"):
            continue
        H = nx.from_graph6_bytes(raw.encode())
        H = nx.convert_node_labels_to_integers(H, ordering="sorted")
        if H.number_of_nodes() != n:
            raise ValueError("wrong catalogue order")
        counts["graphs"] += 1

        if n == 7:
            if any(independent(H, S) for S in combinations(H.nodes(), 3)):
                continue
            counts["alpha_at_most_two"] += 1
            if has_k4(H):
                counts["k4_positive"] += 1
                continue
            counts["k4_free"] += 1
            cert = degree7_exit(H)
        else:
            triples = [S for S in combinations(H.nodes(), 3) if independent(H, S)]
            if not triples or any(independent(H, Q) for Q in combinations(H.nodes(), 4)):
                continue
            counts["alpha_three"] += 1
            if has_k4(H):
                counts["k4_positive"] += 1
                continue
            counts["k4_free"] += 1
            cert = degree8_exit(H)

        if cert is None:
            counts["survivors"] += 1
            survivors.append({
                "H": graph6(H),
                "edges": H.number_of_edges(),
                "degree_sequence": sorted(dict(H.degree()).values()),
                "complement_components": sorted(len(C) for C in nx.connected_components(nx.complement(H))),
            })
        else:
            counts["rooted_k5_exit"] += 1
            if len(certificates) < 100:
                certificates.append({"H": graph6(H), **cert})

    print(json.dumps({
        "order": n,
        "counts": dict(sorted(counts.items())),
        "survivors": survivors,
        "sample_certificates": certificates,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
