# Audit of the pentagonal order-seven corollary

**Verdict:** GREEN.

**Source audited:** `results/hc7_pentagonal_separation_completion.md` at
SHA-256
`c627b4bc8222a674a13c7e4dc6e7d33f876becb163b24617764afedc7ee8c0da`.

**Audit class:** separate internal line-by-line audit. This is not external
peer review.

## 1. Reduction to the cycle-boundary theorem

The displayed boundary has exactly seven vertices and the two nonempty
connected components `A,B` are the complete open shores of the separation.
If one shore missed a boundary vertex `s`, its full neighbourhood would be
contained in the other six boundary vertices. The opposite shore is
nonempty, so this is a separation of order at most six, contrary to
7-connectivity. Thus both shores are adjacent to every vertex of
`V(C)\cup\{p,q\}`.

All remaining hypotheses of the separately audited
[cycle-boundary completion theorem](hc7_cycle_boundary_completion.md) are
literal: `C` is induced and has length five, `p,q` are adjacent and
complete to `C`, the two shores are connected, nonempty and anticomplete,
and `G-\{p,q\}` contains a `K_5` minor. Invoking that theorem therefore
gives exactly the asserted `K_7` minor. No part of its rooted-minor
planarity proof needs to be repeated here.

## 2. Automatic `K_5`-minor hypothesis

If `G-\{p,q\}` were four-colourable, two fresh colours on `p,q` would
six-colour `G`; the fact that `p,q` are adjacent merely requires those two
fresh colours to be distinct. Hence a seven-chromatic `G` satisfies
`\chi(G-\{p,q\})\ge5`. The established `t=5` case of Hadwiger's
Conjecture then supplies a `K_5` minor in `G-\{p,q\}`.

The proof uses no additional minor-minimality beyond the standing
seven-chromatic setting; retaining that phrase matches the programme's
application and does not invalidate the deduction.

## 3. Scope

The corollary contributes two special deductions not assumed by the
general cycle theorem: full attachment follows from the exact order-seven
boundary, and the `K_5`-minor hypothesis follows from seven-chromaticity
and `HC_5`. It does not strengthen the cycle-boundary theorem or close
other exact-seven boundary graphs.

No unresolved mathematical gap was found.
