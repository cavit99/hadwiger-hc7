#!/usr/bin/env python3
"""Verify the 4-connected robust-carrier barriers and optional minimality."""

from __future__ import annotations

import argparse
import itertools
import os
from pathlib import Path
import shutil
import subprocess
import sys

import networkx as nx


DISTINCT_GRAPH6 = b"HCZTfP}"
DISTINCT_EDGES = {
    (0, 3), (0, 5), (0, 6), (0, 7),
    (1, 4), (1, 5), (1, 7), (1, 8),
    (2, 4), (2, 6), (2, 7), (2, 8),
    (3, 5), (3, 6), (3, 8),
    (4, 7), (4, 8),
    (5, 8), (6, 8),
}
DISTINCT_TERMINALS = (0, 7, 1, 2, 5, 6)

SHARED_GRAPH6 = b"GQyurg"
SHARED_EDGES = {
    (0, 2), (0, 4), (0, 5), (0, 6),
    (1, 3), (1, 4), (1, 6), (1, 7),
    (2, 4), (2, 5), (2, 7),
    (3, 5), (3, 6), (3, 7),
    (4, 6), (5, 7),
}
SHARED_TERMINALS = (0, 5, 1, 3, 6)


def decode(code: bytes, expected_edges: set[tuple[int, int]]) -> nx.Graph:
    """Decode graph6 with its numerical labels and pin the exact edge set."""
    graph = nx.from_graph6_bytes(code)
    assert tuple(graph) == tuple(range(len(graph)))
    actual = {tuple(sorted(edge)) for edge in graph.edges}
    assert actual == expected_edges
    assert nx.to_graph6_bytes(graph, header=False).strip() == code
    return graph


def exact_four_connectivity(graph: nx.Graph) -> None:
    """Brute-force the lower bound and exhibit a four-cut for the upper."""
    vertices = tuple(graph)
    for order in range(4):
        for deleted in itertools.combinations(vertices, order):
            remainder = graph.subgraph(set(vertices) - set(deleted))
            assert nx.is_connected(remainder), deleted
    assert nx.node_connectivity(graph) == 4
    degree_four_vertex = next(vertex for vertex, degree in graph.degree if degree == 4)
    cut = set(graph[degree_four_vertex])
    remainder = graph.subgraph(set(vertices) - cut)
    assert len(remainder) <= 1 or not nx.is_connected(remainder)


def connected(mask: set[int], graph: nx.Graph) -> bool:
    return bool(mask) and nx.is_connected(graph.subgraph(mask))


def has_disjoint_carriers(
    graph: nx.Graph, first: set[int], second: set[int]
) -> bool:
    """Exact test by assigning every optional vertex left/right/unused."""
    assert first.isdisjoint(second)
    optional = tuple(set(graph) - first - second)
    for assignment in itertools.product(range(3), repeat=len(optional)):
        left = set(first)
        right = set(second)
        for vertex, side in zip(optional, assignment):
            if side == 1:
                left.add(vertex)
            elif side == 2:
                right.add(vertex)
        if connected(left, graph) and connected(right, graph):
            return True
    return False


def canonical_cycle(cycle: list[int] | tuple[int, ...]) -> tuple[int, ...]:
    cycle = tuple(cycle)
    candidates = []
    for oriented in (cycle, tuple(reversed(cycle))):
        for offset in range(len(cycle)):
            candidates.append(oriented[offset:] + oriented[:offset])
    return min(candidates)


def facial_cycles(graph: nx.Graph) -> set[tuple[int, ...]]:
    planar, embedding = nx.check_planarity(graph)
    assert planar
    marked: set[tuple[int, int]] = set()
    faces: set[tuple[int, ...]] = set()
    for u, v in embedding.edges:
        for start in ((u, v), (v, u)):
            if start not in marked:
                faces.add(canonical_cycle(embedding.traverse_face(*start, marked)))
    return faces


