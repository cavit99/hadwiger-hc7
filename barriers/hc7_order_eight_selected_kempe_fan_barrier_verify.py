#!/usr/bin/env python3
"""Verify the selected-Kempe-fan barrier at the exact order-eight boundary.

The script uses only the Python standard library.  It checks the literal
graph, a spherical triangulation certificate for the icosahedron,
connectivity, the exact separator and spanning near-clique model, all three
colourings, the ten bichromatic paths, and the claimed separators.
"""

from collections import Counter
from itertools import combinations


TOP = "t"
BOTTOM = "d"
UPPER = tuple(f"u{i}" for i in range(5))
LOWER = tuple(f"w{i}" for i in range(5))
APICES = ("p", "q")
ICO_VERTICES = (TOP, BOTTOM) + UPPER + LOWER
VERTICES = ICO_VERTICES + APICES


def edge_key(x, y):
    assert x != y
    return tuple(sorted((x, y)))


ICO_EDGES = set()
for i in range(5):
    ICO_EDGES.add(edge_key(TOP, UPPER[i]))
    ICO_EDGES.add(edge_key(BOTTOM, LOWER[i]))
    ICO_EDGES.add(edge_key(UPPER[i], UPPER[(i + 1) % 5]))
    ICO_EDGES.add(edge_key(LOWER[i], LOWER[(i + 1) % 5]))
    ICO_EDGES.add(edge_key(UPPER[i], LOWER[i]))
    ICO_EDGES.add(edge_key(UPPER[i], LOWER[(i - 1) % 5]))

EDGES = set(ICO_EDGES)
for apex in APICES:
    for vertex in ICO_VERTICES:
        EDGES.add(edge_key(apex, vertex))
EDGES.add(edge_key(*APICES))

ADJ = {vertex: set() for vertex in VERTICES}
for x, y in EDGES:
    ADJ[x].add(y)
    ADJ[y].add(x)


def is_edge(x, y):
    return edge_key(x, y) in EDGES


def connected(vertex_set):
    vertex_set = set(vertex_set)
    if not vertex_set:
        return False
    seen = {next(iter(vertex_set))}
    stack = list(seen)
    while stack:
        vertex = stack.pop()
        for neighbour in ADJ[vertex] & vertex_set:
            if neighbour not in seen:
                seen.add(neighbour)
                stack.append(neighbour)
    return seen == vertex_set


def components(vertex_set):
    remaining = set(vertex_set)
    answer = []
    while remaining:
        root = next(iter(remaining))
        part = {root}
        stack = [root]
        remaining.remove(root)
        while stack:
            vertex = stack.pop()
            for neighbour in ADJ[vertex] & remaining:
                remaining.remove(neighbour)
                part.add(neighbour)
                stack.append(neighbour)
        answer.append(frozenset(part))
    return answer


def adjacent_sets(left, right):
    return any(is_edge(x, y) for x in left for y in right)


def proper_colouring(host, colouring):
    host = set(host)
    return set(colouring) == host and all(
        colouring[x] != colouring[y]
        for x, y in EDGES
        if x in host and y in host
    )


def palette_at(root, colouring):
    return {colouring[v] for v in ADJ[root] if v in colouring}


def verify_path(path):
    assert len(path) == len(set(path))
    assert all(is_edge(x, y) for x, y in zip(path, path[1:]))


# A face certificate for the standard spherical embedding of I.
FACES = []
for i in range(5):
    FACES.append((TOP, UPPER[i], UPPER[(i + 1) % 5]))
    FACES.append((BOTTOM, LOWER[i], LOWER[(i + 1) % 5]))
    FACES.append((UPPER[i], UPPER[(i + 1) % 5], LOWER[i]))
    FACES.append((UPPER[i], LOWER[(i - 1) % 5], LOWER[i]))

assert len(ICO_VERTICES) == 12
assert len(ICO_EDGES) == 30
assert len(FACES) == 20
face_edge_counts = Counter()
for face in FACES:
    assert len(set(face)) == 3
    for x, y in combinations(face, 2):
        key = edge_key(x, y)
        assert key in ICO_EDGES
        face_edge_counts[key] += 1
assert set(face_edge_counts) == ICO_EDGES
assert set(face_edge_counts.values()) == {2}
assert len(ICO_VERTICES) - len(ICO_EDGES) + len(FACES) == 2
for vertex in ICO_VERTICES:
    link_edges = set()
    link_vertices = set()
    for face in FACES:
        if vertex in face:
            x, y = [item for item in face if item != vertex]
            link_vertices.update((x, y))
            link_edges.add(edge_key(x, y))
    link_adj = {item: set() for item in link_vertices}
    for x, y in link_edges:
        link_adj[x].add(y)
        link_adj[y].add(x)
    assert all(len(link_adj[item]) == 2 for item in link_vertices)
    seen = {next(iter(link_vertices))}
    stack = list(seen)
    while stack:
        item = stack.pop()
        for neighbour in link_adj[item]:
            if neighbour not in seen:
                seen.add(neighbour)
                stack.append(neighbour)
    assert seen == link_vertices

# Five-connectivity of I and seven-connectivity of G.
for order in range(5):
    for deleted in combinations(ICO_VERTICES, order):
        assert connected(set(ICO_VERTICES) - set(deleted))
for order in range(7):
    for deleted in combinations(VERTICES, order):
        assert connected(set(VERTICES) - set(deleted))

