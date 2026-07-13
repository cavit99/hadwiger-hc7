#!/usr/bin/env python3
"""Enumerate proper equality partitions of the degree-nine exact cut.

The fixed boundary vertices are q,h,1,2,3,4,6.  The Moser edges not
involving q are fixed; q's six possible boundary adjacencies are varied.
For every graph, report whether parity of the number of blocks gives two
disjoint trace-complete boundary-state families.
"""

from itertools import combinations

V = ("q", "h", "1", "2", "3", "4", "6")
FIXED = {
    frozenset(e)
    for e in (
        ("h", "1"), ("h", "2"), ("h", "3"), ("h", "4"),
        ("1", "2"), ("1", "6"), ("2", "6"), ("3", "4"),
    )
}


def partitions(items):
    if not items:
        yield ()
        return
    x, *rest = items
    for p in partitions(rest):
        yield ((x,),) + p
        for i in range(len(p)):
            yield p[:i] + (tuple(sorted(p[i] + (x,))),) + p[i + 1 :]


ALL_PARTITIONS = {
    tuple(sorted(tuple(sorted(b)) for b in p)) for p in partitions(list(V))
}


def independent(block, edges):
    return all(frozenset(e) not in edges for e in combinations(block, 2))


def main():
    qothers = V[1:]
    parity_good = []
    state_counts = []
    projection_failures = []
    for mask in range(1 << len(qothers)):
        edges = set(FIXED)
        for i, x in enumerate(qothers):
            if mask & (1 << i):
                edges.add(frozenset(("q", x)))
        proper = [
            p for p in ALL_PARTITIONS
            if len(p) <= 6 and all(independent(b, edges) for b in p)
        ]
        state_counts.append((len(proper), sum(len(p) % 2 == 0 for p in proper),
                             sum(len(p) % 2 == 1 for p in proper)))
        inds = [
            frozenset(s)
            for r in range(1, len(V) + 1)
            for s in combinations(V, r)
            if independent(s, edges)
        ]
        ok = True
        witness = None
        for s in inds:
            parities = {
                len(p) % 2 for p in proper
                if tuple(sorted(s)) in p
            }
            if parities != {0, 1}:
                raise AssertionError((mask, tuple(sorted(s)), sorted(parities)))
        if ok:
            parity_good.append(mask)

        # Projection test: every proper partition on every proper subset of
        # the boundary extends to a proper full partition of each parity.
        for r in range(len(V)):
            for subset in combinations(V, r):
                subset = set(subset)
                restricted = {
                    tuple(sorted(tuple(sorted(set(b) & subset)) for b in p
                                 if set(b) & subset))
                    for p in proper
                }
                # Only retain restrictions that are themselves partitions of
                # the chosen subset (the construction above always is).
                for rp in restricted:
                    parities = {
                        len(p) % 2 for p in proper
                        if tuple(sorted(tuple(sorted(set(b) & subset)) for b in p
                                        if set(b) & subset)) == rp
                    }
                    if parities != {0, 1}:
                        projection_failures.append(
                            (mask, tuple(sorted(subset)), rp, tuple(sorted(parities)))
                        )
    print("q-adjacency masks checked", 1 << len(qothers))
    print("parity trace-complete masks", len(parity_good))
    print("Bell partitions checked per mask", len(ALL_PARTITIONS))
    print("proper-state count range", min(x[0] for x in state_counts),
          max(x[0] for x in state_counts))
    print("even-state count range", min(x[1] for x in state_counts),
          max(x[1] for x in state_counts))
    print("odd-state count range", min(x[2] for x in state_counts),
          max(x[2] for x in state_counts))
    assert len(parity_good) == 64
    print("PASS: both parity families contain an exact trace for every independent set")
    print("proper-subset projection failures", len(projection_failures))
    print("first projection failure", projection_failures[0])


if __name__ == "__main__":
    main()
