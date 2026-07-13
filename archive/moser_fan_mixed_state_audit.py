#!/usr/bin/env python3
"""Audit mixed singleton collisions and the W5 fixed-colouring warning."""

from __future__ import annotations

import itertools
from collections import Counter, defaultdict

from moser_fan_list_atlas import PALETTE, rows
from moser_safe_transition_state_probe import NONEDGES, kind, matching
from wheel_safe_transition_search import (
    A,
    W,
    ABSTRACT_TO_PHYSICAL,
    boundary_colours,
)


def residual_states():
    return [
        es
        for q in (2, 3)
        for es in itertools.combinations(NONEDGES, q)
        if matching(es) and kind(es) != "decorated-T trace"
    ]


def singleton_collisions() -> Counter[tuple[str, str]]:
    ordinary = rows()[:5]
    collisions: Counter[tuple[str, str]] = Counter()
    for es in residual_states():
        for wc in range(6):
            colours = boundary_colours(es, wc)
            for hc in range(6):
                groups: dict[int, list[str]] = defaultdict(list)
                for name, profile, extras in ordinary:
                    physical = {ABSTRACT_TO_PHYSICAL[i] for i in profile}
                    forbidden = {
                        hc,
                        *(colours[x] for x in physical | set(extras)),
                    }
                    available = PALETTE - forbidden
                    if len(available) == 1:
                        groups[next(iter(available))].append(name)
                for names in groups.values():
                    for first, second in itertools.combinations(names, 2):
                        collisions[tuple(sorted((first, second)))] += 1
    return collisions


def wheel_warning() -> None:
    # Boundary blocks {0,5}|{1,3}|{2}|{4}|{6}, and w repeats colour 2.
    colours = boundary_colours(((0, 5), (1, 3)), 2)
    word = ((0, 2), (0, 3), (1, 3), (1, 4), (2, 4))
    contacts = {i: {A, W} for i in range(6)}
    for i, profile in enumerate(word):
        contacts[i].update(ABSTRACT_TO_PHYSICAL[j] for j in profile)
    # Vertex 5 is the hub and has only the reserved contacts a,w.

    def allowed(vertex: int, hub_colour: int | None = None) -> set[int]:
        forbidden = {colours[x] for x in contacts[vertex]}
        if vertex < 5 and hub_colour is not None:
            forbidden.add(hub_colour)
        return set(PALETTE) - forbidden

    # With hub colour 4, the consecutive 03 and 13 rows both force 5.
    assert allowed(1, 4) == {5}
    assert allowed(2, 4) == {5}

    # The remaining rim path 3-4-0 and hub have a proper colouring.
    partial = {0: 3, 3: 3, 4: 0, 5: 4}
    assert all(partial[x] in allowed(x) for x in partial)
    partial_edges = ((3, 4), (4, 0), (5, 0), (5, 3), (5, 4))
    assert all(partial[x] != partial[y] for x, y in partial_edges)

    # Recolouring the whole wheel gives an extension of the same boundary state.
    extension = {0: 3, 1: 4, 2: 5, 3: 3, 4: 5, 5: 0}
    assert all(extension[x] in allowed(x) for x in extension)
    wheel_edges = [
        *((i, (i + 1) % 5) for i in range(5)),
        *((5, i) for i in range(5)),
    ]
    assert all(extension[x] != extension[y] for x, y in wheel_edges)


def main() -> None:
    collisions = singleton_collisions()
    expected = {
        ("P03", "P13"),
        ("P02", "P24"),
        ("P02", "P03"),
        ("P14", "P24"),
        ("P13", "P14"),
        ("P02", "P14"),
        ("P03", "P24"),
    }
    assert set(collisions) == expected
    wheel_warning()
    print("distinct-profile singleton collisions", len(collisions))
    for pair, count in sorted(collisions.items()):
        print(pair, count)
    print("W5 fixed-colouring warning verified")


if __name__ == "__main__":
    main()
