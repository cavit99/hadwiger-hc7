#!/usr/bin/env python3
"""Counterexample to pairwise portal disjointness from the disk rule alone.

Use the pentagram SDR order 0,2,4,1,3 and identify one extra occurrence of
labels 0 and 1 with the SDR occurrence of label 3.  Thus

    P0={b0,b3}, P1={b1,b3}, P2={b2}, P3={b3}, P4={b4}.

All five exact crossless-frame disk constraints remain consistent.
"""

import itertools
import subprocess

from c6_circular_witness_degenerate_smt import antipodal_forbidden
from moser_c5_three_crossless_exact_probe import frame


ORDER = (0, 2, 4, 1, 3)
OCC = {
    0: ("b0", "b3"),
    1: ("b1", "b3"),
    2: ("b2",),
    3: ("b3",),
    4: ("b4",),
}

lines = ["(set-logic QF_LIA)"]
for i in range(5):
    lines.append(f"(declare-fun b{i} () Int)")
    lines.append(f"(assert (and (<= 0 b{i}) (< b{i} 5)))")
lines.append("(assert (= b0 0))")
for first, second in zip(ORDER, ORDER[1:]):
    lines.append(f"(assert (< b{first} b{second}))")
for j in range(5):
    for values in itertools.product(*(OCC[label] for label in frame(j))):
        lines.append(f"(assert {antipodal_forbidden(*values, 5)})")
lines.extend(("(check-sat)", "(get-model)"))

result = subprocess.run(
    ["z3", "-in"], input="\n".join(lines), text=True,
    capture_output=True, check=False,
)
assert result.stdout.splitlines()[0] == "sat", result.stdout + result.stderr
print("SAT: all five disk rules permit P0 cap P1 = P3 = {b3}")
print(result.stdout)
