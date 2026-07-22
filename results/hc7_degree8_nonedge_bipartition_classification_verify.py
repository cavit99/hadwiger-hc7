#!/usr/bin/env python3
"""Verify the compact order-eight nonedge-bipartition classification.

Run from the repository root with nauty's ``geng`` on PATH:

    geng -q 8 | python3 results/hc7_degree8_nonedge_bipartition_classification_verify.py

The retained graphs have independence number at most three and every
six-vertex induced subgraph is K4-minor-free.  The imported routines are
the dependency-free exact graph6 and K4-minor checks already retained for
the order-eight boundary census.
"""

from __future__ import annotations

import hashlib
import subprocess
import sys
from itertools import combinations

from hc7_order8_three_component_boundary_verify import (
    bipartite_after_deleting,
    decode_g6,
    encode_g6,
    has_compact_k4,
)


N = 8


def catalogue_lines():
    """Use piped graph6 input, or invoke ``geng`` when stdin is empty."""

    first = sys.stdin.readline()
    if first:
        yield first
        yield from sys.stdin
        return

    process = subprocess.Popen(
        ["geng", "-q", str(N)],
        stdout=subprocess.PIPE,
        text=True,
    )
    assert process.stdout is not None
    yield from process.stdout
    if process.wait() != 0:
        raise RuntimeError("geng failed")


def has_independent_four(adjacency: tuple[int, ...]) -> bool:
    return any(
        all(
            not ((adjacency[left] >> right) & 1)
            for left, right in combinations(vertices, 2)
        )
        for vertices in combinations(range(N), 4)
    )


def aligned_nonedges(adjacency: tuple[int, ...]) -> list[tuple[int, int]]:
    return [
        (left, right)
        for left, right in combinations(range(N), 2)
        if not ((adjacency[left] >> right) & 1)
        and bipartite_after_deleting(
            adjacency, (1 << left) | (1 << right)
        )
    ]


def is_k1_join_c7(adjacency: tuple[int, ...]) -> bool:
    hubs = [vertex for vertex, row in enumerate(adjacency) if row.bit_count() == 7]
    if len(hubs) != 1:
        return False
    hub = hubs[0]
    rim = [vertex for vertex in range(N) if vertex != hub]
    rim_mask = sum(1 << vertex for vertex in rim)
    if any((adjacency[vertex] & rim_mask).bit_count() != 2 for vertex in rim):
        return False
    reached = {rim[0]}
    frontier = [rim[0]]
    while frontier:
        vertex = frontier.pop()
        for other in rim:
            if other not in reached and ((adjacency[vertex] >> other) & 1):
                reached.add(other)
                frontier.append(other)
    return len(reached) == 7


def main() -> None:
    total = 0
    compact = 0
    aligned = 0
    survivors: list[str] = []
    exceptions: list[tuple[str, tuple[int, ...]]] = []

    for line in catalogue_lines():
        adjacency = decode_g6(line)
        if not adjacency:
            continue
        total += 1
        if (
            has_independent_four(adjacency)
            or has_compact_k4(adjacency)
        ):
            continue
        compact += 1
        survivors.append(encode_g6(adjacency))
        if aligned_nonedges(adjacency):
            aligned += 1
        else:
            exceptions.append((encode_g6(adjacency), adjacency))

    assert total == 12_346
    assert compact == 185
    assert aligned == 184
    assert len(exceptions) == 1
    assert is_k1_join_c7(exceptions[0][1])

    survivor_codes = "\n".join(sorted(survivors)) + "\n"
    survivor_digest = hashlib.sha256(survivor_codes.encode()).hexdigest()
    exception_codes = (
        "\n".join(sorted(code for code, _adjacency in exceptions)) + "\n"
    )
    exception_digest = hashlib.sha256(exception_codes.encode()).hexdigest()

    print(f"order8_graphs {total}")
    print(f"compact_boundaries {compact}")
    print(f"compact_boundary_sha256 {survivor_digest}")
    print(f"aligned_nonedge_boundaries {aligned}")
    print(f"exceptions {len(exceptions)}")
    print(f"exception_graph6 {exceptions[0][0]}")
    print(f"exception_sha256 {exception_digest}")
    print("exception_structure K1_join_C7")
    print("PASS degree8_nonedge_bipartition_classification")


if __name__ == "__main__":
    main()
