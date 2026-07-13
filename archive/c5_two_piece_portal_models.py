#!/usr/bin/env python3
"""Classify two-piece portal patterns forcing K7 over K2 join C5.

Boundary vertices 0..4 induce C5 and 5,6 are universal to it and adjacent.
Vertices 7,8 are adjacent shore pieces with prescribed boundary contacts;
vertex 9 is the contracted opposite full shore and sees all boundary
vertices, but neither shore piece.
"""

from __future__ import annotations

import itertools

S = tuple(range(7))
A, X, B = 7, 8, 9
V = tuple(range(10))


def set_partitions_k(items, k):
    """Yield unlabeled partitions of items into exactly k blocks."""
    items = tuple(items)
    if not items:
        if k == 0:
            yield ()
        return
    first = items[0]
    for rest in set_partitions_k(items[1:], k - 1):
        yield ((first,),) + rest
    for rest in set_partitions_k(items[1:], k):
        for i in range(len(rest)):
            yield rest[:i] + ((first,) + rest[i],) + rest[i + 1 :]


PARTITION_CANDIDATES = tuple(
    partition
    for size in range(7, 11)
    for used in itertools.combinations(V, size)
    for partition in set_partitions_k(used, 7)
)


def base_edges():
    edges = {tuple(sorted((i, (i + 1) % 5))) for i in range(5)}
    edges.add((5, 6))
    edges.update((i, u) for i in range(5) for u in (5, 6))
    edges.add((A, X))
    edges.update((s, B) for s in S)
    return {tuple(sorted(e)) for e in edges}


def k_minor_model(edges, k=7):
    assert k == 7
    adjacency = [0] * len(V)
    for i, j in edges:
        adjacency[i] |= 1 << j
        adjacency[j] |= 1 << i
    def connected(block):
        target = sum(1 << i for i in block)
        reached = 1 << block[0]
        while True:
            neighbours = 0
            x = reached
            while x:
                bit = x & -x
                neighbours |= adjacency[bit.bit_length() - 1]
                x ^= bit
            expanded = reached | (neighbours & target)
            if expanded == reached:
                break
            reached = expanded
        return reached == target

    def adjacent(a, b):
        return any(adjacency[x] >> y & 1 for x in a for y in b)

    for partition in PARTITION_CANDIDATES:
        if not all(connected(block) for block in partition):
            continue
        if all(adjacent(a, b) for a, b in itertools.combinations(partition, 2)):
            return tuple(sum(1 << x for x in block) for block in partition)
    return None


def as_sets(model):
    return tuple(tuple(i for i in V if mask >> i & 1) for mask in model)


def dihedral(mask):
    out = set()
    core = mask & 31
    universal = mask & ~31
    for shift in range(5):
        r = sum(1 << ((i + shift) % 5) for i in range(5) if core >> i & 1)
        out.add(r | universal)
        f = sum(1 << ((-i + shift) % 5) for i in range(5) if core >> i & 1)
        out.add(f | universal)
    return out


def pair_orbit(pair):
    p, q = pair
    out = set()
    # Same dihedral action on both contact masks; optionally swap universals 5,6
    for shift in range(5):
        for reflect in (False, True):
            for swap_u in (False, True):
                vals = []
                for mask in (p, q):
                    m = 0
                    for i in range(5):
                        if mask >> i & 1:
                            j = ((-i if reflect else i) + shift) % 5
                            m |= 1 << j
                    b5, b6 = bool(mask & 32), bool(mask & 64)
                    if swap_u:
                        b5, b6 = b6, b5
                    if b5:
                        m |= 32
                    if b6:
                        m |= 64
                    vals.append(m)
                out.add(tuple(vals))
                out.add(tuple(reversed(vals)))
    return out


def main():
    base = base_edges()
    good = {}
    pairs = [
        (p, q)
        for p, q in itertools.product(range(1 << 7), repeat=2)
        if p | q == (1 << 7) - 1
    ]
    pairs.sort(key=lambda z: (z[0].bit_count() + z[1].bit_count(), z))
    for p, q in pairs:
        inherited = None
        sp = p
        while True:
            sq = q
            while True:
                if (sp, sq) != (p, q) and (sp, sq) in good:
                    inherited = good[(sp, sq)]
                    break
                if sq == 0:
                    break
                sq = (sq - 1) & q
            if inherited is not None or sp == 0:
                break
            sp = (sp - 1) & p
        if inherited is not None:
            good[(p, q)] = inherited
            continue
        edges = set(base)
        edges.update(tuple(sorted((A, s))) for s in S if p >> s & 1)
        edges.update(tuple(sorted((X, s))) for s in S if q >> s & 1)
        model = k_minor_model(edges)
        if model:
            good[(p, q)] = as_sets(model)

    minimal = []
    for p, q in good:
        dominated = False
        pp = p
        while True:
            qq = q
            while True:
                if (pp, qq) != (p, q) and (pp, qq) in good:
                    dominated = True
                    break
                if qq == 0:
                    break
                qq = (qq - 1) & q
            if dominated or pp == 0:
                break
            pp = (pp - 1) & p
        if dominated:
            continue
        minimal.append((p, q))

    seen = set()
    reps = []
    for pair in minimal:
        if pair in seen:
            continue
        orb = pair_orbit(pair)
        seen.update(orb)
        reps.append(min(orb))
    print("good", len(good), "minimal labeled", len(minimal), "orbits", len(reps))
    for p, q in sorted(reps, key=lambda x: (x[0].bit_count() + x[1].bit_count(), x)):
        print(
            tuple(i for i in S if p >> i & 1),
            tuple(i for i in S if q >> i & 1),
            "model", good.get((p, q)) or good.get((q, p)),
        )


if __name__ == "__main__":
    main()
