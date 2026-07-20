#!/usr/bin/env python3
"""Verify the compound-separator terminal-edge response barrier.

The checker is dependency-free.  It exhausts all relevant support sets and
six-colour extensions and checks explicit tree decompositions.
"""

from itertools import combinations


D = (0, 1)
X = (2, 3, 4)
Y = (5, 6, 7)
S = D + X + Y
Q0 = (8, 9, 12)
Q1 = (10, 11)
R = Q0 + Q1
V = S + R
TERMINAL_EDGE = frozenset((8, 12))

EDGE_LIST = (
    (0, 3), (0, 6), (0, 8), (0, 9), (0, 10),
    (1, 3), (1, 4), (1, 5), (1, 6), (1, 9), (1, 11),
    (2, 11), (2, 12),
    (3, 5), (3, 6), (3, 8), (3, 10),
    (4, 5), (4, 9), (4, 11),
    (5, 9), (5, 10), (5, 11),
    (6, 8), (6, 9), (6, 10), (6, 11),
    (7, 8), (7, 11),
    (8, 9), (8, 10), (8, 11), (8, 12),
    (9, 10), (9, 11), (10, 11),
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


def all_subsets(vertices):
    vertices = tuple(vertices)
    return [
        frozenset(choice)
        for size in range(1, len(vertices) + 1)
        for choice in combinations(vertices, size)
    ]


def root_connector(part):
    return connected(part) and all(ADJ[root] & set(part) for root in D)


def block_support(part, block):
    union = set(part) | set(block)
    return connected(union) and any(
        frozenset(edge) <= union for edge in EDGE_LIST
    )


def minimal_members(family):
    return sorted(
        (member for member in family if not any(other < member for other in family)),
        key=lambda member: (len(member), tuple(sorted(member))),
    )


def colour_extension(split_roots, deleted_edge=None):
    colour = {vertex: 0 for vertex in X}
    colour.update({vertex: 1 for vertex in Y})
    colour[0] = 2
    colour[1] = 3 if split_roots else 2
    order = sorted(R, key=lambda vertex: -len(ADJ[vertex]))

    def search(position):
        if position == len(order):
            return dict(colour)
        vertex = order[position]
        forbidden = {
            colour[other]
            for other in ADJ[vertex]
            if other in colour and frozenset((vertex, other)) != deleted_edge
        }
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
    assert max(map(len, bags)) - 1 <= width
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
        containing = {i for i, bag in enumerate(bags) if vertex in bag}
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


def main():
    q0, q1 = set(Q0), set(Q1)
    assert connected(R) and connected(q0) and connected(q1)
    assert any(frozenset((u, v)) in EDGES for u in q0 for v in q1)
    assert all(ADJ[s] & q0 and ADJ[s] & q1 for s in S)

    split = colour_extension(split_roots=True)
    assert split is not None
    assert tuple(split[v] for v in V) == (
        2, 3, 0, 0, 0, 1, 1, 1, 3, 4, 1, 5, 2
    )
    assert colour_extension(split_roots=False) is None
    assert colour_extension(split_roots=False, deleted_edge=TERMINAL_EDGE) is None

    subsets = all_subsets(R)
    roots = [part for part in subsets if root_connector(part)]
    x_supports = [part for part in subsets if block_support(part, X)]
    y_supports = [part for part in subsets if block_support(part, Y)]

    assert minimal_members(roots) == [
        frozenset((9,)), frozenset((8, 11)), frozenset((10, 11))
    ]
    assert minimal_members(x_supports) == [
        frozenset((8, 11)), frozenset((10, 11)), frozenset((8, 9, 12))
    ]
    assert minimal_members(y_supports) == [
        frozenset((11,)), frozenset((8, 9)), frozenset((8, 10))
    ]

    for part in (q0, q1):
        local_roots = [item for item in roots if item <= part]
        local_x = [item for item in x_supports if item <= part]
        local_y = [item for item in y_supports if item <= part]
        assert all(a & b for a in local_roots for b in local_x)
        assert all(a & b for a in local_roots for b in local_y)
        assert all(a & b for a in local_x for b in local_y)

    a_support = frozenset((8, 9, 12))
    b_support = frozenset((11,))
    compound = a_support | b_support
    assert a_support in minimal_members(x_supports)
    assert b_support in minimal_members(y_supports)
    assert all(compound & root for root in roots)
    assert TERMINAL_EDGE <= a_support
    assert ADJ[12] & a_support == {8}
    assert not any(
        not (root & x_part or root & y_part or x_part & y_part)
        for root in roots for x_part in x_supports for y_part in y_supports
    )

    # Width five certifies exclusion of a K7 minor.
    bags = (
        (7, 8, 11),
        (2, 8, 9, 11),
        (1, 4, 5, 9, 11),
        (0, 3, 6, 8, 9, 10),
        (1, 3, 5, 6, 9, 11),
        (3, 5, 6, 9, 10, 11),
        (3, 6, 8, 9, 10, 11),
        (2, 8, 12),
    )
    tree_edges = ((0, 1), (1, 6), (2, 4), (3, 6), (4, 5), (5, 6), (1, 7))
    verify_tree_decomposition(V, EDGE_LIST, bags, tree_edges, width=5)

    # Width two certifies exclusion of a boundary K5 minor.
    s_bags = ((0, 3, 6), (1, 3, 5), (1, 3, 6), (1, 4, 5), (2,), (7,))
    s_tree_edges = ((0, 2), (1, 2), (1, 3), (0, 4), (0, 5))
    s_edges = [(left, right) for left, right in EDGE_LIST if left in S and right in S]
    verify_tree_decomposition(S, s_edges, s_bags, s_tree_edges, width=2)

    print("GREEN compound-separator terminal-edge response barrier")
    print("two S-full connected parts; all three local support families cross-intersect")
    print("minimal compound root separator A_X union B_Y has terminal edge 8-12")
    print("merged trace rejected before and after deleting 8-12")
    print("treewidth upper bounds: tw(G[S union R])<=5, tw(G[S])<=2")
    print("scope: no opposite shore, seven-connectivity, or contraction-critical host")


if __name__ == "__main__":
    main()
