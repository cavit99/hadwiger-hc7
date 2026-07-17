#!/usr/bin/env python3
"""Classify small two-full-shore boundary graphs by coarse state invariants.

Input is graph6, one graph per line.  We retain graphs J such that J is
four-colourable and I_2 vee J has no K_7 minor, then report whether the
one-private-block gluing criterion is available.  This is a falsification
probe, not a promoted theorem certificate.
"""

from __future__ import annotations

import sys
from functools import lru_cache

from hc7_boundary_join_probe import (
    colorable,
    complete,
    contract_edge,
    decode_g6,
    delete_vertex,
)


def independent(adj: tuple[int, ...], mask: int) -> bool:
    while mask:
        bit = mask & -mask
        v = bit.bit_length() - 1
        mask ^= bit
        if adj[v] & mask:
            return False
    return True


def clique(adj: tuple[int, ...], mask: int) -> bool:
    vertices = [v for v in range(len(adj)) if (mask >> v) & 1]
    return all((adj[u] >> v) & 1 for i, u in enumerate(vertices)
               for v in vertices[i + 1:])


def alpha(adj: tuple[int, ...]) -> int:
    return max(mask.bit_count() for mask in range(1 << len(adj))
               if independent(adj, mask))


def private_block_glues(adj: tuple[int, ...]) -> bool:
    """Some independent P has |S-P|<=5 and S-P is a clique."""
    n = len(adj)
    full = (1 << n) - 1
    return any(
        mask.bit_count() >= n - 5
        and independent(adj, mask)
        and clique(adj, full ^ mask)
        for mask in range(1, 1 << n)
    )


def induced_mask(adj: tuple[int, ...], keep_mask: int) -> tuple[int, ...]:
    keep = tuple(v for v in range(len(adj)) if (keep_mask >> v) & 1)
    pos = {v: i for i, v in enumerate(keep)}
    return tuple(sum(1 << pos[w] for w in keep if (adj[v] >> w) & 1)
                 for v in keep)


def has_clique_oct(adj: tuple[int, ...]) -> bool:
    n = len(adj)
    full = (1 << n) - 1
    return any(clique(adj, mask) and colorable(induced_mask(adj, full ^ mask), 2)
               for mask in range(1 << n))


def connected_after_deleting(adj: tuple[int, ...], deleted: int) -> bool:
    remaining = ((1 << len(adj)) - 1) ^ deleted
    if remaining == 0:
        return True
    seen = 0
    stack = remaining & -remaining
    while stack:
        bit = stack & -stack
        stack ^= bit
        if seen & bit:
            continue
        seen |= bit
        v = bit.bit_length() - 1
        stack |= adj[v] & remaining & ~seen
    return seen == remaining


def connectivity_at_least(adj: tuple[int, ...], k: int) -> bool:
    n = len(adj)
    if n <= k:
        return False
    return all(connected_after_deleting(adj, mask)
               for mask in range(1 << n) if mask.bit_count() < k)


def degeneracy(adj: tuple[int, ...]) -> int:
    remaining = set(range(len(adj)))
    answer = 0
    while remaining:
        v = min(remaining, key=lambda x: sum((adj[x] >> w) & 1 for w in remaining))
        answer = max(answer, sum((adj[v] >> w) & 1 for w in remaining))
        remaining.remove(v)
    return answer


def has_clique_minor(adj: tuple[int, ...], k: int) -> bool:
    """Exact bounded-order deletion/contraction search."""
    @lru_cache(maxsize=None)
    def rec(g: tuple[int, ...]) -> bool:
        n = len(g)
        if n < k:
            return False
        if n == k:
            return complete(g)
        # A clique model either omits a vertex, or is spanning and therefore
        # has a nonsingleton branch set containing an edge to contract.
        if any(rec(delete_vertex(g, v)) for v in range(n)):
            return True
        return any(
            ((g[u] >> v) & 1) and rec(contract_edge(g, u, v))
            for u in range(n) for v in range(u + 1, n)
        )
    return rec(adj)


def join_i2_has_k7(adj: tuple[int, ...]) -> bool:
    """I_2 vee J has K7 iff J has K6 or J-v has K5 for some v."""
    if has_clique_minor(adj, 6):
        return True
    return any(has_clique_minor(delete_vertex(adj, v), 5)
               for v in range(len(adj)))


def main() -> None:
    total = four = join_free = gluable = 0
    by_alpha: dict[int, int] = {}
    examples: dict[tuple[int, bool, bool], str] = {}
    five_connected = five_connected_nongluable = clique_oct = 0
    by_degeneracy: dict[int, int] = {}
    for line in sys.stdin:
        n, adj = decode_g6(line)
        if not n:
            continue
        total += 1
        if not colorable(adj, 4):
            continue
        four += 1
        if join_i2_has_k7(adj):
            continue
        join_free += 1
        a = alpha(adj)
        g = private_block_glues(adj)
        c5 = connectivity_at_least(adj, 5)
        oct2 = has_clique_oct(adj)
        d = degeneracy(adj)
        gluable += int(g)
        clique_oct += int(oct2)
        five_connected += int(c5)
        five_connected_nongluable += int(c5 and not g)
        by_alpha[a] = by_alpha.get(a, 0) + 1
        by_degeneracy[d] = by_degeneracy.get(d, 0) + 1
        examples.setdefault((a, g, c5, oct2), line.strip())
    print(f"total={total} four={four} join_free={join_free} "
          f"private_block_gluable={gluable}")
    print(f"five_connected={five_connected} "
          f"five_connected_nongluable={five_connected_nongluable}")
    print(f"clique_oct={clique_oct} no_clique_oct={join_free-clique_oct}")
    print("by_alpha", sorted(by_alpha.items()))
    print("by_degeneracy", sorted(by_degeneracy.items()))
    print("examples", sorted(examples.items()))


if __name__ == "__main__":
    main()