def verify_distinct() -> None:
    graph = decode(DISTINCT_GRAPH6, DISTINCT_EDGES)
    assert len(graph) == 9 and graph.number_of_edges() == 19
    exact_four_connectivity(graph)
    faces = facial_cycles(graph)
    assert canonical_cycle((5, 0, 7, 1)) in faces
    assert canonical_cycle((7, 0, 6, 2)) in faces

    alpha, beta, a1, a2, b1, b2 = DISTINCT_TERMINALS
    assert len(set(DISTINCT_TERMINALS)) == 6
    patterns = (
        ({alpha, a1, a2}, {beta, b1}),
        ({alpha, a1, a2}, {beta, b2}),
        ({alpha, a1}, {beta, b1, b2}),
        ({alpha, a2}, {beta, b1, b2}),
    )
    assert all(not has_disjoint_carriers(graph, left, right) for left, right in patterns)


def verify_shared_one() -> None:
    graph = decode(SHARED_GRAPH6, SHARED_EDGES)
    assert len(graph) == 8 and graph.number_of_edges() == 16
    assert all(degree == 4 for _, degree in graph.degree)
    exact_four_connectivity(graph)
    assert canonical_cycle((6, 0, 5, 3)) in facial_cycles(graph)

    alpha, beta, common, old_only, new_only = SHARED_TERMINALS
    assert len(set(SHARED_TERMINALS)) == 5
    nontrivial_patterns = (
        ({alpha, common, old_only}, {beta, new_only}),
        ({alpha, old_only}, {beta, common, new_only}),
    )
    assert all(
        not has_disjoint_carriers(graph, left, right)
        for left, right in nontrivial_patterns
    )
    # The other two robust patterns both demand the common singleton on
    # opposite sides and are impossible before any graph structure is used.
    assert {common} & {common, old_only}
    assert {common} & {common, new_only}


def verify_shared_two() -> None:
    graph = nx.complete_graph(5)
    exact_four_connectivity(graph)
    alpha, beta, c1, c2 = 0, 1, 2, 3
    patterns = (
        ({alpha, c1, c2}, {beta, c1}),
        ({alpha, c1, c2}, {beta, c2}),
        ({alpha, c1}, {beta, c1, c2}),
        ({alpha, c2}, {beta, c1, c2}),
    )
    assert all(not left.isdisjoint(right) for left, right in patterns)


def run_search(n: int, variant: str) -> str:
    geng = shutil.which("geng")
    if geng is None:
        raise SystemExit("--minimality requires nauty-geng (`geng`) on PATH")
    root = Path(__file__).resolve().parents[1]
    search = root / "active" / "hc7_robust_carrier_geng_search.py"
    generated = subprocess.run(
        [geng, "-q", "-d4", str(n)],
        check=True,
        stdout=subprocess.PIPE,
    )
    environment = os.environ.copy()
    completed = subprocess.run(
        [
            sys.executable,
            str(search),
            "--variant",
            variant,
            "--progress",
            "0",
        ],
        check=True,
        input=generated.stdout,
        stdout=subprocess.PIPE,
        env=environment,
    )
    return completed.stdout.decode().strip()


def verify_minimality() -> None:
    for n in (6, 7, 8):
        result = run_search(n, "distinct4")
        assert "'result': 'NONE'" in result, (n, result)
    result = run_search(9, "distinct4")
    assert "'result': 'COUNTEREXAMPLE'" in result, result

    for n in (5, 6, 7):
        result = run_search(n, "shared1")
        assert "'result': 'NONE'" in result, (n, result)
    result = run_search(8, "shared1")
    assert "'result': 'COUNTEREXAMPLE'" in result, result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--minimality", action="store_true")
    args = parser.parse_args()
    verify_distinct()
    verify_shared_one()
    verify_shared_two()
    if args.minimality:
        verify_minimality()
    print(
        "GREEN: exact kappa=4, planar crossed faces, four carrier failures; "
        "shared-label variants verified"
        + ("; nauty minimal-order search verified" if args.minimality else "")
    )


if __name__ == "__main__":
    main()
