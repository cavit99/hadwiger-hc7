#!/usr/bin/env python3
"""Random Ore compositions stress-test the connected-dominating lemma."""

from __future__ import annotations

import argparse
import random

from critical_dominating_search import chromatic_number, graph6, has_cd_remainder, is_vertex_critical


def complete(k: int) -> list[int]:
    return [((1 << k) - 1) ^ (1 << v) for v in range(k)]


def edges(g: list[int]) -> list[tuple[int, int]]:
    return [(u, v) for u in range(len(g)) for v in range(u + 1, len(g)) if (g[u] >> v) & 1]


def ore(g1: list[int], g2: list[int], e: tuple[int, int], z: int,
        part: set[int]) -> list[int]:
    """Ore compose edge-side g1-e and split-side g2 at z.

    Split z into the endpoints x,y of e, assigning N(z) according to nonempty
    proper ``part``; all other vertices of g2 remain disjoint from g1.
    """
    x, y = e
    n1 = len(g1)
    others = [v for v in range(len(g2)) if v != z]
    pos = {v: n1 + i for i, v in enumerate(others)}
    out = [0] * (n1 + len(others))

    def add(a: int, b: int) -> None:
        out[a] |= 1 << b
        out[b] |= 1 << a

    for a, b in edges(g1):
        if {a, b} != {x, y}:
            add(a, b)
    for a, b in edges(g2):
        if a != z and b != z:
            add(pos[a], pos[b])
    for w in others:
        if (g2[z] >> w) & 1:
            add(x if w in part else y, pos[w])
    return out


def random_ore(k: int, copies: int, rng: random.Random) -> list[int]:
    g = complete(k)
    for _ in range(copies - 1):
        h = complete(k)
        e = rng.choice(edges(g))
        z = rng.randrange(k)
        nz = [w for w in range(k) if w != z]
        q = rng.randrange(1, len(nz))
        rng.shuffle(nz)
        g = ore(g, h, e, z, set(nz[:q]))
        # Randomly choose which existing factor is edge-side in later versions
        # by relabeling; this already samples many nonisomorphic k-Ore graphs.
        perm = list(range(len(g)))
        rng.shuffle(perm)
        inv = {v: i for i, v in enumerate(perm)}
        gg = [0] * len(g)
        for a, b in edges(g):
            aa, bb = inv[a], inv[b]
            gg[aa] |= 1 << bb
            gg[bb] |= 1 << aa
        g = gg
    return g


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=4)
    ap.add_argument("--copies", type=int, default=4)
    ap.add_argument("--trials", type=int, default=100)
    ap.add_argument("--seed", type=int, default=7)
    args = ap.parse_args()
    rng = random.Random(args.seed)
    seen = set()
    for i in range(args.trials):
        g = random_ore(args.k, args.copies, rng)
        code = graph6(g)
        if code in seen:
            continue
        seen.add(code)
        assert chromatic_number(g) == args.k
        assert is_vertex_critical(g, args.k)
        ok, d = has_cd_remainder(g, args.k)
        print(i, len(g), ok, code, hex(d), flush=True)
        if not ok:
            print("COUNTEREXAMPLE")
            for v, a in enumerate(g):
                print(v, [u for u in range(len(g)) if (a >> u) & 1])
            break


if __name__ == "__main__":
    main()
