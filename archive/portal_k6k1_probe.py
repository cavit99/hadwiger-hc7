#!/usr/bin/env python3
"""Exploratory exact CEGIS for a six-vertex distinguished shore.

This is the order-six analogue of portal_k5k1_cegis.py.  It is intentionally
kept as a probe until every one of the 112 connected internal types closes and
an independent certificate is exported.
"""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import dataclass

import networkx as nx
import z3

from portal_k5k1_cegis import A, B, LABELS, M, N, U, W, lex_leq


ORDER = 6
DA = tuple(range(8, 8 + ORDER))
DB = 8 + ORDER
TOTAL = DB + 1


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
    canon = {tuple(sorted(e)) for e in fedges}
    return [
        p for p in itertools.permutations(range(ORDER))
        if {tuple(sorted((p[x], p[y]))) for x, y in canon} == canon
    ]


@dataclass(frozen=True)
class Instance:
    aw: bool
    rows: tuple[int, ...]


class AttachmentSolver:
    def __init__(self, fedges, blocked_only=False):
        self.fedges = {tuple(sorted(e)) for e in fedges}
        self.solver = z3.Solver()
        self.x = [[z3.Bool(f"x_{i}_{j}") for j in range(7)] for i in range(ORDER)]
        self.aw = z3.Bool("aw")
        degrees = [sum(i in e for e in self.fedges) for i in range(ORDER)]
        for i in range(ORDER):
            self.solver.add(z3.PbGe(
                [(self.x[i][j], 1) for j in range(7)], 7 - degrees[i]
            ))
        for j in range(7):
            self.solver.add(z3.Or(*(self.x[i][j] for i in range(ORDER))))
        self.solver.add(z3.PbGe(
            [(self.aw, 1)] + [(self.x[i][6], 1) for i in range(ORDER)], 3
        ))
        for subset in range(1, (1 << ORDER) - 1):
            outside = {
                y
                for x in range(ORDER) if subset >> x & 1
                for y in range(ORDER) if not (subset >> y & 1)
                if tuple(sorted((x, y))) in self.fedges
            }
            unions = [
                z3.Or(*(self.x[i][j] for i in range(ORDER) if subset >> i & 1))
                for j in range(7)
            ]
            self.solver.add(z3.PbGe(
                [(term, 1) for term in unions], 7 - len(outside)
            ))
        rowints = [
            z3.Sum(*[z3.If(self.x[i][j], 1 << j, 0) for j in range(7)])
            for i in range(ORDER)
        ]
        identity = tuple(range(ORDER))
        for p in automorphisms(self.fedges):
            if p != identity:
                self.solver.add(lex_leq(rowints, [rowints[p[i]] for i in range(ORDER)]))
        if blocked_only:
            for edge in self.fedges:
                self.solver.add(z3.Not(safe_contraction(self.x, self.aw, self.fedges, edge)))

    def next(self):
        if self.solver.check() != z3.sat:
            return None
        model = self.solver.model()
        return Instance(
            z3.is_true(model.eval(self.aw)),
            tuple(
                sum(1 << j for j in range(7) if z3.is_true(model.eval(self.x[i][j])))
                for i in range(ORDER)
            ),
        )

    def exclude_support(self, support):
        literals = []
        for key in support:
            if key[0] == "aw":
                literals.append(z3.Not(self.aw))
            else:
                literals.append(z3.Not(self.x[key[1]][key[2]]))
        assert literals
        self.solver.add(z3.Or(*literals))


def safe_contraction(x, aw, fedges, edge):
    """Whether contracting ``edge`` preserves every order-five hypothesis."""
    groups = [tuple(edge)] + [(i,) for i in range(ORDER) if i not in edge]
    assert len(groups) == 5
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
    adjacency = [0] * TOTAL
    for x, y in edges:
        adjacency[x] |= 1 << y
        adjacency[y] |= 1 << x
    neighbour_union = [0] * (1 << TOTAL)
    connected = []
    for mask in range(1, 1 << TOTAL):
        low = mask & -mask
        neighbour_union[mask] = neighbour_union[mask ^ low] | adjacency[low.bit_length() - 1]
        reached = low
        while True:
            expanded = reached | (neighbour_union[reached] & mask)
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            connected.append(mask)
    return neighbour_union, connected


