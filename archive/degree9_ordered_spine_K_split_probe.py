#!/usr/bin/env python3
"""Quotient test for splitting K behind an ordered L0 prefix."""

from itertools import product

from pure_moser_degree9_model_occupancy_probe import has_k7


def build(root_side=0, d_state=0):
    # K=X+Y. root_side contains the L6 root.
    # d_state: 0=X only, 1=Y only, 2=both contacts D.
    vertices = (
        "v", "h", "1", "2", "3", "4",
        "P", "S", "X", "Y", "D", "R5", "R0",
    )
    edges = set()

    def add(a, b):
        edges.add(frozenset((a, b)))

    for z in ("h", "1", "2", "3", "4", "D", "R5"):
        add("v", z)
    for z in ("1", "2", "3", "4", "P", ("X", "Y")[root_side], "R5", "R0"):
        add("h", z)
    add("1", "2"); add("3", "4")
    for z in ("P", ("X", "Y")[root_side], "D"):
        add(z, "1"); add(z, "2")
    for z in ("R5", "R0"):
        add(z, "3"); add(z, "4")
    for a, b in (
        ("P", "S"), ("P", "X"), ("P", "Y"), ("X", "Y"),
        ("S", "X"), ("S", "Y"),
        ("D", "R5"), ("D", "R0"),
        ("S", "R5"), ("S", "R0"), ("R5", "R0"),
    ):
        add(a, b)
    if d_state in (0, 2): add("X", "D")
    if d_state in (1, 2): add("Y", "D")
    return vertices, edges


if __name__ == "__main__":
    for root_side, d_state in product(range(2), range(3)):
        print(root_side, d_state, has_k7(*build(root_side, d_state)))