# The exact order-eight separator.
R = {"p", "q", "t"}
e = {"u0", "w0"}
f = {"u2", "w2"}
x = "d"
S = R | e | f | {x}
C = frozenset({"u3", "u4", "w3", "w4"})
D = frozenset({"u1", "w1"})
assert len(S) == 8
assert all(is_edge(y, z) for y, z in combinations(R, 2))
assert is_edge(*tuple(e)) and is_edge(*tuple(f))
assert not adjacent_sets(e, f)
assert all(any(is_edge(y, r) for y in e) for r in R)
assert all(any(is_edge(y, r) for y in f) for r in R)
assert set(components(set(VERTICES) - S)) == {C, D}
for part in (C, D):
    assert all(any(is_edge(s, vertex) for vertex in part) for s in S)

# The spanning singleton K7-minus-one-edge model.
a, b = "u0", "u2"
B_C = set(C)
B_D = set(D) | {"d", "w0", "w2"}
FRAME = [B_C, B_D, {"p"}, {"q"}, {"t"}]
MODEL = [{a}, {b}] + FRAME
assert set().union(*MODEL) == set(VERTICES)
assert sum(map(len, MODEL)) == len(VERTICES)
assert all(connected(bag) for bag in MODEL)
for i, left in enumerate(MODEL):
    for j, right in enumerate(MODEL[i + 1 :], i + 1):
        if {i, j} == {0, 1}:
            assert not adjacent_sets(left, right)
        else:
            assert adjacent_sets(left, right)

J = set(VERTICES) - {a, b}

# Exclusive deletion witness c_a.
c_a = {
    "d": 1,
    "u1": 1,
    "u3": 1,
    "w0": 2,
    "w3": 2,
    b: 2,
    "u4": 3,
    "w1": 3,
    "t": 4,
    "w2": 4,
    "w4": 4,
    "p": 5,
    "q": 6,
}
assert proper_colouring(set(VERTICES) - {a}, c_a)
assert palette_at(a, c_a) == set(range(1, 7))
assert c_a[b] not in palette_at(b, {v: c for v, c in c_a.items() if v != b})
paths_a = {
    1: [a, "u1", b],
    3: [a, "w0", "w1", b],
    4: [a, "t", b],
    5: [a, "p", b],
    6: [a, "q", b],
}
interiors_a = []
for beta, path in paths_a.items():
    verify_path(path)
    assert {c_a[v] for v in path[1:] if v in c_a} <= {2, beta}
    interiors_a.append(set(path[1:-1]))
assert all(not left & right for left, right in combinations(interiors_a, 2))

# Exclusive deletion witness c_b.
c_b = {
    "d": 1,
    "u3": 1,
    a: 1,
    "w0": 2,
    "w3": 2,
    "t": 2,
    "u4": 3,
    "w1": 3,
    "u1": 4,
    "w2": 4,
    "w4": 4,
    "p": 5,
    "q": 6,
}
assert proper_colouring(set(VERTICES) - {b}, c_b)
assert palette_at(b, c_b) == set(range(1, 7))
assert c_b[a] not in palette_at(a, {v: c for v, c in c_b.items() if v != a})
paths_b = {
    2: [b, "t", a],
    3: [b, "u3", "u4", a],
    4: [b, "u1", a],
    5: [b, "p", a],
    6: [b, "q", a],
}
interiors_b = []
for beta, path in paths_b.items():
    verify_path(path)
    assert {c_b[v] for v in path[1:] if v in c_b} <= {1, beta}
    interiors_b.append(set(path[1:-1]))
assert all(not left & right for left, right in combinations(interiors_b, 2))

# The six-colouring of J in which neither root sees every colour.
c_neither = {
    "d": 1,
    "u3": 1,
    "w0": 2,
    "w3": 2,
    "u1": 3,
    "u4": 3,
    "w2": 3,
    "t": 4,
    "w1": 4,
    "w4": 4,
    "p": 5,
    "q": 6,
}
assert proper_colouring(J, c_neither)
assert 1 not in palette_at(a, c_neither)
assert 2 not in palette_at(b, c_neither)

# Exact six-chromatic lower-bound certificate in J.
odd_wheel = {"d"} | set(LOWER)
assert all(is_edge("d", w) for w in LOWER)
assert all(is_edge(LOWER[i], LOWER[(i + 1) % 5]) for i in range(5))
assert all(is_edge(apex, vertex) for apex in APICES for vertex in odd_wheel)
assert is_edge("p", "q")

# A fan component with an actual order-nine, not order-seven, boundary.
two_three_vertices = {v for v, colour in c_a.items() if colour in {2, 3}}
component_at_b = next(part for part in components(two_three_vertices) if b in part)
K = frozenset({b, "w0", "w1"})
assert component_at_b == K
N_K = set().union(*(ADJ[vertex] for vertex in K)) - set(K)
assert N_K == {"d", "p", "q", "t", "u0", "u1", "u3", "w2", "w4"}
assert len(N_K) == 9
assert set(components(set(VERTICES) - N_K)) == {K, frozenset({"u4", "w3"})}

# The roots are not a K5 transversal, but the apex pair is; an exact 7-cut exists.
literal_k5 = {"p", "q", "t", "u3", "u4"}
assert literal_k5 <= J
assert all(is_edge(y, z) for y, z in combinations(literal_k5, 2))
order_seven_cut = {"p", "q", "u0", "u1", "u2", "u3", "u4"}
remaining_components = set(components(set(VERTICES) - order_seven_cut))
assert remaining_components == {
    frozenset({"t"}),
    frozenset({"d", "w0", "w1", "w2", "w3", "w4"}),
}

print("icosahedron certificate: 12 vertices, 30 edges, 20 triangular faces")
print("connectivity checks: I is 5-connected; G is 7-connected")
print("exact boundary components:", sorted((sorted(C), sorted(D))))
print("spanning near-K7 bag orders:", [len(bag) for bag in MODEL])
print("exclusive fan paths: 5 + 5, internally disjoint in each witness")
print("selected {2,3}-component boundary order:", len(N_K))
print("universal saturation: explicitly false")
print("ALL CHECKS PASSED")
