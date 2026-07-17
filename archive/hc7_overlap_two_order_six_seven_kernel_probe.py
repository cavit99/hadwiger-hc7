#!/usr/bin/env python3
"""Probe the full seven-root kernel on one overlap-two order-six state."""

from __future__ import annotations

import functools
import itertools

import hc7_cross_arm_overlap_three_kernel_decoder as relation
import hc7_overlap_three_six_terminal_kernel_verify as kernel
import hc7_overlap_two_kernel_probe as overlap


@functools.lru_cache(maxsize=1)
def minimal_seven_terminal_carriers():
    pairs, _ = kernel.pair_data(7)
    carriers = []
    for mask in range(1 << len(pairs)):
        if mask.bit_count() < 11 or not kernel.three_connected(mask, 7, pairs):
            continue
        if any(
            kernel.three_connected(mask & ~(1 << index), 7, pairs)
            for index in range(len(pairs))
            if mask >> index & 1
        ):
            continue
        carriers.append(mask)
    return tuple(carriers)


def lift_local(mask, labels, global_index):
    pairs, _ = kernel.pair_data(len(labels))
    return sum(
        1 << global_index[relation.pair(labels[left], labels[right])]
        for index, (left, right) in enumerate(pairs)
        if mask >> index & 1
    )


def charged_cycle_carriers(labels, global_index):
    first = labels[0]
    for tail in itertools.permutations(labels[1:]):
        order = (first,) + tail
        if order[1] > order[-1]:
            continue
        cycle = sum(
            1 << global_index[
                relation.pair(order[index], order[(index + 1) % 7])
            ]
            for index in range(7)
        )
        for charged in itertools.combinations(labels, 4):
            owners = tuple(
                cycle
                | sum(
                    1 << global_index[relation.pair(owner, other)]
                    for other in charged
                    if other != owner
                )
                for owner in charged
            )
            yield order, charged, owners


def main():
    cell, pairs, pair_index, states = overlap.joined_states(6)
    n, a, common, _x, p, q, terminals, *_ = cell
    noncommon = sorted(
        state
        for state in states
        if relation.common_rooted_k4(state[0], n, a, common, p, q) is None
    )
    ones, zeros = noncommon[0]
    reserved = (p, q)
    labels = tuple(root for root in terminals if root not in reserved)
    detector = overlap.FastK7(n, pairs, pair_index)

    order7 = minimal_seven_terminal_carriers()
    first_order7_failure = next(
        (
            carrier
            for carrier in order7
            if not detector(ones | lift_local(carrier, labels, pair_index))
        ),
        None,
    )
    first_order8_failure = None
    if first_order7_failure is None:
        for order, charged, owners in charged_cycle_carriers(labels, pair_index):
            if not any(detector(ones | carrier) for carrier in owners):
                first_order8_failure = order, charged
                break

    print("joined", len(states), "noncommon", len(noncommon))
    print("minimal_order7", len(order7))
    print("fixed_reserved", reserved)
    print("order7_failure", first_order7_failure)
    print("order8_charged_cycle_failure", first_order8_failure)
    print("state", ones, zeros)


if __name__ == "__main__":
    main()
