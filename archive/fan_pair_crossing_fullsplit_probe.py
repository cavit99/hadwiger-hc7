#!/usr/bin/env python3
"""Test every ordered ordinary fan-profile pair against a full crossing split."""

from __future__ import annotations

import itertools

from reserved_terminal_specific_web_quotient_verify import e, minor_model
from wheel_safe_transition_search import ABSTRACT_TO_PHYSICAL, PRESENT_PROFILES


def main() -> None:
    moser = {e(x, y) for x, y in {
        (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
        (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
    }}
    u = {0, 2, 4, 5, 6}
    a, b, w, v, body, z1, z2, x, y, t = 1, 3, 7, 8, 9, 10, 11, 12, 13, 14
    order = (0, 2, 6, 5, 4)
    base = moser | {e(v, q) for q in range(7)} | {
        e(body, z1), e(body, z2), e(z1, z2), e(x, t), e(y, t)
    }
    forced_pairs = {
        (0, 0), (0, 1), (0, 3), (0, 4),
        (1, 0), (1, 1), (1, 2), (1, 4),
        (2, 1), (2, 2), (2, 3),
        (3, 0), (3, 2), (3, 3), (3, 4),
        (4, 0), (4, 1), (4, 3), (4, 4),
    }
    checked = 0
    for p1, p2 in sorted(forced_pairs):
        profile1, profile2 = PRESENT_PROFILES[p1], PRESENT_PROFILES[p2]
        physical1 = {ABSTRACT_TO_PHYSICAL[i] for i in profile1}
        physical2 = {ABSTRACT_TO_PHYSICAL[i] for i in profile2}
        labels1, labels2 = physical1 | {a, w}, physical2 | {a, w}
        body_labels = (u | {a, w}) - labels1 - labels2
        local = (base | {e(z1, q) for q in labels1} | {e(z2, q) for q in labels2}
                 | {e(body, q) for q in body_labels})
        for i, r, j, s in itertools.combinations(range(5), 4):
            first, second = {order[i], order[j]}, {order[r], order[s]}
            remaining = tuple((u | {b, w}) - first - second)
            for mask in range(1 << len(remaining)):
                px = first | {remaining[k] for k in range(len(remaining)) if mask >> k & 1}
                py = second | (set(remaining) - set(px))
                graph = local | {e(x, y)} | {e(x, q) for q in px} | {e(y, q) for q in py}
                checked += 1
                if minor_model(15, graph, 7) is None:
                    print("FAIL", profile1, profile2, first, second, px, py)
                    return
    print("checked", checked, "all positive")


if __name__ == "__main__":
    main()
