#!/usr/bin/env python3
"""Falsification probe for the three-path bichromatic-gate branch.

The quotient has two anticomplete gate vertices, four common roots, and
one lobe behind each root.  The root graph is the matching 12,34.  For
each of the four remaining rooted-bag pairs we choose one of the four
possible root/lobe contact edges.  Gate/lobe contacts are arbitrary.

We ask whether three root-avoiding gate paths already force a K6 minor in
this smallest two-lobe skeleton.  A survivor is a counterexample to that
optimistic local statement, not to Hadwiger's conjecture.  The first
survivor has a dispensable lobe; the script also prints its nine-vertex
minimal core.
"""

from __future__ import annotations

import itertools

A, B = 0, 1
ROOTS = (2, 3, 4, 5)
LOBES = (6, 7, 8, 9)
N = 10


def k_minor_model(edges: set[tuple[int, int]], k: int = 6):
    adjacency = [0] * N
    for i, j in edges:
        adjacency[i] |= 1 << j
        adjacency[j] |= 1 << i

    neighbour_union = [0] * (1 << N)
    connected: list[int] = []
    for mask in range(1, 1 << N):
        low = mask & -mask
        i = low.bit_length() - 1
        neighbour_union[mask] = neighbour_union[mask ^ low] | adjacency[i]
        reached = low
        while True:
            expanded = reached | (neighbour_union[reached] & mask)
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            connected.append(mask)
    connected.sort(key=lambda mask: (mask.bit_count(), mask))

    def adjacent(first: int, second: int) -> bool:
        return not first & second and bool(neighbour_union[first] & second)

    def search(chosen: list[int], candidates: list[int], used: int):
        if len(chosen) == k:
            return chosen
        needed = k - len(chosen)
        if len(candidates) < needed:
            return None
        for pos, candidate in enumerate(candidates):
            if candidate & used:
                continue
            next_candidates = [
                other
                for other in candidates[pos + 1 :]
                if not other & (used | candidate)
                and adjacent(candidate, other)
            ]
            if len(next_candidates) >= needed - 1:
                answer = search(
                    chosen + [candidate], next_candidates, used | candidate
                )
                if answer is not None:
                    return answer
        return None

    return search([], connected, 0)


def root_avoiding_connectivity(edges: set[tuple[int, int]]) -> int:
    """Return the A--B local connectivity, truncated at three."""
    vertices = {A, B, *LOBES}
    adjacency = {vertex: set() for vertex in vertices}
    for x, y in edges:
        if x in vertices and y in vertices:
            adjacency[x].add(y)
            adjacency[y].add(x)

    def joined(deleted: set[int]) -> bool:
        reached = {A}
        stack = [A]
        while stack:
            x = stack.pop()
            for y in adjacency[x] - deleted - reached:
                reached.add(y)
                stack.append(y)
        return B in reached

    for size in range(3):
        for deleted in itertools.combinations(LOBES, size):
            if not joined(set(deleted)):
                return size
    return 3


def as_bags(model: list[int] | None):
    if model is None:
        return None
    return [tuple(i for i in range(N) if mask >> i & 1) for mask in model]


def main() -> None:
    fixed = set()
    for root in ROOTS:
        fixed.add(tuple(sorted((A, root))))
        fixed.add(tuple(sorted((B, root))))
    fixed.update(((2, 3), (4, 5)))
    fixed.update(tuple(sorted(pair)) for pair in zip(ROOTS, LOBES))

    cross_pairs = ((0, 2), (0, 3), (1, 2), (1, 3))
    cross_choices = []
    for i, j in cross_pairs:
        cross_choices.append(
            tuple(
                tuple(sorted((left, right)))
                for left in (ROOTS[i], LOBES[i])
                for right in (ROOTS[j], LOBES[j])
            )
        )

    tested = capacity_three = 0
    for chosen_cross in itertools.product(*cross_choices):
        for gate_mask in range(1 << 8):
            tested += 1
            edges = fixed | set(chosen_cross)
            for i, lobe in enumerate(LOBES):
                if gate_mask >> (2 * i) & 1:
                    edges.add((A, lobe))
                if gate_mask >> (2 * i + 1) & 1:
                    edges.add((B, lobe))

            if root_avoiding_connectivity(edges) < 3:
                continue
            capacity_three += 1
            model = k_minor_model(edges)
            if model is None:
                print("survivor")
                print("edges", sorted(edges))
                print("gate_mask", gate_mask)
                print("cross", chosen_cross)
                pruned = {edge for edge in edges if 6 not in edge}
                assert k_minor_model(pruned) is None
                print("nine_vertex_core_delete_6", sorted(pruned))
                return

    print("tested", tested, "capacity_three", capacity_three,
          "all contain K6")


if __name__ == "__main__":
    main()
