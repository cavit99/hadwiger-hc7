#!/usr/bin/env python3
"""Apply the audited sharp-core CEGIS engine to order-five/six shores."""

import itertools
import os
import sys

import sharp_core_order4_shore_sat as engine


ORDER = int(os.environ.get("SHORE_ORDER", "5"))
LOCAL = tuple(range(ORDER))
LOCAL_PAIRS = tuple(itertools.combinations(LOCAL, 2))


def connected(mask):
    adjacency = [set() for _ in LOCAL]
    for index, (a, b) in enumerate(LOCAL_PAIRS):
        if mask >> index & 1:
            adjacency[a].add(b)
            adjacency[b].add(a)
    reached = {0}
    while True:
        expanded = reached | {y for x in reached for y in adjacency[x]}
        if expanded == reached:
            return len(reached) == len(LOCAL)
        reached = expanded


def relabel(mask, permutation):
    edge_index = {edge: i for i, edge in enumerate(LOCAL_PAIRS)}
    answer = 0
    for index, (a, b) in enumerate(LOCAL_PAIRS):
        if mask >> index & 1:
            x, y = sorted((permutation[a], permutation[b]))
            answer |= 1 << edge_index[(x, y)]
    return answer


def canonical(mask):
    return min(relabel(mask, permutation)
               for permutation in itertools.permutations(LOCAL))


def representatives():
    direct = os.environ.get("DIRECT_MASK")
    if direct:
        mask = int(direct.removeprefix("m"), 16)
        assert connected(mask)
        edges = tuple(
            (7 + a, 7 + b) for index, (a, b) in enumerate(LOCAL_PAIRS)
            if mask >> index & 1
        )
        return {f"m{mask:03x}": edges}
    reps = sorted({canonical(mask) for mask in range(1 << len(LOCAL_PAIRS))
                   if connected(mask)}, key=lambda mask: (mask.bit_count(), mask))
    expected = {5: 21, 6: 112}[ORDER]
    assert len(reps) == expected
    answer = {}
    for mask in reps:
        edges = tuple(
            (7 + a, 7 + b) for index, (a, b) in enumerate(LOCAL_PAIRS)
            if mask >> index & 1
        )
        answer[f"m{mask:03x}"] = edges
    return answer


def configure():
    engine.D = tuple(range(7, 7 + ORDER))
    engine.H = 7 + ORDER
    engine.V = tuple(range(8 + ORDER))
    engine.VARIABLE = tuple((s, d) for d in engine.D for s in engine.S)
    engine.INTERNAL_TYPES = representatives()


def main():
    configure()
    selected_core = sys.argv[1] if len(sys.argv) > 1 else None
    selected_internal = sys.argv[2] if len(sys.argv) > 2 else None
    cores = (selected_core,) if selected_core else ("C5+2K1", "K3+2K2")
    names = ((selected_internal,) if selected_internal
             else tuple(engine.INTERNAL_TYPES))
    print("connected shore types", ORDER, len(engine.INTERNAL_TYPES), flush=True)
    if os.environ.get("LIST_ONLY"):
        print(" ".join(engine.INTERNAL_TYPES))
        return
    for core_kind in cores:
        for name in names:
            result = engine.solve(core_kind, name, limit=200000)
            print(core_kind, name, len(engine.INTERNAL_TYPES[name]), result,
                  flush=True)


if __name__ == "__main__":
    main()
