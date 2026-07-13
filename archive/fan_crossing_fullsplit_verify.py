#!/usr/bin/env python3
"""Dependency-free replay of the atomic fan/crossing K7 certificates."""

from __future__ import annotations

import itertools
import json


def edge(x: int, y: int):
    return (x, y) if x < y else (y, x)


ABSTRACT_TO_PHYSICAL = (0, 5, 2, 4, 6)
PRESENT = tuple(
    frozenset(pair) for pair in itertools.combinations(range(5), 2)
    if (pair[1] - pair[0]) % 5 not in (1, 4)
)


def graph_for(profile, first, second, px, py):
    moser = {
        edge(x, y) for x, y in {
            (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
            (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
        }
    }
    u = {0, 2, 4, 5, 6}
    a, w, v, body, z1, z2, x, y = 1, 7, 8, 9, 10, 11, 12, 13
    physical = {ABSTRACT_TO_PHYSICAL[i] for i in profile}
    fan_labels = physical | {a, w}
    body_labels = (u | {a, w}) - fan_labels
    return (
        moser
        | {edge(v, q) for q in range(7)}
        | {edge(body, z1), edge(body, z2), edge(z1, z2), edge(x, y)}
        | {edge(z, q) for z in (z1, z2) for q in fan_labels}
        | {edge(body, q) for q in body_labels}
        | {edge(x, q) for q in px}
        | {edge(y, q) for q in py}
    )


def connected(bag, edges):
    bag = set(bag)
    reached = {next(iter(bag))}
    while True:
        expanded = reached | {
            y for x, y in edges if x in reached and y in bag
        } | {
            x for x, y in edges if y in reached and x in bag
        }
        if expanded == reached:
            return reached == bag
        reached = expanded


def main() -> None:
    with open("fan_crossing_fullsplit_certificate.json", encoding="utf-8") as handle:
        records = json.load(handle)
    order = (0, 2, 6, 5, 4)
    u, b, w = {0, 2, 4, 5, 6}, 3, 7
    expected = set()
    for profile in PRESENT:
        for i, r, j, s in itertools.combinations(range(5), 4):
            first, second = frozenset({order[i], order[j]}), frozenset({order[r], order[s]})
            remaining = tuple((u | {b, w}) - first - second)
            for mask in range(1 << len(remaining)):
                px = first | {remaining[k] for k in range(len(remaining)) if mask >> k & 1}
                py = second | (set(remaining) - set(px))
                expected.add((tuple(sorted(profile)), tuple(sorted(first)), tuple(sorted(second)),
                              tuple(sorted(px)), tuple(sorted(py))))
    seen = set()
    for record in records:
        key = tuple(tuple(record[name]) for name in ("profile", "first", "second", "px", "py"))
        assert key in expected and key not in seen
        seen.add(key)
        profile, first, second, px, py = map(frozenset, key)
        assert first <= px and second <= py
        assert px.isdisjoint(py) and px | py == u | {b, w}
        edges = graph_for(profile, first, second, px, py)
        bags = [set(bag) for bag in record["bags"]]
        assert len(bags) == 7 and all(bags)
        assert all(bags[i].isdisjoint(bags[j]) for i in range(7) for j in range(i))
        assert all(connected(bag, edges) for bag in bags)
        assert all(
            any(edge(x, y) in edges for x in bags[i] for y in bags[j])
            for i in range(7) for j in range(i)
        )
    assert seen == expected and len(seen) == 200
    print("verified 200 atomic fan/full-split K7 certificates")


if __name__ == "__main__":
    main()
