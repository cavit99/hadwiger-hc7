#!/usr/bin/env python3
"""Transition table for contiguous interval reversals of valid SDR orders."""

from __future__ import annotations

from c6_circular_witness_smt import ORDERS, owned_base


VALID = {tuple(order) for order in ORDERS}


def normalize(word: list[int]) -> tuple[int, ...]:
    start = word.index(0)
    return tuple(word[start:] + word[:start])


def reverse_cyclic_interval(word: tuple[int, ...], start: int, length: int) -> tuple[int, ...]:
    indexes = [(start + offset) % 6 for offset in range(length)]
    result = list(word)
    values = [word[index] for index in indexes][::-1]
    for index, value in zip(indexes, values):
        result[index] = value
    return normalize(result)


def main() -> None:
    transitions = set()
    for word in ORDERS:
        source = owned_base(word)
        for length in range(2, 6):
            for start in range(6):
                target_word = reverse_cyclic_interval(word, start, length)
                if target_word not in VALID:
                    continue
                labels = frozenset(word[(start + offset) % 6] for offset in range(length))
                transitions.add((word, source, tuple(sorted(labels)), target_word,
                                 owned_base(target_word)))
    for word, source, labels, target, destination in sorted(transitions):
        print("".join(map(str, word)), source, labels, "->",
              "".join(map(str, target)), destination)
    print("transitions", len(transitions))


if __name__ == "__main__":
    main()
