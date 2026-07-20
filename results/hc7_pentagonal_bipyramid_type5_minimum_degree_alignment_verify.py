#!/usr/bin/env python3
"""Verify the canonical type-5 minimum-degree alignment theorem.

The proof itself is the explicit model in the adjacent Markdown file.
This dependency-free script additionally checks the redundant count of 35
five-connected part-respecting supergraphs and all sixteen root choices.
"""

from itertools import combinations


V = ("a0", "a1", "d0", "d1", "b", "c1", "c2", "c3", "c4")


def e(x, y):
    return frozenset((x, y))


BASE = {
    e("a0", "a1"), e("d0", "d1"), e("a0", "d0"), e("a1", "d1"),
    e("a0", "c4"), e("a1", "c1"), e("a1", "c2"), e("a1", "c3"),
    e("b", "d1"), e("b", "c1"), e("b", "c2"), e("b", "c3"),
    e("b", "c4"), e("d0", "c1"), e("d1", "c4"),
    e("c1", "c2"), e("c2", "c3"), e("c3", "c4"),
}

OPTIONAL = (
    e("b", "d0"), e("a0", "c1"), e("d1", "c1"),
    e("a0", "c2"), e("a0", "c3"), e("a1", "c4"),
    e("d0", "c4"), e("a0", "d1"), e("a1", "d0"),
)

MODEL = (
    {"b"}, {"d0", "d1"}, {"c1"}, {"a0", "c2"}, {"a1", "c3"}
)


def adjacent(edges, x, y):
    return x != y and e(x, y) in edges


def connected(edges, vertices):
    vertices = set(vertices)
    if not vertices:
        return False
    seen = {next(iter(vertices))}
    todo = list(seen)
    while todo:
        x = todo.pop()
        for y in vertices - seen:
            if adjacent(edges, x, y):
                seen.add(y)
                todo.append(y)
    return seen == vertices


def five_connected(edges):
    for size in range(5):
        for deleted in combinations(V, size):
            if not connected(edges, set(V) - set(deleted)):
                return False
    return True


def verify_model(edges, left, right):
    assert len(set().union(*MODEL)) == sum(map(len, MODEL))
    assert all(connected(edges, bag) for bag in MODEL)
    for first, second in combinations(MODEL, 2):
        assert any(adjacent(edges, x, y) for x in first for y in second)
    assert all(bag & left and bag & right for bag in MODEL)


five_connected_count = 0
for mask in range(1 << len(OPTIONAL)):
    edges = BASE | {
        OPTIONAL[i] for i in range(len(OPTIONAL)) if mask & (1 << i)
    }
    if not five_connected(edges):
        continue
    five_connected_count += 1
    assert e("a0", "c2") in edges
    for roots in range(16):
        left = {"b", "c1", "c2", "c3", "c4"}
        right = set(left)
        left.add(("a0", "a1")[(roots >> 0) & 1])
        right.add(("a0", "a1")[(roots >> 1) & 1])
        left.add(("d0", "d1")[(roots >> 2) & 1])
        right.add(("d0", "d1")[(roots >> 3) & 1])
        verify_model(edges, left, right)

assert five_connected_count == 35
print("GREEN type-5 minimum-degree alignment: 35 supergraphs, 16 roots each")
