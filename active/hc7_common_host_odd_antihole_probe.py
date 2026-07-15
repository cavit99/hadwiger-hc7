#!/usr/bin/env python3
"""Deterministic q=6 certificates for the common-host odd-antihole barrier."""

from itertools import combinations


Q = 6
N = 2 * Q + 1
VERTICES = tuple(range(N))
E = frozenset((1, 12))
F = frozenset((0, 11))


def pair(u: int, v: int) -> frozenset[int]:
    return frozenset((u, v))


def complement_cycle_edges() -> set[frozenset[int]]:
    edges: set[frozenset[int]] = set()
    for u, v in combinations(VERTICES, 2):
        if (u - v) % N not in (1, N - 1):
            edges.add(pair(u, v))
    return edges


G = complement_cycle_edges()
H = G - {E, F}


def adjacent(edges: set[frozenset[int]], u: int, v: int) -> bool:
    return pair(u, v) in edges


def independent(edges: set[frozenset[int]], vertices: set[int]) -> bool:
    return all(not adjacent(edges, u, v) for u, v in combinations(vertices, 2))


def clique(edges: set[frozenset[int]], vertices: set[int]) -> bool:
    return all(adjacent(edges, u, v) for u, v in combinations(vertices, 2))


def connected(edges: set[frozenset[int]], vertices: set[int]) -> bool:
    if len(vertices) <= 1:
        return True
    reached = {next(iter(vertices))}
    while True:
        expanded = reached | {
            v
            for v in vertices - reached
            if any(adjacent(edges, u, v) for u in reached)
        }
        if expanded == reached:
            return reached == vertices
        reached = expanded


def valid_colouring(
    edges: set[frozenset[int]], classes: tuple[frozenset[int], ...]
) -> bool:
    if set().union(*map(set, classes)) != set(VERTICES):
        return False
    if sum(map(len, classes)) != N:
        return False
    return all(independent(edges, set(colour_class)) for colour_class in classes)


def colourable(
    edges: set[frozenset[int]],
    colours: int,
    equalities: tuple[tuple[int, int], ...] = (),
    vertices: tuple[int, ...] = VERTICES,
) -> bool:
    """Small deterministic DSATUR search, with optional forced equalities."""

    parent = {v: v for v in vertices}

    def find(v: int) -> int:
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    def union(u: int, v: int) -> None:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[rv] = ru

    for u, v in equalities:
        union(u, v)

    for edge in edges:
        u, v = tuple(edge)
        if u in parent and v in parent and find(u) == find(v):
            return False

    groups: dict[int, set[int]] = {}
    for v in vertices:
        groups.setdefault(find(v), set()).add(v)
    nodes = tuple(groups)
    graph = {node: set() for node in nodes}
    for edge in edges:
        u, v = tuple(edge)
        if u not in parent or v not in parent:
            continue
        ru, rv = find(u), find(v)
        if ru != rv:
            graph[ru].add(rv)
            graph[rv].add(ru)

    assigned: dict[int, int] = {}

    def search() -> bool:
        if len(assigned) == len(nodes):
            return True
        node = max(
            (x for x in nodes if x not in assigned),
            key=lambda x: (
                len({assigned[y] for y in graph[x] if y in assigned}),
                len(graph[x]),
                -x,
            ),
        )
        forbidden = {assigned[y] for y in graph[node] if y in assigned}
        for colour in range(colours):
            if colour in forbidden:
                continue
            assigned[node] = colour
            if search():
                return True
            del assigned[node]
        return False

    return search()


def valid_model(
    edges: set[frozenset[int]], bags: tuple[frozenset[int], ...]
) -> bool:
    if set().union(*map(set, bags)) != set(VERTICES):
        return False
    if sum(map(len, bags)) != N:
        return False
    if not all(connected(edges, set(bag)) for bag in bags):
        return False
    return all(
        any(adjacent(edges, u, v) for u in bags[i] for v in bags[j])
        for i, j in combinations(range(len(bags)), 2)
    )


