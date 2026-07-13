# Singleton-gate holonomy is forced to backtrack

## Status

This is a lifted, label-preserving composition theorem for two successive
single-gate rotations over one fixed `K_5` row frame.  In the branch with
no `K_7^-` minor, a singleton gate cannot be followed through the same
two-shore carrier by a different singleton gate.  The only second move is
the exact inverse.

Thus the `C_5`-type holonomy suggested by the quotient labels cannot live
inside one fixed-frame singleton connector.  Any genuine rotation cycle
must change the five-row frame, use a nonsingleton connector, or use the
separate two-piece concentrated exchange.

## 1. Two consecutive pivots on one frame

Fix pairwise adjacent connected rows `F_1,...,F_5`.  Start with a
single-gate rotation datum

\[
                   A,\quad U=W\mathbin{\dot\cup}Z,
                   \quad F_1,\ldots,F_5,                 \tag{1.1}
\]

as in `../results/hc7_near_k7_rotation_edge.md`.  Thus `A` is the old
centre with missing set `D`, the old donor `U` is full to all five rows,
and the first pivot gives

\[
                  W,\quad A'=A\cup Z,quad F_1,\ldots,F_5 \tag{1.2}
\]

with new missing set `E`.  The connector `Z` meets every row in
`D union E`.

Now make a second single-gate pivot **through the donor `A'`**, retaining
the same five fixed rows.  Write

\[
                     A'=R\mathbin{\dot\cup}Y             \tag{1.3}
\]

with `R,Y` nonempty and connected.  The second gate `Y` must meet the
current centre `W` and every row in `E`; moving it into `W` leaves `R` as
the next centre.

## Lemma 1 (common-label shadow persistence)

For every label `c in D cap E`, every `Y-F_c` contact has its `Y`-end in
`Y cap Z`.  In particular,

\[
                         D\cap E\ne\varnothing
            \quad\Longrightarrow\quad Y\cap Z\ne\varnothing. \tag{1.4}
\]

### Proof

The old centre `A` is anticomplete to every row in `D`, hence to `F_c`.
The donor for the second pivot is `A'=A union Z`.  Therefore every
`A'F_c` edge has its `A'`-end in `Z`.  Since the second gate must meet
every currently missing row, it contains an `F_c`-neighbour.  That
neighbour lies in `Y cap Z`. \(\square\)

This is the literal lift of pair overlap: a common old/new missing label
cannot be serviced by a fresh vertex of the old centre.  Its portal must
be carried forward from the old gate.

## Theorem 2 (singleton backtracking)

Assume `G` has no `K_7^-` minor and

\[
                              |D|=|E|=2.                  \tag{2.1}
\]

If both the first and second gates are singletons, then the second pivot
is the exact inverse of the first.

### Proof

The missing-pair overlap theorem gives `D cap E nonempty`; otherwise the
first rotation datum already contains a literal `K_7^-` minor.

Write `Z={s}` and `Y={t}`.  Lemma 1 gives

\[
                              t=s.                        \tag{2.2}
\]

Thus the second pivot removes from `A'=A union {s}` exactly the vertex
inserted by the first pivot.  Its residual centre is `A`, while the
enlarged donor is `W union {s}=U`.  The exact involution theorem says that
the recovered missing set is precisely `D`.  Hence the second move is the
literal inverse, not merely an isomorphic state. \(\square\)

## Corollary 3 (where nontrivial holonomy can occur)

In a `K_7^-`-minor-free host, quotient the fixed-frame single-gate state
graph by exact inverse edges.  No vertex represented by a singleton
connector has a nontrivial singleton continuation through the opposite
shore.  A non-backtracking walk must use at least one of:

1. a second gate `Y` of order at least two which contains a literal portal
   inherited from `Z` for every common missing label;
2. a pivot through one of the five fixed rows, thereby changing the
   `K_5` frame; or
3. the two-piece concentrated rotation, which is not a single connected
   gate and is not involutive by the preceding theorem.

Consequently a five-cycle of abstract missing pairs is not by itself a
lifted holonomy certificate.  It must also specify frame changes or a
strictly non-atomic connector.  This removes the atomic fixed-frame cycle
from the composition gap.

## General missing-star form

Lemma 1 is independent of the numbers five and two.  In any missing-star
model, if a gate changes missing set `D` to `E` and the next pivot uses
the enlarged old centre as donor, every common label in `D cap E` forces
the next gate to reuse an old-gate portal.  Whenever an external theorem
forces `D cap E nonempty`, singleton gates are exact backtracks.

