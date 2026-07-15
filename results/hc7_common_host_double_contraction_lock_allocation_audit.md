# Audit: common-host double-contraction lock allocation

**Verdict:** GREEN.  Lemmas 2.1 and 3.1, the same- and distinct-colour
counts, Corollary 5.2, and the one-restoration transfer in Theorem 6.1 are
valid under the stated strong minor-criticality hypothesis.  In
particular, deleting the restored edge can destroy at most one palette
lock, giving the exact \(q-2\) guarantee.  No row, boundary-duty, path
disjointness, or common-response allocation follows.

**Audited source:**
`results/hc7_common_host_double_contraction_lock_allocation.md`.

**Source SHA-256:**
`753dbf0fc251584dac8a67d907988737ac8dda30daa3dcc24b6fbabd949cf467`.

## 1. Double-contraction state

The edges \(e=ab\) and \(f=cd\) are vertex-disjoint, so contracting both
identifies exactly the two classes \(\{a,b\}\) and \(\{c,d\}\), reduces
the number of vertices, and gives a proper minor `G/e/f`.  A
\(q\)-colouring of that minor expands to `H` by assigning each pair the
colour of its contracted image.

The expansion is proper.  Every edge of `H` has endpoints in distinct
contraction classes and maps to an edge of `G/e/f`.  This includes all
cross-edges between the two named pairs: each becomes an edge between the
two distinct contracted images.  Edges from a common outside neighbour to
both ends of a pair become parallel before simplification, but the outside
neighbour already has a colour different from the image; expanding the
parallel edge back to two edges remains proper.  The only edges becoming
loops are `e,f` themselves, and those are absent from `H`.

Thus state `(equal,equal)` exists.  State `(proper,proper)` is impossible,
because restoring both deleted edges would then preserve the colouring and
\(q\)-colour `G`.

The one-edge hosts satisfy

\[
                         H+e=G-f,
\qquad                    H+f=G-e.
\]

Each is a proper edge-deletion minor and hence has a \(q\)-colouring.
Every colouring of `H+e` makes `e` proper and must make the ends of `f`
equal; otherwise restoring `f` would colour `G`.  The symmetric statement
holds for `H+f`.  Hence all four clauses of Lemma 2.1, including existence
and universality of the two opposite one-restoration states, are exact.

The double-contraction colouring need not use every nominal member of
`[q]` a priori.  This causes no problem in the later lock arguments: an
unused alternate colour makes each vertex of the common colour an isolated
vertex in that two-colour subgraph, so the relevant unlocked switch is
still available and would yield the same contradiction.

## 2. Component switching over \(\mathbf F_2\)

Switching `i,j` on a whole component of the induced two-colour graph
preserves properness.  An edge from the component to an external vertex of
colour `i` or `j` would put that vertex in the same component; all other
external colours are unaffected.  Distinct components can therefore be
switched independently.

For a same-coloured pair whose endpoints lie in components `p,r`, exactly
one end changes precisely when \(s_p+s_r=1\).  Thus the displayed linear
forms give the exact proper/equal status after switching.  A pair is
unlocked exactly when its two component indices differ, equivalently when
its form is nonzero.

Over \(\mathbf F_2\), two nonzero linear forms are either equal or linearly
independent.  In the equal case any vector on which the common form is one
makes both pairs proper.  In the distinct case the map to
\(\mathbf F_2^2\) has rank two and attains `(1,1)`.  This proves the final
simultaneous-switch assertion without requiring the pairs to occur in a
crossed or uncrossed component order.

## 3. Same-colour count

When all four endpoints have colour `i`, fix any \(j\ne i\).  If both
pairs were unlocked in the `i-j` graph, Lemma 3.1 would produce a
`(proper,proper)` colouring of `H`, forbidden by Lemma 2.1.  Hence each of
the \(q-1\) alternate colours contributes at least one lock incidence
across the two named pairs.  Pigeonhole gives

\[
                 \max\{L_e,L_f\}
                 \ge \left\lceil\frac{q-1}{2}\right\rceil.
\]

For \(q=6\) this is exactly the claimed lower bound three.  Locks for
different colours are counted as palette incidences; no disjointness of
their witnessing paths is implied.

## 4. Distinct-colour count

Suppose the equality colours are distinct, `i` on `ab` and `k` on `cd`.
For \(\beta\in U\), one `i-beta` component switch makes `ab` proper; for
\(\delta\in V\), one `k-delta` switch makes `cd` proper.  If
\(\beta\ne\delta\), the palettes

