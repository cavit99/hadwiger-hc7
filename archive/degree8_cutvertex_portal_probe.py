#!/usr/bin/env python3
"""Refined cutvertex probe retaining the portal z as an adhesion vertex."""

from itertools import combinations, permutations, product
from pathlib import Path
import sys

import z3

from degree8_cutvertex_split_probe import MISS_TYPES, PARTITIONS


N = 8
Z = 8
R1, R2, D = 9, 10, 11
TOTAL = 12
VARIABLE_PAIRS = tuple(combinations(range(N), 2)) + tuple((x, Z) for x in range(N))


def misses(miss_type):
    return (set(miss_type[0]), set(miss_type[1]), {miss_type[2]})


def concrete_adjacency(edges, miss_type):
    defect = misses(miss_type)
    adj = [0] * TOTAL
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    for branch in (R1, R2):
        adj[Z] |= 1 << branch
        adj[branch] |= 1 << Z
    for i, shore in enumerate((R1, R2, D)):
        for x in range(N):
            if x not in defect[i]:
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
    adj = concrete_adjacency(edges, miss_type)
    for partition in PARTITIONS:
        base = [sum(1 << x for x in block) for block in partition]
        # z and the three shore vertices may be placed or omitted.
        for placement in product(range(-1, 6), repeat=4):
            bags = base[:]
            for vertex, target in zip((Z, R1, R2, D), placement):
                if target >= 0:
                    bags[target] |= 1 << vertex
            if not all(connected(bag, adj) for bag in bags):
                continue
            if all(adjacent(bags[i], bags[j], adj)
                   for i in range(6) for j in range(i + 1, 6)):
                return tuple(bags)
    return None


def symbolic_edge(u, v, miss_type, variables):
    defect = misses(miss_type)
    if u > v:
        u, v = v, u
    if v < N:
        return variables[(u, v)]
    if v == Z and u < N:
        return variables[(u, Z)]
    if (u, v) in ((Z, R1), (Z, R2)):
        return z3.BoolVal(True)
    if u < N and v in (R1, R2, D):
        return z3.BoolVal(u not in defect[v - R1])
    return z3.BoolVal(False)


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


