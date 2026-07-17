#!/usr/bin/env python3
"""Exact falsifier for unrestricted seven-root kernel composition.

The host relation is the normalized arm-order-six, overlap-three cell.  The
carrier is a labelled edge-minimal three-connected graph on the seven literal
terminals.  The union has no ``K_7`` minor, as checked by the exact branch-set
enumerator shared with the positive overlap decoders.
"""

from __future__ import annotations

import itertools

import hc7_cross_arm_overlap_three_kernel_decoder as decoder


ORIGINAL_EDGES = (
    "01 02 04 05 06 08 09 12 14 15 17 18 19 23 24 25 26 27 28 29 "
    "34 35 38 39 49 58 67 68 69 79"
)
KERNEL_EDGES = "34 35 36 45 49 58 67 68 69 78 79"


def decode_edges(words: str) -> tuple[tuple[int, int], ...]:
    return tuple((int(word[0]), int(word[1])) for word in words.split())


def mask_of(edges, pair_index) -> int:
    return sum(1 << pair_index[decoder.pair(*edge)] for edge in edges)


def main() -> None:
    cell, pairs, pair_index, states = decoder.joined_states(6)
    n, a, common, x, p, q, terminals, *_ = cell
    original = mask_of(decode_edges(ORIGINAL_EDGES), pair_index)
    kernel = mask_of(decode_edges(KERNEL_EDGES), pair_index)

    matching_states = tuple((ones, zeros) for ones, zeros in states if ones == original)
    assert matching_states
    # Carrier adjacencies are edges between rooted bags.  They are added only
    # in the quotient layer and may coexist with a forced nonedge between the
    # two literal roots.
    assert decoder.common_rooted_k4(original, n, a, common, p, q) is None

    assert decoder.is_three_connected(kernel, terminals, pair_index)
    for edge in decode_edges(KERNEL_EDGES):
        assert not decoder.is_three_connected(
            kernel & ~(1 << pair_index[edge]), terminals, pair_index
        )

    specs = decoder.partition_specs(n, 7)
    assert decoder.has_k_minor(original | kernel, specs) is None

    repairs = {}
    for edge in itertools.combinations(terminals, 2):
        bit = 1 << pair_index[edge]
        if kernel & bit:
            continue
        repairs[edge] = decoder.has_k_minor(original | kernel | bit, specs) is not None

    assert {edge for edge, closes in repairs.items() if not closes} == {
        (3, 7),
        (3, 8),
        (3, 9),
    }
    print("rooted-kernel universality: falsified")
    print("joined witnesses", len(matching_states))
    print("kernel is edge-minimal three-connected")
    print("union has no K7 minor")
    print("single-edge nonrepairs", sorted(edge for edge, closes in repairs.items() if not closes))


if __name__ == "__main__":
    main()
