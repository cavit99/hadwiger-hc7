#!/usr/bin/env python3
"""Smallest raw-role-compatible seven-connected terminal-lobe diagnostic.

This graph deliberately contains a K7 minor.  Its purpose is to prove
that seven-connectivity plus the raw terminal portal/model data does not
by itself force the internal two-root swap.  It violates the subsequent
direct-cross exclusions of Lemma 2.2.
"""

from itertools import combinations

from pure_moser_degree9_model_occupancy_probe import has_k7


VERTICES = (
    "v", "h", "1", "2", "3", "4", "5", "6",
    "Z", "J", "r5", "r0", "p1", "s",
)
MOSER = {
    frozenset(edge) for edge in (
        ("h", "1"), ("h", "2"), ("h", "3"), ("h", "4"),
        ("1", "2"), ("1", "6"), ("2", "6"),
        ("3", "4"), ("3", "5"), ("4", "5"), ("5", "6"),
    )
}


def build():
    n_v = {"h", "1", "2", "3", "4", "5", "6"}
    n_h = {"v", "1", "2", "3", "4", "Z", "J", "r5", "r0"}
    n_z = {"h", "1", "2", "6", "J", "p1", "s"}
    root_lobe = {"J", "p1"}
    right_bags = {"5", "r5", "r0"}
    edges = set()
    for x, y in combinations(VERTICES, 2):
        edge = frozenset((x, y))
        allowed = True
        if "v" in edge:
            allowed = (y if x == "v" else x) in n_v
        if "h" in edge:
            allowed = (y if x == "h" else x) in n_h
        if "Z" in edge:
            allowed = (y if x == "Z" else x) in n_z
        if {x, y} <= {"h", "1", "2", "3", "4", "5", "6"}:
            allowed = edge in MOSER
        if ((x in root_lobe and y in right_bags) or
                (y in root_lobe and x in right_bags)):
            allowed = False
        if allowed:
            edges.add(edge)
    return edges


def adjacency(edges):
    answer = {x: set() for x in VERTICES}
    for edge in edges:
        x, y = edge
        answer[x].add(y); answer[y].add(x)
    return answer


def connected_after(adjacency_map, deleted):
    deleted = set(deleted)
    remaining = set(VERTICES) - deleted
    root = next(iter(remaining))
    seen = {root}; stack = [root]
    while stack:
        x = stack.pop()
        for y in adjacency_map[x] - deleted - seen:
            seen.add(y); stack.append(y)
    return seen == remaining


def check_model(edges, model):
    used = set()
    for bag in model:
        bag = set(bag)
        assert bag and not (used & bag)
        used |= bag
        reached = {next(iter(bag))}
        while True:
            grown = reached | {
                y for x in reached for y in bag
                if frozenset((x, y)) in edges
            }
            if grown == reached:
                break
            reached = grown
        assert reached == bag
    for i in range(7):
        for j in range(i + 1, 7):
            assert any(
                frozenset((x, y)) in edges
                for x in model[i] for y in model[j]
            )


def main():
    edges = build()
    adj = adjacency(edges)

    assert adj["v"] == {"h", "1", "2", "3", "4", "5", "6"}
    assert {edge for edge in edges if edge <= adj["v"]} == MOSER
    assert len(adj["h"]) == 9
    assert adj["Z"] == {"h", "1", "2", "6", "J", "p1", "s"}

    # Q={J,p1,s}; deleting s leaves the root-bearing lobe {J,p1},
    # which has no contact to either right bag.  J,p1,s are three
    # distinct active portal endpoints from the singleton Z.
    assert frozenset(("J", "p1")) in edges
    assert frozenset(("J", "s")) in edges
    for x in ("J", "p1"):
        for y in ("5", "r5", "r0"):
            assert frozenset((x, y)) not in edges
    assert all(frozenset(("Z", x)) in edges for x in ("J", "p1", "s"))
    assert all(frozenset(("s", x)) in edges for x in ("r5", "r0"))

    # Four connected bags L6={Z,6}, L0={J,p1,s}, R5={5,r5}, R0={r0}
    # and their six pairwise adjacencies.
    assert frozenset(("Z", "6")) in edges
    assert frozenset(("5", "r5")) in edges
    for edge in (
        ("Z", "J"), ("6", "5"), ("6", "r0"),
        ("s", "r5"), ("s", "r0"), ("r5", "r0"),
    ):
        assert frozenset(edge) in edges

    # Exhaustive vertex-connectivity audit.
    for order in range(7):
        for deleted in combinations(VERTICES, order):
            assert connected_after(adj, deleted), (order, deleted)
    # N(v) is a seven-cut, so connectivity is exactly seven.
    assert not connected_after(adj, adj["v"])

    assert has_k7(VERTICES, edges)
    # Direct-cross certificate (2.7): Z--S and J--D are both present.
    check_model(edges, [
        ["h"], ["1"], ["2"], ["Z"], ["J"],
        ["6", "5", "r5"], ["v", "3", "s", "r0"],
    ])
    print("PASS: exact terminal data and vertex-connectivity 7 on 14 vertices")
    print("PASS: direct-cross K7 certificate; graph is not an ordered-web survivor")


if __name__ == "__main__":
    main()
