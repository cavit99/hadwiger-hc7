#!/usr/bin/env python3
"""Exact order-eight test for the universal rooted-K4 cut lemma."""

from __future__ import annotations

import itertools


T = (0, 1, 2)
A = (3, 4)
B = (5, 6, 7)
VARIABLE = tuple(itertools.combinations(T, 2)) + tuple(itertools.combinations(B, 2)) + tuple((b, t) for b in B for t in T)
FIXED = {(3, 4)} | {(a, t) for a in A for t in T}
ALL = (1 << 8)-1


def connected(mask, adj):
    if not mask:
        return False
    reached = mask & -mask
    while True:
        expanded = reached
        todo = reached
        while todo:
            bit = todo & -todo; todo ^= bit
            expanded |= adj[bit.bit_length()-1] & mask
        if expanded == reached:
            return reached == mask
        reached = expanded


def three_connected(adj):
    for r in range(3):
        for deleted in itertools.combinations(range(8), r):
            mask = ALL
            for v in deleted:
                mask ^= 1 << v
            if not connected(mask, adj):
                return False
    return True


def rooted_k4(adj, roots):
    roots = tuple(roots)
    others = tuple(v for v in range(8) if v not in roots)
    for assignment in itertools.product(range(-1, 4), repeat=4):
        bags = [1 << roots[i] for i in range(4)]
        for v, target in zip(others, assignment):
            if target >= 0:
                bags[target] |= 1 << v
        if not all(connected(b, adj) for b in bags):
            continue
        okay = True
        for i in range(4):
            nbr = 0
            todo = bags[i]
            while todo:
                bit = todo & -todo; todo ^= bit
                nbr |= adj[bit.bit_length()-1]
            if any(not nbr & bags[j] for j in range(i)):
                okay = False; break
        if okay:
            return tuple(bags)
    return None


def main():
    hosts = 0
    for variable_mask in range(1 << len(VARIABLE)):
        adj = [0] * 8
        edges = set(FIXED)
        edges.update(VARIABLE[i] for i in range(len(VARIABLE)) if variable_mask >> i & 1)
        for u, v in edges:
            adj[u] |= 1 << v; adj[v] |= 1 << u
        if min(a.bit_count() for a in adj) < 4 or not three_connected(adj):
            continue
        hosts += 1
        for roots in itertools.combinations(range(8), 4):
            if rooted_k4(adj, roots) is None:
                print("counterexample edges", sorted(edges), "roots", roots)
                return
    print("hosts", hosts, "all four-root sets positive")


if __name__ == "__main__":
    main()
