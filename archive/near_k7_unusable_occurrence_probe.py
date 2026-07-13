#!/usr/bin/env python3
"""Probe the full-SDR / unusable-occurrence residue in the near-K7 shell.

The literal core is J=K6-{ab,ac}.  Four connected dark lobes are
contracted to vertices; each sees two torso poles and all literal labels
except one named row.  We test the five canonical portal set systems in
which an SDR exists but a fixed occurrence p in P1 is used by no SDR.

This is a discovery probe.  Every returned model is independently
replayed against the literal quotient; the script does not prove that the
five portal systems exhaust the Hall classification.
"""

from __future__ import annotations

from itertools import combinations, product

from z3 import And, Bool, If, Implies, Int, Or, Solver, Sum, sat


LABELS = tuple(range(6))
LOBE_NAMES = ("D1", "D2", "D3", "D4")

# Canonical set systems.  Pole names are local to each row.
CASES = {
    "two-pq_then_pr": (("p", "s"), ("p", "q"), ("p", "q"), ("p", "r")),
    "two-pq_then_qr": (("p", "s"), ("p", "q"), ("p", "q"), ("q", "r")),
    "two-pq_then_sr": (("p", "s"), ("p", "q"), ("p", "q"), ("s", "r")),
    "two-pq_then_rt": (("p", "s"), ("p", "q"), ("p", "q"), ("r", "t")),
    "triangle_tail_double_qr": (("p", "s"), ("p", "q"), ("q", "r"), ("q", "r")),
}


def edge(u: int, v: int) -> tuple[int, int]:
    return (u, v) if u < v else (v, u)


def quotient(portals: tuple[tuple[str, str], ...], profile: tuple[int, ...]):
    pole_names = tuple(dict.fromkeys(x for pair in portals for x in pair))
    pole_index = {name: 6 + i for i, name in enumerate(pole_names)}
    lobe0 = 6 + len(pole_names)
    names = ("a", "b", "c", "r1", "r2", "r3") + pole_names + LOBE_NAMES
    edges = {
        edge(u, v)
        for u, v in combinations(LABELS, 2)
        if (u, v) not in {(0, 1), (0, 2)}
    }
    for i, (pair, miss) in enumerate(zip(portals, profile)):
        d = lobe0 + i
        edges.update(edge(d, pole_index[p]) for p in pair)
        edges.update(edge(d, x) for x in LABELS if x != miss)
    return names, edges


def connected(bag: set[int], edges: set[tuple[int, int]]) -> bool:
    reached = {next(iter(bag))}
    while True:
        expanded = reached | {
            v
            for u in reached
            for v in bag
            if edge(u, v) in edges
        }
        if expanded == reached:
            return reached == bag
        reached = expanded


def verify(bags: tuple[set[int], ...], edges: set[tuple[int, int]]) -> None:
    assert len(bags) == 7 and all(bags)
    assert sum(map(len, bags)) == len(set().union(*bags))
    assert all(connected(bag, edges) for bag in bags)
    assert all(
        any(edge(u, v) in edges for u in bags[i] for v in bags[j])
        for i in range(7)
        for j in range(i)
    )


def find_model(n: int, edges: set[tuple[int, int]]):
    adj = {v: set() for v in range(n)}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    solver = Solver()
    x = [[Bool(f"x_{v}_{b}") for b in range(7)] for v in range(n)]
    root = [[Bool(f"r_{v}_{b}") for b in range(7)] for v in range(n)]
    depth = [[Int(f"d_{v}_{b}") for b in range(7)] for v in range(n)]

    for v in range(n):
        solver.add(Sum([If(x[v][b], 1, 0) for b in range(7)]) <= 1)
    for b in range(7):
        solver.add(Sum([If(root[v][b], 1, 0) for v in range(n)]) == 1)
        for v in range(n):
            solver.add(Implies(root[v][b], And(x[v][b], depth[v][b] == 0)))
            solver.add(Implies(x[v][b], And(depth[v][b] >= 0, depth[v][b] < n)))
            parents = [And(x[u][b], depth[u][b] < depth[v][b]) for u in adj[v]]
            solver.add(Implies(And(x[v][b], depth[v][b] > 0), Or(parents)))
            solver.add(Implies(And(x[v][b], depth[v][b] == 0), root[v][b]))

    for i in range(7):
        for j in range(i):
            solver.add(Or([
                Or(And(x[u][i], x[v][j]), And(x[v][i], x[u][j]))
                for u, v in edges
            ]))

    if solver.check() != sat:
        return None
    model = solver.model()
    bags = tuple(
        {v for v in range(n) if model.evaluate(x[v][b], model_completion=True)}
        for b in range(7)
    )
    verify(bags, edges)
    return bags


def valid_for_profile(bags, portals, profile) -> bool:
    names, edges = quotient(portals, profile)
    try:
        verify(bags, edges)
        return True
    except AssertionError:
        return False


def render(bags, names) -> str:
    return " | ".join(
        "{" + ",".join(names[v] for v in sorted(bag)) + "}" for bag in bags
    )


def main() -> None:
    universe = set(product(LABELS, repeat=4))
    for case, portals in CASES.items():
        uncovered = set(universe)
        certificates = []
        while uncovered:
            profile = min(uncovered)
            names, edges = quotient(portals, profile)
            bags = find_model(len(names), edges)
            if bags is None:
                print(case, "NEGATIVE", profile)
                break
            covered = {p for p in uncovered if valid_for_profile(bags, portals, p)}
            assert covered
            uncovered -= covered
            certificates.append((profile, bags, len(covered)))
        else:
            print(case, "POSITIVE", len(certificates), "templates")
            for profile, bags, count in certificates[:3]:
                names, _ = quotient(portals, profile)
                print(" ", profile, "covers", count, render(bags, names))


if __name__ == "__main__":
    main()
