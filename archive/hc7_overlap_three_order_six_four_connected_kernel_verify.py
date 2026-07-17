#!/usr/bin/env python3
"""Exact four-connected seven-root carrier certificate.

The script has two independent finite layers.

* It enumerates every labelled edge-minimal four-connected graph on seven
  vertices directly from the ``2^21`` possible edge sets.
* It composes each such carrier with every symmetry orbit of the surviving
  joined arm-order-six, overlap-three relation and invokes the exact
  branch-set enumerator for ``K_7``.

Only carrier edges are added in the second layer.  They are not fed back
into any irredundant-support constraint.
"""

from __future__ import annotations

import itertools

import hc7_cross_arm_overlap_three_kernel_decoder as decoder


SEVEN_PAIRS = tuple(itertools.combinations(range(7), 2))


def adjacency(mask: int) -> tuple[int, ...]:
    answer = [0] * 7
    for index, (left, right) in enumerate(SEVEN_PAIRS):
        if mask >> index & 1:
            answer[left] |= 1 << right
            answer[right] |= 1 << left
    return tuple(answer)


def connected_after_deletion(adj: tuple[int, ...], deleted: int) -> bool:
    remaining = ((1 << 7) - 1) & ~deleted
    first = remaining & -remaining
    reached = first
    while True:
        old = reached
        frontier = reached
        neighbours = 0
        while frontier:
            bit = frontier & -frontier
            neighbours |= adj[bit.bit_length() - 1]
            frontier -= bit
        reached |= neighbours & remaining
        if reached == old:
            return reached == remaining


def four_connected(mask: int) -> bool:
    adj = adjacency(mask)
    if any(neighbours.bit_count() < 4 for neighbours in adj):
        return False
    for size in range(4):
        for deleted_vertices in itertools.combinations(range(7), size):
            deleted = sum(1 << vertex for vertex in deleted_vertices)
            if not connected_after_deletion(adj, deleted):
                return False
    return True


def minimal_four_connected_carriers() -> tuple[int, ...]:
    carriers = []
    for mask in range(1 << len(SEVEN_PAIRS)):
        if mask.bit_count() < 14 or not four_connected(mask):
            continue
        if any(
            four_connected(mask & ~(1 << index))
            for index in range(len(SEVEN_PAIRS))
            if mask >> index & 1
        ):
            continue
        carriers.append(mask)
    carriers = tuple(carriers)
    assert len(carriers) == 1522
    assert {size: sum(mask.bit_count() == size for mask in carriers) for size in (14, 15)} == {
        14: 360,
        15: 1162,
    }
    return carriers


def category_automorphisms() -> tuple[tuple[int, ...], ...]:
    answer = []
    for image_i in itertools.permutations((0, 1, 2)):
        for image_a in itertools.permutations((3, 4, 5)):
            for image_x in itertools.permutations((6, 7)):
                for image_roots in itertools.permutations((8, 9)):
                    image = list(range(10))
                    image[0:3] = image_i
                    image[3:6] = image_a
                    image[6:8] = image_x
                    image[8:10] = image_roots
                    answer.append(tuple(image))
    return tuple(answer)


def transform(mask: int, image, pairs, pair_index) -> int:
    return sum(
        1 << pair_index[decoder.pair(image[left], image[right])]
        for index, (left, right) in enumerate(pairs)
        if mask >> index & 1
    )


def live_state_orbits():
    cell, pairs, pair_index, states = decoder.joined_states(6)
    n, a, common, x, p, q, terminals, *_ = cell
    automorphisms = category_automorphisms()
    representatives = {}
    weights = {}
    for ones, zeros in states:
        if decoder.common_rooted_k4(ones, n, a, common, p, q) is not None:
            continue
        key = min(
            (transform(ones, image, pairs, pair_index), transform(zeros, image, pairs, pair_index))
            for image in automorphisms
        )
        representatives.setdefault(key, (ones, zeros))
        weights[key] = weights.get(key, 0) + 1

    specs = decoder.partition_specs(n, 7)
    live = tuple(
        (ones, zeros, weights[key])
        for key, (ones, zeros) in representatives.items()
        if decoder.has_k_minor(ones, specs) is None
    )
    assert len(live) == 110
    assert sum(weight for _, _, weight in live) == 6636
    return cell, pairs, pair_index, specs, live


def lift_carrier(mask: int, terminals, pair_index) -> int:
    return sum(
        1 << pair_index[decoder.pair(terminals[left], terminals[right])]
        for index, (left, right) in enumerate(SEVEN_PAIRS)
        if mask >> index & 1
    )


def main() -> None:
    carriers = minimal_four_connected_carriers()
    cell, pairs, pair_index, specs, live = live_state_orbits()
    n, a, common, x, p, q, terminals, *_ = cell
    lifted = tuple(lift_carrier(mask, terminals, pair_index) for mask in carriers)

    tested = 0
    for ones, zeros, weight in live:
        for carrier in lifted:
            tested += 1
            assert decoder.has_k_minor(ones | carrier, specs) is not None

    assert tested == 167420
    print("four-connected seven-root carrier composition: verified")
    print("minimal labelled carriers=1522 (360 with 14 edges; 1162 with 15)")
    print("live state orbits=110; weighted states=6636")
    print("exact compositions=167420; failures=0")


if __name__ == "__main__":
    main()
