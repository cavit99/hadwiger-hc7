#!/usr/bin/env python3
"""Random/exhaustive-pattern search for the degree-nine paired-bag lemma.

Rows are seven exterior components, columns are nine boundary vertices.  Each
row misses two columns.  We seek an injection f with f(i) outside row i's
missed pair and with no mutually missed pair of representatives.  Such an f
gives seven pairwise adjacent connected bags {C_i,f(i)} and hence a K7 minor.
"""

from itertools import combinations
from random import Random
import sys


V = tuple(range(9))
PAIRS = tuple(combinations(V, 2))


def certificate(missed):
    order = sorted(range(7), key=lambda i: -sum(i in m for m in missed))
    chosen = [-1] * 7
    used = set()

    def rec(pos):
        if pos == 7:
            return tuple(chosen)
        i = order[pos]
        for x in V:
            if x in used or x in missed[i]:
                continue
            good = True
            for j, y in enumerate(chosen):
                if y < 0:
                    continue
                if y in missed[i] and x in missed[j]:
                    good = False
                    break
            if not good:
                continue
            chosen[i] = x
            used.add(x)
            answer = rec(pos + 1)
            if answer is not None:
                return answer
            used.remove(x)
            chosen[i] = -1
        return None

    return rec(0)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "sat":
        symbolic_search()
        return
    rng = Random(20260711)
    worst = None
    for trial in range(200_000):
        missed = tuple(rng.choice(PAIRS) for _ in range(7))
        cert = certificate(missed)
        if cert is None:
            print("COUNTEREXAMPLE", missed)
            return
        if trial % 20_000 == 0:
            print("checked", trial)
        worst = (missed, cert)
    print("NO_RANDOM_COUNTEREXAMPLE", worst)


def symbolic_search():
    from itertools import permutations
    from z3 import And, Bool, Or, PbEq, Solver, sat

    miss = [[Bool(f"m_{i}_{x}") for x in V] for i in range(7)]
    solver = Solver()
    for i in range(7):
        solver.add(PbEq([(miss[i][x], 1) for x in V], 2))
    # Column symmetry fixes the first missed pair.
    solver.add(miss[0][0], miss[0][1])
    for x in range(2, 9):
        solver.add(~miss[0][x])

    count = 0
    for xs in permutations(V, 7):
        failures = [miss[i][xs[i]] for i in range(7)]
        failures.extend(
            And(miss[i][xs[j]], miss[j][xs[i]])
            for i, j in combinations(range(7), 2)
        )
        solver.add(Or(*failures))
        count += 1
    print("constraints", count)
    result = solver.check()
    print(result)
    if result == sat:
        model = solver.model()
        rows = []
        for i in range(7):
            rows.append(tuple(x for x in V if bool(model.eval(miss[i][x]))))
        print(rows, certificate(rows))


if __name__ == "__main__":
    main()
