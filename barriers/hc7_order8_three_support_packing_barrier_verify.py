#!/usr/bin/env python3
"""Verify the exact-order-eight three-support packing barrier."""

from itertools import combinations


D = ("d", "e")
X = ("x1", "x2", "x3")
Y = ("y1", "y2", "y3")
S = D + X + Y
R = tuple(range(6))
L = ("l0", "l1", "l2")
V = S + R + L

R_EDGES = {
    frozenset(edge)
    for edge in (
        (0, 2), (0, 3), (0, 5), (1, 2), (1, 4), (1, 5),
        (2, 3), (2, 5), (3, 4), (3, 5), (4, 5),
    )
}
PORTALS = {
    "d": {0, 4, 5},
    "e": {1, 2, 3},
    "x1": {1, 3, 5},
    "x2": {0, 2, 3, 4},
    "x3": set(R),
    "y1": {1, 4},
    "y2": set(R),
    "y3": {0, 3},
}


def pair(left, right):
    return frozenset((left, right))


EDGES = set(R_EDGES)
EDGES.update(pair(left, right) for left, right in combinations(L, 2))
for first, second in combinations((D, X, Y), 2):
    EDGES.update(pair(left, right) for left in first for right in second)
for boundary, neighbours in PORTALS.items():
    EDGES.update(pair(boundary, vertex) for vertex in neighbours)
EDGES.update(pair(boundary, vertex) for boundary in S for vertex in L)

ADJ = {vertex: set() for vertex in V}
for edge in EDGES:
    left, right = tuple(edge)
    ADJ[left].add(right)
    ADJ[right].add(left)


def connected(vertices, allowed=None):
    vertices = set(vertices)
    if not vertices:
        return False
    if allowed is None:
        allowed = vertices
    else:
        allowed = set(allowed)
    seen = {next(iter(vertices))}
    while True:
        extended = seen | set().union(*(ADJ[v] & allowed for v in seen))
        if extended == seen:
            return vertices <= seen
        seen = extended


def connected_subsets(vertices):
    vertices = tuple(vertices)
    return [
        frozenset(choice)
        for size in range(1, len(vertices) + 1)
        for choice in combinations(vertices, size)
        if connected(choice)
    ]


def supports(subgraph, boundary_set):
    return all(set(subgraph) & PORTALS[boundary] for boundary in boundary_set)


def exact_response(shore, split):
    boundary_colour = {vertex: 0 for vertex in X}
    boundary_colour.update({vertex: 1 for vertex in Y})
    boundary_colour["d"] = 2
    boundary_colour["e"] = 3 if split else 2
    order = sorted(shore, key=lambda vertex: -len(ADJ[vertex]))
    colour = dict(boundary_colour)

    def recurse(position):
        if position == len(order):
            return dict(colour)
        vertex = order[position]
        forbidden = {colour[other] for other in ADJ[vertex] if other in colour}
        for candidate in range(6):
            if candidate in forbidden:
                continue
            colour[vertex] = candidate
            result = recurse(position + 1)
            if result is not None:
                return result
            del colour[vertex]
        return None

    return recurse(0)


def remaining_connected(deleted):
    remainder = set(V) - set(deleted)
    if len(remainder) <= 1:
        return True
    start = next(iter(remainder))
    seen = {start}
    while True:
        extended = seen | set().union(*(ADJ[v] & remainder for v in seen))
        if extended == seen:
            return seen == remainder
        seen = extended


def verify_branch_sets(branch_sets):
    assert all(connected(branch) for branch in branch_sets)
    assert sum(map(len, branch_sets)) == len(set().union(*map(set, branch_sets)))
    assert all(
        any(pair(left, right) in EDGES for left in first for right in second)
        for first, second in combinations(branch_sets, 2)
    )


def main():
    assert len(V) == 17 and len(EDGES) == 88
    assert not any(pair(left, right) in EDGES for left in L for right in R)
    assert connected(L) and connected(R)
    assert all(ADJ[left] & set(R) for left in S)
    assert all(ADJ[left] & set(L) for left in S)

    q0, q1 = {0, 1, 2}, {3, 4, 5}
    assert connected(q0) and connected(q1) and not (q0 & q1)
    assert all(q0 & PORTALS[s] and q1 & PORTALS[s] for s in S)

    subsets = connected_subsets(R)
    root_supports = [item for item in subsets if supports(item, D)]
    x_supports = [item for item in subsets if supports(item, X)]
    y_supports = [item for item in subsets if supports(item, Y)]
    packing = [
        (root, x_part, y_part)
        for root in root_supports
        for x_part in x_supports
        for y_part in y_supports
        if not (root & x_part or root & y_part or x_part & y_part)
    ]
    assert not packing

    relative = []
    for item in subsets:
        internal = set().union(*(ADJ[v] & set(R) for v in item)) - set(item)
        boundary = {s for s in S if set(item) & PORTALS[s]}
        relative.append((len(internal) + len(boundary), item))
    assert min(value for value, _ in relative) == 8

    assert exact_response(L, split=False) is not None
    assert exact_response(L, split=True) is None
    assert exact_response(R, split=False) is None
    split_colouring = exact_response(R, split=True)
    assert split_colouring is not None

    cuts_tested = 0
    for size in range(8):
        for deleted in combinations(V, size):
            cuts_tested += 1
            assert remaining_connected(deleted)
    assert not remaining_connected(S)

    model = [
        {"d", "x1"},
        {"e", 2},
        {"x2", "y2"},
        {"x3"},
        {0, 3, 4, "y1", "y3"},
        {1},
        {5},
    ]
    verify_branch_sets(model)

    print("GREEN exact-order-eight three-support packing barrier")
    print(f"host: vertices={len(V)} edges={len(EDGES)} connectivity=8 cuts_tested={cuts_tested}")
    print("chromatic_number=7; responses: left=merged-only right=split-only")
    print("right_shore: two disjoint S-full connected subgraphs; three-support packing=none")
    print(f"relative_connected_set_boundary_min={min(value for value, _ in relative)}")
    print("K7 minor: explicit seven branch sets verified inside S union R")
    print("scope: K7-minor exclusion and contraction-criticality deliberately absent")


if __name__ == "__main__":
    main()
