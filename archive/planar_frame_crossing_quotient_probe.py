#!/usr/bin/env python3
"""Classify conservative crossing quotients for C5 + adjacent pair.

Vertices 0..4 form the frame cycle, 5,6 are adjacent, and 7 is the
degree-seven apex complete to 0..6.  Vertices 8,9 represent the adjacent
connected pieces of a crossing in the sole exterior.  For every boundary
cross-edge pattern with independence number at most two, test all five
four-terminal crossings for a K7 minor.
"""

from itertools import combinations


BOUNDARY = tuple(range(7))
V = tuple(range(10))
APEX, X, Y = 7, 8, 9
CYCLE = {tuple(sorted((i, (i + 1) % 5))) for i in range(5)}
BASE = CYCLE | {(5, 6)}
CROSS_EDGES = tuple((u, t) for t in (5, 6) for u in range(5))


def adjacency(edges):
    out = [0] * len(V)
    for a, b in edges:
        out[a] |= 1 << b
        out[b] |= 1 << a
    return out


def alpha_at_most_two(edges):
    adj = adjacency(edges)
    return all(
        (adj[a] & (1 << b)) or (adj[a] & (1 << c)) or (adj[b] & (1 << c))
        for a, b, c in combinations(BOUNDARY, 3)
    )


def connected(mask, adj):
    reached = mask & -mask
    while True:
        expanded = reached
        bits = reached
        while bits:
            bit = bits & -bits
            bits ^= bit
            expanded |= adj[bit.bit_length() - 1] & mask
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


PARTITIONS = {
    size: tuple(
        tuple(partitions(used, 7))
        for used in combinations(V, size)
    )
    for size in range(7, 11)
}


def has_k7(edges):
    adj = adjacency(edges)
    for size in range(7, 11):
        for family in PARTITIONS[size]:
            for bags in family:
                masks = [sum(1 << v for v in bag) for bag in bags]
                if not all(connected(mask, adj) for mask in masks):
                    continue
                if all(
                    any(adj[u] & masks[j] for u in bags[i])
                    for i in range(7)
                    for j in range(i)
                ):
                    return True, bags
    return False, None


def crossing_pairs(omitted):
    order = [v for v in range(5) if v != omitted]
    # Preserve cyclic order after deleting one point.
    start = (omitted + 1) % 5
    order = [(start + step) % 5 for step in range(4)]
    return (order[0], order[2]), (order[1], order[3])


def transforms():
    for reverse in (False, True):
        for shift in range(5):
            for swap in (False, True):
                mapping = {}
                for u in range(5):
                    w = -u if reverse else u
                    mapping[u] = (w + shift) % 5
                mapping[5], mapping[6] = ((6, 5) if swap else (5, 6))
                yield mapping


def canonical(boundary_edges):
    forms = []
    for mapping in transforms():
        forms.append(tuple(sorted(tuple(sorted((mapping[a], mapping[b]))) for a, b in boundary_edges)))
    return min(forms)


def main():
    negative = {}
    checked = 0
    for mask in range(1 << len(CROSS_EDGES)):
        boundary = set(BASE)
        boundary.update(CROSS_EDGES[i] for i in range(len(CROSS_EDGES)) if mask & (1 << i))
        boundary = {tuple(sorted(edge)) for edge in boundary}
        if not alpha_at_most_two(boundary):
            continue
        checked += 1
        failed = []
        for omitted in range(5):
            xpair, ypair = crossing_pairs(omitted)
            fixed_x, fixed_y = set(xpair), set(ypair)
            remaining = tuple(sorted(set(BOUNDARY) - fixed_x - fixed_y))
            bad_partitions = 0
            for side_mask in range(1 << len(remaining)):
                xrow = set(fixed_x)
                yrow = set(fixed_y)
                for index, u in enumerate(remaining):
                    (xrow if side_mask & (1 << index) else yrow).add(u)
                edges = set(boundary)
                edges.update((min(APEX, u), max(APEX, u)) for u in BOUNDARY)
                edges.add((X, Y))
                edges.update((min(X, u), max(X, u)) for u in xrow)
                edges.update((min(Y, u), max(Y, u)) for u in yrow)
                positive, bags = has_k7(edges)
                if not positive:
                    bad_partitions += 1
            if bad_partitions:
                failed.append((omitted, bad_partitions))
        if failed:
            key = canonical(boundary)
            negative.setdefault(key, set()).update(failed)
    print("alpha_patterns", checked, "negative_orbits", len(negative))
    for form, failed in sorted(negative.items(), key=lambda item: (len(item[0]), item[0])):
        cross = tuple(edge for edge in form if edge not in BASE)
        print("edge_count", len(form), "cross", cross, "failed", tuple(sorted(failed)))


if __name__ == "__main__":
    main()
