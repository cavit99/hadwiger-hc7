#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Verify the sharp C6 unique-interface counterexample from the note."""

from __future__ import annotations

from contact_order7_sixedge_web_probe import generic_minor_model


S = tuple(range(7))
Z = 0
C = tuple(range(1, 7))
H, X, Y = 7, 8, 9


def normalized(edges):
    return {tuple(sorted(edge)) for edge in edges}


edges = {(Z, c) for c in C}
edges.update((C[i], C[(i + 1) % 6]) for i in range(6))
edges.update((s, helper) for s in S for helper in (H, X, Y))
edges.add((X, Y))
edges = normalized(edges)

# Exact connected-branch-set searches.
assert generic_minor_model(10, edges, 7) is None
without_z = {(a - 1, b - 1) for a, b in edges if a != Z and b != Z}
assert generic_minor_model(9, without_z, 6) is None

# The displayed coloring of the edge deletion.
color = {
    Z: 1,
    C[0]: 2,
    C[1]: 3,
    C[2]: 4,
    C[3]: 2,
    C[4]: 3,
    C[5]: 5,
    H: 6,
    X: 6,
    Y: 6,
}
deleted = edges - {tuple(sorted((X, Y)))}
assert all(color[a] != color[b] for a, b in deleted)
assert color[X] == color[Y] == 6
assert {color[s] for s in S} == {1, 2, 3, 4, 5}
for gamma in range(1, 6):
    assert any(color[s] == gamma and tuple(sorted((X, s))) in edges for s in S)
    assert any(color[s] == gamma and tuple(sorted((Y, s))) in edges for s in S)

assert len({v for edge in edges if X in edge for v in edge if v != X}) == 8
assert len({v for edge in edges if Y in edge for v in edge if v != Y}) == 8

print("verified: K7-negative full-row quotient")
print("verified: five simultaneous two-sided anchors")
print("verified: neither unique-interface side exposes a seven-cut")
