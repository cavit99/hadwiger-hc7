#!/usr/bin/env python3
"""Verify the six-edge critical-kernel extraction barrier."""

from itertools import combinations


V = set(range(15))
F = [
    {9, 10, 11, 12, 13, 14},
    {3, 4, 7, 9, 10, 13},
    {0, 1, 2, 5, 8, 14},
    {0, 4, 5, 8, 11, 12},
    {1, 2, 7, 11, 12, 13},
    {4, 6, 7, 10, 12, 14},
]
PRIVATE_PAIRS = [
    {0, 7},
    {0, 12},
    {3, 12},
    {1, 10},
    {0, 10},
    {0, 13},
]


def transversal_number(family):
    for size in range(len(V) + 1):
        for candidate in combinations(V, size):
            if all(set(candidate) & edge for edge in family):
                return size
    raise AssertionError("finite family must have a transversal")


def main():
    assert all(len(edge) == 6 for edge in F)
    assert set().union(*F) == V
    assert transversal_number(F) == 3

    for i, pair in enumerate(PRIVATE_PAIRS):
        assert pair.isdisjoint(F[i])
        assert all(pair & F[j] for j in range(len(F)) if j != i)
        assert transversal_number(F[:i] + F[i + 1 :]) <= 2

    for indices in combinations(range(len(F)), 3):
        edges = [F[i] for i in indices]
        assert len(set().union(*edges)) <= 14
        assert len(set.intersection(*edges)) <= 2

    print("GREEN: tau=3, every deletion has tau<=2, and all triple bounds hold")


if __name__ == "__main__":
    main()
