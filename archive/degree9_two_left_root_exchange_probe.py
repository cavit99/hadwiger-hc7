#!/usr/bin/env python3
"""Minimal quotient for the two-left-bag root exchange."""

from pure_moser_degree9_model_occupancy_probe import has_k7


def build(extra=()):
    vertices=("v","h","1","2","3","4","P","S","E","T","D","R5","R0")
    edges=set()
    def add(a,b): edges.add(frozenset((a,b)))
    for z in ("h","1","2","3","4","D","R5"):add("v",z)
    # r0 is in P; e6 is in E.
    for z in ("1","2","3","4","P","E","R5","R0"):add("h",z)
    add("1","2");add("3","4")
    for z in ("P","E","D"):
        add(z,"1");add(z,"2")
    for z in ("R5","R0"):
        add(z,"3");add(z,"4")
    # Minimal old model and exchange contacts.
    for a,b in (
        ("P","S"),("P","T"),("S","E"),("E","T"),("T","D"),
        ("D","R5"),("D","R0"),("S","R5"),("S","R0"),("R5","R0"),
    ):add(a,b)
    for a,b in extra:add(a,b)
    return vertices,edges


if __name__=="__main__":
    print("minimal",has_k7(*build()))
    print("both_P",has_k7(*build((("P","E"),))))
    print("both_S",has_k7(*build((("S","T"),))))
    print("both",has_k7(*build((("P","E"),("S","T")))))
