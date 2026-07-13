#!/usr/bin/env python3
"""Independent exact replay of the order-five-shore certificate.

This verifier does not import the discovery program and does not invoke a
graph-minor oracle.  It independently regenerates the 21 connected
unlabelled five-vertex shore types, checks every archived six-bag model from
its listed edges, and proves coverage with a fresh Boolean formula.

Coverage is checked over *all labelled* attachment systems.  For every
verified support the verifier adds all images under automorphisms of the
internal shore.  Therefore this replay does not rely on the lex-leader
constraints used during discovery.  The only solver task is a transparent
36-variable UNSAT check for the degree, full-attachment, terminal-degree,
local seven-cut, and support-avoidance clauses.
"""

from __future__ import annotations

import itertools
import json

import z3


N = set(range(7))
U = (0, 2, 4, 5, 6)
A, B, W = 1, 3, 7
DA = (8, 9, 10, 11, 12)
DB = 13
LABELS = U + (W, A)
M = {
    tuple(sorted(e))
    for e in (
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 6), (2, 6),
        (3, 4), (3, 5), (4, 5), (5, 6),
    )
}
PAIRS = tuple(itertools.combinations(range(5), 2))


def mask_edges(mask):
    return {edge for i, edge in enumerate(PAIRS) if mask >> i & 1}


def edge_mask(edges):
    edges = {tuple(sorted(e)) for e in edges}
    return sum(1 << i for i, edge in enumerate(PAIRS) if edge in edges)


def permuted_graph_mask(mask, p):
    return edge_mask(tuple(sorted((p[x], p[y]))) for x, y in mask_edges(mask))


def graph_connected(edges):
    reached = {0}
    while True:
        expanded = reached | {
            y for x in reached for y in range(5)
            if tuple(sorted((x, y))) in edges
        }
        if expanded == reached:
            return len(reached) == 5
        reached = expanded


def graph_types():
    perms = tuple(itertools.permutations(range(5)))
    result = []
    for mask in range(1 << len(PAIRS)):
        edges = mask_edges(mask)
        if not graph_connected(edges):
            continue
        if mask != min(permuted_graph_mask(mask, p) for p in perms):
            continue
        result.append((mask.bit_count(), mask, edges))
    result.sort()
    assert len(result) == 21
    return {
        f"g{index:02d}_e{size}_{mask:03x}": edges
        for index, (size, mask, edges) in enumerate(result)
    }


TYPES = graph_types()


def automorphisms(fedges):
    canon = {tuple(sorted(e)) for e in fedges}
    return [
        p for p in itertools.permutations(range(5))
        if {tuple(sorted((p[x], p[y]))) for x, y in canon} == canon
    ]


def fixed_edges(fedges):
    edges = set(M)
    edges.update(tuple(sorted((DA[i], DA[j]))) for i, j in fedges)
    edges.update(tuple(sorted((DB, x))) for x in set(U) | {W, B})
    return edges


def parse_required(required):
    edges = set()
    mask = 0
    seen = set()
    for key in required:
        key = tuple(key)
        assert key not in seen
        seen.add(key)
        if key[0] == "aw":
            assert key == ("aw",)
            edges.add(tuple(sorted((A, W))))
            mask |= 1 << 35
        else:
            assert key[0] == "x" and len(key) == 3
            i, j = key[1], key[2]
            assert 0 <= i < 5 and 0 <= j < 7
            edges.add(tuple(sorted((DA[i], LABELS[j]))))
            mask |= 1 << (7 * i + j)
    assert mask
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


def transform_support(mask, p):
    image = mask & (1 << 35)
    for i in range(5):
        for j in range(7):
            if mask >> (7 * i + j) & 1:
                image |= 1 << (7 * p[i] + j)
    return image


def minimal_masks(masks):
    result = []
    for mask in sorted(set(masks), key=lambda value: (value.bit_count(), value)):
        if not any(old & ~mask == 0 for old in result):
            result.append(mask)
    return result


def add_base_constraints(solver, x, aw, fedges):
    degrees = [sum(i in e for e in fedges) for i in range(5)]
    for i in range(5):
        solver.add(z3.PbGe([(x[i][j], 1) for j in range(7)], 7 - degrees[i]))
    for j in range(7):
        solver.add(z3.Or(*(x[i][j] for i in range(5))))
    solver.add(z3.PbGe([(aw, 1)] + [(x[i][6], 1) for i in range(5)], 3))
    for subset in range(1, 31):
        outside_internal = {
            y
            for i in range(5) if subset >> i & 1
            for y in range(5) if not (subset >> y & 1)
            if tuple(sorted((i, y))) in fedges
        }
        unions = [
            z3.Or(*(x[i][j] for i in range(5) if subset >> i & 1))
            for j in range(7)
        ]
        solver.add(z3.PbGe([(term, 1) for term in unions], 7 - len(outside_internal)))


def avoidance_clause(mask, x, aw):
    literals = []
    if mask >> 35 & 1:
        literals.append(z3.Not(aw))
    for i in range(5):
        for j in range(7):
            if mask >> (7 * i + j) & 1:
                literals.append(z3.Not(x[i][j]))
    assert literals
    return z3.Or(*literals)


with open("portal_k5k1_cegis_result.json", encoding="utf-8") as source:
    archive = json.load(source)

assert archive["format"] == 1
assert archive["type_order"] == list(TYPES)
assert set(archive["types"]) == set(TYPES)

grand_records = 0
grand_clauses = 0
for name, fedges in TYPES.items():
    section = archive["types"][name]
    assert {tuple(edge) for edge in section["internal_edges"]} == fedges
    assert section["survivor"] is None
    fixed = fixed_edges(fedges)
    supports = []
    for record in section["supports"]:
        extra, support = parse_required(record["required"])
        edges = fixed | extra
        bags = [set(bag) for bag in record["bags"]]
        assert len(bags) == 6
        assert all(bag and bag & N for bag in bags)
        assert all(max(bag) < 14 and min(bag) >= 0 for bag in bags)
        assert all(
            bags[i].isdisjoint(bags[j])
            for i, j in itertools.combinations(range(6), 2)
        )
        assert all(connected(bag, edges) for bag in bags)
        assert all(
            adjacent(bags[i], bags[j], edges)
            for i, j in itertools.combinations(range(6), 2)
        )
        supports.append(support)

    autos = automorphisms(fedges)
    orbit_masks = minimal_masks(
        transform_support(mask, p) for mask in supports for p in autos
    )

    solver = z3.Solver()
    x = [[z3.Bool(f"{name}_x_{i}_{j}") for j in range(7)] for i in range(5)]
    aw = z3.Bool(f"{name}_aw")
    add_base_constraints(solver, x, aw, fedges)
    solver.add(*(avoidance_clause(mask, x, aw) for mask in orbit_masks))
    assert solver.check() == z3.unsat, name

    grand_records += len(supports)
    grand_clauses += len(orbit_masks)
    print(
        f"{name}: verified {len(supports)} models; "
        f"all labelled states covered by {len(orbit_masks)} orbit clauses"
    )

print(
    f"verified all 21 order-five shore types: {grand_records} models, "
    f"{grand_clauses} irredundant labelled support clauses"
)
