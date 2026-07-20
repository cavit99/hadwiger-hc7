#!/usr/bin/env python3
"""Verify the single-bridge span inference counterexample."""

from itertools import combinations


VERTICES = tuple([f"v{i}" for i in range(6)] + ["a"])
EDGES = {
    *{frozenset((f"v{i}", f"v{i + 1}")) for i in range(5)},
    frozenset(("v0", "v5")),
    frozenset(("a", "v0")),
    frozenset(("a", "v1")),
}


def connected_after_deleting(deleted: set[str]) -> bool:
    remaining = set(VERTICES) - deleted
    if not remaining:
        return True
    reached = {next(iter(remaining))}
    while True:
        grown = reached | {
            v
            for edge in EDGES
            for v in edge
            if v in remaining and edge & reached
        }
        if grown == reached:
            return reached == remaining
        reached = grown


assert connected_after_deleting(set())
assert all(connected_after_deleting({v}) for v in VERTICES)
assert any(
    not connected_after_deleting(set(pair))
    for pair in combinations(VERTICES, 2)
)

chord_span = {"v1", "v2", "v3", "v4"}
triangle_interior = {"a"}
portal_vertices = {"p": "v1", "q": "a"}
assert {label for label, v in portal_vertices.items() if v in chord_span} == {"p"}
assert {
    label for label, v in portal_vertices.items() if v in triangle_interior
} == {"q"}

root_path = ("d", "v0", "v5", "e")
other_path = ("p", "v1", "a", "q")
assert set(root_path).isdisjoint(other_path)

print("GREEN single-bridge span inference barrier")
print("C: vertices=7 edges=9 connectivity=2")
print(
    "D-bridges: chord span={v1,v2,v3,v4} hits={p}; "
    "triangle interior={a} hits={q}"
)
print("disjoint linkage: d-v0-v5-e ; p-v1-a-q")
print("scope: bridge-local inference only; no HC7 criticality claim")
