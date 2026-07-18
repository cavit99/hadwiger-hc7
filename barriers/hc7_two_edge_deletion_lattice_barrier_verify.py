#!/usr/bin/env python3
"""Verify the minimal three-state boundary-colouring gadget."""

from itertools import combinations, product


TARGET = {(0, 0, 0), (0, 0, 1), (0, 1, 0)}


def canonical(values):
    names = {}
    answer = []
    for value in values:
        if value not in names:
            names[value] = len(names)
        answer.append(names[value])
    return tuple(answer)


def signature(order, edges):
    """Return terminal partition types induced by proper 3-colourings."""
    answer = set()
    for colours in product(range(3), repeat=order):
        if all(colours[u] != colours[v] for u, v in edges):
            answer.add(canonical(colours[:3]))
    return answer


def all_graphs_with_independent_terminals(internal_order):
    order = 3 + internal_order
    possible = [
        edge
        for edge in combinations(range(order), 2)
        if not (edge[0] < 3 and edge[1] < 3)
    ]
    for mask in range(1 << len(possible)):
        yield {
            possible[index]
            for index in range(len(possible))
            if mask & (1 << index)
        }


def main():
    # Terminals are 0=b, 1=i_0, 2=i_1; internals are 3=x,4=y,5=z.
    edges = {
        (0, 3), (0, 4), (0, 5),
        (1, 4), (1, 5),
        (2, 3), (2, 5),
        (3, 4),
    }
    assert signature(6, edges) == TARGET

    e0 = (0, 1)
    e1 = (0, 2)
    assert signature(6, edges | {e1}) == {(0, 0, 1)}
    assert signature(6, edges | {e0}) == {(0, 1, 0)}
    assert signature(6, edges | {e0, e1}) == set()

    four_colouring = (0, 1, 1, 2, 3, 2)
    assert all(
        four_colouring[u] != four_colouring[v]
        for u, v in edges | {e0, e1}
    )

    for internal_order in range(3):
        for candidate in all_graphs_with_independent_terminals(internal_order):
            assert signature(3 + internal_order, candidate) != TARGET

    print("GREEN: exact three-state deletion lattice verified")
    print("GREEN: no realization with at most two internal vertices")


if __name__ == "__main__":
    main()
