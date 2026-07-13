#!/usr/bin/env python3
"""Dependency-free audit of the C5 vertex-state / 5-pole-state map."""

from __future__ import annotations

import itertools


def normalize(word: tuple[int, ...]) -> tuple[int, ...]:
    seen: list[int] = []
    out: list[int] = []
    for value in word:
        if value not in seen:
            seen.append(value)
        out.append(seen.index(value))
    return tuple(out)


def vertex_states() -> set[tuple[int, ...]]:
    out = set()
    for word in itertools.product(range(4), repeat=5):
        if any(word[i] == word[(i + 1) % 5] for i in range(5)):
            continue
        out.add(normalize(word))
    return out


def semiedge_state(word: tuple[int, ...]) -> tuple[int, ...]:
    # Four vertex colours are F_2^2 = {0,1,2,3}; addition is xor.
    differences = tuple(word[i] ^ word[(i + 1) % 5] for i in range(5))
    assert 0 not in differences
    return normalize(differences)


def admissible_semiedge_states() -> set[tuple[int, ...]]:
    # For five semiedges, the parity lemma says every one of the three
    # edge colours occurs an odd number of times.
    out = set()
    for word in itertools.product((1, 2, 3), repeat=5):
        if all(word.count(c) % 2 == 1 for c in (1, 2, 3)):
            out.add(normalize(word))
    return out


def main() -> None:
    vertices = vertex_states()
    image = {semiedge_state(word) for word in vertices}
    admissible = admissible_semiedge_states()
    assert len(vertices) == 10
    assert len(image) == 10
    assert image == admissible
    print("verified 10 C5 equality states biject with 10 admissible 5-pole states")


if __name__ == "__main__":
    main()
