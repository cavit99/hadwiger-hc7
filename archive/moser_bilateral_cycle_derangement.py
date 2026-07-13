#!/usr/bin/env python3
"""Search for two circular portal orders realizing packet derangement."""

from __future__ import annotations

from itertools import combinations, permutations

from moser_matching_hexagram_order import MATCHINGS, alternate, realizes


ORDERS = tuple((0,) + tail for tail in permutations(range(1, 7)))
FRAMES = tuple(
    tuple((mode, first, second) for first, second in combinations(matching, 2))
    for mode, matching in enumerate(MATCHINGS)
)


def packets(order: tuple[int, ...], mode: int):
    return {
        tuple(sorted((tuple(sorted(first)), tuple(sorted(second)))))
        for _, first, second in FRAMES[mode]
        if not alternate(order, first, second)
    }


def main() -> None:
    total = 0
    for locked in combinations(range(5), 2):
        witnesses = []
        for far in ORDERS:
            if not all(realizes(far, MATCHINGS[i]) for i in locked):
                continue
            far_packets = tuple(packets(far, i) for i in range(5))
            if any(not far_packets[i] for i in range(5) if i not in locked):
                continue
            for near in ORDERS:
                near_packets = tuple(packets(near, i) for i in range(5))
                if any(not near_packets[i] for i in range(5)):
                    continue
                if any(
                    near_packets[i] & far_packets[i]
                    for i in range(5) if i not in locked
                ):
                    continue
                witnesses.append((far, near, far_packets, near_packets))
                break
            if witnesses:
                break
        print(tuple(i + 1 for i in locked), "cycle_derangement", bool(witnesses))
        if witnesses:
            total += 1
            far, near, far_packets, near_packets = witnesses[0]
            print(" far", far, "near", near)
            for mode in range(5):
                fmt = lambda values: [
                    "|".join("".join(map(str, edge)) for edge in value)
                    for value in sorted(values)
                ]
                print("  mode", mode + 1, "far", fmt(far_packets[mode]),
                      "near", fmt(near_packets[mode]))
    print("locked_pairs_with_witness", total)


if __name__ == "__main__":
    main()
