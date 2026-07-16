#!/usr/bin/env python3
"""Exact seven-terminal-kernel decoder for the overlap-one order-five cell.

The normalized labels are

    A=0..5, I={0}, X={0,6,7,8}, p=9, q=10.

The arms ``X+p`` and ``X+q`` are literal K5s.  The three irredundant
six-supports are ``A``, ``(A-0)+p`` and ``(A-0)+q``.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import itertools
import time

import hc7_cross_arm_overlap_three_kernel_decoder as relation


N = 11
A = tuple(range(6))
I = (0,)
X = (0, 6, 7, 8)
P, Q = 9, 10
T = tuple(range(1, 11))
SUPPORTS = (A, (1, 2, 3, 4, 5, P), (1, 2, 3, 4, 5, Q))
LITERAL = (X + (P,), X + (Q,))
PAIRS = tuple(itertools.combinations(range(N), 2))
PAIR_INDEX = {edge: index for index, edge in enumerate(PAIRS)}


def global_patterns(support):
    local_pairs = tuple(itertools.combinations(range(6), 2))
    indices = tuple(
        PAIR_INDEX[relation.pair(support[left], support[right])]
        for left, right in local_pairs
    )
    return tuple(
        (
            sum(1 << indices[i] for i in range(15) if ones >> i & 1),
            sum(1 << indices[i] for i in range(15) if zeros >> i & 1),
        )
        for ones, zeros in relation.LOCAL_SIX
    )


def joined_states():
    constraints = tuple(global_patterns(support) for support in SUPPORTS)
    fixed = 0
    for five in LITERAL:
        for edge in itertools.combinations(five, 2):
            fixed |= 1 << PAIR_INDEX[edge]
    states = set()

    def visit(done, ones, zeros):
        if ones & zeros:
            return
        if len(done) == len(constraints):
            states.add((ones, zeros))
            return
        selected = min(
            (index for index in range(len(constraints)) if index not in done),
            key=lambda index: sum(
                not (pattern[0] & zeros or pattern[1] & ones)
                for pattern in constraints[index]
            ),
        )
        options = {
            (ones | present, zeros | absent)
            for present, absent in constraints[selected]
            if not (present & zeros or absent & ones)
        }
        for new_ones, new_zeros in options:
            visit(done | {selected}, new_ones, new_zeros)

    visit(frozenset(), fixed, 0)
    return states


def category_images():
    categories = ((1, 2, 3, 4, 5), (6, 7, 8), (P, Q))
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


def digest(values):
    return hashlib.sha256("\n".join(map(str, values)).encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test-kernel", action="store_true")
    parser.add_argument(
        "--crosscheck",
        action="store_true",
        help="crosscheck every K7 decision with the independent witness detector",
    )
    args = parser.parse_args()
    if args.crosscheck:
        args.test_kernel = True
    started = time.time()
    states = joined_states()
    noncommon = {
        (ones, zeros)
        for ones, zeros in states
        if relation.common_rooted_k4(ones, N, A, I, P, Q) is None
    }
    masks = {ones for ones, _zeros in noncommon}
    minima = []
    for mask in sorted(masks, key=lambda value: (value.bit_count(), value)):
        if not any(old & mask == old for old in minima):
            minima.append(mask)
    assert all(
        any(minimum & ones == minimum for minimum in minima)
        for ones, _zeros in noncommon
    )

    live = set(minima)
    images = tuple(category_images())
    assert len(images) == 1440
    orbit_sizes = []
    representatives = []
    orbit_sets = []
    covered = set()
    while live:
        representative = min(live)
        orbit = {transform(representative, image) for image in images}
        assert orbit <= set(minima)
        assert not (orbit & covered)
        representatives.append(representative)
        orbit_sizes.append(len(orbit))
        orbit_sets.append(orbit)
        covered |= orbit
        live -= orbit
    assert covered == set(minima)

    assert len(relation.LOCAL_SIX) == 375
    assert len(states) == 8055
    assert len(noncommon) == 5410
    assert len(minima) == 400
    assert collections.Counter(mask.bit_count() for mask in minima) == {
        29: 10,
        31: 30,
        33: 360,
    }
    assert sorted(orbit_sizes) == [10, 30, 60, 60, 120, 120]

    print("joined", len(states))
    print("common", len(states) - len(noncommon))
    print("noncommon", len(noncommon))
    print("minimal_one_masks", len(minima))
    print("minimal_profile", dict(sorted(collections.Counter(mask.bit_count() for mask in minima).items())))
    print("minimal_orbits", len(orbit_sizes))
    print("orbit_size_profile", dict(sorted(collections.Counter(orbit_sizes).items())))

    if not args.test_kernel:
        return

    from hc7_overlap_two_order_six_adaptive_kernel_probe import (
        FastK7,
        exact_order_eight_families,
        lift,
        minimal_order_seven_carriers,
    )

    detector = FastK7(N, PAIRS, PAIR_INDEX)
    audit_detector = None
    if args.crosscheck:
        from hc7_overlap_one_order_five_seven_terminal_kernel_verify import (
            WitnessK7,
        )

        audit_detector = WitnessK7()

    def has_k7(edges):
        answer = detector(edges)
        if audit_detector is not None:
            independent = audit_detector(edges)
            assert answer == (independent is not None), edges
        return answer

    order_seven = minimal_order_seven_carriers()
    order_eight = exact_order_eight_families()
    assert len(order_seven) == 5495
    assert len(order_eight) == 30600
    assert collections.Counter(mask.bit_count() for mask in order_seven) == {
        11: 5040,
        12: 455,
    }
    assert collections.Counter(map(len, order_eight)) == {
        4: 2520,
        5: 10080,
        6: 12600,
        7: 5400,
    }
    guards_seven = []
    guards_eight = []
    profile = collections.Counter()
    certificates = []

    for orbit_index, ones in enumerate(representatives):
        if has_k7(ones):
            profile["direct"] += 1
            certificates.append((orbit_index, ones, orbit_sizes[orbit_index], "direct"))
            print("ORBIT", orbit_index, "direct", flush=True)
            continue
        valid = None
        failure_kinds = collections.Counter()
        for reserved in itertools.combinations(T, 3):
            labels = tuple(vertex for vertex in T if vertex not in reserved)
            bad_seven = next(
                (
                    carrier
                    for carrier in guards_seven
                    if not has_k7(ones | lift(carrier, labels, PAIR_INDEX))
                ),
                None,
            )
            if bad_seven is None:
                bad_seven = next(
                    (
                        carrier
                        for carrier in order_seven
                        if not has_k7(ones | lift(carrier, labels, PAIR_INDEX))
                    ),
                    None,
                )
                if bad_seven is not None and bad_seven not in guards_seven:
                    guards_seven.append(bad_seven)
            if bad_seven is not None:
                failure_kinds["order7"] += 1
                continue

            def closes(family):
                return any(
                    has_k7(ones | lift(carrier, labels, PAIR_INDEX))
                    for carrier in family
                )

            bad_eight = next(
                (family for family in guards_eight if not closes(family)),
                None,
            )
            if bad_eight is None:
                bad_eight = next(
                    (family for family in order_eight if not closes(family)),
                    None,
                )
                if bad_eight is not None and bad_eight not in guards_eight:
                    guards_eight.append(bad_eight)
            if bad_eight is not None:
                failure_kinds["order8"] += 1
                continue
            valid = reserved
            break

        if valid is None:
            print("KERNEL_FAIL", orbit_index, ones, dict(failure_kinds), flush=True)
            return
        profile[valid] += 1
        certificates.append((orbit_index, ones, orbit_sizes[orbit_index], valid))
        print("ORBIT", orbit_index, "reserve", valid, flush=True)

    assert [record[3] for record in certificates] == [
        (1, 2, 9),
        (1, 2, 3),
        (1, 2, 3),
        (1, 2, 3),
        (1, 2, 3),
        (1, 2, 3),
    ]
    state_digest = digest(sorted(noncommon))
    minimum_digest = digest(sorted(minima))
    order7_digest = digest(order_seven)
    order8_digest = digest(order_eight)
    certificate_digest = digest(certificates)
    assert state_digest == "bbcd05839b15cabb5a6d7b2ef1a7e3743154be9d12d3849903a80d479369a907"
    assert minimum_digest == "1f62f3282bb2134f4e422cec810b280c059476a849d474db53f6c69129cf2343"
    assert order7_digest == "16aad7592a7f5412ab7b254434ca7f02b6454b2a8ba644d962f9f283788edec1"
    assert order8_digest == "0189701148e17b1f792e83ec1737f753c23b99dcb52c149808428602f12021e1"
    assert certificate_digest == "384761c399bd17b1c7d574801703236d3d50c8730af018e87458cbfd7511e033"
    print("kernel_closed_orbits", len(representatives))
    print("catalogues", len(order_seven), len(order_eight))
    print("guards", len(guards_seven), len(guards_eight))
    print("profile", dict(profile))
    print("state_digest", state_digest)
    print("minimum_digest", minimum_digest)
    print("order7_digest", order7_digest)
    print("order8_digest", order8_digest)
    print("certificate_digest", certificate_digest)
    if audit_detector is not None:
        print("crosschecked_masks", len(audit_detector.cache))
    print("elapsed", round(time.time() - started, 2))


if __name__ == "__main__":
    main()
