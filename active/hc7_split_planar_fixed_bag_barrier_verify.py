#!/usr/bin/env python3
"""Verify the finite fixed-bag exchange barrier in the split-planar note.

Run from the repository root:

    python3 active/hc7_split_planar_fixed_bag_barrier_verify.py

Expected output:

    split-planar fixed-bag barrier: verified
"""

from itertools import combinations


VERTICES = set(range(10))
EDGES = {
    tuple(sorted((int(edge[0]), int(edge[1]))))
    for edge in (
        "03 04 06 08 09 13 15 16 17 18 24 25 27 "
        "28 29 36 38 39 46 47 49 57 58 59 67 89"
    ).split()
}
T = {0, 2, 6, 7, 8, 9}


def adjacent(u, v, edges=EDGES):
    return tuple(sorted((u, v))) in edges


def components(vertices, edges=EDGES):
    vertices = set(vertices)
    answer = []
    while vertices:
        start = min(vertices)
        reached = {start}
        stack = [start]
        while stack:
            u = stack.pop()
            for v in tuple(vertices - reached):
                if tuple(sorted((u, v))) in edges:
                    reached.add(v)
                    stack.append(v)
        answer.append(reached)
        vertices -= reached
    return answer


def is_k_connected(vertices, edges, k):
    vertices = set(vertices)
    if len(vertices) <= k:
        return False
    for size in range(k):
        for deleted in combinations(sorted(vertices), size):
            if len(components(vertices - set(deleted), edges)) != 1:
                return False
    return True


def contract_89():
    vertices = set(range(9))
    edges = set()
    for u, v in EDGES:
        u = 8 if u == 9 else u
        v = 8 if v == 9 else v
        if u != v:
            edges.add(tuple(sorted((u, v))))
    return vertices, edges


def graph6(vertices, edges):
    vertices = sorted(vertices)
    assert vertices == list(range(len(vertices))) and len(vertices) <= 62
    bits = []
    for j in range(len(vertices)):
        for i in range(j):
            bits.append(int((i, j) in edges))
    while len(bits) % 6:
        bits.append(0)
    encoded = [chr(len(vertices) + 63)]
    for offset in range(0, len(bits), 6):
        value = 0
        for bit in bits[offset : offset + 6]:
            value = 2 * value + bit
        encoded.append(chr(value + 63))
    return "".join(encoded)


def verify_planar_faces(vertices, edges):
    faces = [
        (0, 6, 3),
        (0, 4, 6),
        (0, 8, 4),
        (0, 3, 8),
        (1, 5, 8),
        (1, 7, 5),
        (1, 6, 7),
        (1, 8, 3),
        (1, 3, 6),
        (2, 4, 8),
        (2, 7, 4),
        (2, 8, 5),
        (2, 5, 7),
        (4, 7, 6),
    ]
    darts = []
    for face in faces:
        darts.extend(zip(face, face[1:] + face[:1]))
    expected = {(u, v) for edge in edges for u, v in (edge, edge[::-1])}
    assert set(darts) == expected and len(darts) == len(expected)
    assert len(vertices) - len(edges) + len(faces) == 2


def connected(branch):
    return len(components(branch)) == 1


def q_edge(i, j):
    return abs(i - j) >= 2


def q_model(branches):
    if set().union(*branches) != VERTICES:
        return False
    if sum(map(len, branches)) != len(VERTICES):
        return False
    if not all(connected(branch) for branch in branches):
        return False
    for i, j in combinations(range(7), 2):
        if q_edge(i, j) and not any(
            adjacent(u, v) for u in branches[i] for v in branches[j]
        ):
            return False
    return True


def neighbourhood(component):
    return {
        v
        for u in component
        for v in VERTICES - component
        if adjacent(u, v)
    }


def main():
    assert is_k_connected(VERTICES, EDGES, 5)

    contracted_vertices, contracted_edges = contract_89()
    assert is_k_connected(contracted_vertices, contracted_edges, 4)
    verify_planar_faces(contracted_vertices, contracted_edges)
    assert graph6(contracted_vertices, contracted_edges) == "HEher^{"

    outside = components(VERTICES - T)
    assert {frozenset(part) for part in outside} == {
        frozenset({4}),
        frozenset({1, 3, 5}),
    }
    assert neighbourhood({4}) == T - {8}
    assert neighbourhood({1, 3, 5}) == T

    original = [
        {0, 1, 6},
        {2},
        {5},
        {4},
        {3, 8},
        {7},
        {9},
    ]
    assert q_model(original)
    assert sum(bool(branch & T) for branch in original) == 5

    for root in (0, 6):
        for target in (2, 3):
            moved = [set(branch) for branch in original]
            moved[0].remove(root)
            moved[target].add(root)
            assert not q_model(moved)

    reselected = [
        {0, 1, 3},
        {2},
        {5},
        {4, 6},
        {8},
        {7},
        {9},
    ]
    assert q_model(reselected)
    assert sum(bool(branch & T) for branch in reselected) == 6

    print("split-planar fixed-bag barrier: verified")


if __name__ == "__main__":
    main()
