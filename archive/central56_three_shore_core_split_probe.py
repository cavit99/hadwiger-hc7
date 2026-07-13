#!/usr/bin/env python3
"""Exact quotient probe for the three-shore central-56 core split.

The boundary is the pure Moser spindle on h,1,2,5,6,y,z.  One full
shore contains the original literal triangle v,3,4, hence has an
adjacent connected split whose two rows both meet h and 5.  The other
two shores are contracted to full helper vertices.  This probe checks
whether row coverage plus the two common contacts already forces K7.
"""

from __future__ import annotations

from itertools import combinations, product


S = tuple(range(7))
H, ONE, TWO, FIVE, SIX, Y, Z = S
X, W, A, B = 7, 8, 9, 10
V = tuple(range(11))

# The labelled central boundary in the direct pure-Moser placement:
# y,z play the second literal pair.
BOUNDARY = {
    tuple(sorted(edge))
    for edge in (
        (H, ONE), (H, TWO), (H, Y), (H, Z),
        (ONE, TWO), (ONE, SIX), (TWO, SIX),
        (Y, Z), (Y, FIVE), (Z, FIVE), (FIVE, SIX),
    )
}


def set_partitions(values, blocks):
    values = tuple(values)
    current = [[values[0]]]

    def visit(index):
        if index == len(values):
            if len(current) == blocks:
                yield tuple(
                    sum(1 << vertex for vertex in block) for block in current
                )
            return
        vertex = values[index]
        for block in current:
            block.append(vertex)
            yield from visit(index + 1)
            block.pop()
        if len(current) < blocks:
            current.append([vertex])
            yield from visit(index + 1)
            current.pop()

    yield from visit(1)


def candidate_partitions():
    answer = []
    for order in range(7, len(V) + 1):
        for support in combinations(V, order):
            answer.extend(set_partitions(support, 7))
    answer.sort(key=lambda bags: (-sum(mask.bit_count() for mask in bags), bags))
    return tuple(answer)


CANDIDATES = candidate_partitions()


def quotient_edges(row_x, row_w):
    edges = set(BOUNDARY)
    edges.add((X, W))
    for helper in (A, B):
        edges.update((root, helper) for root in S)
    edges.update((root, X) for root in row_x)
    edges.update((root, W) for root in row_w)
    return edges


def k7_model(edges):
    adjacency = [0] * len(V)
    for first, second in edges:
        adjacency[first] |= 1 << second
        adjacency[second] |= 1 << first

    connected_cache = {}
    neighbour_cache = {}

    def connected(mask):
        if mask not in connected_cache:
            reached = mask & -mask
            while True:
                expanded = reached
                bits = reached
                while bits:
                    bit = bits & -bits
                    bits ^= bit
                    expanded |= adjacency[bit.bit_length() - 1] & mask
                if expanded == reached:
                    break
                reached = expanded
            connected_cache[mask] = reached == mask
        return connected_cache[mask]

    def neighbours(mask):
        if mask not in neighbour_cache:
            union = 0
            bits = mask
            while bits:
                bit = bits & -bits
                bits ^= bit
                union |= adjacency[bit.bit_length() - 1]
            neighbour_cache[mask] = union
        return neighbour_cache[mask]

    for bags in CANDIDATES:
        if not all(connected(bag) for bag in bags):
            continue
        if all(
            neighbours(bags[first]) & bags[second]
            for first in range(7)
            for second in range(first)
        ):
            return bags
    return None


def main():
    names = ("h", "1", "2", "5", "6", "y", "z", "X", "W", "A", "B")
    failures = []
    variable = (ONE, TWO, SIX, Y, Z)
    # h and 5 occur in both rows; every other boundary root occurs in at
    # least one row.  Choice 0/1/2 means X-only/W-only/both.
    for choices in product(range(3), repeat=len(variable)):
        row_x = {H, FIVE}
        row_w = {H, FIVE}
        for root, choice in zip(variable, choices):
            if choice != 1:
                row_x.add(root)
            if choice != 0:
                row_w.add(root)
        model = k7_model(quotient_edges(row_x, row_w))
        if model is None:
            failures.append((frozenset(row_x), frozenset(row_w)))

    maximal = [
        pair
        for pair in failures
        if not any(
            pair != other and pair[0] <= other[0] and pair[1] <= other[1]
            for other in failures
        )
    ]
    print("candidate partitions", len(CANDIDATES))
    print("states", 3 ** len(variable), "failures", len(failures), "maximal", len(maximal))
    for left, right in maximal:
        print("X", tuple(names[root] for root in sorted(left)),
              "W", tuple(names[root] for root in sorted(right)))


if __name__ == "__main__":
    main()
