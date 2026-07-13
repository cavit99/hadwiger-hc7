#!/usr/bin/env python3
"""Exact CEGIS search for an order-five full shore versus one full helper.

The setting is the pure-Moser reserved-connector residual.  The selected
shore D has five vertices and terminal a=1.  Its arbitrary opposite shore is
contracted to one helper complete to S union {b}.  For each of the 21
connected unlabelled graphs F on five vertices, Z3 ranges over *all* boundary
attachment rows satisfying:

* minimum degree seven at every shore vertex;
* full attachment to L=S union {a};
* minimum degree seven at a; and
* every local shore-subset consequence of kappa(G)>=7.

Every found N-meeting K6 model is reduced to a monotone support and excluded.
Thus UNSAT means that the finite family of archived supports covers every
admissible attachment system.  This is a discovery program; the archive is
replayed independently by portal_k5k1_verify.py.
"""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import dataclass

import z3


N = tuple(range(7))
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


def mask_edges(mask: int) -> set[tuple[int, int]]:
    return {edge for i, edge in enumerate(PAIRS) if mask >> i & 1}


def edge_mask(edges) -> int:
    edges = {tuple(sorted(e)) for e in edges}
    return sum(1 << i for i, edge in enumerate(PAIRS) if edge in edges)


def permuted_mask(mask: int, p) -> int:
    return edge_mask(tuple(sorted((p[x], p[y]))) for x, y in mask_edges(mask))


def graph_connected(edges) -> bool:
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
    """Return deterministic canonical representatives of the 21 types."""
    perms = tuple(itertools.permutations(range(5)))
    representatives = []
    for mask in range(1 << len(PAIRS)):
        edges = mask_edges(mask)
        if not graph_connected(edges):
            continue
        if mask != min(permuted_mask(mask, p) for p in perms):
            continue
        representatives.append((mask.bit_count(), mask, edges))
    representatives.sort()
    assert len(representatives) == 21
    return {
        f"g{index:02d}_e{size}_{mask:03x}": edges
        for index, (size, mask, edges) in enumerate(representatives)
    }


TYPES = graph_types()


def automorphisms(fedges):
    canon = {tuple(sorted(e)) for e in fedges}
    return [
        p for p in itertools.permutations(range(5))
        if {tuple(sorted((p[x], p[y]))) for x, y in canon} == canon
    ]


def lex_leq(left, right):
    clauses = []
    prefix = z3.BoolVal(True)
    for x, y in zip(left, right):
        clauses.append(z3.And(prefix, x < y))
        prefix = z3.And(prefix, x == y)
    clauses.append(prefix)
    return z3.Or(*clauses)


@dataclass(frozen=True)
class Instance:
    aw: bool
    rows: tuple[int, int, int, int, int]


class AttachmentSolver:
    def __init__(self, fedges):
        self.fedges = {tuple(sorted(e)) for e in fedges}
        self.solver = z3.Solver()
        self.x = [[z3.Bool(f"x_{i}_{j}") for j in range(7)] for i in range(5)]
        self.aw = z3.Bool("aw")

        degrees = [sum(i in e for e in self.fedges) for i in range(5)]
        for i in range(5):
            self.solver.add(z3.PbGe(
                [(self.x[i][j], 1) for j in range(7)], 7 - degrees[i]
            ))

        for j in range(7):
            self.solver.add(z3.Or(*(self.x[i][j] for i in range(5))))

        # d_G(a)=4+1_aw+number of contacts from a into D.
        self.solver.add(z3.PbGe(
            [(self.aw, 1)] + [(self.x[i][6], 1) for i in range(5)], 3
        ))

        # Every nonempty proper X subset D has at least seven external
        # neighbours.  The two terms are disjoint: vertices of D-X and L.
        for mask in range(1, 31):
            outside_internal = {
                y
                for x in range(5) if mask >> x & 1
                for y in range(5) if not (mask >> y & 1)
                if tuple(sorted((x, y))) in self.fedges
            }
            union_bits = [
                z3.Or(*(self.x[i][j] for i in range(5) if mask >> i & 1))
                for j in range(7)
            ]
            self.solver.add(z3.PbGe(
                [(bit, 1) for bit in union_bits], 7 - len(outside_internal)
            ))

        rowints = [
            z3.Sum(*[z3.If(self.x[i][j], 1 << j, 0) for j in range(7)])
            for i in range(5)
        ]
        identity = tuple(range(5))
        for p in automorphisms(self.fedges):
            if p != identity:
                self.solver.add(lex_leq(rowints, [rowints[p[i]] for i in range(5)]))

    def next(self):
        if self.solver.check() != z3.sat:
            return None
        model = self.solver.model()
        rows = tuple(
            sum(1 << j for j in range(7) if z3.is_true(model.eval(self.x[i][j])))
            for i in range(5)
        )
        return Instance(z3.is_true(model.eval(self.aw)), rows)

    def exclude_support(self, support):
        literals = []
        for key in support:
            if key[0] == "aw":
                literals.append(z3.Not(self.aw))
            else:
                _, i, j = key
                literals.append(z3.Not(self.x[i][j]))
        assert literals
        self.solver.add(z3.Or(*literals))


