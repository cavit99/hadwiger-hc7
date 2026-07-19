#!/usr/bin/env python3
"""Verify the clean-path geometry barrier and its width-five certificate."""

from collections import deque
from itertools import combinations


S = {"m1", "m2", "x", "y", "k1", "k2", "k3"}
M = {"m1", "m2"}
K = {"k1", "k2", "k3"}
L = {"d"}
R = {"p1", "p2", "w"}
V = S | L | R


def edge(u: str, v: str) -> frozenset[str]:
    assert u != v
    return frozenset((u, v))


E: set[frozenset[str]] = set()
for u, v in combinations(sorted(K), 2):
    E.add(edge(u, v))
for universal in ("d", "p1", "p2"):
    for s in S:
        E.add(edge(universal, s))
for u, v in (("x", "w"), ("w", "y"), ("w", "p1"), ("w", "p2")):
    E.add(edge(u, v))

BAGS = {
    "C": {"d", "p1", "p2", "k1", "k2", "k3"},
    "B": {"d", "p1", "p2", "x", "y"},
    "W": {"p1", "p2", "x", "y", "w"},
    "I1": {"d", "p1", "p2", "m1"},
    "I2": {"d", "p1", "p2", "m2"},
}
TREE_EDGES = {edge("C", "B"), edge("B", "W"), edge("C", "I1"), edge("C", "I2")}


def adjacent(u: str, v: str) -> bool:
    return edge(u, v) in E


def induced_tree_connected(nodes: set[str]) -> bool:
    if not nodes:
        return True
    start = next(iter(nodes))
    reached = {start}
    queue = deque([start])
    while queue:
        a = queue.popleft()
        for b in nodes - reached:
            if edge(a, b) in TREE_EDGES:
                reached.add(b)
                queue.append(b)
    return reached == nodes


assert len(S) == 7 and M.isdisjoint(K | {"x", "y"})
assert not adjacent("m1", "m2")
assert all(adjacent(u, v) for u, v in combinations(sorted(K), 2))
assert not adjacent("x", "y")

for full in ("d", "p1", "p2"):
    assert all(adjacent(full, s) for s in S)
assert all(not adjacent(l, r) for l in L for r in R)
assert adjacent("p1", "w") and adjacent("w", "p2")
assert adjacent("x", "w") and adjacent("w", "y")
assert "w" not in {"p1", "p2"}
assert all(not adjacent("w", k) for k in K)

assert set().union(*BAGS.values()) == V
assert len(TREE_EDGES) == len(BAGS) - 1
assert induced_tree_connected(set(BAGS))
for uv in E:
    assert any(set(uv) <= bag for bag in BAGS.values()), f"uncovered edge {sorted(uv)}"
for v in V:
    containing = {name for name, bag in BAGS.items() if v in bag}
    assert induced_tree_connected(containing), f"running-intersection failure at {v}"

max_bag = max(map(len, BAGS.values()))
assert max_bag == 6
print("PASS: clean-path geometry; tree decomposition width 5; no K7 minor")
