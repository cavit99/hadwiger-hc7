#!/usr/bin/env python3
"""Search for a counterexample to a finite degree-eight quotient lemma.

For each multiplicity pattern of five missed boundary vertices, seek a graph A
on eight vertices with alpha(A) <= 3 for which no K7 model of the following
explicit form exists: two adjacent singleton boundary bags y,z and five bags
{c_i,x_i}, where c_i is adjacent to every boundary vertex except m_i.

UNSAT for all patterns proves the restricted paired-bag certificate; it does
not by itself test arbitrary K7 minor models.
"""

from itertools import combinations, permutations
from z3 import And, Bool, Not, Or, Solver, sat


V = range(8)
PAIRS = list(combinations(V, 2))


def partitions(n, max_part=None):
    if n == 0:
        yield []
        return
    if max_part is None or max_part > n:
        max_part = n
    for first in range(max_part, 0, -1):
        for rest in partitions(n - first, first):
            yield [first] + rest


def missed_row(partition):
    row = []
    for vertex, multiplicity in enumerate(partition):
        row.extend([vertex] * multiplicity)
    return row


def solve_pattern(partition):
    missed = missed_row(partition)
    edge = {(u, v): Bool(f"e_{u}_{v}") for u, v in PAIRS}

    def e(u, v):
        if u == v:
            return False
        return edge[tuple(sorted((u, v)))]

    solver = Solver()

    # alpha(A) <= 3.
    for four in combinations(V, 4):
        solver.add(Or(*(e(u, v) for u, v in combinations(four, 2))))

    # Forbid every certificate with singleton bags y,z and paired bags c_i x_i.
    for y, z in PAIRS:
        remaining = [x for x in V if x not in (y, z)]
        for xs in permutations(remaining, 5):
            conditions = [e(y, z)]
            valid = True
            for i, x in enumerate(xs):
                if x == missed[i]:
                    valid = False
                    break
                conditions.append(Or(y != missed[i], e(y, x)))
                conditions.append(Or(z != missed[i], e(z, x)))
            if not valid:
                continue
            for i, j in combinations(range(5), 2):
                conditions.append(
                    Or(
                        xs[j] != missed[i],
                        xs[i] != missed[j],
                        e(xs[i], xs[j]),
                    )
                )
            solver.add(Not(And(*conditions)))

    result = solver.check()
    if result == sat:
        model = solver.model()
        edges = [uv for uv, var in edge.items() if bool(model.eval(var))]
        return "SAT", edges
    return str(result).upper(), None


def main():
    for partition in partitions(5):
        status, edges = solve_pattern(partition)
        print(partition, status, edges if edges is not None else "")


if __name__ == "__main__":
    main()
