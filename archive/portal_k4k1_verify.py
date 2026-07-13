#!/usr/bin/env python3
"""Dependency-free replay of the order-four-shore K6 certificate.

The archive contains monotone model supports.  This verifier checks every
support directly and then exhausts every automorphism-canonical attachment
system satisfying all degree, full-attachment, terminal-degree, and local
seven-connectivity inequalities.  Every such system must contain a certified
support.
"""

import itertools
import json


N = set(range(7))
U = (0, 2, 4, 5, 6)
A, B, W = 1, 3, 7
DA = (8, 9, 10, 11)
DB = 12
LABELS = U + (W, A)
M = {
    tuple(sorted(e))
    for e in (
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 6), (2, 6),
        (3, 4), (3, 5), (4, 5), (5, 6),
    )
}
TYPES = {
    "p4": {(0, 1), (1, 2), (2, 3)},
    "claw": {(0, 1), (0, 2), (0, 3)},
    "c4": {(0, 1), (1, 2), (2, 3), (0, 3)},
    "paw": {(0, 1), (1, 2), (0, 2), (0, 3)},
    "diamond": {(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)},
    "k4": set(itertools.combinations(range(4), 2)),
}


def automorphisms(fedges):
    canon = {tuple(sorted(e)) for e in fedges}
    return [
        p for p in itertools.permutations(range(4))
        if {tuple(sorted((p[x], p[y]))) for x, y in canon} == canon
    ]


def canonical(rows, autos):
    return all(rows <= tuple(rows[p[i]] for i in range(4)) for p in autos)


def row_options(fedges):
    degrees = [sum(i in e for e in fedges) for i in range(4)]
    return [tuple(row for row in range(128) if row.bit_count() >= 7 - degree) for degree in degrees]


def row_systems(name, fedges):
    options = row_options(fedges)
    if name == "claw":
        for r0 in options[0]:
            for tail in itertools.combinations_with_replacement(options[1], 3):
                yield (r0,) + tail
        return
    if name == "paw":
        for r0 in options[0]:
            for r1, r2 in itertools.combinations_with_replacement(options[1], 2):
                for r3 in options[3]:
                    yield (r0, r1, r2, r3)
        return
    if name == "diamond":
        for r0, r1 in itertools.combinations_with_replacement(options[0], 2):
            for r2, r3 in itertools.combinations_with_replacement(options[2], 2):
                yield (r0, r1, r2, r3)
        return
    if name == "k4":
        yield from itertools.combinations_with_replacement(options[0], 4)
        return
    autos = automorphisms(fedges)
    for rows in itertools.product(*options):
        if canonical(rows, autos):
            yield rows


def valid(rows, aw, fedges):
    if rows[0] | rows[1] | rows[2] | rows[3] != 127:
        return False
    if int(aw) + sum(bool(row & 64) for row in rows) < 3:
        return False
    for mask in range(1, 15):
        outside_internal = {
            y
            for x in range(4) if mask >> x & 1
            for y in range(4) if not (mask >> y & 1)
            if tuple(sorted((x, y))) in fedges
        }
        union = 0
        for i, row in enumerate(rows):
            if mask >> i & 1:
                union |= row
        if union.bit_count() + len(outside_internal) < 7:
            return False
    return True


def fixed_edges(fedges):
    edges = set(M)
    edges.update(tuple(sorted((DA[i], DA[j]))) for i, j in fedges)
    edges.update(tuple(sorted((DB, x))) for x in set(U) | {W, B})
    return edges


def required_edges(required):
    edges = set()
    mask = 0
    for key in required:
        if key[0] == "aw":
            assert key == ["aw"]
            edges.add(tuple(sorted((A, W))))
            mask |= 1 << 28
        else:
            assert key[0] == "x" and len(key) == 3
            i, j = key[1], key[2]
            assert 0 <= i < 4 and 0 <= j < 7
            edges.add(tuple(sorted((DA[i], LABELS[j]))))
            mask |= 1 << (7 * i + j)
    return edges, mask


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


def truth_mask(rows, aw):
    mask = int(aw) << 28
    for i, row in enumerate(rows):
        mask |= row << (7 * i)
    return mask


with open("portal_k4k1_cegis_result.json", encoding="utf-8") as source:
    archive = json.load(source)

assert archive["format"] == 1
assert set(archive["types"]) == set(TYPES)

grand_total = 0
for name, fedges in TYPES.items():
    section = archive["types"][name]
    assert {tuple(edge) for edge in section["internal_edges"]} == fedges
    assert section["survivor"] is None
    fixed = fixed_edges(fedges)
    support_masks = []
    for record in section["supports"]:
        extra, support_mask = required_edges(record["required"])
        edges = fixed | extra
        bags = [set(bag) for bag in record["bags"]]
        assert len(bags) == 6 and all(bag & N for bag in bags)
        assert all(bags[i].isdisjoint(bags[j]) for i, j in itertools.combinations(range(6), 2))
        assert all(connected(bag, edges) for bag in bags)
        assert all(adjacent(bags[i], bags[j], edges) for i, j in itertools.combinations(range(6), 2))
        support_masks.append(support_mask)

    # A larger support containing a smaller support is redundant for coverage.
    support_masks = list(set(support_masks))
    support_masks = [
        mask for mask in support_masks
        if not any(other != mask and other & ~mask == 0 for other in support_masks)
    ]

    count = 0
    for rows in row_systems(name, fedges):
        for aw in (False, True):
            if not valid(rows, aw, fedges):
                continue
            count += 1
            assignment = truth_mask(rows, aw)
            assert any(assignment & support == support for support in support_masks), (name, rows, aw)
    grand_total += count
    print(f"{name}: verified {count} canonical cut-free attachment systems")

print(f"verified all six order-four shore types ({grand_total} canonical systems)")
