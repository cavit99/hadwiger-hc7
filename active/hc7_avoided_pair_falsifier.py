#!/usr/bin/env python3
"""Exact small-order falsifier for the avoided-pair HC7 target.

Input is a graph6 stream.  With ``--complements`` each input graph is first
complemented, which is convenient when enumerating seven-connected hosts.
The search reports a graph precisely when it is seven-connected,
K7-minor-free, contains K7^vee as a minor, and every two-vertex deletion
still contains a K5 minor.
"""

from __future__ import annotations

import argparse
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from pathlib import Path
import sys

import networkx as nx


ORACLE_PATH = Path(__file__).parents[1] / "barriers" / "hc7_broad_near_k7_falsifier.py"
SPEC = spec_from_file_location("broad_near_k7_oracle", ORACLE_PATH)
assert SPEC is not None and SPEC.loader is not None
ORACLE = module_from_spec(SPEC)
SPEC.loader.exec_module(ORACLE)


def has_clique_minor(graph: nx.Graph, order: int) -> bool:
    if len(graph) < order or not nx.is_connected(graph):
        return False
    if any(len(clique) >= order for clique in nx.find_cliques(graph)):
        return True
    for _, quotient in ORACLE.spanning_quotients(graph, order):
        if all(row.bit_count() == order - 1 for row in quotient):
            return True
    return False


def avoided_pairs(graph: nx.Graph) -> list[tuple[object, object]]:
    vertices = tuple(graph)
    answer = []
    for pair in combinations(vertices, 2):
        remainder = graph.subgraph(set(vertices) - set(pair)).copy()
        if not has_clique_minor(remainder, 5):
            answer.append(pair)
    return answer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--complements", action="store_true")
    parser.add_argument("--stop", action="store_true")
    args = parser.parse_args()

    counts: dict[str, int] = {}
    for raw in sys.stdin.buffer:
        raw = raw.strip()
        if not raw:
            continue
        graph = nx.from_graph6_bytes(raw)
        if args.complements:
            graph = nx.complement(graph)
        if nx.node_connectivity(graph) < 7:
            counts["connectivity<7"] = counts.get("connectivity<7", 0) + 1
            continue
        if any(len(clique) >= 7 for clique in nx.find_cliques(graph)):
            counts["has-K7"] = counts.get("has-K7", 0) + 1
            continue
        pair_list = avoided_pairs(graph)
        if pair_list:
            counts["has-avoided-pair"] = counts.get("has-avoided-pair", 0) + 1
            continue
        k7, vee, _ = ORACLE.exact_minor_models(graph)
        if k7 is not None:
            counts["has-K7"] = counts.get("has-K7", 0) + 1
            continue
        if vee is None:
            counts["no-K7vee"] = counts.get("no-K7vee", 0) + 1
            continue
        code = nx.to_graph6_bytes(graph, header=False).decode().strip()
        print(
            {
                "graph6": code,
                "order": len(graph),
                "size": graph.number_of_edges(),
                "kappa": nx.node_connectivity(graph),
                "vee_model": vee,
            },
            flush=True,
        )
        counts["counterexample"] = counts.get("counterexample", 0) + 1
        if args.stop:
            break
    print(counts)


if __name__ == "__main__":
    main()
