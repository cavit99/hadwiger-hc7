#!/usr/bin/env python3
"""Dependency-light replay of all K2/K2 one-one portal certificates."""

import itertools
import json


N = set(range(7))
U = (0, 2, 4, 5, 6)
A, B, W = 1, 3, 7
DA = (8, 9)
DB = (10, 11)
M = {
    tuple(sorted(e))
    for e in (
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 6), (2, 6),
        (3, 4), (3, 5), (4, 5), (5, 6),
    )
}


def edges_for(defects):
    edges = set(M)
    edges.update({(A, W), (B, W), tuple(sorted(DA)), tuple(sorted(DB))})
    edges.update(tuple(sorted((A, x))) for x in DA)
    edges.update(tuple(sorted((B, x))) for x in DB)
    portals = set(U) | {W}
    for x, missed in zip(DA + DB, defects):
        edges.update(tuple(sorted((x, s))) for s in portals if s != missed)
    return edges


def connected(bag, edges):
    reached = {next(iter(bag))}
    while True:
        expanded = reached | {
            y for x in reached for y in bag
            if tuple(sorted((x, y))) in edges
        }
        if expanded == reached:
            return reached == bag
        reached = expanded


def adjacent(left, right, edges):
    return any(tuple(sorted((x, y))) in edges for x in left for y in right)


with open("portal_k2k2_certificate.json", encoding="utf-8") as source:
    archive = json.load(source)

assert archive["format"] == 1
expected = set(itertools.product((None,) + U + (W,), repeat=4))
seen = set()
for record in archive["records"]:
    defects = tuple(None if x == -1 else x for x in record["defects"])
    assert defects in expected and defects not in seen
    seen.add(defects)
    bags = [set(bag) for bag in record["bags"]]
    edges = edges_for(defects)
    assert len(bags) == 6 and all(bags)
    assert all(bag & N for bag in bags)
    assert all(bags[i].isdisjoint(bags[j])
               for i, j in itertools.combinations(range(6), 2))
    assert all(connected(bag, edges) for bag in bags)
    assert all(adjacent(bags[i], bags[j], edges)
               for i, j in itertools.combinations(range(6), 2))

assert seen == expected
assert len(seen) == 7 ** 4
print(f"verified {len(seen)} K2/K2 defect certificates")
