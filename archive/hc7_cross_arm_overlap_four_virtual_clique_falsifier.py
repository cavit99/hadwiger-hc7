#!/usr/bin/env python3
"""Audit the rooted-K4 decoder with literal and virtual edges separated.

The eleven support constraints are imposed on the original graph.  Only
afterwards are the six adjacencies supplied by an exterior rooted K4 added
for the final K7 composition test.  This is a falsifier, not a proof.
"""

from __future__ import annotations

import itertools

import hc7_cross_arm_overlap_four_decoder_verify as base


def main() -> None:
    original_states = base.joined_states()
    print(f"original_states={len(original_states)}")
    for clique in itertools.combinations(base.TERMINALS, 4):
        omitted = next(vertex for vertex in base.TERMINALS if vertex not in clique)
        originals = base.relevant_complements(original_states, omitted)
        virtual_mask = sum(
            1 << base.PAIR_INDEX[pair]
            for pair in itertools.combinations(clique, 2)
        )
        common = 0
        direct = 0
        failures: list[int] = []
        for original in originals:
            if base.common_rooted_k4(original):
                common += 1
                continue
            augmented = original & ~virtual_mask
            if base.k7_avoiding(augmented, omitted):
                direct += 1
            elif len(failures) < 5:
                failures.append(original)
        print(
            f"clique={clique} omitted={omitted} originals={len(originals)} "
            f"common={common} direct={direct} failures={len(failures)}"
        )
        for complement in failures:
            missing = [
                f"{u}{v}"
                for u, v in base.ALL_PAIRS
                if complement >> base.PAIR_INDEX[(u, v)] & 1
            ]
            print("  original_non_edges=" + " ".join(missing))


if __name__ == "__main__":
    main()
