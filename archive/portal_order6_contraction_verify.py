#!/usr/bin/env python3
"""Independent replay of the order-six contraction census and partial closure.

The verifier does not import either discovery program.  It regenerates the
112 connected six-vertex types, rechecks the 47/65 safe-contraction census,
validates every archived branch-set model, expands supports by the full
internal automorphism group, and proves exact all-labelled coverage for every
completed blocked-cell section.
"""

from __future__ import annotations

import glob
import itertools
import json

import networkx as nx
import z3


ORDER = 6
N = set(range(7))
U = (0, 2, 4, 5, 6)
A, B, W = 1, 3, 7
DA = tuple(range(8, 14))
DB = 14
TOTAL = 15
LABELS = U + (W, A)
M = {
    tuple(sorted(e))
    for e in (
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 6), (2, 6),
        (3, 4), (3, 5), (4, 5), (5, 6),
    )
}


def graph_types():
    records = []
    for graph in nx.graph_atlas_g():
        if len(graph) != ORDER or not nx.is_connected(graph):
            continue
        edges = {tuple(sorted(edge)) for edge in graph.edges()}
        code = nx.to_graph6_bytes(graph, header=False).decode().strip()
        records.append((len(edges), code, edges))
    records.sort(key=lambda item: (item[0], item[1]))
    assert len(records) == 112
    return {
        f"g{index:03d}_e{size}_{code}": edges
        for index, (size, code, edges) in enumerate(records)
    }


TYPES = graph_types()


def automorphisms(fedges):
    canon = {tuple(sorted(edge)) for edge in fedges}
    return [
        p for p in itertools.permutations(range(ORDER))
        if {tuple(sorted((p[x], p[y]))) for x, y in canon} == canon
    ]


def base_constraints(solver, x, aw, fedges):
    degrees = [sum(i in edge for edge in fedges) for i in range(ORDER)]
    for i in range(ORDER):
        solver.add(z3.PbGe([(x[i][j], 1) for j in range(7)], 7 - degrees[i]))
    for j in range(7):
        solver.add(z3.Or(*(x[i][j] for i in range(ORDER))))
    solver.add(z3.PbGe([(aw, 1)] + [(x[i][6], 1) for i in range(ORDER)], 3))
    for subset in range(1, 63):
        outside = {
            y
            for i in range(ORDER) if subset >> i & 1
            for y in range(ORDER) if not (subset >> y & 1)
            if tuple(sorted((i, y))) in fedges
        }
        unions = [
            z3.Or(*(x[i][j] for i in range(ORDER) if subset >> i & 1))
            for j in range(7)
        ]
        solver.add(z3.PbGe([(term, 1) for term in unions], 7 - len(outside)))


def safe_contraction(x, aw, fedges, edge):
    groups = [tuple(edge)] + [(i,) for i in range(ORDER) if i not in edge]
    rows = [
        [z3.Or(*(x[i][j] for i in group)) for j in range(7)]
        for group in groups
    ]
    internal = {
        (p, q)
        for p in range(5) for q in range(p + 1, 5)
        if any(tuple(sorted((i, j))) in fedges for i in groups[p] for j in groups[q])
    }
    conditions = [z3.PbGe([(aw, 1)] + [(rows[i][6], 1) for i in range(5)], 3)]
    for subset in range(1, 31):
        outside = {
            q
            for p in range(5) if subset >> p & 1
            for q in range(5) if not (subset >> q & 1)
            if tuple(sorted((p, q))) in internal
        }
        unions = [
            z3.Or(*(rows[i][j] for i in range(5) if subset >> i & 1))
            for j in range(7)
        ]
        conditions.append(z3.PbGe(
            [(term, 1) for term in unions], 7 - len(outside)
        ))
    return z3.And(*conditions)


def blocked_solver(name, fedges):
    solver = z3.Solver()
    x = [[z3.Bool(f"{name}_x_{i}_{j}") for j in range(7)] for i in range(ORDER)]
    aw = z3.Bool(f"{name}_aw")
    base_constraints(solver, x, aw, fedges)
    solver.add(*(z3.Not(safe_contraction(x, aw, fedges, edge)) for edge in fedges))
    return solver, x, aw


