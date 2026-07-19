#!/usr/bin/env python3
"""Probe three full exterior subgraphs plus one defect-two subgraph.

Input is the complete graph6 catalogue on eight vertices.  The script keeps
the 82 residual boundary graphs from the promoted classification, adds three
independent vertices complete to the boundary, and a fourth independent
vertex adjacent to an arbitrary boundary subset of order at least six.  It
then tests the resulting twelve-vertex quotient for a K7 minor.

Run from the repository root with::

    geng -q 8 | python3 barriers/hc7_order8_three_full_defect2_probe.py

The summary begins ``boundaries=82``, ``cases=3034``, and
``failures=62``.  This is a research probe, not a promoted proof
certificate; the adjacent barrier has a computation-independent proof.
"""

from __future__ import annotations

import sys
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "active"), str(ROOT / "results")]

from hc7_boundary_join_probe import has_k7_minor
from hc7_order8_three_component_boundary_verify import decode_g6, is_residual


def has_triangle_anchor_model(
    boundary: tuple[int, ...], contact: frozenset[int]
) -> bool:
    """Recognize the explicit four-shore/three-singleton construction.

    Three full exterior vertices are anchored at three unused boundary
    vertices.  The defect-two exterior vertex is anchored at ``y``.  The
    remaining three singleton boundary vertices form a triangle.  The only
    nonautomatic adjacencies are from the partial exterior bag to the
    triangle, so every triangle vertex missed by the exterior vertex must be
    adjacent to ``y`` in the boundary.
    """

    vertices = range(8)
    for triangle in combinations(vertices, 3):
        q0, q1, q2 = triangle
        if not (
            (boundary[q0] >> q1) & 1
            and (boundary[q0] >> q2) & 1
            and (boundary[q1] >> q2) & 1
        ):
            continue
        triangle_set = frozenset(triangle)
        for y in contact - triangle_set:
            if all(
                q in contact or ((boundary[y] >> q) & 1)
                for q in triangle
            ):
                return True
    return False


def quotient(boundary: tuple[int, ...], contact: frozenset[int]) -> tuple[int, ...]:
    order = 12
    answer = [0] * order
    for vertex, neighbours in enumerate(boundary):
        answer[vertex] = neighbours

    for full in (8, 9, 10):
        for boundary_vertex in range(8):
            answer[full] |= 1 << boundary_vertex
            answer[boundary_vertex] |= 1 << full

    for boundary_vertex in contact:
        answer[11] |= 1 << boundary_vertex
        answer[boundary_vertex] |= 1 << 11
    return tuple(answer)


def main() -> None:
    explicit_only = "--explicit-only" in sys.argv[1:]
    boundaries = 0
    cases = 0
    failures: list[tuple[str, tuple[int, ...]]] = []
    by_defect = {0: 0, 1: 0, 2: 0}
    explicit_failures: list[tuple[str, tuple[int, ...]]] = []

    for line in sys.stdin:
        boundary = decode_g6(line)
        if not boundary or not is_residual(boundary):
            continue
        boundaries += 1
        code = line.strip()
        for defect_order in (0, 1, 2):
            for defect in combinations(range(8), defect_order):
                contact = frozenset(set(range(8)) - set(defect))
                cases += 1
                explicit_model = has_triangle_anchor_model(boundary, contact)
                if not explicit_model:
                    explicit_failures.append((code, defect))
                if (
                    not explicit_only
                    and not explicit_model
                    and not has_k7_minor(quotient(boundary, contact))
                ):
                    failures.append((code, defect))
                    by_defect[defect_order] += 1

    print(f"boundaries={boundaries}")
    print(f"cases={cases}")
    print(f"exact_minor_search={'skipped' if explicit_only else 'run'}")
    print(f"failures={len(failures)}")
    print(f"explicit_triangle_anchor_failures={len(explicit_failures)}")
    print(
        "failures_by_defect="
        + " ".join(f"{order}:{by_defect[order]}" for order in (0, 1, 2))
    )
    for code, defect in failures[:20]:
        print(f"failure {code} defect={defect}")
    for code, defect in explicit_failures[:20]:
        print(f"explicit_failure {code} defect={defect}")


if __name__ == "__main__":
    main()
