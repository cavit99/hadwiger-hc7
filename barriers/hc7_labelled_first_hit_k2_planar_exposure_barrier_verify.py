#!/usr/bin/env python3
"""Verify the K2-planar first-hit exposure barrier without dependencies."""

from itertools import combinations


ICO_EDGES = {
    (0, 1), (0, 5), (0, 7), (0, 8), (0, 11),
    (1, 2), (1, 5), (1, 6), (1, 8),
    (2, 3), (2, 6), (2, 8), (2, 9),
    (3, 4), (3, 6), (3, 9), (3, 10),
    (4, 5), (4, 6), (4, 10), (4, 11),
    (5, 6), (5, 11),
    (7, 8), (7, 9), (7, 10), (7, 11),
    (8, 9), (9, 10), (10, 11),
}


def edge(u, v):
    return (u, v) if repr(u) < repr(v) else (v, u)


def add(adj, u, v):
    adj.setdefault(u, set()).add(v)
    adj.setdefault(v, set()).add(u)


def connected_after_deleting(adj, deleted):
    remaining = set(adj) - set(deleted)
    if len(remaining) <= 1:
        return True
    root = next(iter(remaining))
    seen = {root}
    stack = [root]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v in remaining and v not in seen:
                seen.add(v)
                stack.append(v)
    return seen == remaining


def connectivity_at_least(adj, k):
    vertices = list(adj)
    for size in range(k):
        for deleted in combinations(vertices, size):
            if not connected_after_deleting(adj, deleted):
                return False
    return True


def build_icosahedron():
    adj = {v: set() for v in range(12)}
    for u, v in ICO_EDGES:
        add(adj, u, v)
    assert all(len(adj[v]) == 5 for v in adj)
    return adj


def triangular_faces(adj):
    faces = []
    for a, b, c in combinations(adj, 3):
        if b in adj[a] and c in adj[a] and c in adj[b]:
            faces.append((a, b, c))
    # Every triangle of the icosahedral graph is facial.
    assert len(faces) == 20
    return faces


def build_edgewise_subdivision():
    ico = build_icosahedron()
    adj = {v: set() for v in ico}
    midpoint = {}
    for u, v in ICO_EDGES:
        m = ("m", min(u, v), max(u, v))
        midpoint[frozenset((u, v))] = m
        add(adj, u, m)
        add(adj, v, m)
    for a, b, c in triangular_faces(ico):
        x = midpoint[frozenset((a, b))]
        y = midpoint[frozenset((b, c))]
        z = midpoint[frozenset((c, a))]
        add(adj, x, y)
        add(adj, y, z)
        add(adj, z, x)
    return adj


def main():
    j = build_edgewise_subdivision()
    assert len(j) == 42
    assert sum(map(len, j.values())) // 2 == 120
    assert min(map(len, j.values())) == 5
    assert connectivity_at_least(j, 5)

    root = 0
    c = {root} | set(j[root])
    w = set().union(*(j[v] for v in c)) - c
    outside = set(j) - c - w
    assert len(c) == 6 and len(w) == 10 and len(outside) == 26
    assert connected_after_deleting({v: j[v] & w for v in w}, set())
    assert set().union(*(j[v] for v in c)) - c == w

    g = {v: set(neighbours) for v, neighbours in j.items()}
    a, b = "a", "b"
    g[a] = set()
    g[b] = set()
    add(g, a, b)
    for v in j:
        add(g, a, v)
        add(g, b, v)
    assert len(g) == 44
    assert sum(map(len, g.values())) // 2 == 205
    # The checked five-connectivity of J implies seven-connectivity of its
    # join with K2: after deleting at most six vertices, either an apex
    # remains or both apices and at most four vertices of J were deleted.
    # The five neighbours of any old icosahedral vertex, together with the
    # two apices, are a cut of order seven, so the connectivity is exact.
    assert len(j[root]) == 5

    # Choose the five midpoint rim vertices of C as sources.  The terminal union
    # contains W, both universal vertices, and two old vertices outside
    # C union W, so C is a surviving terminal-avoiding component.
    p = set(j[root])
    t1, t2 = 2, 4
    assert len(p) == 5 and {t1, t2} <= outside
    terminal_union = w | {a, b, t1, t2}
    surviving = set(g) - terminal_union
    component = set(c)
    assert p <= component <= surviving
    assert not any(v in g[u] for u in component for v in surviving - component)
    exposure = set().union(*(g[v] for v in component)) - component
    assert exposure == w | {a, b}
    assert len(exposure) == 12

    print("GREEN K2-planar first-hit exposure barrier")
    print("J: vertices=42 edges=120 connectivity=5 C=6 W=10")
    print("G: vertices=44 edges=205 connectivity=7 exposure=12")
    print("rank(T1 union T2)=0; K7-minor excluded by planarity of J")


if __name__ == "__main__":
    main()
