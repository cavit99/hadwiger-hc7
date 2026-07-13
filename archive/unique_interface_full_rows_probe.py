#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["networkx"]
# ///
"""Exact atlas check for the unique-interface, two-full-row quotient.

The seven boundary vertices are 0,...,6.  Vertex 7 is the opposite full
shore.  Vertices 8 and 9 are the two pieces of the crossed shore; both are
full to the boundary and 8--9 is the unique interface edge.  We restrict to
boundary graphs whose missing graph is nonsplit and whose ordinary
two-full-shore quotient (helpers 7 and 8, nonadjacent) is K7-minor-free.
"""

from __future__ import annotations

from collections import Counter

import networkx as nx

from contact_order7_all_unlabelled_atlas import is_split
from contact_order7_sixedge_web_probe import generic_minor_model


S = tuple(range(7))


def edges_with_helpers(boundary: nx.Graph, split: bool) -> set[tuple[int, int]]:
    edges = {tuple(sorted(edge)) for edge in boundary.edges()}
    if split:
        helpers = (7, 8, 9)
        edges.add((8, 9))
    else:
        helpers = (7, 8)
    edges.update((s, h) for s in S for h in helpers)
    return {tuple(sorted(edge)) for edge in edges}


def main() -> None:
    counts = Counter()
    failures: list[nx.Graph] = []
    for raw in nx.graph_atlas_g():
        if raw.number_of_nodes() != 7:
            continue
        boundary = nx.convert_node_labels_to_integers(raw)
        missing = nx.complement(boundary)
        if is_split(missing):
            continue
        counts["nonsplit"] += 1
        if generic_minor_model(9, edges_with_helpers(boundary, False)) is not None:
            continue
        counts["ordinary_quotient_negative"] += 1
        model = generic_minor_model(10, edges_with_helpers(boundary, True))
        if model is None:
            failures.append(missing)
            counts["full_rows_negative"] += 1
        else:
            counts["full_rows_positive"] += 1

    print(dict(counts))
    print("negative signatures")
    for missing in failures:
        print(
            missing.number_of_edges(),
            tuple(sorted(dict(missing.degree()).values(), reverse=True)),
            tuple(sorted((len(c) for c in nx.connected_components(missing)), reverse=True)),
            sorted(tuple(sorted(e)) for e in missing.edges()),
        )


if __name__ == "__main__":
    main()
