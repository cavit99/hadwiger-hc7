#!/usr/bin/env python3
"""Check residual traces against maximally portalized conservative crossings."""

from __future__ import annotations

import itertools

from moser_safe_transition_state_probe import NONEDGES, classes, kind, matching


U = {0, 2, 4, 5, 6}
ORDER = (0, 2, 6, 5, 4)


def state_colours(edges):
    out = {}
    for colour, block in enumerate(classes(edges)):
        for x in block:
            out[x] = colour
    return out


def extends(edges, crossed_terminal, opposite_terminal, first, second):
    boundary = state_colours(edges)
    palette = set(range(6))
    used_n = set(boundary.values())
    for cv in palette - used_n:  # v's colour
        for cw in palette:       # w's colour
            forbidden_h = {boundary[z] for z in U | {opposite_terminal}} | {cw}
            forbidden_x = {boundary[z] for z in set(first) | {crossed_terminal}} | {cw}
            forbidden_y = {boundary[z] for z in set(second) | {crossed_terminal}} | {cw}
            for ch in palette - forbidden_h:
                for cx in palette - forbidden_x:
                    for cy in palette - forbidden_y:
                        if cx != cy:
                            return cv, cw, ch, cx, cy
    return None


def main() -> None:
    residual = [
        es for q in (2, 3) for es in itertools.combinations(NONEDGES, q)
        if matching(es) and kind(es) != "decorated-T trace"
    ]
    failures = []
    checked = 0
    for crossed_terminal, opposite_terminal in ((1, 3), (3, 1)):
        for i, r, j, s in itertools.combinations(range(5), 4):
            first, second = (ORDER[i], ORDER[j]), (ORDER[r], ORDER[s])
            for state in residual:
                checked += 1
                if extends(state, crossed_terminal, opposite_terminal, first, second) is None:
                    failures.append((crossed_terminal, first, second, state))
    print("checked", checked, "compatible", checked - len(failures), "failures", len(failures))
    for row in failures:
        print("FAIL", row)


if __name__ == "__main__":
    main()
