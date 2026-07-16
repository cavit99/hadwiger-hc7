#!/usr/bin/env python3
"""Deterministically verify the seven-vertex paired-repair barrier."""

from itertools import combinations


VERTICES = frozenset(range(7))
EDGES = {
    tuple(sorted(edge))
    for edge in [
        (0, 1), (0, 3), (0, 4), (0, 5), (0, 6),
        (1, 3), (1, 4), (1, 5), (1, 6),
        (2, 3), (2, 4), (2, 5), (2, 6),
        (3, 6), (4, 5), (4, 6), (5, 6),
    ]
}


def adjacent(x: int, y: int) -> bool:
    return tuple(sorted((x, y))) in EDGES


def connected(vertices: frozenset[int]) -> bool:
    if not vertices:
        return False
    reached = {next(iter(vertices))}
    frontier = list(reached)
    while frontier:
        x = frontier.pop()
        for y in vertices - reached:
            if adjacent(x, y):
                reached.add(y)
                frontier.append(y)
    return reached == set(vertices)


def induced_connected_after_deleting(deleted: frozenset[int]) -> bool:
    return connected(VERTICES - deleted)


def all_supersets(required: frozenset[int]):
    optional = sorted(VERTICES - required)
    for size in range(len(optional) + 1):
        for chosen in combinations(optional, size):
            yield required | frozenset(chosen)


def main() -> None:
    # Every deletion of fewer than four vertices leaves the graph connected.
    for size in range(4):
        for deleted in combinations(VERTICES, size):
            assert induced_connected_after_deleting(frozenset(deleted))

    # A four-cut exists, so the connectivity is exactly four.
    four_cuts = []
    for deleted in combinations(VERTICES, 4):
        if not induced_connected_after_deleting(frozenset(deleted)):
            four_cuts.append(deleted)
    assert four_cuts

    clique = {0, 1, 4, 5, 6}
    assert all(adjacent(x, y) for x, y in combinations(clique, 2))
    assert not adjacent(2, 0) and not adjacent(2, 1)
    assert not adjacent(3, 4) and not adjacent(3, 5)

    left = [s for s in all_supersets(frozenset({2, 0, 1})) if connected(s)]
    right = [s for s in all_supersets(frozenset({3, 4, 5})) if connected(s)]
    assert left and right
    opposite_left = frozenset({3, 4, 5})
    opposite_right = frozenset({2, 0, 1})
    assert all(6 in s for s in left if s.isdisjoint(opposite_left))
    assert all(6 in s for s in right if s.isdisjoint(opposite_right))
    assert not any(a.isdisjoint(b) for a in left for b in right)

    print("GREEN")
    print(f"vertex connectivity: 4; example four-cut: {four_cuts[0]}")
    print(f"connected left supersets: {len(left)}")
    print(f"connected right supersets: {len(right)}")
    print("disjoint prescribed connected pairs: 0")


if __name__ == "__main__":
    main()
