#!/usr/bin/env python3
"""Conservative quotient for two symmetric ordered root-portal spines."""

from pure_moser_degree9_model_occupancy_probe import has_k7


def build(extra=()):
    vertices = (
        "v", "h", "1", "2", "3", "4",
        "K", "D", "V", "C", "PL", "QL", "PR", "QR",
    )
    edges = set()

    def add(a, b):
        edges.add(frozenset((a, b)))

    for z in ("h", "1", "2", "3", "4", "D", "C"):
        add("v", z)
    for z in ("1", "2", "3", "4", "K", "PL", "V", "PR"):
        add("h", z)
    add("1", "2")
    add("3", "4")
    for z in ("K", "D", "PL"):
        add(z, "1")
        add(z, "2")
    for z in ("V", "C", "PR"):
        add(z, "3")
        add(z, "4")

    for a, b in (
        # Outer locked bags and the outer edge 65.
        ("K", "D"), ("V", "C"), ("D", "C"),
        # Two root spines, with both halves seeing their gate root side.
        ("PL", "QL"), ("K", "PL"), ("K", "QL"),
        ("PR", "QR"), ("V", "PR"), ("V", "QR"),
        # The three old cross-bag adjacencies land on target sides.
        ("D", "QR"), ("C", "QL"), ("QL", "QR"),
    ):
        add(a, b)
    for a, b in extra:
        add(a, b)
    return vertices, edges


if __name__ == "__main__":
    print("base", has_k7(*build()))
    for e in (("PL", "QR"), ("PR", "QL"), ("PL", "C"),
              ("PR", "D"), ("K", "C"), ("V", "D")):
        print(e, has_k7(*build((e,))))
