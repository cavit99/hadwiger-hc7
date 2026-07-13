#!/usr/bin/env python3
"""Verify the sharp degree-9 row-five two-linkage counterarchitecture.

The graph has the type-2 boundary, the two other exact shores, and a
row-five shore split into P and a connected two-vertex Q.  The two missing
labels have disjoint one-edge paths to distinct P-interface vertices in Q.
An explicit width-four tree decomposition proves that the quotient has no
K6 minor.
"""


N = set(range(9))
P, Q7, Q8, C2, C3 = 9, 10, 11, 12, 13


def edge(left, right):
    return tuple(sorted((left, right)))


def main():
    edges = {
        edge(0, 1), edge(0, 2), edge(1, 2), edge(2, 5),
        edge(4, 5), edge(3, 7), edge(6, 8),
        edge(P, Q7), edge(P, Q8), edge(Q7, Q8),
    }
    rows = {
        P: {2, 3, 4, 5, 6},
        Q7: {2, 3, 7},
        Q8: {6, 8},
        C2: N - {0, 2},
        C3: N - {1, 2},
    }
    for piece, contacts in rows.items():
        edges.update(edge(piece, label) for label in contacts)

    # Exact row-five state and its two disjoint label-preserving paths.
    assert rows[P] | rows[Q7] | rows[Q8] == N - {0, 1}
    assert (rows[Q7] | rows[Q8]) == {2, 3, 6, 7, 8}
    assert 7 in rows[Q7] and edge(P, Q7) in edges
    assert 8 in rows[Q8] and edge(P, Q8) in edges

    bags = (
        {6, P, Q8, C2, C3},
        {6, 8, Q8, C2, C3},
        {3, P, Q7, C2, C3},
        {3, 7, Q7, C2, C3},
        {2, P, Q7, C2, C3},
        {2, 5, P, C2, C3},
        {4, 5, P, C2, C3},
        {1, 2, C2, C3},
        {0, 1, 2, C3},
        {P, Q7, Q8, C2, C3},
    )
    tree_edges = (
        (9, 0), (9, 2), (9, 4), (0, 1), (2, 3),
        (4, 5), (4, 7), (5, 6), (7, 8),
    )
    assert max(map(len, bags)) == 5
    tree = [set() for _ in bags]
    for left, right in tree_edges:
        tree[left].add(right)
        tree[right].add(left)

    reached = {0}
    frontier = [0]
    while frontier:
        current = frontier.pop()
        for other in tree[current] - reached:
            reached.add(other)
            frontier.append(other)
    assert reached == set(range(len(bags)))
    assert len(tree_edges) == len(bags) - 1

    assert all(any(left in bag and right in bag for bag in bags)
               for left, right in edges)
    for vertex in range(14):
        containing = {index for index, bag in enumerate(bags)
                      if vertex in bag}
        assert containing
        reached = {next(iter(containing))}
        frontier = list(reached)
        while frontier:
            current = frontier.pop()
            for other in (tree[current] & containing) - reached:
                reached.add(other)
                frontier.append(other)
        assert reached == containing

    print("two_label_paths=True distinct_interface_vertices=True")
    print("treewidth_at_most=4 hence_no_K6_minor=True")


if __name__ == "__main__":
    main()
