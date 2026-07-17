#!/usr/bin/env python3
"""Falsification probe for a bridge-bearing shore at the star order-eight boundary.

The quotient has boundary R (a triangle), two anticomplete edges e,f, and
one further vertex x.  One shore is contracted to a universal boundary
vertex z.  The other shore is split across a bridge into vertices p,q;
each of p,q contacts at least six boundary vertices and together they
contact all eight.  Only the boundary edges forced by the normalized
star interface are included.  A survivor is a guardrail, not an HC7
counterexample.
"""

from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "boundary_join_probe", HERE / "hc7_boundary_join_probe.py"
)
assert spec and spec.loader
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)


R = (0, 1, 2)
E = (3, 4)
F = (5, 6)
X = 7
P, Q, Z = 8, 9, 10
S = tuple(range(8))


def add_edge(adj: list[int], u: int, v: int) -> None:
    adj[u] |= 1 << v
    adj[v] |= 1 << u


def quotient(e_choices: tuple[int, ...], f_choices: tuple[int, ...],
             miss_p: tuple[int, int], miss_q: tuple[int, int]) -> tuple[int, ...]:
    adj = [0] * 11
    for u, v in itertools.combinations(R, 2):
        add_edge(adj, u, v)
    add_edge(adj, *E)
    add_edge(adj, *F)
    for r, endpoint in zip(R, e_choices):
        add_edge(adj, r, endpoint)
    for r, endpoint in zip(R, f_choices):
        add_edge(adj, r, endpoint)
    add_edge(adj, P, Q)
    for s in S:
        add_edge(adj, Z, s)
        if s not in miss_p:
            add_edge(adj, P, s)
        if s not in miss_q:
            add_edge(adj, Q, s)
    return tuple(adj)


def edge_list(adj: tuple[int, ...]) -> list[tuple[int, int]]:
    return [(u, v) for u in range(len(adj)) for v in range(u + 1, len(adj))
            if (adj[u] >> v) & 1]


def main() -> None:
    tested = 0
    for e_choices in itertools.product(E, repeat=3):
        for f_choices in itertools.product(F, repeat=3):
            for miss_p in itertools.combinations(S, 2):
                for miss_q in itertools.combinations(S, 2):
                    if set(miss_p) & set(miss_q):
                        continue
                    tested += 1
                    g = quotient(e_choices, f_choices, miss_p, miss_q)
                    if not probe.has_k7_minor(g):
                        print("SURVIVOR")
                        print("e_choices", e_choices)
                        print("f_choices", f_choices)
                        print("miss_p", miss_p, "miss_q", miss_q)
                        print("edges", edge_list(g))
                        print("tested", tested)
                        return
    print("NO_SURVIVOR", tested)


if __name__ == "__main__":
    main()
