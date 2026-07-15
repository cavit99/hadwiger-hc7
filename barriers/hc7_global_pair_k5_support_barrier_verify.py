#!/usr/bin/env python3
"""Exact K5-support census for the two-apex icosahedron guardrail.

For every unordered vertex pair P in G = K2 join I, compute

    mu(P) = min |union M|

over all K5 minor models M in G-P, with infinity when none exists.  The
search is dependency-free and exhaustive: for a proposed order bound b it
enumerates every connected candidate bag of order at most b-4, then every
disjoint pairwise-adjacent five-tuple whose total order is at most b.
"""

from itertools import combinations


TOP, BOTTOM = 10, 11
APEX_A, APEX_B = 12, 13
VERTICES = tuple(range(14))


def edge(a, b):
    return tuple(sorted((a, b)))


I_EDGES = set()
for i in range(5):
    I_EDGES.update(
        {
            edge(TOP, i),
            edge(BOTTOM, 5 + i),
            edge(i, (i + 1) % 5),
            edge(5 + i, 5 + (i + 1) % 5),
            edge(i, 5 + i),
            edge(i, 5 + (i - 1) % 5),
        }
    )

G_EDGES = set(I_EDGES)
for apex in (APEX_A, APEX_B):
    for vertex in range(12):
        G_EDGES.add(edge(apex, vertex))
G_EDGES.add(edge(APEX_A, APEX_B))

ADJ = [0] * len(VERTICES)
for left, right in G_EDGES:
    ADJ[left] |= 1 << right
    ADJ[right] |= 1 << left


def connected(mask):
    if not mask:
        return False
    seen = mask & -mask
    frontier = seen
    while frontier:
        vertex_bit = frontier & -frontier
        frontier ^= vertex_bit
        vertex = vertex_bit.bit_length() - 1
        new = ADJ[vertex] & mask & ~seen
        seen |= new
        frontier |= new
    return seen == mask


def touch(left, right):
    scan = left
    neighbours = 0
    while scan:
        vertex_bit = scan & -scan
        scan ^= vertex_bit
        neighbours |= ADJ[vertex_bit.bit_length() - 1]
    return bool(neighbours & right)


def candidate_bags(pair, maximum_order):
    forbidden = (1 << pair[0]) | (1 << pair[1])
    allowed = [vertex for vertex in VERTICES if not forbidden & (1 << vertex)]
    bags = []
    for size in range(1, maximum_order + 1):
        for choice in combinations(allowed, size):
            mask = sum(1 << vertex for vertex in choice)
            if connected(mask):
                bags.append(mask)
    return bags


def find_model(pair, order_bound):
    bags = candidate_bags(pair, order_bound - 4)
    sizes = [bag.bit_count() for bag in bags]

    def search(start, chosen, used, order):
        needed = 5 - len(chosen)
        if not needed:
            return tuple(bags[index] for index in chosen)
        if order + needed > order_bound:
            return None
        for index in range(start, len(bags)):
            bag = bags[index]
            new_order = order + sizes[index]
            if new_order + needed - 1 > order_bound:
                continue
            if bag & used:
                continue
            if any(not touch(bag, bags[old]) for old in chosen):
                continue
            answer = search(
                index + 1,
                (*chosen, index),
                used | bag,
                new_order,
            )
            if answer is not None:
                return answer
        return None

    return search(0, (), 0, 0)


def minimum_support(pair):
    # The apex pair leaves the planar icosahedron, which has no K5 minor.
    # This is the unique terminal and needs no exponential failed search.
    if pair == edge(APEX_A, APEX_B):
        return None, None
    for order_bound in range(5, 9):
        witness = find_model(pair, order_bound)
        if witness is not None:
            return order_bound, witness
    raise AssertionError(f"no order-at-most-eight witness for {pair}")


def classify_pair(pair):
    apex_count = sum(vertex in (APEX_A, APEX_B) for vertex in pair)
    base_edge = apex_count == 0 and edge(*pair) in I_EDGES
    return apex_count, base_edge


def main():
    census = {}
    witnesses = {}
    values = {}
    for pair in combinations(VERTICES, 2):
        value, witness = minimum_support(pair)
        census.setdefault((classify_pair(pair), value), []).append(pair)
        witnesses[pair] = witness
        values[pair] = value

    for key in sorted(census, key=str):
        print(key, len(census[key]), census[key][:5])

    terminal = edge(APEX_A, APEX_B)
    assert witnesses[terminal] is None
    assert all(
        witnesses[pair] is not None
        for pair in combinations(VERTICES, 2)
        if pair != terminal
    )

    # Exact distribution.  Every pair wholly in the planar base has a
    # literal K5 after deletion (the two apices plus a surviving triangle),
    # every apex--base pair first admits a K5 model at order seven, and the
    # apex pair is terminal.
    assert sum(value == 5 for value in values.values()) == 66
    assert sum(value == 7 for value in values.values()) == 24
    assert sum(value is None for value in values.values()) == 1

    # The reduced rotation triangle from
    # hc7_global_invariant_rotation_triangle.md has these three unique
    # missing bag pairs.  Verify the three near-K7 quotients literally and
    # then check the stronger plateau: *every* choice of one literal vertex
    # from each missing bag has mu=5.
    C = frozenset({3, 4, 8, 9})
    fixed_rows = (
        frozenset({1, 6}),
        frozenset({2}),
        frozenset({5, 7, BOTTOM}),
        frozenset({APEX_A}),
        frozenset({APEX_B}),
    )
    states = (
        (frozenset({TOP}), frozenset({0}) | C, 2),
        (C, frozenset({TOP, 0}), 0),
        (frozenset({0}), frozenset({TOP}) | C, 1),
    )
    for centre, donor, missed_row in states:
        bags = (centre, donor, *fixed_rows)
        assert len(set().union(*bags)) == sum(map(len, bags))
        assert all(connected(sum(1 << vertex for vertex in bag)) for bag in bags)
        for left, right in combinations(range(7), 2):
            left_mask = sum(1 << vertex for vertex in bags[left])
            right_mask = sum(1 << vertex for vertex in bags[right])
            is_missing = {left, right} == {0, 2 + missed_row}
            assert touch(left_mask, right_mask) != is_missing
        for left in centre:
            for right in fixed_rows[missed_row]:
                assert values[edge(left, right)] == 5

    # The three rotations preserve the coarse carrier exactly.
    assert all(centre | donor == frozenset({TOP, 0}) | C for centre, donor, _ in states)
    print(
        "GREEN: the neutral near-K7 rotation triangle sees only mu=5 "
        "missing pairs, while the hidden apex pair has mu=infinity"
    )


if __name__ == "__main__":
    main()
