#!/usr/bin/env python3
"""Does an opposite-shore Moser crossing close a degree-eight triple lock?

The all-crossless shore is represented by x and its connected body B=D-x.
The opposite shore crossing is represented by adjacent connected carriers
E,F, each contacting the endpoints of one of two disjoint missing-C5 edges.
No unused remainder of the opposite shore is assumed.
"""

from itertools import combinations, product

from moser_curvature_quotient_probe import MOSER, N, U, W, X, BODY, L, connected, adjacent, partitions

A = 1
E, F = 10, 11
CYCLE = (0, 5, 2, 4, 6)
FRAMES = []
for i in range(5):
    e = frozenset((CYCLE[i], CYCLE[(i + 1) % 5]))
    f = frozenset((CYCLE[(i + 2) % 5], CYCLE[(i + 3) % 5]))
    key = frozenset((e, f))
    if key not in FRAMES:
        FRAMES.append(key)


def base_edges(pair):
    i = CYCLE.index(pair[0])
    assert CYCLE[(i + 1) % 5] == pair[1]
    shield = CYCLE[(i + 3) % 5]
    contacts = {pair[0], pair[1], shield, W, A}
    edges = set(MOSER)
    edges.add(frozenset((X, BODY)))
    edges |= {frozenset((X, z)) for z in contacts}
    edges |= {frozenset((BODY, z)) for z in L - {shield}}
    return edges, shield


def find_model(edges):
    helpers = (W, X, BODY, E, F)
    for size in (6, 7):
        for used_n in combinations(sorted(N), size):
            for base in partitions(used_n, 6):
                for assignments in product(range(7), repeat=len(helpers)):
                    bags = [set(bag) for bag in base]
                    for helper, label in zip(helpers, assignments):
                        if label < 6:
                            bags[label].add(helper)
                    if not all(connected(bag, edges) for bag in bags):
                        continue
                    if all(adjacent(bags[i], bags[j], edges)
                           for i in range(6) for j in range(i)):
                        return bags
    return None


def fmt(bags):
    return " | ".join("{" + ",".join(map(str, sorted(b))) + "}" for b in bags)


def main():
    for pair in ((0, 5), (6, 0)):
        base, shield = base_edges(pair)
        print("TRIPLE", pair, "shield", shield)
        for frame in FRAMES:
            e, f = tuple(frame)
            edges = set(base)
            edges.add(frozenset((E, F)))
            edges |= {frozenset((E, z)) for z in e}
            edges |= {frozenset((F, z)) for z in f}
            model = find_model(edges)
            print(" frame", "E", sorted(e), "F", sorted(f),
                  "model", fmt(model) if model else None)


if __name__ == "__main__":
    main()
