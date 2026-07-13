#!/usr/bin/env python3
"""Sixteen-row certificate for the normalized circular occurrence lemma."""

from __future__ import annotations

import itertools
import subprocess

from c6_circular_witness_degenerate_smt import formula, verify_sdr_orders


ORDER = (0, 2, 4, 1, 5, 3)
EXTRA = 1

# In abstract matching notation these are B2, B1, A1, A0.
PIECES = (("f0", "f1"), ("f2", "f3"),
          ("g0", "g1"), ("g2", "g3"))


def force_pattern(source: str, pattern: tuple[bool, ...]) -> str:
    assertions = []
    for collapsed, (first, second) in zip(pattern, PIECES):
        relation = "=" if collapsed else "distinct"
        assertions.append(f"(assert ({relation} {first} {second}))")
    return source.replace("(check-sat)", "\n".join(assertions) + "\n(check-sat)")


def main() -> None:
    verify_sdr_orders()
    total = 0
    for pattern in itertools.product((False, True), repeat=4):
        result = subprocess.run(
            ["z3", "-in"],
            input=force_pattern(formula(ORDER, EXTRA), pattern),
            text=True,
            capture_output=True,
            check=False,
        )
        status = result.stdout.splitlines()[0] if result.stdout else "error"
        word = "".join("C" if value else "N" for value in pattern)
        print(word, status)
        assert status == "unsat"
        total += 1
    print("patterns", total, "satisfiable", 0)


if __name__ == "__main__":
    main()
