#!/usr/bin/env python3
"""Solver-free replay of the rooted-K4-to-K7 upgrade barrier."""

from __future__ import annotations

from itertools import combinations


S = {"c", "a1", "t1", "a2", "t2", "a3", "t3"}
CORE = {"r", "h1", "h2", "h3"}
V = S | CORE | {"p", "q"}


def edge(left: str, right: str) -> tuple[str, str]:
    assert left != right
    return tuple(sorted((left, right)))


E = {edge(left, right) for left, right in combinations(CORE, 2)}
E |= {
    edge("h1", "a1"),
    edge("h1", "t3"),
    edge("h2", "a2"),
    edge("h2", "t2"),
    edge("h3", "a3"),
    edge("h3", "t1"),
    edge("c", "r"),
}
E |= {edge(packet, literal) for packet in ("p", "q") for literal in S}
E |= {
    edge("a1", "a2"),
    edge("a1", "c"),
    edge("a1", "t3"),
    edge("a2", "c"),
    edge("a2", "t3"),
    edge("a3", "c"),
}


def connected(vertices: set[str]) -> bool:
    reached = {next(iter(vertices))}
    while True:
        larger = reached | {
            vertex
            for vertex in vertices - reached
            if any(edge(vertex, old) in E for old in reached)
        }
        if larger == reached:
            return reached == vertices
        reached = larger


def adjacent(left: set[str], right: set[str]) -> bool:
    return any(edge(x, y) in E for x in left for y in right)


PAIRS = ({"a1", "t1"}, {"a2", "t2"}, {"a3", "t3"})
assert all(edge(*pair) not in E for pair in PAIRS)
assert all(any(edge("c", x) in E for x in pair) for pair in PAIRS)
assert all(
    any(edge(x, y) in E for x in left for y in right)
    for left, right in combinations(PAIRS, 2)
)
assert all(edge(x, y) in E for x, y in combinations(CORE, 2))
assert all(edge(packet, literal) in E for packet in ("p", "q") for literal in S)


MODEL = (
    {"a3"},
    {"a2", "h2"},
    {"h1"},
    {"c", "r"},
    {"p", "t2", "t3"},
    {"h3", "t1"},
    {"a1", "q"},
)
assert all(left.isdisjoint(right) for left, right in combinations(MODEL, 2))
assert all(connected(bag) for bag in MODEL)
assert all(
    adjacent(MODEL[i], MODEL[j])
    for i, j in combinations(range(7), 2)
    if not (i == 0 and j in {1, 2})
)


DECOMP = (
    {"h2", "p", "q", "t2"},
    {"h3", "p", "q", "t1"},
    {"a3", "c", "h3", "p", "q"},
    {"c", "h1", "h2", "h3", "r"},
    {"a1", "a2", "c", "h1", "p", "q"},
    {"a1", "a2", "h1", "p", "q", "t3"},
    {"a2", "c", "h1", "h2", "p", "q"},
    {"c", "h1", "h2", "h3", "p", "q"},
)
TREE_EDGES = ((4, 5), (6, 4), (6, 7), (6, 0), (7, 2), (7, 3), (7, 1))

assert max(map(len, DECOMP)) == 6
assert set().union(*DECOMP) == V
assert all(any({left, right} <= bag for bag in DECOMP) for left, right in E)

tree_adjacency = {i: set() for i in range(len(DECOMP))}
for left, right in TREE_EDGES:
    tree_adjacency[left].add(right)
    tree_adjacency[right].add(left)
assert len(TREE_EDGES) == len(DECOMP) - 1
seen = {0}
while True:
    larger = seen | set().union(*(tree_adjacency[i] for i in seen))
    if larger == seen:
        break
    seen = larger
assert seen == set(range(len(DECOMP)))

for vertex in V:
    support = {i for i, bag in enumerate(DECOMP) if vertex in bag}
    reached = {next(iter(support))}
    while True:
        larger = reached | (
            set().union(*(tree_adjacency[i] for i in reached)) & support
        )
        if larger == reached:
            break
        reached = larger
    assert reached == support

print("GREEN: rooted-K4 quotient has K7^vee and treewidth at most five")
