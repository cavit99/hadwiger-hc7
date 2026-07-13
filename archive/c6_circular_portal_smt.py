#!/usr/bin/env python3
"""Search circular portal-incidence systems with an SDR but incoherent frames.

This is a finite combinatorial probe.  Positions are vertices in cyclic order;
``x[p,i]`` says that position ``p`` is a portal for boundary label ``i``.
We impose an SDR, forbid every boundary-realizable antipodal two-linkage, and
ask two opposite frame pairs to be boundary-realizable (possibly using
different representatives).  A satisfying assignment is a warning that Hall
alone does not synchronize representatives.
"""

from __future__ import annotations

import argparse
import itertools
import subprocess


def alternate(n: int, a: int, b: int, c: int, d: int) -> bool:
    """Whether chords ab and cd alternate in the cyclic order 0,...,n-1."""
    between = lambda x, u, v: 0 < ((x - u) % n) < ((v - u) % n)
    return between(c, a, b) != between(d, a, b)


def selections(n: int, pair1: tuple[int, int], pair2: tuple[int, int]):
    """Incidence literals for distinct, nonalternating endpoint choices."""
    a, b = pair1
    c, d = pair2
    for pa, pb, pc, pd in itertools.permutations(range(n), 4):
        if not alternate(n, pa, pb, pc, pd):
            yield (f"x_{pa}_{a}", f"x_{pb}_{b}", f"x_{pc}_{c}", f"x_{pd}_{d}")


def or_of_ands(terms: list[tuple[str, ...]]) -> str:
    return "(or " + " ".join("(and " + " ".join(t) + ")" for t in terms) + ")"


def build(
    n: int,
    owned_pair_indices: tuple[int, int],
    fixed_matching: dict[int, int] | None = None,
) -> str:
    lines = ["(set-logic QF_UF)"]
    for p in range(n):
        for i in range(6):
            lines.append(f"(declare-fun x_{p}_{i} () Bool)")
    if fixed_matching is None:
        for i in range(6):
            for p in range(n):
                lines.append(f"(declare-fun y_{i}_{p} () Bool)")

        # A system of distinct representatives.
        for i in range(6):
            ys = [f"y_{i}_{p}" for p in range(n)]
            lines.append("(assert (or " + " ".join(ys) + "))")
            for p, q in itertools.combinations(range(n), 2):
                lines.append(f"(assert (not (and y_{i}_{p} y_{i}_{q})))")
            for p in range(n):
                lines.append(f"(assert (=> y_{i}_{p} x_{p}_{i}))")
        for p in range(n):
            for i, j in itertools.combinations(range(6), 2):
                lines.append(f"(assert (not (and y_{i}_{p} y_{j}_{p})))")
    else:
        for i, p in fixed_matching.items():
            lines.append(f"(assert x_{p}_{i})")

    # No boundary-realizable linkage for antipodal missing-cycle edges.
    for r in range(3):
        p1 = (r, (r + 1) % 6)
        p2 = ((r + 3) % 6, (r + 4) % 6)
        for term in selections(n, p1, p2):
            lines.append("(assert (not (and " + " ".join(term) + ")))" )

    # Each selected opposite pair means frames i and i+3 are both owned.
    for base in owned_pair_indices:
        for i in (base, base + 3):
            p1 = ((i - 2) % 6, (i - 1) % 6)
            p2 = ((i + 2) % 6, (i + 3) % 6)
            lines.append("(assert " + or_of_ands(list(selections(n, p1, p2))) + ")")

    lines.extend(["(check-sat)", "(get-model)"])
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int)
    ap.add_argument("--pairs", default="0,1")
    ap.add_argument("--fixed-enumeration", action="store_true")
    args = ap.parse_args()
    pairs = tuple(map(int, args.pairs.split(",")))
    if not args.fixed_enumeration:
        text = build(args.n, pairs)  # type: ignore[arg-type]
        out = subprocess.run(["z3", "-in"], input=text, text=True, capture_output=True)
        print(out.stdout)
        if out.stderr:
            print(out.stderr)
        return

    valid_orders = [
        (0, 2, 4, 1, 5, 3),
        (0, 2, 5, 3, 1, 4),
        (0, 3, 1, 5, 2, 4),
        (0, 3, 5, 1, 4, 2),
        (0, 4, 1, 3, 5, 2),
        (0, 4, 2, 5, 1, 3),
    ]
    checked = 0
    for order in valid_orders:
        for rest in itertools.combinations(range(1, args.n), 5):
            positions = (0,) + rest
            fixed = {label: p for label, p in zip(order, positions)}
            text = build(args.n, pairs, fixed)  # type: ignore[arg-type]
            out = subprocess.run(
                ["z3", "-T:5", "-in"], input=text, text=True,
                capture_output=True,
            )
            checked += 1
            if out.stdout.startswith("sat"):
                print(f"sat after {checked}: order={order}, positions={positions}")
                print(out.stdout)
                return
            if not out.stdout.startswith("unsat"):
                print(f"unknown after {checked}: order={order}, positions={positions}")
                print(out.stdout, out.stderr)
                return
    print(f"unsat: checked {checked} fixed SDR placements")


if __name__ == "__main__":
    main()
