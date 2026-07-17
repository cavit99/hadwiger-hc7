#!/usr/bin/env python3
"""Verify the named-model Gallai--Edmonds transversal barrier.

The script checks the edge list, the two support-six K5 models, the full
two-shore interface, the Gallai--Edmonds decomposition by exhaustive
maximum matching, and the displayed width-five elimination certificate.
It has no third-party dependencies.
"""

from functools import lru_cache


N = 12
EDGES = {
    (0, 1), (0, 8), (0, 10),
    (1, 4), (1, 7), (1, 9), (1, 10),
    (2, 5), (2, 6), (2, 7), (2, 8), (2, 10),
    (3, 5), (3, 6), (3, 7), (3, 8), (3, 10), (3, 11),
    (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10),
    (5, 6), (5, 7), (5, 8), (5, 11),
    (6, 7), (6, 9), (6, 10), (6, 11),
    (7, 8), (7, 9), (7, 10),
    (8, 9), (10, 11),
}


def adjacency(n: int, edges: set[tuple[int, int]]) -> tuple[int, ...]:
    out = [0] * n
    for u, v in edges:
        assert 0 <= u < v < n
        out[u] |= 1 << v
        out[v] |= 1 << u
    return tuple(out)


ADJ = adjacency(N, EDGES)


def is_clique(vertices: tuple[int, ...]) -> bool:
    return all((ADJ[u] >> v) & 1 for i, u in enumerate(vertices)
               for v in vertices[i + 1:])


def verify_model(core: tuple[int, ...], edge: tuple[int, int]) -> None:
    assert is_clique(core)
    u, v = edge
    assert (ADJ[u] >> v) & 1
    assert set(core).isdisjoint(edge)
    assert all(((ADJ[u] | ADJ[v]) >> q) & 1 for q in core)


def maximum_matching_size(adj: tuple[int, ...], mask: int) -> int:
    @lru_cache(None)
    def rec(active: int) -> int:
        if not active:
            return 0
        bit = active & -active
        v = bit.bit_length() - 1
        best = rec(active ^ bit)
        neighbours = adj[v] & active
        while neighbours:
            mate = neighbours & -neighbours
            neighbours ^= mate
            best = max(best, 1 + rec(active ^ bit ^ mate))
        return best

    return rec(mask)


def verify_gallai_edmonds() -> None:
    boundary = range(8)
    complement_edges = {
        (u, v)
        for u in boundary
        for v in boundary
        if u < v and not ((ADJ[u] >> v) & 1)
    }
    comp = adjacency(8, complement_edges)
    full = (1 << 8) - 1
    nu = maximum_matching_size(comp, full)
    assert nu == 3
    d_set = {
        v for v in boundary
        if maximum_matching_size(comp, full ^ (1 << v)) == nu
    }
    a_set = {
        w for v in d_set for w in boundary
        if ((comp[v] >> w) & 1) and w not in d_set
    }
    c_set = set(boundary) - d_set - a_set
    assert d_set == {2, 3, 4, 5, 6, 7}
    assert a_set == {0, 1}
    assert c_set == set()


def verify_width_five() -> None:
    order = [0, 11, 1, 2, 3, 5, 4, 6, 7, 8, 9, 10]
    adj = list(ADJ)
    active = (1 << N) - 1
    maximum = 0
    for v in order:
        neighbours = adj[v] & active & ~(1 << v)
        maximum = max(maximum, neighbours.bit_count())
        vertices = [u for u in range(N) if (neighbours >> u) & 1]
        for i, u in enumerate(vertices):
            for w in vertices[i + 1:]:
                adj[u] |= 1 << w
                adj[w] |= 1 << u
        active ^= 1 << v
        for u in range(N):
            adj[u] &= active
    assert maximum == 5


def main() -> None:
    s = set(range(8))
    c = {8, 9}
    d = {10, 11}
    assert (8, 9) in EDGES and (10, 11) in EDGES
    assert all(not ((ADJ[u] >> v) & 1) for u in c for v in d)
    assert all(any((ADJ[s0] >> v) & 1 for v in c) for s0 in s)
    assert all(any((ADJ[s0] >> v) & 1 for v in d) for s0 in s)

    verify_model((4, 7, 8, 9), (0, 1))
    verify_model((3, 6, 10, 11), (2, 5))
    assert {0, 1, 4, 7, 8, 9}.isdisjoint({2, 3, 5, 6, 10, 11})
    assert {0, 1}.isdisjoint({2, 3, 5, 6, 10, 11})

    verify_gallai_edmonds()
    verify_width_five()
    print("GREEN: named-model Gallai--Edmonds transversal barrier verified")


if __name__ == "__main__":
    main()
