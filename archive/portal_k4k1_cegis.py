#!/usr/bin/env python3
"""CEGIS search for an order-four full shore against a contracted opposite shore.

For each of the six connected graphs on four vertices, this script searches the
attachment rows allowed by minimum degree, full seven-attachment, the terminal
degree inequality, and every local consequence of seven-connectivity.  A found
N-meeting K6 model is converted into a monotone support clause; Z3 then asks for
an attachment system avoiding all models seen so far.

The script is a discovery aid.  Any closed cell must subsequently be exported
to a finite, solver-free certificate/replay.
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
    result = []
    canon = {tuple(sorted(e)) for e in fedges}
    for p in itertools.permutations(range(4)):
        image = {tuple(sorted((p[x], p[y]))) for x, y in canon}
        if image == canon:
            result.append(p)
    return result


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
    rows: tuple[int, int, int, int]


class AttachmentSolver:
    def __init__(self, fedges):
        self.fedges = {tuple(sorted(e)) for e in fedges}
        self.solver = z3.Solver()
        self.x = [[z3.Bool(f"x_{i}_{j}") for j in range(7)] for i in range(4)]
        self.aw = z3.Bool("aw")

        degrees = [sum(i in e for e in self.fedges) for i in range(4)]
        for i in range(4):
            self.solver.add(z3.PbGe([(self.x[i][j], 1) for j in range(7)], 7 - degrees[i]))

        # Every one of S union {a} is hit by the shore.
        for j in range(7):
            self.solver.add(z3.Or(*(self.x[i][j] for i in range(4))))

        # d_G(a) = 4 + 1_aw + number of shore contacts.
        self.solver.add(z3.PbGe(
            [(self.aw, 1)] + [(self.x[i][6], 1) for i in range(4)], 3
        ))

        # If a nonempty proper X subset D had at most six external
        # neighbours, that neighbourhood would be a forbidden cut in G.
        for mask in range(1, 15):
            outside_internal = {
                y
                for x in range(4) if mask >> x & 1
                for y in range(4) if not (mask >> y & 1)
                if tuple(sorted((x, y))) in self.fedges
            }
            union_bits = [z3.Or(*(self.x[i][j] for i in range(4) if mask >> i & 1)) for j in range(7)]
            self.solver.add(z3.PbGe(
                [(bit, 1) for bit in union_bits], 7 - len(outside_internal)
            ))

        # One lexicographically least representative per automorphism orbit.
        rowints = [z3.Sum(*[z3.If(self.x[i][j], 1 << j, 0) for j in range(7)]) for i in range(4)]
        for p in automorphisms(self.fedges):
            if p != tuple(range(4)):
                self.solver.add(lex_leq(rowints, [rowints[p[i]] for i in range(4)]))

    def next(self):
        if self.solver.check() != z3.sat:
            return None
        model = self.solver.model()
        rows = tuple(sum((1 << j) for j in range(7) if z3.is_true(model.eval(self.x[i][j]))) for i in range(4))
        return Instance(z3.is_true(model.eval(self.aw)), rows)

    def exclude_support(self, support):
        literals = []
        for key in support:
            if key[0] == "aw":
                literals.append(z3.Not(self.aw))
            else:
                _, i, j = key
                literals.append(z3.Not(self.x[i][j]))
        self.solver.add(z3.Or(*literals))

    def exclude_exact(self, instance):
        terms = [self.aw != instance.aw]
        for i, row in enumerate(instance.rows):
            terms.extend(self.x[i][j] != bool(row >> j & 1) for j in range(7))
        self.solver.add(z3.Or(*terms))


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
    count = 13
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
    """Select fixed-first spanning trees and one edge per bag pair."""
    support = set()

    def add_if_variable(edge):
        edge = tuple(sorted(edge))
        if edge in variable:
            support.add(variable[edge])

    all_edges = fixed | set(variable)
    for mask in bags:
        vertices = [v for v in range(13) if mask >> v & 1]
        parent = {v: v for v in vertices}

        def root(v):
            while parent[v] != v:
                parent[v] = parent[parent[v]]
                v = parent[v]
            return v

        for variable_pass in (False, True):
            for edge in all_edges:
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
        left = [v for v in range(13) if bags[i] >> v & 1]
        right = [v for v in range(13) if bags[j] >> v & 1]
        crossing = [tuple(sorted((x, y))) for x in left for y in right if tuple(sorted((x, y))) in all_edges]
        fixed_crossing = [e for e in crossing if e in fixed]
        chosen = fixed_crossing[0] if fixed_crossing else crossing[0]
        add_if_variable(chosen)
    return support


def bags_as_lists(bags):
    return [[v for v in range(13) if mask >> v & 1] for mask in bags]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("types", nargs="*", choices=tuple(TYPES), default=tuple(TYPES))
    parser.add_argument("--limit", type=int, default=100000)
    parser.add_argument("--output", default="portal_k4k1_cegis_result.json")
    args = parser.parse_args()

    archive = {"format": 1, "types": {}}
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
                survivor = {"aw": instance.aw, "rows": instance.rows}
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
