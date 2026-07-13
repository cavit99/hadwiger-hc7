#!/usr/bin/env python3
"""Local SAT probe for how many pure-Moser degree-7 centres one
degree-9 vertex can serve as the distinguished four-contact hub.

This is a falsification/structure probe, not a proof certificate.
"""

from itertools import combinations
import sys

from z3 import And, Bool, If, Implies, Not, Or, Solver, Sum, sat


N = 9
V = range(N)


def edge_var(i, j):
    if i == j:
        return False
    if i > j:
        i, j = j, i
    return edges[i, j]


edges = {(i, j): Bool(f"e_{i}_{j}") for i, j in combinations(V, 2)}
marked = [Bool(f"m_{i}") for i in V]
s = Solver()
forbid_two_pair_domination = "--forbid-two-pair-domination" in sys.argv

# Dirac's local bound for a degree-nine vertex in the HC7 setting.
for five in combinations(V, 5):
    s.add(Or(*[edge_var(i, j) for i, j in combinations(five, 2)]))

# A K6 in the neighbourhood together with the hub is a K7 subgraph.
for six in combinations(V, 6):
    s.add(Or(*[~edge_var(i, j) for i, j in combinations(six, 2)]))

# A marked vertex is a degree-seven pure-Moser centre for which the
# ambient degree-nine vertex is label 0.  It has four common neighbours,
# and those four induce exactly 2K2.
for i in V:
    neigh = [edge_var(i, j) for j in V if j != i]
    s.add(Implies(marked[i], Sum([If(x, 1, 0) for x in neigh]) == 4))
    for j in V:
        if j == i:
            continue
        common_edges = [
            If(edge_var(i, k) & edge_var(j, k), 1, 0)
            for k in V
            if k not in (i, j)
        ]
        s.add(
            Implies(
                marked[i] & edge_var(i, j),
                Sum(common_edges) == 1,
            )
        )
    if forbid_two_pair_domination:
        failures = []
        for a, b in combinations([x for x in V if x != i], 2):
            for e in V:
                if e in (i, a, b):
                    continue
                failures.append(
                    And(
                        edge_var(i, a),
                        edge_var(i, b),
                        edge_var(a, b),
                        Not(edge_var(i, e)),
                        Not(edge_var(a, e)),
                        Not(edge_var(b, e)),
                    )
                )
        s.add(Implies(marked[i], Or(*failures)))

for target in range(N, -1, -1):
    s.push()
    s.add(Sum([If(x, 1, 0) for x in marked]) >= target)
    if s.check() == sat:
        model = s.model()
        M = [i for i in V if model.eval(marked[i])]
        E = [ij for ij, x in edges.items() if model.eval(x)]
        print("maximum-mark lower witness:", len(M))
        print("marked:", M)
        print("edges:", E)
        for i in M:
            W = [j for j in V if j != i and model.eval(edge_var(i, j))]
            print(i, "neighbours", W)
        break
    s.pop()
