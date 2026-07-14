# Independent audit: two-spare Kempe Hall barrier

Audited files:

- `hc7_exact7_two_spare_kempe_hall_barrier.md`;
- `hc7_exact7_two_spare_kempe_hall_barrier_verify.py`.

## Verdict

**GREEN.**  The page is planar and three-connected, realizes the paired
state and zero spare-column, has the displayed literal reversed linkage,
and has neither two disjoint outer-duty carriers nor the named reversed
rooted-`K_4` expansion.  Three internally disjoint row locks exclude a
two-vertex transversal of that lock family.

The artificial-terminal graph is planar with the four terminals alternating
on one face, so the carrier obstruction is topological rather than a
palette inference.  The rooted-model encoding was also rerun without its
root-order symmetry restrictions and remained unsatisfiable.  Both normal
and optimized Python runs produced the same six GREEN checks; proof checks
do not rely on assertions.

The scope is honest: this is not a seven-connected or contraction-critical
host.  It falsifies the generic Kempe-Hall shortcut only.  The independently
proved curvature exchange uses the additional full three-duty
nonreflection and host degree constraints, so the two results are
consistent.
