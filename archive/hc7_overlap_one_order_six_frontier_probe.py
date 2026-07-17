#!/usr/bin/env python3
"""Enumerate the normalized order-six-arm, overlap-one frontier relation.

This is a discovery probe only.  It determines the size and monotone
symmetry kernel before choosing between a four-connected carrier and an
eight-terminal contraction kernel.
"""

from __future__ import annotations

import collections
import functools
import itertools

import numpy as np

import hc7_cross_arm_overlap_three_kernel_decoder as relation


N = 12
A = tuple(range(6))
I = (0,)
X = (0, 6, 7, 8, 9)
P, Q = 10, 11
T = tuple(range(1, 12))
SUPPORTS = (
    A,
    X + (P,),
    X + (Q,),
    (1, 2, 3, 4, 5, P),
    (1, 2, 3, 4, 5, Q),
)
PAIRS = tuple(itertools.combinations(range(N), 2))
PAIR_INDEX = {edge: index for index, edge in enumerate(PAIRS)}


def patterns(support):
    local = tuple(itertools.combinations(range(6), 2))
    positions = tuple(
        PAIR_INDEX[relation.pair(support[left], support[right])]
        for left, right in local
    )
    return tuple(
        (
            sum(1 << positions[i] for i in range(15) if ones >> i & 1),
            sum(1 << positions[i] for i in range(15) if zeros >> i & 1),
        )
        for ones, zeros in relation.LOCAL_SIX
    )


def joined_states():
    constraints = tuple(patterns(support) for support in SUPPORTS)
    states = set()

    def visit(done, ones, zeros):
        if ones & zeros:
            return
        if len(done) == len(constraints):
            states.add((ones, zeros))
            return
        candidates = []
        for index, choices in enumerate(constraints):
            if index in done:
                continue
            compatible = {
                (ones | present, zeros | absent)
                for present, absent in choices
                if not (present & zeros or absent & ones)
            }
            candidates.append((len(compatible), index, compatible))
        _size, selected, compatible = min(candidates, key=lambda item: item[0])
        for new_ones, new_zeros in compatible:
            visit(done | {selected}, new_ones, new_zeros)

    visit(frozenset(), 0, 0)
    return states


def images():
    categories = ((1, 2, 3, 4, 5), (6, 7, 8, 9), (P, Q))
    for perms in itertools.product(
        *(tuple(itertools.permutations(category)) for category in categories)
    ):
        image = list(range(N))
        for category, perm in zip(categories, perms):
            for old, new in zip(category, perm):
                image[old] = new
        yield tuple(image)


def transform(mask, image):
    answer = 0
    for index, (left, right) in enumerate(PAIRS):
        if mask >> index & 1:
            answer |= 1 << PAIR_INDEX[
                relation.pair(image[left], image[right])
            ]
    return answer


def main():
    states = joined_states()
    print("joined_raw", len(states), flush=True)

    # Fast guardrail for the simplest four-connected composition route.
    # Reserve r,s; the overlap vertex 0 and r,s must be a triangle, and
    # five other exterior terminals must be complete to that triangle.
    bad_good_core = None
    good_core_profile = collections.Counter()
    for ones, zeros in states:
        witnesses = []
        for r, s in itertools.combinations(T, 2):
            core = (0, r, s)
            if any(
                not (ones >> PAIR_INDEX[relation.pair(u, v)] & 1)
                for u, v in itertools.combinations(core, 2)
            ):
                continue
            good = tuple(
                v
                for v in T
                if v not in (r, s)
                and all(
                    ones >> PAIR_INDEX[relation.pair(v, u)] & 1
                    for u in core
                )
            )
            if len(good) >= 5:
                witnesses.append((r, s, good))
        good_core_profile[len(witnesses)] += 1
        if not witnesses:
            bad_good_core = (ones, zeros)
            break
    print("good_core_first_failure", bad_good_core, flush=True)
    print("good_core_prefix_profile", dict(sorted(good_core_profile.items())), flush=True)

    common_vertices = A + (P, Q)
    common_projection = sum(
        1 << PAIR_INDEX[relation.pair(left, right)]
        for left, right in itertools.combinations(common_vertices, 2)
    )

    @functools.lru_cache(maxsize=None)
    def common_projected(projected):
        return relation.common_rooted_k4(
            projected, N, A, I, P, Q
        ) is not None

    masks = set()
    noncommon_count = 0
    for ones, _zeros in states:
        if common_projected(ones & common_projection):
            continue
        noncommon_count += 1
        masks.add(ones)
    print("common_projection_states", common_projected.cache_info().currsize, flush=True)
    print("noncommon_state_count", noncommon_count, flush=True)
    print("noncommon_mask_count", len(masks), flush=True)
    print(
        "noncommon_mask_profile",
        dict(sorted(collections.Counter(mask.bit_count() for mask in masks).items())),
        flush=True,
    )
    mask_values = sorted(masks, key=lambda value: (value.bit_count(), value))
    low = np.array(
        [mask & ((1 << 64) - 1) for mask in mask_values], dtype=np.uint64
    )
    high = np.array([mask >> 64 for mask in mask_values], dtype=np.uint64)
    weights = np.array([mask.bit_count() for mask in mask_values], dtype=np.uint8)
    covered = np.zeros(len(mask_values), dtype=bool)
    minima = []
    for weight in sorted(set(int(value) for value in weights)):
        indices = np.flatnonzero((weights == weight) & ~covered)
        if len(indices):
            print("new_minima_weight", weight, "count", len(indices), flush=True)
        for index in indices:
            mask = mask_values[int(index)]
            minima.append(mask)
            mask_low = np.uint64(mask & ((1 << 64) - 1))
            mask_high = np.uint64(mask >> 64)
            covered |= ((low & mask_low) == mask_low) & (
                (high & mask_high) == mask_high
            )

    group = tuple(images())
    live = set(minima)
    orbit_sizes = []
    while live:
        representative = min(live)
        orbit = {transform(representative, image) for image in group}
        assert orbit <= set(minima)
        orbit_sizes.append(len(orbit))
        live -= orbit

    print("joined", len(states))
    print("common", len(states) - noncommon_count)
    print("noncommon", noncommon_count)
    print("minimal_one_masks", len(minima))
    print("minimal_profile", dict(sorted(collections.Counter(mask.bit_count() for mask in minima).items())))
    print("group_order", len(group))
    print("minimal_orbits", len(orbit_sizes))
    print("orbit_size_profile", dict(sorted(collections.Counter(orbit_sizes).items())))


if __name__ == "__main__":
    main()
