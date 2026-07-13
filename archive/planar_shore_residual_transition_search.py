#!/usr/bin/env python3
"""Search all small 3-connected planar portal-face shores for residual transitions."""

from __future__ import annotations

import itertools

import networkx as nx

from moser_safe_transition_state_probe import NONEDGES, N, classes, kind, matching
from wheel_safe_transition_search import (
    A,
    W,
    ABSTRACT_TO_PHYSICAL,
    PRESENT_PROFILES,
    boundary_colours,
    circular_crossless,
    colourable,
    relative7,
)


def faces(embedding: nx.PlanarEmbedding):
    seen: set[tuple[int, int]] = set()
    for x, y in embedding.edges():
        if (x, y) in seen:
            continue
        face = embedding.traverse_face(x, y, seen)
        yield tuple(face)


def transition(graph, contacts, residual):
    palette = frozenset(range(6))
    for es in residual:
        for wc in range(6):
            bc = boundary_colours(es, wc)
            allowed = {x: palette - {bc[z] for z in contacts[x]} for x in graph}
            if any(not ls for ls in allowed.values()) or colourable(graph, allowed):
                continue
            for x, y in graph.edges:
                q = nx.contracted_edge(graph, (x, y), self_loops=False)
                q_allowed = {u: allowed[u] for u in q if u != x}
                q_allowed[x] = allowed[x] & allowed[y]
                if q_allowed[x] and colourable(q, q_allowed):
                    return es, wc, (x, y)
    return None


def main() -> None:
    residual = [
        es for q in (2, 3) for es in itertools.combinations(NONEDGES, q)
        if matching(es) and kind(es) != "decorated-T trace"
    ]
    words_by_length = {
        m: [w for w in itertools.product(PRESENT_PROFILES, repeat=m)
            if circular_crossless(w)]
        for m in range(5, 8)
    }
    examined = 0
    for graph in nx.graph_atlas_g():
        if len(graph) < 6 or len(graph) > 7 or not nx.is_connected(graph):
            continue
        if nx.node_connectivity(graph) < 3:
            continue
        planar, embedding = nx.check_planarity(graph)
        if not planar:
            continue
        for face in faces(embedding):
            m = len(face)
            if m not in words_by_length:
                continue
            if any(graph.degree[x] < 5 for x in set(graph) - set(face)):
                continue
            for word in words_by_length[m]:
                contacts = {x: {A, W} for x in graph}
                for x, profile in zip(face, word):
                    contacts[x].update(ABSTRACT_TO_PHYSICAL[i] for i in profile)
                if not relative7(graph, contacts):
                    continue
                examined += 1
                found = transition(graph, contacts, residual)
                if found:
                    print("FOUND", len(graph), nx.to_graph6_bytes(graph).strip(), face, word, found)
                    print("contacts", contacts)
                    return
    print("no transition; systems", examined)


if __name__ == "__main__":
    main()
