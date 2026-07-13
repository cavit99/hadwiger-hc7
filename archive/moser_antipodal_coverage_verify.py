#!/usr/bin/env python3
"""Verify the sharp seven-chord bound for Moser antipodal modes."""

from itertools import combinations, permutations


VERTICES = tuple(range(7))
MOSER = {
    frozenset(edge)
    for edge in {
        (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
        (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
    }
}
NONEDGES = {
    frozenset(edge) for edge in combinations(VERTICES, 2)
} - MOSER


def matching_modes():
    modes = []
    for edges in combinations(NONEDGES, 3):
        used = set().union(*edges)
        if len(used) == 6:
            modes.append((frozenset(edges), next(iter(set(VERTICES) - used))))
    return modes


def antipodal(order, matching, singleton):
    six = [vertex for vertex in order if vertex != singleton]
    position = {vertex: index for index, vertex in enumerate(six)}
    for edge in matching:
        first, second = tuple(edge)
        if (position[first] - position[second]) % 6 != 3:
            return False
    return True


def main():
    modes = matching_modes()
    assert len(modes) == 16
    maximum = 0
    achievers = 0
    for tail in permutations(VERTICES[1:]):
        order = (0,) + tail
        if order[1] > order[-1]:
            continue
        realized = [
            matching for matching, singleton in modes
            if antipodal(order, matching, singleton)
        ]
        covered = set().union(*realized) if realized else set()
        current = len(covered)
        if current > maximum:
            maximum = current
            achievers = 1
        elif current == maximum:
            achievers += 1
    assert maximum == 7
    assert achievers == 4
    print("modes", len(modes))
    print("maximum_nonedge_coverage", maximum)
    print("unoriented_orders_attaining_maximum", achievers)
    print("PASS")


if __name__ == "__main__":
    main()
