#!/usr/bin/env python3
"""Probe equitable four-colouring obstructions on 8/9 boundary vertices."""

from __future__ import annotations

import sys

from hc7_boundary_join_probe import colorable, decode_g6, has_k7_minor, join_i2


def has_independent_blocks(adj: tuple[int, ...], sizes: tuple[int, ...]) -> bool:
    n = len(adj)
    order = sorted(range(n), key=lambda v: adj[v].bit_count(), reverse=True)
    blocks: list[list[int]] = [[] for _ in sizes]

    def rec(i: int) -> bool:
        if i == n:
            return all(len(blocks[j]) == sizes[j] for j in range(len(sizes)))
        v = order[i]
        seen: set[tuple[int, tuple[int, ...]]] = set()
        for j, cap in enumerate(sizes):
            if len(blocks[j]) >= cap:
                continue
            signature = (cap, tuple(sorted(blocks[j])))
            if not blocks[j]:
                signature = (cap, ())
            if signature in seen:
                continue
            seen.add(signature)
            if all(not ((adj[v] >> u) & 1) for u in blocks[j]):
                blocks[j].append(v)
                if rec(i + 1):
                    return True
                blocks[j].pop()
        return False

    return rec(0)


def universal_clique(adj: tuple[int, ...]) -> int:
    n = len(adj)
    univ = [v for v in range(n) if adj[v].bit_count() == n - 1]
    return len(univ)


def main() -> None:
    total = four = bad = 0
    types: dict[tuple[int, int, int], tuple[int, str]] = {}
    for raw in sys.stdin:
        raw = raw.strip()
        if not raw or raw.startswith(">"):
            continue
        _, adj = decode_g6(raw)
        n = len(adj)
        sizes = (2, 2, 2, 2) if n == 8 else (3, 2, 2, 2)
        total += 1
        if not colorable(adj, 4) or colorable(adj, 3):
            continue
        four += 1
        if has_independent_blocks(adj, sizes):
            continue
        if has_k7_minor(join_i2(adj)):
            continue
        bad += 1
        key = (universal_clique(adj), max(a.bit_count() for a in adj), sum(a.bit_count() for a in adj) // 2)
        types.setdefault(key, (0, raw))
        types[key] = (types[key][0] + 1, types[key][1])
    print(f"# total={total} four={four} inequitable={bad} types={len(types)}")
    for key, (count, witness) in sorted(types.items()):
        print(key, count, witness)


if __name__ == "__main__":
    main()