\[
                         \{i,\beta\},
\qquad                    \{k,\delta\}
\]

are disjoint because \(\beta,\delta\notin\{i,k\}\).  Their switched
vertex sets are consequently disjoint, neither switch changes membership
in the other two-colour graph, and every edge between the two sets still
has endpoints in disjoint palettes.  The switches commute and make both
deleted edges proper, a contradiction.

It follows that every element of nonempty `U` equals every element of
nonempty `V`; hence either one set is empty or both are the same singleton.
Applying Lemma 3.1 to the `i-k` graph also forces at least one named pair
to be `i-k` locked.  The counts are then:

* if `U` is empty, `ab` has all \(q-2\) locks indexed by `J`;
* if `V` is empty, `cd` has all \(q-2\) such locks; and
* if \(U=V=\{\theta\}\), both have \(q-3\) locks from
  `J-{theta}`, and one receives the additional `i-k` lock.

Thus one pair has at least \(q-2\) alternate-colour locks.  The formula is
valid also for the small endpoint cases \(q=2,3\), although it is not
sharp for \(q=2\).  For \(q=6\) it gives four.

## 5. Cross-edge sharpening

A cross-edge between \(\{a,b\}\) and \(\{c,d\}\) survives in `H` and
becomes an edge between the two distinct contracted images in `G/e/f`.
Therefore their colours differ in every expanded double-contraction
colouring.  Equivalently, the same conclusion follows directly in `H`
because a cross-edge cannot have equal-coloured ends.  Theorem 5.1 rather
than Theorem 4.1 consequently applies, giving four locks when \(q=6\).

This conclusion needs only one cross-edge.  It does not say which named
pair receives the four-lock majority.

## 6. Transfer from a one-edge restoration

Let `rho_e` colour `H+e`.  Its edge `e=ab` is proper, and the endpoints
`c,d` of `f` have a common colour `k`.  Fix \(j\ne k\).  If `c,d` were in
different components of the `k-j` graph, switching the component
containing exactly one of them would:

1. preserve properness of the whole host `H+e`, including its present edge
   `e`;
2. make `c,d` different; and therefore
3. remain proper after restoring `f`, producing a forbidden
   \(q\)-colouring of `G`.

Thus `cd` is locked for all \(q-1\) alternate colours in `H+e`.

Write `r,s` for the distinct colours on `a,b`.  The deleted edge `e`
belongs to the induced `k-j` graph precisely when
\(\{r,s\}=\{k,j\}\).  Since `r,s` are fixed and distinct, this happens for
at most one choice of `j`: it happens once if one of `r,s` is `k`, and
never otherwise.  For every other `j`, deleting `e` removes no edge of the
`k-j` induced subgraph, so the existing `c-d` component and a literal lock
path remain wholly in `H`.

At least \((q-1)-1=q-2\) common-host locks therefore survive.  The
argument is universal for every colouring of `H+e`; the symmetric argument
is universal for every colouring of `H+f`.  For \(q=6\), one response
colouring supplies four common-host locks for `cd`, while the opposite
response supplies four for `ab`.

The two response colourings may be unrelated.  The theorem does not put
both four-lock systems into one colouring, and paths from different
palettes may share vertices.

## 7. Atomic specialization and exact scope

For \(q=6\), the double-contraction colouring of the atomic named edges
has one of two audited forms:

1. equal equality colours, yielding a three-lock majority by Theorem 4.1;
2. distinct equality colours, yielding a four-lock majority by Theorem
   5.1.

Any cross-edge forces the second form.  All these locks are in the common
edge-deletion host `H`.  The separate one-restoration colourings give four
common-host locks for each named pair by Theorem 6.1, but not in one common
colouring.

The result does **not** prove:

* internal disjointness of lock paths;
* correspondence between palette colours and rows of the spanning
  \(K_6\) model;
* a split of any model row or allocation to exact-seven boundary duties;
* equality of the exact boundary partitions returned by the one-edge
  contraction responses and the double-contraction colouring; or
* a fixed pair, literal \(K_7\), or strict ranked exact-seven handoff.

The double-contraction colouring descends to `G/e/f`, but not to `G/e` or
`G/f` separately: the other uncontracted named edge would be
monochromatic.  The source correctly stops at a graph-global lock
allocation input.
