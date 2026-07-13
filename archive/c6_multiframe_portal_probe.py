#!/usr/bin/env python3
"""Adversarial probe for the C6 multi-frame portal-lock claim.

First model: the six boundary portal classes have distinct representatives
0,...,5 in a connected shore graph.  For each of the six frames, enumerate
all pairs of disjoint connected sets joining its two crossing missing edges.
Record whether the linkage is present and whether it can absorb either of
the two outward portal classes.  Search for one- and two-shore abstract
counterarchitectures.
"""

from __future__ import annotations

import itertools


N = 6
PAIRS = tuple(itertools.combinations(range(N), 2))

# Missing-cycle order; frame i omits c_i,c_{i+1}, crosses the two end edges
# of the complementary four-vertex path, and is repaired by absorbing the
# corresponding omitted endpoint into its adjacent crossing set.
C = (0, 4, 2, 3, 1, 5)
FRAMES = []
for i in range(6):
    xpair = (C[(i - 2) % 6], C[(i - 1) % 6])
    ypair = (C[(i + 2) % 6], C[(i + 3) % 6])
    FRAMES.append((xpair, ypair, C[i], C[(i + 1) % 6]))


def adjacency(edge_mask):
    out = [0] * N
    for i, (u, v) in enumerate(PAIRS):
        if edge_mask >> i & 1:
            out[u] |= 1 << v
            out[v] |= 1 << u
    return out


def connected(mask, adj):
    reached = mask & -mask
    while True:
        nxt = reached
        bits = reached
        while bits:
            bit = bits & -bits
            bits ^= bit
            nxt |= adj[bit.bit_length() - 1] & mask
        if nxt == reached:
            return reached == mask
        reached = nxt


def signatures(edge_mask):
    adj = adjacency(edge_mask)
    if not connected((1 << N) - 1, adj):
        return None
    conn = tuple(mask for mask in range(1, 1 << N) if connected(mask, adj))
    support = unlock = 0
    for i, (xp, yp, px, py) in enumerate(FRAMES):
        for x in conn:
            if not all(x >> q & 1 for q in xp):
                continue
            for y in conn:
                if x & y or not all(y >> q & 1 for q in yp):
                    continue
                support |= 1 << i
                if (x >> px & 1) or (y >> py & 1):
                    unlock |= 1 << i
        # Only whether some model exists matters.
    return support, unlock


def main():
    locked = []
    all_support = []
    for edge_mask in range(1 << len(PAIRS)):
        sig = signatures(edge_mask)
        if sig is None:
            continue
        support, unlock = sig
        if support:
            locked.append((edge_mask, support, unlock))
        if support == 0b111111 and not unlock:
            all_support.append(edge_mask)
    print("connected supporting graphs", len(locked))
    print("one-shore all-six locked", len(all_support))

    # A frame supported by either shore must be unlocked by neither shore.
    candidates = [(m, s) for m, s, u in locked if not u]
    pairs = []
    for i, (m1, s1) in enumerate(candidates):
        for m2, s2 in candidates[i:]:
            if s1 | s2 == 0b111111:
                pairs.append((m1, s1, m2, s2))
                if len(pairs) <= 20:
                    print("PAIR", bin(s1), bin(s2), hex(m1), hex(m2))
    print("two-shore locked covers", len(pairs))


if __name__ == "__main__":
    main()
