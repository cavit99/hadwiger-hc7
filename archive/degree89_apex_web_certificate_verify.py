#!/usr/bin/env python3
"""Independent finite check of the two crossing completions.

For k=4,5 and every alternating four-terminal choice, this verifier checks
from first principles that:

* cycle + cross + an adjacent universal pair + apex has a K7 minor; and
* cycle + cross + one universal boundary vertex + an opposite full shore
  has a boundary-meeting K6 minor.

The paths are represented conservatively by two degree-two helper vertices.
No contact other than the two prescribed terminal pairs is granted to the
crossed shore.
"""

from itertools import combinations


def add_edge(adj, x, y):
    adj[x] |= 1 << y
    adj[y] |= 1 << x


def connected(mask, adj):
    first = (mask & -mask).bit_length() - 1
    seen = frontier = 1 << first
    while frontier:
        bit = frontier & -frontier
        frontier -= bit
        x = bit.bit_length() - 1
        new = adj[x] & mask & ~seen
        seen |= new
        frontier |= new
    return seen == mask


def adjacent(left, right, adj):
    bits = left
    while bits:
        bit = bits & -bits
        bits -= bit
        x = bit.bit_length() - 1
        if adj[x] & right:
            return True
    return False


def find_model(adj, target, required_trace=0):
    total = len(adj)
    candidates = [
        mask for mask in range(1, 1 << total)
        if (not required_trace or mask & required_trace)
        and connected(mask, adj)
    ]

    def search(options, chosen):
        if len(chosen) == target:
            return tuple(chosen)
        if len(options) < target - len(chosen):
            return None
        while options:
            bag = options.pop()
            compatible = [
                other for other in options
                if not (bag & other) and adjacent(bag, other, adj)
            ]
            result = search(compatible, chosen + [bag])
            if result is not None:
                return result
        return None

    return search(candidates, [])


def base_cross(k, four):
    # Frame 0,...,k-1.  Helpers k,k+1 realize chords a-c and b-d.
    adj = [0] * (k + 2)
    for x in range(k):
        add_edge(adj, x, (x + 1) % k)
    a, b, c, d = four
    for x in (a, c):
        add_edge(adj, k, x)
    for x in (b, d):
        add_edge(adj, k + 1, x)
    return adj


def verify_universal_pair(k, four):
    base = base_cross(k, four)
    # p,q,v
    p, q, v = k + 2, k + 3, k + 4
    adj = base + [0, 0, 0]
    for r in range(k):
        add_edge(adj, p, r)
        add_edge(adj, q, r)
        add_edge(adj, v, r)
    add_edge(adj, p, q)
    add_edge(adj, v, p)
    add_edge(adj, v, q)
    model = find_model(adj, 7)
    assert model is not None, (k, four, "universal pair")
    return model


def verify_opposite_shore(k, four):
    base = base_cross(k, four)
    # p,q are boundary vertices.  d is the opposite full shore.
    p, q, shore = k + 2, k + 3, k + 4
    adj = base + [0, 0, 0]
    for r in range(k):
        add_edge(adj, p, r)
        add_edge(adj, shore, r)
    add_edge(adj, shore, p)
    add_edge(adj, shore, q)
    boundary = (1 << k) - 1 | 1 << p | 1 << q
    model = find_model(adj, 6, required_trace=boundary)
    assert model is not None, (k, four, "opposite shore")
    return model


def main():
    checked = 0
    for k in (4, 5):
        for four in combinations(range(k), 4):
            universal = verify_universal_pair(k, four)
            opposite = verify_opposite_shore(k, four)
            assert len(universal) == 7
            assert len(opposite) == 6
            checked += 1
    print("verified", checked, "cyclic crossing types for both completions")


if __name__ == "__main__":
    main()
