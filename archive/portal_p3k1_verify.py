#!/usr/bin/env python3
"""Independent replay of the P3/opposite-shore K6 certificates."""

import itertools
import json


N = set(range(7))
U = (0, 2, 4, 5, 6)
A, B, W = 1, 3, 7
DA = (8, 9, 10)
DB = 11
LABELS = U + (W, A)
M = {
    tuple(sorted(e))
    for e in (
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 6), (2, 6),
        (3, 4), (3, 5), (4, 5), (5, 6),
    )
}


def valid(rows, aw):
    if rows[0].bit_count() < 6 or rows[1].bit_count() < 5 or rows[2].bit_count() < 6:
        return False
    if rows[0] | rows[1] | rows[2] != 127:
        return False
    contacts = sum(bool(row & 64) for row in rows)
    return 4 + int(aw) + contacts >= 7


def edges_for(rows, aw):
    edges = set(M)
    edges.update({(8, 9), (9, 10)})
    if aw:
        edges.add((A, W))
    for d, row in zip(DA, rows):
        edges.update(tuple(sorted((d, LABELS[i]))) for i in range(7) if row >> i & 1)
    edges.update(tuple(sorted((DB, x))) for x in set(U) | {W, B})
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


choices = (
    [row for row in range(128) if row.bit_count() >= 6],
    [row for row in range(128) if row.bit_count() >= 5],
    [row for row in range(128) if row.bit_count() >= 6],
)
expected = {
    (aw, rows)
    for aw in (False, True)
    for rows in itertools.product(*choices)
    if valid(rows, aw)
}

with open("portal_p3k1_certificate.json", encoding="utf-8") as source:
    archive = json.load(source)

assert archive["format"] == 1
seen = set()
for record in archive["records"]:
    key = (record["aw"], tuple(record["rows"]))
    assert key in expected and key not in seen
    seen.add(key)
    edges = edges_for(key[1], key[0])
    bags = [set(bag) for bag in record["bags"]]
    assert len(bags) == 6 and all(bag & N for bag in bags)
    assert all(bags[i].isdisjoint(bags[j])
               for i, j in itertools.combinations(range(6), 2))
    assert all(connected(bag, edges) for bag in bags)
    assert all(adjacent(bags[i], bags[j], edges)
               for i, j in itertools.combinations(range(6), 2))

assert seen == expected
assert len(seen) == 2729
print(f"verified {len(seen)} P3/K1 certificates")
