#!/usr/bin/env python3
"""Exact circular-order audit for the five fixed-13 Moser matchings."""

from itertools import combinations, permutations


MATCHINGS = (
    ((0, 5), (1, 3), (2, 4)),
    ((0, 5), (1, 3), (4, 6)),
    ((0, 6), (1, 3), (2, 4)),
    ((0, 6), (1, 3), (2, 5)),
    ((1, 3), (2, 5), (4, 6)),
)


def alternate(order, first, second):
    position = {vertex: index for index, vertex in enumerate(order)}
    size = len(order)
    a, b = first
    c, d = second

    def inside(vertex):
        return (
            0
            < (position[vertex] - position[a]) % size
            < (position[b] - position[a]) % size
        )

    return inside(c) != inside(d)


def realizes(order, matching):
    return all(
        alternate(order, first, second)
        for first, second in combinations(matching, 2)
    )


def main():
    signatures = {}
    maximum = 0
    witnesses = {}

    # Fix vertex 0 first to quotient cyclic rotation. Retaining reversals
    # is harmless and makes the check especially transparent.
    for tail in permutations(range(1, 7)):
        order = (0,) + tail
        signature = tuple(
            index
            for index, matching in enumerate(MATCHINGS)
            if realizes(order, matching)
        )
        maximum = max(maximum, len(signature))
        signatures[signature] = signatures.get(signature, 0) + 1
        witnesses.setdefault(signature, order)

    assert maximum == 3
    assert not any(len(signature) >= 4 for signature in signatures)

    maximal_triples = sorted(
        tuple(index + 1 for index in signature)
        for signature in signatures
        if len(signature) == 3
    )
    assert maximal_triples == [
        (1, 2, 3),
        (1, 2, 5),
        (1, 3, 4),
        (2, 4, 5),
        (3, 4, 5),
    ]

    print("orders_checked", 720)
    print("maximum_simultaneous_matchings", maximum)
    print("maximal_triples", maximal_triples)


if __name__ == "__main__":
    main()
