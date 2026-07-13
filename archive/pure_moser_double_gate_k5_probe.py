#!/usr/bin/env python3
"""Exact quotient check showing that a K--5 edge alone is not enough.

The two locked bags L6 and R5 are both split:

    L6 = U + D,     R5 = V + C,

where U,V contain the exterior roots, D contains 6, and C contains 5.
All four old adjacencies to L0,R0 are placed on the outer pieces D,C.
In addition to the unavoidable D--C edge 56, add U--C, representing a
literal K--5 edge.  The exact branch-set search returns no K7 minor.
"""

from pure_moser_degree9_model_occupancy_probe import has_k7


def graph():
    vertices = (
        "v", "h", "1", "2", "3", "4",
        "U", "D", "V", "C", "L0", "R0",
    )
    edges: set[frozenset[str]] = set()

    def add(x: str, y: str) -> None:
        edges.add(frozenset((x, y)))

    for z in ("h", "1", "2", "3", "4", "D", "C"):
        add("v", z)
    for z in ("1", "2", "3", "4", "U", "L0", "V", "R0"):
        add("h", z)
    add("1", "2")
    add("3", "4")
    for z in ("U", "D", "L0"):
        add(z, "1")
        add(z, "2")
    for z in ("V", "C", "R0"):
        add(z, "3")
        add(z, "4")

    # The two internal gates and the literal edges K--5 and 56.
    for x, y in (("U", "D"), ("V", "C"), ("U", "C"), ("D", "C")):
        add(x, y)

    # Conservative allocation of the remaining old rooted-model edges.
    for x, y in (
        ("L0", "R0"),
        ("D", "L0"), ("D", "R0"),
        ("C", "L0"), ("C", "R0"),
    ):
        add(x, y)
    return vertices, edges


if __name__ == "__main__":
    print("has_K7", has_k7(*graph()))
