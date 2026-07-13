#!/usr/bin/env python3
"""Single-edge repair atlas for the two degree-eight triple-lock quotients.

This is a finite quotient calculation only.  It records which absent edges
would make the contracted boundary/body/opposite-shore graph contain K6.
Positive entries are useful only when a graph-theoretic argument supplies
the corresponding contact without consuming one of the displayed bags.
"""

from itertools import combinations, product

from moser_curvature_quotient_probe import (
    BODY, L, MOSER, N, OPP, U, W, X, adjacent, connected, partitions,
)

A = 1


VERTICES = tuple(sorted(N | {W, X, BODY, OPP}))


def base_edges(pair: tuple[int, int]):
    cycle = (0, 5, 2, 4, 6)
    i = cycle.index(pair[0])
    assert cycle[(i + 1) % 5] == pair[1]
    shield = cycle[(i + 3) % 5]
    contacts = {pair[0], pair[1], shield, W, A}
    edges = set(MOSER)
    edges.add(frozenset((X, BODY)))
    edges |= {frozenset((X, z)) for z in contacts}
    edges |= {frozenset((BODY, z)) for z in L - {shield}}
    edges |= {frozenset((OPP, z)) for z in U | {W, 3}}
    return edges, shield


def find_model(edges, forbidden=frozenset()):
    for size in (6, 7):
        for used_n in combinations(sorted(N), size):
            for base in partitions(used_n, 6):
                helpers = tuple(h for h in (W, X, BODY, OPP) if h not in forbidden)
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
        edges, shield = base_edges(pair)
        print("PAIR", pair, "shield", shield, "base", find_model(edges))
        repairs = []
        failures = []
        for u, v in combinations(VERTICES, 2):
            e = frozenset((u, v))
            if e in edges:
                continue
            model = find_model(edges | {e})
            (repairs if model else failures).append((u, v, model))
        print("repairs", len(repairs))
        for u, v, model in repairs:
            print(" +", (u, v), fmt(model))
        print("failures", [(u, v) for u, v, _ in failures])
        for forced in (pair, (1, 5)):
            e = frozenset(forced)
            if e in edges:
                continue
            print(" forced", forced,
                  "drop BODY", find_model(edges | {e}, {BODY}),
                  "drop OPP", find_model(edges | {e}, {OPP}),
                  "drop both", find_model(edges | {e}, {BODY, OPP}))


if __name__ == "__main__":
    main()
