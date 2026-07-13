#!/usr/bin/env python3
"""Test the candidate lemma on Schrijver's vertex-critical Kneser graphs."""

from __future__ import annotations

import argparse
import itertools

from critical_dominating_search import chromatic_number, graph6, has_cd_remainder, is_vertex_critical


def schrijver(ground: int, rank: int) -> tuple[list[int], list[tuple[int, ...]]]:
    verts = []
    for s in itertools.combinations(range(ground), rank):
        ss = set(s)
        if all(((x + 1) % ground) not in ss for x in ss):
            verts.append(s)
    masks = [sum(1 << x for x in s) for s in verts]
    adj = [0] * len(verts)
    for i in range(len(verts)):
        for j in range(i + 1, len(verts)):
            if not (masks[i] & masks[j]):
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    return adj, verts


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("ground", type=int)
    ap.add_argument("rank", type=int)
    args = ap.parse_args()
    g, labels = schrijver(args.ground, args.rank)
    k = args.ground - 2 * args.rank + 2
    print("vertices", len(g), "expected chi", k, "exact chi", chromatic_number(g), "critical", is_vertex_critical(g, k))
    ok, d = has_cd_remainder(g, k)
    print("property", ok, "D", hex(d), "labels", [labels[v] for v in range(len(g)) if (d >> v) & 1], "g6", graph6(g))


if __name__ == "__main__":
    main()
