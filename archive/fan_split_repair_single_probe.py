#!/usr/bin/env python3
"""Test the first atomic-pair quotient failure with a portal-carrying split."""

from __future__ import annotations

from reserved_terminal_specific_web_quotient_verify import e, minor_model
from wheel_safe_transition_search import ABSTRACT_TO_PHYSICAL, PRESENT_PROFILES


def main() -> None:
    moser = {e(x, y) for x, y in {
        (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
        (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
    }}
    u = {0, 2, 4, 5, 6}
    a, w, v, body, z1, z2, x, y, t = 1, 7, 8, 9, 10, 11, 12, 13, 14
    p1, p2 = PRESENT_PROFILES[0], PRESENT_PROFILES[3]  # 02,14
    q1 = {ABSTRACT_TO_PHYSICAL[i] for i in p1} | {a, w}
    q2 = {ABSTRACT_TO_PHYSICAL[i] for i in p2} | {a, w}
    body_labels = (u | {a, w}) - q1 - q2
    px, py = {0, 3, 6}, {2, 4, 5, 7}
    base = (moser | {e(v, q) for q in range(7)}
            | {e(body, z1), e(body, z2), e(z1, z2), e(x, y), e(x, t), e(y, t)}
            | {e(z1, q) for q in q1} | {e(z2, q) for q in q2}
            | {e(body, q) for q in body_labels} | {e(x, q) for q in px})
    # y retains the crossing pair 25.  Split the remaining labels 4,w.
    for tlabels in ({4}, {7}, {4, 7}):
        ylabels = py - set(tlabels)
        graph = base | {e(y, q) for q in ylabels} | {e(t, q) for q in tlabels}
        model = minor_model(15, graph, 7)
        print("tlabels", tlabels, "model", model)


if __name__ == "__main__":
    main()