def support_for_model(bags, fixed, variable):
    support = set()
    all_edges = fixed | set(variable)

    def add(edge):
        edge = tuple(sorted(edge))
        if edge in variable:
            support.add(variable[edge])

    for bag in bags:
        vertices = [v for v in range(TOTAL) if bag >> v & 1]
        parent = {v: v for v in vertices}

        def root(v):
            while parent[v] != v:
                parent[v] = parent[parent[v]]
                v = parent[v]
            return v

        for variable_pass in (False, True):
            for edge in sorted(all_edges):
                x, y = edge
                if x not in parent or y not in parent or (edge in variable) != variable_pass:
                    continue
                rx, ry = root(x), root(y)
                if rx != ry:
                    parent[rx] = ry
                    add(edge)
    for i, j in itertools.combinations(range(6), 2):
        left = [v for v in range(TOTAL) if bags[i] >> v & 1]
        right = [v for v in range(TOTAL) if bags[j] >> v & 1]
        crossing = [
            tuple(sorted((x, y))) for x in left for y in right
            if tuple(sorted((x, y))) in all_edges
        ]
        fixed_crossing = [edge for edge in crossing if edge in fixed]
        add(min(fixed_crossing) if fixed_crossing else min(crossing))
    assert support
    return support


def find_model(fedges, instance):
    fixed, variable = edge_data(fedges, instance)
    edges = fixed | set(variable)
    neighbours, connected = connected_masks(edges)
    nmask = sum(1 << x for x in N)
    for omitted in N:
        roots = [x for x in N if x != omitted]
        rootmask = nmask ^ (1 << omitted)
        candidates = {
            root: [mask for mask in connected if mask & rootmask == 1 << root]
            for root in roots
        }
        order = sorted(roots, key=lambda root: len(candidates[root]))

        def rec(k, bags, used):
            if k == 6:
                return bags
            for bag in candidates[order[k]]:
                if bag & used or any(not (neighbours[bag] & old) for old in bags):
                    continue
                found = rec(k + 1, bags + [bag], used | bag)
                if found is not None:
                    return found
            return None

        bags = rec(0, [], 0)
        if bags is not None:
            return bags, support_for_model(bags, fixed, variable)
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("types", nargs="*", choices=tuple(TYPES), default=tuple(TYPES))
    parser.add_argument("--limit", type=int, default=100000)
    parser.add_argument("--output", default="portal_k6k1_probe_result.json")
    parser.add_argument("--blocked-only", action="store_true")
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--end", type=int, default=len(TYPES))
    args = parser.parse_args()
    selected = list(args.types) if args.types else list(TYPES)
    selected = selected[args.start:args.end]
    archive = {
        "format": 0,
        "blocked_only": args.blocked_only,
        "type_order": list(TYPES),
        "types": {},
    }
    for name in selected:
        solver = AttachmentSolver(TYPES[name], blocked_only=args.blocked_only)
        supports = []
        survivor = None
        for iteration in range(args.limit):
            instance = solver.next()
            if instance is None:
                print(name, "closed", iteration, flush=True)
                break
            found = find_model(TYPES[name], instance)
            if found is None:
                survivor = {"aw": instance.aw, "rows": list(instance.rows)}
                print(name, "SURVIVOR", survivor, flush=True)
                break
            bags, support = found
            supports.append({
                "required": [list(key) for key in sorted(support)],
                "bags": [[v for v in range(TOTAL) if bag >> v & 1] for bag in bags],
            })
            solver.exclude_support(support)
            if iteration % 100 == 0:
                print(name, iteration, len(support), flush=True)
        archive["types"][name] = {
            "internal_edges": [list(edge) for edge in sorted(TYPES[name])],
            "supports": supports,
            "survivor": survivor,
        }
        with open(args.output, "w", encoding="utf-8") as target:
            json.dump(archive, target, indent=2)


if __name__ == "__main__":
    main()
