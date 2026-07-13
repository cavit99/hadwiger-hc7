#!/usr/bin/env python3
"""Explicit 81-profile K7 atlas for the overlapping-Moser outer peel.

This is not an arbitrary minor search.  For each ordered pair of the nine
realizable component profiles, the table selects one of nine displayed
branch-set templates and checks it directly.

Profiles:
  A, B:  the component meets only a or only b, and is full to W;
  F:     the component meets a,b and is full to W;
  1,2,3,4,P,Q: it meets a,b and misses exactly that one vertex of W.
"""

from itertools import combinations


def edge(a, b):
    return frozenset((a, b))


W = ("x1", "x2", "x3", "x4", "p", "q")
LABELS = ("A", "B", "F", "1", "2", "3", "4", "P", "Q")
MISSED = {
    "A": None,
    "B": None,
    "F": None,
    "1": "x1",
    "2": "x2",
    "3": "x3",
    "4": "x4",
    "P": "p",
    "Q": "q",
}
OUTER_CONTACTS = {
    "A": ("a",),
    "B": ("b",),
    "F": ("a", "b"),
    "1": ("a", "b"),
    "2": ("a", "b"),
    "3": ("a", "b"),
    "4": ("a", "b"),
    "P": ("a", "b"),
    "Q": ("a", "b"),
}


CORE_EDGES = {
    edge("u", "v"),
    *(edge("u", x) for x in W),
    *(edge("v", x) for x in ("x1", "x2", "x3", "x4", "a", "b")),
    edge("x1", "x2"),
    edge("x3", "x4"),
    edge("a", "b"),
    edge("p", "q"),
    edge("a", "x1"),
    edge("a", "x2"),
    edge("b", "x3"),
    edge("b", "x4"),
    edge("p", "x3"),
    edge("p", "x4"),
    edge("q", "x1"),
    edge("q", "x2"),
}


TEMPLATES = {
    1: (("u",), ("x1",), ("x2",), ("v", "x3"),
        ("p", "r1"), ("q", "r2"), ("x4", "a", "b")),
    2: (("u",), ("x1",), ("x2",), ("v", "x3"),
        ("q", "r1"), ("p", "r2"), ("x4", "a", "b")),
    3: (("u",), ("x3",), ("x4",), ("v", "x2"),
        ("p", "r1"), ("q", "r2"), ("x1", "a", "b")),
    4: (("u",), ("x3",), ("x4",), ("v", "x1"),
        ("q", "r1"), ("p", "r2"), ("x2", "a", "b")),
    5: (("u",), ("x3",), ("x4",), ("v", "x1"),
        ("p", "r1"), ("q", "r2"), ("x2", "a", "b")),
    6: (("u",), ("x1",), ("x2",), ("v", "x4"),
        ("p", "r1"), ("q", "r2"), ("x3", "a", "b")),
    7: (("u",), ("x1",), ("x2",), ("v", "x4"),
        ("q", "r1"), ("p", "r2"), ("x3", "a", "b")),
    8: (("u",), ("x3",), ("x4",), ("v", "x2"),
        ("q", "r1"), ("p", "r2"), ("x1", "a", "b")),
    9: (("v",), ("x1",), ("x2",), ("u", "x3"),
        ("a", "r1"), ("b", "r2"), ("x4", "p", "q")),
}


# Rows and columns occur in LABELS order.  Entry k selects TEMPLATES[k].
ATLAS = (
    (1, 1, 1, 1, 1, 2, 1, 1, 2),
    (1, 1, 1, 1, 1, 2, 1, 1, 2),
    (1, 1, 1, 1, 1, 2, 1, 1, 2),
    (2, 2, 2, 3, 4, 2, 2, 3, 2),
    (2, 2, 2, 5, 5, 2, 2, 5, 2),
    (1, 1, 1, 1, 1, 6, 1, 1, 7),
    (1, 1, 1, 1, 1, 2, 1, 1, 2),
    (2, 2, 2, 8, 4, 2, 2, 9, 2),
    (1, 1, 1, 1, 1, 6, 1, 1, 9),
)


def graph_for(first, second):
    edges = set(CORE_EDGES)
    for shore, profile in (("r1", first), ("r2", second)):
        for x in OUTER_CONTACTS[profile]:
            edges.add(edge(shore, x))
        missed = MISSED[profile]
        for x in W:
            if x != missed:
                edges.add(edge(shore, x))
    return edges


def connected(edges, bag):
    bag = set(bag)
    reached = {next(iter(bag))}
    while True:
        expanded = reached | {
            y for x in reached for y in bag if edge(x, y) in edges
        }
        if expanded == reached:
            return reached == bag
        reached = expanded


def touching(edges, left, right):
    return any(edge(x, y) in edges for x in left for y in right)


def is_k7_model(edges, bags):
    bags = tuple(frozenset(bag) for bag in bags)
    return (
        all(bags[i].isdisjoint(bags[j])
            for i, j in combinations(range(7), 2))
        and all(connected(edges, bag) for bag in bags)
        and all(touching(edges, bags[i], bags[j])
                for i, j in combinations(range(7), 2))
    )


def main():
    assert len(ATLAS) == len(LABELS)
    checked = 0
    usage = {number: 0 for number in TEMPLATES}
    for i, first in enumerate(LABELS):
        for j, second in enumerate(LABELS):
            number = ATLAS[i][j]
            assert number in TEMPLATES
            assert is_k7_model(graph_for(first, second), TEMPLATES[number]), (
                first, second, number
            )
            usage[number] += 1
            checked += 1

    assert checked == 81
    assert all(usage.values())
    print("explicit two-component portal profiles verified: 81/81")
    print("template usage:", " ".join(
        f"{number}:{usage[number]}" for number in sorted(usage)
    ))


if __name__ == "__main__":
    main()
