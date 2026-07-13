#!/usr/bin/env python3
"""Discovery/CEGAR probe for two one-miss shores on an 8-boundary."""

from itertools import combinations, product
import sys

import z3


N = 8
SHORES = (8, 9)
TOTAL = 10


def partitions_of_selected(selected):
    selected = tuple(selected)
    blocks = []

    def rec(pos):
        if pos == len(selected):
            if len(blocks) == 6:
                yield tuple(tuple(block) for block in blocks)
            return
        if len(blocks) + len(selected) - pos < 6:
            return
        x = selected[pos]
        for i in range(len(blocks)):
            blocks[i].append(x)
            yield from rec(pos + 1)
            blocks[i].pop()
        if len(blocks) < 6:
            blocks.append([x])
            yield from rec(pos + 1)
            blocks.pop()

    yield from rec(0)


PARTITIONS = tuple(
    partition
    for size in range(6, N + 1)
    for selected in combinations(range(N), size)
    for partition in partitions_of_selected(selected)
)
assert len(PARTITIONS) == 462


def adjacency(boundary_edges, miss):
    adj = [0] * TOTAL
    for u, v in boundary_edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    for i, shore in enumerate(SHORES):
        for x in range(N):
            if x != miss[i]:
                adj[shore] |= 1 << x
                adj[x] |= 1 << shore
    return adj


def connected(mask, adj):
    seen = mask & -mask
    frontier = seen
    while frontier:
        bit = frontier & -frontier
        frontier -= bit
        vertex = bit.bit_length() - 1
        new = adj[vertex] & mask & ~seen
        seen |= new
        frontier |= new
    return seen == mask


def cross(a, b, adj):
    while a:
        bit = a & -a
        a -= bit
        if adj[bit.bit_length() - 1] & b:
            return True
    return False


def find_model(edges, miss):
    adj = adjacency(edges, miss)
    for partition in PARTITIONS:
        base = [sum(1 << x for x in block) for block in partition]
        for placement in product(range(-1, 6), repeat=2):
            bags = base[:]
            for i, target in enumerate(placement):
                if target >= 0:
                    bags[target] |= 1 << SHORES[i]
            if not all(connected(bag, adj) for bag in bags):
                continue
            if all(cross(bags[i], bags[j], adj)
                   for i in range(6) for j in range(i + 1, 6)):
                return tuple(bags)
    return None


def anchor_partition(edges, miss):
    eset = {tuple(sorted(edge)) for edge in edges}
    for colors in product(range(5), repeat=N):
        used = set(colors)
        if 0 not in used or 1 not in used or not used.issubset(set(range(5))):
            continue
        # Colors 0 and 1 are S,T; colors >=2 are singleton blocks.
        blocks = [set(x for x in range(N) if colors[x] == c) for c in range(5)]
        if any(len(blocks[c]) > 1 for c in range(2, 5)):
            continue
        if any(tuple(sorted(edge)) in eset
               for c in (0, 1) for edge in combinations(blocks[c], 2)):
            continue
        if miss[0] in blocks[1] or miss[1] in blocks[1]:
            continue
        singles = [next(iter(blocks[c])) for c in range(2, 5) if blocks[c]]
        if any(tuple(sorted(edge)) not in eset for edge in combinations(singles, 2)):
            continue
        good = True
        for shore_miss in miss:
            for w in singles:
                if w == shore_miss and not any(
                        tuple(sorted((w, t))) in eset for t in blocks[1]):
                    good = False
        if good:
            return tuple(tuple(sorted(block)) for block in blocks if block)
    return None


EDGE_PAIRS = tuple(combinations(range(N), 2))


def edge_kind(u, v, miss):
    if u > v:
        u, v = v, u
    if v < N:
        return (u, v)
    if u >= N:
        return False
    return u != miss[v - N]


def template_clauses(bags, miss):
    clauses = set()

    def require(left, right):
        variables = set()
        for u in left:
            for v in right:
                kind = edge_kind(u, v, miss)
                if kind is True:
                    return True
                if kind is not False:
                    variables.add(kind)
        if not variables:
            return False
        clauses.add(tuple(sorted(variables)))
        return True

    vertices_by_bag = []
    for bag in bags:
        vertices = tuple(x for x in range(TOTAL) if bag >> x & 1)
        vertices_by_bag.append(vertices)
        root, rest = vertices[0], vertices[1:]
        for bits in range(1 << len(rest)):
            left = {root}
            left.update(rest[k] for k in range(len(rest)) if bits >> k & 1)
            if len(left) == len(vertices):
                continue
            if not require(left, set(vertices) - left):
                return None
    for i in range(6):
        for j in range(i + 1, 6):
            if not require(vertices_by_bag[i], vertices_by_bag[j]):
                return None
    return tuple(sorted(clauses))


def prove(miss):
    variables = {edge: z3.Bool("e_%d_%d" % edge) for edge in EDGE_PAIRS}
    solver = z3.Solver()
    for four in combinations(range(N), 4):
        solver.add(z3.Or(*(variables[edge] for edge in combinations(four, 2))))

    # Exclude S|T|singletons anchor closures (at most three singletons).
    seen = set()
    for assignment in product(range(5), repeat=N):
        if 0 not in assignment or 1 not in assignment:
            continue
        blocks = tuple(tuple(x for x in range(N) if assignment[x] == c)
                       for c in range(5))
        if any(len(blocks[c]) > 1 for c in range(2, 5)):
            continue
        key = (blocks[0], blocks[1], tuple(sorted(blocks[2:])))
        if key in seen:
            continue
        seen.add(key)
        if miss[0] in blocks[1] or miss[1] in blocks[1]:
            continue
        independence = z3.And(*(
            z3.Not(variables[tuple(sorted(edge))])
            for c in (0, 1) for edge in combinations(blocks[c], 2)
        ))
        singles = tuple(block[0] for block in blocks[2:] if block)
        clique = z3.And(*(variables[tuple(sorted(edge))]
                          for edge in combinations(singles, 2)))
        side_conditions = []
        for shore_miss in miss:
            for w in singles:
                if w == shore_miss:
                    side_conditions.append(z3.Or(*(
                        variables[tuple(sorted((w, t)))] for t in blocks[1]
                    )))
        solver.add(z3.Not(z3.And(independence, clique, *side_conditions)))

    certificate = []
    while solver.check() == z3.sat:
        model = solver.model()
        edges = [edge for edge, variable in variables.items()
                 if z3.is_true(model.eval(variable, model_completion=True))]
        bags = find_model(edges, miss)
        if bags is None:
            print("COUNTEREXAMPLE", miss, edges,
                  "anchor", anchor_partition(edges, miss))
            return False
        clauses = template_clauses(bags, miss)
        assert clauses is not None
        certificate.append(bags)
        solver.add(z3.Not(z3.And(*(
            z3.Or(*(variables[edge] for edge in clause)) for clause in clauses
        ))))
        if len(certificate) % 100 == 0:
            print(miss, len(certificate))
    print("UNSAT", miss, len(certificate))
    return True


if __name__ == "__main__":
    patterns = ((0, 0), (0, 1))
    raise SystemExit(0 if prove(patterns[int(sys.argv[1])]) else 1)
