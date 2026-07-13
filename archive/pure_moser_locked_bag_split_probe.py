#!/usr/bin/env python3
"""Classify contact allocations after splitting the locked L6 bag."""

from itertools import product

from pure_moser_degree9_model_occupancy_probe import has_k7


def build(states):
    # state 1=U only, 2=D only, 3=both, for targets L0,R5,R0.
    vertices = ("v", "h", "1", "2", "3", "4", "U", "D", "L0", "R5", "R0")
    edges: set[frozenset[str]] = set()

    def add(x, y):
        edges.add(frozenset((x, y)))

    for x in ("h", "1", "2", "3", "4", "D", "R5"):
        add("v", x)
    for x in ("1", "2", "3", "4", "U", "L0", "R5", "R0"):
        add("h", x)
    add("1", "2"); add("3", "4")
    for x in ("U", "D", "L0"):
        add(x, "1"); add(x, "2")
    for x in ("R5", "R0"):
        add(x, "3"); add(x, "4")
    add("U", "D")
    # The fixed outer edge 56 joins D to the bag R5.
    add("D", "R5")
    # The three unaffected old bags remain a K3.
    add("L0", "R5"); add("L0", "R0"); add("R5", "R0")
    for state, target in zip(states, ("L0", "R5", "R0")):
        if state & 1:
            add("U", target)
        if state & 2:
            add("D", target)
    return vertices, edges


def main():
    negative = []
    for states in product((1, 2, 3), repeat=3):
        if not has_k7(*build(states)):
            negative.append(states)
    print("negative", len(negative), "of 27")
    for states in negative:
        print(states)


if __name__ == "__main__":
    main()
