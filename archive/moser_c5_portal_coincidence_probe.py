#!/usr/bin/env python3
"""Can an all-crossless C5 portal society share one portal vertex across
the ends of a missing-cycle edge?

The encoding is deliberately relaxed.  It fixes an SDR in either possible
pentagram order, adds one occurrence z to portal classes 0 and 1, permits z
to coincide with any SDR occurrence, and imposes the exact disk rule for
all five crossless frames and every occurrence choice.  UNSAT therefore
rules out such a shared portal in every real common-face society.
"""

from __future__ import annotations

import itertools
import subprocess

from c6_circular_witness_degenerate_smt import antipodal_forbidden


ORDERS = ((0, 2, 4, 1, 3), (0, 3, 1, 4, 2))


def frame(j: int) -> tuple[int, int, int, int]:
    return ((j + 1) % 5, (j + 2) % 5,
            (j + 3) % 5, (j + 4) % 5)


def formula(order: tuple[int, ...], mask: int) -> str:
    n = 6
    lines = ["(set-logic QF_LIA)"]
    occurrences = {i: [f"b{i}"] for i in range(5)}
    for i in range(5):
        if mask & (1 << i):
            occurrences[i].append("z")
    for value in [*(f"b{i}" for i in range(5)), "z"]:
        lines.append(f"(declare-fun {value} () Int)")
        lines.append(f"(assert (and (<= 0 {value}) (< {value} {n})))")
    lines.append("(assert (= b0 0))")
    for first, second in zip(order, order[1:]):
        lines.append(f"(assert (< b{first} b{second}))")
    # The mask is the exact portal profile of the physical vertex z.  If z
    # were equal to the SDR representative of an omitted class, it would in
    # fact belong to that class as well.
    for i in range(5):
        if not (mask & (1 << i)):
            lines.append(f"(assert (distinct z b{i}))")
    for j in range(5):
        labels = frame(j)
        for values in itertools.product(*(occurrences[x] for x in labels)):
            lines.append(f"(assert {antipodal_forbidden(*values, n)})")
    lines.extend(("(check-sat)", "(get-model)"))
    return "\n".join(lines)


def main() -> None:
    feasible: set[int] = set()
    for mask in range(1, 1 << 5):
        statuses = []
        for order in ORDERS:
            result = subprocess.run(
                ["z3", "-in"], input=formula(order, mask), text=True,
                capture_output=True, check=False,
            )
            status = result.stdout.splitlines()[0] if result.stdout else "error"
            statuses.append(status)
            if status == "sat":
                feasible.add(mask)
        labels = tuple(i for i in range(5) if mask & (1 << i))
        print(labels, tuple(statuses))
    maximal = [
        mask for mask in feasible
        if not any(mask != other and mask & other == mask for other in feasible)
    ]
    print("maximal feasible profiles", [
        tuple(i for i in range(5) if mask & (1 << i)) for mask in maximal
    ])


if __name__ == "__main__":
    main()
