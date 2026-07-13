#!/usr/bin/env python3
"""Exact circular-occurrence test for three crossless Moser C5 frames.

The SDR order test only proves that three crossless frames force a
pentagram order on one representative from each portal class.  This probe
asks the stronger, occurrence-level question: can either remaining frame
nevertheless have two disjoint connected supports in the same disk?

All coincidences within one support and between a support occurrence and an
SDR occurrence are allowed.  Occurrences belonging to the two disjoint
supports are forced distinct.  For each crossless frame, the boundary-arc
obstruction is imposed for every choice of occurrences in its four portal
classes.
"""

from __future__ import annotations

import itertools
import subprocess

from c6_circular_witness_degenerate_smt import (
    antipodal_forbidden,
    frame_realized,
)


LABELS = tuple(range(5))
ORDERS = tuple((0,) + p for p in itertools.permutations((1, 2, 3, 4)))


def frame(j: int) -> tuple[int, int, int, int]:
    """Two disjoint missing-cycle edges avoiding vertex j."""

    return ((j + 1) % 5, (j + 2) % 5,
            (j + 3) % 5, (j + 4) % 5)


def cyclic_between(order: tuple[int, ...], x: int, a: int, b: int) -> bool:
    pos = {v: i for i, v in enumerate(order)}
    return 0 < (pos[x] - pos[a]) % 5 < (pos[b] - pos[a]) % 5


def alternates(order: tuple[int, ...], labels: tuple[int, int, int, int]) -> bool:
    a, b, c, d = labels
    return cyclic_between(order, c, a, b) != cyclic_between(order, d, a, b)


def formula(
    order: tuple[int, ...],
    crossless: tuple[int, int, int],
    linked: int,
) -> str:
    # Five SDR occurrences plus four support occurrences.
    n = 9
    lines = ["(set-logic QF_LIA)"]
    occurrences: dict[int, list[str]] = {i: [f"b{i}"] for i in LABELS}
    variables = [f"b{i}" for i in LABELS]

    linked_labels = frame(linked)
    support = tuple(f"x{i}" for i in range(4))
    variables.extend(support)
    for label, value in zip(linked_labels, support):
        occurrences[label].append(value)

    for value in variables:
        lines.append(f"(declare-fun {value} () Int)")
        lines.append(f"(assert (and (<= 0 {value}) (< {value} {n})))")

    lines.append("(assert (= b0 0))")
    ordered = [f"b{i}" for i in order]
    for first, second in zip(ordered, ordered[1:]):
        lines.append(f"(assert (< {first} {second}))")

    # The linked frame has two disjoint connected supports in the disk.
    lines.append(f"(assert {frame_realized(*support, n)})")

    # Every occurrence choice for each forbidden frame obeys the exact disk
    # rule, including collapses within one portal pair.
    for j in crossless:
        labels = frame(j)
        for values in itertools.product(*(occurrences[label] for label in labels)):
            lines.append(f"(assert {antipodal_forbidden(*values, n)})")

    lines.extend(("(check-sat)", "(get-model)"))
    return "\n".join(lines)


def main() -> None:
    checked = 0
    sat = 0
    for crossless in itertools.combinations(LABELS, 3):
        compatible = [
            order for order in ORDERS
            if all(alternates(order, frame(j)) for j in crossless)
        ]
        if not compatible:
            continue
        for order in compatible:
            for linked in LABELS:
                if linked in crossless:
                    continue
                result = subprocess.run(
                    ["z3", "-in"],
                    input=formula(order, crossless, linked),
                    text=True,
                    capture_output=True,
                    check=False,
                )
                checked += 1
                status = result.stdout.splitlines()[0] if result.stdout else "error"
                print(crossless, order, "linked", linked, status)
                if status == "sat":
                    sat += 1
                    print(result.stdout)
                elif status != "unsat":
                    raise RuntimeError(result.stderr or result.stdout)
    print("checked", checked, "satisfiable", sat)


if __name__ == "__main__":
    main()
