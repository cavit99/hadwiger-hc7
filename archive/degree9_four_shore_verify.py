#!/usr/bin/env python3
"""Independent verifier for the degree-nine four-shore certificates."""

import ast
from itertools import combinations, permutations, product
from pathlib import Path
import sys

import z3


N = 9
TOTAL = 13
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
    for _ in range(4):
        new_states = set()
        for edges in states:
            used_count = len(set(x for edge in edges for x in edge))
            additions = list(combinations(range(used_count), 2))
            additions += [(x, used_count) for x in range(used_count)]
            additions += [(used_count, used_count + 1)]
            for edge in additions:
                new_states.add(canonical_multigraph(edges + (edge,)))
        states = new_states
    result = tuple(sorted(states,
                          key=lambda value: (
                              len(set(x for edge in value for x in edge)), value)))
    assert len(result) == 23
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


def anchor_formula(blocks, w, misses, variables):
    sides = []
    for retained in range(4):
        outside = tuple(i for i in range(4) if i != retained)
        assignments = []
        for shore_order in permutations(outside):
            if any(set(misses[shore_order[pos - 1]]) & set(blocks[pos])
                   for pos in (1, 2, 3)):
                continue
            contacts = []
            for a, b in combinations((1, 2, 3), 2):
                shore_a = shore_order[a - 1]
                shore_b = shore_order[b - 1]
                fixed = (any(x not in misses[shore_a] for x in blocks[b])
                         or any(x not in misses[shore_b] for x in blocks[a]))
                contacts.append(z3.BoolVal(True) if fixed
                                else cross(blocks[a], blocks[b],
                                           misses, variables))
            if w is not None:
                for pos in (1, 2, 3):
                    shore = shore_order[pos - 1]
                    contacts.append(z3.BoolVal(True)
                                    if w not in misses[shore]
                                    else cross((w,), blocks[pos],
                                               misses, variables))
            assignments.append(z3.And(*contacts))
        sides.append(z3.Or(*assignments))
    return z3.And(independent(blocks, variables), *sides)


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
        solver.add(z3.Not(anchor_formula(blocks, None, misses, variables)))

    seen = set()
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
            solver.add(z3.Not(anchor_formula(blocks, w, misses, variables)))


def model_formula(bags, misses, variables):
    assert len(bags) == 6
    used = 0
    vertices_by_bag = []
    conditions = []
    for bag in bags:
        assert 0 < bag < (1 << TOTAL)
        assert bag & ((1 << N) - 1), "every branch set must meet N"
        assert not (used & bag), "branch sets overlap"
        used |= bag
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


def verify(index):
    base = Path(__file__).resolve().parent
    path = base / ("degree9_four_shore_certificate_%02d.txt" % index)
    data = ast.literal_eval(path.read_text(encoding="utf-8"))
    assert data["type"] == index
    misses = tuple(tuple(edge) for edge in data["misses"])
    assert misses == MISS_TYPES[index]

    variables = {edge: z3.Bool("e_%d_%d" % edge) for edge in EDGE_PAIRS}
    solver = z3.Solver()
    # alpha(A)<=4.
    for five in combinations(range(N), 5):
        solver.add(z3.Or(*(variables[edge] for edge in combinations(five, 2))))
    add_anchor_exclusions(solver, misses, variables)
    for bags in data["bags"]:
        solver.add(z3.Not(model_formula(tuple(bags), misses, variables)))
    result = solver.check()
    assert result == z3.unsat, (index, result)
    print("type", index, "verified UNSAT with", len(data["bags"]),
          "quotient templates")


def main():
    indices = [int(value) for value in sys.argv[1:]] if len(sys.argv) > 1 \
        else list(range(23))
    for index in indices:
        verify(index)


if __name__ == "__main__":
    main()
