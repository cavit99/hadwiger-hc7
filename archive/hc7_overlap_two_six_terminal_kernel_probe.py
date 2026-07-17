#!/usr/bin/env python3
"""Probe the six-terminal kernel in the order-five-arm overlap-two cell.

This is an exploratory exact finite layer.  It joins the five irredundant
six-support relations and two literal five-clique arms, removes the audited
common rooted-K4 outcome, then tests every possible six-terminal kernel
after reserving two of the eight exterior roots.
"""

from __future__ import annotations

import collections
import itertools

import hc7_cross_arm_overlap_three_kernel_decoder as relation
import hc7_overlap_three_six_terminal_kernel_verify as kernel


def build_cell():
    n = 10
    a = tuple(range(6))
    overlap = (0, 1)
    x = overlap + (6, 7)
    p, q = 8, 9
    terminals = tuple(range(2, 10))
    six_supports = [a]
    for omitted in overlap:
        base = tuple(vertex for vertex in a if vertex != omitted)
        six_supports.extend((base + (p,), base + (q,)))
    literal_fives = (x + (p,), x + (q,))
    return (
        n,
        a,
        overlap,
        x,
        p,
        q,
        terminals,
        tuple(six_supports),
        literal_fives,
    )


def joined_states():
    cell = build_cell()
    n, _a, _overlap, _x, _p, _q, _terminals, supports, literal = cell
    pairs = tuple(itertools.combinations(range(n), 2))
    pair_index = {edge: position for position, edge in enumerate(pairs)}
    constraints = [relation.global_patterns(support, pair_index) for support in supports]
    fixed_ones = 0
    for clique in literal:
        for edge in itertools.combinations(clique, 2):
            fixed_ones |= 1 << pair_index[edge]
    states: set[tuple[int, int]] = set()

    def visit(done: frozenset[int], ones: int, zeros: int):
        if ones & zeros:
            return
        if len(done) == len(constraints):
            states.add((ones, zeros))
            return
        selected = -1
        options = None
        for index, patterns in enumerate(constraints):
            if index in done:
                continue
            compatible = [
                pattern
                for pattern in patterns
                if not (pattern[0] & zeros or pattern[1] & ones)
            ]
            if options is None or len(compatible) < len(options):
                selected, options = index, compatible
        assert options is not None
        seen = set()
        for pattern_ones, pattern_zeros in options:
            state = ones | pattern_ones, zeros | pattern_zeros
            if state in seen:
                continue
            seen.add(state)
            visit(done | {selected}, *state)

    visit(frozenset(), fixed_ones, 0)
    return cell, pairs, pair_index, states


def category_automorphisms():
    for pi_i in itertools.permutations((0, 1)):
        for pi_a in itertools.permutations((2, 3, 4, 5)):
            for pi_x in itertools.permutations((6, 7)):
                for pi_r in itertools.permutations((8, 9)):
                    image = list(range(10))
                    image[0:2] = pi_i
                    image[2:6] = pi_a
                    image[6:8] = pi_x
                    image[8:10] = pi_r
                    yield tuple(image)


def canonical_key(ones, zeros, pairs, pair_index, automorphisms):
    return min(
        (
            kernel.transformed_mask(ones, image, pairs, pair_index),
            kernel.transformed_mask(zeros, image, pairs, pair_index),
        )
        for image in automorphisms
    )


def main() -> None:
    cell, pairs, pair_index, states = joined_states()
    n, a, overlap, _x, p, q, terminals, *_ = cell
    automorphisms = tuple(category_automorphisms())
    assert len(automorphisms) == 192

    representatives = {}
    weights = collections.Counter()
    common_weight = 0
    for ones, zeros in states:
        if relation.common_rooted_k4(ones, n, a, overlap, p, q) is not None:
            common_weight += 1
            continue
        key = canonical_key(ones, zeros, pairs, pair_index, automorphisms)
        representatives.setdefault(key, (ones, zeros))
        weights[key] += 1

    six_carriers = kernel.minimal_six_terminal_carriers()
    seven_kernels = kernel.irreducible_seven_vertex_kernels()
    has_k7 = kernel.FastK7(pairs, pair_index)
    failures = []
    closed_weight = 0
    reserve_count_weight = collections.Counter()
    for orbit, (key, (ones, zeros)) in enumerate(representatives.items()):
        valid_reserves = []
        first_failures = {}
        for reserved in itertools.combinations(terminals, 2):
            labels = tuple(root for root in terminals if root not in reserved)
            bad = None
            for carrier in six_carriers:
                if not has_k7(
                    ones | kernel.lift_six_mask(carrier, labels, pair_index)
                ):
                    bad = ("order6", carrier)
                    break
            if bad is None:
                for terminal_mask, neighbours in seven_kernels:
                    if not any(
                        has_k7(
                            ones
                            | kernel.lift_six_mask(
                                kernel.owner_quotient(
                                    terminal_mask, neighbours, owner
                                ),
                                labels,
                                pair_index,
                            )
                        )
                        for owner in range(6)
                        if neighbours >> owner & 1
                    ):
                        bad = ("order7", terminal_mask, neighbours)
                        break
            if bad is None:
                valid_reserves.append(reserved)
            else:
                first_failures[reserved] = bad

        weight = weights[key]
        if valid_reserves:
            closed_weight += weight
            reserve_count_weight[len(valid_reserves)] += weight
        else:
            failures.append((orbit, weight, ones, zeros, first_failures))
            print("FAIL", failures[-1], flush=True)
        if (orbit + 1) % 10 == 0:
            print(
                f"tested={orbit + 1}/{len(representatives)}",
                f"failures={len(failures)}",
                flush=True,
            )

    noncommon_weight = sum(weights.values())
    print("order-five-arm overlap-two six-terminal kernel probe")
    print("joined_states", len(states))
    print("common_weight", common_weight)
    print("noncommon_orbits", len(representatives))
    print("noncommon_weight", noncommon_weight)
    print("closed_weight", closed_weight)
    print("failure_orbits", len(failures))
    print("failure_weight", noncommon_weight - closed_weight)
    print("reserve_count_weight", dict(sorted(reserve_count_weight.items())))


if __name__ == "__main__":
    main()
