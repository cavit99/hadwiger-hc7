#!/usr/bin/env python3
"""Search small static full-deletion hub cycles over the C6+K1 gate.

This is an invariant/counterarchitecture finder.  It asks whether the
hub-cycle hypotheses before operation-state compatibility already force a
K7 minor.  The first shore is K4, every boundary label has at least two
portals there (so deletion of every shore vertex leaves it full), every
shore vertex has at most four boundary contacts, and a second full shore is
represented by one helper vertex.
"""

from __future__ import annotations

import itertools
import random

from contact_order7_sixedge_web_probe import generic_minor_model


S = tuple(range(7))
D = tuple(range(7, 11))
H = 11

MISSING = {(0, 4), (0, 5), (1, 3), (1, 5), (2, 3), (2, 4)}
BOUNDARY = set(itertools.combinations(S, 2)) - MISSING


def host(rows: tuple[int, ...]) -> set[tuple[int, int]]:
    e = set(BOUNDARY)
    e.update(itertools.combinations(D, 2))
    e.update((s, H) for s in S)
    for u, row in zip(D, rows):
        e.update((s, u) for s in S if row >> s & 1)
    return {tuple(sorted(x)) for x in e}


def first_three_full_deletion(rows: tuple[int, ...]) -> bool:
    # D[H] contains the triangle on the first three K4 vertices.  For each
    # of these deletions the remaining shore must still contact every label.
    return all(
        any(i != deleted and rows[i] >> s & 1 for i in range(4))
        for deleted in range(3) for s in S
    )


def fmt(rows: tuple[int, ...]):
    return tuple(tuple(s for s in S if row >> s & 1) for row in rows)


def main() -> None:
    manual = (
        sum(1 << s for s in (0, 1, 2, 6)),
        sum(1 << s for s in (0, 5)),
        sum(1 << s for s in (1, 2, 5, 6)),
        sum(1 << s for s in (3, 4)),
    )
    print("manual", fmt(manual), "K7-model", generic_minor_model(12, host(manual), 7))

    # Minimal portal patterns when vertices 7,8,9 are all full-deletion
    # hubs and vertex 10 is the fourth bag: each boundary label either has
    # its sole portal at 10, or has portals at a pair of the three hubs.
    options = ((3,), (0, 1), (0, 2), (1, 2))
    for number, word in enumerate(itertools.product(range(4), repeat=7), 1):
        min_rows = [0, 0, 0, 0]
        for s, choice in enumerate(word):
            for i in options[choice]:
                min_rows[i] |= 1 << s
        if generic_minor_model(12, host(tuple(min_rows)), 7) is None:
            print("minimal negative", word, fmt(tuple(min_rows)))
            return
    print("all", 4**7, "minimal triangle-hub patterns force K7")
    return
    rng = random.Random(7107)
    candidates = tuple(
        sum(1 << s for s in row)
        for size in range(2, 5)
        for row in itertools.combinations(S, size)
    )
    tested = 0
    for _ in range(20000):
        rows = tuple(rng.choice(candidates) for _ in D)
        if not first_three_full_deletion(rows):
            continue
        tested += 1
        model = generic_minor_model(12, host(rows), 7)
        if model is None:
            print("negative", fmt(rows), "tested", tested)
            return
    print("no negative in", tested, "eligible samples")


if __name__ == "__main__":
    main()
