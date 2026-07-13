#!/usr/bin/env python3
"""Independent verifier for the degree-eight three-shore certificates.

The verifier reconstructs, from first principles, the finite boundary
statement used in ``hadwiger_degree8_three_component_closure.md``.  It does
not import the discovery program.
"""

import ast
from itertools import combinations, product
from pathlib import Path

import z3


BOUNDARY = 8
TOTAL = 11
SHORE_VERTICES = (8, 9, 10)
EDGE_PAIRS = tuple(combinations(range(BOUNDARY), 2))


def edge_value(u, v, miss, variables):
    if u > v:
        u, v = v, u
    if v < BOUNDARY:
        return variables[(u, v)]
    if u >= BOUNDARY:
        return z3.BoolVal(False)
    return z3.BoolVal(u != miss[v - BOUNDARY])


def cross(left, right, miss, variables):
    return z3.Or(*(edge_value(u, v, miss, variables)
                   for u in left for v in right))


def model_expression(bags, miss, variables):
    assert len(bags) == 6
    used = 0
    for bag in bags:
        assert 0 < bag < (1 << TOTAL)
        assert bag & ((1 << BOUNDARY) - 1), "every bag must meet N"
        assert not (used & bag), "branch sets must be disjoint"
        used |= bag

    conditions = []
    bag_vertices = []
    for bag in bags:
        vertices = tuple(v for v in range(TOTAL) if bag >> v & 1)
        bag_vertices.append(vertices)
        root, others = vertices[0], vertices[1:]
        for bits in range(1 << len(others)):
            left = {root}
            left.update(others[k] for k in range(len(others))
                        if bits >> k & 1)
            if len(left) == len(vertices):
                continue
            right = set(vertices) - left
            conditions.append(cross(left, right, miss, variables))

    for i in range(6):
        for j in range(i + 1, 6):
            conditions.append(cross(bag_vertices[i], bag_vertices[j],
                                    miss, variables))
    return z3.And(*conditions)


def add_three_anchor_exclusions(solver, miss, variables):
    seen = set()
    for colors in product(range(3), repeat=BOUNDARY):
        if set(colors) != {0, 1, 2}:
            continue
        blocks = tuple(tuple(x for x in range(BOUNDARY)
                             if colors[x] == color)
                       for color in range(3))
        key = (blocks[0],) + tuple(sorted((blocks[1], blocks[2])))
        if key in seen:
            continue
        seen.add(key)
        bsets = tuple(set(block) for block in blocks)
        usable = True
        for retained in range(3):
            first, second = [x for x in range(3) if x != retained]
            if not ((miss[first] not in bsets[1]
                     and miss[second] not in bsets[2])
                    or (miss[first] not in bsets[2]
                        and miss[second] not in bsets[1])):
                usable = False
                break
        if not usable:
            continue
        internal_edges = [variables[tuple(sorted(edge))]
                          for block in blocks
                          for edge in combinations(block, 2)]
        # At least one block is not independent.
        solver.add(z3.Or(*internal_edges))


def add_four_anchor_exclusions(solver, miss, variables):
    seen = set()
    for w in range(BOUNDARY):
        rest = tuple(x for x in range(BOUNDARY) if x != w)
        for tail_colors in product(range(3), repeat=len(rest)):
            if set(tail_colors) != {0, 1, 2}:
                continue
            blocks = tuple(tuple(x for x, color in zip(rest, tail_colors)
                                 if color == target)
                           for target in range(3))
            key = (blocks[0],) + tuple(sorted((blocks[1], blocks[2]))) + ((w,),)
            if key in seen:
                continue
            seen.add(key)

            independence = z3.And(*(
                z3.Not(variables[tuple(sorted(edge))])
                for block in blocks for edge in combinations(block, 2)
            ))
            all_sides = []
            for retained in range(3):
                j, k = [x for x in range(3) if x != retained]
                assignments = []
                for first, second in ((j, k), (k, j)):
                    # first connects block 1, second connects block 2.
                    if miss[first] in blocks[1] or miss[second] in blocks[2]:
                        continue
                    bd_fixed = (any(x != miss[first] for x in blocks[2])
                                or any(x != miss[second] for x in blocks[1]))
                    bd = (z3.BoolVal(True) if bd_fixed
                          else cross(blocks[1], blocks[2], miss, variables))
                    wb = (z3.BoolVal(True) if w != miss[first]
                          else cross((w,), blocks[1], miss, variables))
                    wd = (z3.BoolVal(True) if w != miss[second]
                          else cross((w,), blocks[2], miss, variables))
                    assignments.append(z3.And(bd, wb, wd))
                all_sides.append(z3.Or(*assignments))
            solver.add(z3.Not(z3.And(independence, *all_sides)))


def verify(path):
    data = ast.literal_eval(Path(path).read_text(encoding="utf-8"))
    miss = tuple(data["miss"])
    bags_list = data["bags"]
    assert miss in {(0, 0, 0), (0, 0, 1), (0, 1, 2)}

    variables = {edge: z3.Bool("e_%d_%d" % edge) for edge in EDGE_PAIRS}
    solver = z3.Solver()

    # alpha(A)<=3: every four boundary vertices span an edge.
    for four in combinations(range(BOUNDARY), 4):
        solver.add(z3.Or(*(variables[edge]
                           for edge in combinations(four, 2))))

    add_three_anchor_exclusions(solver, miss, variables)
    add_four_anchor_exclusions(solver, miss, variables)

    for bags in bags_list:
        solver.add(z3.Not(model_expression(tuple(bags), miss, variables)))

    result = solver.check()
    assert result == z3.unsat, (path, result)
    print(path, "verified UNSAT with", len(bags_list), "model templates")


def main():
    base = Path(__file__).resolve().parent
    for index in range(3):
        verify(base / ("degree8_three_shore_certificate_%d.txt" % index))


if __name__ == "__main__":
    main()
