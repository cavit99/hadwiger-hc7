#!/usr/bin/env python3
"""Diagnostic quotients for the root-bearing Moser gate."""

from itertools import product

from pure_moser_degree9_model_occupancy_probe import has_k7


def build(u3=False, u4=False, extra=()):
    vertices = (
        "v", "h", "1", "2", "3", "4",
        "K", "U", "Q", "D", "R5", "R0",
    )
    edges = set()

    def add(a, b):
        edges.add(frozenset((a, b)))

    for z in ("h", "1", "2", "3", "4", "D", "R5"):
        add("v", z)
    for z in ("1", "2", "3", "4", "K", "U", "R5", "R0"):
        add("h", z)
    add("1", "2")
    add("3", "4")
    for z in ("K", "U", "D"):
        add(z, "1")
        add(z, "2")
    for z in ("R5", "R0"):
        add(z, "3")
        add(z, "4")
    for a, b in (
        ("K", "U"), ("U", "Q"), ("K", "D"),
        ("D", "R5"), ("D", "R0"),
        ("Q", "R5"), ("Q", "R0"), ("R5", "R0"),
    ):
        add(a, b)
    if u3:
        add("U", "3")
    if u4:
        add("U", "4")
    for a, b in extra:
        add(a, b)
    return vertices, edges


def main():
    candidates = (("U", "D"), ("U", "R5"), ("U", "R0"),
                  ("K", "R5"), ("K", "R0"), ("Q", "D"))
    for u3, u4 in product((False, True), repeat=2):
        print("literal", u3, u4, has_k7(*build(u3, u4)))
        for edge in candidates:
            print(" +", edge, has_k7(*build(u3, u4, (edge,))))


if __name__ == "__main__":
    main()
