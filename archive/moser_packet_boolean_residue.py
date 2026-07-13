#!/usr/bin/env python3
"""Boolean audit of the final two-state packet-derangement residue."""

from __future__ import annotations

from itertools import combinations, product

from moser_matching_hexagram_order import MATCHINGS


def frame(first: tuple[int, int], second: tuple[int, int]):
    return tuple(sorted((tuple(sorted(first)), tuple(sorted(second)))))


MODE_FRAMES = tuple(
    frozenset(frame(first, second) for first, second in combinations(mode, 2))
    for mode in MATCHINGS
)
FRAMES = tuple(sorted(set().union(*MODE_FRAMES)))


def name(value) -> str:
    return "|".join("".join(map(str, edge)) for edge in value)


def main() -> None:
    print("frames", len(FRAMES), [name(value) for value in FRAMES])
    for locked in combinations(range(5), 2):
        forced_false = set().union(*(MODE_FRAMES[i] for i in locked))
        free = [value for value in FRAMES if value not in forced_false]
        witnesses = []
        for bits in product((False, True), repeat=len(free)):
            owner = {value for value, bit in zip(free, bits) if bit}
            if any(not (owner & MODE_FRAMES[i]) for i in range(5) if i not in locked):
                continue
            # The minimum shore can choose a disjoint packet type in every mode
            # iff the opposite owner has not occupied all three types of a mode.
            if any(MODE_FRAMES[i] <= owner for i in range(5)):
                continue
            witnesses.append(owner)
        print(tuple(i + 1 for i in locked), "boolean_witnesses", len(witnesses))
        if witnesses:
            smallest = min(witnesses, key=lambda values: (len(values), sorted(values)))
            print(" ", [name(value) for value in sorted(smallest)])


if __name__ == "__main__":
    main()
