#!/usr/bin/env python3
"""Exhaust the static triangle-core singleton quotient.

The quotient has a singleton K4 S, a protected carrier triangle T, and
two nonadjacent shore vertices E,V.  Each shore meets at least two
vertices of T and every vertex of S.  The script checks every such portal
assignment and every possible seven-bag minor model.
"""

from __future__ import annotations

import itertools


VERTICES = ("h", "1", "2", "r", "a", "b", "c", "E", "V")
S = ("h", "1", "2", "r")
T = ("a", "b", "c")


def pair(x: str, y: str) -> tuple[str, str]:
    return tuple(sorted((x, y)))


BASE_SPOKES = {pair(x, y) for x, y in (("h", "a"), ("1", "b"), ("2", "b"), ("r", "c"))}
OPTIONAL_CROSS_EDGES = tuple(
    pair(x, y)
    for x in S
    for y in T
    if pair(x, y) not in BASE_SPOKES
)


def quotient_edges(
    a_portals: set[str],
    v_portals: set[str],
    extra_cross_edges: set[tuple[str, str]] | None = None,
):
    edges: set[tuple[str, str]] = set()
    edges.update(pair(x, y) for x, y in itertools.combinations(S, 2))
    edges.update(pair(x, y) for x, y in itertools.combinations(T, 2))
    edges.update(BASE_SPOKES)
    edges.update(extra_cross_edges or ())
    for shore, portals in (("E", a_portals), ("V", v_portals)):
        edges.update(pair(shore, s) for s in S)
        edges.update(pair(shore, t) for t in portals)
    return edges


def connected(block: tuple[str, ...], edges: set[tuple[str, str]]) -> bool:
    unseen = set(block)
    reached = {unseen.pop()}
    while unseen:
        new = {y for x in reached for y in unseen if pair(x, y) in edges}
        if not new:
            return False
        reached.update(new)
        unseen.difference_update(new)
    return True


def is_clique_model(
    blocks: tuple[tuple[str, ...], ...], edges: set[tuple[str, str]]
) -> bool:
    if not all(connected(block, edges) for block in blocks):
        return False
    return all(
        any(pair(x, y) in edges for x in left for y in right)
        for left, right in itertools.combinations(blocks, 2)
    )


def partitions_into_seven(used: tuple[str, ...]):
    blocks: list[list[str]] = []

    def generate(i: int):
        if i == len(used):
            if len(blocks) == 7:
                yield tuple(tuple(block) for block in blocks)
            return
        if len(blocks) + len(used) - i < 7:
            return
        x = used[i]
        for block in blocks:
            block.append(x)
            yield from generate(i + 1)
            block.pop()
        if len(blocks) < 7:
            blocks.append([x])
            yield from generate(i + 1)
            blocks.pop()

    yield from generate(0)


def has_k7_minor(edges: set[tuple[str, str]]) -> bool:
    for order in range(7, len(VERTICES) + 1):
        for used in itertools.combinations(VERTICES, order):
            for blocks in partitions_into_seven(used):
                if is_clique_model(blocks, edges):
                    return True
    return False


def independent(block: tuple[str, ...], edges: set[tuple[str, str]]) -> bool:
    return all(pair(x, y) not in edges for x, y in itertools.combinations(block, 2))


def canonical_four_partition(extra_cross_edges: set[tuple[str, str]]):
    """Return the guaranteed (2,2,2,1) partition for a surviving boundary."""
    centers = {
        s
        for s in ("1", "2")
        if any(s in edge for edge in extra_cross_edges)
    }
    if len(centers) > 1:
        return None
    x = next(iter(centers), "1")
    y = "2" if x == "1" else "1"
    return (("h", "c"), ("r", "b"), (y, "a"), (x,))


def main() -> None:
    portal_sets = [
        set(subset)
        for size in (2, 3)
        for subset in itertools.combinations(T, size)
    ]
    checked = 0
    for a_portals in portal_sets:
        for v_portals in portal_sets:
            edges = quotient_edges(a_portals, v_portals)
            assert not has_k7_minor(edges), (a_portals, v_portals)
            checked += 1
    print(f"verified {checked} triangle-core portal assignments: no K7 minor")

    # At the terminal of the seven-connected descent, both shores are full
    # to S union T.  Exhaust all optional cross edges between the two
    # cliques.  Exactly seven augmented boundaries avoid a quotient K7.
    survivors = []
    for mask in range(1 << len(OPTIONAL_CROSS_EDGES)):
        extras = {
            edge
            for i, edge in enumerate(OPTIONAL_CROSS_EDGES)
            if mask >> i & 1
        }
        edges = quotient_edges(set(T), set(T), extras)
        if has_k7_minor(edges):
            continue
        partition = canonical_four_partition(extras)
        assert partition is not None
        assert all(independent(block, edges) for block in partition)
        # The only permitted extras form a star of order at most two at
        # one of 1,2, and no edge is incident with h or r.
        assert not any("h" in edge or "r" in edge for edge in extras)
        assert len(extras) <= 2
        assert len({x for edge in extras for x in edge if x in {"1", "2"}}) <= 1
        survivors.append((mask, partition))
    assert len(survivors) == 7, survivors
    print("verified 256 full-shore boundary augmentations: 7 survivors")
    print("all survivors have a canonical independent (2,2,2,1) partition")


if __name__ == "__main__":
    main()
