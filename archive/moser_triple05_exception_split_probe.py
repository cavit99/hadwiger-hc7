#!/usr/bin/env python3
"""Refine the unique degree-eight 05 crossing exception by splitting F."""

from itertools import combinations, product

from moser_curvature_quotient_probe import MOSER, N, U, W, X, L, connected, adjacent, partitions

A = 1
B, E, F0, F5 = 9, 10, 11, 12


def find_model(edges):
    helpers = (W, X, B, E, F0, F5)
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
    edges = set(MOSER)
    # All-crossless 05 triple x and body B (shield 4).
    for z in {0, 5, 4, W, A}:
        edges.add(frozenset((X, z)))
    edges.add(frozenset((X, B)))
    for z in L - {4}:
        edges.add(frozenset((B, z)))
    # Maximal exceptional opposite carrier E.
    for z in {0, 2, 4, 5, 6, W}:
        edges.add(frozenset((E, z)))
    # Split the 05 carrier into adjacent rooted pieces, both seeing E.
    edges |= {frozenset((F0, 0)), frozenset((F5, 5)),
              frozenset((F0, F5)), frozenset((E, F0)), frozenset((E, F5))}
    for state in (1, 2, 3):
        # terminal b=3 contacts F0, F5, or both.
        trial = set(edges)
        if state & 1:
            trial.add(frozenset((F0, 3)))
        if state & 2:
            trial.add(frozenset((F5, 3)))
        model = find_model(trial)
        print("b-state", state, "model", fmt(model) if model else None, flush=True)


if __name__ == "__main__":
    main()
