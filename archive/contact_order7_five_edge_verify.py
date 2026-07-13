#!/usr/bin/env python3
"""Exact finite audit for five missing edges on an order-seven boundary.

For every labelled five-edge graph F on S, form Q=(K7-F) plus two
nonadjacent helpers complete to S.  An exact branch-set search proves
that Q has a K7 minor except when F is C5+2K1 or K3+2K2.
"""

import itertools


S = tuple(range(7))
H1, H2 = 7, 8
V = tuple(range(9))
PAIRS = tuple(itertools.combinations(S, 2))
PAIR_INDEX = {edge: i for i, edge in enumerate(PAIRS)}


def edge_mask(edges):
    answer = 0
    for a, b in edges:
        if a > b:
            a, b = b, a
        answer |= 1 << PAIR_INDEX[(a, b)]
    return answer


def relabel(mask, permutation):
    answer = 0
    for index, (a, b) in enumerate(PAIRS):
        if mask >> index & 1:
            x, y = sorted((permutation[a], permutation[b]))
            answer |= 1 << PAIR_INDEX[(x, y)]
    return answer


def orbit(mask):
    return {relabel(mask, permutation)
            for permutation in itertools.permutations(S)}


def quotient_edges(missing_mask):
    edges = {
        edge for index, edge in enumerate(PAIRS)
        if not (missing_mask >> index & 1)
    }
    edges.update((s, H1) for s in S)
    edges.update((s, H2) for s in S)
    return {tuple(sorted(edge)) for edge in edges}


def k_minor_model(edges, k=7):
    n = len(V)
    adjacency = [0] * n
    for i, j in edges:
        adjacency[i] |= 1 << j
        adjacency[j] |= 1 << i

    neighbour_union = [0] * (1 << n)
    connected = []
    for mask in range(1, 1 << n):
        low = mask & -mask
        i = low.bit_length() - 1
        neighbour_union[mask] = neighbour_union[mask ^ low] | adjacency[i]
        reached = low
        while True:
            expanded = reached | (neighbour_union[reached] & mask)
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            connected.append(mask)
    connected.sort(key=lambda mask: (mask.bit_count(), mask))

    def adjacent(a, b):
        return not (a & b) and bool(neighbour_union[a] & b)

    def rec(chosen, candidates, used):
        if len(chosen) == k:
            return chosen
        needed = k - len(chosen)
        if len(candidates) < needed:
            return None
        for pos, a in enumerate(candidates):
            if a & used:
                continue
            nxt = [
                b for b in candidates[pos + 1:]
                if not b & (used | a) and adjacent(a, b)
            ]
            if len(nxt) >= needed - 1:
                answer = rec(chosen + [a], nxt, used | a)
                if answer is not None:
                    return answer
        return None

    return rec([], connected, 0)


def as_sets(model):
    return tuple(tuple(v for v in V if mask >> v & 1) for mask in model)


def verify_model(edges, model):
    edges = set(edges)
    bags = [set(bag) for bag in model]
    assert len(bags) == 7
    assert all(bags)
    assert all(bags[i].isdisjoint(bags[j])
               for i in range(7) for j in range(i))
    for bag in bags:
        reached = {next(iter(bag))}
        while True:
            expanded = reached | {
                y for x in reached for y in bag
                if tuple(sorted((x, y))) in edges
            }
            if expanded == reached:
                break
            reached = expanded
        assert reached == bag
    for i in range(7):
        for j in range(i):
            assert any(tuple(sorted((x, y))) in edges
                       for x in bags[i] for y in bags[j])


C5 = edge_mask(((0, 1), (1, 2), (2, 3), (3, 4), (4, 0)))
K3_2K2 = edge_mask(((0, 1), (1, 2), (0, 2), (3, 4), (5, 6)))


def main():
    expected_failures = orbit(C5) | orbit(K3_2K2)
    failures = set()
    checked = 0
    for missing in itertools.combinations(PAIRS, 5):
        mask = edge_mask(missing)
        edges = quotient_edges(mask)
        model = k_minor_model(edges)
        if model is None:
            failures.add(mask)
        else:
            verify_model(edges, as_sets(model))
        checked += 1

    assert failures == expected_failures, (
        len(failures), len(expected_failures), failures ^ expected_failures
    )
    assert k_minor_model(quotient_edges(C5)) is None
    assert k_minor_model(quotient_edges(K3_2K2)) is None
    print("all labelled five-edge complements checked", checked)
    print("labelled exceptions", len(failures))
    print("C5+2K1 orbit", len(orbit(C5)))
    print("K3+2K2 orbit", len(orbit(K3_2K2)))
    print("exactly the two asserted isomorphism types fail")


if __name__ == "__main__":
    main()
