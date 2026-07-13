#!/usr/bin/env python3
"""Parity witnesses on the ordered P6 lobe boundary with one cone edge missing."""

from itertools import combinations

from degree9_lobe_equality_transition_search import partitions


S = tuple(range(7))
# The ordered lobe boundary: a path on 1,...,6 and a carrier owner 0
# adjacent to 2,...,6 but not 1.  The one missing owner--spine edge makes
# every boundary label genuinely visible to an exact-parity realizer.
BOUNDARY_EDGES = {
    frozenset((0, i)) for i in range(2, 7)
} | {
    frozenset((i, i + 1)) for i in range(1, 6)
}


def independent(vertices):
    return all(frozenset(pair) not in BOUNDARY_EDGES
               for pair in combinations(vertices, 2))


ALL_PARTITIONS = {
    tuple(sorted(tuple(sorted(block)) for block in partition))
    for partition in partitions(list(S))
}
STATES = tuple(
    (None, partition)
    for partition in ALL_PARTITIONS
    if len(partition) <= 6 and all(independent(block) for block in partition)
)


def main():
    independent_sets = [
        frozenset(vertices)
        for size in range(1, len(S) + 1)
        for vertices in combinations(S, size)
        if independent(vertices)
    ]
    for trace in independent_sets:
        parities = {
            len(partition) % 2
            for _, partition in STATES
            if tuple(sorted(trace)) in partition
        }
        assert parities == {0, 1}, (trace, parities)

    print("proper states", len(STATES))
    print("independent exact traces", len(independent_sets))
    print("PASS: even and odd state families are both trace-complete")

    # A portal-edge deletion ux with c(u)=c(x) forces x to be the unique
    # member of its boundary block among N_S(u).  Taking x singleton is
    # compatible with every possible portal neighborhood.  Check that both
    # a five-block (odd) and a six-block (even) state exist for every x.
    for x in S:
        witnesses = {}
        for _, partition in STATES:
            if (x,) not in partition or len(partition) not in (5, 6):
                continue
            witnesses.setdefault(len(partition), partition)
        assert set(witnesses) == {5, 6}, (x, witnesses)
        print("portal", x, "odd-5", witnesses[5], "even-6", witnesses[6])

        # Fullness check used in the realization note: find opposite-parity
        # states with exactly the same equality relation after x is omitted.
        by_restriction = {}
        other = set(S) - {x}
        for _, partition in STATES:
            restricted = tuple(sorted(
                tuple(sorted(set(block) & other))
                for block in partition if set(block) & other
            ))
            by_restriction.setdefault(restricted, {})[
                len(partition) % 2
            ] = partition
        flip = next((pair for pair in by_restriction.values()
                     if set(pair) == {0, 1}), None)
        assert flip is not None, x
        print("projection-flip", x, flip[0], flip[1])


if __name__ == "__main__":
    main()
