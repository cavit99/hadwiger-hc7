#!/usr/bin/env python3
"""Search the support-four one-sibling quotient for a uniform K7^vee lift.

The two old full packets are kept as singleton rim bags.  It is therefore
enough to find four pairwise adjacent, disjoint, connected S-rooted bags in
the twelve-vertex boundary/theta core, and a fifth disjoint connected
S-rooted bag adjacent to at least two of them.  The search restricts core
bags to order at most three; success is a monotone literal certificate.
"""

from itertools import combinations, product


SHAPES = {
    "claw_411": [(0, 3), (0, 6), (1, 4), (2, 5), (2, 6), (4, 6)],
    "claw_321": [(0, 6), (1, 3), (1, 4), (2, 5), (2, 6), (4, 6)],
    "claw_222": [(0, 6), (1, 3), (1, 5), (2, 5), (2, 6), (4, 6)],
    "c6_leaf": [
        (0, 3), (0, 6), (1, 3), (1, 5), (2, 5), (2, 6), (4, 6)
    ],
    "claw_plus_triangle": [(0, 6), (1, 3), (1, 5), (2, 6), (3, 5), (4, 6)],
}

S = range(7)
GATES = (7, 8, 9)
K, J = 10, 11
FOUR_SETS = tuple(combinations(S, 4))


def rows_for(shape_edges, a_support, b_support, gate_contacts):
    rows = [0] * 12

    def add(u, v):
        rows[u] |= 1 << v
        rows[v] |= 1 << u

    for edge in shape_edges:
        add(*edge)
    for gate in GATES:
        add(K, gate)
        add(J, gate)
    for s in a_support:
        add(K, s)
    for s in b_support:
        add(J, s)
    for s, gate in gate_contacts:
        add(s, gate)
    return rows


def connected(mask, rows):
    reached = mask & -mask
    while True:
        old = reached
        bits = reached
        while bits:
            bit = bits & -bits
            bits ^= bit
            reached |= rows[bit.bit_length() - 1] & mask
        if reached == old:
            return reached == mask


def adjacent(a, b, rows):
    bits = a
    neighbourhood = 0
    while bits:
        bit = bits & -bits
        bits ^= bit
        neighbourhood |= rows[bit.bit_length() - 1]
    return bool(neighbourhood & b)


def certificate(rows):
    candidates = []
    for size in (1, 2, 3):
        for vertices in combinations(range(12), size):
            mask = sum(1 << v for v in vertices)
            if not (mask & ((1 << 7) - 1)):
                continue
            if connected(mask, rows):
                candidates.append(mask)

    pair_ok = {}

    def compatible(a, b):
        key = (a, b) if a < b else (b, a)
        if key not in pair_ok:
            pair_ok[key] = not (a & b) and adjacent(a, b, rows)
        return pair_ok[key]

    def extend(chosen, used, start):
        if len(chosen) == 4:
            for centre in candidates:
                if centre & used:
                    continue
                if sum(compatible(centre, rim) for rim in chosen) >= 2:
                    return tuple(chosen), centre
            return None

        for index in range(start, len(candidates)):
            bag = candidates[index]
            if bag & used:
                continue
            if all(compatible(bag, old) for old in chosen):
                found = extend(chosen + [bag], used | bag, index + 1)
                if found is not None:
                    return found
        return None

    return extend([], 0, 0)


def names(mask):
    labels = ("0", "1", "2", "3", "4", "5", "6", "x", "y", "z", "K", "J")
    return tuple(labels[v] for v in range(12) if mask >> v & 1)


def main():
    checked = 0
    maximum_bag = 0
    examples = {}
    for shape, edges in SHAPES.items():
        for a_support in FOUR_SETS:
            for b_support in FOUR_SETS:
                missing = sorted(set(S) - set(a_support) - set(b_support))
                for assignment in product(GATES, repeat=len(missing)):
                    contacts = tuple(zip(missing, assignment))
                    rows = rows_for(edges, a_support, b_support, contacts)
                    found = certificate(rows)
                    checked += 1
                    if found is None:
                        print(
                            "SURVIVOR",
                            shape,
                            a_support,
                            b_support,
                            contacts,
                        )
                        return
                    rim, centre = found
                    maximum_bag = max(
                        maximum_bag,
                        *(bag.bit_count() for bag in (*rim, centre)),
                    )
                    examples.setdefault(
                        shape,
                        {
                            "A": a_support,
                            "B": b_support,
                            "contacts": contacts,
                            "rim": tuple(names(bag) for bag in rim),
                            "centre": names(centre),
                        },
                    )
    print("GREEN", "checked", checked, "maximum_bag", maximum_bag)
    for shape, example in examples.items():
        print(shape, example)


if __name__ == "__main__":
    main()
