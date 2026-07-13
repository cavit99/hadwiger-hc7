#!/usr/bin/env python3
"""Test relaxed cyclic web frames in the six-missing-edge quotients.

A frame is a cyclically ordered subset R of the seven boundary vertices
such that every *actual* boundary edge with both ends in R is a frame edge.
Frame edges themselves need not be present: they may be inserted in both web
augmentations and deleted after the two disk embeddings have been glued.

For each of the twelve exceptional six-edge complement types, enumerate all
four- and five-vertex frames with a bipartite omitted set Z and test every
alternating crossing quotient for a K7 minor.
"""

from __future__ import annotations

import itertools

import contact_order7_sixedge_web_probe as web
from contact_order7_six_edge_probe import PERMS


def canonical_cycle(order):
    """Canonical representative under rotation and reversal."""
    order = tuple(order)
    variants = []
    for seq in (order, tuple(reversed(order))):
        for shift in range(len(seq)):
            variants.append(seq[shift:] + seq[:shift])
    return min(variants)


def is_frame(order, j_edges):
    frame_edges = {
        tuple(sorted((order[i], order[(i + 1) % len(order)])))
        for i in range(len(order))
    }
    induced_edges = {
        edge for edge in j_edges if edge[0] in order and edge[1] in order
    }
    return induced_edges <= frame_edges


def relaxed_frames(missing_mask):
    missing = {
        edge for i, edge in enumerate(web.PAIRS) if missing_mask >> i & 1
    }
    j_edges = set(web.PAIRS) - missing
    answer = []
    for size in (4, 5):
        for vertices in itertools.combinations(web.S, size):
            seen_orders = set()
            for order in itertools.permutations(vertices):
                order = canonical_cycle(order)
                if order in seen_orders:
                    continue
                seen_orders.add(order)
                if not is_frame(order, j_edges):
                    continue
                omitted = tuple(x for x in web.S if x not in vertices)
                if not web.bipartite(omitted, j_edges):
                    continue
                witnesses = web.crossing_forces(j_edges, order)
                if witnesses is not None:
                    answer.append((order, omitted, witnesses))
    return tuple(answer)


def candidate_frames(missing_mask):
    """All admissible frames, including those with a bad crossing."""
    missing = {
        edge for i, edge in enumerate(web.PAIRS) if missing_mask >> i & 1
    }
    j_edges = set(web.PAIRS) - missing
    answer = []
    for size in (4, 5):
        for vertices in itertools.combinations(web.S, size):
            seen_orders = set()
            for order in itertools.permutations(vertices):
                order = canonical_cycle(order)
                if order in seen_orders:
                    continue
                seen_orders.add(order)
                if not is_frame(order, j_edges):
                    continue
                omitted = tuple(x for x in web.S if x not in vertices)
                if not web.bipartite(omitted, j_edges):
                    continue
                failures = []
                for i, r, j, s in itertools.combinations(range(size), 4):
                    first = (order[i], order[j])
                    second = (order[r], order[s])
                    xpiece, ypiece, helper = 7, 8, 9
                    edges = set(j_edges)
                    edges.add((xpiece, ypiece))
                    edges.update((helper, z) for z in web.S)
                    edges.update((xpiece, z) for z in first)
                    edges.update((ypiece, z) for z in second)
                    edges = {tuple(sorted(edge)) for edge in edges}
                    model = web.generic_minor_model(10, edges)
                    if model is None:
                        failures.append((first, second))
                answer.append((order, omitted, tuple(failures)))
    return tuple(answer)


def exceptional_representatives():
    failures = []
    for missing in itertools.combinations(web.PAIRS, 6):
        mask = web.base.edge_mask(missing)
        if web.quotient_model(mask) is None:
            failures.append(mask)
    remaining = set(failures)
    reps = []
    while remaining:
        seed = min(remaining)
        orbit = {web.base.relabel(seed, p) for p in PERMS}
        reps.append(min(orbit))
        remaining -= orbit
    return tuple(sorted(reps))


def fmt_model(model):
    return tuple(tuple(i for i in range(10) if bag >> i & 1)
                 for bag in model)


def main():
    for number, mask in enumerate(exceptional_representatives(), 1):
        missing = tuple(edge for i, edge in enumerate(web.PAIRS)
                        if mask >> i & 1)
        frames = relaxed_frames(mask)
        print("TYPE", number, "missing", missing, "frames", len(frames))
        for order, omitted, witnesses in frames[:10]:
            print(" frame", order, "Z", omitted,
                  "crossings", len(witnesses))
            for first, second, model in witnesses:
                print("  cross", first, second, "bags", fmt_model(model))
        if not frames:
            for order, omitted, failures in candidate_frames(mask):
                print(" candidate", order, "Z", omitted,
                      "bad_crossings", failures)


if __name__ == "__main__":
    main()
