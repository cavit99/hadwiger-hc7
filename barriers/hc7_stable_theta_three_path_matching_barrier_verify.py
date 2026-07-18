#!/usr/bin/env python3
"""Verify the finite stable-theta/three-path incidence barrier."""

from collections import deque


U = {f"u{i}" for i in range(4)}
B = {"b", "q", "r"}
T = U | B
L = {"v"} | {f"x{i}" for i in range(5)}
R = {"d", "e", "f"}
V = T | L | R

edges: set[frozenset[str]] = set()


def add(x: str, y: str) -> None:
    assert x != y
    edges.add(frozenset((x, y)))


def adjacent(x: str, y: str) -> bool:
    return frozenset((x, y)) in edges


def set_adjacent(x: set[str], y: set[str]) -> bool:
    return any(adjacent(a, b) for a in x for b in y)


def connected(x: set[str]) -> bool:
    if not x:
        return False
    seen = {next(iter(x))}
    queue = deque(seen)
    while queue:
        a = queue.popleft()
        for b in x - seen:
            if adjacent(a, b):
                seen.add(b)
                queue.append(b)
    return seen == x


for i in range(5):
    add(f"x{i}", f"x{(i + 1) % 5}")
for i in range(4):
    add(f"u{i}", f"x{i}")
    add(f"u{i}", f"u{(i + 1) % 4}")
for z in B | {f"x{i}" for i in range(5)}:
    add("v", z)
for i, a in enumerate(sorted(R)):
    for b in sorted(R)[i + 1 :]:
        add(a, b)
for a in R:
    for t in T:
        add(a, t)

sector_vertices = {f"u{i}" for i in range(4)} | {f"x{i}" for i in range(5)}
omitted = {frozenset(("r", "u1")), frozenset(("r", "x1")), frozenset(("r", "x4"))}
for b in B:
    for z in sector_vertices:
        if frozenset((b, z)) not in omitted:
            add(b, z)

C = [{f"u{i}", f"x{i}"} for i in range(4)] + [{"x4"}]
D = set(R)

assert all(connected(c) for c in C)
assert all(C[i].isdisjoint(C[j]) for i in range(5) for j in range(i))
assert all(set_adjacent(C[i], C[(i + 1) % 5]) for i in range(5))
assert {sum(adjacent(v, z) for z in V) for v in {"v"}} == {8}
assert all(f"x{i}" in C[i] and adjacent("v", f"x{i}") for i in range(5))
assert all(f"u{i}" in C[i] for i in range(4))

labels = [{z} for z in sorted(B)] + C
contacts = [set_adjacent(D, label) for label in labels]
assert sum(contacts) == 7
assert contacts[-1] is False

paths = [
    ("b", "d", "u0"),
    ("b", "e", "u0"),
    ("b", "f", "u0"),
]
assert all(all(adjacent(path[i], path[i + 1]) for i in range(2)) for path in paths)
terminals = {"b", "u0", "u2"}
interiors = [set(path) - terminals for path in paths]
assert all(interiors[i].isdisjoint(interiors[j]) for i in range(3) for j in range(i))

defects = {
    (b, i)
    for b in B
    for i, c in enumerate(C)
    if not set_adjacent({b}, c)
}
assert defects == {("r", 1), ("r", 4)}
assert len({b for b, _ in defects}) < len(defects)  # not a matching
assert all(not adjacent(l, r) for l in L for r in R)
assert sum(adjacent("x1", z) for z in V) == 6

print("stable-theta three-path matching barrier: PASS")
