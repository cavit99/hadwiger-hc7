#!/usr/bin/env python3
"""CEGAR probe for four two-miss shores on a nine-vertex boundary."""

from itertools import combinations, permutations, product
from pathlib import Path
import sys

import z3


N = 9
SHORES = (9, 10, 11, 12)
TOTAL = 13
EDGE_PAIRS = tuple(combinations(range(N), 2))


def canonical_multigraph(edges):
    vertices = sorted(set(x for edge in edges for x in edge))
    relabel = {x: i for i, x in enumerate(vertices)}
    normalized = tuple((relabel[a], relabel[b]) for a, b in edges)
    best = None
    for perm in permutations(range(len(vertices))):
        candidate = tuple(sorted(tuple(sorted((perm[a], perm[b])))
                                 for a, b in normalized))
        if best is None or candidate < best:
            best = candidate
    return best


def miss_types():
    states = {()}
    for _ in range(4):
        next_states = set()
        for edges in states:
            used = sorted(set(x for edge in edges for x in edge))
            count = len(used)
            choices = list(combinations(range(count), 2))
            choices.extend((x, count) for x in range(count))
            choices.append((count, count + 1))
            for edge in choices:
                next_states.add(canonical_multigraph(edges + (edge,)))
        states = next_states
    return tuple(sorted(states,
                        key=lambda e: (len(set(x for p in e for x in p)), e)))


MISS_TYPES = miss_types()
assert len(MISS_TYPES) == 23


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


def adjacent(a, b, adj):
    while a:
        bit = a & -a
        a -= bit
        if adj[bit.bit_length() - 1] & b:
            return True
    return False


def find_simple_model(edges, misses):
    """Four one-root shore bags plus two boundary singleton bags."""
    adj = quotient_adjacency(edges, misses)
    for roots in permutations(range(N), 4):
        if any(roots[i] in misses[i] for i in range(4)):
            continue
        bags = tuple((1 << SHORES[i]) | (1 << roots[i]) for i in range(4))
        if not all(adjacent(bags[i], bags[j], adj)
                   for i in range(4) for j in range(i + 1, 4)):
            continue
        remaining = [x for x in range(N) if x not in roots]
        for y, z in combinations(remaining, 2):
            all_bags = bags + (1 << y, 1 << z)
            if all(adjacent(all_bags[i], all_bags[j], adj)
                   for i in range(6) for j in range(i + 1, 6)):
                return all_bags
    return None


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


def template_expression(bags, misses, variables):
    conditions = []
    vertices = []
    for bag in bags:
        current = tuple(x for x in range(TOTAL) if bag >> x & 1)
        vertices.append(current)
        # The simple templates have two-vertex or singleton bags; retain the
        # exact cut formulation so the certificate format can later expand.
        root, rest = current[0], current[1:]
        for bits in range(1 << len(rest)):
            left = {root}
            left.update(rest[k] for k in range(len(rest)) if bits >> k & 1)
            if len(left) != len(current):
                conditions.append(cross(left, set(current) - left,
                                        misses, variables))
    for i in range(6):
        for j in range(i + 1, 6):
            conditions.append(cross(vertices[i], vertices[j],
                                    misses, variables))
    return z3.And(*conditions)


def independent_expression(blocks, variables):
    return z3.And(*(
        z3.Not(variables[tuple(sorted(edge))])
        for block in blocks for edge in combinations(block, 2)
    ))


def anchor_expression(blocks, w, misses, variables):
    """Star block 0; blocks 1..3 are connected by outside shores."""
    independence = independent_expression(blocks, variables)
    side_expressions = []
    connector_positions = (1, 2, 3)
    for retained in range(4):
        outside = tuple(i for i in range(4) if i != retained)
        assignments = []
        for shore_order in permutations(outside):
            if any(set(misses[shore_order[pos - 1]]) & set(blocks[pos])
                   for pos in connector_positions):
                continue
            conditions = []
            for a, b in combinations(connector_positions, 2):
                shore_a = shore_order[a - 1]
                shore_b = shore_order[b - 1]
                fixed = (any(x not in misses[shore_a] for x in blocks[b])
                         or any(x not in misses[shore_b] for x in blocks[a]))
                conditions.append(
                    z3.BoolVal(True) if fixed
                    else cross(blocks[a], blocks[b], misses, variables)
                )
            if w is not None:
                for pos in connector_positions:
                    shore = shore_order[pos - 1]
                    conditions.append(
                        z3.BoolVal(True) if w not in misses[shore]
                        else cross((w,), blocks[pos], misses, variables)
                    )
            assignments.append(z3.And(*conditions))
        side_expressions.append(z3.Or(*assignments))
    return z3.And(independence, *side_expressions)


def add_anchor_exclusions(solver, misses, variables):
    seen = set()
    for colors in product(range(4), repeat=N):
        if set(colors) != {0, 1, 2, 3}:
            continue
        blocks = tuple(tuple(x for x in range(N) if colors[x] == c)
                       for c in range(4))
        key = (blocks[0],) + tuple(sorted(blocks[1:]))
        if key in seen:
            continue
        seen.add(key)
        solver.add(z3.Not(anchor_expression(blocks, None, misses, variables)))

    seen.clear()
    for w in range(N):
        rest = tuple(x for x in range(N) if x != w)
        for colors in product(range(4), repeat=len(rest)):
            if set(colors) != {0, 1, 2, 3}:
                continue
            blocks = tuple(tuple(x for x, color in zip(rest, colors)
                                 if color == c)
                           for c in range(4))
            key = (blocks[0],) + tuple(sorted(blocks[1:])) + ((w,),)
            if key in seen:
                continue
            seen.add(key)
            solver.add(z3.Not(anchor_expression(blocks, w, misses, variables)))


def prove_type(type_index):
    misses = MISS_TYPES[type_index]
    variables = {edge: z3.Bool("e_%d_%d" % edge) for edge in EDGE_PAIRS}
    solver = z3.Solver()
    for five in combinations(range(N), 5):
        solver.add(z3.Or(*(variables[edge] for edge in combinations(five, 2))))
    add_anchor_exclusions(solver, misses, variables)

    certificate = []
    while solver.check() == z3.sat:
        model = solver.model()
        edges = [edge for edge, variable in variables.items()
                 if z3.is_true(model.eval(variable, model_completion=True))]
        bags = find_simple_model(edges, misses)
        if bags is None:
            print("COUNTEREXAMPLE type", type_index, misses, edges)
            return False
        certificate.append(bags)
        solver.add(z3.Not(template_expression(bags, misses, variables)))
        if len(certificate) % 100 == 0:
            print(type_index, len(certificate))
    print("UNSAT type", type_index, "templates", len(certificate), misses)
    path = Path(__file__).resolve().parent / (
        "degree9_four_shore_certificate_%02d.txt" % type_index)
    path.write_text(repr({"type": type_index, "misses": misses,
                          "bags": certificate}) + "\n", encoding="utf-8")
    return True


if __name__ == "__main__":
    index = int(sys.argv[1])
    raise SystemExit(0 if prove_type(index) else 1)
