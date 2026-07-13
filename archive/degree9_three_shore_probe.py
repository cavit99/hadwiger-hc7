#!/usr/bin/env python3
"""CEGIS discovery probe for three two-miss shores on a 9-boundary.

This program is not part of the trusted proof.  It searches for a finite
list of N-meeting K6 quotient models after excluding every usable
star-plus-two-shore anchor with zero, one, or two boundary singletons.
It prints the resulting certificate as a Python literal; it does not write
the certificate file.
"""

from itertools import combinations, permutations, product
import sys

import z3


N = 9
SHORES = (9, 10, 11)
TOTAL = 12
EDGE_PAIRS = tuple(combinations(range(N), 2))


def canonical_multigraph(edges):
    vertices = sorted(set(x for edge in edges for x in edge))
    relabel = {x: i for i, x in enumerate(vertices)}
    normalized = tuple((relabel[a], relabel[b]) for a, b in edges)
    candidates = []
    for perm in permutations(range(len(vertices))):
        candidates.append(tuple(sorted(tuple(sorted((perm[a], perm[b])))
                                       for a, b in normalized)))
    return min(candidates)


def all_miss_types():
    states = {()}
    for _ in range(3):
        next_states = set()
        for edges in states:
            count = len(set(x for edge in edges for x in edge))
            additions = list(combinations(range(count), 2))
            additions += [(x, count) for x in range(count)]
            additions += [(count, count + 1)]
            for edge in additions:
                next_states.add(canonical_multigraph(edges + (edge,)))
        states = next_states
    result = tuple(sorted(states,
                          key=lambda value: (
                              len(set(x for edge in value for x in edge)),
                              value)))
    assert len(result) == 8
    return result


MISS_TYPES = all_miss_types()


def symbolic_edge(u, v, misses, variables):
    if u > v:
        u, v = v, u
    if v < N:
        return variables[(u, v)]
    if u >= N:
        return z3.BoolVal(False)
    return z3.BoolVal(u not in misses[v - N])


def cross(left, right, misses, variables):
    return z3.Or(*(symbolic_edge(u, v, misses, variables)
                   for u in left for v in right))


def independent(blocks, variables):
    return z3.And(*(
        z3.Not(variables[tuple(sorted(edge))])
        for block in blocks for edge in combinations(block, 2)
    ))


def anchor_formula(blocks, singletons, misses, variables):
    """Exact star + two shore-block clique, with 0--2 singletons."""
    singleton_clique = z3.And(*(
        variables[tuple(sorted(edge))]
        for edge in combinations(singletons, 2)
    ))
    sides = []
    for retained in range(3):
        outside = tuple(i for i in range(3) if i != retained)
        assignments = []
        for first, second in (outside, outside[::-1]):
            if set(misses[first]) & set(blocks[1]):
                continue
            if set(misses[second]) & set(blocks[2]):
                continue

            contacts = []
            fixed = (any(x not in misses[first] for x in blocks[2])
                     or any(x not in misses[second] for x in blocks[1]))
            contacts.append(z3.BoolVal(True) if fixed
                            else cross(blocks[1], blocks[2],
                                       misses, variables))
            for w in singletons:
                contacts.append(z3.BoolVal(True)
                                if w not in misses[first]
                                else cross((w,), blocks[1],
                                           misses, variables))
                contacts.append(z3.BoolVal(True)
                                if w not in misses[second]
                                else cross((w,), blocks[2],
                                           misses, variables))
            assignments.append(z3.And(*contacts))
        sides.append(z3.Or(*assignments))
    return z3.And(independent(blocks, variables), singleton_clique, *sides)


def add_anchor_exclusions(solver, misses, variables):
    for singleton_count in range(3):
        seen = set()
        for singletons in combinations(range(N), singleton_count):
            rest = tuple(x for x in range(N) if x not in singletons)
            for colors in product(range(3), repeat=len(rest)):
                if set(colors) != {0, 1, 2}:
                    continue
                blocks = tuple(tuple(x for x, color in zip(rest, colors)
                                     if color == target)
                               for target in range(3))
                key = ((blocks[0],) + tuple(sorted(blocks[1:]))
                       + (tuple(singletons),))
                if key in seen:
                    continue
                seen.add(key)
                solver.add(z3.Not(anchor_formula(
                    blocks, singletons, misses, variables)))


def quotient_adjacency(edges, misses):
    adj = [0] * TOTAL
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    for i, shore in enumerate(SHORES):
        for x in range(N):
            if x not in misses[i]:
                adj[shore] |= 1 << x
                adj[x] |= 1 << shore
    return adj


def adjacent(left, right, adj):
    while left:
        bit = left & -left
        left -= bit
        if adj[bit.bit_length() - 1] & right:
            return True
    return False


