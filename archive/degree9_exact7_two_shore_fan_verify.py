#!/usr/bin/env python3
"""Replay the separated-fan K7 model in the central exact two-shore cut."""

from itertools import combinations


S = ("h", "1", "2", "5", "6", "y", "z")
V, R, X, Y = "v", "R", "X", "Y"


def norm(e):
    return tuple(sorted(e))


def connected(bag, edges):
    reached = {next(iter(bag))}
    while True:
        nxt = reached | {b for a in reached for b in bag
                         if norm((a, b)) in edges}
        if nxt == reached:
            return reached == bag
        reached = nxt


def adjacent(a, b, edges):
    return any(norm((x, y)) in edges for x in a for y in b)


def main():
    for defect in (None, "y", "z"):
        edges = {norm(e) for e in (
            ("h", "1"), ("h", "2"), ("1", "2"),
            ("1", "6"), ("2", "6"), ("5", "6"),
            (V, "h"), (V, "1"), (V, "2"), (V, "5"), (V, "6"),
            (V, R),
            (X, "h"), (X, "1"), (X, "2"), (X, "5"),
            (Y, "h"), (Y, "6"),
        )}
        edges |= {norm((R, s)) for s in S if s != defect}
        bags = (
            {"h"}, {"1"}, {"2"}, {V}, {R}, {X, "5"}, {Y, "6"}
        )
        assert all(connected(set(b), edges) for b in bags)
        assert all(set(a).isdisjoint(b) for a, b in combinations(bags, 2))
        assert all(adjacent(set(a), set(b), edges)
                   for a, b in combinations(bags, 2))
        print(f"PASS defect={defect}")
    # Literal-K4 placement: the unoperated opposite shore D is full.
    D = "D"
    edges = {norm(e) for e in (
        ("v", "h"), ("v", "1"), ("v", "2"),
        ("h", "1"), ("h", "2"), ("1", "2"),
        ("v", "5"), ("v", "6"), ("1", "6"),
        ("2", "6"), ("5", "6"),
        (X, "h"), (X, "1"), (X, "2"), (X, "5"),
        (Y, "h"), (Y, "6"),
    )}
    edges |= {norm((D, s)) for s in S}
    edges.add(norm((D, "v")))
    bags = (
        {"v"}, {"h"}, {"1"}, {"2"}, {D}, {X, "5"}, {Y, "6"}
    )
    assert all(connected(set(b), edges) for b in bags)
    assert all(set(a).isdisjoint(b) for a, b in combinations(bags, 2))
    assert all(adjacent(set(a), set(b), edges)
               for a, b in combinations(bags, 2))
    print("PASS literal-K4 placement")
    print("verified the separated central fan models")


if __name__ == "__main__":
    main()
