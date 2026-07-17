#!/usr/bin/env python3
"""Classify four-colourable order-8/9 two-shore boundaries.

The probe records three structural predicates needed by the current
support-six composition argument:

* whether ``I_2 join J`` is K7-minor-free;
* whether every edge of ``J`` has boundary codegree at most three; and
* whether ``J`` has a four-colouring of type 2+2+2+2 (order 8) or
  3+2+2+2 (order 9).

Input is graph6, one graph per line.  This is a falsification/classification
probe, not by itself a promoted proof certificate.
"""

from __future__ import annotations

import sys

from hc7_boundary_join_probe import (
    colorable,
    decode_g6,
    has_k7_minor,
    join_i2,
)


def max_edge_codegree(adj: tuple[int, ...]) -> int:
    ans = 0
    for u in range(len(adj)):
        for v in range(u + 1, len(adj)):
            if (adj[u] >> v) & 1:
                ans = max(ans, (adj[u] & adj[v]).bit_count())
    return ans


def has_class_sizes(adj: tuple[int, ...], target: tuple[int, ...]) -> bool:
    """Return whether a proper colouring has the prescribed class sizes."""

    n = len(adj)
    target = tuple(sorted(target, reverse=True))
    if sum(target) != n:
        return False
    colors = [-1] * n
    used = [0] * len(target)

    def rec(done: int) -> bool:
        if done == n:
            return sorted(used, reverse=True) == list(target)

        uncolored = [v for v in range(n) if colors[v] < 0]
        v = max(uncolored, key=lambda x: adj[x].bit_count())
        forbidden = {
            colors[w]
            for w in range(n)
            if colors[w] >= 0 and ((adj[v] >> w) & 1)
        }

        # Equal target sizes are symmetric.  Trying only the first unused
        # colour of each current occupancy removes redundant branches.
        seen_occupancies = set()
        for c, cap in enumerate(target):
            if c in forbidden or used[c] >= cap or used[c] in seen_occupancies:
                continue
            seen_occupancies.add(used[c])
            colors[v] = c
            used[c] += 1
            if rec(done + 1):
                return True
            used[c] -= 1
            colors[v] = -1
        return False

    return rec(0)


def main() -> None:
    total = four = join_safe = low_codegree = balanced = residue = 0
    examples = []
    for line in sys.stdin:
        n, adj = decode_g6(line)
        if not n:
            continue
        if n not in (8, 9):
            raise ValueError("only orders 8 and 9 are supported")
        total += 1
        if not colorable(adj, 4):
            continue
        four += 1
        if has_k7_minor(join_i2(adj)):
            continue
        join_safe += 1
        if max_edge_codegree(adj) >= 4:
            continue
        low_codegree += 1
        target = (2, 2, 2, 2) if n == 8 else (3, 2, 2, 2)
        if has_class_sizes(adj, target):
            balanced += 1
            continue
        residue += 1
        if len(examples) < 100:
            examples.append(line.strip())

    for example in examples:
        print(example)
    print(
        f"# total={total} four={four} join_safe={join_safe} "
        f"low_codegree={low_codegree} balanced={balanced} residue={residue}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
