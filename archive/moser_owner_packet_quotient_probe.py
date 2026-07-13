#!/usr/bin/env python3
"""Exact K7 test for one two-block packet plus an opposite full shore."""

from itertools import combinations


S = tuple(range(7))
MOSER = {
    tuple(sorted(map(int, edge)))
    for edge in "01 02 03 04 12 16 26 34 35 45 56".split()
}
NONEDGES = set(combinations(S, 2)) - MOSER
X, Y, H = 7, 8, 9
V = tuple(range(10))


def connected(mask, adjacency):
    first = mask & -mask
    reached = first
    while True:
        expanded = reached
        bits = reached
        while bits:
            bit = bits & -bits
            bits ^= bit
            expanded |= adjacency[bit.bit_length() - 1] & mask
        if expanded == reached:
            return reached == mask
        reached = expanded


def partitions(items, count):
    items = tuple(items)
    bags = []

    def rec(index):
        if index == len(items):
            if len(bags) == count:
                yield tuple(tuple(bag) for bag in bags)
            return
        value = items[index]
        for bag in bags:
            bag.append(value)
            yield from rec(index + 1)
            bag.pop()
        if len(bags) < count:
            bags.append([value])
            yield from rec(index + 1)
            bags.pop()

    yield from rec(0)


def has_k7(edges):
    adjacency = [0] * len(V)
    for u, v in edges:
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u
    for size in range(7, 11):
        for used in combinations(V, size):
            for bags in partitions(used, 7):
                masks = [sum(1 << vertex for vertex in bag) for bag in bags]
                if not all(connected(mask, adjacency) for mask in masks):
                    continue
                if all(
                    any(adjacency[u] & masks[j] for u in bags[i])
                    for i in range(7) for j in range(i)
                ):
                    return True, bags
    return False, None


def matchings():
    out = []
    for singleton in S:
        for chosen in combinations(NONEDGES, 3):
            ends = [v for edge in chosen for v in edge]
            if len(set(ends)) == 6 and set(ends) == set(S) - {singleton}:
                out.append((singleton, tuple(sorted(chosen))))
    return tuple(sorted(set(out)))


def quotient(first, second):
    edges = set(MOSER)
    edges.add((X, Y))
    edges.update((min(H, s), max(H, s)) for s in S)
    edges.update((min(X, s), max(X, s)) for s in first)
    edges.update((min(Y, s), max(Y, s)) for s in second)
    return edges


def main():
    for singleton, matching in matchings():
        row = []
        for i, j in combinations(range(3), 2):
            positive, bags = has_k7(quotient(matching[i], matching[j]))
            row.append((matching[i], matching[j], positive, bags))
        print("state", singleton, matching)
        for result in row:
            print(" ", result)


if __name__ == "__main__":
    main()
