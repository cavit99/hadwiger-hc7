#!/usr/bin/env python3
"""Conservative quotient probe for splitting the root-bearing exact-cut shore Z.

The root e0 lies in X.  For each of q,3,4,6, a state 0/1/2 means
contact with X only, Y only, or both.  Only contacts forced by the
degree-nine pure-Moser exact-cut frame are retained.
"""

from itertools import product

from pure_moser_degree9_model_occupancy_probe import has_k7


def build(states):
    vertices = (
        "v", "h", "1", "2", "3", "4", "6", "q",
        "X", "Y", "R5", "R0",
    )
    edges = set()

    def add(a, b):
        if a != b:
            edges.add(frozenset((a, b)))

    # Literal Moser frame after 5 is absorbed in R5.
    for z in ("h", "1", "2", "3", "4", "6", "R5"):
        add("v", z)
    for z in ("1", "2", "3", "4", "X", "R5", "R0"):
        add("h", z)
    add("1", "2")
    add("3", "4")
    add("1", "6")
    add("2", "6")
    for z in ("3", "4"):
        add("R5", z)
        add("R0", z)
    add("6", "R5")
    add("R5", "R0")
    add("q", "R0")
    add("X", "Y")

    for state, terminal in zip(states, ("q", "3", "4", "6")):
        if state in (0, 2):
            add("X", terminal)
        if state in (1, 2):
            add("Y", terminal)
    return vertices, edges


def main():
    negative = []
    for states in product(range(3), repeat=4):
        if has_k7(*build(states)):
            print("K7", states)
        else:
            negative.append(states)
    print("negative", len(negative), negative)


if __name__ == "__main__":
    main()
