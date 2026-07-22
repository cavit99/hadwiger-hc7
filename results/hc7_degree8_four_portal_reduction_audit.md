# Separate internal audit of the fourfold portal reduction

**Verdict:** **GREEN**.

**Audited source:**
[`hc7_degree8_four_portal_reduction.md`](hc7_degree8_four_portal_reduction.md)

**Audited SHA-256:**
`f619a3166654e3fb2f07b7448c317b026aa04d73322c21377f4dd858bdb43a3e`.

This is a separate internal mathematical audit, not external peer review.
It does not prove `HC_7`.

## Hypothesis matching and the packing branch

For each `(Q,B)` in `{E,F} x {I,T}`, the substitution

\[
                 d=p,\qquad e=q,\qquad \{x_1,x_2,x_3\}=B
\]

meets every hypothesis of the audited three-portal reduction.  The graph
`G-S` has components `{u},E,F`; hence `Q` is a component, another component
is present, and fullness gives `N_G(Q)=S`.  The five boundary vertices are
distinct and all five portal sets are nonempty.

A positive three-portal packing contains a nontrivial `p`--`q` path whose
vertex set is a root connector.  Its disjoint connected triple-portal
subgraph is a `B`-carrier.  This contradicts Theorem 3.1 of the audited
two-defect component closure.  The proof therefore eliminates exactly the
positive branch and does not assume a converse that would fail for a
singleton root connector.

## Separation outcomes

An actual order-seven separation supplies a generic exact-seven response:
choose a connected component behind the separator and an entering edge.
Seven-connectivity makes its full neighbourhood the entire seven-set, and
minor-criticality gives a six-colouring of the edge deletion with equal
endpoint colours.  If the induced boundary partition extended through the
intact selected side, the two colourings would glue and six-colour `G`.
No inherited `p,q,I,T` compatibility is inferred.

The small-shore outcome is retained literally.  For a proper connected set
returned by the completed five-terminal cut, boundary order eight meets the
hypotheses of the audited small-boundary lobe theorem.  Its alternatives are
the preceding order-seven response or a strict order-eight lobe with exactly
two or three boundary-full complementary components.  Boundary order at
least nine is therefore the only remaining confined-set case.

## Positive-excess arithmetic and colouring response

Put `R=N_{G[Q]}(C)`.  The three-portal reduction gives (R\subseteq K),
`|K|<=5`, and

\[
 N_G(C)=R\mathbin{\dot\cup}(N_G(C)\cap S),\qquad |N_G(C)|\ge9.
\]

Since `|S|=8`, these identities give

\[
 9\le |N_G(C)|\le |R|+8\le13,
 \qquad |N_G(C)\cap S|\ge9-|R|,
\]

and consequently

\[
                 |S-N_G(C)|\le |R|-1\le4.
\]

Thus (2.1)--(2.3) are correct.  The five nominated representatives and the
two possible completed-cut terminal distributions are retained exactly from
Theorem 2.1 of the three-portal reduction.

For every entering edge `xy`, every six-colouring of `G-xy` makes `x,y`
monochromatic, or the edge could be restored.  The asserted full-separator
partition mismatch is also valid.  The fixed aligned colouring `c_Q`
colours `C union N_G(C)`, while an edge-deletion colouring restricted to
the opposite closed side colours the complement of `C`.  If their equality
partitions on the literal set `N_G(C)` agreed, one palette permutation would
align them vertexwise; gluing would restore `xy` through the intact
`c_Q`-side and six-colour `G`.

Applying the proved one-pair alternative four times gives Corollary 2.2.
The four displayed sets are selected witnesses and may repeat; the result
does not bound the total number of confined connected sets in the host.

## Minimum-excess normal form

Corollary 2.3 applies the minimum positive-excess separator theorem with
the correct hypotheses.  An item-4 set is nonempty and connected, its
displayed neighbourhood is the boundary of an actual separation, and its
boundary order lies between nine and thirteen.  It is therefore eligible.
Choosing an eligible set with globally minimum boundary order gives a
separator `X` with

\[
                         8\le |X|\le13.
\]

If a component behind `X` has neighbourhood of order seven, the cited
theorem supplies the generic exact-seven response in item 1.  Otherwise all
components are full to the literal set `X`, and the same theorem proves that
there are exactly two or three.  Since then `r<=3`, every value of `r` used
in (2.6) lies inside the cited contraction profile's range
`1<=r<=min{m,5}`.  The chromatic and minor inequalities in (2.6), and the
operation-specific extension/rejection assertion, are consequently copied
without strengthening.

This normalization is deliberately block-blind.  The minimizing set need
not be the original selected lobe and the conclusion does not retain its
shore, independent triple, aligned operation, or portal representatives.
The bound on `|X|` bounds only the separator; it does not make the interiors
of its two or three full components finite.

## Three-component tagged-lobe exit

Corollary 2.4 is valid for the selected item-4 lobe itself.  With
`X=N_G(C)`, connectedness of `Q` and the proper inclusion `C subsetneq Q`
make `R=X cap Q` nonempty.  If `M=S-X` were empty, the degree-eight root
`u`, whose neighbourhood is exactly `S`, would be a singleton component of
`G-X` missing every vertex of the nonempty set `R`; this contradicts the
assumed fullness of all three components.  Hence `M` is nonempty.

The inherited aligned setup has exactly the two components `E,F` outside
`N_G[u]`.  Every surviving vertex outside `Q` lies in the component of
`G-X` containing `u`: the vertices of `M` join to `u`, and fullness of the
opposite original shore to `S` joins that shore through every vertex of
`M`.  Besides this component and `C`, the third component `D` is therefore
contained in `Q`.

For any `r in R`, the sets `C union {r}` and `D` are disjoint and connected.
Fullness makes `D` adjacent to `r`, so the two sets are adjacent.  The
identity `X=N_G(C)` and fullness of `D` make both sets adjacent to every
literal vertex of `S-M`.  Thus they have one common defect set `M`, and the
four-bag theorem becomes applicable only under the additional displayed
condition `|M|<=2`.  The corollary does not assert that condition in the
general item-4 case, where (2.3) permits defect as large as four.

## Status of Section 3

Section 3 correctly separates proved reductions from proposed closure
work.  The possible equality of the `I`- and `T`-indexed witnesses is not
silently treated as two lobes, Corollary 2.3 is identified as losing all
portal roles, and the common-defect four-bag theorem is invoked only after
two adjacent sets with one defect of order at most two have been obtained.
The proposed order-eight coupling cases and the finite-signature replacement
lemma are targets, not claimed consequences.  The warning that bounded
`X` does not bound component interiors correctly prevents the suggested
computation from being presented as an exhaustive proof.

## Nonterminal gaps

The proof does not show that the two block-indexed witnesses in one shore
are disjoint, adjacent, nested, or have a common separator or defect.  They
may meet the aligned path and are not thereby post-path residual components
or block carriers.  Their edge-deletion colourings and separator partitions
need not be mutually compatible.  The defect bound is four, not two.

The small-shore branch remains open.  The order-seven and order-eight
interfaces carry fresh responses but do not preserve the original aligned
operation labels.  None of these structural outputs is by itself a common
boundary partition, an explicit `K_7`-minor model, or a strict restart on an
actual component of `G-N[u]`.

All five linked mathematical inputs exist at the stated relative paths and
carry adjacent GREEN internal audits.  This audit treats those promoted
inputs as dependencies rather than reclassifying their conclusions.
