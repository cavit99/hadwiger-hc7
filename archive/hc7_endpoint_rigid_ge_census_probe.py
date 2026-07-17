#!/usr/bin/env python3
"""Falsification census for Gallai--Edmonds types under endpoint rigidity.

This reuses the exhaustive exact-star-boundary generator and minor test.
It is a research probe, not a promoted proof.  It reports the canonical
Gallai--Edmonds types among boundary graphs which satisfy endpoint rigidity,
have no perfect matching in the complement, and survive the `I_2`-join
`K_7`-minor test.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "barriers" / "hc7_star_order_eight_boundary_state_barrier_verify.py"
SPEC = importlib.util.spec_from_file_location("star_census", SOURCE)
assert SPEC and SPEC.loader
star = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(star)


def matching_number(adj: tuple[int, ...], allowed: int | None = None) -> int:
    if allowed is None:
        allowed = (1 << len(adj)) - 1

    @lru_cache(maxsize=None)
    def solve(mask: int) -> int:
        if not mask:
            return 0
        bit = mask & -mask
        v = bit.bit_length() - 1
        rest = mask ^ bit
        best = solve(rest)
        neighbours = adj[v] & rest
        while neighbours:
            w_bit = neighbours & -neighbours
            neighbours ^= w_bit
            best = max(best, 1 + solve(rest ^ w_bit))
        return best

    return solve(allowed)


def complement(adj: tuple[int, ...]) -> tuple[int, ...]:
    full = (1 << len(adj)) - 1
    return tuple((full ^ (1 << v)) & ~adj[v] for v in range(len(adj)))


def components(adj: tuple[int, ...], vertices: int) -> list[int]:
    result = []
    unseen = vertices
    while unseen:
        seed = unseen & -unseen
        reached = seed
        frontier = seed
        while frontier:
            v_bit = frontier & -frontier
            frontier ^= v_bit
            v = v_bit.bit_length() - 1
            new = adj[v] & unseen & ~reached
            reached |= new
            frontier |= new
        result.append(reached)
        unseen &= ~reached
    return result


def ge_type(boundary: tuple[int, ...]) -> tuple[int, int, tuple[int, ...], int, int, int]:
    f = complement(boundary)
    full = (1 << len(f)) - 1
    nu = matching_number(f)
    d = sum(
        1 << v
        for v in range(len(f))
        if matching_number(f, full ^ (1 << v)) == nu
    )
    neighbours = 0
    for v in range(len(f)):
        if (d >> v) & 1:
            neighbours |= f[v]
    a = neighbours & ~d
    c = full & ~(a | d)
    parts = components(f, d)
    return a.bit_count(), len(parts), tuple(sorted(p.bit_count() for p in parts)), d, a, c


def endpoint_rigid(adj: tuple[int, ...]) -> bool:
    return all(any(not ((adj[v] >> r) & 1) for r in star.R) for v in (3, 4, 5, 6))


def edge_list(adj: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple(
        (u, v)
        for u in range(len(adj))
        for v in range(u + 1, len(adj))
        if (adj[u] >> v) & 1
    )


def main() -> None:
    orbits, _ = star.candidate_orbits()
    counts: Counter[tuple[int, int]] = Counter()
    witnesses: dict[tuple[int, int], tuple[tuple[int, ...], tuple[int, ...], int, int, int]] = {}
    survivors = 0
    for code in orbits:
        j = star.adjacency(code)
        if not endpoint_rigid(j):
            continue
        if star.complement_has_perfect_matching(j):
            continue
        if star.join_i2_has_k7(j):
            continue
        a_size, q, sizes, d, a, c = ge_type(j)
        key = (a_size, q)
        counts[key] += 1
        survivors += 1
        witnesses.setdefault(key, (j, sizes, d, a, c))

    print("survivors", survivors)
    print("types", sorted(counts.items()))
    for key in sorted(witnesses):
        j, sizes, d, a, c = witnesses[key]
        print("witness", key, "D-sizes", sizes, "D", d, "A", a, "C", c)
        print("edges", edge_list(j))


if __name__ == "__main__":
    main()
