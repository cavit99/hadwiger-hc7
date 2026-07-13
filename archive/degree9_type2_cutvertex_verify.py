#!/usr/bin/env python3
"""Verifier for the exact-miss type-2 cutvertex lobe certificate."""

import ast
from itertools import combinations
from pathlib import Path


N = 9
TOTAL = 13
PIECES = (9, 10, 11, 12)
EXPECTED_EDGES = {
    (0, 1), (0, 2), (1, 2), (2, 5),
    (3, 7), (4, 5), (6, 8),
}
EXPECTED_MISSES = ({0, 1}, {0, 2}, {1, 2})


def row(shore, lost):
    answer = set(range(N)) - EXPECTED_MISSES[shore]
    if lost >= 0:
        answer.remove(lost)
    return answer


def expected_keys():
    keys = set()
    for shore in range(3):
        allowed = sorted(set(range(N)) - EXPECTED_MISSES[shore])
        keys.add((shore, -1, -1))
        keys.update((shore, -1, lost) for lost in allowed)
        keys.update((shore, first, second)
                    for first, second in combinations(allowed, 2))
    assert len(keys) == 87
    return keys


def adjacency(rows):
    adj = [0] * TOTAL
    for x, y in EXPECTED_EDGES:
        adj[x] |= 1 << y
        adj[y] |= 1 << x
    for index, contacts in enumerate(rows):
        piece = PIECES[index]
        for x in contacts:
            adj[piece] |= 1 << x
            adj[x] |= 1 << piece
    return adj


def cross(left, right, adj):
    return any(adj[x] & right for x in range(TOTAL) if left >> x & 1)


def connected(mask, adj):
    reached = mask & -mask
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier -= bit
        vertex = bit.bit_length() - 1
        new = adj[vertex] & mask & ~reached
        reached |= new
        frontier |= new
    return reached == mask


def verify_case(shore, lost_first, lost_second, bags):
    others = [index for index in range(3) if index != shore]
    rows = (
        row(shore, lost_first),
        row(shore, lost_second),
        row(others[0], -1),
        row(others[1], -1),
    )
    assert rows[0] | rows[1] == row(shore, -1)
    adj = adjacency(rows)

    assert len(bags) == 6
    used = 0
    for bag in bags:
        assert bag and bag < 1 << TOTAL
        assert bag & ((1 << N) - 1), "bag does not meet the boundary"
        assert not used & bag, "overlapping bags"
        used |= bag
        assert connected(bag, adj), "disconnected bag"
    assert all(cross(bags[i], bags[j], adj)
               for i in range(6) for j in range(i + 1, 6))


def verify_sharpness_decomposition():
    """Check the width-four two-row example from Section 5 of the note."""
    rows = (
        {2, 3, 4, 5, 6},
        {2, 3, 6, 7, 8},
        {1, 3, 4, 5, 6, 7, 8},
        {0, 3, 4, 5, 6, 7, 8},
    )
    edges = set(EXPECTED_EDGES)
    edges.add((9, 10))
    for index, contacts in enumerate(rows):
        edges.update(tuple(sorted((PIECES[index], x))) for x in contacts)
    bags = (
        {6, 9, 10, 11, 12}, {6, 8, 10, 11, 12},
        {3, 9, 10, 11, 12}, {3, 7, 10, 11, 12},
        {2, 9, 10, 11, 12}, {2, 5, 9, 11, 12},
        {4, 5, 9, 11, 12}, {1, 2, 11, 12},
        {0, 1, 2, 12},
    )
    tree_edges = ((0, 1), (0, 2), (0, 4), (2, 3),
                  (4, 5), (4, 7), (5, 6), (7, 8))
    assert max(map(len, bags)) == 5
    tree_adj = [set() for _ in bags]
    for x, y in tree_edges:
        tree_adj[x].add(y)
        tree_adj[y].add(x)
    assert len(tree_edges) == len(bags) - 1
    reached_tree = {0}
    frontier_tree = [0]
    while frontier_tree:
        current = frontier_tree.pop()
        for nxt in tree_adj[current] - reached_tree:
            reached_tree.add(nxt)
            frontier_tree.append(nxt)
    assert len(reached_tree) == len(bags)
    assert all(any(x in bag and y in bag for bag in bags) for x, y in edges)
    for vertex in range(TOTAL):
        containing = {i for i, bag in enumerate(bags) if vertex in bag}
        reached = {next(iter(containing))}
        frontier = list(reached)
        while frontier:
            current = frontier.pop()
            for nxt in (tree_adj[current] & containing) - reached:
                reached.add(nxt)
                frontier.append(nxt)
        assert reached == containing


def main():
    path = Path(__file__).resolve().parent / (
        "degree9_type2_cutvertex_certificate.txt")
    data = ast.literal_eval(path.read_text(encoding="utf-8"))
    assert set(map(tuple, data["boundary_edges"])) == EXPECTED_EDGES
    assert tuple(map(set, data["misses"])) == EXPECTED_MISSES

    cases = data["cases"]
    keys = [(shore, first, second)
            for shore, first, second, _bags in cases]
    assert len(keys) == len(set(keys)) == 87
    assert set(keys) == expected_keys()
    for shore, first, second, bags in cases:
        verify_case(shore, first, second, tuple(bags))
    verify_sharpness_decomposition()
    print("verified 87 exact-miss lobe states and sharp width-four residue")


if __name__ == "__main__":
    main()
