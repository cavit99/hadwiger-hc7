#!/usr/bin/env python3
"""Independent replay of the displayed 2K3+K1 portal-lock models."""

from __future__ import annotations

import itertools


def check(vertices, edges, bags):
    edges = {frozenset(edge) for edge in edges}
    assert all(bags)
    assert sum(map(len, bags)) == len(set().union(*bags))
    assert all(not (bags[i] & bags[j])
               for i, j in itertools.combinations(range(7), 2))

    def connected(bag):
        reached = {next(iter(bag))}
        while True:
            more = {y for x in reached for y in bag
                    if frozenset((x, y)) in edges}
            if more <= reached:
                return reached == bag
            reached |= more

    assert all(connected(bag) for bag in bags)
    assert all(any(frozenset((x, y)) in edges for x in bags[i]
                   for y in bags[j])
               for i, j in itertools.combinations(range(7), 2))


def boundary_edges():
    A = ("a", "ap", "app")
    B = ("b", "bp", "bpp")
    S = A + B + ("c",)
    return ({frozenset((x, y)) for x in A for y in B}
            | {frozenset(("c", x)) for x in A + B}), S


def branching_model():
    edges, S = boundary_edges()
    edges |= {frozenset(("h", s)) for s in S}
    edges |= {frozenset((x, s)) for x in ("x", "y")
              for s in S if s != "a"}
    edges |= {frozenset(("z", x)) for x in ("a", "x", "y")}
    bags = tuple(map(set, (
        ("a",), ("b",), ("c",), ("h",), ("ap", "bp"),
        ("x", "bpp"), ("y", "z", "app"),
    )))
    check(set(S) | {"h", "x", "y", "z"}, edges, bags)


def second_contact_model():
    edges, S = boundary_edges()
    edges |= {frozenset(("h", s)) for s in S}
    edges |= {frozenset(("r", s)) for s in S if s != "a"}
    edges |= {frozenset(("z", x)) for x in ("a", "ap", "r")}
    bags = tuple(map(set, (
        ("a",), ("b",), ("c",), ("h",), ("app", "bp"),
        ("r", "bpp"), ("z", "ap"),
    )))
    check(set(S) | {"h", "r", "z"}, edges, bags)


def two_opposite_contacts_model():
    edges, S = boundary_edges()
    edges |= {frozenset(("h", s)) for s in S}
    edges |= {frozenset(("r", s)) for s in S if s != "a"}
    edges |= {frozenset(("z", x)) for x in ("a", "bp", "bpp", "r")}
    bags = tuple(map(set, (
        ("ap",), ("bp",), ("c",), ("r",), ("a", "b"),
        ("z", "bpp"), ("h", "app"),
    )))
    check(set(S) | {"h", "r", "z"}, edges, bags)


if __name__ == "__main__":
    branching_model()
    second_contact_model()
    two_opposite_contacts_model()
    print("portal-lock models replayed: 3")
