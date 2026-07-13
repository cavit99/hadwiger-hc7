#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["networkx>=3.4"]
# ///
"""Classify sharp order-seven boundaries with complement maximum degree two."""

from __future__ import annotations

import networkx as nx

import contact_order7_sixedge_web_probe as web
from contact_order7_all_unlabelled_atlas import is_split
from contact_order7_five_edge_verify import (
    as_sets,
    edge_mask,
    quotient_edges,
    verify_model,
)


def union(*graphs: nx.Graph) -> nx.Graph:
    return nx.disjoint_union_all(graphs)


EXPECTED_NEGATIVE = (
    nx.cycle_graph(7),
    union(nx.cycle_graph(3), nx.cycle_graph(4)),
    union(nx.cycle_graph(6), nx.empty_graph(1)),
    union(nx.cycle_graph(3), nx.cycle_graph(3), nx.empty_graph(1)),
    union(nx.cycle_graph(3), nx.path_graph(4)),
    union(nx.cycle_graph(5), nx.path_graph(2)),
    union(nx.cycle_graph(5), nx.empty_graph(1), nx.empty_graph(1)),
    union(nx.cycle_graph(3), nx.path_graph(2), nx.path_graph(2)),
)


def main() -> None:
    checked = positive = negative = 0
    seen_types: set[int] = set()
    for raw in nx.graph_atlas_g():
        if raw.number_of_nodes() != 7:
            continue
        missing = nx.convert_node_labels_to_integers(raw)
        if max(dict(missing.degree()).values(), default=0) > 2:
            continue
        if is_split(missing):
            continue
        checked += 1
        mask = edge_mask(tuple(sorted(edge)) for edge in missing.edges())
        model = web.quotient_model(mask)
        if model is not None:
            verify_model(quotient_edges(mask), as_sets(model))
            positive += 1
            continue
        matches = [
            index
            for index, expected in enumerate(EXPECTED_NEGATIVE)
            if nx.is_isomorphic(missing, expected)
        ]
        assert len(matches) == 1, sorted(missing.edges())
        seen_types.add(matches[0])
        negative += 1

    assert seen_types == set(range(len(EXPECTED_NEGATIVE)))
    assert (checked, positive, negative) == (24, 16, 8)
    print("nonsplit max-degree-two missing graphs", checked)
    print("K7-positive two-full-shore quotients", positive)
    print("K7-negative types", negative)
    print("negative list: C7, C3+C4, C6+K1, 2C3+K1, C3+P4, C5+K2, C5+2K1, C3+2K2")


if __name__ == "__main__":
    main()
