#!/usr/bin/env python3
"""Verify a K7-minor-free split shore with packing number obstruction.

The verifier is dependency-free.  It checks the two boundary responses,
enumerates every relevant connected subset of the four-vertex shore, and
checks explicit tree decompositions certifying the claimed minor exclusions.
"""

from itertools import combinations


D = (0, 1)
X = (2, 3, 4)
Y = (5, 6, 7)
S = D + X + Y
R = (8, 9, 10, 11)
V = S + R

EDGE_LIST = (
    (0, 3), (0, 6), (0, 8), (0, 9), (0, 10),
    (1, 3), (1, 4), (1, 5), (1, 6), (1, 9), (1, 11),
    (2, 8), (2, 9), (2, 11),
    (3, 5), (3, 6), (3, 8), (3, 10),
    (4, 5), (4, 9), (4, 11),
    (5, 9), (5, 10), (5, 11),
    (6, 8), (6, 9), (6, 10), (6, 11),
    (7, 8), (7, 11),
    (8, 9), (8, 10), (8, 11), (9, 10), (9, 11), (10, 11),
)
EDGES = {frozenset(edge) for edge in EDGE_LIST}
ADJ = {vertex: set() for vertex in V}
for left, right in EDGE_LIST:
    ADJ[left].add(right)
    ADJ[right].add(left)


def connected(vertices):
    vertices = set(vertices)
    if not vertices:
        return False
    seen = {next(iter(vertices))}
    while True:
        extended = seen | set().union(*(ADJ[v] & vertices for v in seen))
        if extended == seen:
            return seen == vertices
        seen = extended


def connected_subsets(vertices):
    vertices = tuple(vertices)
    return [
        frozenset(choice)
        for size in range(1, len(vertices) + 1)
        for choice in combinations(vertices, size)
        if connected(choice)
    ]


def block_carrier(part, boundary_block):
    return connected(set(part) | set(boundary_block))


def root_connector(part):
    return connected(part) and all(ADJ[root] & set(part) for root in D)


def colour_extension(split):
    colour = {vertex: 0 for vertex in X}
    colour.update({vertex: 1 for vertex in Y})
    colour[0] = 2
    colour[1] = 3 if split else 2
    order = sorted(R, key=lambda vertex: -len(ADJ[vertex]))

    def search(position):
        if position == len(order):
            return dict(colour)
        vertex = order[position]
        forbidden = {colour[other] for other in ADJ[vertex] if other in colour}
        for candidate in range(6):
            if candidate in forbidden:
                continue
            colour[vertex] = candidate
            answer = search(position + 1)
            if answer is not None:
                return answer
            del colour[vertex]
        return None

    return search(0)


def verify_tree_decomposition(vertices, edges, bags, tree_edges, width):
    vertices = set(vertices)
    bags = [set(bag) for bag in bags]
    assert max(len(bag) for bag in bags) - 1 <= width
    assert set().union(*bags) == vertices
    assert all(any({left, right} <= bag for bag in bags) for left, right in edges)

    tree = {index: set() for index in range(len(bags))}
    for left, right in tree_edges:
        tree[left].add(right)
        tree[right].add(left)
    assert len(tree_edges) == len(bags) - 1
    seen = {0}
    while True:
        extended = seen | set().union(*(tree[index] for index in seen))
        if extended == seen:
            break
        seen = extended
    assert seen == set(tree)

    for vertex in vertices:
        containing = {index for index, bag in enumerate(bags) if vertex in bag}
        reached = {next(iter(containing))}
        while True:
            extended = reached | {
                neighbour
                for index in reached
                for neighbour in tree[index]
                if neighbour in containing
            }
            if extended == reached:
                break
            reached = extended
        assert reached == containing


def minimal_members(family):
    return sorted(
        (member for member in family if not any(other < member for other in family)),
        key=lambda member: (len(member), tuple(sorted(member))),
    )


def main():
    q0, q1 = {8, 9}, {10, 11}
    assert connected(R) and connected(q0) and connected(q1)
    assert all(ADJ[vertex] & q0 and ADJ[vertex] & q1 for vertex in S)

    split = colour_extension(split=True)
    merged = colour_extension(split=False)
    assert split is not None and merged is None
    assert tuple(split[vertex] for vertex in V) == (2, 3, 0, 0, 0, 1, 1, 1, 3, 4, 5, 2)

    subsets = connected_subsets(R)
    roots = [part for part in subsets if root_connector(part)]
    x_carriers = [
        part for part in (frozenset(choice) for size in range(1, 5)
                          for choice in combinations(R, size))
        if block_carrier(part, X)
    ]
    y_carriers = [
        part for part in (frozenset(choice) for size in range(1, 5)
                          for choice in combinations(R, size))
        if block_carrier(part, Y)
    ]
    minimal = tuple(map(minimal_members, (roots, x_carriers, y_carriers)))
    assert minimal == (
        [frozenset({9}), frozenset({8, 11}), frozenset({10, 11})],
        [frozenset({8, 9}), frozenset({8, 11}),
         frozenset({9, 10}), frozenset({10, 11})],
        [frozenset({11}), frozenset({8, 9}), frozenset({8, 10})],
    )
    assert not any(
        not (root & x_part or root & y_part or x_part & y_part)
        for root in roots for x_part in x_carriers for y_part in y_carriers
    )
    all_supports = roots + x_carriers + y_carriers
    assert not any(
        all(set(transversal) & support for support in all_supports)
        for size in range(3)
        for transversal in combinations(R, size)
    )
    assert all({8, 9, 11} & support for support in all_supports)

    # Width five certifies that G[S union R] has no K7 minor.
    bags = (
        (7, 8, 11),
        (2, 8, 9, 11),
        (1, 4, 5, 9, 11),
        (0, 3, 6, 8, 9, 10),
        (1, 3, 5, 6, 9, 11),
        (3, 5, 6, 9, 10, 11),
        (3, 6, 8, 9, 10, 11),
    )
    tree_edges = ((0, 1), (1, 6), (2, 4), (3, 6), (4, 5), (5, 6))
    verify_tree_decomposition(V, EDGE_LIST, bags, tree_edges, width=5)

    # Width two certifies, more strongly, that G[S] has no K5 minor.
    s_bags = ((0, 3, 6), (1, 3, 5), (1, 3, 6), (1, 4, 5), (2,), (7,))
    s_tree_edges = ((0, 2), (1, 2), (1, 3), (0, 4), (0, 5))
    s_edges = [(left, right) for left, right in EDGE_LIST if left in S and right in S]
    verify_tree_decomposition(S, s_edges, s_bags, s_tree_edges, width=2)

    print("GREEN K7-minor-free split-shore packing/transversal barrier")
    print("shore: |R|=4, two connected S-full parts, split-only response")
    print("three-piece packing=none; common transversal number=3")
    print("treewidth upper bounds: tw(G[S union R])<=5, tw(G[S])<=2")
    print("scope: no opposite merged shore, seven-connectivity, or minor-criticality")


if __name__ == "__main__":
    main()
