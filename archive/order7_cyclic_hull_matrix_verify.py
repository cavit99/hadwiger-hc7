#!/usr/bin/env python3
"""Exact verifier for the seven-boundary cyclic-hull matrix lemma.

After choosing an induced four-vertex Földes--Hammer core, failure of the
core itself to leave a two-colourable omitted triple means that triple is
independent in the missing graph.  The only remaining data are the twelve
core--triple incidences.  This script checks those 2*2^12 matrices, not the
783 unlabelled boundary atlas.
"""

from __future__ import annotations

import itertools
from collections import Counter

import networkx as nx

import contact_order7_sixedge_web_probe as web
from contact_order7_five_edge_verify import (
    as_sets,
    edge_mask,
    quotient_edges,
    verify_model,
)
from order7_induced_core_direct_atlas import routing_frame


S = tuple(range(7))
R = (0, 1, 2, 3)
Z = (4, 5, 6)
PAIRS = set(itertools.combinations(S, 2))
CROSS = tuple((r, z) for r in R for z in Z)
CORES = {
    "2K2": {(0, 1), (2, 3)},
    "C4": {(0, 1), (1, 2), (2, 3), (0, 3)},
}


def special_graph() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(S)
    graph.add_edges_from(((0, 1), (1, 2), (0, 2),
                          (3, 4), (4, 5), (3, 5)))
    return graph


def main() -> None:
    special = special_graph()
    counts = Counter()
    exceptional_masks = Counter()
    for name, core in CORES.items():
        for bits in range(1 << len(CROSS)):
            missing_edges = set(core)
            missing_edges.update(CROSS[i] for i in range(len(CROSS))
                                 if bits >> i & 1)
            missing = nx.Graph()
            missing.add_nodes_from(S)
            missing.add_edges_from(missing_edges)
            boundary = nx.complement(missing)
            counts[(name, "matrices")] += 1

            missing_mask = edge_mask(missing_edges)
            model = web.quotient_model(missing_mask)
            if model is not None:
                verify_model(quotient_edges(missing_mask), as_sets(model))
                counts[(name, "quotient_positive")] += 1
                continue
            counts[(name, "quotient_negative")] += 1

            if routing_frame(boundary) is not None:
                counts[(name, "cyclic_hull")] += 1
                continue

            assert nx.is_isomorphic(missing, special), (
                name, bits, sorted(missing_edges),
            )
            counts[(name, "exception")] += 1
            exceptional_masks[name] += 1

    print("verified 2 x 2^12 core--triple incidence matrices")
    for key in sorted(counts):
        print(key, counts[key])
    print("all quotient-negative no-hull matrices are 2K3+K1")
    print("labelled exceptional matrices", dict(exceptional_masks))


if __name__ == "__main__":
    main()
