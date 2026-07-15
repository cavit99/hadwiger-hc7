#!/usr/bin/env python3
"""Falsify balanced four-colour states on small two-shore boundaries.

Input is graph6.  We retain four-colourable graphs J for which I_2 vee J
has no K_7 minor, and test whether J has a proper colouring with class
sizes (2,2,2,2) at order eight or (3,2,2,2) at order nine.
"""

from __future__ import annotations

import sys
from collections import Counter

from hc7_boundary_join_probe import colorable, decode_g6, has_k7_minor, join_i2


def independent(adj: tuple[int, ...], mask: int) -> bool:
    while mask:
        bit = mask & -mask
        mask ^= bit
        v = bit.bit_length() - 1
        if adj[v] & mask:
            return False
    return True


def balanced_four_partition(adj: tuple[int, ...]) -> bool:
    n = len(adj)
    if n not in (8, 9):
        raise ValueError("only orders eight and nine are supported")

    full = (1 << n) - 1

    def pairable(rest: int) -> bool:
        if rest == 0:
            return True
        if rest.bit_count() % 2:
            return False
        first = rest & -rest
        mates = rest ^ first
        while mates:
            mate = mates & -mates
            mates ^= mate
            pair = first | mate
            if independent(adj, pair) and pairable(rest ^ pair):
                return True
        return False

    if n == 8:
        return pairable(full)

    # The unique 3-class is distinguished from the three pair classes, so
    # it cannot be required to contain the first vertex.  Enumerate it
    # explicitly, then use the matching recursion on the remaining six.
    triple = full
    while triple:
        if triple.bit_count() == 3 and independent(adj, triple):
            if pairable(full ^ triple):
                return True
        triple = (triple - 1) & full
    return False


def universal_count(adj: tuple[int, ...]) -> int:
    return sum(a.bit_count() == len(adj) - 1 for a in adj)


def main() -> None:
    total = four = join_free = balanced = 0
    obstructions: Counter[tuple[int, int, int]] = Counter()
    examples: dict[tuple[int, int, int], str] = {}
    for line in sys.stdin:
        n, adj = decode_g6(line)
        if not n:
            continue
        total += 1
        if not colorable(adj, 4):
            continue
        four += 1
        is_balanced = balanced_four_partition(adj)
        # The expensive minor test matters only for an unbalanced graph.
        # Balanced graphs are counted separately but need not be classified
        # as join-free for this falsification probe.
        if is_balanced:
            balanced += 1
            continue
        if has_k7_minor(join_i2(adj)):
            continue
        join_free += 1
        key = (universal_count(adj), min(a.bit_count() for a in adj),
               max(a.bit_count() for a in adj))
        obstructions[key] += 1
        examples.setdefault(key, line.strip())
    print(f"total={total} four={four} balanced={balanced} "
          f"unbalanced_join_free={join_free}")
    print("obstruction signatures (universal,min_degree,max_degree):")
    for key, count in sorted(obstructions.items()):
        print(key, count, examples[key])


if __name__ == "__main__":
    main()
