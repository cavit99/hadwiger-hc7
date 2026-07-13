#!/usr/bin/env python3
"""Test K7 minors forced by two Moser shores with distinct packet types.

Each shore packet is represented by two adjacent contracted carrier
vertices, one for each of two pair blocks in a 2+2+2+1 boundary mode.
The apex is complete to the seven boundary vertices.  This is the weakest
quotient justified by two-packet capacity on each shore.
"""

from itertools import combinations


S = tuple(range(7))
MOSER = {
    tuple(sorted(map(int, edge)))
    for edge in "01 02 03 04 12 16 26 34 35 45 56".split()
}
NONEDGES = set(combinations(S, 2)) - MOSER
APEX = 7
D0, D1 = 8, 9
E0, E1 = 10, 11
V = tuple(range(12))


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
    for size in range(7, len(V) + 1):
        for used in combinations(V, size):
            for bags in partitions(used, 7):
                masks = [sum(1 << vertex for vertex in bag) for bag in bags]
                if not all(connected(mask, adjacency) for mask in masks):
                    continue
                if all(
                    any(adjacency[u] & masks[j] for u in bags[i])
                    for i in range(7)
                    for j in range(i)
                ):
                    return True, bags
    return False, None


def matching_modes():
    out = []
    for singleton in S:
        for chosen in combinations(NONEDGES, 3):
            ends = [vertex for edge in chosen for vertex in edge]
            if len(set(ends)) == 6 and set(ends) == set(S) - {singleton}:
                out.append((singleton, tuple(sorted(chosen))))
    return tuple(sorted(set(out)))


def quotient(matching, d_type, e_type):
    edges = set(MOSER)
    edges.update((min(APEX, s), max(APEX, s)) for s in S)
    d_pairs = [matching[index] for index in d_type]
    e_pairs = [matching[index] for index in e_type]
    edges.add((D0, D1))
    edges.add((E0, E1))
    for carrier, pair in zip((D0, D1), d_pairs):
        edges.update((min(carrier, s), max(carrier, s)) for s in pair)
    for carrier, pair in zip((E0, E1), e_pairs):
        edges.update((min(carrier, s), max(carrier, s)) for s in pair)
    return edges


def main():
    packet_types = tuple(combinations(range(3), 2))
    negative = []
    for singleton, matching in matching_modes():
        for d_type in packet_types:
            for e_type in packet_types:
                if d_type == e_type:
                    continue
                positive, bags = has_k7(quotient(matching, d_type, e_type))
                if not positive:
                    negative.append((singleton, matching, d_type, e_type))
                else:
                    print("positive", singleton, matching, d_type, e_type, bags)
    print("negative_count", len(negative))
    for item in negative:
        print("negative", item)


if __name__ == "__main__":
    main()
