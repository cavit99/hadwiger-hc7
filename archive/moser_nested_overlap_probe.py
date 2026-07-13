#!/usr/bin/env python3
"""Probe nested pure-Moser seven-cuts with five common boundary roots.

The old cut has boundary S=0,...,6 and two full helper shores A,B.
The nested cut replaces two old roots by portals p,q; in the three-side
case it has two inner full shores C,E.  We enumerate every labelled pure
Moser graph on (S-{u,v})+{p,q} compatible with the old induced graph and
test the minimal quotient for a K7 minor.

This is a discovery/verifier script.  A positive model is monotone under
all omitted ambient edges.
"""

from __future__ import annotations

import itertools
from functools import lru_cache


S = tuple(range(7))
P, Q, A, B, C, E = range(7, 13)
MOSER_EDGES = frozenset(
    {
        (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
        (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
    }
)
MOSER_EDGES = frozenset(tuple(sorted(edge)) for edge in MOSER_EDGES)


def relabelled_moser(target: tuple[int, ...], perm: tuple[int, ...]):
    image = dict(zip(S, perm))
    return frozenset(tuple(sorted((image[x], image[y]))) for x, y in MOSER_EDGES)


def connected_masks(adjacency: tuple[int, ...]) -> tuple[int, ...]:
    order = len(adjacency)
    out = []
    for mask in range(1, 1 << order):
        reached = mask & -mask
        while True:
            expanded = reached
            bits = reached
            while bits:
                bit = bits & -bits
                bits ^= bit
                expanded |= adjacency[bit.bit_length() - 1] & mask
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            out.append(mask)
    return tuple(out)


def k7_model(edges: frozenset[tuple[int, int]]):
    order = 13
    adjacency = [0] * order
    for x, y in edges:
        adjacency[x] |= 1 << y
        adjacency[y] |= 1 << x
    adjacency_t = tuple(adjacency)
    connected = connected_masks(adjacency_t)
    neighbours = {}
    for mask in connected:
        union = 0
        bits = mask
        while bits:
            bit = bits & -bits
            bits ^= bit
            union |= adjacency[bit.bit_length() - 1]
        neighbours[mask] = union

    # Any branch set may be shrunk to an inclusion-minimal connected set.
    # Search candidates in increasing size; order branch sets by their
    # least vertex to remove permutation symmetry.
    candidates = sorted(connected, key=lambda m: (m.bit_count(), m))

    @lru_cache(maxsize=None)
    def extend(chosen: tuple[int, ...], used: int, lower: int):
        if len(chosen) == 7:
            return chosen
        need = 7 - len(chosen)
        if order - used.bit_count() < need:
            return None
        for bag in candidates:
            low = (bag & -bag).bit_length() - 1
            if low < lower or bag & used:
                continue
            if any(not (neighbours[bag] & old) for old in chosen):
                continue
            result = extend(chosen + (bag,), used | bag, low + 1)
            if result is not None:
                return result
        return None

    return extend(tuple(), 0, 0)


def rooted_k7_model(edges: frozenset[tuple[int, int]]):
    """Search models with one old boundary root in every branch set."""
    adjacency = [0] * 13
    for x, y in edges:
        adjacency[x] |= 1 << y
        adjacency[y] |= 1 << x

    extras = (P, Q, A, B, C, E)
    bags = [1 << x for x in S]

    def connected(mask: int):
        reached = mask & -mask
        while True:
            expanded = reached
            bits = reached
            while bits:
                bit = bits & -bits
                bits ^= bit
                expanded |= adjacency[bit.bit_length() - 1] & mask
            if expanded == reached:
                return reached == mask
            reached = expanded

    def adjacent(first: int, second: int):
        bits = first
        union = 0
        while bits:
            bit = bits & -bits
            bits ^= bit
            union |= adjacency[bit.bit_length() - 1]
        return bool(union & second)

    # The value 7 leaves an extra unused.
    for assignment in itertools.product(range(8), repeat=len(extras)):
        trial = bags.copy()
        for extra, owner in zip(extras, assignment):
            if owner < 7:
                trial[owner] |= 1 << extra
        if not all(connected(bag) for bag in trial):
            continue
        if all(
            adjacent(trial[i], trial[j])
            for i in range(7)
            for j in range(i)
        ):
            return tuple(trial)
    return None


def quotient(old_omitted: tuple[int, int], nested_edges):
    old = set(MOSER_EDGES)
    old.update(nested_edges)
    old.update((A, x) for x in S)
    old.update((B, x) for x in S)
    nested = tuple(x for x in S if x not in old_omitted) + (P, Q)
    old.update((C, x) for x in nested)
    old.update((E, x) for x in nested)
    return frozenset(tuple(sorted(edge)) for edge in old)


def main():
    total = 0
    failures = []
    representatives = set()
    hard_pairs = {(1, 3), (1, 4), (2, 3), (2, 4)}
    for omitted in itertools.combinations(S, 2):
        if omitted not in hard_pairs:
            continue
        target = tuple(x for x in S if x not in omitted) + (P, Q)
        fixed_edges = {
            edge for edge in MOSER_EDGES if edge[0] in target and edge[1] in target
        }
        candidates = set()
        for perm in itertools.permutations(target):
            edges = relabelled_moser(target, perm)
            induced_old = {
                edge for edge in edges if edge[0] in S and edge[1] in S
            }
            if induced_old == fixed_edges:
                candidates.add(edges)
        for nested_edges in candidates:
            key = (omitted, nested_edges)
            if key in representatives:
                continue
            representatives.add(key)
            total += 1
            graph = quotient(omitted, nested_edges)
            model = rooted_k7_model(graph)
            if model is None:
                model = k7_model(graph)
            if model is None:
                failures.append(key)
                print("FAIL", omitted, sorted(nested_edges), flush=True)
            else:
                print("PASS", omitted, tuple(hex(x) for x in model), flush=True)
    print("compatible nested boundaries", total)
    print("failures", len(failures))


if __name__ == "__main__":
    main()
