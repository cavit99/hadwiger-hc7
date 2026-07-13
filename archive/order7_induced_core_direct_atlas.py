#!/usr/bin/env python3
"""Test the direct induced-core/web closure on order-seven boundaries.

This is deliberately a diagnostic, not an atlas-as-proof.  For every
unlabelled quotient-negative nonsplit missing graph Q, it asks whether an
induced Földes--Hammer core R (2K2, C4, or C5) has

* a relaxed cyclic order in J=K7-Q;
* a bipartite omitted boundary J[S-R]; and
* a K7 certificate for every alternating crossing quotient.

The output isolates the first boundary geometries for which a theorem must
use simultaneous frames, portal placement, or minor transitions.
"""

from __future__ import annotations

import argparse
import itertools
from collections import Counter

import networkx as nx

import contact_order7_sixedge_web_probe as web
from contact_order7_all_unlabelled_atlas import is_split, quotient_edges
from contact_order7_five_edge_verify import as_sets, k_minor_model, verify_model


S = tuple(range(7))
PAIRS = set(itertools.combinations(S, 2))


def core_kind(graph: nx.Graph, vertices: tuple[int, ...]) -> str | None:
    sub = graph.subgraph(vertices)
    degrees = sorted(dict(sub.degree()).values())
    edges = sub.number_of_edges()
    if len(vertices) == 4 and edges == 2 and degrees == [1, 1, 1, 1]:
        return "2K2"
    if len(vertices) == 4 and edges == 4 and degrees == [2, 2, 2, 2]:
        return "C4"
    if len(vertices) == 5 and edges == 5 and degrees == [2, 2, 2, 2, 2]:
        return "C5"
    return None


def canonical_orders(vertices: tuple[int, ...], j_edges: set[tuple[int, int]]):
    root = min(vertices)
    rest = tuple(x for x in vertices if x != root)
    seen = set()
    for tail in itertools.permutations(rest):
        order = (root,) + tail
        reverse = (root,) + tuple(reversed(tail))
        key = min(order, reverse)
        if key in seen:
            continue
        seen.add(key)
        frame = {tuple(sorted((order[i], order[(i + 1) % len(order)])))
                 for i in range(len(order))}
        if all(edge in frame for edge in j_edges
               if edge[0] in vertices and edge[1] in vertices):
            yield order


def direct_witness(boundary: nx.Graph, missing: nx.Graph):
    j_edges = {tuple(sorted(edge)) for edge in boundary.edges()}
    for size in (4, 5):
        for vertices in itertools.combinations(S, size):
            kind = core_kind(missing, vertices)
            if kind is None:
                continue
            omitted = tuple(x for x in S if x not in vertices)
            if not nx.is_bipartite(boundary.subgraph(omitted)):
                continue
            for order in canonical_orders(vertices, j_edges):
                witnesses = web.crossing_forces(j_edges, order)
                if witnesses is not None:
                    return kind, order, omitted
    return None


def split_crossing_forces(j_edges: set[tuple[int, int]], order: tuple[int, ...]):
    """Test every minimal full-shore contact split for every crossing.

    A crossing can be extended to a connected bipartition X,Y of its
    entire shore.  Since the shore is full, N_S(X) union N_S(Y)=S.  By
    monotonicity it is enough to test disjoint assignments of the three
    nonterminal boundary vertices; there are at most 2^3 of these.
    """
    xpiece, ypiece, helper = 7, 8, 9
    certificates = []
    for i, r, j, s in itertools.combinations(range(len(order)), 4):
        first = {order[i], order[j]}
        second = {order[r], order[s]}
        free = tuple(z for z in S if z not in first | second)
        crossing_certificates = []
        for bits in range(1 << len(free)):
            x_contacts = set(first)
            y_contacts = set(second)
            for pos, z in enumerate(free):
                (x_contacts if bits >> pos & 1 else y_contacts).add(z)
            edges = set(j_edges)
            edges.add((xpiece, ypiece))
            edges.update((helper, z) for z in S)
            edges.update((xpiece, z) for z in x_contacts)
            edges.update((ypiece, z) for z in y_contacts)
            edges = {tuple(sorted(edge)) for edge in edges}
            model = web.generic_minor_model(10, edges)
            if model is None:
                return None
            crossing_certificates.append((tuple(sorted(x_contacts)), model))
        certificates.append((tuple(sorted(first)), tuple(sorted(second)),
                             crossing_certificates))
    return tuple(certificates)


def split_witness(boundary: nx.Graph, missing: nx.Graph):
    j_edges = {tuple(sorted(edge)) for edge in boundary.edges()}
    for size in (4, 5):
        for vertices in itertools.combinations(S, size):
            kind = core_kind(missing, vertices)
            if kind is None:
                continue
            omitted = tuple(x for x in S if x not in vertices)
            if not nx.is_bipartite(boundary.subgraph(omitted)):
                continue
            for order in canonical_orders(vertices, j_edges):
                witnesses = split_crossing_forces(j_edges, order)
                if witnesses is not None:
                    return kind, order, omitted
    return None


