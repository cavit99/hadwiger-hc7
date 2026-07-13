#!/usr/bin/env python3
"""Exact circular checks used in the arbitrary-order wheel reduction."""

from __future__ import annotations

import itertools


ORDERS = ((0, 2, 4, 1, 3), (0, 3, 1, 4, 2))
PRESENT = tuple(
    frozenset(pair) for pair in itertools.combinations(range(5), 2)
    if (pair[1] - pair[0]) % 5 not in (1, 4)
)
TRIPLES = tuple(
    frozenset({i, (i + 1) % 5, (i + 3) % 5}) for i in range(5)
)


def frame(j: int):
    return ((j + 1) % 5, (j + 2) % 5,
            (j + 3) % 5, (j + 4) % 5)


def alternates(a: int, b: int, c: int, d: int, n: int) -> bool:
    def between(x: int, p: int, q: int) -> bool:
        return 0 < (x - p) % n < (q - p) % n
    return between(c, a, b) != between(d, a, b)


def crossless(occurrences: dict[int, set[int]], n: int) -> bool:
    for j in range(5):
        a, b, c, d = frame(j)
        for pa, pb, pc, pd in itertools.product(
            occurrences[a], occurrences[b], occurrences[c], occurrences[d]
        ):
            if {pa, pb}.isdisjoint({pc, pd}):
                if pa == pb or pc == pd:
                    return False
                if len({pa, pb, pc, pd}) != 4 or not alternates(pa, pb, pc, pd, n):
                    return False
    return True


def admissible(word: tuple[frozenset[int], ...]) -> bool:
    if set().union(*word) != set(range(5)):
        return False
    for i, triple in enumerate(TRIPLES):
        if triple in word:
            shield = (i + 3) % 5
            if sum(shield in profile for profile in word) != 1:
                return False
    occurrences = {
        i: {p for p, profile in enumerate(word) if i in profile}
        for i in range(5)
    }
    return crossless(occurrences, len(word))


def profile_word_check() -> None:
    profiles = PRESENT + TRIPLES
    counts = {}
    for n in (5, 6):
        words = [w for w in itertools.product(profiles, repeat=n) if admissible(w)]
        ordinary = [w for w in words if all(len(p) == 2 for p in w)]
        locked = [w for w in words if any(len(p) == 3 for p in w)]
        counts[n] = (len(words), len(ordinary), len(locked))
        for word in locked:
            triples = [p for p in word if len(p) == 3]
            assert len(triples) == 1
            triple = triples[0]
            i = TRIPLES.index(triple)
            complement = frozenset({(i + 2) % 5, (i + 4) % 5})
            assert all(p == triple or p == complement for p in word)
    assert counts == {5: (35, 10, 25), 6: (30, 0, 30)}, counts


def main() -> None:
    profile_word_check()
    print("verified length-five/six wheel profile classification")


if __name__ == "__main__":
    main()
