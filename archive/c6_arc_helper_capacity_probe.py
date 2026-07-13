#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Discover one-defect helper capacity in the antipodal arc quotient."""

from __future__ import annotations

from contact_order7_sixedge_web_probe import generic_minor_model


PAIRS = ((1, 5), (2, 4), (1, 4), (2, 5))


def graph(
    mode: str,
    pair: tuple[int, int],
    deficient_helper: int,
    missed_label: int,
) -> set[tuple[int, int]]:
    edges = {
        tuple(sorted((i, (i + 1) % 6))) for i in range(6)
    } | {(i, 6) for i in range(6)} | {(9, 10)}
    edges.add((7, 8) if mode == "O" else (8, 9))
    for s in range(7):
        if deficient_helper != 7 or s != missed_label:
            edges.add(tuple(sorted((s, 7))))
        if deficient_helper != 8 or s != missed_label:
            edges.add(tuple(sorted((s, 8))))
    for s in (0, 1, 2, 3, 6):
        edges.add(tuple(sorted((s, 9))))
    for s in (0, 3, 4, 5, 6):
        edges.add(tuple(sorted((s, 10))))
    for s in pair:
        edges.add(tuple(sorted((s, 11))))
    return edges


def main() -> None:
    for mode in ("O", "A"):
        for pair in PAIRS:
            for helper in (7, 8):
                negative = []
                for missed in range(7):
                    model = generic_minor_model(
                        12, graph(mode, pair, helper, missed), 7
                    )
                    if model is None:
                        negative.append(missed)
                print(mode, pair, helper, tuple(negative))


if __name__ == "__main__":
    main()

