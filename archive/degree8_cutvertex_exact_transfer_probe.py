#!/usr/bin/env python3
"""CEGAR proof search using arbitrary exact complementary boundary states."""

from itertools import combinations, product
from pathlib import Path
import sys

import z3

from degree8_cutvertex_portal_probe import (
    N, Z, R1, R2, D, TOTAL, VARIABLE_PAIRS, MISS_TYPES,
    concrete_adjacency, find_model, model_expression, symbolic_edge, cross,
)


APEX = 12
FULL_TOTAL = 13
X = tuple(range(9))
TARGETS = (R1, R2, D)


def all_partitions():
    blocks = []

    def rec(pos):
        if pos == len(X):
            if 1 <= len(blocks) <= 6:
                partition = tuple(tuple(block) for block in blocks)
                if sum(any(x < N for x in block) for block in partition) <= 5:
                    yield partition
            return
        x = X[pos]
        for i in range(len(blocks)):
            blocks[i].append(x)
            yield from rec(pos + 1)
            blocks[i].pop()
        if len(blocks) < 6:
            blocks.append([x])
            yield from rec(pos + 1)
            blocks.pop()

    yield from rec(0)


PARTITIONS = tuple(all_partitions())


def full_adjacency(edges, miss_type):
    adj = concrete_adjacency(edges, miss_type) + [0]
    for x in range(N):
        adj[APEX] |= 1 << x
        adj[x] |= 1 << APEX
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


def independent(partition, adj):
    for block in partition:
        for x, y in combinations(block, 2):
            if adj[x] >> y & 1:
                return False
    return True


def realization(partition, target, adj):
    optional = [APEX, R1, R2, D]
    optional.remove(target)
    q = len(partition)
    base = [sum(1 << x for x in block) for block in partition]
    for assignment in product(range(-1, q), repeat=3):
        bags = base[:]
        for vertex, block in zip(optional, assignment):
            if block >= 0:
                bags[block] |= 1 << vertex
        if not all(connected(bag, adj) for bag in bags):
            continue
        if all(adjacent(bags[i], bags[j], adj)
               for i in range(q) for j in range(i + 1, q)):
            return tuple(bags)
    return None


def exact_state(edges, miss_type):
    adj = full_adjacency(edges, miss_type)
    for partition in PARTITIONS:
        if not independent(partition, adj):
            continue
        witnesses = []
        for target in TARGETS:
            bags = realization(partition, target, adj)
            if bags is None:
                break
            witnesses.append(bags)
        if len(witnesses) == 3:
            return partition, tuple(witnesses)
    return None


def full_symbolic_edge(u, v, miss_type, variables):
    if u > v:
        u, v = v, u
    if v == APEX and u < N:
        return z3.BoolVal(True)
    if v == APEX:
        return z3.BoolVal(False)
    return symbolic_edge(u, v, miss_type, variables)


def full_cross(left, right, miss_type, variables):
    return z3.Or(*(full_symbolic_edge(u, v, miss_type, variables)
                   for u in left for v in right))


def bags_expression(bags, miss_type, variables):
    conditions = []
    vertices_by_bag = []
    for bag in bags:
        vertices = tuple(x for x in range(FULL_TOTAL) if bag >> x & 1)
        vertices_by_bag.append(vertices)
        root, rest = vertices[0], vertices[1:]
        for bits in range(1 << len(rest)):
            left = {root}
            left.update(rest[k] for k in range(len(rest)) if bits >> k & 1)
            if len(left) != len(vertices):
                conditions.append(full_cross(left, set(vertices) - left,
                                             miss_type, variables))
    for i in range(len(bags)):
        for j in range(i + 1, len(bags)):
            conditions.append(full_cross(vertices_by_bag[i],
                                         vertices_by_bag[j],
                                         miss_type, variables))
    return z3.And(*conditions)


def state_expression(partition, witnesses, miss_type, variables):
    independence = z3.And(*(
        z3.Not(variables[tuple(sorted((x, y)))])
        for block in partition for x, y in combinations(block, 2)
    ))
    return z3.And(independence, *(
        bags_expression(bags, miss_type, variables) for bags in witnesses
    ))


def prove(index):
    miss_type = MISS_TYPES[index]
    variables = {edge: z3.Bool("e_%d_%d" % edge) for edge in VARIABLE_PAIRS}
    solver = z3.Solver()
    for four in combinations(range(N), 4):
        solver.add(z3.Or(*(variables[edge] for edge in combinations(four, 2))))

    certificate = []
    while solver.check() == z3.sat:
        assignment = solver.model()
        edges = [edge for edge, variable in variables.items()
                 if z3.is_true(assignment.eval(variable, model_completion=True))]

        state = exact_state(edges, miss_type)
        if state is not None:
            partition, witnesses = state
            certificate.append(("state", partition, witnesses))
            solver.add(z3.Not(state_expression(partition, witnesses,
                                               miss_type, variables)))
            continue

        quotient_model = find_model(edges, miss_type)
        if quotient_model is not None:
            certificate.append(("model", quotient_model))
            solver.add(z3.Not(model_expression(quotient_model, miss_type,
                                               variables)))
            continue

        print("COUNTEREXAMPLE", index, miss_type, edges)
        return False

    states = sum(entry[0] == "state" for entry in certificate)
    models = len(certificate) - states
    print("UNSAT", index, miss_type, "states", states, "models", models)
    path = Path(__file__).resolve().parent / (
        "degree8_cutvertex_exact_transfer_certificate_%d.txt" % index)
    path.write_text(repr({"type": index, "miss_type": miss_type,
                          "entries": certificate}) + "\n", encoding="utf-8")
    return True


if __name__ == "__main__":
    index = int(sys.argv[1])
    raise SystemExit(0 if prove(index) else 1)
