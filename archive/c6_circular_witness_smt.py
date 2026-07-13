#!/usr/bin/env python3
"""Exact order-type search for the common-face C6 portal lemma.

A counterexample needs only six vertices of an SDR and eight endpoints
witnessing one additional opposite frame pair.  Coincidences between the
two frame witnesses and the SDR are allowed.  The script asks Z3 for that
14-occurrence order type while universally enforcing the three forbidden
antipodal crossings on every occurrence choice.
"""

from __future__ import annotations

import itertools
import subprocess
import sys


ORDERS = [
    (0, 2, 4, 1, 5, 3),
    (0, 2, 5, 3, 1, 4),
    (0, 3, 1, 5, 2, 4),
    (0, 3, 5, 1, 4, 2),
    (0, 4, 1, 3, 5, 2),
    (0, 4, 2, 5, 1, 3),
]


def between(x: str, a: str, b: str, n: int) -> str:
    # Strict clockwise betweenness, written without mod arithmetic.
    return (
        f"(ite (< {a} {b}) (and (< {a} {x}) (< {x} {b})) "
        f"(or (< {a} {x}) (< {x} {b})))"
    )


def alternate(a: str, b: str, c: str, d: str, n: int) -> str:
    return f"(xor {between(c, a, b, n)} {between(d, a, b, n)})"


def frame_labels(i: int) -> tuple[int, int, int, int]:
    return ((i - 2) % 6, (i - 1) % 6, (i + 2) % 6, (i + 3) % 6)


def formula(order: tuple[int, ...], extra: int, enforce_disk_degeneracy: bool = True) -> str:
    n = 14
    lines = ["(set-logic QF_LIA)"]
    occ: dict[int, list[str]] = {i: [f"b{i}"] for i in range(6)}
    variables = [f"b{i}" for i in range(6)]

    # Only the extra opposite pair needs witnesses; the SDR order itself
    # already realizes its own unique opposite frame pair.
    frame_vars: list[tuple[tuple[int, int, int, int], tuple[str, str, str, str]]] = []
    for tag, i in (("f", extra), ("g", extra + 3)):
        labels = frame_labels(i)
        vs = tuple(f"{tag}{j}" for j in range(4))
        frame_vars.append((labels, vs))  # type: ignore[arg-type]
        variables.extend(vs)
        for label, v in zip(labels, vs):
            occ[label].append(v)

    for v in variables:
        lines.append(f"(declare-fun {v} () Int)")
        lines.append(f"(assert (and (<= 0 {v}) (< {v} {n})))")

    # Normalize the cyclic order by putting the SDR representative of 0 at 0.
    lines.append("(assert (= b0 0))")
    ordered_vars = [f"b{i}" for i in order]
    for a, b in zip(ordered_vars, ordered_vars[1:]):
        lines.append(f"(assert (< {a} {b}))")

    # The two connected path pieces are disjoint, but a single piece may
    # meet both of its portal classes at the same shore vertex.  Thus only
    # cross-piece inequalities are valid.  If neither pair collapses, the
    # four occurrences must be nonalternating in a disk.
    for labels, vs in frame_vars:
        a, b, c, d = vs
        for x in (a, b):
            for y in (c, d):
                lines.append(f"(assert (not (= {x} {y})))")
        lines.append(
            f"(assert (or (= {a} {b}) (= {c} {d}) "
            f"(not {alternate(*vs, n)})))"
        )
        if enforce_disk_degeneracy:
            # With an SDR on the same face, a collapse x in two consecutive
            # portal classes is itself one path of the antipodal demand.
            # The two distinct SDR representatives of the opposite edge
            # are joined by the facial arc avoiding x, a forbidden linkage.
            lines.append(f"(assert (not (= {a} {b})))")
            lines.append(f"(assert (not (= {c} {d})))")

    # Any distinct representatives of an antipodal demand must alternate;
    # otherwise the two disjoint boundary arcs realize the forbidden frame.
    for r in range(3):
        labels = (r, (r + 1) % 6, (r + 3) % 6, (r + 4) % 6)
        for vs in itertools.product(*(occ[label] for label in labels)):
            lines.append(
                "(assert (=> (distinct " + " ".join(vs) + ") "
                + alternate(*vs, n) + "))"
            )

    lines.extend(["(check-sat)", "(get-model)"])
    return "\n".join(lines)


def owned_base(order: tuple[int, ...]) -> int:
    pos = {label: i for i, label in enumerate(order)}

    def alt(labels: tuple[int, int, int, int]) -> bool:
        a, b, c, d = map(pos.get, labels)
        assert None not in (a, b, c, d)
        bt = lambda x, u, v: 0 < ((x - u) % 6) < ((v - u) % 6)
        return bt(c, a, b) != bt(d, a, b)

    bases = [i for i in range(3) if not alt(frame_labels(i))]
    assert len(bases) == 1
    return bases[0]


def main() -> None:
    enforce_disk_degeneracy = "--raw-overlap" not in sys.argv
    checked = 0
    for order in ORDERS:
        base = owned_base(order)
        for extra in range(3):
            if extra == base:
                continue
            out = subprocess.run(
                ["z3", "-in"],
                input=formula(order, extra, enforce_disk_degeneracy), text=True,
                capture_output=True,
            )
            checked += 1
            status = out.stdout.splitlines()[0] if out.stdout else "error"
            print(order, "base", base, "extra", extra, status)
            if status == "sat":
                print(out.stdout)
                return
            if status != "unsat":
                print(out.stdout, out.stderr)
                return
    print("all", checked, "order types unsatisfiable")


if __name__ == "__main__":
    main()
