#!/usr/bin/env python3
"""Exhaust the pure-Moser pentagon state system with pair transfer.

Values 0, 1, 2 assign a boundary state to neither side, side 1, or
side 2.  Exclusivity is built into this encoding.  The check supplements
the previous axioms by the geometric fact that two vertex-disjoint missing
edges supported on one side force their triple state on the opposite side.
"""

from itertools import product


P_EDGES = ((0, 2), (0, 3), (1, 3), (1, 4), (2, 4))
STATES = tuple(("D", i) for i in range(5)) + tuple(
    ("T", i, j) for i, j in P_EDGES
)


def compatible(word, assignment):
    owner = dict(zip(STATES, assignment))

    # A side not supporting e_i admits the one-swap state D_i.
    for i, symbol in enumerate(word):
        if symbol == "1" and owner[("D", i)] != 2:
            return False
        if symbol == "2" and owner[("D", i)] != 1:
            return False

    # Every side has a two-anchor state extending D_i.
    for side in (1, 2):
        for i in range(5):
            incident = [
                ("T", a, b) for a, b in P_EDGES if i in (a, b)
            ]
            if owner[("D", i)] != side and not any(
                owner[state] == side for state in incident
            ):
                return False

    # Supported-pair transfer: paths in side s yield T_ij on side 3-s.
    for i, j in P_EDGES:
        if word[i] in "1B" and word[j] in "1B":
            if owner[("T", i, j)] != 2:
                return False
        if word[i] in "2B" and word[j] in "2B":
            if owner[("T", i, j)] != 1:
                return False

    return True


def feasible(word):
    return any(compatible(word, assignment) for assignment in product(range(3), repeat=10))


REPRESENTATIVES = (
    "11112", "11122", "1112B", "11212", "1121B", "1122B",
    "112B2", "112BB", "11B2B", "1212B", "121BB", "12B1B",
    "12BBB", "1B2BB",
)


def main():
    result = {word: feasible(word) for word in REPRESENTATIVES}
    assert not any(result.values()), result
    print("verified: all 14 genuinely mixed support orbits are infeasible")
    print(" ".join(REPRESENTATIVES))


if __name__ == "__main__":
    main()
