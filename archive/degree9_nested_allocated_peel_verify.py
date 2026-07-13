#!/usr/bin/env python3
"""Audit the four literal allocations in the nested one-sided peel.

The quotient vertices E,T represent the two connected root sides after a
connected piece of J is peeled into Z.  D,S,R5,R0 denote connected bags;
D contains 6 and R5 contains 5.
"""

from itertools import combinations


def add(edges, x, y):
    edges.add(frozenset((x, y)))


def connected(bag, edges):
    seen = {next(iter(bag))}
    while True:
        grown = seen | {
            y for x in seen for y in bag
            if frozenset((x, y)) in edges
        }
        if grown == seen:
            return grown == bag
        seen = grown


def check_model(edges, bags):
    used = set()
    for bag in bags:
        bag = set(bag)
        assert bag and not bag & used
        used |= bag
        assert connected(bag, edges), ("disconnected", bag)
    for i, j in combinations(range(len(bags)), 2):
        assert any(frozenset((x, y)) in edges
                   for x in bags[i] for y in bags[j]), (i, j, bags)


def base_graph():
    edges = set()
    # Moser boundary, with 6 represented by D and 5 represented by R5.
    for x in ("h", "1", "2", "3", "4", "D", "R5"):
        add(edges, "v", x)
    for x, y in (
        ("h", "1"), ("h", "2"), ("h", "3"), ("h", "4"),
        ("1", "2"), ("1", "D"), ("2", "D"),
        ("3", "4"), ("3", "R5"), ("4", "R5"),
        ("D", "R5"),
    ):
        add(edges, x, y)

    # Both left root sides see h,1,2.  Right bags see h,3,4.
    for left in ("E", "T"):
        for x in ("h", "1", "2"):
            add(edges, left, x)
    for right in ("R5", "R0"):
        for x in ("h", "3", "4"):
            add(edges, right, x)

    # Connected split and retained four-bag carrier adjacencies.
    for x, y in (
        ("E", "T"), ("E", "D"),
        ("D", "R0"), ("S", "R5"), ("S", "R0"),
        ("R5", "R0"),
    ):
        add(edges, x, y)
    return edges


def audit_all_allocations():
    literals = {"3", "4"}
    for mask in range(4):
        on_d = {str(3 + i) for i in range(2) if mask & (1 << i)}
        on_s = literals - on_d
        edges = base_graph()

        # The peeled E side already sees D.  Give it one S-class exit.
        if on_s:
            add(edges, "E", min(on_s))
        else:
            add(edges, "E", "S")

        # The root-bearing T side sees both allocated carrier classes.
        if on_d:
            add(edges, "T", min(on_d))
        else:
            add(edges, "T", "D")
        if on_s:
            add(edges, "T", min(on_s))
        else:
            add(edges, "T", "S")

        if on_s:
            carrier_d = {"D", "R5"} | on_d
            carrier_s = {"S", "R0", "v"} | on_s
        else:
            # With no literal on the v-side, v attaches through v5.
            carrier_d = {"D", "R0"} | on_d
            carrier_s = {"S", "R5", "v"}

        check_model(edges, [
            {"h"}, {"1"}, {"2"}, {"E"}, {"T"},
            carrier_d, carrier_s,
        ])
        print("PASS allocation D:", "".join(sorted(on_d)) or "-",
              "S:", "".join(sorted(on_s)) or "-")


if __name__ == "__main__":
    audit_all_allocations()
