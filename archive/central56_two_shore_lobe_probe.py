#!/usr/bin/env python3
"""Discovery atlas for the central exact-cut two-shore lobe quotient.

One shore contains v and a connected v-lobe R containing 3,4.  The lobe
contacts all but at most one of the seven boundary roots.  The opposite
shore is full.  Optional boundary edges are precisely those incident
with the separator vertices y,z.  The output lists maximal optional-edge
masks for which this conservative quotient has no K7 model.
"""

from central56_full_shore_quotient_probe import BOUNDARY, OPTIONAL, boundary_graph
from k331_two_piece_contact_atlas import fast_k7_model


V, R, A = 7, 8, 9
ROOTS = tuple(range(7))


def edges(mask: int, defect: int | None):
    graph = boundary_graph(mask)
    result = {tuple(sorted(edge)) for edge in graph.edges()}
    result.update(tuple(sorted((V, root))) for root in (0, 1, 2, 3, 4))
    result.add((V, R))
    result.update((A, root) for root in ROOTS)
    result.update(tuple(sorted((R, root))) for root in ROOTS if root != defect)
    return result


def maximal_negative(defect: int | None):
    negative_maxima: list[int] = []
    tests = 0
    masks = sorted(range(1 << len(OPTIONAL)), key=lambda m: (-m.bit_count(), -m))
    for mask in masks:
        if any(mask & ~maximum == 0 for maximum in negative_maxima):
            continue
        tests += 1
        if fast_k7_model(edges(mask, defect)) is None:
            negative_maxima.append(mask)
    return tests, negative_maxima


def main():
    names = (None,) + BOUNDARY
    for defect_index, defect_name in enumerate(names):
        defect = None if defect_index == 0 else defect_index - 1
        tests, maxima = maximal_negative(defect)
        print("defect", defect_name, "tests", tests, "maximal_negative", len(maxima))
        for mask in maxima:
            print(" ", tuple(tuple(edge) for bit, edge in enumerate(OPTIONAL) if mask >> bit & 1))


if __name__ == "__main__":
    main()
