#!/usr/bin/env python3
"""Repair audit for the order-six all-crossless pentagram wheel.

Unlike the first probe, rim portal rows include the exact triple-lock
profiles allowed by the circular disk rule.  A triple lock for missing edge
i(i+1) has U-profile {i,i+1,i+3}; its shield class i+3 must occur at no
other shore vertex.  Singleton cut inequalities force a two-root row to see
both extra labels a,w, and a triple row to see at least one of them.
"""

from __future__ import annotations

import itertools

from pentagram_critical_web_probe import (
    A,
    D,
    HUB,
    U,
    W,
    cut_ok,
    linked,
    transition_report,
)


def bits(items: set[int]) -> int:
    return sum(1 << x for x in items)


PRESENT = tuple(
    frozenset(pair) for pair in itertools.combinations(U, 2)
    if (pair[1] - pair[0]) % 5 not in (1, 4)
)
TRIPLES = {
    frozenset({i, (i + 1) % 5, (i + 3) % 5}): (i + 3) % 5
    for i in U
}


def main() -> None:
    base = (1 << W) | (1 << A)
    row_types: list[tuple[int, int | None]] = []
    for pair in PRESENT:
        row_types.append((base | bits(set(pair)), None))
    for triple, shield in TRIPLES.items():
        for extras in ({W}, {A}, {W, A}):
            row_types.append((bits(set(triple) | set(extras)), shield))

    found: list[tuple[int, ...]] = []
    triple_found: list[tuple[int, ...]] = []
    examined = 0
    for choices in itertools.product(row_types, repeat=5):
        masks = tuple(mask for mask, _ in choices)
        if set().union(*(
            {j for j in U if masks[x] >> j & 1} for x in range(5)
        )) != set(U):
            continue

        # Exact singleton-shield condition for every triple row.
        valid = True
        for x, (_, shield) in enumerate(choices):
            if shield is None:
                continue
            if any(y != x and (masks[y] >> shield & 1) for y in range(5)):
                valid = False
                break
        if not valid:
            continue

        rows = masks + (base,)
        examined += 1
        if not cut_ok(rows):
            continue
        if any(linked(rows, frame) for frame in U):
            continue
        found.append(rows)
        if any(shield is not None for _, shield in choices):
            triple_found.append(rows)

    print("row types", len(row_types), "examined", examined,
          "all-crossless", len(found), "with triple lock", len(triple_found))
    assert len(row_types) == 20
    assert examined == 8895
    assert len(found) == 10
    assert not triple_found
    for rows in triple_found[:50]:
        print("triple-crossless", tuple(f"{r:07b}" for r in rows))
        transition_report(rows)
    if not triple_found:
        for rows in found:
            transition_report(rows)


if __name__ == "__main__":
    main()
