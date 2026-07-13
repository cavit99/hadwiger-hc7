#!/usr/bin/env python3
"""Replay the six rotated opposite-crossing K7 certificates."""

from __future__ import annotations

import itertools


C = (0, 4, 2, 3, 1, 5)
Z = 6
X0, Y0, X3, Y3 = 7, 8, 9, 10
V = tuple(range(11))
MISSING = {tuple(sorted((C[i], C[(i + 1) % 6]))) for i in range(6)}


def valid(edges, bags):
    adj = {v: set() for v in V}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    assert len(bags) == 7
    assert all(bags[i].isdisjoint(bags[j])
               for i, j in itertools.combinations(range(7), 2))
    for bag in bags:
        reached = {next(iter(bag))}
        while True:
            expanded = reached | {v for u in reached for v in adj[u]
                                  if v in bag}
            if expanded == reached:
                break
            reached = expanded
        assert reached == bag
    assert all(any(v in adj[u] for u in bags[i] for v in bags[j])
               for i, j in itertools.combinations(range(7), 2))


def main():
    boundary = set(itertools.combinations(range(7), 2)) - MISSING
    for i in range(6):
        ci = tuple(C[(i + j) % 6] for j in range(6))
        edges = set(boundary)
        edges.update(((X0, Y0), (X3, Y3)))
        edges.update((min(X0, s), max(X0, s)) for s in (ci[4], ci[5]))
        edges.update((min(Y0, s), max(Y0, s)) for s in (ci[2], ci[3]))
        edges.update((min(X3, s), max(X3, s)) for s in (ci[1], ci[2]))
        edges.update((min(Y3, s), max(Y3, s)) for s in (ci[5], ci[0]))
        bags = (
            {ci[2]}, {ci[5]}, {Z},
            {X0, ci[4]}, {Y0, ci[3]},
            {X3, ci[1]}, {Y3, ci[0]},
        )
        valid(edges, bags)
    print("opposite crossing certificates verified", 6)


if __name__ == "__main__":
    main()
