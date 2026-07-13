#!/usr/bin/env python3
"""Exact boundary audit for a canonical rank-(2,2) C6 transition.

After descending into one component of the canonical two-cut state, the
new seven-boundary missing graph has a fixed six-edge core.  The only
additional missing edges are the six permitted pole--boundary contacts and
the pole edge.  This verifier checks the base quotient and identifies all
seven one-extra-defect graphs in the audited seven-edge atlas.
"""

from __future__ import annotations

import networkx as nx

from contact_order7_all_unlabelled_atlas import quotient_edges
from contact_order7_five_edge_verify import k_minor_model
from equality_gate_seven_edge_packet_atlas import (
    DIRECT_WITNESSES,
    NONBIPARTITE_COMPATIBILITY,
    seven_edge_types,
)


# Vertices are (c0,c2,c3,c5,z,p,q) = (0,1,2,3,4,5,6).
BASE_MISSING = {
    (1, 2),  # c2 c3
    (0, 3),  # c0 c5
    (0, 5), (2, 5),  # p misses c0,c3
    (0, 6), (2, 6),  # q misses c0,c3
}

OPTIONAL_MISSING = (
    (1, 5), (3, 5), (4, 5),  # p may miss c2,c5,z
    (1, 6), (3, 6), (4, 6),  # q may miss c2,c5,z
    (5, 6),                   # pq may be absent
)


def graph(edges: set[tuple[int, int]]) -> nx.Graph:
    answer = nx.Graph()
    answer.add_nodes_from(range(7))
    answer.add_edges_from(edges)
    return answer


def bags(model: list[int] | tuple[int, ...], order: int = 9):
    return tuple(
        tuple(vertex for vertex in range(order) if mask >> vertex & 1)
        for mask in model
    )


def main() -> None:
    base = graph(BASE_MISSING)
    boundary = nx.complement(base)
    model = k_minor_model(quotient_edges(boundary))
    assert model is not None
    assert bags(model) == (
        (1,), (3,), (4,), (5,), (6,), (7,), (0, 8)
    )

    types = seven_edge_types()
    manifest = {}
    for missing_edge in OPTIONAL_MISSING:
        candidate = graph(BASE_MISSING | {missing_edge})
        indices = tuple(
            index for index, representative in enumerate(types)
            if nx.is_isomorphic(candidate, representative)
        )
        assert len(indices) == 1
        index = indices[0]
        if missing_edge == (5, 6):
            assert index in NONBIPARTITE_COMPATIBILITY
            status = "compatibility-descent"
        else:
            assert index in DIRECT_WITNESSES
            status = "direct-cyclic-hull"
        manifest[missing_edge] = (index, status)

    assert {index for index, _ in manifest.values()} == {1, 4, 13}
    print("base K7 bags", bags(model))
    print("one-extra-defect manifest", manifest)


if __name__ == "__main__":
    main()
