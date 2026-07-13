#!/usr/bin/env python3
"""CEGIS probe for the singleton-shore C5 contact core.

Vertices 0,...,4 induce the boundary cycle.  The remaining vertices form
one connected exterior, meet every boundary vertex, and the whole graph is
4-connected (the consequence of deleting the three clique vertices
v,r1,r2 from a 7-connected contact-core realization).

For a missing cycle chord ab, a usable rooted K4 model has exact boundary
traces ab | c | d | e.  Such a model, together with v,r1,r2, is a K7
model in the original graph.  This script searches for small graphs that
avoid all five traces.  It is a falsification probe, not a proof.
"""

from __future__ import annotations

import itertools
import sys

import z3


ROOTS = tuple(range(5))
CYCLE = {tuple(sorted((i, (i + 1) % 5))) for i in ROOTS}
CHORDS = tuple(
    tuple(sorted((i, (i + 2) % 5))) for i in ROOTS
)


def cuts(vertices, size):
    return itertools.combinations(vertices, size)


class Probe:
    def __init__(self, n: int):
        self.n = n
        self.V = tuple(range(n))
        self.I = tuple(range(5, n))
        self.pairs = tuple(itertools.combinations(self.V, 2))
        self.var = {e: z3.Bool(f"e_{e[0]}_{e[1]}") for e in self.pairs}
        self.solver = z3.Solver()

        for e in itertools.combinations(ROOTS, 2):
            self.solver.add(self.edge(*e) == (e in CYCLE))

        # The exterior is nonempty and collectively touches every root.
        assert self.I
        for r in ROOTS:
            self.solver.add(z3.Or(*[self.edge(r, x) for x in self.I]))

        # It is safe to impose exterior connectedness directly.
        self.solver.add(self.connected_formula(self.I))

        # In the original contact core an exterior vertex can lose only
        # r1,r2 when we pass to this graph (it is not adjacent to v).
        # Thus delta(G)>=7 gives degree at least five here.
        for x in self.I:
            self.solver.add(z3.Sum(*[
                z3.If(self.edge(x, y), 1, 0) for y in self.V if y != x
            ]) >= 5)

    def edge(self, x, y):
        return self.var[tuple(sorted((x, y)))]

    def connected_formula(self, block):
        block = tuple(sorted(block))
        if len(block) <= 1:
            return z3.BoolVal(True)
        first = block[0]
        rest = block[1:]
        clauses = []
        for mask in range(1 << len(rest)):
            left = {first}
            left.update(rest[i] for i in range(len(rest)) if mask >> i & 1)
            if len(left) == len(block):
                continue
            right = set(block) - left
            clauses.append(z3.Or(*[self.edge(x, y) for x in left for y in right]))
        return z3.And(*clauses)

    def model_formula(self, bags):
        clauses = [self.connected_formula(bag) for bag in bags]
        for i in range(4):
            for j in range(i):
                clauses.append(z3.Or(*[
                    self.edge(x, y) for x in bags[i] for y in bags[j]
                ]))
        return z3.And(*clauses)

    def edge_set(self, model):
        return {e for e in self.pairs if z3.is_true(model.eval(self.var[e]))}

    def components_after(self, edges, deleted):
        rem = set(self.V) - set(deleted)
        if not rem:
            return []
        adj = {v: set() for v in rem}
        for x, y in edges:
            if x in rem and y in rem:
                adj[x].add(y)
                adj[y].add(x)
        comps = []
        while rem:
            seed = next(iter(rem))
            seen = {seed}
            stack = [seed]
            while stack:
                x = stack.pop()
                for y in adj[x] - seen:
                    seen.add(y)
                    stack.append(y)
            comps.append(seen)
            rem -= seen
        return comps

    def bad_four_connectivity_cut(self, edges):
        for k in range(4):
            for cut in cuts(self.V, k):
                comps = self.components_after(edges, cut)
                if len(comps) > 1:
                    return cut, comps[0], set().union(*comps[1:])
        return None

    def connected_masks(self, edges):
        adj = [0] * self.n
        for x, y in edges:
            adj[x] |= 1 << y
            adj[y] |= 1 << x
        out = []
        for mask in range(1, 1 << self.n):
            low = mask & -mask
            reached = low
            while True:
                expand = reached
                bits = reached
                while bits:
                    b = bits & -bits
                    bits ^= b
                    expand |= adj[b.bit_length() - 1] & mask
                if expand == reached:
                    break
                reached = expand
            if reached == mask:
                out.append(mask)
        return out, adj

    def rooted_model(self, edges):
        connected, adj = self.connected_masks(edges)

        def adjacent(a, b):
            bits = a
            neighbours = 0
            while bits:
                low = bits & -bits
                bits ^= low
                neighbours |= adj[low.bit_length() - 1]
            return bool(neighbours & b)

        root_mask = (1 << 5) - 1
        for a, b in CHORDS:
            others = tuple(r for r in ROOTS if r not in (a, b))
            traces = (1 << a | 1 << b,) + tuple(1 << r for r in others)
            candidates = [
                [m for m in connected if m & root_mask == trace]
                for trace in traces
            ]

            def rec(i, chosen, used):
                if i == 4:
                    return tuple(chosen)
                for m in candidates[i]:
                    if m & used:
                        continue
                    if all(adjacent(m, q) for q in chosen):
                        ans = rec(i + 1, chosen + [m], used | m)
                        if ans:
                            return ans
                return None

            answer = rec(0, [], 0)
            if answer:
                return answer
        return None

    def run(self, limit=20000):
        cuts_added = models_forbidden = 0
        for iteration in range(limit):
            verdict = self.solver.check()
            if verdict != z3.sat:
                print("UNSAT", self.n, iteration, cuts_added, models_forbidden)
                return None
            model = self.solver.model()
            edges = self.edge_set(model)
            bad = self.bad_four_connectivity_cut(edges)
            if bad:
                _cut, left, right = bad
                self.solver.add(z3.Or(*[
                    self.edge(x, y) for x in left for y in right
                ]))
                cuts_added += 1
                continue
            rooted = self.rooted_model(edges)
            if rooted is None:
                print("FOUND", self.n, "iteration", iteration,
                      "cuts", cuts_added, "models", models_forbidden)
                print(sorted(edges))
                return edges
            bags = [tuple(i for i in self.V if mask >> i & 1) for mask in rooted]
            self.solver.add(z3.Not(self.model_formula(bags)))
            models_forbidden += 1
            if iteration and iteration % 500 == 0:
                print("progress", self.n, iteration, cuts_added, models_forbidden,
                      flush=True)
        print("LIMIT", self.n, limit, cuts_added, models_forbidden)
        return None


if __name__ == "__main__":
    orders = [int(x) for x in sys.argv[1:]] or list(range(6, 11))
    for order in orders:
        Probe(order).run()
