#!/usr/bin/env python3
"""Verify the connected-shore common-portal response barrier."""

from __future__ import annotations

from itertools import combinations, product


S = ("d", "e", "p1", "p2", "p3", "r1", "r2", "r3")
P = frozenset(("p1", "p2", "p3"))
R = frozenset(("r1", "r2", "r3"))
H = frozenset(("a", "b", "c"))
V = frozenset(S) | H


def pair(x: str, y: str) -> frozenset[str]:
    return frozenset((x, y))


EDGES = {
    pair(x, y)
    for triangle in (("d", "p1", "r1"), ("e", "p2", "r2"))
    for x, y in combinations(triangle, 2)
}
EDGES |= {pair(x, y) for x, y in combinations(H, 2)}
EDGES |= {pair(h, s) for h in H for s in S}


def proper(colouring: dict[str, int]) -> bool:
    return all(colouring[x] != colouring[y] for x, y in map(tuple, EDGES))


def extends(equal_roots: bool) -> bool:
    # Fix colour names on the prescribed blocks; every colouring with the
    # same equality partition is equivalent up to a permutation.
    fixed = {**{p: 0 for p in P}, **{r: 1 for r in R}, "d": 2}
    fixed["e"] = 2 if equal_roots else 3
    for colours in product(range(6), repeat=3):
        colouring = {**fixed, **dict(zip(sorted(H), colours))}
        if proper(colouring):
            return True
    return False


def main() -> None:
    assert pair("d", "e") not in EDGES
    assert not any(pair(x, y) in EDGES for x, y in combinations(P, 2))
    assert not any(pair(x, y) in EDGES for x, y in combinations(R, 2))
    assert pair("p1", "r1") in EDGES
    assert all(any(pair(root, x) in EDGES for x in block) for root in ("d", "e") for block in (P, R))

    for h in H:
        assert all(pair(h, s) in EDGES for s in S)
    assert {h for h in ("b",) if pair("d", h) in EDGES} == {"b"}
    assert {h for h in ("b",) if pair("e", h) in EDGES} == {"b"}

    assert extends(True)
    assert not extends(False)

    clique6 = H | frozenset(("d", "p1", "r1"))
    assert len(clique6) == 6
    assert all(pair(x, y) in EDGES for x, y in combinations(clique6, 2))

    # Eliminating the boundary first and then the full triangle has width
    # five.  The fill computation is retained explicitly rather than using
    # a heuristic treewidth routine.
    graph = {v: {w for w in V if pair(v, w) in EDGES} for v in V}
    alive = set(V)
    width = 0
    for vertex in S + tuple(sorted(H)):
        later = graph[vertex] & alive
        width = max(width, len(later))
        for x, y in combinations(later, 2):
            graph[x].add(y)
            graph[y].add(x)
        alive.remove(vertex)
    assert width == 5

    # Derive the boundary components from the constructed edge set.
    remaining = set(S)
    boundary_components = []
    while remaining:
        component = {remaining.pop()}
        frontier = list(component)
        while frontier:
            vertex = frontier.pop()
            neighbours = {
                other
                for other in remaining
                if pair(vertex, other) in EDGES
            }
            remaining -= neighbours
            component |= neighbours
            frontier.extend(neighbours)
        boundary_components.append(frozenset(component))
    assert sorted(map(len, boundary_components)) == [1, 1, 3, 3]

    print("GREEN connected-shore common-portal barrier")
    print("closed shore: K3 join (2K3 plus 2K1), chromatic number 6")
    print("responses: equality=yes unequal=no")
    print("minor scope: elimination width 5; every minor is six-colourable")
    print("trust boundary: not seven-connected or contraction-critical")


if __name__ == "__main__":
    main()
