#!/usr/bin/env python3
"""Probe static K7 models in the C6+K1 boundary plus a C4 shore square.

This is an invariant finder, not a proof certificate.  Boundary vertices
are 0,...,6, square helpers 7,...,10, and the opposite full helper is 11.
"""

from __future__ import annotations

import itertools


S = tuple(range(7))
Q = tuple(range(7, 11))
H = 11
V = tuple(range(12))
MISSING = {(0, 4), (0, 5), (1, 3), (1, 5), (2, 3), (2, 4)}
BOUNDARY = set(itertools.combinations(S, 2)) - MISSING
SQUARE = {(7, 8), (8, 9), (9, 10), (7, 10)}


def edges(rows: tuple[int, int, int, int]) -> set[tuple[int, int]]:
    answer = set(BOUNDARY) | set(SQUARE)
    answer.update((s, H) for s in S)
    for i, row in enumerate(rows):
        answer.update((s, Q[i]) for s in S if row >> s & 1)
    return {tuple(sorted(e)) for e in answer}


def k7_model(edge_set: set[tuple[int, int]]):
    adjacency = [0] * len(V)
    for u, v in edge_set:
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u

    connected = []
    nbr = {}
    for mask in range(1, 1 << len(V)):
        reached = mask & -mask
        while True:
            expanded = reached
            bits = reached
            while bits:
                bit = bits & -bits
                expanded |= adjacency[bit.bit_length() - 1] & mask
                bits ^= bit
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            connected.append(mask)
            union = 0
            bits = mask
            while bits:
                bit = bits & -bits
                union |= adjacency[bit.bit_length() - 1]
                bits ^= bit
            nbr[mask] = union

    # Larger branch-set supports first gives much faster witnesses.
    connected.sort(key=lambda m: (-m.bit_count(), m))

    def rec(chosen, candidates, used):
        if len(chosen) == 7:
            return chosen
        needed = 7 - len(chosen)
        for pos, bag in enumerate(candidates):
            if bag & used:
                continue
            nxt = [other for other in candidates[pos + 1 :]
                   if not other & (used | bag) and nbr[bag] & other]
            if len(nxt) >= needed - 1:
                result = rec(chosen + [bag], nxt, used | bag)
                if result:
                    return result
        return None

    return rec([], connected, 0)


def fmt(mask):
    return tuple(i for i in S if mask >> i & 1)


def main():
    # Q0,Q1 form one grouped side and Q2,Q3 the other.  The base rows
    # cover S.  The augmented rows duplicate label 6 across the grouping.
    base = (
        1 << 6,
        1 << 0,
        (1 << 1) | (1 << 2) | (1 << 5),
        (1 << 3) | (1 << 4),
    )
    duplicated = list(base)
    duplicated[2] |= 1 << 6
    tests = (base, tuple(duplicated))
    for name, rows in zip(("base", "duplicated-6"), tests):
        model = k7_model(edges(rows))
        print(name, tuple(fmt(row) for row in rows),
              "K7-model", model)
        assert model is None

    # Even replacing the square by a K4 does not close the promoted
    # joint-edge core from hadwiger_c6_specified_side_warehouse_exchange.
    # Q0,Q1 are the edge endpoints.  Q2,Q3 form a body missing only 0,
    # and 0 is contacted by both endpoints.
    joint_rows = (
        (1 << 0) | (1 << 6),
        1 << 0,
        (1 << 1) | (1 << 2) | (1 << 5) | (1 << 6),
        (1 << 3) | (1 << 4),
    )
    joint_edges = edges(joint_rows) | set(itertools.combinations(Q, 2))
    model = k7_model(joint_edges)
    print("joint-edge-K4", tuple(fmt(row) for row in joint_rows),
          "K7-model", model)
    assert model is None


if __name__ == "__main__":
    main()
