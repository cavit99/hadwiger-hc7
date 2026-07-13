#!/usr/bin/env python3
"""Exact test of the maximal cyclic-arc rows left by the minimal census."""

from __future__ import annotations

from unique_interface_c6_surplus_split_fast_probe import find_k7
import unique_interface_c6_surplus_split_probe as base


def edges_for(left: set[int], right: set[int], split_opposite: bool):
    edges = base.boundary_edges()
    if split_opposite:
        edges.update(((base.A, base.B), (base.P, base.Q)))
        edges.update((s, h) for s in base.S for h in (base.A, base.B))
    else:
        edges.update(((base.P, base.Q), (base.B, base.P)))
        edges.update((s, h) for s in base.S for h in (base.A, base.B))
    edges.update((s, base.P) for s in left)
    edges.update((s, base.Q) for s in right)
    return {tuple(sorted(e)) for e in edges}


def arcs(i: int, j: int):
    # Cycle labels are 1,...,6. Return the two closed i-j arcs.
    first = [i]
    cur = i
    while cur != j:
        cur = cur % 6 + 1
        first.append(cur)
    second = [i]
    cur = i
    while cur != j:
        cur = (cur - 2) % 6 + 1
        second.append(cur)
    return set(first), set(second)


def main():
    for split_opposite in (False, True):
        for j in (2, 3, 4):
            a, b = arcs(1, j)
            for swap in (False, True):
                if swap:
                    a, b = b, a
                for zcode in (1, 2, 3):
                    left, right = set(a), set(b)
                    if zcode & 1:
                        left.add(0)
                    if zcode & 2:
                        right.add(0)
                    model = find_k7(edges_for(left, right, split_opposite))
                    print("opposite" if split_opposite else "arm",
                          (1, j), "swap", swap, "z", zcode,
                          "positive", model is not None,
                          "model", model)


if __name__ == "__main__":
    main()
