#!/usr/bin/env python3
"""Exact boundary-state transitions of the order-six wheel web.

Exploratory finite-state probe.  It enumerates every exact equality
partition of the six-vertex adhesion and tests six-colour extension before
and after every internal deletion/contraction.
"""

from __future__ import annotations

import itertools

from reserved_w_majority_counterexample_verify import (
    A,
    D,
    EDGES,
    Q0,
    Q1,
    Q2,
    Q4,
    R,
    W,
    L,
    adjacent,
    edge,
)


S = (Q0, Q1, Q2, Q4, R, W)
V = tuple(sorted(D | set(S) | {A}))
INTERNAL_EDGES = sorted(e for e in EDGES if e[0] in D and e[1] in D)


def partitions(items: tuple[int, ...]):
    blocks: list[list[int]] = []

    def rec(i: int):
        if i == len(items):
            yield tuple(tuple(b) for b in blocks)
            return
        x = items[i]
        for b in blocks:
            b.append(x)
            yield from rec(i + 1)
            b.pop()
        blocks.append([x])
        yield from rec(i + 1)
        blocks.pop()

    yield from rec(0)


def independent_state(state: tuple[tuple[int, ...], ...]) -> bool:
    return all(not adjacent(x, y) for block in state for x, y in itertools.combinations(block, 2))


def extends(
    state: tuple[tuple[int, ...], ...],
    *,
    delete_vertex: int | None = None,
    delete_edge: tuple[int, int] | None = None,
    contract_edge: tuple[int, int] | None = None,
) -> bool:
    vertices = [x for x in V if x != delete_vertex]
    graph_edges = set(EDGES)
    if delete_edge is not None:
        graph_edges.discard(delete_edge)
    equal_pair = contract_edge
    if equal_pair is not None:
        graph_edges.discard(equal_pair)

    color: dict[int, int] = {}
    for c, block in enumerate(state):
        for x in block:
            color[x] = c

    if any(color.get(x) == color.get(y) for x, y in graph_edges if x in color and y in color):
        return False

    uncolored = [x for x in vertices if x not in color]

    def compatible(x: int, c: int) -> bool:
        if equal_pair is not None and x in equal_pair:
            other = equal_pair[0] if x == equal_pair[1] else equal_pair[1]
            if other in color and color[other] != c:
                return False
        return all(
            color.get(y) != c
            for y in vertices
            if y in color and edge(x, y) in graph_edges
        )

    def dfs(left: list[int]) -> bool:
        if not left:
            return equal_pair is None or color[equal_pair[0]] == color[equal_pair[1]]
        # DSATUR-style choice.
        x = max(
            left,
            key=lambda z: (
                len({color[y] for y in vertices if y in color and edge(z, y) in graph_edges}),
                sum(edge(z, y) in graph_edges for y in vertices),
            ),
        )
        rest = [z for z in left if z != x]
        if equal_pair is not None and x in equal_pair:
            other = equal_pair[0] if x == equal_pair[1] else equal_pair[1]
            choices = [color[other]] if other in color else range(6)
        else:
            choices = range(6)
        for c in choices:
            if compatible(x, c):
                color[x] = c
                if dfs(rest):
                    return True
                del color[x]
        return False

    return dfs(uncolored)


def fmt(state: tuple[tuple[int, ...], ...]) -> str:
    names = {Q0: "q0", Q1: "q1", Q2: "q2", Q4: "q4", R: "r", W: "w"}
    return "|".join("".join(names[x] for x in b) for b in state)


def main() -> None:
    states = [p for p in partitions(S) if independent_state(p)]
    base = {p for p in states if extends(p)}
    print("independent states", len(states), "base extensions", len(base))

    for e in INTERNAL_EDGES:
        deleted = {p for p in states if extends(p, delete_edge=e)} - base
        contracted = {p for p in states if extends(p, contract_edge=e)} - base
        print(
            "edge", e,
            "delete-new", len(deleted), [fmt(s) for s in sorted(deleted)[:8]],
            "contract-new", len(contracted), [fmt(s) for s in sorted(contracted)[:8]],
        )
    for x in sorted(D):
        new = {p for p in states if extends(p, delete_vertex=x)} - base
        print("vertex", x, "delete-new", len(new), [fmt(s) for s in sorted(new)[:8]])

    full_states = [
        p
        for p in partitions(tuple(sorted(L)))
        if len(p) <= 6 and independent_state(p)
    ]
    full_base = {p for p in full_states if extends(p)}
    print(
        "full seven-label boundary states", len(full_states),
        "extensions", len(full_base),
    )
    assert full_base == set(full_states)

    # In the actual reserved-connector separation the full local boundary is
    # L=S+{a}.  Audit every label-preserving operation incident with D, not
    # only the ten edges of the wheel.  Since the base family is universal,
    # no operation can create a new boundary state; contractions may delete
    # states and their exact family sizes are recorded here.
    incident_edges = sorted(e for e in EDGES if e[0] in D or e[1] in D)
    full_counts: list[tuple[str, object, int, int]] = []
    for e in incident_edges:
        deleted_family = {p for p in full_states if extends(p, delete_edge=e)}
        contracted_family = {p for p in full_states if extends(p, contract_edge=e)}
        assert not (deleted_family - full_base)
        assert not (contracted_family - full_base)
        full_counts.append(("edge-delete", e, len(deleted_family), 0))
        full_counts.append(("edge-contract", e, len(contracted_family), 0))
    for x in sorted(D):
        family = {p for p in full_states if extends(p, delete_vertex=x)}
        assert not (family - full_base)
        full_counts.append(("vertex-delete", x, len(family), 0))
    from collections import Counter
    summary = Counter((op, size) for op, _, size, _ in full_counts)
    print("full-L operation family-size summary", sorted(summary.items()))
    print(
        "full-L internal contractions",
        [(e, len({p for p in full_states if extends(p, contract_edge=e)}))
         for e in INTERNAL_EDGES],
    )


if __name__ == "__main__":
    main()
