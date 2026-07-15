#!/usr/bin/env python3
"""Verify the two parity extension languages on K4 disjoint-union K4."""

from __future__ import annotations

from itertools import combinations, permutations


X = tuple(range(4))
Y = tuple(range(4, 8))


def permutation_sign(values: tuple[int, ...]) -> int:
    inversions = sum(values[i] > values[j]
                     for i in range(4) for j in range(i + 1, 4))
    return inversions % 2


def partition_from_permutation(sigma: tuple[int, ...], omitted: int | None = None):
    blocks = []
    for i in X:
        if i == omitted:
            blocks.append(frozenset({i}))
        else:
            blocks.append(frozenset({i, 4 + sigma[i]}))
    if omitted is not None:
        blocks.append(frozenset({4 + sigma[omitted]}))
    return frozenset(blocks)


def main() -> None:
    languages = {0: set(), 1: set()}
    for sigma in permutations(range(4)):
        sign = permutation_sign(sigma)
        languages[sign].add(partition_from_permutation(sigma))
        for omitted in X:
            languages[sign].add(partition_from_permutation(sigma, omitted))

    assert languages[0].isdisjoint(languages[1])
    assert all(len(state) <= 6 for states in languages.values() for state in states)

    independent_sets = [frozenset({v}) for v in range(8)]
    independent_sets += [frozenset({x, y}) for x in X for y in Y]
    for block in independent_sets:
        for sign in (0, 1):
            assert any(block in state for state in languages[sign])

    # Width-five decomposition of I2 vee (K4 dot-union K4).
    apex = {8, 9}
    bags = [apex | set(X), apex | set(Y)]
    assert max(map(len, bags)) == 6
    edges = set(combinations(X, 2)) | set(combinations(Y, 2))
    edges |= {(a, s) for a in apex for s in range(8)}
    assert all(any(u in bag and v in bag for bag in bags) for u, v in edges)

    print("GREEN: parity languages are disjoint and answer every private-block query")


if __name__ == "__main__":
    main()
