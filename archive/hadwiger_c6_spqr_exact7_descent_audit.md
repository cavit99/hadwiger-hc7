# Independent audit: SPQR exact-seven descent

## Verdict

**GREEN, conditional on the already stated exact two-piece contact atlas.**

Theorem 2.1 correctly proves that every separation pair of the
two-connected `C_6 dotunion K_1` shore has an open component with exactly
two old-boundary defects.  Its neighbourhood with the two poles is an
exact seven-cut, and the complementary vertices form one connected shore.

The proof does **not** make the two classification errors which would
invalidate it:

1. a size-two defect is not assumed to be an antipodal pair or a
   cycle-neighbour pair; and
2. an enlargement `{v,w}|N_F(v)` of the singleton-base row is allowed.

The enlarged singleton row is harmless for the descent: whenever the
first component already has defect two, it is selected immediately.  The
atlas is used more specifically only when that first defect is a
singleton.

This is an internal logical audit, not an independent certification of the
computer-generated 28-row atlas or a novelty claim.

The supplied atlas generator was nevertheless replayed during this audit.
It checked all `3^7=2187` contact pairs, found `762` negative pairs and
exactly `28` maximal negative pairs, and printed the advertised rows.

## 1. Low-defect atlas domination

Let the two components of `D-{p,q}` be `A,B`.  For the connected split

\[
                         A\mid(D-A)
\]

write

\[
 \Delta_A=S-N_S(A),\qquad E_A=S-N_S(D-A).
\]

Seven-connectivity gives `|Delta_A|,|Delta_B|<=2`, and

\[
                         E_A\subseteq\Delta_B,      \tag{1.1}
\]

because `B` is contained in `D-A`.  Thus both atlas coordinates have size
at most two.

Among the base negative rows, every row with an empty coordinate has the
other coordinate of order at least three.  Hence it cannot be dominated by
this low-defect pair.  The remaining possibilities are precisely:

* a singleton-base row, possibly enlarged on its singleton side,
  \[
       \{v\}\subseteq d_X,\qquad d_Y=N_F(v);
  \]
* two distinct antipodal pairs.

Both coordinates are therefore nonempty.  If `|Delta_A|=2`, the desired
component is already `A`, regardless of whether that two-set is antipodal,
a cycle-neighbour set, contains `z`, or is the enlarged singleton defect
`{v,w}`.

If `|Delta_A|=1`, write `Delta_A={v}`.  It cannot be an antipodal pair or
the two-element `N_F(u)` coordinate.  It is necessarily the singleton
coordinate itself, and atlas domination forces

\[
                         E_A=N_F(v).                \tag{1.2}
\]

By (1.1) and `|Delta_B|<=2`, equation (1.2) gives
`Delta_B=E_A`, so `B` has defect exactly two.  This proves the core
selection without classifying arbitrary size-two defects.

## 2. The new cut is literal

For the selected component `C`, every neighbour outside `C` lies either in
`N_S(C)` or at one of the poles.  Since `D` is two-connected, each pole has
a neighbour in every component of `D-{p,q}`.  Therefore

\[
                         N_G(C)=N_S(C)\mathbin{\dot\cup}\{p,q\}.
\]

The right side has order `(7-2)+2=7`, separates `C` from the old opposite
shore `H`, and consists entirely of actual neighbours.  It is therefore a
literal exact seven-cut.  The fragment `C` is nonempty and proper in `D`.
No labelled portal is contracted to a pole.

## 3. Far-side connectivity

Return to `C=A`, with `|Delta_A|=2`.  The negative atlas makes `E_A`
nonempty.  Take `t in E_A`.  The set `D-A` contains `B,p,q`, so none of
those vertices contacts `t`.  Fullness of `D` forces an `A` contact, and
hence

\[
               t\notin\Delta_A,\qquad t\in\Delta_B. \tag{3.1}
\]

If `B` missed both members of `Delta_A`, then

\[
                    \Delta_A\cup\{t\}\subseteq\Delta_B,
\]

contradicting `|Delta_B|<=2`.  Thus `B` contacts at least one retained
vertex of `Delta_A`.

After deleting the new cut, the vertices outside `A` are exactly

\[
                         B\cup\Delta_A\cup H.
\]

The old full shore `H` contacts both members of `Delta_A`, and `B` contacts
at least one, so this union is connected.  Hence the new cut has exactly
two complementary components.  The standard minimum-cut argument makes
both full: if one component missed a cut vertex, deleting the other six
cut vertices would still separate it.

This far-side check is the point at which nonemptiness of the opposite
atlas defect is essential.  Two-connectivity alone would not connect `B`
to the old boundary vertices which survive the new cut.

## 4. Boundary-core classification

The four induced missing-graph types after deleting the two old defect
vertices are correct and exhaustive:

* delete `z` and one cycle vertex: `P_5`;
* delete two cycle vertices at cyclic distance one: `P_4 dotunion K_1`;
* distance two: `P_3 dotunion 2K_1`;
* distance three: `2K_2 dotunion K_1`.

The two promoted poles may have arbitrary literal contacts with this
five-vertex old-boundary core and may be nonadjacent.  Thus the note does
not overreduce the transfer state to neighbour-pair or antipodal defects.

## 5. Exact scope

The audited consequence is:

> a nontrivial SPQR tree in the original `C_6 dotunion K_1` two-full-shore
> cell always yields a strictly smaller exact-seven fragment.

It does not recursively close the problem, because the new seven-boundary
is one of the four cores above decorated by two arbitrary pole-contact
rows.  Continuing without accepting descent requires a boundary-transfer
theorem for those new cores.  Nothing in the proof produces a global
portal face or proves `HC_7`.
