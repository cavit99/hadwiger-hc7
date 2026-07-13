#!/usr/bin/env python3
"""Dependency-free labelled verification of the seven-boundary classification.

All 2^21 labelled simple graphs are checked.  No graph atlas or graph
isomorphism library is used.
"""

import itertools


VERTICES = tuple(range(7))
PAIRS = tuple(itertools.combinations(VERTICES, 2))
INDEX = {edge: i for i, edge in enumerate(PAIRS)}


def edge_bit(a, b):
    if a > b:
        a, b = b, a
    return 1 << INDEX[(a, b)]


TRIPLES = tuple(
    sum(edge_bit(a, b) for a, b in itertools.combinations(triple, 2))
    for triple in itertools.combinations(VERTICES, 3)
)


def alpha_at_most_two(graph):
    return all(graph & triangle for triangle in TRIPLES)


def clique_mask(vertices):
    return sum(edge_bit(a, b) for a, b in itertools.combinations(vertices, 2))


def has_usable_model(graph):
    # Four singleton branch sets, leaving three possible anchors.
    for used in itertools.combinations(VERTICES, 4):
        if graph & clique_mask(used) != clique_mask(used):
            continue
        unused = set(VERTICES) - set(used)
        if any(graph & edge_bit(a, b) for a, b in itertools.combinations(unused, 2)):
            return True

    # On five used vertices, a four-bag model has one two-vertex bag and
    # three singleton bags.  The two unused anchors must be adjacent.
    for unused in itertools.combinations(VERTICES, 2):
        if not graph & edge_bit(*unused):
            continue
        used = set(VERTICES) - set(unused)
        for pair in itertools.combinations(used, 2):
            if not graph & edge_bit(*pair):
                continue
            singles = used - set(pair)
            triangle = clique_mask(singles)
            if graph & triangle != triangle:
                continue
            if all(any(graph & edge_bit(x, y) for x in pair) for y in singles):
                return True
    return False


def graph_mask(edges):
    return sum(edge_bit(a, b) for a, b in edges)


MOSER = graph_mask(
    ((0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
     (2, 6), (3, 4), (3, 5), (4, 5), (5, 6))
)
MOSER_PLUS = MOSER | edge_bit(1, 3)


def relabel(graph, permutation):
    answer = 0
    for index, (a, b) in enumerate(PAIRS):
        if graph >> index & 1:
            answer |= edge_bit(permutation[a], permutation[b])
    return answer


def orbit(graph):
    return {relabel(graph, permutation)
            for permutation in itertools.permutations(VERTICES)}


def main():
    expected = orbit(MOSER) | orbit(MOSER_PLUS)
    failures = set()
    alpha_count = 0
    for graph in range(1 << len(PAIRS)):
        if not alpha_at_most_two(graph):
            continue
        alpha_count += 1
        if not has_usable_model(graph):
            failures.add(graph)

    assert failures == expected, (len(failures), len(expected), failures ^ expected)
    by_edges = {}
    for graph in failures:
        by_edges[graph.bit_count()] = by_edges.get(graph.bit_count(), 0) + 1
    print("verified all", 1 << len(PAIRS), "labelled seven-vertex graphs")
    print("alpha<=2 labelled graphs", alpha_count)
    print("strong failures", len(failures), "by edge count", sorted(by_edges.items()))
    print("failure orbits: Moser and Moser+13 only")


if __name__ == "__main__":
    main()