def add_portal_anchor_exclusions(solver, miss_type, variables):
    defect1, defect2, defect_d = misses(miss_type)
    # z is forced into block T.  Besides S,T,P, allow up to two singleton
    # boundary blocks; the common adhesion then uses at most five colors.
    for singleton_count in range(3):
        for w_set in combinations(range(N), singleton_count):
            remaining = tuple(x for x in range(N) if x not in w_set)
            for colors_n in product(range(3), repeat=len(remaining)):
                if 0 not in colors_n or 2 not in colors_n:
                    continue
                s = tuple(x for x, color in zip(remaining, colors_n)
                          if color == 0)
                t_n = tuple(x for x, color in zip(remaining, colors_n)
                            if color == 1)
                p = tuple(x for x, color in zip(remaining, colors_n)
                          if color == 2)
                t = t_n + (Z,)

                # R1 and R2 must both connect all of T; D connects all of P.
                if defect1 & set(t_n) or defect2 & set(t_n):
                    continue
                if defect_d & set(p):
                    continue

                independence = z3.And(*(
                    z3.Not(variables[tuple(sorted(edge))])
                    for block in (s, t, p)
                    for edge in combinations(block, 2)
                ))
                singleton_clique = z3.And(*(
                    variables[tuple(sorted(edge))]
                    for edge in combinations(w_set, 2)
                ))

                # The star v+S must be adjacent to the T anchor.
                star_t = (z3.BoolVal(True) if t_n
                          else cross(s, (Z,), miss_type, variables))

                # On branch side Ri, the other branch connects T and D P.
                branch_side = []
                for other_defect in (defect2, defect1):
                    conditions = []
                    fixed = (any(x not in other_defect for x in p)
                             or any(x not in defect_d for x in t_n))
                    conditions.append(z3.BoolVal(True) if fixed
                                      else cross(t, p, miss_type, variables))
                    for w in w_set:
                        conditions.append(
                            z3.BoolVal(True) if w not in other_defect
                            else cross((w,), t, miss_type, variables)
                        )
                        conditions.append(
                            z3.BoolVal(True) if w not in defect_d
                            else cross((w,), p, miss_type, variables)
                        )
                    branch_side.append(z3.And(*conditions))

                # On D, orient the two branches onto T and P.  Their anchors
                # are automatically adjacent through z--R_P.
                orientations = []
                for t_defect, p_defect in ((defect1, defect2),
                                            (defect2, defect1)):
                    if p_defect & set(p):
                        continue
                    conditions = []
                    for w in w_set:
                        conditions.append(
                            z3.BoolVal(True) if w not in t_defect
                            else cross((w,), t, miss_type, variables)
                        )
                        conditions.append(
                            z3.BoolVal(True) if w not in p_defect
                            else cross((w,), p, miss_type, variables)
                        )
                    orientations.append(z3.And(*conditions))
                d_side = z3.Or(*orientations)

                closure = z3.And(independence, singleton_clique, star_t,
                                 *branch_side, d_side)
                solver.add(z3.Not(closure))

    # Second mode: z itself is a singleton color.  The three contracted
    # anchors use independent N-blocks S,T,P, with at most one further
    # singleton w.  This mode is essential when z has contacts to both the
    # star block and the D-connected block.
    for extra_count in range(2):
        for extra in combinations(range(N), extra_count):
            remaining = tuple(x for x in range(N) if x not in extra)
            for colors in product(range(3), repeat=len(remaining)):
                if set(colors) != {0, 1, 2}:
                    continue
                s = tuple(x for x, color in zip(remaining, colors)
                          if color == 0)
                t = tuple(x for x, color in zip(remaining, colors)
                          if color == 1)
                p = tuple(x for x, color in zip(remaining, colors)
                          if color == 2)

                # On either branch side, the other branch connects T and D
                # connects P.
                if defect1 & set(t) or defect2 & set(t):
                    continue
                if defect_d & set(p):
                    continue

                independence = z3.And(*(
                    z3.Not(variables[tuple(sorted(edge))])
                    for block in (s, t, p)
                    for edge in combinations(block, 2)
                ))
                z_contacts = z3.And(
                    cross((Z,), s, miss_type, variables),
                    cross((Z,), p, miss_type, variables),
                )
                extra_clique = z3.And(*(
                    variables[tuple(sorted((w, Z)))] for w in extra
                ))

                branch_sides = []
                for other_defect in (defect2, defect1):
                    conditions = []
                    fixed = (any(x not in other_defect for x in p)
                             or any(x not in defect_d for x in t))
                    conditions.append(z3.BoolVal(True) if fixed
                                      else cross(t, p, miss_type, variables))
                    for w in extra:
                        conditions.append(
                            z3.BoolVal(True) if w not in other_defect
                            else cross((w,), t, miss_type, variables)
                        )
                        conditions.append(
                            z3.BoolVal(True) if w not in defect_d
                            else cross((w,), p, miss_type, variables)
                        )
                    branch_sides.append(z3.And(*conditions))

                d_orientations = []
                for t_defect, p_defect in ((defect1, defect2),
                                            (defect2, defect1)):
                    if p_defect & set(p):
                        continue
                    conditions = []
                    fixed = (any(x not in t_defect for x in p)
                             or any(x not in p_defect for x in t))
                    conditions.append(z3.BoolVal(True) if fixed
                                      else cross(t, p, miss_type, variables))
                    for w in extra:
                        conditions.append(
                            z3.BoolVal(True) if w not in t_defect
                            else cross((w,), t, miss_type, variables)
                        )
                        conditions.append(
                            z3.BoolVal(True) if w not in p_defect
                            else cross((w,), p, miss_type, variables)
                        )
                    d_orientations.append(z3.And(*conditions))
                closure = z3.And(independence, z_contacts, extra_clique,
                                 *branch_sides, z3.Or(*d_orientations))
                solver.add(z3.Not(closure))


def prove(index):
    miss_type = MISS_TYPES[index]
    variables = {edge: z3.Bool("e_%d_%d" % edge) for edge in VARIABLE_PAIRS}
    solver = z3.Solver()
    for four in combinations(range(N), 4):
        solver.add(z3.Or(*(variables[edge] for edge in combinations(four, 2))))
    add_portal_anchor_exclusions(solver, miss_type, variables)

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
    path = Path(__file__).resolve().parent / (
        "degree8_cutvertex_portal_certificate_%d.txt" % index)
    path.write_text(repr({"type": index, "miss_type": miss_type,
                          "bags": certificate}) + "\n", encoding="utf-8")
    return True


if __name__ == "__main__":
    index = int(sys.argv[1])
    raise SystemExit(0 if prove(index) else 1)
