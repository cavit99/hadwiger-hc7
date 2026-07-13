#!/usr/bin/env python3
"""Independent verifier for the degree-9/three-shore static obstruction.

The checked quotient has no K6 minor at all (certified by a width-four
tree decomposition) and has no usable star-plus-two-shore anchor with at
most two boundary singletons.  It does not import the discovery probe or
use an SMT solver.
"""

from itertools import combinations, product


N = 9
SHORES = (9, 10, 11)
TOTAL = 12
MISSES = ((0, 1), (0, 2), (1, 2))
BOUNDARY_EDGES = {
    (0, 1), (0, 2), (1, 2), (2, 5),
    (3, 7), (4, 5), (6, 8),
}


def graph_edges():
    edges = {tuple(sorted(edge)) for edge in BOUNDARY_EDGES}
    for index, shore in enumerate(SHORES):
        for vertex in range(N):
            if vertex not in MISSES[index]:
                edges.add(tuple(sorted((shore, vertex))))
    return edges


EDGES = graph_edges()


def adjacent_sets(left, right):
    return any(tuple(sorted((x, y))) in EDGES for x in left for y in right)


def alpha_check():
    assert all(any(tuple(sorted(edge)) in BOUNDARY_EDGES
                   for edge in combinations(five, 2))
               for five in combinations(range(N), 5))
    independent = {0, 4, 6, 7}
    assert all(tuple(sorted(edge)) not in BOUNDARY_EDGES
               for edge in combinations(independent, 2))


def anchor_exists(singleton_count):
    for singletons in combinations(range(N), singleton_count):
        rest = tuple(x for x in range(N) if x not in singletons)
        for colors in product(range(3), repeat=len(rest)):
            if set(colors) != {0, 1, 2}:
                continue
            blocks = tuple({x for x, color in zip(rest, colors)
                            if color == target}
                           for target in range(3))
            if any(any(tuple(sorted(edge)) in BOUNDARY_EDGES
                       for edge in combinations(block, 2))
                   for block in blocks):
                continue
            if any(tuple(sorted(edge)) not in BOUNDARY_EDGES
                   for edge in combinations(singletons, 2)):
                continue

            all_sides = True
            for retained in range(3):
                outside = tuple(i for i in range(3) if i != retained)
                side = False
                for first, second in (outside, outside[::-1]):
                    if set(MISSES[first]) & blocks[1]:
                        continue
                    if set(MISSES[second]) & blocks[2]:
                        continue
                    first_bag = blocks[1] | {SHORES[first]}
                    second_bag = blocks[2] | {SHORES[second]}
                    if not adjacent_sets(first_bag, second_bag):
                        continue
                    if any(not adjacent_sets({w}, first_bag)
                           or not adjacent_sets({w}, second_bag)
                           for w in singletons):
                        continue
                    side = True
                    break
                if not side:
                    all_sides = False
                    break
            if all_sides:
                return True
    return False


def tree_decomposition_check():
    bags = (
        frozenset((6, 8, 9, 10, 11)),
        frozenset((5, 9, 10, 11)),
        frozenset((4, 5, 9, 10, 11)),
        frozenset((7, 9, 10, 11)),
        frozenset((3, 7, 9, 10, 11)),
        frozenset((2, 5, 9, 10, 11)),
        frozenset((1, 2, 10, 11)),
        frozenset((0, 1, 2, 11)),
    )
    tree_edges = (
        (0, 1), (0, 3), (1, 2), (1, 5),
        (3, 4), (5, 6), (6, 7),
    )

    assert max(map(len, bags)) == 5
    assert len(tree_edges) == len(bags) - 1
    tree_adj = [set() for _ in bags]
    for x, y in tree_edges:
        tree_adj[x].add(y)
        tree_adj[y].add(x)
    reached = {0}
    frontier = [0]
    while frontier:
        x = frontier.pop()
        for y in tree_adj[x] - reached:
            reached.add(y)
            frontier.append(y)
    assert len(reached) == len(bags)

    assert set().union(*bags) == set(range(TOTAL))
    assert all(any(u in bag and v in bag for bag in bags)
               for u, v in EDGES)
    for vertex in range(TOTAL):
        containing = {i for i, bag in enumerate(bags) if vertex in bag}
        reached = {next(iter(containing))}
        frontier = list(reached)
        while frontier:
            x = frontier.pop()
            for y in (tree_adj[x] & containing) - reached:
                reached.add(y)
                frontier.append(y)
        assert reached == containing


def main():
    alpha_check()
    tree_decomposition_check()
    for count in range(3):
        assert not anchor_exists(count), count
    assert not set.intersection(*(set(miss) for miss in MISSES))
    print("verified alpha=4, treewidth<=4, no 0/1/2-singleton anchor")


if __name__ == "__main__":
    main()
