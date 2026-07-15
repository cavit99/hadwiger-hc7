#!/usr/bin/env python3
"""Probe small boundary graphs J for K7 in I_2 join J.

Input is graph6, one graph per line (for example from nauty `geng`).
The script first filters for 5-vertex-critical graphs, then tests whether
adding two nonadjacent vertices complete to J has a K7 minor.  This is a
research probe, not a promoted proof certificate.
"""

from __future__ import annotations

import sys
from functools import lru_cache


def decode_g6(line: str) -> tuple[int, tuple[int, ...]]:
    s = line.strip()
    if not s or s.startswith(">"):
        return 0, ()
    vals = [ord(c) - 63 for c in s]
    n = vals[0]
    bits = []
    for x in vals[1:]:
        bits.extend((x >> k) & 1 for k in range(5, -1, -1))
    adj = [0] * n
    p = 0
    for j in range(1, n):
        for i in range(j):
            if bits[p]:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
            p += 1
    return n, tuple(adj)


def induced(adj: tuple[int, ...], keep: tuple[int, ...]) -> tuple[int, ...]:
    pos = {v: i for i, v in enumerate(keep)}
    out = [0] * len(keep)
    for i, v in enumerate(keep):
        for w in keep:
            if (adj[v] >> w) & 1:
                out[i] |= 1 << pos[w]
    return tuple(out)


def colorable(adj: tuple[int, ...], k: int) -> bool:
    n = len(adj)
    colors = [-1] * n
    sat = [0] * n

    def rec(done: int) -> bool:
        if done == n:
            return True
        un = [v for v in range(n) if colors[v] < 0]
        v = max(un, key=lambda x: ((sat[x]).bit_count(), adj[x].bit_count()))
        forbidden = sat[v]
        for c in range(k):
            if (forbidden >> c) & 1:
                continue
            colors[v] = c
            changed = []
            for w in un:
                if w != v and ((adj[v] >> w) & 1) and not ((sat[w] >> c) & 1):
                    sat[w] |= 1 << c
                    changed.append(w)
            if rec(done + 1):
                return True
            colors[v] = -1
            for w in changed:
                # recompute: n is at most 11, so clarity beats bookkeeping
                mask = 0
                for u in range(n):
                    if colors[u] >= 0 and ((adj[w] >> u) & 1):
                        mask |= 1 << colors[u]
                sat[w] = mask
        return False

    return rec(0)


def is_5_vertex_critical(adj: tuple[int, ...]) -> bool:
    n = len(adj)
    if colorable(adj, 4):
        return False
    return all(colorable(induced(adj, tuple(w for w in range(n) if w != v)), 4)
               for v in range(n))


def join_i2(adj: tuple[int, ...]) -> tuple[int, ...]:
    n = len(adj)
    out = list(adj) + [0, 0]
    for v in range(n):
        out[v] |= (1 << n) | (1 << (n + 1))
        out[n] |= 1 << v
        out[n + 1] |= 1 << v
    return tuple(out)


def delete_vertex(adj: tuple[int, ...], v: int) -> tuple[int, ...]:
    return induced(adj, tuple(x for x in range(len(adj)) if x != v))


def contract_edge(adj: tuple[int, ...], u: int, v: int) -> tuple[int, ...]:
    if u > v:
        u, v = v, u
    keep = [x for x in range(len(adj)) if x != v]
    pos = {x: i for i, x in enumerate(keep)}
    out = [0] * len(keep)
    for a_i, a in enumerate(keep):
        for b_i in range(a_i + 1, len(keep)):
            b = keep[b_i]
            edge = ((adj[a] >> b) & 1) != 0
            if a == u:
                edge |= ((adj[v] >> b) & 1) != 0
            if b == u:
                edge |= ((adj[a] >> v) & 1) != 0
            if edge:
                out[a_i] |= 1 << b_i
                out[b_i] |= 1 << a_i
    return tuple(out)


def complete(adj: tuple[int, ...]) -> bool:
    n = len(adj)
    return all(adj[v].bit_count() == n - 1 for v in range(n))


def canonical_key(adj: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    # Isomorphism-free canonicalization is unnecessary at order <=11;
    # degree-sorted adjacency is only a cache accelerator, never a proof step.
    return len(adj), tuple(sorted(adj[v].bit_count() for v in range(len(adj)))) + adj


def has_k7_minor(adj: tuple[int, ...]) -> bool:
    seen = set()

    def rec(g: tuple[int, ...]) -> bool:
        n = len(g)
        if n < 7:
            return False
        if n == 7:
            return complete(g)
        key = canonical_key(g)
        if key in seen:
            return False
        seen.add(key)
        # A K7 model either omits a vertex or uses every vertex; branch on both
        # vertex deletion and one contraction edge.
        for v in range(n):
            if rec(delete_vertex(g, v)):
                return True
        for u in range(n):
            for v in range(u + 1, n):
                if (g[u] >> v) & 1 and rec(contract_edge(g, u, v)):
                    return True
        return False

    return rec(adj)


def main() -> None:
    total = critical = survivors = 0
    for line in sys.stdin:
        n, adj = decode_g6(line)
        if not n:
            continue
        total += 1
        if not is_5_vertex_critical(adj):
            continue
        critical += 1
        if not has_k7_minor(join_i2(adj)):
            survivors += 1
            print(line.strip())
    print(f"# total={total} critical5={critical} join_survivors={survivors}", file=sys.stderr)


if __name__ == "__main__":
    main()
