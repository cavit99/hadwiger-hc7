#!/usr/bin/env python3
"""Falsify composition of the overlap-four cell with a terminal cycle.

The eleven support constraints are imposed on the original nine labels.
For each cyclic order of the five exterior terminals, the five cycle
edges are then added as virtual edges.  Such a graph is a minor of any
host containing a cycle through the terminals.  The script tests whether
the augmented graph always has a K7 minor or the original graph already
has the audited common three-rooted K4.  It is a finite experiment, not a
proof.
"""

from __future__ import annotations

import itertools

import hc7_cross_arm_overlap_four_decoder_verify as base


def full_complements() -> set[int]:
    states = base.joined_states()
    all_mask = (1 << len(base.ALL_PAIRS)) - 1
    answers: set[int] = set()
    for ones, zeros in states:
        unknown = all_mask & ~(ones | zeros)
        bits = [1 << i for i in range(len(base.ALL_PAIRS)) if unknown >> i & 1]
        for choices in range(1 << len(bits)):
            extra = sum(bit for i, bit in enumerate(bits) if choices >> i & 1)
            answers.add(ones | extra)
    return answers


def has_k7(complement: int) -> bool:
    vertices = tuple(range(base.N))
    for support_size in (7, 8, 9):
        for support in itertools.combinations(vertices, support_size):
            for bags in base.partitions(support, 7):
                if all(base.connected(complement, bag) for bag in bags) and all(
                    base.touch(complement, left, right)
                    for left, right in itertools.combinations(bags, 2)
                ):
                    return True
    return False


def cyclic_orders() -> tuple[tuple[int, ...], ...]:
    first = base.TERMINALS[0]
    orders = []
    for tail in itertools.permutations(base.TERMINALS[1:]):
        order = (first,) + tail
        if order[1] < order[-1]:
            orders.append(order)
    return tuple(orders)


def main() -> None:
    originals = full_complements()
    unresolved = [c for c in originals if not base.common_rooted_k4(c)]
    print(f"originals={len(originals)} unresolved_before_cycle={len(unresolved)}")
    for order in cyclic_orders():
        cycle_pairs = {
            base.pair(order[i], order[(i + 1) % len(order)])
            for i in range(len(order))
        }
        virtual_mask = sum(1 << base.PAIR_INDEX[pair] for pair in cycle_pairs)
        failures = []
        for original in unresolved:
            augmented = original & ~virtual_mask
            if not has_k7(augmented):
                failures.append(original)
                if len(failures) == 3:
                    break
        print(f"order={order} failures={len(failures)}")
        for complement in failures:
            missing = [
                f"{u}{v}"
                for u, v in base.ALL_PAIRS
                if complement >> base.PAIR_INDEX[(u, v)] & 1
            ]
            print("  original_non_edges=" + " ".join(missing))


if __name__ == "__main__":
    main()
