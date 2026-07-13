#!/usr/bin/env python3
"""Independent replay of the transported leaf one-shore boundary lemma.

For each p=0,...,4, this independently rebuilds the eight-vertex boundary
constraints and every N-meeting K6 model template in the quotient obtained
by contracting the sole exterior component.  It then asks Z3 for a boundary
graph satisfying the hypotheses and avoiding every template.

This file deliberately does not import the discovery probe.
"""

from itertools import combinations
import z3

N = tuple(range(8))
SHORE = 8
V = tuple(range(9))
PAIRS = tuple(combinations(N, 2))


def boundary_partitions():
    """All partitions of any selected boundary subset into six blocks."""
    answer = []
    for size in range(6, 9):
        for selected in combinations(N, size):
            blocks = []
            def rec(i):
                if i == len(selected):
                    if len(blocks) == 6:
                        answer.append(tuple(tuple(b) for b in blocks))
                    return
                if len(blocks) + len(selected) - i < 6:
                    return
                x = selected[i]
                for block in blocks:
                    block.append(x); rec(i + 1); block.pop()
                if len(blocks) < 6:
                    blocks.append([x]); rec(i + 1); blocks.pop()
            rec(0)
    return tuple(answer)


PARTITIONS = boundary_partitions()
assert len(PARTITIONS) == 462


def fixed_or_variable_edge(a, b, edge, shore_miss=7):
    if a > b:
        a, b = b, a
    if b < 8:
        return edge[(a, b)]
    assert b == SHORE and a < 8
    return z3.BoolVal(a != shore_miss)


def some_edge(left, right, edge):
    return z3.Or(*(fixed_or_variable_edge(a, b, edge)
                   for a in left for b in right))


def model_expression(bags, edge):
    requirements = []
    for bag in bags:
        vertices = sorted(bag)
        root, tail = vertices[0], vertices[1:]
        # Every cut of a connected bag has an edge across it.
        for bits in range(1 << len(tail)):
            left = {root} | {tail[i] for i in range(len(tail))
                             if bits >> i & 1}
            if len(left) == len(vertices):
                continue
            requirements.append(some_edge(left, set(vertices) - left, edge))
    for i, j in combinations(range(6), 2):
        requirements.append(some_edge(bags[i], bags[j], edge))
    return z3.And(*requirements)


def verify(p):
    edge = {ab: z3.Bool("p%d_e%d_%d" % (p, *ab)) for ab in PAIRS}
    solver = z3.Solver()

    # alpha(N)<=3.
    for four in combinations(N, 4):
        solver.add(z3.Or(*(edge[ab] for ab in combinations(four, 2))))

    # P={0,...,p-1} is a clique.
    for ab in combinations(range(p), 2):
        solver.add(edge[ab])

    # Vertex 7 is w.  The vertices p,...,6 are the private y_s.
    solver.add(z3.PbGe([(edge[tuple(sorted((7, x)))], 1)
                        for x in N if x != 7], 6))
    for y in range(p, 7):
        solver.add(z3.PbGe([(edge[tuple(sorted((y, x)))], 1)
                            for x in N if x != y], 5))

    # D-u is full to every old-boundary label in P.
    for x in range(p):
        solver.add(z3.Or(*(edge[(x, y)] for y in range(p, 8))))

    templates = 0
    for partition in PARTITIONS:
        for destination in range(-1, 6):
            bags = [set(block) for block in partition]
            if destination >= 0:
                bags[destination].add(SHORE)
            solver.add(z3.Not(model_expression(bags, edge)))
            templates += 1

    result = solver.check()
    assert result == z3.unsat, (p, result, solver.model())
    print("p=%d verified UNSAT with %d exhaustive model templates"
          % (p, templates))


if __name__ == "__main__":
    for p in range(5):
        verify(p)
