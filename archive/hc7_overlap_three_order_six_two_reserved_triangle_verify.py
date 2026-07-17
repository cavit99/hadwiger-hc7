#!/usr/bin/env python3
"""Test the two-reserved rooted-triangle composition in the order-six cell.

The three carrier bags come from the elementary rooted-triangle theorem in
the two-connected graph obtained by deleting the two reserved terminals.
Only the three carrier adjacencies are added in the final eight-object
quotient.
"""

from __future__ import annotations

import collections
import itertools
import argparse

import hc7_cross_arm_overlap_three_kernel_decoder as decoder
import hc7_overlap_three_order_six_carrier_probe as probe


def live_orbits():
    cell, pairs, pair_index, states = decoder.joined_states(6)
    n, a, core, _x, p, q, terminals, _supports, _fives = cell
    automorphisms = tuple(probe.category_automorphisms())
    representatives = {}
    weights = collections.Counter()
    for ones, zeros in states:
        if decoder.common_rooted_k4(ones, n, a, core, p, q) is not None:
            continue
        key = probe.canonical_key(
            ones, zeros, pairs, pair_index, automorphisms
        )
        representatives.setdefault(key, (ones, zeros))
        weights[key] += 1

    direct_specs = decoder.partition_specs(n, 7)
    live = tuple(
        (ones, zeros, weights[key])
        for key, (ones, zeros) in representatives.items()
        if decoder.has_k_minor(ones, direct_specs) is None
    )
    assert len(live) == 110
    assert sum(weight for _ones, _zeros, weight in live) == 6636
    return cell, pairs, live


def triangle_quotient_closes(
    ones, old_pairs, core, reserved, roots, quotient_specs
):
    selected = tuple(core) + tuple(reserved) + tuple(roots)
    assert len(selected) == 8 and len(set(selected)) == 8
    base = probe.induced_mask(ones, selected, old_pairs)
    pair_index = {
        edge: position
        for position, edge in enumerate(itertools.combinations(range(8), 2))
    }
    image = {old: new for new, old in enumerate(selected)}
    carrier = sum(
        1 << pair_index[decoder.pair(image[u], image[v])]
        for u, v in itertools.combinations(roots, 2)
    )
    return decoder.has_k_minor(
        base | carrier, quotient_specs
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--compare-f5", action="store_true")
    args = parser.parse_args()
    cell, pairs, live = live_orbits()
    _n, _a, core, _x, _p, _q, terminals, _supports, _fives = cell

    strategy_histogram = collections.Counter()
    failure_profile = collections.Counter()
    failures = []
    f5_failures = 0
    f5_failure_triangle_closed = 0
    f5_failure_records = []
    quotient_specs = decoder.partition_specs(8, 7)

    first_failure = None
    pair_index = {edge: i for i, edge in enumerate(pairs)}
    for orbit, (ones, zeros, weight) in enumerate(live):
        strategies = []
        for reserved in itertools.combinations(terminals, 2):
            available = tuple(t for t in terminals if t not in reserved)
            for roots in itertools.combinations(available, 3):
                certificate = triangle_quotient_closes(
                    ones, pairs, core, reserved, roots, quotient_specs
                )
                if certificate is not None:
                    strategies.append((reserved, roots, certificate))

        strategy_histogram[len(strategies)] += weight
        if not strategies:
            failures.append((orbit, weight))
            good = tuple(
                t
                for t in terminals
                if all(
                    ones >> pair_index[decoder.pair(i, t)] & 1
                    for i in core
                )
            )
            core_edges = tuple(
                edge
                for edge in itertools.combinations(core, 2)
                if ones >> pair_index[edge] & 1
            )
            failure_profile[(len(good), len(core_edges))] += weight
            if first_failure is None:
                first_failure = {
                    "orbit": orbit,
                    "weight": weight,
                    "good": good,
                    "ones": tuple(
                        edge
                        for i, edge in enumerate(pairs)
                        if ones >> i & 1
                    ),
                    "zeros": tuple(
                        edge
                        for i, edge in enumerate(pairs)
                        if zeros >> i & 1
                    ),
                }

        if args.compare_f5:
            f5 = probe.reserved_five_terminal_fan_strategy(
                ones, pairs, core, terminals
            )
            if f5 is None:
                f5_failures += 1
                f5_failure_records.append((orbit, weight))
                if strategies:
                    f5_failure_triangle_closed += 1

    print("two-reserved rooted-triangle composition")
    print("live_orbits=110 live_weight=6636")
    print("failure_orbits", len(failures), failures)
    print("failure_profile_weight", dict(sorted(failure_profile.items())))
    print("first_failure", first_failure)
    print("strategy_count_weight", dict(sorted(strategy_histogram.items())))
    if args.compare_f5:
        print(
            "reserved_f5_failure_orbits",
            f5_failures,
            "closed_by_triangle",
            f5_failure_triangle_closed,
        )
        print("reserved_f5_failure_records", f5_failure_records)


if __name__ == "__main__":
    main()
