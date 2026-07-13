#!/usr/bin/env python3
"""Extend the same-bag split probe by the L0--D portal class."""

from itertools import product

from pure_moser_degree9_model_occupancy_probe import has_k7


def build(state):
    # states: R5, R0, D.  0=X only, 1=Y only, 2=both, 3=neither.
    vertices = ("v","h","1","2","3","4","K","D","X","Y","R5","R0")
    edges = set()
    def add(a,b):
        if a != b:
            edges.add(frozenset((a,b)))
    for x in ("h","1","2","3","4","D","R5"):
        add("v",x)
    for x in ("1","2","3","4","K","Y","R5","R0"):
        add("h",x)
    add("1","2"); add("3","4")
    for x in ("K","D","Y"):
        add(x,"1"); add(x,"2")
    for x in ("R5","R0"):
        add(x,"3"); add(x,"4")
    add("K","D"); add("K","X"); add("K","Y"); add("X","Y")
    add("D","R5"); add("D","R0"); add("R5","R0")
    for s,target in zip(state[:2],("R5","R0")):
        if s in (0,2): add("X",target)
        if s in (1,2): add("Y",target)
    s = state[2]
    if s in (0,2): add("X","D")
    if s in (1,2): add("Y","D")
    return vertices,edges


def main():
    for state in product(range(3), repeat=3):
        print(state, has_k7(*build(state)))


if __name__ == "__main__":
    main()
