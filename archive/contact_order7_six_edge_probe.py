#!/usr/bin/env python3
"""Probe the six-missing-edge layer of an order-seven two-shore quotient.

This is a discovery script.  It enumerates every six-edge complement F on
the seven boundary vertices, adds two nonadjacent full helpers, and records
the quotients with no K7 model.  It then groups failures by a canonical
label obtained from all 7! permutations and prints orbit representatives.
"""

from __future__ import annotations

import itertools
from collections import Counter, defaultdict

from contact_order7_five_edge_verify import (
    PAIRS,
    S,
    edge_mask,
    quotient_edges,
    relabel,
)


PERMS = tuple(itertools.permutations(S))


def candidate_partitions():
    """All possible seven-bag partitions on at most nine vertices.

    A K7 model on nine vertices has only two vertices beyond its seven
    mandatory bags.  Hence every branch set has size at most three and the
    only size patterns are 1^7, 2+1^6, 3+1^6, or 2+2+1^5.
    """
    V = tuple(range(9))
    out = []
    for used in itertools.combinations(V, 7):
        out.append(tuple(1 << x for x in used))
    for unused in V:
        rem = tuple(x for x in V if x != unused)
        for a, b in itertools.combinations(rem, 2):
            out.append((1 << a | 1 << b,) +
                       tuple(1 << x for x in rem if x not in (a, b)))
    for triple in itertools.combinations(V, 3):
        out.append((sum(1 << x for x in triple),) +
                   tuple(1 << x for x in V if x not in triple))
    pairs = tuple(itertools.combinations(V, 2))
    for p_index, p in enumerate(pairs):
        for q in pairs[p_index + 1:]:
            if set(p).isdisjoint(q):
                used = set(p) | set(q)
                out.append((sum(1 << x for x in p),
                            sum(1 << x for x in q)) +
                           tuple(1 << x for x in V if x not in used))
    return tuple(out)


PARTITIONS = candidate_partitions()


def fast_k7_model(edges):
    adj = [0] * 9
    for x, y in edges:
        adj[x] |= 1 << y
        adj[y] |= 1 << x

    def connected(mask):
        if mask & (mask - 1) == 0:
            return True
        low = mask & -mask
        reached = low
        while True:
            expanded = reached
            bits = reached
            while bits:
                bit = bits & -bits
                bits ^= bit
                expanded |= adj[bit.bit_length() - 1] & mask
            if expanded == reached:
                return reached == mask
            reached = expanded

    def adjacent(a, b):
        bits = a
        while bits:
            bit = bits & -bits
            bits ^= bit
            if adj[bit.bit_length() - 1] & b:
                return True
        return False

    for bags in PARTITIONS:
        if not all(connected(b) for b in bags):
            continue
        if all(adjacent(bags[i], bags[j])
               for i in range(7) for j in range(i)):
            return bags
    return None


def canonical(mask):
    return min(relabel(mask, p) for p in PERMS)


def degree_sequence(mask):
    deg = [0] * 7
    for i, (x, y) in enumerate(PAIRS):
        if mask >> i & 1:
            deg[x] += 1
            deg[y] += 1
    return tuple(sorted(deg, reverse=True))


def components(mask):
    adj = {v: set() for v in S}
    for i, (x, y) in enumerate(PAIRS):
        if mask >> i & 1:
            adj[x].add(y)
            adj[y].add(x)
    rem = set(S)
    sizes = []
    while rem:
        seed = next(iter(rem))
        seen = {seed}
        stack = [seed]
        while stack:
            x = stack.pop()
            for y in adj[x] - seen:
                seen.add(y)
                stack.append(y)
        sizes.append(len(seen))
        rem -= seen
    return tuple(sorted(sizes, reverse=True))


def edges_of(mask):
    return tuple(e for i, e in enumerate(PAIRS) if mask >> i & 1)


def main():
    failures = []
    for missing in itertools.combinations(PAIRS, 6):
        mask = edge_mask(missing)
        if fast_k7_model(quotient_edges(mask)) is None:
            failures.append(mask)

    # Canonicalizing one representative at a time avoids 5040 relabels for
    # every labelled failure: first bucket by cheap invariants, then consume
    # each full orbit from the failure set.
    remaining = set(failures)
    reps = []
    while remaining:
        seed = min(remaining)
        orb = {relabel(seed, p) for p in PERMS}
        class_members = remaining & orb
        rep = min(orb)
        reps.append((rep, len(class_members), degree_sequence(rep), components(rep)))
        remaining -= class_members

    print("labelled failures", len(failures))
    print("unlabelled failures", len(reps))
    print("degree sequences", Counter(degree_sequence(m) for m in failures))
    for index, (rep, orbit_size, degrees, comps) in enumerate(
        sorted(reps, key=lambda row: (row[2], row[3], row[0]))
    ):
        print(index, "orbit", orbit_size, "degrees", degrees,
              "components", comps, "edges", edges_of(rep))


if __name__ == "__main__":
    main()
