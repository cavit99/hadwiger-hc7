#!/usr/bin/env python3
"""Search small atomic q=2 relative-seven web shores.

The body is a wheel.  Every rim vertex sees all three singleton labels
and one endpoint of each active pair.  We test the relative boundary
inequality and the absence of two disjoint pair carriers.
"""

from __future__ import annotations

import itertools

PAIR_LABELS = ("p0", "p1", "q0", "q1")
R = ("z0", "z1", "z2")


def is_connected(g: dict[int, set[int]], subset: frozenset[int]) -> bool:
    reached = {next(iter(subset))}
    while True:
        more = {y for x in reached for y in g[x] if y in subset}
        if more <= reached:
            return reached == set(subset)
        reached |= more


def connected_subsets(g: dict[int, set[int]]):
    vertices = tuple(g)
    for size in range(1, len(vertices) + 1):
        for subset in itertools.combinations(vertices, size):
            if is_connected(g, frozenset(subset)):
                yield frozenset(subset)


def capacity(g: dict[int, set[int]], portals: dict[str, set[int]]) -> bool:
    p_carriers = []
    q_carriers = []
    for x in connected_subsets(g):
        if x & portals["p0"] and x & portals["p1"]:
            p_carriers.append(x)
        if x & portals["q0"] and x & portals["q1"]:
            q_carriers.append(x)
    return any(not (x & y) for x in p_carriers for y in q_carriers)


def relative_min(g: dict[int, set[int]], portals: dict[str, set[int]]):
    vertices = tuple(g)
    answer = 99
    witness = None
    for size in range(1, len(vertices)):
        for xs in itertools.combinations(vertices, size):
            x = set(xs)
            internal = set().union(*(set(g[v]) for v in x)) - x
            labels = {label for label, ps in portals.items() if x & ps}
            value = len(internal) + len(labels)
            if value < answer:
                answer, witness = value, tuple(sorted(x))
    return answer, witness


def wheel(n: int) -> dict[int, set[int]]:
    # Rim vertices 0,...,n-1 and hub n.
    g = {i: set() for i in range(n + 1)}
    for i in range(n):
        for x, y in ((i, (i + 1) % n), (i, n)):
            g[x].add(y)
            g[y].add(x)
    return g


def main() -> None:
    for n in range(4, 10):
        g = wheel(n)
        found = []
        # A type chooses one p endpoint and one q endpoint.
        for types in itertools.product(range(4), repeat=n):
            portals = {label: set() for label in PAIR_LABELS + R}
            for v, t in enumerate(types):
                portals[f"p{t // 2}"].add(v)
                portals[f"q{t % 2}"].add(v)
                for z in R:
                    portals[z].add(v)
            if any(not portals[label] for label in PAIR_LABELS):
                continue
            if capacity(g, portals):
                continue
            minimum, witness = relative_min(g, portals)
            if minimum >= 8:
                found.append((types, minimum, witness))
                break
        print(n, found[:1])


if __name__ == "__main__":
    main()
