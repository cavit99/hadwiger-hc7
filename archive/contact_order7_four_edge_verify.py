#!/usr/bin/env python3
"""Exact finite audit for four missing edges on an order-seven boundary.

For each of the C(21,4)=5985 labelled four-edge complements F on S,
form Q=(K7-F) plus two nonadjacent helpers, each complete to S.  An
exact connected-branch-set search verifies that Q has a K7 minor.

The script also prints witnesses for the only three isomorphism types
with vertex-cover number at least three.  All other types follow from
the two-shore vertex-cover lemma.
"""

import itertools


S = tuple(range(7))
H1, H2 = 7, 8
V = tuple(range(9))
PAIRS = tuple(itertools.combinations(S, 2))


def vertex_cover_number(edges):
    edges = set(edges)
    for size in range(8):
        for cover in itertools.combinations(S, size):
            cover = set(cover)
            if all(a in cover or b in cover for a, b in edges):
                return size
    raise AssertionError


def quotient_edges(missing):
    missing = set(missing)
    edges = {e for e in PAIRS if e not in missing}
    edges.update((s, H1) for s in S)
    edges.update((s, H2) for s in S)
    return {tuple(sorted(e)) for e in edges}


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


REPRESENTATIVES = {
    "K3+K2": ((0, 1), (1, 2), (0, 2), (3, 4)),
    "P4+K2": ((0, 1), (1, 2), (2, 3), (4, 5)),
    "P3+2K2": ((0, 1), (1, 2), (3, 4), (5, 6)),
}


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


def main():
    checked = 0
    high_cover = 0
    for missing in itertools.combinations(PAIRS, 4):
        edges = quotient_edges(missing)
        model = k_minor_model(edges)
        assert model is not None, missing
        verify_model(edges, as_sets(model))
        checked += 1
        high_cover += vertex_cover_number(missing) >= 3

    print("all labelled four-edge complements checked", checked)
    print("labelled complements with vertex-cover number >=3", high_cover)
    for name, missing in REPRESENTATIVES.items():
        assert vertex_cover_number(missing) == 3
        edges = quotient_edges(missing)
        model = as_sets(k_minor_model(edges))
        verify_model(edges, model)
        print(name, "missing", missing, "model", model)


if __name__ == "__main__":
    main()
