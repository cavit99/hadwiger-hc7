#!/usr/bin/env python3
"""Exhaustively verify the length-four near-complete portal obstruction.

The graph is the nine-vertex leafless core from Section 12 of
hadwiger_dynamic_transit_tree_principle.md.  The three shadow leaves are
irrelevant to a K_6 model, so they are omitted from the exhaustive search.
"""

from itertools import combinations


NAMES = ("a", "x1", "x2", "b", "v", "j", "q1", "q2", "qb")
INDEX = {name: i for i, name in enumerate(NAMES)}


def edge_set():
    edges = {
        tuple(sorted((INDEX[u], INDEX[v])))
        for u, v in (
            ("a", "x1"),
            ("x1", "x2"),
            ("x2", "b"),
            ("v", "a"),
            ("v", "b"),
            ("j", "a"),
        )
    }
    clique = ("j", "q1", "q2", "qb")
    for u, v in combinations(clique, 2):
        edges.add(tuple(sorted((INDEX[u], INDEX[v]))))
    for x in ("a", "x2", "b"):
        edges.add(tuple(sorted((INDEX["q1"], INDEX[x]))))
    for x in ("a", "x1", "b"):
        edges.add(tuple(sorted((INDEX["q2"], INDEX[x]))))
    for x in ("a", "x1", "x2"):
        edges.add(tuple(sorted((INDEX["qb"], INDEX[x]))))
    return edges


EDGES = edge_set()
ADJ = [0] * len(NAMES)
for u, v in EDGES:
    ADJ[u] |= 1 << v
    ADJ[v] |= 1 << u


def connected(mask):
    first = (mask & -mask).bit_length() - 1
    seen = 1 << first
    frontier = seen
    while frontier:
        bit = frontier & -frontier
        frontier -= bit
        u = bit.bit_length() - 1
        new = ADJ[u] & mask & ~seen
        seen |= new
        frontier |= new
    return seen == mask


CONNECTED = [m for m in range(1, 1 << len(NAMES)) if connected(m)]


def touches(a, b):
    if a & b:
        return False
    union_neighbours = 0
    bits = a
    while bits:
        bit = bits & -bits
        bits -= bit
        union_neighbours |= ADJ[bit.bit_length() - 1]
    return bool(union_neighbours & b)


COMPATIBLE = {
    a: {b for b in CONNECTED if b > a and touches(a, b)} for a in CONNECTED
}


def clique_model(order):
    """Return branch-set masks for a K_order model, or None."""

    def search(chosen, candidates, used):
        if len(chosen) == order:
            return chosen
        if len(chosen) + len(candidates) < order:
            return None
        for pos, bag in enumerate(candidates):
            if bag & used:
                continue
            remaining = [
                other
                for other in candidates[pos + 1 :]
                if not (other & (used | bag))
                and other in COMPATIBLE[bag]
            ]
            result = search(chosen + [bag], remaining, used | bag)
            if result is not None:
                return result
        return None

    return search([], CONNECTED, 0)


def decode(mask):
    return {NAMES[i] for i in range(len(NAMES)) if mask & (1 << i)}


assert clique_model(6) is None
witness = clique_model(5)
assert witness is not None

print("PASS: no K6 model in the nine-vertex core")
print("K5 witness:", [sorted(decode(mask)) for mask in witness])

