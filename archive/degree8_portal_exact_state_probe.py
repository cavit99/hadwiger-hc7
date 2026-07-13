#!/usr/bin/env python3
"""Enumerate exact portal-boundary states in the explicit split survivor."""

from itertools import product

from degree8_cutvertex_portal_probe import (
    N, Z, R1, R2, D, TOTAL, concrete_adjacency,
)
from degree8_cutvertex_split_probe import MISS_TYPES


V = 12
APEX = 12
FULL = 13
X = tuple(range(9))

# The type-0 survivor emitted by degree8_cutvertex_portal_probe.py.
MISS_TYPE = MISS_TYPES[0]
VARIABLE_EDGES = [
    (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3),
    (3, 6), (4, 7), (5, 6), (2, Z), (3, Z),
]


def full_adjacency():
    base = concrete_adjacency(VARIABLE_EDGES, MISS_TYPE)
    adj = base + [0]
    for x in range(N):
        adj[APEX] |= 1 << x
        adj[x] |= 1 << APEX
    return adj


ADJ = full_adjacency()


def connected(mask):
    seen = mask & -mask
    frontier = seen
    while frontier:
        bit = frontier & -frontier
        frontier -= bit
        vertex = bit.bit_length() - 1
        new = ADJ[vertex] & mask & ~seen
        seen |= new
        frontier |= new
    return seen == mask


def adjacent(a, b):
    while a:
        bit = a & -a
        a -= bit
        if ADJ[bit.bit_length() - 1] & b:
            return True
    return False


def partitions():
    blocks = []

    def rec(pos):
        if pos == len(X):
            if 1 <= len(blocks) <= 6:
                yield tuple(tuple(block) for block in blocks)
            return
        x = X[pos]
        for i in range(len(blocks)):
            blocks[i].append(x)
            yield from rec(pos + 1)
            blocks[i].pop()
        if len(blocks) < 6:
            blocks.append([x])
            yield from rec(pos + 1)
            blocks.pop()

    yield from rec(0)


def independent(block):
    return all(not (ADJ[x] >> y & 1)
               for i, x in enumerate(block) for y in block[i + 1:])


def realizes(partition, target):
    optional = [APEX, R1, R2, D]
    optional.remove(target)
    q = len(partition)
    base = [sum(1 << x for x in block) for block in partition]
    for assignment in product(range(-1, q), repeat=len(optional)):
        bags = base[:]
        for vertex, block in zip(optional, assignment):
            if block >= 0:
                bags[block] |= 1 << vertex
        if not all(connected(bag) for bag in bags):
            continue
        if all(adjacent(bags[i], bags[j])
               for i in range(q) for j in range(i + 1, q)):
            return tuple(bags)
    return None


def main():
    checked = 0
    one = 0
    two = 0
    for partition in partitions():
        if sum(any(x < N for x in block) for block in partition) > 5:
            continue
        if not all(independent(block) for block in partition):
            continue
        checked += 1
        witnesses = []
        for target in (R1, R2, D):
            witness = realizes(partition, target)
            if witness is None:
                break
            witnesses.append(witness)
        if len(witnesses) >= 1:
            one += 1
        if len(witnesses) >= 2:
            two += 1
        if len(witnesses) == 3:
            print("UNIVERSAL", partition)
            for target, witness in zip((R1, R2, D), witnesses):
                print(" target", target, witness)
            return
    print("no universal exact state; independent partitions", checked,
          "one-side prefixes", one, "two-side prefixes", two)


if __name__ == "__main__":
    main()
