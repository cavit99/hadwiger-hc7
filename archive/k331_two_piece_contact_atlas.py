#!/usr/bin/env python3
"""Exact two-piece contact atlas for the K_{3,3} join K_1 boundary.

The quotient has the seven boundary vertices, two adjacent vertices x,y
obtained by splitting one shore, and a full helper h obtained by
contracting the opposite shore.  For every pair of nonempty contact
masks M_x,M_y whose union is the boundary, determine whether the
ten-vertex quotient contains K_7.  The output lists the maximal negative
contact pairs; negativity is downward closed.
"""

import itertools


S = tuple(range(7))
A = frozenset((0, 1, 5))
B = frozenset((2, 3, 4))
U = 6
X, Y, H = 7, 8, 9
V = tuple(range(10))


def set_partitions(values, blocks):
    """Yield canonical partitions of values into exactly blocks blocks."""
    values = tuple(values)
    if not values:
        if blocks == 0:
            yield ()
        return
    first = values[0]

    def rec(index, current):
        if index == len(values):
            if len(current) == blocks:
                yield tuple(tuple(block) for block in current)
            return
        value = values[index]
        for position in range(len(current)):
            current[position].append(value)
            yield from rec(index + 1, current)
            current[position].pop()
        if len(current) < blocks:
            current.append([value])
            yield from rec(index + 1, current)
            current.pop()

    yield from rec(1, [[first]])


def candidate_partitions():
    answer = []
    for order in range(7, 11):
        for support in itertools.combinations(V, order):
            for partition in set_partitions(support, 7):
                answer.append(tuple(sum(1 << v for v in block)
                                    for block in partition))
    answer.sort(key=lambda bags: (-sum(mask.bit_count() for mask in bags),
                                  bags))
    return tuple(answer)


CANDIDATES = candidate_partitions()


def quotient_edges(mask_x, mask_y):
    missing = (set(itertools.combinations(A, 2)) |
               set(itertools.combinations(B, 2)))
    edges = set(itertools.combinations(S, 2)) - missing
    edges.add((X, Y))
    edges.update((s, H) for s in S)
    edges.update((s, X) for s in mask_x)
    edges.update((s, Y) for s in mask_y)
    return {tuple(sorted(edge)) for edge in edges}


def fast_k7_model(edges):
    adjacency = [0] * len(V)
    for a, b in edges:
        adjacency[a] |= 1 << b
        adjacency[b] |= 1 << a

    connected_cache = {}

    def connected(mask):
        if mask in connected_cache:
            return connected_cache[mask]
        reached = mask & -mask
        while True:
            expanded = reached
            bits = reached
            while bits:
                low = bits & -bits
                expanded |= adjacency[low.bit_length() - 1] & mask
                bits ^= low
            if expanded == reached:
                result = reached == mask
                connected_cache[mask] = result
                return result
            reached = expanded

    neighbour_cache = {}

    def neighbour_union(mask):
        if mask not in neighbour_cache:
            union = 0
            bits = mask
            while bits:
                low = bits & -bits
                union |= adjacency[low.bit_length() - 1]
                bits ^= low
            neighbour_cache[mask] = union
        return neighbour_cache[mask]

    for bags in CANDIDATES:
        if not all(connected(bag) for bag in bags):
            continue
        if all(neighbour_union(bags[i]) & bags[j]
               for i in range(7) for j in range(i)):
            return bags
    return None


def mask_set(mask):
    return frozenset(s for s in S if mask >> s & 1)


def main():
    failures = []
    full = (1 << 7) - 1
    # Three choices per boundary vertex: x only, y only, or both.
    for code in range(3 ** 7):
        value = code
        mask_x = mask_y = 0
        for s in S:
            choice = value % 3
            value //= 3
            if choice != 1:
                mask_x |= 1 << s
            if choice != 0:
                mask_y |= 1 << s
        assert mask_x | mask_y == full
        mx, my = mask_set(mask_x), mask_set(mask_y)
        if fast_k7_model(quotient_edges(mx, my)) is None:
            failures.append((mx, my))

    maximal = []
    for pair in failures:
        if not any(pair != other and pair[0] <= other[0] and
                   pair[1] <= other[1] for other in failures):
            maximal.append(pair)

    print("candidate branch partitions", len(CANDIDATES))
    print("contact pairs checked", 3 ** 7)
    print("negative pairs", len(failures))
    print("maximal negative pairs", len(maximal))
    for mx, my in sorted(maximal,
                         key=lambda p: (tuple(sorted(p[0])),
                                        tuple(sorted(p[1])))):
        print("X", tuple(sorted(mx)), "Y", tuple(sorted(my)))


if __name__ == "__main__":
    main()
