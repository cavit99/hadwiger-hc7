#!/usr/bin/env python3
"""Verify the two-root Kempe-class icosahedron barrier.

The script uses only the Python standard library.  It checks the
icosahedral triangulation, the connectivity claims, all four-colourings,
the ten Kempe classes and their root orientations, the spanning labelled
minor models, and every root-edge exact trace in the icosahedral factor.
"""

from collections import Counter
from itertools import combinations


ICO_VERTICES = tuple(range(12))
ICO_EDGES = {
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

A_NEIGHBOURS = frozenset({0, 1, 2, 3, 5})
B_NEIGHBOURS = frozenset({2, 3, 4, 8, 11})


def edge_key(x, y):
    assert x != y
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


def all_colourings(vertices, adj, number_of_colours):
    order = sorted(vertices, key=lambda v: (-len(adj[v]), str(v)))
    current = {}
    answer = []

    def search(index):
        if index == len(order):
            answer.append(dict(current))
            return
        vertex = order[index]
        forbidden = {current[u] for u in adj[vertex] if u in current}
        for colour in range(number_of_colours):
            if colour not in forbidden:
                current[vertex] = colour
                search(index + 1)
        current.pop(vertex, None)

    search(0)
    return answer


def is_colourable(vertices, adj, number_of_colours):
    order = sorted(vertices, key=lambda v: (-len(adj[v]), str(v)))
    current = {}

    def search(index):
        if index == len(order):
            return True
        vertex = order[index]
        forbidden = {current[u] for u in adj[vertex] if u in current}
        for colour in range(number_of_colours):
            if colour not in forbidden:
                current[vertex] = colour
                if search(index + 1):
                    return True
        current.pop(vertex, None)
        return False

    return search(0)


def contracted_graph(vertices, edges, left, right):
    merged = f"[{left},{right}]"
    new_vertices = tuple(v for v in vertices if v not in {left, right}) + (merged,)

    def image(vertex):
        return merged if vertex in {left, right} else vertex

    new_edges = set()
    for x, y in edges:
        x_image, y_image = image(x), image(y)
        if x_image != y_image:
            new_edges.add(edge_key(x_image, y_image))
    return new_vertices, new_edges, adjacency(new_vertices, new_edges)


def partition(colouring, vertices, number_of_colours):
    return tuple(
        sorted(
            tuple(sorted(v for v in vertices if colouring[v] == colour))
            for colour in range(number_of_colours)
        )
    )


def dominates(neighbourhood, colouring):
    return len({colouring[v] for v in neighbourhood}) == 4


ICO_ADJ = adjacency(ICO_VERTICES, ICO_EDGES)

# Spherical triangulation certificate: the twenty triangles form a closed
# two-manifold with Euler characteristic two.
triangles = [
    tuple(sorted(triple))
    for triple in combinations(ICO_VERTICES, 3)
    if all(tuple(sorted(edge)) in ICO_EDGES for edge in combinations(triple, 2))
]
assert len(ICO_VERTICES) == 12
assert len(ICO_EDGES) == 30
assert len(triangles) == 20
triangle_edge_count = Counter(
    tuple(sorted(edge)) for face in triangles for edge in combinations(face, 2)
)
assert set(triangle_edge_count) == ICO_EDGES
assert set(triangle_edge_count.values()) == {2}
assert len(ICO_VERTICES) - len(ICO_EDGES) + len(triangles) == 2
for vertex in ICO_VERTICES:
    link_edges = {
        tuple(sorted(face - {vertex}))
        for raw_face in triangles
        for face in [set(raw_face)]
        if vertex in face
    }
    link_vertices = set().union(*map(set, link_edges))
    link_adj = adjacency(link_vertices, link_edges)
    assert all(len(link_adj[v]) == 2 for v in link_vertices)
    assert connected(link_vertices, link_adj)

# Five-connectivity of I.
for order in range(5):
    for deleted in combinations(ICO_VERTICES, order):
        assert connected(set(ICO_VERTICES) - set(deleted), ICO_ADJ)

# Build F=I+{a,b} and G=K2 join F.
F_VERTICES = ICO_VERTICES + ("a", "b")
F_EDGES = {edge_key(*edge) for edge in ICO_EDGES}
F_EDGES |= {edge_key("a", v) for v in A_NEIGHBOURS}
F_EDGES |= {edge_key("b", v) for v in B_NEIGHBOURS}
F_ADJ = adjacency(F_VERTICES, F_EDGES)

G_VERTICES = F_VERTICES + ("p", "q")
G_EDGES = set(F_EDGES)
G_EDGES.add(edge_key("p", "q"))
for apex in ("p", "q"):
    G_EDGES |= {edge_key(apex, v) for v in F_VERTICES}
G_ADJ = adjacency(G_VERTICES, G_EDGES)

# F is five-connected and G is exactly seven-connected.
for order in range(5):
    for deleted in combinations(F_VERTICES, order):
        assert connected(set(F_VERTICES) - set(deleted), F_ADJ)
for order in range(7):
    for deleted in combinations(G_VERTICES, order):
        assert connected(set(G_VERTICES) - set(deleted), G_ADJ)
assert len(G_ADJ["a"]) == 7
assert not connected(set(G_VERTICES) - G_ADJ["a"], G_ADJ)

# Enumerate the complete four-colouring space of I.
colourings = all_colourings(ICO_VERTICES, ICO_ADJ, 4)
assert len(colourings) == 240
partitions = {}
for colouring in colourings:
    key = partition(colouring, ICO_VERTICES, 4)
    status = (
        "AB" if dominates(A_NEIGHBOURS, colouring)
        and dominates(B_NEIGHBOURS, colouring)
        else "A" if dominates(A_NEIGHBOURS, colouring)
        else "B" if dominates(B_NEIGHBOURS, colouring)
        else "--"
    )
    partitions.setdefault(key, set()).add(status)

expected = {
    ((0, 2, 4), (1, 3, 7), (5, 8, 10), (6, 9, 11)): "B",
    ((0, 2, 4), (1, 9, 11), (3, 5, 7), (6, 8, 10)): "B",
    ((0, 2, 10), (1, 4, 7), (3, 5, 8), (6, 9, 11)): "B",
    ((0, 2, 10), (1, 4, 9), (3, 5, 7), (6, 8, 11)): "B",
    ((0, 4, 9), (1, 3, 7), (2, 5, 10), (6, 8, 11)): "B",
    ((0, 4, 9), (1, 3, 11), (2, 5, 7), (6, 8, 10)): "B",
    ((0, 6, 9), (1, 3, 11), (2, 4, 7), (5, 8, 10)): "A",
    ((0, 6, 9), (1, 4, 7), (2, 5, 10), (3, 8, 11)): "A",
    ((0, 6, 10), (1, 4, 9), (2, 5, 7), (3, 8, 11)): "A",
    ((0, 6, 10), (1, 9, 11), (2, 4, 7), (3, 5, 8)): "A",
}
assert {key: next(iter(value)) for key, value in partitions.items()} == expected
assert all(len(value) == 1 for value in partitions.values())
assert Counter(expected.values()) == Counter({"A": 4, "B": 6})

# Every two colour classes induce a connected graph.  Hence every Kempe
# interchange only permutes whole classes, and each unordered partition is
# one Kempe component (720 six-colourings after adjoining p,q).
for blocks in expected:
    for left, right in combinations(blocks, 2):
        assert connected(set(left) | set(right), ICO_ADJ)
assert len(expected) == 10
assert 720 == 6 * 5 * 4 * 3 * 2

# The spanning root-adjacent K5 model in J.
J_MODEL = [
    {"p"},
    {"q"},
    {0, 1, 2},
    {3},
    {4, 5, 6, 7, 8, 9, 10, 11},
]
assert set().union(*J_MODEL) == set(ICO_VERTICES) | {"p", "q"}
assert sum(map(len, J_MODEL)) == 14
assert all(connected(bag, G_ADJ) for bag in J_MODEL)
assert all(adjacent_sets(x, y, G_EDGES) for x, y in combinations(J_MODEL, 2))
for root in ("a", "b"):
    assert all(adjacent_sets({root}, bag, G_EDGES) for bag in J_MODEL)

# Exact root-edge traces inside the icosahedral factor.  For a root r and
# neighbour s, find an exclusive colouring in which s is the unique
# r-neighbour of its colour.  Assigning the other root a missed colour is
# exactly a four-colouring of F/rs.
def has_exact_trace(root_neighbours, other_neighbours, orientation, s):
    for colouring in colourings:
        if orientation == "A":
            exclusive = dominates(A_NEIGHBOURS, colouring) and not dominates(
                B_NEIGHBOURS, colouring
            )
        else:
            exclusive = dominates(B_NEIGHBOURS, colouring) and not dominates(
                A_NEIGHBOURS, colouring
            )
        if not exclusive:
            continue
        if sum(
            colouring[v] == colouring[s] for v in root_neighbours
        ) != 1:
            continue
        if len({colouring[v] for v in other_neighbours}) < 4:
            return True
    return False


assert all(
    has_exact_trace(A_NEIGHBOURS, B_NEIGHBOURS, "A", s)
    for s in A_NEIGHBOURS
)
assert all(
    has_exact_trace(B_NEIGHBOURS, A_NEIGHBOURS, "B", s)
    for s in B_NEIGHBOURS
)
for root, neighbours in (("a", A_NEIGHBOURS), ("b", B_NEIGHBOURS)):
    for s in neighbours:
        vertices, edges, adj = contracted_graph(F_VERTICES, F_EDGES, root, s)
        assert is_colourable(vertices, adj, 4)

# Explicit K7 model and the actual order-seven separator.
K7_MODEL = [
    {"p"},
    {"q"},
    {0, 7, 8, 11},
    {"a", 1, 2, 5},
    {3, 9, 10},
    {4, 6},
    {"b"},
]
assert all(connected(bag, G_ADJ) for bag in K7_MODEL)
assert all(adjacent_sets(x, y, G_EDGES) for x, y in combinations(K7_MODEL, 2))
assert G_ADJ["a"] == {"p", "q", 0, 1, 2, 3, 5}
remaining = set(G_VERTICES) - G_ADJ["a"]
assert "a" in remaining and len(remaining) > 1
assert not connected(remaining, G_ADJ)

print("icosahedron colourings: 240 labelled, 10 unordered partitions")
print("Kempe components in J: 10 of order 720; orientations 4 A-only + 6 B-only")
print("ambient connectivity: 7; root a has an actual order-seven neighbourhood cut")
print("spanning root-adjacent K5 model: verified")
print("root-edge exact traces in I: 5 at a + 5 at b")
print("explicit K7 model: verified")
print("ALL CHECKS PASSED")
