#!/usr/bin/env python3
"""Classify all optional pole-defect descendants of the rank-(2,2) cut.

This is a discovery/audit tool, not a proof of the remaining cases.  It
records which of the 2^7 boundary patterns already have a two-full-shore
K7 quotient, which missing graphs are split (hence color-gluable in the
minor-critical application), and which survive the coherent orientation
(A,B)=(1,0).
"""

from __future__ import annotations

import itertools

import networkx as nx

from c6_rank22_nested_boundary_atlas import (
    BASE_MISSING,
    OPTIONAL_MISSING,
    bags,
    graph,
)
from contact_order7_all_unlabelled_atlas import quotient_edges
from contact_order7_five_edge_verify import k_minor_model


def is_split(g: nx.Graph) -> bool:
    forbidden = (
        nx.disjoint_union(nx.complete_graph(2), nx.complete_graph(2)),
        nx.cycle_graph(4),
        nx.cycle_graph(5),
    )
    for order, target in ((4, forbidden[0]), (4, forbidden[1]), (5, forbidden[2])):
        for vertices in itertools.combinations(g, order):
            if nx.is_isomorphic(g.subgraph(vertices), target):
                return False
    return True


def main() -> None:
    counts = {}
    residue = []
    for mask in range(1 << len(OPTIONAL_MISSING)):
        optional = {
            edge for index, edge in enumerate(OPTIONAL_MISSING) if mask >> index & 1
        }
        missing = graph(BASE_MISSING | optional)
        boundary = nx.complement(missing)
        model = k_minor_model(quotient_edges(boundary))
        positive = model is not None
        split = is_split(missing)

        # Normalize the unique pole orientation to (A,B)=(1,0).  The
        # opposite pin p-c2 and q-c5 cannot both be present.
        coherent = (1, 5) in optional or (3, 6) in optional
        key = (len(optional), positive, split, coherent)
        counts[key] = counts.get(key, 0) + 1
        if not positive and not split and coherent:
            residue.append(tuple(sorted(optional)))

    print("counts by (extra, quotient-K7, split, coherent)")
    for key in sorted(counts):
        print(key, counts[key])
    print("nonsplit coherent quotient-negative residue", len(residue))
    for state in residue:
        print(state)


if __name__ == "__main__":
    main()