def fixed_edges(fedges):
    edges = set(M)
    edges.update(tuple(sorted((DA[i], DA[j]))) for i, j in fedges)
    edges.update(tuple(sorted((DB, x))) for x in set(U) | {W, B})
    return edges


def parse_required(required):
    edges = set()
    mask = 0
    seen = set()
    for item in required:
        key = tuple(item)
        assert key not in seen
        seen.add(key)
        if key[0] == "aw":
            assert key == ("aw",)
            edges.add(tuple(sorted((A, W))))
            mask |= 1 << 42
        else:
            assert key[0] == "x" and len(key) == 3
            i, j = key[1], key[2]
            assert 0 <= i < ORDER and 0 <= j < 7
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
    image = mask & (1 << 42)
    for i in range(ORDER):
        for j in range(7):
            if mask >> (7 * i + j) & 1:
                image |= 1 << (7 * p[i] + j)
    return image


def avoidance(mask, x, aw):
    literals = [z3.Not(aw)] if mask >> 42 & 1 else []
    literals.extend(
        z3.Not(x[i][j])
        for i in range(ORDER) for j in range(7)
        if mask >> (7 * i + j) & 1
    )
    assert literals
    return z3.Or(*literals)


# Independently replay the global 47/65 contraction census.  SAT records also
# carry a concrete assignment; pinning it prevents an accidental status-only
# archive from passing.
with open("portal_order6_contraction_obstruction.json", encoding="utf-8") as source:
    census = json.load(source)
assert census["format"] == 1
assert [record["type"] for record in census["records"]] == list(TYPES)
status_count = {"unsat": 0, "sat": 0}
for record in census["records"]:
    name = record["type"]
    solver, x, aw = blocked_solver(name, TYPES[name])
    if record["status"] == "unsat":
        assert solver.check() == z3.unsat
        status_count["unsat"] += 1
    else:
        assert record["status"] == "sat"
        rows = record["rows"]
        assert len(rows) == ORDER and all(0 <= row < 128 for row in rows)
        solver.add(aw == record["aw"])
        solver.add(*(
            x[i][j] == bool(rows[i] >> j & 1)
            for i in range(ORDER) for j in range(7)
        ))
        assert solver.check() == z3.sat
        status_count["sat"] += 1
assert status_count == {"unsat": 47, "sat": 65}
print("verified order-six contraction census: 47 automatic, 65 blocked")


# Independently replay every completed direct blocked-cell section.
seen_types = set()
direct_types = set()
model_total = 0
for path in sorted(glob.glob("portal_k6k1_blocked_*.json")):
    with open(path, encoding="utf-8") as source:
        archive = json.load(source)
    assert archive["format"] == 0 and archive["blocked_only"] is True
    assert archive["type_order"] == list(TYPES)
    for name, section in archive["types"].items():
        assert name in TYPES and name not in seen_types
        seen_types.add(name)
        fedges = TYPES[name]
        assert {tuple(edge) for edge in section["internal_edges"]} == fedges
        assert section["survivor"] is None
        fixed = fixed_edges(fedges)
        supports = []
        for record in section["supports"]:
            extra, support = parse_required(record["required"])
            edges = fixed | extra
            bags = [set(bag) for bag in record["bags"]]
            assert len(bags) == 6 and all(bag and bag & N for bag in bags)
            assert all(min(bag) >= 0 and max(bag) < TOTAL for bag in bags)
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

        solver, x, aw = blocked_solver("cover_" + name, fedges)
        orbit_masks = {
            transform_support(mask, p)
            for mask in supports for p in automorphisms(fedges)
        }
        solver.add(*(avoidance(mask, x, aw) for mask in orbit_masks))
        assert solver.check() == z3.unsat, name
        if supports:
            direct_types.add(name)
            model_total += len(supports)
            print(name, "verified", len(supports), "blocked-cell models")

assert len(direct_types) == 20
assert model_total == 8916
print(
    "verified partial order-six closure: 47 safe-contraction types +",
    len(direct_types), "direct types =", 47 + len(direct_types), "of 112",
)
