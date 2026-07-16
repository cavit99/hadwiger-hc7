#!/usr/bin/env python3
"""Verify the sharp icosahedral example for the K2-join dichotomy."""

from collections import Counter
from itertools import combinations


I_VERTICES = tuple(range(12))
I_EDGES = {
    tuple(sorted(edge))
    for edge in (
        (0, 1), (0, 5), (0, 7), (0, 8), (0, 11),
        (1, 2), (1, 5), (1, 6), (1, 8),
        (2, 3), (2, 6), (2, 8), (2, 9),
        (3, 4), (3, 6), (3, 9), (3, 10),
        (4, 5), (4, 6), (4, 10), (4, 11),
        (5, 6), (5, 11),
        (7, 8), (7, 9), (7, 10), (7, 11),
        (8, 9), (9, 10), (10, 11),
    )
}


def edge_key(x, y):
    return tuple(sorted((x, y), key=str))


def adjacency(vertices, edges):
    answer = {vertex: set() for vertex in vertices}
    for x, y in edges:
        answer[x].add(y)
        answer[y].add(x)
    return answer


def connected(vertex_set, adj):
    vertex_set = set(vertex_set)
    if not vertex_set:
        return False
    seen = {next(iter(vertex_set))}
    stack = list(seen)
    while stack:
        vertex = stack.pop()
        for neighbour in adj[vertex] & vertex_set:
            if neighbour not in seen:
                seen.add(neighbour)
                stack.append(neighbour)
    return seen == vertex_set


def adjacent_sets(left, right, edges):
    return any(edge_key(x, y) in edges for x in left for y in right)


I_ADJ = adjacency(I_VERTICES, I_EDGES)

# A checkable spherical-triangulation certificate for planarity.
triangles = [
    tuple(sorted(triple))
    for triple in combinations(I_VERTICES, 3)
    if all(tuple(sorted(edge)) in I_EDGES for edge in combinations(triple, 2))
]
assert len(I_VERTICES) == 12
assert len(I_EDGES) == 30
assert len(triangles) == 20
triangle_edge_count = Counter(
    tuple(sorted(edge)) for face in triangles for edge in combinations(face, 2)
)
assert set(triangle_edge_count) == I_EDGES
assert set(triangle_edge_count.values()) == {2}
assert len(I_VERTICES) - len(I_EDGES) + len(triangles) == 2
for vertex in I_VERTICES:
    link_edges = {
        tuple(sorted(face - {vertex}))
        for raw_face in triangles
        for face in [set(raw_face)]
        if vertex in face
    }
    link_vertices = set().union(*map(set, link_edges))
    link_adj = adjacency(link_vertices, link_edges)
    assert all(len(link_adj[x]) == 2 for x in link_vertices)
    assert connected(link_vertices, link_adj)

# I is five-connected.
for order in range(5):
    for deleted in combinations(I_VERTICES, order):
        assert connected(set(I_VERTICES) - set(deleted), I_ADJ)

# Form G=K2 join I.
G_VERTICES = I_VERTICES + ("p", "q")
G_EDGES = {edge_key(*edge) for edge in I_EDGES}
G_EDGES.add(edge_key("p", "q"))
for apex in ("p", "q"):
    G_EDGES |= {edge_key(apex, vertex) for vertex in I_VERTICES}
G_ADJ = adjacency(G_VERTICES, G_EDGES)

# G is seven-connected.
for order in range(7):
    for deleted in combinations(G_VERTICES, order):
        assert connected(set(G_VERTICES) - set(deleted), G_ADJ)

# The explicit spanning singleton-root K7-minus-one-edge model.
MODEL = [
    {0},
    {2},
    {"p"},
    {"q"},
    {1, 3, 4, 5, 6},
    {7, 8},
    {9, 10, 11},
]
assert set().union(*MODEL) == set(G_VERTICES)
assert sum(map(len, MODEL)) == len(G_VERTICES)
assert all(connected(bag, G_ADJ) for bag in MODEL)
missing_pairs = [
    (left, right)
    for left, right in combinations(MODEL, 2)
    if not adjacent_sets(left, right, G_EDGES)
]
assert missing_pairs == [({0}, {2})]

# The normalized dominating-cycle substrate in J=G-{0,2}.
X, Y, C = {"p"}, {"q"}, {1, 5, 6}
assert connected(X, G_ADJ) and connected(Y, G_ADJ)
assert adjacent_sets(X, Y, G_EDGES)
assert all(any(edge_key(x, y) in G_EDGES for x in X) for y in Y)
assert all(
    adjacent_sets({cycle_vertex}, root_set, G_EDGES)
    for cycle_vertex in C
    for root_set in (X, Y)
)
assert all(edge_key(*edge) in G_EDGES for edge in combinations(C, 2))

# The actual order-seven separator.
separator = {"p", "q"} | I_ADJ[0]
assert len(separator) == 7
remaining = set(G_VERTICES) - separator
assert 0 in remaining and len(remaining) == 7
assert not connected(remaining, G_ADJ)
assert not (G_ADJ[0] & (remaining - {0}))

print("icosahedral factor: spherical triangulation and 5-connectivity verified")
print("join: 7-connectivity verified")
print("spanning singleton-root K7-minus-one-edge model verified")
print("normalized dominating-cycle substrate verified")
print("actual order-seven separator verified")
print("ALL CHECKS PASSED")
