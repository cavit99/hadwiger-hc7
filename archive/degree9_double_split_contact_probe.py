#!/usr/bin/env python3
"""Probe sufficient quotient contacts after splitting L6 and R0.

U denotes K plus a peeled connected piece X of R0; Y is the rooted
residue of R0.  The fixed case is K not adjacent to L0, so D (the
6-side of L6) retains the old L6--L0 contact.  We vary the contacts
U--R5, D--Y, L0--Y, and R5--Y.  The peel itself gives U--L0 and U--Y.
"""

from itertools import product

from pure_moser_degree9_model_occupancy_probe import has_k7


def build(bits):
    vertices = (
        "v", "h", "1", "2", "3", "4",
        "U", "D", "L0", "R5", "Y",
    )
    edges: set[frozenset[str]] = set()

    def add(x, y):
        edges.add(frozenset((x, y)))

    for x in ("h", "1", "2", "3", "4", "D", "R5"):
        add("v", x)
    for x in ("1", "2", "3", "4", "U", "L0", "R5", "Y"):
        add("h", x)
    add("1", "2"); add("3", "4")
    for x in ("U", "D", "L0"):
        add(x, "1"); add(x, "2")
    for x in ("R5", "Y"):
        add(x, "3"); add(x, "4")

    # Fixed connected pieces and inherited contacts.
    add("U", "D")
    add("D", "L0")
    add("D", "R5")  # 6--5
    add("L0", "R5")
    add("U", "L0")  # peeled X reaches an L0 portal
    add("U", "Y")   # X is adjacent to its connected residue

    for bit, pair in zip(bits, (
        ("U", "R5"), ("D", "Y"), ("L0", "Y"), ("R5", "Y")
    )):
        if bit:
            add(*pair)
    return vertices, edges


def main():
    for bits in product((0, 1), repeat=4):
        print(bits, has_k7(*build(bits)))


if __name__ == "__main__":
    main()