def relaxed_frame_witness(boundary: nx.Graph, *, full_split: bool):
    """Search a cyclic hull, without requiring the frame itself be a core."""
    j_edges = {tuple(sorted(edge)) for edge in boundary.edges()}
    for size in range(4, 8):
        for vertices in itertools.combinations(S, size):
            omitted = tuple(x for x in S if x not in vertices)
            if not nx.is_bipartite(boundary.subgraph(omitted)):
                continue
            for order in canonical_orders(vertices, j_edges):
                witnesses = (split_crossing_forces(j_edges, order) if full_split
                             else web.crossing_forces(j_edges, order))
                if witnesses is not None:
                    return order, omitted
    return None


def routing_frame(boundary: nx.Graph):
    """Return any relaxed frame whose omitted boundary is 2-colourable."""
    j_edges = {tuple(sorted(edge)) for edge in boundary.edges()}
    for size in range(4, 8):
        for vertices in itertools.combinations(S, size):
            omitted = tuple(x for x in S if x not in vertices)
            if not nx.is_bipartite(boundary.subgraph(omitted)):
                continue
            for order in canonical_orders(vertices, j_edges):
                return order, omitted
    return None


def induced_core_routing_frame(boundary: nx.Graph, missing: nx.Graph):
    j_edges = {tuple(sorted(edge)) for edge in boundary.edges()}
    for size in (4, 5):
        for vertices in itertools.combinations(S, size):
            if core_kind(missing, vertices) is None:
                continue
            omitted = tuple(x for x in S if x not in vertices)
            if not nx.is_bipartite(boundary.subgraph(omitted)):
                continue
            for order in canonical_orders(vertices, j_edges):
                return order, omitted
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-missing", type=int, default=21)
    parser.add_argument("--show", type=int, default=40)
    parser.add_argument("--routing-only", action="store_true")
    parser.add_argument("--all-boundaries", action="store_true")
    args = parser.parse_args()

    totals = Counter()
    direct = Counter()
    split = Counter()
    hull = Counter()
    hull_split = Counter()
    routing = Counter()
    core_routing = Counter()
    no_routing: list[tuple[int, str, str]] = []
    no_core_routing: list[tuple[int, str, str]] = []
    residuals: list[tuple[int, str, str]] = []
    for raw in nx.graph_atlas_g():
        if raw.number_of_nodes() != 7:
            continue
        boundary = nx.convert_node_labels_to_integers(raw)
        missing = nx.complement(boundary)
        m = missing.number_of_edges()
        if m > args.max_missing:
            continue
        if not args.all_boundaries:
            edges = quotient_edges(boundary)
            model = k_minor_model(edges)
            if model is not None:
                verify_model(edges, as_sets(model))
                continue
        if is_split(missing):
            continue
        totals[m] += 1
        if induced_core_routing_frame(boundary, missing) is not None:
            core_routing[m] += 1
        else:
            no_core_routing.append((m, nx.to_graph6_bytes(missing, header=False).decode().strip(),
                                    repr(sorted(tuple(sorted(e)) for e in missing.edges()))))
        if routing_frame(boundary) is not None:
            routing[m] += 1
        else:
            no_routing.append((m, nx.to_graph6_bytes(missing, header=False).decode().strip(),
                               repr(sorted(tuple(sorted(e)) for e in missing.edges()))))
        if args.routing_only:
            continue
        witness = direct_witness(boundary, missing)
        if witness is not None:
            direct[m] += 1
            split[m] += 1
            hull[m] += 1
            hull_split[m] += 1
        else:
            witness = split_witness(boundary, missing)
            if witness is not None:
                split[m] += 1
            if relaxed_frame_witness(boundary, full_split=False) is not None:
                hull[m] += 1
                hull_split[m] += 1
            elif relaxed_frame_witness(boundary, full_split=True) is not None:
                hull_split[m] += 1
            else:
                residuals.append((m, nx.to_graph6_bytes(missing, header=False).decode().strip(),
                                  repr(sorted(tuple(sorted(e)) for e in missing.edges()))))
        print(f"progress missing={m} totals={sum(totals.values())} "
              f"direct={sum(direct.values())} split={sum(split.values())} "
              f"hull={sum(hull.values())} hull_split={sum(hull_split.values())} "
              f"routing={sum(routing.values())} no_routing={len(no_routing)} "
              f"residual={len(residuals)}", flush=True)

    print("totals", sorted(totals.items()))
    if not args.routing_only:
        print("direct", sorted(direct.items()))
        print("split", sorted(split.items()))
        print("hull", sorted(hull.items()))
        print("hull_split", sorted(hull_split.items()))
    print("routing", sorted(routing.items()))
    print("core_routing", sorted(core_routing.items()))
    print("no_core_routing", Counter(m for m, _, _ in no_core_routing))
    print("no_routing", Counter(m for m, _, _ in no_routing))
    for item in no_routing[:args.show]:
        print("NO_ROUTING", item)
    print("residual", Counter(m for m, _, _ in residuals))
    for item in residuals[:args.show]:
        print("FAIL", item)


if __name__ == "__main__":
    main()
