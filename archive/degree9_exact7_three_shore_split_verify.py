#!/usr/bin/env python3
"""Replay the branch sets in the central exact-7 three-shore closure."""

from itertools import combinations, permutations


S = ("h", "1", "2", "5", "6", "y", "z")
V, R, A, B = "v", "R", "A", "B"

CORE = {
    ("h", "1"), ("h", "2"), ("1", "2"),
    ("1", "6"), ("2", "6"), ("5", "6"),
}

ROWS = (
    {("5", "y"), ("5", "z"), ("y", "z"),
     ("6", "y"), ("h", "z")},
    {("5", "y"), ("5", "z"), ("y", "z"),
     ("6", "z"), ("h", "y")},
    {("5", "y"), ("5", "z"), ("y", "z"),
     ("h", "y"), ("h", "z")},
)

MOSER = {
    (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
    (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
}


def norm(edge):
    return tuple(sorted(edge))


def connected(bag, edges):
    if not bag:
        return False
    reached = {next(iter(bag))}
    while True:
        nxt = reached | {
            y for x in reached for y in bag if norm((x, y)) in edges
        }
        if nxt == reached:
            return reached == bag
        reached = nxt


def adjacent(left, right, edges):
    return any(norm((x, y)) in edges for x in left for y in right)


def bags_for(defect, row):
    triangle = ({"h"}, {"1"}, {"2"})
    if defect in (None, "y", "z"):
        tail = ({V}, {R}, {A, "5"}, {B, "6"})
    elif defect == "h":
        q = "y" if norm(("h", "y")) in row else "z"
        tail = ({V}, {R, q}, {A, "5"}, {B, "6"})
    elif defect in ("1", "2"):
        tail = ({A}, {V, "5"}, {R, "6"}, {B, "y"})
    elif defect == "5":
        tail = ({V}, {R}, {A, "6"}, {B, "5", "y"})
    elif defect == "6":
        tail = ({V}, {R}, {A, "5"}, {B, "6", "y", "z"})
    else:
        raise AssertionError(defect)
    return triangle + tail


def main():
    # Reconstruct, rather than assume, every labelled pure-Moser row
    # containing the six forced boundary edges.
    reconstructed = set()
    for image in permutations(range(7)):
        labelling = dict(zip(S, image))
        if not all(norm((labelling[x], labelling[y])) in MOSER
                   for x, y in CORE):
            continue
        labelled_edges = frozenset(
            norm((x, y)) for x, y in combinations(S, 2)
            if norm((labelling[x], labelling[y])) in MOSER
        )
        reconstructed.add(labelled_edges)
    expected = {
        frozenset(norm(e) for e in CORE | extra) for extra in ROWS
    }
    assert reconstructed == expected
    assert all(all(norm(e) in row for e in (("5", "y"),
                                             ("5", "z"),
                                             ("y", "z")))
               for row in reconstructed)
    print("verified the three exhaustive labelled Moser rows")

    checked = 0
    for row_number, extra in enumerate(ROWS, start=1):
        boundary = {norm(e) for e in CORE | extra}
        for defect in (None,) + S:
            edges = set(boundary)
            edges |= {norm((V, x)) for x in ("h", "1", "2", "5", "6")}
            edges.add(norm((V, R)))
            edges |= {norm((R, x)) for x in S if x != defect}
            edges |= {norm((shore, x)) for shore in (A, B) for x in S}

            bags = bags_for(defect, boundary)
            assert all(connected(set(bag), edges) for bag in bags)
            assert all(set(x).isdisjoint(y) for x, y in combinations(bags, 2))
            assert all(adjacent(set(x), set(y), edges)
                       for x, y in combinations(bags, 2))
            checked += 1
            print(f"PASS row={row_number} defect={defect}")
    assert checked == 24
    print("verified 24 three-shore branch-set rows")


if __name__ == "__main__":
    main()
