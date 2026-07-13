#!/usr/bin/env python3
"""Conservative quotient for a root-prefix row on the ordered L0 spine."""

from pure_moser_degree9_model_occupancy_probe import has_k7


def build(add_pd=False):
    vertices=("v","h","1","2","3","4","P","S","K","D","R5","R0")
    edges=set()
    def add(a,b): edges.add(frozenset((a,b)))
    for x in ("h","1","2","3","4","D","R5"): add("v",x)
    for x in ("1","2","3","4","P","K","R5","R0"): add("h",x)
    add("1","2");add("3","4")
    for x in ("P","K","D"):
        add(x,"1");add(x,"2")
    for x in ("R5","R0"):
        add(x,"3");add(x,"4")
    for a,b in (
        ("P","S"),("P","K"),("S","K"),("K","D"),
        ("D","R5"),("D","R0"),("S","R5"),("S","R0"),("R5","R0"),
    ): add(a,b)
    if add_pd: add("P","D")
    return vertices,edges


if __name__=="__main__":
    print("K_only",has_k7(*build(False)))
    print("with_PD",has_k7(*build(True)))
