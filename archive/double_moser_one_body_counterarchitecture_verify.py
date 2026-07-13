#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Verify the 14-vertex atlas-negative double-Moser architecture.

Checks, without a graph library:

* global vertex-connectivity is at least seven;
* every connected covering split rooted at b|a is atlas-negative;
* every nonempty proper subset of C satisfies relative boundary >=7; and
* the displayed three-carrier bags form a K7 model.
"""

from itertools import combinations, product


VERTICES = (
    "u", "v", "x1", "x2", "x3", "x4", "a", "b", "p", "q",
    "r0", "r1", "r2", "r3",
)
BODY = ("r0", "r1", "r2", "r3")
SHORE = ("a", "b", *BODY)
BOUNDARY = ("v", "x1", "x2", "x3", "x4", "p", "q")


def edge(left, right):
    return frozenset((left, right))


EDGES = {
    edge("u", "v"),
    *(edge("u", x) for x in ("x1", "x2", "x3", "x4", "p", "q")),
    *(edge("v", x) for x in ("x1", "x2", "x3", "x4", "a", "b")),
    edge("x1", "x2"), edge("x3", "x4"), edge("a", "b"), edge("p", "q"),
    edge("a", "x1"), edge("a", "x2"), edge("b", "x3"), edge("b", "x4"),
    edge("p", "x3"), edge("p", "x4"), edge("q", "x1"), edge("q", "x2"),
}

ROWS = {
    "a": ("b", "p", "r0", "r1", "v", "x1", "x2"),
    "b": ("a", "p", "q", "r1", "v", "x3", "x4"),
    "r0": ("a", "p", "q", "r1", "r2", "r3", "x1"),
    "r1": ("a", "b", "p", "q", "r0", "r3", "x3"),
    "r2": ("p", "q", "r0", "r3", "x1", "x2", "x4"),
    "r3": ("q", "r0", "r1", "r2", "x2", "x3", "x4"),
}
for vertex, neighbours in ROWS.items():
    EDGES.update(edge(vertex, neighbour) for neighbour in neighbours)


MAXIMAL_BAD = (
    (0, 0, 1, 1, 3, 3), (0, 1, 0, 1, 3, 3),
    (0, 1, 1, 0, 3, 3), (0, 1, 1, 1, 2, 2),
    (1, 0, 0, 1, 3, 3), (1, 0, 1, 0, 3, 3),
    (1, 0, 1, 1, 2, 2), (1, 1, 0, 0, 3, 3),
    (1, 1, 0, 1, 1, 1), (1, 1, 1, 0, 1, 1),
)


def connected(vertices, deleted=frozenset()):
    vertices = set(vertices) - set(deleted)
    if not vertices:
        return True
    reached = {next(iter(vertices))}
    while True:
        expanded = reached | {
            y for x in reached for y in vertices if edge(x, y) in EDGES
        }
        if expanded == reached:
            return reached == vertices
        reached = expanded


def touches(left, right):
    return any(edge(x, y) in EDGES for x in left for y in right)


def contact(side, label):
    return any(edge(vertex, label) in EDGES for vertex in side)


def split_state(side_a, side_b):
    bits = (
        int(contact(side_a, "x1")), int(contact(side_a, "x2")),
        int(contact(side_b, "x3")), int(contact(side_b, "x4")),
    )

    def side_state(label):
        at_a, at_b = contact(side_a, label), contact(side_b, label)
        assert at_a or at_b
        return (1 if at_a else 0) | (2 if at_b else 0)

    return (*bits, side_state("p"), side_state("q"))


def below(state, maximum):
    if any(bit and not cap for bit, cap in zip(state[:4], maximum[:4])):
        return False
    for value, cap in zip(state[4:], maximum[4:]):
        if cap != 3 and value != cap:
            return False
    return True


def is_model(bags):
    return (
        all(set(bags[i]).isdisjoint(bags[j])
            for i, j in combinations(range(len(bags)), 2))
        and all(connected(bag) for bag in bags)
        and all(touches(bags[i], bags[j])
                for i, j in combinations(range(len(bags)), 2))
    )


def main():
    # Direct definition of 7-connectivity: deletion of at most six vertices
    # leaves the remaining graph connected.
    checked_deletions = 0
    for order in range(7):
        for deleted in combinations(VERTICES, order):
            assert connected(VERTICES, frozenset(deleted)), deleted
            checked_deletions += 1

    checked_relative = 0
    for order in range(1, len(SHORE)):
        for subset_tuple in combinations(SHORE, order):
            subset = set(subset_tuple)
            internal_frontier = {
                outside for outside in SHORE if outside not in subset
                and any(edge(vertex, outside) in EDGES for vertex in subset)
            }
            boundary_contacts = {
                label for label in BOUNDARY
                if any(edge(vertex, label) in EDGES for vertex in subset)
            }
            assert len(internal_frontier) + len(boundary_contacts) >= 7
            checked_relative += 1

    checked_splits = 0
    for assignment in product((0, 1), repeat=4):
        # Atlas A is rooted at old outer b; atlas B is rooted at old outer a.
        side_a = {"b", *(v for v, side in zip(BODY, assignment) if side == 0)}
        side_b = {"a", *(v for v, side in zip(BODY, assignment) if side == 1)}
        if connected(side_a) and connected(side_b):
            state = split_state(side_a, side_b)
            assert any(below(state, maximum) for maximum in MAXIMAL_BAD), state
            checked_splits += 1

    model = (
        ("u",), ("v",), ("x1",), ("x2",),
        ("a", "p"), ("b", "q"), ("x4", "r2"),
    )
    assert is_model(model)

    print(f"vertex deletions checked: {checked_deletions}")
    print(f"relative shore subsets checked: {checked_relative}")
    print(f"connected atlas-negative covering splits checked: {checked_splits}")
    print("three-carrier K7 model: verified")


if __name__ == "__main__":
    main()
