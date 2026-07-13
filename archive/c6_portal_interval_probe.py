#!/usr/bin/env python3
"""Allowed facial positions of one extra portal occurrence.

The six SDR representatives occupy even positions of a 12-point cyclic
refinement; odd positions represent the six open facial arcs.  For each
portal label, test every possible equality/gap position against the exact
facial-arc consequence of the three forbidden antipodal linkages.
"""

from __future__ import annotations

import itertools

from c6_circular_witness_smt import ORDERS


def between(x: int, a: int, b: int, n: int = 12) -> bool:
    return 0 < (x - a) % n < (b - a) % n


def alternate(a: int, b: int, c: int, d: int) -> bool:
    return between(c, a, b) != between(d, a, b)


def forbidden_ok(a: int, b: int, c: int, d: int) -> bool:
    # If the two selected supports are disjoint, absence of a facial-arc
    # linkage requires two noncollapsed pairs in alternating order.
    if {a, b}.isdisjoint({c, d}):
        return a != b and c != d and alternate(a, b, c, d)
    return True


def allowed(order: tuple[int, ...], label: int, candidate: int) -> bool:
    pos = {lab: 2 * index for index, lab in enumerate(order)}
    occ = {i: [pos[i]] for i in range(6)}
    occ[label].append(candidate)
    for r in range(3):
        labels = (r, (r + 1) % 6, (r + 3) % 6, (r + 4) % 6)
        for values in itertools.product(*(occ[i] for i in labels)):
            if not forbidden_ok(*values):
                return False
    return True


def main() -> None:
    for order in ORDERS:
        print("order", "".join(map(str, order)))
        for label in range(6):
            values = [p for p in range(12) if allowed(order, label, p)]
            print(label, values)


if __name__ == "__main__":
    main()
