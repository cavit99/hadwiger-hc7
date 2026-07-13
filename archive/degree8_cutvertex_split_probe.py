#!/usr/bin/env python3
"""Probe the degree-8 two-component cutvertex split quotient.

Shore vertices 8 and 9 are adjacent and miss at most two boundary
vertices.  Shore 10 is anticomplete to them and misses at most one.
"""

from itertools import combinations, permutations, product
import sys

import z3


N = 8
TOTAL = 11
SHORES = (8, 9, 10)
EDGE_PAIRS = tuple(combinations(range(N), 2))


def canonical_type(edge_a, edge_b, singleton):
    vertices = sorted(set(edge_a) | set(edge_b) | {singleton})
    relabel = {x: i for i, x in enumerate(vertices)}
    ea = tuple(relabel[x] for x in edge_a)
    eb = tuple(relabel[x] for x in edge_b)
    s = relabel[singleton]
    best = None
    for perm in permutations(range(len(vertices))):
        edges = tuple(sorted((tuple(sorted((perm[ea[0]], perm[ea[1]]))),
                              tuple(sorted((perm[eb[0]], perm[eb[1]]))))))
        candidate = (edges[0], edges[1], perm[s])
        if best is None or candidate < best:
            best = candidate
    return best


def miss_types():
    types = set()
    edges = tuple(combinations(range(N), 2))
    for ea in edges:
        for eb in edges:
            for s in range(N):
                types.add(canonical_type(ea, eb, s))
    return tuple(sorted(types,
                        key=lambda value: (
                            len(set(value[0]) | set(value[1]) | {value[2]}),
                            value)))


MISS_TYPES = miss_types()


def boundary_partitions():
    def selected_partitions(selected):
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

    return tuple(
        partition
        for size in range(6, N + 1)
        for selected in combinations(range(N), size)
        for partition in selected_partitions(selected)
    )


PARTITIONS = boundary_partitions()
assert len(PARTITIONS) == 462


def adjacency(edges, miss_type):
    misses = (set(miss_type[0]), set(miss_type[1]), {miss_type[2]})
    adj = [0] * TOTAL
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    adj[8] |= 1 << 9
    adj[9] |= 1 << 8
    for i, shore in enumerate(SHORES):
        for x in range(N):
            if x not in misses[i]:
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


def adjacent(a, b, adj):
    while a:
        bit = a & -a
        a -= bit
        if adj[bit.bit_length() - 1] & b:
            return True
    return False


def find_model(edges, miss_type):
    adj = adjacency(edges, miss_type)
    for partition in PARTITIONS:
        base = [sum(1 << x for x in block) for block in partition]
        for placement in product(range(-1, 6), repeat=3):
            bags = base[:]
            for i, target in enumerate(placement):
                if target >= 0:
                    bags[target] |= 1 << SHORES[i]
            if not all(connected(bag, adj) for bag in bags):
                continue
            if all(adjacent(bags[i], bags[j], adj)
                   for i in range(6) for j in range(i + 1, 6)):
                return tuple(bags)
    return None


def symbolic_edge(u, v, miss_type, variables):
    misses = (set(miss_type[0]), set(miss_type[1]), {miss_type[2]})
    if u > v:
        u, v = v, u
    if v < N:
        return variables[(u, v)]
    if u >= N:
        return z3.BoolVal((u, v) == (8, 9))
    return z3.BoolVal(u not in misses[v - N])


def cross(left, right, miss_type, variables):
    return z3.Or(*(symbolic_edge(u, v, miss_type, variables)
                   for u in left for v in right))


def model_expression(bags, miss_type, variables):
    conditions = []
    vertices_by_bag = []
    for bag in bags:
        vertices = tuple(x for x in range(TOTAL) if bag >> x & 1)
        vertices_by_bag.append(vertices)
        root, rest = vertices[0], vertices[1:]
        for bits in range(1 << len(rest)):
            left = {root}
            left.update(rest[k] for k in range(len(rest)) if bits >> k & 1)
            if len(left) != len(vertices):
                conditions.append(cross(left, set(vertices) - left,
                                        miss_type, variables))
    for i in range(6):
        for j in range(i + 1, 6):
            conditions.append(cross(vertices_by_bag[i], vertices_by_bag[j],
                                    miss_type, variables))
    return z3.And(*conditions)


def prove(index):
    miss_type = MISS_TYPES[index]
    variables = {edge: z3.Bool("e_%d_%d" % edge) for edge in EDGE_PAIRS}
    solver = z3.Solver()
    for four in combinations(range(N), 4):
        solver.add(z3.Or(*(variables[edge] for edge in combinations(four, 2))))

    certificate = []
    while solver.check() == z3.sat:
        model = solver.model()
        edges = [edge for edge, variable in variables.items()
                 if z3.is_true(model.eval(variable, model_completion=True))]
        bags = find_model(edges, miss_type)
        if bags is None:
            print("COUNTEREXAMPLE", index, miss_type, edges)
            return False
        certificate.append(bags)
        solver.add(z3.Not(model_expression(bags, miss_type, variables)))
        if len(certificate) % 100 == 0:
            print(index, len(certificate))
    print("UNSAT", index, miss_type, len(certificate))
    return True


if __name__ == "__main__":
    print("types", len(MISS_TYPES))
    index = int(sys.argv[1])
    raise SystemExit(0 if prove(index) else 1)
