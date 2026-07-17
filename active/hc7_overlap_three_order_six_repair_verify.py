#!/usr/bin/env python3
"""Exact repair-terminal invariant for the order-six overlap-three cell.

This checker deliberately stops before any generic ``K_7``-minor search.
It joins the nine irredundant six-support relations, removes only the
already-audited common three-rooted small-``K_4`` outcome, and inspects the
literal three-core/terminal incidences of every remaining partial state.
"""

from __future__ import annotations

import collections
import itertools

import hc7_cross_arm_overlap_three_kernel_decoder as decoder


def main() -> None:
    cell, pairs, pair_index, states = decoder.joined_states(6)
    n, a, core, _x, p, q, terminals, _supports, _literal_fives = cell

    profile = collections.Counter()
    repair_profile = collections.Counter()
    noncommon = 0

    for ones, _zeros in states:
        if decoder.common_rooted_k4(ones, n, a, core, p, q) is not None:
            continue
        noncommon += 1

        core_edges = tuple(
            edge
            for edge in itertools.combinations(core, 2)
            if ones >> pair_index[edge] & 1
        )
        good = tuple(
            terminal
            for terminal in terminals
            if all(
                ones >> pair_index[decoder.pair(i, terminal)] & 1
                for i in core
            )
        )
        profile[(len(core_edges), len(good))] += 1

        # The joined relation leaves only K3 or P3 on the three-core.
        assert len(core_edges) in (2, 3)
        if len(core_edges) == 3:
            continue

        missing = next(
            edge
            for edge in itertools.combinations(core, 2)
            if edge not in core_edges
        )
        repairs = tuple(
            terminal
            for terminal in terminals
            if terminal not in good
            and all(
                ones >> pair_index[decoder.pair(i, terminal)] & 1
                for i in missing
            )
        )
        assert repairs
        repair_profile[(len(good), len(repairs))] += 1

    assert len(states) == 60162
    assert noncommon == 7878
    assert profile == collections.Counter(
        {
            (3, 4): 2592,
            (3, 5): 336,
            (2, 3): 153,
            (2, 4): 1557,
            (2, 5): 1782,
            (2, 6): 1458,
        }
    )
    assert repair_profile == collections.Counter(
        {
            (3, 3): 144,
            (3, 4): 9,
            (4, 2): 1332,
            (4, 3): 225,
            (5, 1): 324,
            (5, 2): 1458,
            (6, 1): 1458,
        }
    )

    print("order-six overlap-three repair invariant: verified")
    print("joined=60162 noncommon=7878")
    print("(core_edges,good)", dict(sorted(profile.items())))
    print("P3 (good,repair)", dict(sorted(repair_profile.items())))


if __name__ == "__main__":
    main()
