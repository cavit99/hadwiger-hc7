#!/usr/bin/env python3
"""Static falsification of an automatic surplus-interface peel.

The helper Y is a portal-2 pocket attached to F and to two different
residual carriers E4,E6.  Replacing the single Y--F edge by arbitrarily
many physical attachments does not change this quotient.  The exact search
shows that this portal-separated architecture still has no N(v)-meeting
K6 model, so attachment multiplicity alone cannot close the 05 lock.
"""

from itertools import combinations, product

from moser_curvature_quotient_probe import (
    L, MOSER, N, W, X, adjacent, connected, partitions,
)

B, F, Y, E4, E6 = 9, 10, 11, 12, 13


def main() -> None:
    edges = set(MOSER)
    for z in {0, 4, 5, W, 1}:
        edges.add(frozenset((X, z)))
    edges.add(frozenset((X, B)))
    for z in L - {4}:
        edges.add(frozenset((B, z)))

    for z in {0, 3, 5}:
        edges.add(frozenset((F, z)))
    for edge in ((F, Y), (Y, E4), (Y, E6), (Y, 2), (E4, 4), (E6, 6)):
        edges.add(frozenset(edge))

    helpers = (W, X, B, F, Y, E4, E6)
    checked = 0
    for size in (6, 7):
        for used in combinations(sorted(N), size):
            for base in partitions(used, 6):
                for assignment in product(range(7), repeat=len(helpers)):
                    checked += 1
                    bags = [set(bag) for bag in base]
                    for helper, label in zip(helpers, assignment):
                        if label < 6:
                            bags[label].add(helper)
                    if not all(connected(bag, edges) for bag in bags):
                        continue
                    if all(
                        adjacent(bags[i], bags[j], edges)
                        for i in range(6) for j in range(i)
                    ):
                        raise AssertionError(("unexpected K6 model", bags))

    assert checked == 23_059_204, checked
    print("verified portal-separated pocket assignments", checked)
    print("no N(v)-meeting K6 model")


if __name__ == "__main__":
    main()
