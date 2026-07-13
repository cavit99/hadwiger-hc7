#!/usr/bin/env python3
"""Exact K7 quotient probe for the pure-core gate adhesion.

Boundary: apex v, four roots X inducing 2K2, and two extra core vertices
p,q.  Two contracted full shores are nonadjacent helpers complete to the
boundary.  We enumerate every p/q boundary contact pattern consistent
with some four-colouring in which X has four distinct colours.
"""

from __future__ import annotations

import itertools


V, X, P, Q, HA, HB = 0, (1, 2, 3, 4), 5, 6, 7, 8
N = 9


def k_minor_model(edges: set[tuple[int, int]], k: int = 7):
    adjacency = [0] * N
    for i, j in edges:
        adjacency[i] |= 1 << j
        adjacency[j] |= 1 << i
    neighbour_union = [0] * (1 << N)
    connected = []
    for mask in range(1, 1 << N):
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

    def adjacent(a: int, b: int) -> bool:
        return not a & b and bool(neighbour_union[a] & b)

    def search(chosen, candidates, used):
        if len(chosen) == k:
            return chosen
        needed = k - len(chosen)
        if len(candidates) < needed:
            return None
        for pos, a in enumerate(candidates):
            if a & used:
                continue
            nxt = [
                b for b in candidates[pos + 1 :]
                if not b & (used | a) and adjacent(a, b)
            ]
            if len(nxt) >= needed - 1:
                answer = search(chosen + [a], nxt, used | a)
                if answer is not None:
                    return answer
        return None

    return search([], connected, 0)


def as_bags(model):
    return tuple(
        tuple(i for i in range(N) if mask >> i & 1) for mask in model
    )


def main() -> None:
    fixed = {(V, x) for x in X} | {(1, 2), (3, 4)}
    fixed |= {(h, s) for h in (HA, HB) for s in range(7)}
    optional = tuple((P, x) for x in X) + tuple((Q, x) for x in X) + ((P, Q),)

    seen = set()
    bad = []
    good_models = {}
    for cp, cq in itertools.product(X, repeat=2):
        for mask in range(1 << len(optional)):
            chosen = {optional[i] for i in range(len(optional)) if mask >> i & 1}
            if (P, cp) in chosen or (Q, cq) in chosen:
                continue
            if cp == cq and (P, Q) in chosen:
                continue
            boundary = frozenset(chosen)
            if boundary in seen:
                continue
            seen.add(boundary)
            edges = {tuple(sorted(edge)) for edge in fixed | chosen}
            model = k_minor_model(edges)
            if model is None:
                bad.append(boundary)
            else:
                good_models[boundary] = as_bags(model)

    maximal_bad = [
        state for state in bad
        if not any(state < other for other in bad)
    ]
    print("states", len(seen), "good", len(good_models), "bad", len(bad),
          "maximal_bad", len(maximal_bad))
    for state in sorted(maximal_bad, key=lambda s: (len(s), sorted(s))):
        print("bad", sorted(state))


if __name__ == "__main__":
    main()

