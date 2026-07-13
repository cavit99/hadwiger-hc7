#!/usr/bin/env python3
"""Exact quotient probe for the first D-transfer split.

W is the absorbed left rooted side; D=X+Y with 6 in Y.  Both X,Y
are W-adjacent.  L is the residual L0 core and retains both right-bag
contacts.  Its literal left root may remain in L or have been absorbed
into W.  State entries record extra D contacts to R5,R0:
0=X only, 1=Y only, 2=both.  The edge Y--R5 is always present via 65.
"""

from itertools import product

from pure_moser_degree9_model_occupancy_probe import has_k7


def build(root_in_l: bool, states):
    vertices = (
        "v","h","1","2","3","4",
        "W","X","Y","L","R5","R0",
    )
    edges = set()
    def add(a,b):
        if a != b:
            edges.add(frozenset((a,b)))
    for z in ("h","1","2","3","4","Y","R5"):
        add("v",z)
    for z in ("1","2","3","4","W","R5","R0"):
        add("h",z)
    add("1","2"); add("3","4")
    for z in ("W","Y"):
        add(z,"1"); add(z,"2")
    if root_in_l:
        add("h","L"); add("1","L"); add("2","L")
    for z in ("R5","R0"):
        add(z,"3"); add(z,"4")

    for a,b in (
        ("W","X"),("W","Y"),("W","L"),("X","Y"),
        ("Y","R5"),("L","R5"),("L","R0"),("R5","R0"),
    ):
        add(a,b)
    for state,target in zip(states,("R5","R0")):
        if state in (0,2): add("X",target)
        if state in (1,2): add("Y",target)
    return vertices,edges


def main():
    for root in (False,True):
        print("root_in_L",root)
        for states in product(range(3),repeat=2):
            print(states,has_k7(*build(root,states)))


if __name__ == "__main__":
    main()
