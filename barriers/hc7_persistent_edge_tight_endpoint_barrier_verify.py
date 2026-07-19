#!/usr/bin/env python3
"""Verify the Grötzsch-plus-chord persistent-edge barrier.

Expected output:

    verified Grötzsch-plus-chord persistent-edge barrier
"""

from __future__ import annotations


def groetzsch_edges() -> set[tuple[int, int]]:
    """Return M(C5) on x_i=i, y_i=5+i, and z=10."""

    edges: set[tuple[int, int]] = set()

    def add(u: int, v: int) -> None:
        edges.add((u, v) if u < v else (v, u))

    for i in range(5):
        j = (i + 1) % 5
        add(i, j)
        add(i, 5 + j)
        add(j, 5 + i)
        add(5 + i, 10)
    return edges


def adjacency(
    edges: set[tuple[int, int]], order: int = 11
) -> list[set[int]]:
    adj = [set() for _ in range(order)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def colouring(
    edges: set[tuple[int, int]],
    colours: int,
    deleted: int | None = None,
    order: int = 11,
) -> dict[int, int] | None:
    """Return one deterministic proper colouring, or None."""

    adj = adjacency(edges, order)
    vertices = [v for v in range(order) if v != deleted]
    order = sorted(vertices, key=lambda v: (-len(adj[v]), v))
    assigned: dict[int, int] = {}

    def search(position: int) -> bool:
        if position == len(order):
            return True
        vertex = order[position]
        used = {assigned[w] for w in adj[vertex] if w in assigned}
        for colour in range(colours):
            if colour in used:
                continue
            assigned[vertex] = colour
            if search(position + 1):
                return True
            del assigned[vertex]
        return False

    return dict(assigned) if search(0) else None


def is_proper(
    edges: set[tuple[int, int]], assignment: dict[int, int]
) -> bool:
    return all(
        u not in assignment
        or v not in assignment
        or assignment[u] != assignment[v]
        for u, v in edges
    )


def main() -> None:
    base = groetzsch_edges()
    chord = (0, 2)
    augmented = base | {chord}

    assert len(base) == 20
    assert len(augmented) == 21
    assert chord not in base

    # Both graphs are non-three-colourable; the augmented graph is
    # four-colourable.
    assert colouring(base, 3) is None
    assert colouring(augmented, 3) is None
    four_colouring = colouring(augmented, 4)
    assert four_colouring is not None
    assert is_proper(augmented, four_colouring)

    # Both graphs are vertex-minimal non-three-colourable.
    for vertex in range(11):
        base_colouring = colouring(base, 3, vertex)
        augmented_colouring = colouring(augmented, 3, vertex)
        assert base_colouring is not None
        assert augmented_colouring is not None
        assert is_proper(base, base_colouring)
        assert is_proper(augmented, augmented_colouring)

    # With the constant three-element lists, both endpoints remain
    # non-tight after the persistent chord is removed.
    base_adj = adjacency(base)
    assert len(base_adj[0]) == 4
    assert len(base_adj[2]) == 4

    # Check the reflection used to reduce the hand certificate to seven
    # deletion orbits.
    reflection = {0: 2, 2: 0, 1: 1, 3: 4, 4: 3,
                  5: 7, 7: 5, 6: 6, 8: 9, 9: 8, 10: 10}
    reflected = {
        tuple(sorted((reflection[u], reflection[v]))) for u, v in augmented
    }
    assert reflected == augmented

    # The K2 join is the six-chromatic, constant-five-list lift recorded
    # in Corollary 2.2.  Check its paired vertex-criticality directly.
    joined_base = set(base)
    joined_base.add((11, 12))
    for old_vertex in range(11):
        joined_base.add((old_vertex, 11))
        joined_base.add((old_vertex, 12))
    joined_augmented = joined_base | {chord}
    assert colouring(joined_base, 5, order=13) is None
    assert colouring(joined_augmented, 5, order=13) is None
    assert colouring(joined_augmented, 6, order=13) is not None
    for vertex in range(13):
        assert colouring(joined_base, 5, vertex, order=13) is not None
        assert colouring(joined_augmented, 5, vertex, order=13) is not None
    joined_adj = adjacency(joined_base, 13)
    assert len(joined_adj[0]) == 6
    assert len(joined_adj[2]) == 6

    print("verified Grötzsch-plus-chord persistent-edge barrier")


if __name__ == "__main__":
    main()
