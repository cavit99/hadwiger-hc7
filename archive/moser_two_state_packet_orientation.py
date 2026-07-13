#!/usr/bin/env python3
"""Circular packet profiles forced by two deficient Moser modes."""

from __future__ import annotations

from itertools import combinations, permutations

from moser_matching_hexagram_order import MATCHINGS, alternate, realizes


def edge_name(edge: tuple[int, int]) -> str:
    return "".join(map(str, sorted(edge)))


def packet_types(order: tuple[int, ...], mode: int) -> tuple[str, ...]:
    matching = MATCHINGS[mode]
    return tuple(
        f"{edge_name(first)}|{edge_name(second)}"
        for first, second in combinations(matching, 2)
        if not alternate(order, first, second)
    )


def main() -> None:
    orders = [(0,) + tail for tail in permutations(range(1, 7))]
    for first, second in combinations(range(5), 2):
        profiles = {
            tuple(
                (mode + 1, packet_types(order, mode))
                for mode in range(5) if mode not in (first, second)
            )
            for order in orders
            if realizes(order, MATCHINGS[first])
            and realizes(order, MATCHINGS[second])
        }
        print((first + 1, second + 1), "profiles", len(profiles))
        for profile in sorted(profiles):
            print(" ", profile)


if __name__ == "__main__":
    main()
