#!/usr/bin/env python3
"""Exhaust small exact-block partition hypergraphs.

For a graph F on [n] and a palette cap r, vertices of the hypergraph are
partitions of V(F) into at most r independent blocks.  For each nonempty
independent P, the hyperedge Omega(P) consists of the partitions having P
as an exact block.  We test property B and distinguish singleton-edge
obstructions from genuine odd-cycle/higher obstructions.
"""

from __future__ import annotations

import argparse
from collections import Counter
import random


def partitions(items: tuple[int, ...]):
    if not items:
        yield ()
        return
    x, *rest = items
    for pi in partitions(tuple(rest)):
        yield ((x,),) + pi
        for i in range(len(pi)):
            yield pi[:i] + (tuple(sorted(pi[i] + (x,))),) + pi[i + 1 :]


def canonical(pi):
    return tuple(sorted((tuple(sorted(b)) for b in pi), key=lambda b: (b[0], len(b), b)))


def independent(mask: int, edge_mask: int, pairs: list[tuple[int, int]]) -> bool:
    for k, (u, v) in enumerate(pairs):
        if edge_mask >> k & 1 and mask >> u & 1 and mask >> v & 1:
            return False
    return True


def property_b(edges: list[tuple[int, ...]], nv: int):
    # Incremental DPLL on NAE constraints (every edge needs both colors).
    incident = [[] for _ in range(nv)]
    for j, e in enumerate(edges):
        for v in e:
            incident[v].append(j)
    colors = [-1] * nv

    def rec(done: int) -> bool:
        if done == nv:
            return True
        # Prefer a vertex in the shortest currently unresolved edge.
        best = None
        best_len = 10**9
        for e in edges:
            seen = {colors[v] for v in e if colors[v] >= 0}
            if len(seen) == 2:
                continue
            free = [v for v in e if colors[v] < 0]
            if not free:
                return False
            if len(free) < best_len:
                best, best_len = free[0], len(free)
        if best is None:
            return True
        for c in (0, 1):
            colors[best] = c
            bad = False
            for j in incident[best]:
                e = edges[j]
                vals = {colors[v] for v in e if colors[v] >= 0}
                if len(vals) < 2 and all(colors[v] >= 0 for v in e):
                    bad = True
                    break
            if not bad and rec(done + 1):
                return True
            colors[best] = -1
        return False

    return rec(0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=6)
    ap.add_argument("--samples", type=int, default=0,
                    help="sample this many labeled graphs (0 means exhaustive)")
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()
    n = args.n
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    raw_parts = sorted({canonical(pi) for pi in partitions(tuple(range(n)))})
    counts = Counter()
    witnesses = []
    universe = 1 << len(pairs)
    if args.samples:
        rng = random.Random(args.seed)
        graph_masks = [rng.randrange(universe) for _ in range(args.samples)]
    else:
        graph_masks = range(universe)
    for edge_mask in graph_masks:
        indep = {
            mask
            for mask in range(1, 1 << n)
            if independent(mask, edge_mask, pairs)
        }
        for r in range(1, n + 1):
            pis = [
                pi
                for pi in raw_parts
                if len(pi) <= r
                and all(sum(1 << x for x in block) in indep for block in pi)
            ]
            if not pis:
                continue
            idx = {pi: i for i, pi in enumerate(pis)}
            omega = {}
            for P in indep:
                e = tuple(
                    idx[pi]
                    for pi in pis
                    if any(sum(1 << x for x in block) == P for block in pi)
                )
                if e:
                    omega[P] = e
            edges = list(omega.values())
            singleton = any(len(e) == 1 for e in edges)
            pb = False if singleton else property_b(edges, len(pis))
            key = (r, singleton, pb)
            counts[key] += 1
            if not singleton and not pb and len(witnesses) < 20:
                witnesses.append((edge_mask, r, pis, omega))
    tested = args.samples or universe
    print(f"n={n}, graphs={tested}, Bell={len(raw_parts)}")
    for key, value in sorted(counts.items()):
        print(key, value)
    print("genuine_non_property_B", len(witnesses))
    for edge_mask, r, pis, omega in witnesses[:5]:
        es = [pairs[k] for k in range(len(pairs)) if edge_mask >> k & 1]
        print("witness", es, "r", r, "states", len(pis), "sizes", sorted(map(len, omega.values())))


if __name__ == "__main__":
    main()
