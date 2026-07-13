#!/usr/bin/env python3
"""Probe the lock case where K misses both right bags and has multiple
portals in L0; L0 is split into a rooted side Y and a second side X,
both adjacent to K.  Vary which side retains the two old right contacts.
"""

from itertools import product
from pure_moser_degree9_model_occupancy_probe import has_k7


def build(state):
    # state 0=X only, 1=Y only, 2=both for R5 and R0 contacts.
    vertices = ("v","h","1","2","3","4","K","D","X","Y","R5","R0")
    edges = set()
    def add(a,b):
        if a != b: edges.add(frozenset((a,b)))
    for x in ("h","1","2","3","4","D","R5"): add("v",x)
    for x in ("1","2","3","4","K","Y","R5","R0"): add("h",x)
    add("1","2"); add("3","4")
    for x in ("K","D","Y"): add(x,"1"); add(x,"2")
    for x in ("R5","R0"): add(x,"3"); add(x,"4")
    add("K","D"); add("K","X"); add("K","Y"); add("X","Y")
    add("D","R5"); add("D","R0")
    add("R5","R0")
    for s,target in zip(state,("R5","R0")):
        if s in (0,2): add("X",target)
        if s in (1,2): add("Y",target)
    return vertices,edges


for state in product(range(3),repeat=2):
    print(state,has_k7(*build(state)))
