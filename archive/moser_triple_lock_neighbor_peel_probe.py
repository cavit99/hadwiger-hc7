#!/usr/bin/env python3
"""Quotient test for peeling one neighbour of a degree-eight triple lock.

P is one exposed neighbour of x.  R=D-{x,P} is connected and, by the
relative order-seven inequality, contacts at least five boundary labels.
The shield is already absent from R, so R has at most one further defect.
"""

from itertools import combinations, product

from moser_curvature_quotient_probe import MOSER, N, U, W, X, L, connected, adjacent, partitions

A = 1
P, R, O = 9, 10, 11
CYCLE = (0, 5, 2, 4, 6)


def edges_for(pair, p_contacts, defect):
    i = CYCLE.index(pair[0])
    assert CYCLE[(i + 1) % 5] == pair[1]
    shield = CYCLE[(i + 3) % 5]
    x_contacts = {pair[0], pair[1], shield, W, A}
    edges = set(MOSER)
    edges |= {frozenset((X, z)) for z in x_contacts}
    edges |= {frozenset((X, P)), frozenset((X, R)), frozenset((P, R))}
    edges |= {frozenset((P, z)) for z in p_contacts}
    edges |= {frozenset((R, z)) for z in L - {shield} - set(defect)}
    edges |= {frozenset((O, z)) for z in U | {W, 3}}
    return edges, shield


def find_model(edges):
    helpers = (W, X, P, R, O)
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
    for pair, p_contacts in (((0, 5), {A}), ((6, 0), set())):
        print("PAIR", pair, "P contacts", p_contacts)
        _, shield = edges_for(pair, p_contacts, set())
        for defect in (set(), *({z} for z in L - {shield})):
            edges, _ = edges_for(pair, p_contacts, defect)
            model = find_model(edges)
            print(" defect", defect, "model", fmt(model) if model else None)


if __name__ == "__main__":
    main()
