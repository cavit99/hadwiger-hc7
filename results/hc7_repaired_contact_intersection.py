#!/usr/bin/env python3
"""Check the repaired-contact intersection lemma and its local barriers."""

from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path


HERE = Path(__file__).resolve().parent
DECODER = HERE / "hc7_disjoint_k6minus_six_terminal_crossing_decoder.py"
SPEC = importlib.util.spec_from_file_location("six_terminal_decoder", DECODER)
assert SPEC is not None and SPEC.loader is not None
D = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(D)


def edge(left: int, right: int) -> tuple[int, int]:
    return tuple(sorted((left, right)))


def verify_bags(
    order: int,
    edges: frozenset[tuple[int, int]],
    bags: tuple[tuple[int, ...], ...],
) -> None:
    adjacency = D.adjacency(order, edges)
    masks = tuple(sum(1 << vertex for vertex in bag) for bag in bags)
    assert len(masks) == 7
    assert all(masks)
    assert all(
        not (left & right)
        for index, left in enumerate(masks)
        for right in masks[index + 1 :]
    )
    assert all(D.connected(mask, adjacency) for mask in masks)
    assert all(
        D.touches(left, right, adjacency)
        for index, left in enumerate(masks)
        for right in masks[index + 1 :]
    )


def elimination_width(
    order: int, edges: frozenset[tuple[int, int]]
) -> tuple[int, tuple[int, ...]]:
    """Return a deterministic chordal-completion width certificate."""

    adjacency = [set() for _ in range(order)]
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    alive = set(range(order))
    eliminated: list[int] = []
    width = 0
    while alive:
        def score(vertex: int) -> tuple[int, int, int]:
            neighbours = adjacency[vertex] & alive
            missing = sum(
                1
                for left in neighbours
                for right in neighbours
                if left < right and right not in adjacency[left]
            )
            return len(neighbours), missing, vertex

        vertex = min(alive, key=score)
        neighbours = adjacency[vertex] & alive
        width = max(width, len(neighbours))
        for left in neighbours:
            adjacency[left].update(neighbours - {left})
        alive.remove(vertex)
        eliminated.append(vertex)
    return width, tuple(eliminated)


def central_intersection(z: int) -> frozenset[tuple[int, int]]:
    # w=12 gives a3-w-x.  t=13 is adjacent to a3,x,y,z.
    return frozenset(
        set(D.BASE_EDGES)
        | {
            edge(D.A3, 12),
            edge(12, D.X),
            edge(D.A3, 13),
            edge(D.X, 13),
            edge(D.Y, 13),
            edge(z, 13),
        }
    )


def central_r_with_extras(extras: set[int]) -> frozenset[tuple[int, int]]:
    return frozenset(
        set(central_intersection(D.R))
        | {edge(13, vertex) for vertex in extras}
    )


def parallel_repairs(z: int) -> frozenset[tuple[int, int]]:
    # w=12 is the original repair, s=13 the disjoint y-z path, and
    # u=14,v=15 are two independent alternative a3-x paths.
    return frozenset(
        set(D.BASE_EDGES)
        | {
            edge(D.A3, 12),
            edge(12, D.X),
            edge(D.Y, 13),
            edge(13, z),
            edge(D.A3, 14),
            edge(14, D.X),
            edge(D.A3, 15),
            edge(15, D.X),
        }
    )


def rail_internal_attachment(left: int, right: int) -> frozenset[tuple[int, int]]:
    # Replace left-right by left-v-right with v=14.  The central component
    # t=13 attaches to a3,x,y,r and to v; w=12 retains a3-w-x.
    edges = set(central_intersection(D.R))
    edges.remove(edge(left, right))
    edges |= {
        edge(left, 14),
        edge(14, right),
        edge(13, 14),
    }
    return frozenset(edges)


def main() -> None:
    q_graph = central_intersection(D.Q)
    verify_bags(
        14,
        q_graph,
        (
            (D.B0,),
            (D.B1,),
            (D.B2,),
            (D.R,),
            (D.Q,),
            (D.A3, 12, 13, D.P),
            (D.A0, D.A1, D.A2, D.X, D.Y),
        ),
    )

    p_graph = central_intersection(D.P)
    verify_bags(
        14,
        p_graph,
        (
            (D.B0,),
            (D.B1,),
            (D.B2,),
            (D.R,),
            (D.P,),
            (D.X, 13, D.Q),
            (D.A0, D.A1, D.A2, D.A3, 12, D.Y),
        ),
    )

    a0_graph = central_r_with_extras({D.A0})
    verify_bags(
        14,
        a0_graph,
        (
            (D.B0,),
            (D.B1,),
            (D.B2,),
            (D.R,),
            (D.X, D.Y, D.Q),
            (D.A3, 12, D.P),
            (D.A0, D.A1, D.A2, 13),
        ),
    )

    all_b_graph = central_r_with_extras({D.B0, D.B1, D.B2})
    verify_bags(
        14,
        all_b_graph,
        (
            (D.Y, 13),
            (D.B0,),
            (D.B1,),
            (D.B2,),
            (D.R,),
            (D.A0, D.A1, D.A2, D.X, D.Q),
            (D.A3, 12, D.P),
        ),
    )

    first_rail_graph = rail_internal_attachment(D.A0, D.B0)
    verify_bags(
        15,
        first_rail_graph,
        (
            (D.B0,),
            (D.B1,),
            (D.B2,),
            (D.R,),
            (D.X, D.Y, D.Q),
            (D.A3, 12, D.P),
            (D.A0, D.A1, D.A2, 13, 14),
        ),
    )

    rails = (
        (D.A0, D.B0),
        (D.A1, D.B1),
        (D.A2, D.B2),
        (D.A3, D.P),
        (D.X, D.Q),
        (D.Y, D.R),
    )
    rail_outcomes = tuple(
        D.has_k7_minor(15, rail_internal_attachment(left, right))
        for left, right in rails
    )
    assert rail_outcomes == (True, True, True, True, True, False)

    assert not D.has_k7_minor(14, central_intersection(D.R))
    exceptional_endpoints = {D.B0, D.B1, D.B2}
    other_endpoints = set(range(12)) - {D.A3, D.X, D.Y, D.R}
    negative_extra_sets: set[frozenset[int]] = set()
    for size in range(len(other_endpoints) + 1):
        for choice in itertools.combinations(other_endpoints, size):
            extras = frozenset(choice)
            if not D.has_k7_minor(14, central_r_with_extras(set(extras))):
                negative_extra_sets.add(extras)
    expected_negative = {
        frozenset(choice)
        for size in range(3)
        for choice in itertools.combinations(exceptional_endpoints, size)
    }
    assert negative_extra_sets == expected_negative
    assert all(
        elimination_width(14, central_r_with_extras(set(extras)))[0] <= 5
        for extras in expected_negative
    )

    for z in (D.P, D.Q, D.R):
        assert not D.has_k7_minor(16, parallel_repairs(z))

    print("positive_intersection_certificates 5")
    print("negative_central_r 1")
    print("exceptional_r_endpoint_attachment_sets 7")
    print("exceptional_r_treewidth_upper_bound 5")
    print("interior_rail_outcomes", rail_outcomes)
    print("negative_parallel_repair_graphs 3")
    print("GREEN: all repaired-contact intersection checks passed")


if __name__ == "__main__":
    main()
