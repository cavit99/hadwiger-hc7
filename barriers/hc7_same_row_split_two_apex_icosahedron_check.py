#!/usr/bin/env python3
"""Dependency-free verifier for the two-apex icosahedron barrier."""

from itertools import combinations


TOP, BOTTOM = 10, 11
APEX_A, APEX_B = 12, 13
Z, U = TOP, 0


def edge(a, b):
    return tuple(sorted((a, b)))


I_EDGES = set()
for i in range(5):
    I_EDGES.update(
        {
            edge(TOP, i),
            edge(BOTTOM, 5 + i),
            edge(i, (i + 1) % 5),
            edge(5 + i, 5 + (i + 1) % 5),
            edge(i, 5 + i),
            edge(i, 5 + (i - 1) % 5),
        }
    )

G_EDGES = set(I_EDGES)
for apex in (APEX_A, APEX_B):
    for v in range(12):
        G_EDGES.add(edge(apex, v))
G_EDGES.add(edge(APEX_A, APEX_B))


def adjacent(v, w, edges=G_EDGES):
    return edge(v, w) in edges


def connected(vertices, edges=G_EDGES):
    vertices = set(vertices)
    if not vertices:
        return False
    seen = {next(iter(vertices))}
    todo = list(seen)
    while todo:
        v = todo.pop()
        for w in vertices - seen:
            if adjacent(v, w, edges):
                seen.add(w)
                todo.append(w)
    return seen == vertices


def touch(left, right, edges=G_EDGES):
    return any(adjacent(v, w, edges) for v in left for w in right)


def verify_connectivity():
    vertices = set(range(14))
    for k in range(7):
        for deleted in combinations(vertices, k):
            assert connected(vertices - set(deleted))
    cut = {APEX_A, APEX_B}
    cut.update(v for v in range(12) if adjacent(0, v, I_EDGES))
    assert len(cut) == 7
    assert not connected(vertices - cut)


MODEL = [
    {3, 4},       # F_h
    {5, 9},       # F_1
    {1, 2},       # F_2
    {6, 7},       # F_3
    {APEX_A, 8},  # F_4
    {APEX_B, 11}, # F_5
]


def verify_model_and_split_failure():
    assert set().union(*MODEL) == set(range(14)) - {Z, U}
    assert sum(map(len, MODEL)) == 12
    assert all(len(bag) == 2 and connected(bag) for bag in MODEL)
    assert all(
        not (MODEL[i] & MODEL[j]) and touch(MODEL[i], MODEL[j])
        for i in range(6)
        for j in range(i + 1, 6)
    )

    path = [7, 3, Z, U, 4, 8]
    assert all(adjacent(v, w) for v, w in zip(path, path[1:]))
    assert adjacent(7, 8)

    row = MODEL[0]
    portals = [
        {v for v in row if touch({v}, MODEL[i])} for i in range(1, 6)
    ]
    assert portals == [{4}, {3}, {3}, {3, 4}, {3, 4}]

    connected_subsets = []
    row_list = sorted(row)
    for mask in range(1, 1 << len(row_list)):
        part = {row_list[i] for i in range(len(row_list)) if mask & (1 << i)}
        if connected(part):
            connected_subsets.append(part)
    for x_side in connected_subsets:
        for u_side in connected_subsets:
            if x_side & u_side:
                continue
            x_ok = touch({Z}, x_side) and all(
                touch(x_side, MODEL[i]) for i in range(1, 6)
            )
            u_ok = touch({U}, u_side) and all(
                touch(u_side, MODEL[i]) for i in range(1, 6)
            )
            assert not (x_ok and u_ok)


def connected_subsets_of_icosahedron_without_poles():
    vertices = sorted(set(range(12)) - {Z, U})
    adjacency = {v: set() for v in range(12)}
    for v, w in I_EDGES:
        adjacency[v].add(w)
        adjacency[w].add(v)

    def is_connected(part):
        part = set(part)
        seen = {next(iter(part))}
        todo = list(seen)
        while todo:
            v = todo.pop()
            for w in adjacency[v] & part:
                if w not in seen:
                    seen.add(w)
                    todo.append(w)
        return seen == part

    subsets = []
    for mask in range(1, 1 << len(vertices)):
        part = frozenset(
            vertices[i] for i in range(len(vertices)) if mask & (1 << i)
        )
        if is_connected(part):
            subsets.append(part)
    return subsets, adjacency


def verify_contact_maximum():
    subsets, adjacency = connected_subsets_of_icosahedron_without_poles()

    def base_touch(left, right):
        return any(adjacency[v] & set(right) for v in left)

    best = (-1, -1)
    count = 0
    for a_index, a in enumerate(subsets):
        for b_index in range(a_index + 1, len(subsets)):
            b = subsets[b_index]
            if a & b or not base_touch(a, b):
                continue
            for c_index in range(b_index + 1, len(subsets)):
                c = subsets[c_index]
                if c & (a | b) or not base_touch(a, c) or not base_touch(b, c):
                    continue
                for d_index in range(c_index + 1, len(subsets)):
                    d = subsets[d_index]
                    if d & (a | b | c):
                        continue
                    if not all(base_touch(d, old) for old in (a, b, c)):
                        continue
                    count += 1
                    bags = (a, b, c, d)
                    z_contacts = [bool(set(bag) & adjacency[Z]) for bag in bags]
                    u_contacts = [bool(set(bag) & adjacency[U]) for bag in bags]
                    profile = (
                        sum(x or y for x, y in zip(z_contacts, u_contacts)),
                        sum(z_contacts) + sum(u_contacts),
                    )
                    best = max(best, profile)

    assert len(subsets) == 696
    assert count == 4645
    assert best == (3, 5)

    cz = {i for i, bag in enumerate(MODEL) if touch({Z}, bag)}
    cu = {i for i, bag in enumerate(MODEL) if touch({U}, bag)}
    assert (len(cz | cu), len(cz) + len(cu)) == (5, 9)


if __name__ == "__main__":
    verify_connectivity()
    verify_model_and_split_failure()
    verify_contact_maximum()
    print(
        "GREEN: seven-connected K7-free two-apex barrier; "
        "balanced contact-maximal same row does not split"
    )
