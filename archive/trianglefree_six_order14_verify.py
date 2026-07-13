#!/usr/bin/env python3
"""Exhaust the minimal path witnesses of order at most 14.

Targets are K_{2,4} and theta(2,2,3).  A minor-minimal witness may be
assumed to consist of one simple alternating root-to-root path for every
target edge.  Once direct root edges have been excluded, every colour class
has size at least two.  Hence order at most 14 leaves only the orbit
representatives listed below.

This is a falsification/certificate enumerator, not a proof that either target
has property (*) in arbitrary order.
"""

from __future__ import annotations

from trianglefree_six_property_search import exhaustive_path_graphs, rooted_model, targets


CASES: dict[str, tuple[tuple[int, ...], ...]] = {
    # Automorphism orbits: two hubs and four interchangeable leaves.
    "k24": (
        (2, 2, 2, 2, 2, 2),
        (3, 2, 2, 2, 2, 2),  # one extra at a hub
        (2, 2, 3, 2, 2, 2),  # one extra at a leaf
        (4, 2, 2, 2, 2, 2),  # two extras at one hub
        (2, 2, 4, 2, 2, 2),  # two extras at one leaf
        (3, 3, 2, 2, 2, 2),  # one extra at each hub
        (3, 2, 3, 2, 2, 2),  # one at a hub and one at a leaf
        (2, 2, 3, 3, 2, 2),  # one at each of two leaves
    ),
    # Theta labels: hubs 0,1; short branches 2,3; long branch 0-4-5-1.
    "theta": (
        (2, 2, 2, 2, 2, 2),
        (3, 2, 2, 2, 2, 2),  # one extra: hub orbit
        (2, 2, 3, 2, 2, 2),  # short-branch orbit
        (2, 2, 2, 2, 3, 2),  # long-branch orbit
        (4, 2, 2, 2, 2, 2),
        (2, 2, 4, 2, 2, 2),
        (2, 2, 2, 2, 4, 2),
        (3, 3, 2, 2, 2, 2),  # hub-hub
        (3, 2, 3, 2, 2, 2),  # hub-short
        (3, 2, 2, 2, 3, 2),  # hub-long, incident
        (3, 2, 2, 2, 2, 3),  # hub-long, nonincident
        (2, 2, 3, 3, 2, 2),  # short-short
        (2, 2, 3, 2, 3, 2),  # short-long
        (2, 2, 2, 2, 3, 3),  # long-long
    ),
}


def main() -> None:
    for name, size_cases in CASES.items():
        target = targets()[name]
        for sizes in size_cases:
            checked = 0
            for graph in exhaustive_path_graphs(target, sizes):
                checked += 1
                if rooted_model(graph, target, 6) is None:
                    raise AssertionError(
                        f"counterexample: target={name}, sizes={sizes}, "
                        f"edges={sorted(graph.edges())}"
                    )
            print(f"PASS target={name} sizes={sizes} witnesses={checked}")


if __name__ == "__main__":
    main()
