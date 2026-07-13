#!/usr/bin/env python3
"""Monotone contact atlas for a split shore at the C6+K1 boundary.

The active shore is contracted to adjacent connected pieces X,Y, the
opposite full shore to H.  Each boundary vertex contacts X, Y, or both.
The script classifies all 3^7 full-contact assignments and extracts small
positive supports for the K7 models it finds.
"""

from __future__ import annotations

import itertools

import c5_core_k2_shore_verify as exact
import six_edge_web_template_search as web


S = tuple(range(7))
X, Y, H = 7, 8, 9
MISSING = {tuple(sorted(edge)) for edge in web.EXCEPTIONS[3]}
BOUNDARY = web.PAIRS - MISSING
FIXED = ({tuple(sorted(edge)) for edge in BOUNDARY}
         | {(X, Y)} | {(s, H) for s in S})


def valid_model(edges, bags):
    adjacency = [set() for _ in range(10)]
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)

    decoded = [{i for i in range(10) if mask >> i & 1} for mask in bags]
    if any(not bag for bag in decoded):
        return False
    if any(decoded[i] & decoded[j]
           for i, j in itertools.combinations(range(7), 2)):
        return False

    for bag in decoded:
        reached = {next(iter(bag))}
        while True:
            expanded = reached | {v for u in reached for v in adjacency[u]
                                  if v in bag}
            if expanded == reached:
                break
            reached = expanded
        if reached != bag:
            return False

    return all(any(v in adjacency[u] for u in decoded[i]
                   for v in decoded[j])
               for i, j in itertools.combinations(range(7), 2))


def assignment_edges(state):
    edges = set(FIXED)
    for s, value in enumerate(state):
        if value & 1:
            edges.add(tuple(sorted((X, s))))
        if value & 2:
            edges.add(tuple(sorted((Y, s))))
    return edges


def contact_support(edges, model):
    optional = sorted(edges - FIXED)
    kept = set(edges)
    for edge in optional:
        trial = kept - {edge}
        if valid_model(trial, model):
            kept = trial
    return frozenset(kept - FIXED)


def contains_support(edges, supports):
    optional = edges - FIXED
    return any(support <= optional for support in supports)


def fmt_state(state):
    return "".join("X" if x == 1 else "Y" if x == 2 else "B"
                   for x in state)


def main():
    supports = []
    failures = []
    exact_calls = 0
    for state in itertools.product((1, 2, 3), repeat=7):
        edges = assignment_edges(state)
        if contains_support(edges, supports):
            continue
        exact_calls += 1
        model = exact.k_minor_model(edges)
        if model is None:
            failures.append(state)
        else:
            support = contact_support(edges, model)
            if support not in supports:
                supports.append(support)

    # A failure may have been visited before a subsequently discovered
    # support.  Replay the final monotone cover before reporting it.
    failures = [state for state in itertools.product((1, 2, 3), repeat=7)
                if not contains_support(assignment_edges(state), supports)
                and exact.k_minor_model(assignment_edges(state)) is None]

    print("exact discovery calls", exact_calls)
    print("positive supports", len(supports))
    print("failures", len(failures), "of", 3 ** 7)
    for state in failures[:200]:
        print(fmt_state(state), state)


if __name__ == "__main__":
    main()
