#!/usr/bin/env python3
"""Experimental search for highly connected rooted-clique obstructions.

This is a falsification aid, not proof infrastructure.
"""

from __future__ import annotations

import itertools
import random
from collections import deque


def connected(mask: int, adj: list[int]) -> bool:
    if not mask:
        return False
    bit = mask & -mask
    seen = bit
    todo = bit
    while todo:
        b = todo & -todo
        todo -= b
        v = b.bit_length() - 1
        new = adj[v] & mask & ~seen
        seen |= new
        todo |= new
    return seen == mask


def rooted_model(adj: list[int], roots: tuple[int, ...]) -> bool:
    """Whether there is a K_len(roots) model with roots in distinct bags."""
    n = len(adj)
    root_mask = sum(1 << u for u in roots)
    choices: list[list[tuple[int, int]]] = []
    for u in roots:
        others = root_mask ^ (1 << u)
        free = ((1 << n) - 1) ^ root_mask
        cs = []
        sub = free
        while True:
            m = sub | (1 << u)
            if connected(m, adj):
                nbr = 0
                z = m
                while z:
                    b = z & -z
                    z -= b
                    nbr |= adj[b.bit_length() - 1]
                cs.append((m, nbr & ~m))
            if sub == 0:
                break
            sub = (sub - 1) & free
        choices.append(cs)

    # Restrictive roots first, but retain labels only through their lists.
    order = sorted(range(len(roots)), key=lambda i: len(choices[i]))
    picked: list[tuple[int, int]] = []

    def rec(q: int, used: int) -> bool:
        if q == len(order):
            return True
        i = order[q]
        for m, nbr in choices[i]:
            if m & used:
                continue
            if any(not (nbr & pm) for pm, _ in picked):
                continue
            picked.append((m, nbr))
            if rec(q + 1, used | m):
                return True
            picked.pop()
        return False

    return rec(0, 0)


def vertex_connectivity_at_least(adj: list[int], k: int) -> bool:
    n = len(adj)
    if min(a.bit_count() for a in adj) < k:
        return False
    full = (1 << n) - 1
    for s in range(k):
        for X in itertools.combinations(range(n), s):
            rem = full
            for x in X:
                rem ^= 1 << x
            if rem and not connected(rem, adj):
                return False
    return True


def add_edge(adj: list[int], u: int, v: int) -> None:
    adj[u] |= 1 << v
    adj[v] |= 1 << u


def delete_edge(adj: list[int], u: int, v: int) -> None:
    adj[u] &= ~(1 << v)
    adj[v] &= ~(1 << u)


def end_locked(h: int) -> tuple[list[int], tuple[int, ...]]:
    # u=0..h-1, x=h..2h-1, b=2h..3h-2, z=3h-1
    n = 3 * h
    adj = [0] * n
    U = tuple(range(h))
    X = tuple(range(h, 2 * h))
    B = tuple(range(2 * h, 3 * h - 1))
    z = 3 * h - 1
    for i in range(h):
        add_edge(adj, U[i], X[i])
    for i in range(h - 1):
        add_edge(adj, X[i], X[i + 1])
        add_edge(adj, X[i], B[i])
    for i in range(h - 1):
        for j in range(i + 1, h - 1):
            add_edge(adj, B[i], B[j])
        add_edge(adj, z, B[i])
    add_edge(adj, z, X[0])
    return adj, U


def random_maximal(seed: int, h: int = 5) -> tuple[list[int], tuple[int, ...]]:
    rng = random.Random(seed)
    adj, roots = end_locked(h)
    n = len(adj)
    nonedges = [(i, j) for i in range(n) for j in range(i + 1, n)
                if not (adj[i] >> j) & 1]
    rng.shuffle(nonedges)
    changed = True
    while changed:
        changed = False
        rng.shuffle(nonedges)
        for u, v in nonedges:
            if (adj[u] >> v) & 1:
                continue
            add_edge(adj, u, v)
            if rooted_model(adj, roots):
                delete_edge(adj, u, v)
            else:
                changed = True
    return adj, roots


def main() -> None:
    for seed in range(100):
        adj, roots = random_maximal(seed)
        deg = min(a.bit_count() for a in adj)
        conn = 0
        for k in range(1, 6):
            if vertex_connectivity_at_least(adj, k):
                conn = k
            else:
                break
        print(seed, "edges", sum(a.bit_count() for a in adj) // 2,
              "mindeg", deg, "conn", conn)
        if conn >= 5:
            print("FOUND", seed)
            print([(u, v) for u in range(len(adj)) for v in range(u + 1, len(adj))
                   if (adj[u] >> v) & 1])
            return


if __name__ == "__main__":
    main()