def edge_data(fedges, instance):
    fixed = set(M)
    fixed.update(tuple(sorted((DA[i], DA[j]))) for i, j in fedges)
    fixed.update(tuple(sorted((DB, x))) for x in set(U) | {W, B})
    variable = {}
    if instance.aw:
        variable[tuple(sorted((A, W)))] = ("aw",)
    for i, row in enumerate(instance.rows):
        for j, label in enumerate(LABELS):
            if row >> j & 1:
                variable[tuple(sorted((DA[i], label)))] = ("x", i, j)
    return fixed, variable


def connected_masks(edges):
    count = 14
    adjacency = [0] * count
    for x, y in edges:
        adjacency[x] |= 1 << y
        adjacency[y] |= 1 << x
    neighbour_union = [0] * (1 << count)
    connected = []
    for mask in range(1, 1 << count):
        low = mask & -mask
        i = low.bit_length() - 1
        neighbour_union[mask] = neighbour_union[mask ^ low] | adjacency[i]
        reached = low
        while True:
            expanded = reached | (neighbour_union[reached] & mask)
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            connected.append(mask)
    return neighbour_union, connected


def find_model(fedges, instance):
    fixed, variable = edge_data(fedges, instance)
    edges = fixed | set(variable)
    neighbour_union, connected = connected_masks(edges)
    nmask = sum(1 << x for x in N)
    for omitted in N:
        roots = [x for x in N if x != omitted]
        rootmask = nmask ^ (1 << omitted)
        candidates = {
            root: [m for m in connected if m & rootmask == 1 << root]
            for root in roots
        }
        order = sorted(roots, key=lambda root: len(candidates[root]))

        def rec(k, bags, used):
            if k == 6:
                return bags
            for bag in candidates[order[k]]:
                if bag & used:
                    continue
                if all(neighbour_union[bag] & old for old in bags):
                    result = rec(k + 1, bags + [bag], used | bag)
                    if result is not None:
                        return result
            return None

        bags = rec(0, [], 0)
        if bags is not None:
            return bags, support_for_model(bags, fixed, variable)
    return None


def support_for_model(bags, fixed, variable):
    """Keep fixed-first spanning trees and one witness edge per bag pair."""
    support = set()

    def add_if_variable(edge):
        edge = tuple(sorted(edge))
        if edge in variable:
            support.add(variable[edge])

    all_edges = fixed | set(variable)
    for mask in bags:
        vertices = [v for v in range(14) if mask >> v & 1]
        parent = {v: v for v in vertices}

        def root(v):
            while parent[v] != v:
                parent[v] = parent[parent[v]]
                v = parent[v]
            return v

        for variable_pass in (False, True):
            for edge in sorted(all_edges):
                x, y = edge
                if x not in parent or y not in parent:
                    continue
                if (edge in variable) != variable_pass:
                    continue
                rx, ry = root(x), root(y)
                if rx != ry:
                    parent[rx] = ry
                    add_if_variable(edge)

    for i, j in itertools.combinations(range(6), 2):
        left = [v for v in range(14) if bags[i] >> v & 1]
        right = [v for v in range(14) if bags[j] >> v & 1]
        crossing = [
            tuple(sorted((x, y))) for x in left for y in right
            if tuple(sorted((x, y))) in all_edges
        ]
        fixed_crossing = [edge for edge in crossing if edge in fixed]
        chosen = min(fixed_crossing) if fixed_crossing else min(crossing)
        add_if_variable(chosen)
    assert support
    return support


def bags_as_lists(bags):
    return [[v for v in range(14) if mask >> v & 1] for mask in bags]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("types", nargs="*", choices=tuple(TYPES), default=tuple(TYPES))
    parser.add_argument("--limit", type=int, default=100000)
    parser.add_argument("--output", default="portal_k5k1_cegis_result.json")
    args = parser.parse_args()

    archive = {"format": 1, "type_order": list(TYPES), "types": {}}
    for name in args.types:
        fedges = TYPES[name]
        solver = AttachmentSolver(fedges)
        supports = []
        survivor = None
        for iteration in range(args.limit):
            instance = solver.next()
            if instance is None:
                print(name, "closed after", iteration, "model supports", flush=True)
                break
            found = find_model(fedges, instance)
            if found is None:
                survivor = {"aw": instance.aw, "rows": list(instance.rows)}
                print(name, "SURVIVOR", survivor, "after", iteration, flush=True)
                break
            bags, support = found
            supports.append({
                "required": [list(key) for key in sorted(support)],
                "bags": bags_as_lists(bags),
            })
            solver.exclude_support(support)
            if iteration % 100 == 0:
                print(name, "iteration", iteration, "support", len(support), flush=True)
        archive["types"][name] = {
            "internal_edges": [list(e) for e in sorted(fedges)],
            "supports": supports,
            "survivor": survivor,
        }
        with open(args.output, "w", encoding="utf-8") as out:
            json.dump(archive, out, indent=2)


if __name__ == "__main__":
    main()
