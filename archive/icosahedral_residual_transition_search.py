#!/usr/bin/env python3
"""Random/exhaustive falsification search on the deleted-icosahedron disk."""

from __future__ import annotations

import itertools
import random

import networkx as nx

from moser_safe_transition_state_probe import NONEDGES, classes, kind, matching
from wheel_safe_transition_search import (
    A, W, ABSTRACT_TO_PHYSICAL, PRESENT_PROFILES, TRIPLE_PROFILES,
    boundary_colours, circular_crossless, colourable,
)


def rim_order(graph: nx.Graph, deleted: int):
    rim = tuple(graph[deleted])
    rg = graph.subgraph(rim)
    out = [rim[0]]
    prev = None
    while len(out) < 5:
        nxt = next(x for x in rg[out[-1]] if x != prev and x not in out)
        prev = out[-1]
        out.append(nxt)
    assert out[0] in rg[out[-1]]
    return tuple(out)


def exact_word(word):
    if set().union(*word) != set(range(5)):
        return False
    for i, triple in enumerate(TRIPLE_PROFILES):
        if triple in word and sum((i + 3) % 5 in p for p in word) != 1:
            return False
    return circular_crossless(word)


def main() -> None:
    rng = random.Random(20260711)
    ico = nx.icosahedral_graph()
    rim = rim_order(ico, 0)
    d = ico.copy()
    d.remove_node(0)
    vertices = tuple(d)
    index = {x: i for i, x in enumerate(vertices)}
    full_mask = (1 << len(vertices)) - 1
    inner_boundary = [0] * (1 << len(vertices))
    for mask in range(1, full_mask):
        boundary = set()
        for x in vertices:
            if mask >> index[x] & 1:
                boundary.update(y for y in d[x] if not (mask >> index[y] & 1))
        inner_boundary[mask] = len(boundary)

    singles = tuple(frozenset({i}) for i in range(5))
    profiles = singles + PRESENT_PROFILES + TRIPLE_PROFILES
    words = [w for w in itertools.product(profiles, repeat=5) if exact_word(w)]
    print("profile words", len(words))
    residual = [
        es for q in (2, 3) for es in itertools.combinations(NONEDGES, q)
        if matching(es) and kind(es) != "decorated-T trace"
    ]
    palette = frozenset(range(6))

    def decorations(profile):
        if len(profile) == 1:
            return ({A, W},)
        if len(profile) == 2:
            return ({A}, {W}, {A, W})
        return (set(), {A}, {W}, {A, W})

    def relative(rows):
        unions = [0] * (1 << len(vertices))
        for mask in range(1, full_mask):
            bit = mask & -mask
            i = bit.bit_length() - 1
            unions[mask] = unions[mask ^ bit] | rows[vertices[i]]
            if inner_boundary[mask] + unions[mask].bit_count() < 7:
                return False
        return True

    trials = 0
    for _ in range(100000):
        word = rng.choice(words)
        contacts = {x: {A, W} for x in vertices}
        chosen_decorations = []
        for x, profile in zip(rim, word):
            deco = rng.choice(decorations(profile))
            chosen_decorations.append(deco)
            contacts[x] = set(deco) | {ABSTRACT_TO_PHYSICAL[i] for i in profile}
        rows = {x: sum(1 << z for z in contacts[x]) for x in vertices}
        if not relative(rows):
            continue
        trials += 1
        es = rng.choice(residual)
        wc = rng.randrange(6)
        bc = boundary_colours(es, wc)
        allowed = {x: palette - {bc[z] for z in contacts[x]} for x in vertices}
        if any(not ls for ls in allowed.values()) or colourable(d, allowed):
            continue
        for x, y in d.edges:
            q = nx.contracted_edge(d, (x, y), self_loops=False)
            q_allowed = {u: allowed[u] for u in q if u != x}
            q_allowed[x] = allowed[x] & allowed[y]
            if q_allowed[x] and colourable(q, q_allowed):
                print("FOUND", word, chosen_decorations, es, wc, (x, y))
                print("rim", rim, "contacts", contacts)
                return
    print("no transition in", trials, "relative systems sampled")


if __name__ == "__main__":
    main()
