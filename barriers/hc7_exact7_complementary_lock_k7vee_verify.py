#!/usr/bin/env python3
"""Verify the complementary-lock quotient has no K6 minor.

Every connected six-bag minor is represented by a spanning forest of its
bags together with the unused vertices.  The graph has twelve vertices, so
at most six forest edges are needed.  No third-party package is required.
"""

from __future__ import annotations

from itertools import combinations


NAMES = (
    "c",
    "a1",
    "t1",
    "a2",
    "t2",
    "a3",
    "t3",
    "D",
    "E",
    "x",
    "y",
    "Q",
)
INDEX = {name: index for index, name in enumerate(NAMES)}
ORDER = len(NAMES)


def edge(left: str, right: str) -> tuple[int, int]:
    u, v = INDEX[left], INDEX[right]
    return (u, v) if u < v else (v, u)


BOUNDARY_EDGES = (
    edge("c", "a1"),
    edge("c", "a2"),
    edge("c", "a3"),
    edge("a1", "a2"),
    edge("a1", "a3"),
    edge("a2", "t3"),
)

EDGES = tuple(
    sorted(
        set(BOUNDARY_EDGES)
        | {edge("D", name) for name in ("x", "y", "c", "t1", "t2", "a3", "t3")}
        | {edge("E", name) for name in ("x", "y", "c", "a1", "a2", "a3", "t3")}
        | {edge("Q", name) for name in NAMES[:7]}
    )
)

ADJACENCY = [0] * ORDER
for u, v in EDGES:
    ADJACENCY[u] |= 1 << v
    ADJACENCY[v] |= 1 << u

NEIGHBOURHOOD = [0] * (1 << ORDER)
for mask in range(1, 1 << ORDER):
    bit = mask & -mask
    vertex = bit.bit_length() - 1
    NEIGHBOURHOOD[mask] = NEIGHBOURHOOD[mask ^ bit] | ADJACENCY[vertex]


def validate_quotient() -> None:
    boundary = set(BOUNDARY_EDGES)
    blocks = (("a1", "t1"), ("a2", "t2"), ("a3", "t3"))
    assert all(edge(*block) not in boundary for block in blocks)
    assert all(any(edge("c", name) in boundary for name in block) for block in blocks)
    assert all(
        any(edge(left, right) in boundary for left in first for right in second)
        for first, second in combinations(blocks, 2)
    )
    expected_d = {INDEX[name] for name in ("x", "y", "c", "t1", "t2", "a3", "t3")}
    expected_e = {INDEX[name] for name in ("x", "y", "c", "a1", "a2", "a3", "t3")}
    expected_q = set(range(7))
    assert {v for v in range(ORDER) if ADJACENCY[INDEX["D"]] >> v & 1} == expected_d
    assert {v for v in range(ORDER) if ADJACENCY[INDEX["E"]] >> v & 1} == expected_e
    assert {v for v in range(ORDER) if ADJACENCY[INDEX["Q"]] >> v & 1} == expected_q


def forest_components(forest: tuple[int, ...]) -> tuple[list[int], int] | None:
    parent = list(range(ORDER))
    touched = 0

    def find(vertex: int) -> int:
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    for edge_index in forest:
        u, v = EDGES[edge_index]
        root_u, root_v = find(u), find(v)
        if root_u == root_v:
            return None
        parent[root_u] = root_v
        touched |= (1 << u) | (1 << v)

    return [find(vertex) for vertex in range(ORDER)], touched


def contracts_to_k6(roots: list[int], deleted: int) -> bool:
    bags: dict[int, int] = {}
    for vertex, root in enumerate(roots):
        if deleted >> vertex & 1:
            continue
        bags[root] = bags.get(root, 0) | (1 << vertex)
    if len(bags) != 6:
        return False
    branch_sets = tuple(bags.values())
    return all(
        NEIGHBOURHOOD[left] & right
        for left, right in combinations(branch_sets, 2)
    )


def verify_no_k6_minor() -> tuple[int, ...]:
    counts: list[int] = []
    for size in range(7):
        delete_count = 6 - size
        checked = 0
        for forest in combinations(range(len(EDGES)), size):
            result = forest_components(forest)
            if result is None:
                continue
            roots, touched = result
            available = tuple(
                vertex for vertex in range(ORDER) if not (touched >> vertex & 1)
            )
            for deleted_vertices in combinations(available, delete_count):
                deleted = sum(1 << vertex for vertex in deleted_vertices)
                checked += 1
                assert not contracts_to_k6(roots, deleted), (
                    forest,
                    deleted_vertices,
                )
        counts.append(checked)
    return tuple(counts)


def main() -> None:
    validate_quotient()
    counts = verify_no_k6_minor()
    assert counts == (924, 6804, 31178, 102858, 240608, 358192, 252221)
    print("verified paired-triangle complementary-lock quotient")
    print("forest/deletion candidates", counts)
    print("CERTIFIED no K6 minor, hence no K7^vee minor")


if __name__ == "__main__":
    main()
