#!/usr/bin/env python3
"""Probe an atomic forced fan block against a covering opposite crossing."""

from __future__ import annotations

import itertools
import json

from reserved_terminal_specific_web_quotient_verify import e, minor_model
from wheel_safe_transition_search import ABSTRACT_TO_PHYSICAL, PRESENT_PROFILES


def main() -> None:
    moser = {
        e(x, y) for x, y in {
            (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
            (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
        }
    }
    u = {0, 2, 4, 5, 6}
    a, b, w, v, body, z1, z2, x, y = 1, 3, 7, 8, 9, 10, 11, 12, 13
    order = (0, 2, 6, 5, 4)
    base = moser | {e(v, q) for q in range(7)} | {e(body, z1), e(body, z2), e(z1, z2)}
    failures = []
    certificates = []
    checked = 0
    for profile in PRESENT_PROFILES:
        physical = {ABSTRACT_TO_PHYSICAL[i] for i in profile}
        fan_labels = physical | {a, w}
        body_labels = (u | {a, w}) - fan_labels
        local = base | {e(z, q) for z in (z1, z2) for q in fan_labels} | {
            e(body, q) for q in body_labels
        }
        for i, r, j, s in itertools.combinations(range(5), 4):
            first, second = {order[i], order[j]}, {order[r], order[s]}
            remaining = (u | {b, w}) - first - second
            for mask in range(1 << len(remaining)):
                rem = tuple(remaining)
                px = first | {rem[k] for k in range(len(rem)) if mask >> k & 1}
                py = second | (remaining - px)
                graph = local | {e(x, y)} | {e(x, q) for q in px} | {e(y, q) for q in py}
                checked += 1
                model = minor_model(14, graph, 7)
                if model is None:
                    failures.append((profile, first, second, px, py))
                    print("FAIL", failures[-1])
                    if len(failures) >= 20:
                        print("stopping after 20 failures")
                        return
                certificates.append({
                    "profile": sorted(profile),
                    "first": sorted(first),
                    "second": sorted(second),
                    "px": sorted(px),
                    "py": sorted(py),
                    "bags": [
                        [q for q in range(14) if bag >> q & 1]
                        for bag in model
                    ],
                })
    print("checked", checked, "failures", len(failures))
    with open("fan_crossing_fullsplit_certificate.json", "w", encoding="utf-8") as handle:
        json.dump(certificates, handle, indent=2)
        handle.write("\n")


if __name__ == "__main__":
    main()
