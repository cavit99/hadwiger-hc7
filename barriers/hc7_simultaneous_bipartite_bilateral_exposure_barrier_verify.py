#!/usr/bin/env python3
"""Verify the simultaneous bipartite bilateral-exposure barrier."""

from __future__ import annotations

from itertools import combinations


def edge(u: object, v: object) -> frozenset[object]:
    assert u != v
    return frozenset((u, v))


def graph6_edges(code: str) -> tuple[set[int], set[frozenset[int]]]:
    n = ord(code[0]) - 63
    assert 0 <= n <= 62
    bits = "".join(f"{ord(char) - 63:06b}" for char in code[1:])
    pairs = [(i, j) for j in range(1, n) for i in range(j)]
    edges = {edge(i, j) for (i, j), bit in zip(pairs, bits) if bit == "1"}
    return set(range(n)), edges


def adjacency(vertices: set[object], edges: set[frozenset[object]]) -> dict[object, set[object]]:
    adj = {v: set() for v in vertices}
    for e in edges:
        u, v = tuple(e)
        adj[u].add(v)
        adj[v].add(u)
    return adj


def connected(vertices: set[object], edges: set[frozenset[object]]) -> bool:
    if not vertices:
        return False
    adj = adjacency(vertices, {e for e in edges if e <= vertices})
    start = next(iter(vertices))
    seen = {start}
    stack = [start]
    while stack:
        v = stack.pop()
        for w in adj[v] - seen:
            seen.add(w)
            stack.append(w)
    return seen == vertices


def colourable(vertices: set[object], edges: set[frozenset[object]], k: int) -> bool:
    adj = adjacency(vertices, {e for e in edges if e <= vertices})
    colours: dict[object, int] = {}

    def search() -> bool:
        if len(colours) == len(vertices):
            return True
        uncoloured = vertices - colours.keys()
        v = max(
            uncoloured,
            key=lambda x: (len({colours[y] for y in adj[x] if y in colours}), len(adj[x])),
        )
        forbidden = {colours[y] for y in adj[v] if y in colours}
        for c in range(k):
            if c not in forbidden:
                colours[v] = c
                if search():
                    return True
                del colours[v]
        return False

    return search()


def chromatic_number(vertices: set[object], edges: set[frozenset[object]]) -> int:
    for k in range(1, len(vertices) + 1):
        if colourable(vertices, edges, k):
            return k
    raise AssertionError("unreachable")


def vertex_connectivity(vertices: set[object], edges: set[frozenset[object]]) -> int:
    ordered = sorted(vertices, key=str)
    for size in range(len(vertices)):
        for cut in combinations(ordered, size):
            remainder = vertices - set(cut)
            if len(remainder) >= 2 and not connected(remainder, edges):
                return size
    return len(vertices) - 1


def quotient(
    vertices: set[object],
    edges: set[frozenset[object]],
    mapping: dict[object, object],
) -> tuple[set[object], set[frozenset[object]]]:
    image = {mapping.get(v, v) for v in vertices}
    image_edges: set[frozenset[object]] = set()
    for e in edges:
        u, v = tuple(e)
        u2, v2 = mapping.get(u, u), mapping.get(v, v)
        if u2 != v2:
            image_edges.add(edge(u2, v2))
    return image, image_edges


def proper_colouring(edges: set[frozenset[object]], colouring: dict[object, int]) -> bool:
    return all(colouring[u] != colouring[v] for u, v in map(tuple, edges))


def list_colourable(
    vertices: set[object],
    edges: set[frozenset[object]],
    lists: dict[object, set[int]],
) -> bool:
    ordered = sorted(vertices, key=lambda v: len(lists[v]))
    colours: dict[object, int] = {}

    def search(i: int) -> bool:
        if i == len(ordered):
            return True
        v = ordered[i]
        for c in lists[v]:
            if all(
                colours.get(w) != c
                for w in vertices
                if w != v and edge(v, w) in edges
            ):
                colours[v] = c
                if search(i + 1):
                    return True
                del colours[v]
        return False

    return search(0)


def check_model(edges: set[frozenset[object]], bags: list[set[object]]) -> None:
    assert all(bags)
    assert sum(map(len, bags)) == len(set().union(*bags))
    for bag in bags:
        assert connected(bag, edges)
    for a, b in combinations(bags, 2):
        assert any(edge(x, y) in edges for x in a for y in b)


def main() -> None:
    vertices, edges = graph6_edges("GCxvvg")
    expected = {
        edge(0, 3), edge(0, 4), edge(0, 6), edge(0, 7),
        edge(1, 4), edge(1, 5), edge(1, 6), edge(1, 7),
        edge(2, 4), edge(2, 5), edge(2, 6), edge(2, 7),
        edge(3, 5), edge(3, 6), edge(3, 7), edge(4, 6), edge(5, 7),
    }
    assert edges == expected
    x_side, y_side = {4, 6}, {5, 7}
    assert edge(4, 6) in edges and edge(5, 7) in edges
    assert all(edge(x, y) not in edges for x in x_side for y in y_side)

    q_vertices, q_edges = quotient(vertices, edges, {4: "X", 6: "X", 5: "Y", 7: "Y"})
    expected_q_edges = {edge(root, v) for root in ("X", "Y") for v in range(4)}
    expected_q_edges.add(edge(0, 3))
    assert q_edges == expected_q_edges
    q_colouring = {"X": 0, "Y": 0, 0: 1, 1: 1, 2: 1, 3: 2}
    assert proper_colouring(q_edges, q_colouring)

    palette = {0, 1, 2}
    outside = {0, 1, 2, 3}
    adj = adjacency(vertices, edges)
    lists = {
        v: palette - {q_colouring[w] for w in adj[v] & outside}
        for v in x_side | y_side
    }
    assert lists == {4: {0, 2}, 6: {0}, 5: {0}, 7: {0}}
    assert list_colourable(x_side, edges, lists)
    assert not list_colourable(y_side, edges, lists)

    assert chromatic_number(vertices, edges) == 4
    assert vertex_connectivity(vertices, edges) == 4
    check_model(edges, [{0}, {3}, {1, 4, 5}, {6}])

    triangle = {8, 9, 10}
    join_vertices = vertices | triangle
    join_edges = set(edges)
    join_edges |= {edge(a, b) for a, b in combinations(triangle, 2)}
    join_edges |= {edge(a, b) for a in triangle for b in vertices}
    assert chromatic_number(join_vertices, join_edges) == 7
    assert vertex_connectivity(join_vertices, join_edges) == 7

    jq_vertices, jq_edges = quotient(
        join_vertices,
        join_edges,
        {4: "X", 6: "X", 5: "Y", 7: "Y"},
    )
    assert chromatic_number(jq_vertices, jq_edges) == 6
    check_model(join_edges, [{8}, {9}, {10}, {0}, {3}, {1, 4, 5}, {6}])
    assert chromatic_number(join_vertices - {1}, join_edges) == 7

    print("GREEN simultaneous_bipartite_bilateral_exposure_barrier")
    print("chi(F)=4; kappa(F)=4; chi(K3 join F)=7; kappa(K3 join F)=7")
    print("chi(double quotient)=6; X_lists=colourable; Y_lists=uncolourable")
    print("K7_model=true; joined_host_vertex_minimal=false")


if __name__ == "__main__":
    main()
