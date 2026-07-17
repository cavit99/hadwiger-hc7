#!/usr/bin/env python3
"""Test the exact seven-terminal kernel catalogue on overlap-two states.

This is a falsifier for the finite composition step.  It keeps the exact
terminal chords and the full extra-vertex neighbourhood from the structural
classification.  An order-eight template passes only when at least one of
its actual neighbours can own the extra kernel vertex.
"""

from __future__ import annotations

import argparse
import itertools

import hc7_cross_arm_overlap_three_kernel_decoder as relation
import hc7_overlap_two_kernel_probe as overlap


def local_pair_data():
    pairs = tuple(itertools.combinations(range(7), 2))
    return pairs, {edge: position for position, edge in enumerate(pairs)}


def cycle_orders():
    first = 0
    for tail in itertools.permutations(range(1, 7)):
        order = (first,) + tail
        if order[1] < order[-1]:
            yield order


def mask_of(edges, index):
    answer = 0
    for left, right in edges:
        answer |= 1 << index[relation.pair(left, right)]
    return answer


def exact_order_eight_templates():
    """Return all 30,600 labelled pairs (terminal edges, x-neighbours)."""

    _pairs, index = local_pair_data()
    templates = set()
    for order in cycle_orders():
        cycle_edges = tuple(
            relation.pair(order[i], order[(i + 1) % 7]) for i in range(7)
        )
        cycle = mask_of(cycle_edges, index)

        # Wheel type.
        templates.add((cycle, (1 << 7) - 1))

        # One-chord type: choose either cyclic orientation of the distance-3
        # chord by its start position; the set removes duplicates.
        for i in range(7):
            ends = (order[i], order[(i + 3) % 7])
            terminal = cycle | mask_of((ends,), index)
            mandatory = tuple(vertex for vertex in order if vertex not in ends)
            for count in range(3):
                for optional in itertools.combinations(ends, count):
                    neighbours = sum(1 << vertex for vertex in mandatory + optional)
                    templates.add((terminal, neighbours))

        # Two-chord type: the leaves are the two distance-3 vertices from the
        # centre.  They are adjacent on C7.
        for i in range(7):
            centre = order[i]
            leaves = (order[(i - 3) % 7], order[(i + 3) % 7])
            uncharged = leaves + (centre,)
            terminal = cycle | mask_of(
                tuple((centre, leaf) for leaf in leaves), index
            )
            mandatory = tuple(vertex for vertex in order if vertex not in uncharged)
            for count in range(4):
                for optional in itertools.combinations(uncharged, count):
                    neighbours = sum(1 << vertex for vertex in mandatory + optional)
                    templates.add((terminal, neighbours))

    assert len(templates) == 30600
    return tuple(sorted(templates))


def lift(mask, labels, global_index):
    local_pairs, _index = local_pair_data()
    return sum(
        1 << global_index[relation.pair(labels[left], labels[right])]
        for position, (left, right) in enumerate(local_pairs)
        if mask >> position & 1
    )


def owner_mask(terminal_mask, neighbours, owner):
    _pairs, index = local_pair_data()
    return terminal_mask | sum(
        1 << index[relation.pair(owner, other)]
        for other in range(7)
        if other != owner and neighbours >> other & 1
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=1)
    args = parser.parse_args()

    cell, pairs, pair_index, states = overlap.joined_states(6)
    n, a, common, _x, p, q, _terminals, _supports, _literal = cell
    labels = tuple(vertex for vertex in range(n) if vertex not in common + (p, q))
    assert len(labels) == 7
    detector = overlap.FastK7(n, pairs, pair_index)
    templates = exact_order_eight_templates()
    noncommon = sorted(
        state
        for state in states
        if relation.common_rooted_k4(state[0], n, a, common, p, q) is None
    )

    failures = []
    for state_index, (ones, zeros) in enumerate(noncommon[: args.limit]):
        bad = None
        for terminal_mask, neighbours in templates:
            if not any(
                detector(
                    ones
                    | lift(
                        owner_mask(terminal_mask, neighbours, owner),
                        labels,
                        pair_index,
                    )
                )
                for owner in range(7)
                if neighbours >> owner & 1
            ):
                bad = terminal_mask, neighbours
                break
        if bad is not None:
            failures.append((state_index, ones, zeros, bad))
            print("EXACT_ORDER8_FAIL", failures[-1], flush=True)
            break
        print("EXACT_ORDER8_PASS", state_index, flush=True)

    print("templates", len(templates))
    print("tested", min(args.limit, len(noncommon)), "failures", len(failures))


if __name__ == "__main__":
    main()
