#!/usr/bin/env python3
"""Exhaust the circular orders compatible with crossless C5 frames.

The five labels are the vertices of the missing-edge C5, written in
cyclic order 0,1,2,3,4.  Frame j consists of the two disjoint cycle
edges not incident with j:

    (j+1,j+2) and (j+3,j+4)  (indices modulo 5).

For four points on one face, crosslessness of that frame forces the
endpoints of these two pairs to alternate in the circular order.  We
fix label 0 first, enumerate all 4! oriented circular orders, and count
the frames satisfying this necessary facial-order condition.
"""

from collections import Counter
from itertools import permutations


LABELS = tuple(range(5))


def between_cyclic(order: tuple[int, ...], a: int, b: int, x: int) -> bool:
    """Return whether x lies strictly on the clockwise a-to-b arc."""
    pos = {v: i for i, v in enumerate(order)}
    n = len(order)
    dab = (pos[b] - pos[a]) % n
    dax = (pos[x] - pos[a]) % n
    return 0 < dax < dab


def pairs_alternate(
    order: tuple[int, ...], pair1: tuple[int, int], pair2: tuple[int, int]
) -> bool:
    """The endpoints of pair2 lie on opposite arcs cut by pair1."""
    a, b = pair1
    c, d = pair2
    return between_cyclic(order, a, b, c) != between_cyclic(order, a, b, d)


def frame(j: int) -> tuple[tuple[int, int], tuple[int, int]]:
    return ((j + 1) % 5, (j + 2) % 5), ((j + 3) % 5, (j + 4) % 5)


orders = [(0,) + tail for tail in permutations((1, 2, 3, 4))]
counts: Counter[int] = Counter()
strong: list[tuple[tuple[int, ...], tuple[int, ...]]] = []

for order in orders:
    good = tuple(j for j in LABELS if pairs_alternate(order, *frame(j)))
    counts[len(good)] += 1
    if len(good) >= 3:
        strong.append((order, good))

assert counts == Counter({1: 10, 2: 10, 0: 2, 5: 2}), counts
assert strong == [
    ((0, 2, 4, 1, 3), (0, 1, 2, 3, 4)),
    ((0, 3, 1, 4, 2), (0, 1, 2, 3, 4)),
], strong

print("frame-count distribution:", dict(sorted(counts.items())))
for order, good in strong:
    print("order", order, "satisfies frames", good)
