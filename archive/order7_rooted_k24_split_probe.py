#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["networkx"]
# ///
"""Probe a rooted-K_{2,4} replacement for the order-seven bad split.

For every unlabelled seven-vertex boundary J for which
J join \bar K_2 is K7-minor-free and \bar J is nonsplit, search for a
boundary K4 R with the following property.  Add a full helper h and two
adjacent split vertices x,y; require both x and y to see all of R, and
arbitrarily assign the other three boundary labels between them.  Every
one of the eight resulting ten-vertex quotients must contain K7.

This is a diagnostic for the structural route through a rooted K_{2,4}
minor with roots R.  It does not assert the rooted-minor theorem.
"""

from __future__ import annotations

import itertools
from collections import Counter

import networkx as nx

from contact_order7_all_unlabelled_atlas import is_split, quotient_edges
from contact_order7_five_edge_verify import as_sets, k_minor_model, verify_model
from contact_order7_sixedge_web_probe import generic_minor_model


S = tuple(range(7))


def edge_set(graph: nx.Graph) -> set[tuple[int, int]]:
    return {tuple(sorted(edge)) for edge in graph.edges()}


def split_edges(j_edges: set[tuple[int, int]], roots: tuple[int, ...], bits: int):
    h, x, y = 7, 8, 9
    roots = set(roots)
    free = tuple(v for v in S if v not in roots)
    x_contacts = set(roots)
    y_contacts = set(roots)
    for pos, v in enumerate(free):
        (x_contacts if (bits >> pos) & 1 else y_contacts).add(v)
    edges = set(j_edges)
    edges.add((x, y))
    edges.update((h, v) for v in S)
    edges.update((x, v) for v in x_contacts)
    edges.update((y, v) for v in y_contacts)
    return {tuple(sorted(edge)) for edge in edges}


def good_root_clique(boundary: nx.Graph, roots: tuple[int, ...]) -> bool:
    edges = edge_set(boundary)
    # Both centre pieces need a boundary anchor outside the four roots so
    # that the opposite full shore sees both resulting bags.  The all-left
    # and all-right assignments cannot possibly certify K7 and are not part
    # of the rooted-K2,4 splitting target.
    for bits in range(1, 7):
        if generic_minor_model(10, split_edges(edges, roots, bits)) is None:
            return False
    return True


def main() -> None:
    totals = Counter()
    good = Counter()
    residual = []
    for raw in nx.graph_atlas_g():
        if raw.number_of_nodes() != 7:
            continue
        boundary = nx.convert_node_labels_to_integers(raw)
        qmodel = k_minor_model(quotient_edges(boundary))
        if qmodel is not None:
            verify_model(quotient_edges(boundary), as_sets(qmodel))
            continue
        missing = nx.complement(boundary)
        if is_split(missing):
            continue
        m = missing.number_of_edges()
        totals[m] += 1
        roots = [R for R in itertools.combinations(S, 4)
                 if good_root_clique(boundary, R)]
        if roots:
            good[m] += 1
        else:
            residual.append((m,
                             nx.to_graph6_bytes(missing, header=False).decode().strip(),
                             tuple(sorted(dict(missing.degree()).values(), reverse=True)),
                             tuple(sorted(len(c) for c in nx.connected_components(missing)))))
        if sum(totals.values()) % 50 == 0:
            print("progress", sum(totals.values()), "good", sum(good.values()),
                  "residual", len(residual), flush=True)
    print("totals", sorted(totals.items()))
    print("good", sorted(good.items()))
    print("residual_counts", Counter(m for m, *_ in residual))
    for row in residual[:100]:
        print("RESIDUAL", row)


if __name__ == "__main__":
    main()
