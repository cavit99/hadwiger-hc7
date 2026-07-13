#!/usr/bin/env python3
"""Find a uniform hub colour proving every residual wheel state extends."""

from __future__ import annotations

import itertools

from moser_safe_transition_state_probe import NONEDGES, classes, kind, matching
from wheel_safe_transition_search import (
    A,
    W,
    ABSTRACT_TO_PHYSICAL,
    PRESENT_PROFILES,
    boundary_colours,
)


def main() -> None:
    residual = [
        es for q in (2, 3) for es in itertools.combinations(NONEDGES, q)
        if matching(es) and kind(es) != "decorated-T trace"
    ]
    palette = set(range(6))
    failed = []
    for es in residual:
        for wc in range(6):
            bc = boundary_colours(es, wc)
            hub = palette - {bc[A], bc[W]}
            rim_lists = []
            for profile in PRESENT_PROFILES:
                physical = [ABSTRACT_TO_PHYSICAL[i] for i in profile]
                rim_lists.append(palette - {bc[A], bc[W], *(bc[z] for z in physical)})
            choices = [
                gamma for gamma in hub
                if all(len(ls - {gamma}) >= 2 for ls in rim_lists)
            ]
            if not choices:
                failed.append((es, wc, tuple(map(tuple, rim_lists))))
            print(es, "w", wc, "hub choices", choices)
    print("failed", len(failed))
    for row in failed:
        print("FAIL", row)


if __name__ == "__main__":
    main()
