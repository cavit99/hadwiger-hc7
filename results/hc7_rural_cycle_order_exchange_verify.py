"""Finite falsifier for the cyclic-order exchange lemma."""

from __future__ import annotations

from itertools import combinations, permutations


def canonical_edges(order: tuple[int, ...]) -> set[frozenset[int]]:
    return {
        frozenset((order[index], order[(index + 1) % len(order)]))
        for index in range(len(order))
    }


def alternates(edge1: frozenset[int], edge2: frozenset[int], n: int) -> bool:
    if edge1 & edge2:
        return False
    a, b = tuple(edge1)
    c, d = tuple(edge2)
    if a > b:
        a, b = b, a
    inside_c = a < c < b
    inside_d = a < d < b
    return inside_c != inside_d


def main() -> None:
    orders = 0
    for n in range(4, 10):
        boundary = tuple(range(n))
        boundary_edges = canonical_edges(boundary)
        # Fix vertex zero first; reversal remains intentionally present.
        for tail in permutations(range(1, n)):
            order = (0,) + tail
            edges = canonical_edges(order)
            if edges == boundary_edges:
                continue
            orders += 1
            if not any(
                alternates(first, second, n)
                for first, second in combinations(edges, 2)
            ):
                raise AssertionError("non-dihedral order without crossing", n, order)
    print("GREEN:", orders, "non-dihedral cyclic orders through n=9")


if __name__ == "__main__":
    main()
