#!/usr/bin/env python3
"""Exact 12-object composition probe for the last positive-overlap cell."""

from __future__ import annotations

import functools
import itertools

import hc7_eight_terminal_exact_catalogue_probe as kernels


N = 12
PAIRS = tuple(itertools.combinations(range(N), 2))
PAIR_INDEX = {edge: index for index, edge in enumerate(PAIRS)}
ONES = 34440741661133257213
ZEROS = 39346234633704949250
assert ONES & ZEROS == 0
assert ONES | ZEROS == (1 << len(PAIRS)) - 1


class ExactK7:
    """Exact K7 detector on at most twelve quotient objects.

    A seven-bag model on twelve objects has at least two singleton bags.
    For each possible exact singleton core, all other bags are required to
    have size at least two.  This avoids the unsafe three-singleton shortcut
    valid only through order eleven.
    """

    def __init__(self):
        self.cache = {}

    def __call__(self, edges: int) -> bool:
        answer = self.cache.get(edges)
        if answer is None:
            answer = self.test(edges)
            self.cache[edges] = answer
        return answer

    @staticmethod
    def test(edges: int) -> bool:
        adjacency = [0] * N
        for index, (left, right) in enumerate(PAIRS):
            if edges >> index & 1:
                adjacency[left] |= 1 << right
                adjacency[right] |= 1 << left

        @functools.lru_cache(maxsize=None)
        def connected(mask: int) -> bool:
            reached = mask & -mask
            while True:
                old = reached
                frontier = reached
                neighbours = 0
                while frontier:
                    bit = frontier & -frontier
                    neighbours |= adjacency[bit.bit_length() - 1]
                    frontier -= bit
                reached |= neighbours & mask
                if reached == old:
                    return reached == mask

        @functools.lru_cache(maxsize=None)
        def touches(left: int, right: int) -> bool:
            frontier = left
            while frontier:
                bit = frontier & -frontier
                if adjacency[bit.bit_length() - 1] & right:
                    return True
                frontier -= bit
            return False

        full = (1 << N) - 1
        for core_size in range(7, 1, -1):
            bag_count = 7 - core_size
            for core_vertices in itertools.combinations(range(N), core_size):
                if any(
                    not (adjacency[left] >> right & 1)
                    for left, right in itertools.combinations(core_vertices, 2)
                ):
                    continue
                if bag_count == 0:
                    return True
                core = sum(1 << vertex for vertex in core_vertices)
                remainder = full ^ core
                maximum_bag_size = remainder.bit_count() - 2 * (bag_count - 1)
                candidates = []
                subset = remainder
                while subset:
                    if (
                        2 <= subset.bit_count() <= maximum_bag_size
                        and connected(subset)
                        and all(
                            touches(subset, 1 << vertex)
                            for vertex in core_vertices
                        )
                    ):
                        candidates.append(subset)
                    subset = (subset - 1) & remainder

                def search(start: int, chosen: tuple[int, ...], used: int) -> bool:
                    missing = bag_count - len(chosen)
                    if missing == 0:
                        return True
                    if (remainder & ~used).bit_count() < 2 * missing:
                        return False
                    for position in range(start, len(candidates)):
                        candidate = candidates[position]
                        if candidate & used:
                            continue
                        if all(touches(candidate, old) for old in chosen) and search(
                            position + 1, chosen + (candidate,), used | candidate
                        ):
                            return True
                    return False

                if search(0, (), 0):
                    return True
        return False


def lift(mask: int, labels: tuple[int, ...]) -> int:
    return sum(
        1 << PAIR_INDEX[tuple(sorted((labels[left], labels[right])))]
        for index, (left, right) in enumerate(kernels.PAIRS)
        if mask >> index & 1
    )


def main():
    reserve = (1, 2, 4)
    labels = tuple(vertex for vertex in range(1, 12) if vertex not in reserve)
    assert labels == (3, 5, 6, 7, 8, 9, 10, 11)
    detector = ExactK7()
    order_eight = kernels.order_eight_carriers()
    first_bad = None
    for index, carrier in enumerate(order_eight):
        if not detector(ONES | lift(carrier, labels)):
            first_bad = (index, carrier)
            break
    print("reserve", reserve)
    print("order8_tested", len(order_eight) if first_bad is None else first_bad[0] + 1)
    print("order8_first_bad", first_bad)
    print("detector_cache", len(detector.cache))

    if first_bad is not None:
        return

    order_nine_tested = 0
    first_bad_nine = None
    for rooted_index, (adjacency, extra) in enumerate(
        kernels.order_nine_unlabelled_rooted()
    ):
        terminals = tuple(vertex for vertex in range(9) if vertex != extra)
        for image in itertools.permutations(range(8)):
            family = kernels.owner_family(adjacency, extra, terminals, image)
            order_nine_tested += 1
            if not any(
                detector(ONES | lift(carrier, labels))
                for carrier in family
            ):
                first_bad_nine = (rooted_index, image, family)
                break
        if first_bad_nine is not None:
            break
    print("order9_tested", order_nine_tested)
    print("order9_first_bad", first_bad_nine)
    print("detector_cache", len(detector.cache))

    if first_bad_nine is not None:
        return

    order_ten, template_count = kernels.order_ten_families()
    first_bad_ten = None
    for index, family in enumerate(order_ten):
        if not any(
            detector(ONES | lift(carrier, labels))
            for carrier in family
        ):
            first_bad_ten = (index, family)
            break
    print("order10_templates", template_count)
    print(
        "order10_families_tested",
        len(order_ten) if first_bad_ten is None else first_bad_ten[0] + 1,
    )
    print("order10_first_bad", first_bad_ten)
    print("detector_cache", len(detector.cache))


if __name__ == "__main__":
    main()
