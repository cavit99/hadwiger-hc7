#!/usr/bin/env python3
"""Sharp audit for the split-clean-path obstruction at K3+2K2.

The graph is the seven-vertex boundary whose missing graph is
K3+2K2, together with two nonadjacent full helper vertices.  It has
two disjoint boundary-clean paths for the two missing K2 pairs, but no
K7 minor.  Its connectivity is exactly six, showing why seven-
connectivity and a *same-shore* crossing are essential.
"""

import itertools

from contact_order7_five_edge_verify import (
    K3_2K2,
    k_minor_model,
    quotient_edges,
)


S = set(range(7))
V = set(range(9))
EDGES = quotient_edges(K3_2K2)


def connected_after(deleted):
    remaining = V - set(deleted)
    if len(remaining) <= 1:
        return True
    start = next(iter(remaining))
    reached = {start}
    while True:
        expanded = reached | {
            y
            for x in reached
            for y in remaining
            if tuple(sorted((x, y))) in EDGES
        }
        if expanded == reached:
            return reached == remaining
        reached = expanded


def path_edges(path):
    return {
        tuple(sorted((path[i], path[i + 1])))
        for i in range(len(path) - 1)
    }


def main():
    # Helpers 7 and 8 are singleton connected shores, each full to S.
    assert all(tuple(sorted((h, s))) in EDGES for h in (7, 8) for s in S)
    assert (7, 8) not in EDGES

    # The paths repair missing pairs 12 and 34, are vertex-disjoint, and
    # meet the boundary only at their displayed ends.
    p = (1, 7, 2)
    q = (3, 8, 4)
    assert path_edges(p) <= EDGES
    assert path_edges(q) <= EDGES
    assert set(p).isdisjoint(q)
    assert set(p) & S == {1, 2}
    assert set(q) & S == {3, 4}

    # Exact connected-branch-set search from the five-edge atlas.
    assert k_minor_model(EDGES) is None

    # The graph is 6-connected, but not 7-connected.
    for size in range(6):
        assert all(connected_after(cut) for cut in itertools.combinations(V, size))
    six_cut = {3, 4, 5, 6, 7, 8}
    assert not connected_after(six_cut)

    print("two split clean paths verified:", p, q)
    print("exact K7 branch-set search: none")
    print("vertex connectivity: exactly 6")


if __name__ == "__main__":
    main()
