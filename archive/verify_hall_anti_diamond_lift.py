#!/usr/bin/env python3
"""Small-order audit for Proposition 3.1.

No third-party package is required.  This is only a sanity check; the
uniform proof is in hadwiger_hall_circuit_anti_diamond.md.
"""

from __future__ import annotations

from itertools import combinations


def construction(r: int, h: int):
    s = r - h + 1
    assert 2 <= h < r and s >= 2
    cset = [f"c{i}" for i in range(h - 2)]
    left = [f"l{i}" for i in range(s)]
    right = [f"r{i}" for i in range(s)]
    portals = [f"p{i}" for i in range(s)]
    vertices = cset + ["a", "b"] + portals + left + right
    edges: set[frozenset[str]] = set()

    def add(x: str, y: str) -> None:
        if x != y:
            edges.add(frozenset((x, y)))

    for x, y in combinations(cset, 2):
        add(x, y)
    for c in cset:
        for x in vertices:
            add(c, x)
    for clique in (left, right):
        for x, y in combinations(clique, 2):
            add(x, y)
    for x in left:
        add("a", x)
        for p in portals:
            add(p, x)
    for x in right:
        add("b", x)
        for p in portals:
            add(p, x)
    add("a", "b")
    add("b", left[0])
    add("a", right[0])
    return vertices, edges


def connected(vertices, edges, removed=frozenset()):
    remaining = [v for v in vertices if v not in removed]
    if len(remaining) <= 1:
        return True
    seen = {remaining[0]}
    stack = [remaining[0]]
    while stack:
        v = stack.pop()
        for w in remaining:
            if w not in seen and frozenset((v, w)) in edges:
                seen.add(w)
                stack.append(w)
    return len(seen) == len(remaining)


def connectivity(vertices, edges):
    for size in range(len(vertices)):
        for cut in combinations(vertices, size):
            if not connected(vertices, edges, frozenset(cut)):
                return size
    return len(vertices) - 1


def clique_number(vertices, edges):
    answer = 0
    for size in range(1, len(vertices) + 1):
        if any(
            all(frozenset((x, y)) in edges for x, y in combinations(q, 2))
            for q in combinations(vertices, size)
        ):
            answer = size
        else:
            break
    return answer


def colorable(vertices, edges, number_of_colors):
    neighbours = {v: set() for v in vertices}
    for edge in edges:
        x, y = tuple(edge)
        neighbours[x].add(y)
        neighbours[y].add(x)
    colour: dict[str, int] = {}

    def search():
        if len(colour) == len(vertices):
            return True
        v = max(
            (x for x in vertices if x not in colour),
            key=lambda x: sum(y in colour for y in neighbours[x]),
        )
        forbidden = {colour[y] for y in neighbours[v] if y in colour}
        for c in range(number_of_colors):
            if c not in forbidden:
                colour[v] = c
                if search():
                    return True
                del colour[v]
        return False

    return search()


def main() -> None:
    cases = ((3, 2), (4, 2), (4, 3), (5, 3), (5, 4))
    for r, h in cases:
        vertices, edges = construction(r, h)
        kappa = connectivity(vertices, edges)
        omega = clique_number(vertices, edges)
        has_r_coloring = colorable(vertices, edges, r)
        assert kappa == r + 1, (r, h, kappa)
        assert omega == r, (r, h, omega)
        assert not has_r_coloring, (r, h)
        print(
            f"PASS r={r} h={h}: n={len(vertices)}, "
            f"kappa={kappa}, omega={omega}, r-colourable={has_r_coloring}"
        )


if __name__ == "__main__":
    main()
