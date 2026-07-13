#!/usr/bin/env python3
"""Check whether one facial order can cover every Moser nonedge.

For a fixed cyclic order, a packet-deficient perfect matching must be
pairwise alternating.  This script records all valid Moser matchings for
the order and the union of their three edges.
"""

from itertools import combinations, permutations


V = tuple(range(7))
MOSER = {
    tuple(sorted(map(int, edge)))
    for edge in "01 02 03 04 12 16 26 34 35 45 56".split()
}
NONEDGES = set(combinations(V, 2)) - MOSER


def matchings():
    out = []
    for singleton in V:
        for chosen in combinations(NONEDGES, 3):
            ends = [vertex for edge in chosen for vertex in edge]
            if len(set(ends)) == 6 and set(ends) == set(V) - {singleton}:
                out.append((singleton, tuple(sorted(chosen))))
    return tuple(sorted(set(out)))


def alternate(order, first, second):
    position = {vertex: index for index, vertex in enumerate(order)}
    a, b = sorted((position[first[0]], position[first[1]]))
    c, d = sorted((position[second[0]], position[second[1]]))
    return a < c < b < d or c < a < d < b


def main():
    states = matchings()
    assert len(states) == 16
    maximum = -1
    witnesses = []
    for tail in permutations(V[1:]):
        order = (0,) + tail
        if order[1] > order[-1]:
            continue
        valid = [
            state
            for state in states
            if all(
                alternate(order, first, second)
                for first, second in combinations(state[1], 2)
            )
        ]
        covered = set().union(*(set(state[1]) for state in valid)) if valid else set()
        if len(covered) > maximum:
            maximum = len(covered)
            witnesses = [(order, valid, covered)]
        elif len(covered) == maximum:
            witnesses.append((order, valid, covered))

    print("maximum_covered_nonedges", maximum, "of", len(NONEDGES))
    print("witness_count", len(witnesses))
    for order, valid, covered in witnesses[:8]:
        print("order", order)
        print("states", valid)
        print("missing", sorted(NONEDGES - covered))


if __name__ == "__main__":
    main()
