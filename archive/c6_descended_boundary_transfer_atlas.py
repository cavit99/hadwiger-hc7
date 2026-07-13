"""Classify exact-seven boundaries obtained from every negative C6 two-cut.

This is an invariant finder, not a proof by itself.  It reuses the exact
two-piece negative atlas, retains all six connected allocations of the two
poles, descends through every defect-two component, and records the missing
graph on the five old boundary vertices plus the two literal poles.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations

import networkx as nx

from c6_two_piece_contact_atlas_fast import quotient_edges, S
from contact_order7_all_unlabelled_atlas import quotient_edges as full_shore_edges
from contact_order7_five_edge_verify import k_minor_model
from k331_two_piece_contact_atlas import fast_k7_model


FULL = (1 << 7) - 1
RIM = set(range(6))
Z = 6


def bits(mask):
    return frozenset(i for i in S if mask >> i & 1)


def negative_pairs():
    return {
        (x, y)
        for x in range(128)
        for y in range(128)
        if x | y == FULL
        and fast_k7_model(quotient_edges(bits(x), bits(y))) is None
    }


def old_edge(u, v):
    if Z in (u, v):
        return True
    return (u - v) % 6 not in (1, 5)


def descended_boundary(component, pole_p, pole_q, pq_edge):
    retained = sorted(bits(component))
    assert len(retained) == 5
    names = retained + ["p", "q"]
    boundary = nx.Graph()
    boundary.add_nodes_from(range(7))
    for i, j in combinations(range(5), 2):
        if old_edge(retained[i], retained[j]):
            boundary.add_edge(i, j)
    for i, label in enumerate(retained):
        if pole_p >> label & 1:
            boundary.add_edge(i, 5)
        if pole_q >> label & 1:
            boundary.add_edge(i, 6)
    if pq_edge:
        boundary.add_edge(5, 6)
    return names, boundary


def graph6(g):
    # Seven vertices are small enough to canonicalize by all permutations.
    best = None
    for perm in __import__("itertools").permutations(range(7)):
        word = 0
        for i, j in combinations(range(7), 2):
            word = (word << 1) | int(g.has_edge(perm[i], perm[j]))
        if best is None or word < best:
            best = word
    return best


def main():
    neg = negative_pairs()
    large = [m for m in range(128) if m.bit_count() >= 5]
    orbit_counts = Counter()
    edge_counts = Counter()
    core_counts = Counter()
    samples = {}
    static_positive = 0
    states = 0

    for a in large:
        for b in large:
            for p in range(128):
                for q in range(128):
                    if (a, b | p | q) not in neg:
                        continue
                    if (a | p, b | q) not in neg:
                        continue
                    if (a | q, b | p) not in neg:
                        continue
                    if (a | p | q, b) not in neg:
                        continue
                    if (p, a | b | q) not in neg:
                        continue
                    if (q, a | b | p) not in neg:
                        continue
                    states += 1
                    for component in (a, b):
                        if (FULL ^ component).bit_count() != 2:
                            continue
                        for pq_edge in (False, True):
                            names, boundary = descended_boundary(
                                component, p, q, pq_edge
                            )
                            missing = nx.complement(boundary)
                            key = graph6(missing)
                            orbit_counts[key] += 1
                            edge_counts[missing.number_of_edges()] += 1
                            defect = set(bits(FULL ^ component))
                            if Z in defect:
                                core = "P5"
                            else:
                                u, v = sorted(defect)
                                dist = min((u - v) % 6, (v - u) % 6)
                                core = {1: "adjacent", 2: "P3+2K1", 3: "2K2+K1"}[dist]
                            core_counts[core] += 1
                            samples.setdefault(key, (names, tuple(sorted(missing.edges()))))
                            model = k_minor_model(full_shore_edges(boundary))
                            if model is not None:
                                static_positive += 1

    print("valid two-cut contact states", states)
    print("descended labelled states", sum(orbit_counts.values()))
    print("missing-edge counts", dict(sorted(edge_counts.items())))
    print("old-core counts", dict(core_counts))
    print("unlabelled missing-graph orbits", len(orbit_counts))
    print("statically K7-positive descended states", static_positive)
    by_edges = defaultdict(int)
    for key in orbit_counts:
        # recover edge count from the saved sample
        by_edges[len(samples[key][1])] += 1
    print("orbits by missing-edge count", dict(sorted(by_edges.items())))
    for key in sorted(orbit_counts, key=lambda k: (len(samples[k][1]), k))[:30]:
        print(orbit_counts[key], samples[key])


if __name__ == "__main__":
    main()
