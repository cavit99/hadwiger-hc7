#!/usr/bin/env python3
"""Classify C5 + adjacent pair neighbourhoods at a planar-frame vertex.

The five cycle vertices are 0..4 and the adjacent pair is 5,6.  We vary
the ten cross edges, require independence number at most two, and reject a
K4 minor supported on at most five of the seven vertices.  Survivors are
grouped under the dihedral symmetries of the cycle and interchange of 5,6.
"""

from itertools import combinations


V = tuple(range(7))
CYCLE = {(i, (i + 1) % 5) if i < (i + 1) % 5 else ((i + 1) % 5, i) for i in range(5)}
CYCLE = {tuple(sorted(edge)) for edge in CYCLE}
BASE = CYCLE | {(5, 6)}
CROSS = tuple((u, t) for t in (5, 6) for u in range(5))


def adjacency(edges):
    out = {v: set() for v in V}
    for x, y in edges:
        out[x].add(y)
        out[y].add(x)
    return out


def alpha_at_most_two(edges):
    adj = adjacency(edges)
    return all(
        any(y in adj[x] for x, y in combinations(triple, 2))
        for triple in combinations(V, 3)
    )


def connected(part, adj):
    reached = {next(iter(part))}
    while True:
        new = reached | {y for x in reached for y in adj[x] if y in part}
        if new == reached:
            return reached == part
        reached = new


def partitions(items, count):
    items = tuple(items)
    bags = []

    def rec(i):
        if i == len(items):
            if len(bags) == count:
                yield tuple(frozenset(bag) for bag in bags)
            return
        value = items[i]
        for bag in bags:
            bag.append(value)
            yield from rec(i + 1)
            bag.pop()
        if len(bags) < count:
            bags.append([value])
            yield from rec(i + 1)
            bags.pop()

    yield from rec(0)


def has_small_k4(edges):
    adj = adjacency(edges)
    for size in (4, 5):
        for used in combinations(V, size):
            for bags in partitions(used, 4):
                if not all(connected(set(bag), adj) for bag in bags):
                    continue
                if all(
                    any(y in adj[x] for x in bags[i] for y in bags[j])
                    for i in range(4)
                    for j in range(i)
                ):
                    return True
    return False


def transforms():
    maps = []
    for reverse in (False, True):
        for shift in range(5):
            for swap in (False, True):
                mapping = {}
                for u in range(5):
                    w = -u if reverse else u
                    mapping[u] = (w + shift) % 5
                mapping[5], mapping[6] = ((6, 5) if swap else (5, 6))
                maps.append(mapping)
    return maps


def canonical(edges):
    forms = []
    for mapping in transforms():
        forms.append(tuple(sorted(tuple(sorted((mapping[x], mapping[y]))) for x, y in edges)))
    return min(forms)


def main():
    survivors = {}
    for mask in range(1 << len(CROSS)):
        edges = set(BASE)
        edges.update(CROSS[i] for i in range(len(CROSS)) if mask & (1 << i))
        edges = {tuple(sorted(edge)) for edge in edges}
        if not alpha_at_most_two(edges) or has_small_k4(edges):
            continue
        survivors.setdefault(canonical(edges), 0)
        survivors[canonical(edges)] += 1
    print("survivor_orbits", len(survivors), "labelled", sum(survivors.values()))
    for form, orbit_size in sorted(survivors.items(), key=lambda item: (len(item[0]), item[0])):
        cross = tuple(edge for edge in form if edge not in BASE)
        print("orbit", orbit_size, "edge_count", len(form), "cross", cross)


if __name__ == "__main__":
    main()
