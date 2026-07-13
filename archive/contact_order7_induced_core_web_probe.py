#!/usr/bin/env python3
"""Probe web closure around induced C5 and induced 2K2 missing cores.

The missing graph Q is fixed on a core R.  All core--outside and
outside--outside missing edges are enumerated.  We retain only patterns for
which the quotient with two full nonadjacent helpers has no K7 minor and
test the cyclic-frame crossing quotient exactly.
"""

from __future__ import annotations

import itertools
from collections import Counter

import contact_order7_sixedge_web_probe as web


S = tuple(range(7))


def mask(edges):
    return web.base.edge_mask(tuple(tuple(sorted(e)) for e in edges))


def c5_probe():
    # Q[R] is 0-1-2-3-4-0.  Its complement is the frame below.
    core = {(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)}
    frame = (0, 2, 4, 1, 3)
    optional = tuple((x, z) for x in range(5) for z in (5, 6)) + ((5, 6),)
    quotient_failures = []
    web_failures = []
    for bits in range(1 << len(optional)):
        missing = set(core)
        missing.update(optional[i] for i in range(len(optional))
                       if bits >> i & 1)
        missing_mask = mask(missing)
        if web.quotient_model(missing_mask) is not None:
            continue
        quotient_failures.append(bits)
        j_edges = set(web.PAIRS) - {tuple(sorted(e)) for e in missing}
        witnesses = web.crossing_forces(j_edges, frame)
        if witnesses is None:
            web_failures.append(bits)
    print("C5 patterns", 1 << len(optional),
          "quotient failures", len(quotient_failures),
          "crossing failures", len(web_failures))
    print(" C5 failure edge-counts",
          Counter((bits.bit_count() + 5) for bits in web_failures))
    for bits in web_failures:
        present = tuple(optional[i] for i in range(len(optional))
                        if bits >> i & 1)
        print(" C5 FAIL extra-missing", present)


def k22_probe():
    # Q[R]=2K2 on 01 and 23; G[R] is the frame (0,2,1,3).
    core = {(0, 1), (2, 3)}
    frame = (0, 2, 1, 3)
    optional = tuple((x, z) for x in range(4) for z in (4, 5, 6))
    outside = tuple(itertools.combinations((4, 5, 6), 2))
    quotient_failures = web_failures = eligible = 0
    failure_counts = Counter()
    examples = []
    for out_bits in range(1, 1 << len(outside)):
        # At least one missing edge on Z is equivalent to G[Z] bipartite.
        out_missing = {outside[i] for i in range(len(outside))
                       if out_bits >> i & 1}
        for bits in range(1 << len(optional)):
            missing = set(core) | out_missing
            missing.update(optional[i] for i in range(len(optional))
                           if bits >> i & 1)
            eligible += 1
            missing_mask = mask(missing)
            if web.quotient_model(missing_mask) is not None:
                continue
            quotient_failures += 1
            j_edges = set(web.PAIRS) - {tuple(sorted(e)) for e in missing}
            if web.crossing_forces(j_edges, frame) is None:
                web_failures += 1
                failure_counts[len(missing)] += 1
                if len(examples) < 100:
                    examples.append(tuple(sorted(missing)))
    print("2K2 eligible", eligible,
          "quotient failures", quotient_failures,
          "crossing failures", web_failures)
    print(" 2K2 failure edge-counts", failure_counts)
    for missing in examples:
        print(" 2K2 FAIL", missing)


if __name__ == "__main__":
    c5_probe()
    k22_probe()
