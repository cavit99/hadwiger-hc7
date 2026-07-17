#!/usr/bin/env python3
"""Verify the exact three-common-row geodesic two-apex barrier."""

from itertools import combinations


TOP, BOTTOM = 10, 11
APEX_S, APEX_T = 42, 43


def edge(a, b):
    return tuple(sorted((a, b)))


# Icosahedron used as the frequency-two triangulation's base.
icosahedron_edges = set()
for i in range(5):
    icosahedron_edges.update(
        {
            edge(TOP, i),
            edge(BOTTOM, 5 + i),
            edge(i, (i + 1) % 5),
            edge(5 + i, 5 + (i + 1) % 5),
            edge(i, 5 + i),
            edge(i, 5 + (i - 1) % 5),
        }
    )

faces = [
    triple
    for triple in combinations(range(12), 3)
    if all(edge(a, b) in icosahedron_edges for a, b in combinations(triple, 2))
]
assert len(icosahedron_edges) == 30
assert len(faces) == 20

midpoint = {e: 12 + i for i, e in enumerate(sorted(icosahedron_edges))}
planar_edges = set()
for a, b in icosahedron_edges:
    m = midpoint[edge(a, b)]
    planar_edges.update({edge(a, m), edge(m, b)})
for a, b, c in faces:
    mab = midpoint[edge(a, b)]
    mbc = midpoint[edge(b, c)]
    mca = midpoint[edge(c, a)]
    planar_edges.update({edge(mab, mbc), edge(mbc, mca), edge(mca, mab)})

# The lexicographically first face is (0,1,5).
assert faces[0] == (0, 1, 5)
Z = midpoint[edge(0, 1)]
U = midpoint[edge(1, 5)]
W = midpoint[edge(0, 5)]
assert (Z, U, W) == (12, 18, 14)
assert edge(Z, U) in planar_edges
assert edge(Z, W) in planar_edges
planar_edges.remove(edge(Z, W))


def adjacency(vertices, edges):
    result = {v: set() for v in vertices}
    for a, b in edges:
        if a in result and b in result:
            result[a].add(b)
            result[b].add(a)
    return result


def connected(vertices, adj):
    vertices = set(vertices)
    if not vertices:
        return True
    seen = {next(iter(vertices))}
    todo = list(seen)
    while todo:
        v = todo.pop()
        for w in adj[v] & vertices - seen:
            seen.add(w)
            todo.append(w)
    return seen == vertices


P_VERTICES = set(range(42))
P_ADJ = adjacency(P_VERTICES, planar_edges)


def verify_five_connectivity():
    assert len(planar_edges) == 119
    assert min(map(len, P_ADJ.values())) == 5
    for size in range(5):
        for deleted in combinations(P_VERTICES, size):
            assert connected(P_VERTICES - set(deleted), P_ADJ)


# Add the adjacent universal pair.
G_VERTICES = set(range(44))
graph_edges = set(planar_edges)
for apex in (APEX_S, APEX_T):
    for v in P_VERTICES:
        graph_edges.add(edge(apex, v))
graph_edges.add(edge(APEX_S, APEX_T))
G_ADJ = adjacency(G_VERTICES, graph_edges)

MODEL = [
    {APEX_S},
    {APEX_T},
    {1},
    {
        0,
        4,
        8,
        9,
        10,
        11,
        13,
        15,
        16,
        20,
        24,
        25,
        27,
        28,
        29,
        30,
        31,
        33,
        34,
        36,
        37,
        38,
        39,
        40,
        41,
    },
    {5, 6, 7, 14, 19, 22, 23, 26, 32, 35},
    {2, 3, 17, 21},
]


def touch(left, right):
    return any(G_ADJ[v] & set(right) for v in left)


def verify_model_and_contacts():
    assert set().union(*MODEL) == G_VERTICES - {Z, U}
    assert sum(map(len, MODEL)) == 42
    assert all(connected(bag, G_ADJ) for bag in MODEL)
    assert all(
        touch(MODEL[i], MODEL[j]) for i in range(6) for j in range(i + 1, 6)
    )

    z_contacts = [G_ADJ[Z] & bag for bag in MODEL]
    u_contacts = [G_ADJ[U] & bag for bag in MODEL]
    assert z_contacts == [{42}, {43}, {1}, {0, 16, 20}, set(), set()]
    assert u_contacts == [{42}, {43}, {1}, set(), {5, 14, 19, 32}, set()]


COLOUR_CLASSES = {
    0: {10, 12, 13, 17, 18, 21, 25, 33, 36, 37, 39},
    1: {2, 15, 16, 19, 26, 28, 29, 34, 35, 40},
    2: {0, 5, 6, 20, 23, 27, 30, 31, 38, 41},
    3: {1, 3, 4, 7, 8, 9, 11, 14, 22, 24, 32},
    4: {APEX_S},
    5: {APEX_T},
}
COLOUR = {v: colour for colour, vertices in COLOUR_CLASSES.items() for v in vertices}


def verify_colouring_and_kempe_connections():
    assert set(COLOUR) == G_VERTICES
    for a, b in graph_edges - {edge(Z, U)}:
        assert COLOUR[a] != COLOUR[b]
    assert COLOUR[Z] == COLOUR[U] == 0
    assert any(v not in {Z, U} and COLOUR[v] == 0 for v in G_VERTICES)
    assert not any(COLOUR[v] == 0 for v in (G_ADJ[Z] | G_ADJ[U]) - {Z, U})
    assert {COLOUR[v] for v in G_ADJ[Z] - {U}} == {1, 2, 3, 4, 5}
    assert {COLOUR[v] for v in G_ADJ[U] - {Z}} == {1, 2, 3, 4, 5}

    deletion_adj = adjacency(G_VERTICES, graph_edges - {edge(Z, U)})
    for beta in range(1, 6):
        allowed = {v for v in G_VERTICES if COLOUR[v] in {0, beta}}
        seen = {Z}
        todo = [Z]
        while todo:
            v = todo.pop()
            for w in deletion_adj[v] & allowed - seen:
                seen.add(w)
                todo.append(w)
        assert U in seen

    paths = ([16, 20, 1, 19], [0, 14, 5])
    assert set(paths[0]).isdisjoint(paths[1])
    assert all(edge(a, b) in graph_edges for path in paths for a, b in zip(path, path[1:]))
    assert paths[0][0] in MODEL[3] and paths[0][-1] in MODEL[4]
    assert paths[1][0] in MODEL[3] and paths[1][-1] in MODEL[4]
    assert {COLOUR[paths[i][0]] for i in range(2)} == {1, 2}
    assert {COLOUR[paths[i][-1]] for i in range(2)} == {1, 2}


def verify_order_seven_separator():
    separator = set(G_ADJ[Z])
    assert len(separator) == 7
    remainder = G_VERTICES - separator
    assert Z in remainder and len(remainder) > 1
    assert not connected(remainder, G_ADJ)


if __name__ == "__main__":
    verify_five_connectivity()
    verify_model_and_contacts()
    verify_colouring_and_kempe_connections()
    verify_order_seven_separator()
    print(
        "GREEN: exact c=3 profile, buffer-colour locks and two-linkage; "
        "the sharp output is the order-seven separator/two-apex pair"
    )
