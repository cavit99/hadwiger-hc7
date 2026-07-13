#!/usr/bin/env python3
"""Adversarial version of c6_circular_witness_smt.py.

Unlike the original probe, a path joining two boundary classes may use one
shore vertex belonging to both portal sets.  Thus the two occurrences within
one demand may coincide.  The two demand pieces of a frame must remain
vertex-disjoint, so coincidences across the two pairs are forbidden.
"""

from __future__ import annotations

import itertools
import subprocess

from c6_circular_witness_smt import ORDERS, between, alternate, frame_labels, owned_base


def verify_sdr_orders() -> None:
    """Independently derive the six hard-coded SDR order types."""

    def cyclic_between(x: int, a: int, b: int) -> bool:
        return 0 < (x - a) % 6 < (b - a) % 6

    def labels_alternate(order: tuple[int, ...], labels: tuple[int, ...]) -> bool:
        position = {label: index for index, label in enumerate(order)}
        a, b, c, d = (position[label] for label in labels)
        return cyclic_between(c, a, b) != cyclic_between(d, a, b)

    derived = []
    for tail in itertools.permutations(range(1, 6)):
        order = (0, *tail)
        if all(
            labels_alternate(order, (r, (r + 1) % 6, (r + 3) % 6,
                                     (r + 4) % 6))
            for r in range(3)
        ):
            derived.append(order)
    assert sorted(derived) == sorted(ORDERS)

    # Each order facially realizes precisely one complete opposite pair.
    for order in derived:
        realized = [
            frame
            for frame in range(6)
            if not labels_alternate(order, frame_labels(frame))
        ]
        base = owned_base(order)
        assert realized == [base, base + 3]


def pairwise_disjoint_pairs(a: str, b: str, c: str, d: str) -> str:
    return f"(and (distinct {a} {c}) (distinct {a} {d}) (distinct {b} {c}) (distinct {b} {d}))"


def frame_realized(a: str, b: str, c: str, d: str, n: int) -> str:
    # A coincident pair is a singleton connected piece.  With four distinct
    # endpoints, planar disjointness is exactly nonalternation.
    return (
        f"(and {pairwise_disjoint_pairs(a,b,c,d)} "
        f"(or (= {a} {b}) (= {c} {d}) "
        f"(and (distinct {a} {b} {c} {d}) (not {alternate(a,b,c,d,n)}))))"
    )


def antipodal_forbidden(a: str, b: str, c: str, d: str, n: int) -> str:
    # Whenever the two chosen pair supports are disjoint, absence of a
    # boundary-arc linkage forces both pairs to be nondegenerate and their
    # four endpoints to alternate.
    return (
        f"(=> {pairwise_disjoint_pairs(a,b,c,d)} "
        f"(and (distinct {a} {b}) (distinct {c} {d}) "
        f"{alternate(a,b,c,d,n)}))"
    )


def formula(order: tuple[int, ...], extra: int) -> str:
    n = 14
    lines = ["(set-logic QF_LIA)"]
    occurrences: dict[int, list[str]] = {i: [f"b{i}"] for i in range(6)}
    variables = [f"b{i}" for i in range(6)]
    frame_variables: list[tuple[str, str, str, str]] = []

    for tag, frame in (("f", extra), ("g", extra + 3)):
        labels = frame_labels(frame)
        values = tuple(f"{tag}{index}" for index in range(4))
        frame_variables.append(values)  # type: ignore[arg-type]
        variables.extend(values)
        for label, value in zip(labels, values):
            occurrences[label].append(value)

    for variable in variables:
        lines.append(f"(declare-fun {variable} () Int)")
        lines.append(f"(assert (and (<= 0 {variable}) (< {variable} {n})))")

    lines.append("(assert (= b0 0))")
    ordered = [f"b{label}" for label in order]
    for first, second in zip(ordered, ordered[1:]):
        lines.append(f"(assert (< {first} {second}))")

    for values in frame_variables:
        lines.append(f"(assert {frame_realized(*values,n)})")

    for start in range(3):
        labels = (start, (start + 1) % 6, (start + 3) % 6, (start + 4) % 6)
        for values in itertools.product(*(occurrences[label] for label in labels)):
            lines.append(f"(assert {antipodal_forbidden(*values,n)})")

    lines.extend(("(check-sat)", "(get-model)"))
    return "\n".join(lines)


def main() -> None:
    verify_sdr_orders()
    checked = 0
    satisfiable = 0
    for order in ORDERS:
        base = owned_base(order)
        for extra in range(3):
            if extra == base:
                continue
            result = subprocess.run(
                ["z3", "-in"],
                input=formula(order, extra),
                text=True,
                capture_output=True,
                check=False,
            )
            checked += 1
            status = result.stdout.splitlines()[0] if result.stdout else "error"
            print(order, "base", base, "extra", extra, status)
            if status == "sat":
                satisfiable += 1
                print(result.stdout)
            elif status != "unsat":
                print(result.stdout, result.stderr)
                raise SystemExit(2)
    print("checked", checked, "satisfiable", satisfiable)


if __name__ == "__main__":
    main()
