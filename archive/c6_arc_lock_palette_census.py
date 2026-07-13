#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Exact six-colour state census for complementary C6 arc rows."""

from __future__ import annotations

import collections
import itertools


def states() -> tuple[tuple[int, ...], ...]:
    out: list[tuple[int, ...]] = []

    def rec(word: list[int], maximum: int) -> None:
        if len(word) == 7:
            state = tuple(word)
            if max(state) >= 6:
                return
            if any(state[i] == state[(i + 1) % 6] for i in range(6)):
                return
            if any(state[i] == state[6] for i in range(6)):
                return
            out.append(state)
            return
        for colour in range(min(maximum + 1, 5) + 1):
            if colour <= maximum + 1:
                word.append(colour)
                rec(word, max(maximum, colour))
                word.pop()

    rec([0], 0)
    return tuple(out)


def arcs(distance: int) -> tuple[set[int], set[int]]:
    first = set(range(distance + 1))
    second = {0}
    current = 0
    while current != distance:
        current = (current - 1) % 6
        second.add(current)
    return first, second


def category(
    state: tuple[int, ...],
    alpha: int,
    first: set[int],
    second: set[int],
) -> str | None:
    colours_first = {state[x] for x in first}
    colours_second = {state[x] for x in second}
    other = set(range(6)) - {alpha}
    if not (
        (alpha in colours_first or other <= colours_first)
        and (alpha in colours_second or other <= colours_second)
    ):
        return None
    common = first & second
    if any(state[x] == alpha for x in common):
        return "common-alpha"
    if alpha in colours_first and alpha in colours_second:
        return "split-alpha"
    if alpha not in colours_first and alpha not in colours_second:
        return "both-full-other"
    if alpha not in colours_first:
        return "first-full-other"
    return "second-full-other"


def main() -> None:
    all_states = states()
    assert len(all_states) == 40
    alpha_absent: list[tuple[int, int, int, tuple[int, ...], int]] = []

    for distance in (1, 2, 3):
        base_first, base_second = arcs(distance)
        for z_first, z_second in itertools.product((0, 1), repeat=2):
            first = base_first | ({6} if z_first else set())
            second = base_second | ({6} if z_second else set())
            counts: collections.Counter[str] = collections.Counter()
            for state in all_states:
                for alpha in range(6):
                    kind = category(state, alpha, first, second)
                    if kind is not None:
                        counts[kind] += 1
                        if kind == "both-full-other":
                            alpha_absent.append(
                                (distance, z_first, z_second, state, alpha)
                            )
            print(
                distance,
                z_first,
                z_second,
                len(first),
                len(second),
                dict(counts),
            )

    expected = {
        (3, 1, 1, (0, 1, 2, 3, 1, 2, 4), 5),
        (3, 1, 1, (0, 1, 2, 3, 2, 1, 4), 5),
    }
    assert set(alpha_absent) == expected
    print("alpha-absent two-sided locks:", len(alpha_absent))
    for item in alpha_absent:
        print(item)


if __name__ == "__main__":
    main()

