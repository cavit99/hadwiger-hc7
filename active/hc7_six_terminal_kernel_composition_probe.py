#!/usr/bin/env python3
"""Test exact six-terminal irreducible kernels on the last two live masks.

The ambient quotient uses vertices ``0,...,9`` with overlap ``0,1,2`` and
seven peripheral roots ``3,...,9``.  One peripheral root is reserved.  The
other six are the prescribed terminals of a three-connected graph obtained
by deleting the reserved root.

For an order-six kernel it is enough, by monotonicity, to test every labelled
edge-minimal three-connected graph on the six roots.  For an order-seven
terminal-irreducible kernel the hand classification leaves exactly a wheel,
or a six-cycle with an opposite chord and a hub adjacent to the other four
cycle vertices and optionally either chord end.  The hub is retained as a
separate literal carrier bag.
"""

from __future__ import annotations

import functools
import itertools
import sys

sys.path.insert(0, "active")
import hc7_cross_arm_overlap_three_kernel_decoder as decoder  # noqa: E402


STATES = (
    (17061556231165, 420906820610, 36),
    (17044376361981, 438086689794, 9),
)


def pair_index(order: int):
    pairs = tuple(itertools.combinations(range(order), 2))
    return pairs, {edge: position for position, edge in enumerate(pairs)}


@functools.lru_cache(maxsize=1)
def minimal_labelled_three_connected_six_masks():
    vertices = tuple(range(6))
    pairs, index = pair_index(6)
    answer = []
    for mask in range(1 << len(pairs)):
        if mask.bit_count() < 9:
            continue
        if not decoder.is_three_connected(mask, vertices, index):
            continue
        if any(
            decoder.is_three_connected(mask ^ (1 << edge), vertices, index)
            for edge in range(len(pairs))
            if mask >> edge & 1
        ):
            continue
        answer.append(mask)
    return tuple(answer)


def cycle_edges(order):
    return tuple(
        decoder.pair(order[i], order[(i + 1) % len(order)])
        for i in range(len(order))
    )


@functools.lru_cache(maxsize=1)
def labelled_order_seven_kernel_masks():
    """Return exact masks on terminals 0..5 and nonterminal hub 6."""

    pairs, index = pair_index(7)
    masks = set()
    first = 0
    for tail in itertools.permutations(range(1, 6)):
        order = (first,) + tail
        if order[1] > order[-1]:
            continue
        rim = sum(1 << index[edge] for edge in cycle_edges(order))

        wheel = rim | sum(
            1 << index[decoder.pair(6, terminal)] for terminal in range(6)
        )
        masks.add(wheel)

        # The distinguished first cycle label need not be a chord end.  Test
        # each of the three opposite pairs; omitting this loop loses 480 of
        # the 780 labelled rooted kernels.
        for chord_index in range(3):
            chord_ends = (order[chord_index], order[chord_index + 3])
            base = rim | (1 << index[decoder.pair(*chord_ends)])
            charged = tuple(
                terminal for terminal in range(6) if terminal not in chord_ends
            )
            for optional_count in range(3):
                for optional in itertools.combinations(chord_ends, optional_count):
                    neighbours = charged + optional
                    masks.add(
                        base
                        | sum(
                            1 << index[decoder.pair(6, terminal)]
                            for terminal in neighbours
                        )
                    )
    return tuple(sorted(masks))


def lift_original_mask(mask, target_order):
    old_pairs, _ = pair_index(10)
    _, new_index = pair_index(target_order)
    return sum(
        1 << new_index[edge]
        for position, edge in enumerate(old_pairs)
        if mask >> position & 1
    )


def relabel_local_mask(mask, local_order, images, target_order):
    local_pairs, _ = pair_index(local_order)
    _, target_index = pair_index(target_order)
    return sum(
        1 << target_index[decoder.pair(images[x], images[y])]
        for position, (x, y) in enumerate(local_pairs)
        if mask >> position & 1
    )


@functools.lru_cache(maxsize=None)
def specs(order):
    return decoder.partition_specs(order, 7)


def first_failure(ones, reserved):
    terminals = tuple(vertex for vertex in range(3, 10) if vertex != reserved)

    base10 = lift_original_mask(ones, 10)
    for kernel in minimal_labelled_three_connected_six_masks():
        carrier = relabel_local_mask(kernel, 6, terminals, 10)
        if decoder.has_k_minor(base10 | carrier, specs(10)) is None:
            return "order6", kernel

    base11 = lift_original_mask(ones, 11)
    images = terminals + (10,)
    for kernel in labelled_order_seven_kernel_masks():
        carrier = relabel_local_mask(kernel, 7, images, 11)
        if decoder.has_k_minor(base11 | carrier, specs(11)) is None:
            return "order7", kernel
    return None


def main():
    order6 = minimal_labelled_three_connected_six_masks()
    order7 = labelled_order_seven_kernel_masks()
    print("order6_minimal_labelled", len(order6))
    assert len(order7) == 780
    print("order7_exact_labelled", len(order7))
    for ones, zeros, weight in STATES:
        outcomes = {}
        for reserved in range(3, 10):
            failure = first_failure(ones, reserved)
            outcomes[reserved] = failure[0] if failure else "CLOSES"
        print(
            "state",
            (ones, zeros),
            "weight",
            weight,
            "reserved_outcomes",
            outcomes,
        )


if __name__ == "__main__":
    main()
