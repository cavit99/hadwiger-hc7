#!/usr/bin/env python3
"""Verify the finite cores of the repaired-contact two-fan barrier.

The accompanying proof handles every fan length.  The finite checks here
only certify that the seven fourteen-vertex completed cores are K7-minor
free and replay the first seven members of each family.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DECODER = ROOT / "results/hc7_disjoint_k6minus_six_terminal_crossing_decoder.py"
SPEC = importlib.util.spec_from_file_location("six_terminal_decoder", DECODER)
assert SPEC is not None and SPEC.loader is not None
D = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(D)


def edge(left: int, right: int) -> tuple[int, int]:
    return tuple(sorted((left, right)))


PATHS = (
    (D.A0, D.B0),
    (D.A1, D.B1),
    (D.A2, D.B2),
    (D.A3, D.P),
    (D.X, D.Q),
    (D.Y, D.R),
)

# By the simultaneous symmetry of P0,P1,P2 it is enough to use P0 for
# the first fan.  The seven triples are (second residual endpoint,
# first-fan rail, second-fan rail).
CASES = (
    (D.P, 0, 3),
    (D.P, 0, 5),
    (D.Q, 0, 4),
    (D.Q, 0, 5),
    (D.R, 0, 3),
    (D.R, 0, 4),
    (D.R, 0, 5),
)


def completed_core(
    z: int, first_rail: int, second_rail: int
) -> tuple[int, frozenset[tuple[int, int]]]:
    """The fourteen-vertex core after filling both adhesion triangles."""

    edges = set(D.BASE_EDGES)
    c, d = 12, 13
    first_left, first_right = PATHS[first_rail]
    second_left, second_right = PATHS[second_rail]
    edges.update(
        {
            edge(c, D.A3),
            edge(c, D.X),
            edge(c, first_left),
            edge(c, first_right),
            edge(d, D.Y),
            edge(d, z),
            edge(d, second_left),
            edge(d, second_right),
        }
    )
    return 14, frozenset(edges)


def fan_member(
    z: int, first_rail: int, second_rail: int, length: int
) -> tuple[int, frozenset[tuple[int, int]], int, int]:
    """Return the member with ``length`` internal hits on each fan rail."""

    assert length >= 1
    edges = set(D.BASE_EDGES)
    next_vertex = 12
    internal: list[list[int]] = []

    for index, (left, right) in enumerate(PATHS):
        edges.remove(edge(left, right))
        count = length if index in {first_rail, second_rail} else 0
        new_vertices = list(range(next_vertex, next_vertex + count))
        next_vertex += count
        internal.append(new_vertices)
        path = [left, *new_vertices, right]
        edges.update(edge(u, v) for u, v in zip(path, path[1:]))

    c, d = next_vertex, next_vertex + 1
    next_vertex += 2
    edges.update(
        {
            edge(c, D.A3),
            edge(c, D.X),
            edge(d, D.Y),
            edge(d, z),
            *(edge(c, vertex) for vertex in internal[first_rail]),
            *(edge(d, vertex) for vertex in internal[second_rail]),
        }
    )
    return next_vertex, frozenset(edges), c, d


def main() -> None:
    for case in CASES:
        assert not D.has_k7_minor(*completed_core(*case))
        for length in range(1, 8):
            order, edges, c, d = fan_member(*case, length)
            assert edge(c, d) not in edges
            assert not D.has_k7_minor(order, edges)

    print("completed_cores", len(CASES))
    print("finite_family_replay", len(CASES) * 7)
    print("GREEN: all two-fan cores and replay members are K7-minor-free")


if __name__ == "__main__":
    main()
