#!/usr/bin/env python3
"""Falsify the connected-dominating remainder lemma on small/random graphs.

Graph vertices are 0..n-1 and adjacency is represented by Python integers.
No external dependencies are used.
"""

from __future__ import annotations

import argparse
import random


def chromatic_number(adj: list[int], vertices: int | None = None, cutoff: int | None = None) -> int:
    n = len(adj)
    if vertices is None:
        vertices = (1 << n) - 1
    if vertices == 0:
        return 0

    # Greedy DSATUR upper bound, followed by exact branch-and-bound.
    colors = [-1] * n
    sat = [0] * n
    deg = [(adj[v] & vertices).bit_count() for v in range(n)]
    best = vertices.bit_count()

    def greedy() -> int:
        cs = [-1] * n
        used = 0
        left = vertices
        while left:
            candidates = [v for v in range(n) if (left >> v) & 1]
            v = max(candidates, key=lambda x: (len({cs[u] for u in range(n) if cs[u] >= 0 and ((adj[x] >> u) & 1)}), deg[x]))
            forbidden = {cs[u] for u in range(n) if cs[u] >= 0 and ((adj[v] >> u) & 1)}
            c = 0
            while c in forbidden:
                c += 1
            cs[v] = c
            used = max(used, c + 1)
            left &= ~(1 << v)
        return used

    best = greedy()
    if cutoff is not None and best <= cutoff:
        # This is only an upper-bound shortcut; callers use cutoff solely to ask
        # whether a subgraph can still require at least a known value, so exactness
        # is retained below unless the upper bound already settles that question.
        pass

    def rec(left: int, used: int) -> None:
        nonlocal best
        if not left:
            best = min(best, used)
            return
        if used >= best:
            return
        candidates = [v for v in range(n) if (left >> v) & 1]
        v = max(candidates, key=lambda x: (sat[x].bit_count(), deg[x]))
        forbidden = sat[v]
        # Existing colors first.
        for c in range(min(used, best - 1)):
            if (forbidden >> c) & 1:
                continue
            colors[v] = c
            changed: list[tuple[int, int]] = []
            nbrs = adj[v] & left & ~(1 << v)
            while nbrs:
                b = nbrs & -nbrs
                u = b.bit_length() - 1
                old = sat[u]
                new = old | (1 << c)
                if new != old:
                    changed.append((u, old))
                    sat[u] = new
                nbrs ^= b
            rec(left & ~(1 << v), used)
            for u, old in changed:
                sat[u] = old
            colors[v] = -1
        if used + 1 < best:
            c = used
            colors[v] = c
            changed = []
            nbrs = adj[v] & left & ~(1 << v)
            while nbrs:
                b = nbrs & -nbrs
                u = b.bit_length() - 1
                old = sat[u]
                new = old | (1 << c)
                if new != old:
                    changed.append((u, old))
                    sat[u] = new
                nbrs ^= b
            rec(left & ~(1 << v), used + 1)
            for u, old in changed:
                sat[u] = old
            colors[v] = -1

    rec(vertices, 0)
    return best


def connected(adj: list[int], s: int) -> bool:
    if not s:
        return False
    seen = s & -s
    frontier = seen
    while frontier:
        x = frontier & -frontier
        frontier ^= x
        v = x.bit_length() - 1
        add = adj[v] & s & ~seen
        seen |= add
        frontier |= add
    return seen == s


def dominates(adj: list[int], d: int) -> bool:
    covered = d
    x = d
    while x:
        b = x & -x
        v = b.bit_length() - 1
        covered |= adj[v]
        x ^= b
    return covered == (1 << len(adj)) - 1


def is_vertex_critical(adj: list[int], k: int | None = None) -> bool:
    full = (1 << len(adj)) - 1
    if k is None:
        k = chromatic_number(adj)
    return k >= 2 and all(chromatic_number(adj, full & ~(1 << v)) == k - 1 for v in range(len(adj)))


def has_cd_remainder(adj: list[int], k: int) -> tuple[bool, int]:
    full = (1 << len(adj)) - 1
    # Enumerate H=G-D.  For a critical graph every proper H has chi <= k-1.
    for h in range(1, full):
        d = full ^ h
        if connected(adj, d) and dominates(adj, d) and chromatic_number(adj, h) >= k - 1:
            return True, d
    return False, 0


def critical_core(adj: list[int]) -> tuple[list[int], int]:
    k = chromatic_number(adj)
    verts = list(range(len(adj)))
    changed = True
    while changed:
        changed = False
        for old_v in verts.copy():
            trial = [v for v in verts if v != old_v]
            mask = sum(1 << v for v in trial)
            if chromatic_number(adj, mask) == k:
                verts = trial
                changed = True
                break
    remap = {v: i for i, v in enumerate(verts)}
    out = [0] * len(verts)
    for v in verts:
        for u in verts:
            if (adj[v] >> u) & 1:
                out[remap[v]] |= 1 << remap[u]
    return out, k


def random_graph(n: int, p: float, rng: random.Random) -> list[int]:
    adj = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < p:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    return adj


def graph6(adj: list[int]) -> str:
    n = len(adj)
    assert n <= 62
    bits = []
    # graph6 column-major upper triangle: (0,1),(0,2),(1,2),...
    for j in range(1, n):
        for i in range(j):
            bits.append((adj[i] >> j) & 1)
    while len(bits) % 6:
        bits.append(0)
    return chr(n + 63) + "".join(chr(63 + sum(bits[6*q+r] << (5-r) for r in range(6))) for q in range(len(bits)//6))


def contains_clique(adj: list[int], size: int) -> bool:
    """Small recursive clique decision routine."""
    def rec(candidates: int, need: int) -> bool:
        if need == 0:
            return True
        if candidates.bit_count() < need:
            return False
        while candidates.bit_count() >= need:
            b = candidates & -candidates
            v = b.bit_length() - 1
            candidates ^= b
            if rec(candidates & adj[v], need - 1):
                return True
        return False
    return rec((1 << len(adj)) - 1, size)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=14)
    ap.add_argument("--p", type=float, default=.45)
    ap.add_argument("--trials", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()
    rng = random.Random(args.seed)
    seen = set()
    for trial in range(args.trials):
        core, k = critical_core(random_graph(args.n, args.p, rng))
        key = graph6(core)
        if key in seen or k < 3 or len(core) == k:
            continue
        seen.add(key)
        ok, d = has_cd_remainder(core, k)
        print(trial, len(core), k, ok, key, hex(d), flush=True)
        if not ok:
            print("COUNTEREXAMPLE", len(core), k, key)
            for v, a in enumerate(core):
                print(v, [u for u in range(len(core)) if (a >> u) & 1])
            return
    print("tested distinct nonclique critical cores", len(seen))


if __name__ == "__main__":
    main()
