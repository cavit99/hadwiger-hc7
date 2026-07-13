#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Test whether two doubled boundary portals repair the sharp C6 quotient.

The base quotient is J=K1 join C6 with three full helpers, two joined by
the unique interface edge.  Two doubled portals let one connected shore be
split into adjacent pieces which both meet both roots and whose rows cover
the boundary.  We test every minimal covering assignment, both when
the split shore is the opposite helper and when it is an interface arm.
"""

from __future__ import annotations

import itertools

from contact_order7_sixedge_web_probe import generic_minor_model
from contact_order7_five_edge_verify import verify_model


S = tuple(range(7))
Z = 0
C = tuple(range(1, 7))
A, B, P, Q = 7, 8, 9, 10


def boundary_edges() -> set[tuple[int, int]]:
    edges = {(Z, c) for c in C}
    edges.update((C[i], C[(i + 1) % 6]) for i in range(6))
    return {tuple(sorted(edge)) for edge in edges}


def rows(roots: tuple[int, int], bits: int) -> tuple[set[int], set[int]]:
    first = set(roots)
    second = set(roots)
    free = tuple(s for s in S if s not in roots)
    for index, s in enumerate(free):
        (first if bits >> index & 1 else second).add(s)
    return first, second


def graph_edges(roots: tuple[int, int], bits: int, split_opposite: bool) -> set[tuple[int, int]]:
    first, second = rows(roots, bits)
    edges = boundary_edges()
    if split_opposite:
        # A,B are the full unique-interface arms; P,Q split the opposite shore.
        edges.add((A, B))
        edges.add((P, Q))
        edges.update((s, helper) for s in S for helper in (A, B))
    else:
        # A is the full opposite shore, B the other full arm; P,Q split one arm.
        edges.add((P, Q))
        edges.add((B, P))
        edges.update((s, helper) for s in S for helper in (A, B))
    edges.update((s, P) for s in first)
    edges.update((s, Q) for s in second)
    return {tuple(sorted(edge)) for edge in edges}


def main() -> None:
    failures: list[tuple[str, tuple[int, int], int]] = []
    verified = 0
    root_pairs = tuple(itertools.combinations(S, 2))
    for split_opposite, roots, bits in itertools.product(
        (False, True), root_pairs, range(1 << 5)
    ):
        edges = graph_edges(roots, bits, split_opposite)
        model = generic_minor_model(11, edges, 7)
        name = "opposite" if split_opposite else "arm"
        if model is None:
            failures.append((name, roots, bits))
            continue
        bags = tuple(
            tuple(v for v in range(11) if mask >> v & 1)
            for mask in model
        )
        verify_model(edges, bags)
        verified += 1
    print("split quotients checked", 2 * len(root_pairs) * (1 << 5))
    print("verified K7 models", verified)
    print("negative quotients", len(failures))
    for failure in failures[:30]:
        print("failure", failure)


if __name__ == "__main__":
    main()