def contracted_edges(
    edges: set[frozenset[int]],
    u: int,
    v: int,
    new: int,
    vertices: set[int] | None = None,
) -> tuple[set[int], set[frozenset[int]]]:
    source_vertices = set(VERTICES) if vertices is None else set(vertices)
    result_vertices = (source_vertices - {u, v}) | {new}
    result: set[frozenset[int]] = set()
    for edge in edges:
        x, y = tuple(edge)
        x = new if x in (u, v) else x
        y = new if y in (u, v) else y
        if x != y:
            result.add(pair(x, y))
    return result_vertices, result


def main() -> None:
    assert E in G and F in G and E.isdisjoint(F)
    assert pair(0, 1) not in G
    assert pair(0, 12) not in G
    assert pair(11, 12) not in G

    colouring_g_minus_e = (
        frozenset((0, 1, 12)),
        frozenset((2, 3)),
        frozenset((4, 5)),
        frozenset((6, 7)),
        frozenset((8, 9)),
        frozenset((10, 11)),
    )
    colouring_g_minus_f = (
        frozenset((0, 11, 12)),
        frozenset((1, 2)),
        frozenset((3, 4)),
        frozenset((5, 6)),
        frozenset((7, 8)),
        frozenset((9, 10)),
    )
    assert valid_colouring(G - {E}, colouring_g_minus_e)
    assert valid_colouring(G - {F}, colouring_g_minus_f)
    assert not colourable(G, 6)
    assert not colourable(H, 5)
    assert colourable(H, 6)

    independent_triples = {
        frozenset(vertices)
        for vertices in combinations(VERTICES, 3)
        if independent(H, set(vertices))
    }
    assert independent_triples == {
        frozenset((0, 1, 12)),
        frozenset((0, 11, 12)),
    }
    assert not colourable(H, 6, equalities=((1, 12), (0, 11)))

    after_e_vertices, after_e = contracted_edges(G, 1, 12, 13)
    double_vertices, double_contraction = contracted_edges(
        after_e, 0, 11, 14, after_e_vertices
    )
    assert not colourable(
        double_contraction, 6, vertices=tuple(sorted(double_vertices))
    )

    for removed_order in range(10):
        for removed in combinations(VERTICES, removed_order):
            assert connected(G, set(VERTICES) - set(removed))
    assert not connected(G, {0, 1, 2})

    for deleted in combinations(VERTICES, 2):
        remaining = set(VERTICES) - set(deleted)
        assert any(clique(G, set(candidate)) for candidate in combinations(remaining, 6))

    spanning_k6 = (
        frozenset((1, 2, 9)),
        frozenset((8, 12)),
        frozenset((0,)),
        frozenset((6, 11)),
        frozenset((3, 10)),
        frozenset((4, 5, 7)),
    )
    assert valid_model(H, spanning_k6)
    endpoint_rows = {
        endpoint: row
        for row, bag in enumerate(spanning_k6)
        for endpoint in bag & {0, 1, 11, 12}
    }
    assert len(set(endpoint_rows.values())) == 4

    k7_model = (
        frozenset((0,)),
        frozenset((2,)),
        frozenset((4,)),
        frozenset((6,)),
        frozenset((8,)),
        frozenset((10,)),
        frozenset((1, 3, 5, 7, 9, 11, 12)),
    )
    assert valid_model(H, k7_model)

    contracted_vertices, contraction = contracted_edges(G, 0, 3, 13)
    contraction_k7 = {13, 1, 4, 6, 8, 10, 12}
    assert contraction_k7 <= contracted_vertices
    assert clique(contraction, contraction_k7)

    print("GREEN common_host_odd_antihole q=6")
    print("chi(G)=7; chi(H)=chi(G-e)=chi(G-f)=6")
    print("kappa(G)=10; simultaneous_equal_equal=false; chi(G/e/f)>6")
    print("spanning_K6_named_rows=4; fixed_pair_K5_transversal=none")
    print("K7_model_in_H=true; K7_subgraph_in_G_contract_03=true")


if __name__ == "__main__":
    main()