def connected(mask, adj):
    reached = mask & -mask
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier -= bit
        vertex = bit.bit_length() - 1
        new = adj[vertex] & mask & ~reached
        reached |= new
        frontier |= new
    return reached == mask


def find_simple_model(edges, misses):
    """Three one-root shore bags and three boundary singleton bags."""
    adj = quotient_adjacency(edges, misses)
    for roots in permutations(range(N), 3):
        if any(roots[i] in misses[i] for i in range(3)):
            continue
        shore_bags = tuple((1 << SHORES[i]) | (1 << roots[i])
                           for i in range(3))
        if not all(adjacent(shore_bags[i], shore_bags[j], adj)
                   for i in range(3) for j in range(i + 1, 3)):
            continue
        remaining = tuple(x for x in range(N) if x not in roots)
        for singleton_vertices in combinations(remaining, 3):
            bags = shore_bags + tuple(1 << x for x in singleton_vertices)
            if all(adjacent(bags[i], bags[j], adj)
                   for i in range(6) for j in range(i + 1, 6)):
                return bags
    return None


def selected_partitions():
    answer = []
    blocks = []

    def visit(selected, pos):
        if pos == len(selected):
            if len(blocks) == 6:
                answer.append(tuple(tuple(block) for block in blocks))
            return
        if len(blocks) + len(selected) - pos < 6:
            return
        x = selected[pos]
        for block in blocks:
            block.append(x)
            visit(selected, pos + 1)
            block.pop()
        if len(blocks) < 6:
            blocks.append([x])
            visit(selected, pos + 1)
            blocks.pop()

    for size in range(6, N + 1):
        for selected in combinations(range(N), size):
            visit(selected, 0)
    assert len(answer) == 5880
    return tuple(answer)


PARTITIONS = selected_partitions()


def find_general_model(edges, misses):
    """Exhaust all N-meeting K6 quotient models."""
    adj = quotient_adjacency(edges, misses)
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


def model_formula(bags, misses, variables):
    vertices_by_bag = []
    conditions = []
    for bag in bags:
        vertices = tuple(x for x in range(TOTAL) if bag >> x & 1)
        vertices_by_bag.append(vertices)
        root, rest = vertices[0], vertices[1:]
        for bits in range(1 << len(rest)):
            left = {root}
            left.update(rest[k] for k in range(len(rest)) if bits >> k & 1)
            if len(left) != len(vertices):
                conditions.append(cross(left, set(vertices) - left,
                                        misses, variables))
    for i in range(6):
        for j in range(i + 1, 6):
            conditions.append(cross(vertices_by_bag[i], vertices_by_bag[j],
                                    misses, variables))
    return z3.And(*conditions)


def prove_type(index, critical_boundary=False, emit_certificate=False):
    misses = MISS_TYPES[index]
    variables = {edge: z3.Bool("e_%d_%d" % edge) for edge in EDGE_PAIRS}
    solver = z3.Solver()
    for five in combinations(range(N), 5):
        solver.add(z3.Or(*(variables[edge]
                           for edge in combinations(five, 2))))
    if critical_boundary:
        # A boundary vertex missed by all three exterior components has no
        # neighbour outside N[v].  Since delta(G)>=7, it has at least six
        # neighbours in the boundary.  This is the strongest immediate
        # degree constraint visible in the contact quotient.
        common_misses = set.intersection(*(set(miss) for miss in misses))
        for vertex in common_misses:
            solver.add(z3.PbGe(
                [(variables[tuple(sorted((vertex, other)))], 1)
                 for other in range(N) if other != vertex], 6))
    add_anchor_exclusions(solver, misses, variables)

    certificate = []
    while solver.check() == z3.sat:
        boundary = solver.model()
        edges = [edge for edge, variable in variables.items()
                 if z3.is_true(boundary.eval(variable,
                                             model_completion=True))]
        bags = find_simple_model(edges, misses)
        if bags is None:
            bags = find_general_model(edges, misses)
        if bags is None:
            print("COUNTEREXAMPLE", index, misses, edges, flush=True)
            return False
        certificate.append(tuple(bags))
        solver.add(z3.Not(model_formula(bags, misses, variables)))
        if len(certificate) % 25 == 0:
            print("type", index, "templates", len(certificate), flush=True)

    print("UNSAT", index, "templates", len(certificate), misses, flush=True)
    if emit_certificate:
        print("CERTIFICATE", repr({"type": index, "misses": misses,
                                    "bags": certificate}), flush=True)
    return True


if __name__ == "__main__":
    type_index = int(sys.argv[1])
    critical = len(sys.argv) > 2 and sys.argv[2] == "--critical-boundary"
    emit = "--emit-certificate" in sys.argv[2:]
    raise SystemExit(0 if prove_type(type_index, critical, emit) else 1)
