#!/usr/bin/env python3
"""Falsify globalization of separately rural response comparisons.

Each comparison below is individually extendable to a linear order on five
labels.  Their union is a directed triangle, so no single height order
exists.  This is a dependency-free guardrail for the quotient rewrite
theorem; it is not an HC7 counterexample.
"""

from itertools import permutations


LABELS = (1, 2, 3, 4, 5)
COMPARISONS = ((2, 3), (3, 4), (4, 2))


def extends(order: tuple[int, ...], comparisons: tuple[tuple[int, int], ...]) -> bool:
    position = {value: index for index, value in enumerate(order)}
    return all(position[left] < position[right] for left, right in comparisons)


def main() -> None:
    all_orders = tuple(permutations(LABELS))
    for comparison in COMPARISONS:
        witnesses = [order for order in all_orders if extends(order, (comparison,))]
        assert witnesses, comparison

    simultaneous = [order for order in all_orders if extends(order, COMPARISONS)]
    assert not simultaneous
    print("GREEN: local rural orders need not globalize across connectors")


if __name__ == "__main__":
    main()
