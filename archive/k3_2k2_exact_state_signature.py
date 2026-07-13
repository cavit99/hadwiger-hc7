#!/usr/bin/env python3
"""Exact side-signature classifier for Q=K3 disjoint union 2K2.

A state is (triangle_partition, e, f), where triangle_partition is one
of: all singletons, one of three pair+singleton partitions, or the full
triple; e,f record whether either K2 is used as one block.  The unique
seven-block state is excluded by the six-color cap.
"""

from __future__ import annotations

import itertools


STATES = tuple(
    (p, e, f)
    for p in range(5)
    for e in range(2)
    for f in range(2)
    if (p, e, f) != (0, 0, 0)
)
INDEX = {s: i for i, s in enumerate(STATES)}


def state_mask(predicate):
    return sum(1 << i for i, s in enumerate(STATES) if predicate(s))


# Triangle pair types: 1=ab, 2=ac, 3=bc; 4=abc.
HYPEREDGES = (
    state_mask(lambda s: s[0] == 4),
    *(state_mask(lambda s, p=p: s[0] == p) for p in (1, 2, 3)),
    # Exact singleton a,b,c: all-single triangle or the opposite pair.
    state_mask(lambda s: s[0] in (0, 3)),
    state_mask(lambda s: s[0] in (0, 2)),
    state_mask(lambda s: s[0] in (0, 1)),
    state_mask(lambda s: s[1] == 1),
    state_mask(lambda s: s[1] == 0),
    state_mask(lambda s: s[2] == 1),
    state_mask(lambda s: s[2] == 0),
)


def hits_all(mask):
    return all(mask & edge for edge in HYPEREDGES)


def minimal(mask):
    if not hits_all(mask):
        return False
    x = mask
    while x:
        bit = x & -x
        if hits_all(mask ^ bit):
            return False
        x ^= bit
    return True


def permute_state(s, perm, swap_ef):
    p, e, f = s
    if p in (1, 2, 3):
        pairs = ((0, 1), (0, 2), (1, 2))
        pair = tuple(sorted((perm[pairs[p - 1][0]], perm[pairs[p - 1][1]])))
        p = pairs.index(pair) + 1
    if swap_ef:
        e, f = f, e
    return p, e, f


AUTOS = tuple(
    (perm, swap)
    for perm in itertools.permutations(range(3))
    for swap in (False, True)
)


def permute_mask(mask, auto):
    ans = 0
    for i, s in enumerate(STATES):
        if mask >> i & 1:
            ans |= 1 << INDEX[permute_state(s, *auto)]
    return ans


def orbit_pair(a, b):
    out = set()
    for auto in AUTOS:
        x, y = permute_mask(a, auto), permute_mask(b, auto)
        out.add((x, y))
        out.add((y, x))
    return out


def show(mask):
    return tuple(STATES[i] for i in range(len(STATES)) if mask >> i & 1)


def main():
    transversals = [m for m in range(1 << len(STATES)) if minimal(m)]
    pairs = [(a, b) for a in transversals for b in transversals if not a & b]
    seen = set()
    reps = []
    for pair in pairs:
        if pair in seen:
            continue
        orb = orbit_pair(*pair)
        seen.update(orb)
        reps.append(min(orb))
    print("states", len(STATES))
    print("hyperedge sizes", sorted(edge.bit_count() for edge in HYPEREDGES))
    print("minimal one-side covers", len(transversals))
    print("labeled disjoint minimal pairs", len(pairs))
    print("orbits under S3 x S2 x shore-swap", len(reps))
    sizes = {}
    for a, b in reps:
        sizes[(a.bit_count(), b.bit_count())] = sizes.get((a.bit_count(), b.bit_count()), 0) + 1
    print("orbit size-pair histogram", sorted(sizes.items()))
    for j, (a, b) in enumerate(sorted(reps)[:40], 1):
        print(j, "A", show(a), "B", show(b))


if __name__ == "__main__":
    main()
