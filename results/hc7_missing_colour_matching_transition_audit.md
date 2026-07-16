# Independent audit: missing-colour matching transition

**Verdict:** **GREEN.**

This is a cold audit of
[`hc7_missing_colour_matching_transition.md`](hc7_missing_colour_matching_transition.md).

**Audited source SHA-256:**
`23afae3deec7e3a0506964206f22264de555024f17faf7b2b80ff49c2afd94b0`.

This hash is the strengthened source in which Theorem 2.1 starts from an
arbitrary nonempty exact matching state `D`.  The theorem is an exact
Kempe-bookkeeping statement.  It does not assert that the resulting
carriers are disjoint or that their transition graph has a global
decreasing rank, and the source records those limitations.

## 1. The matching-signature formula

For an edge of `F`, there are three exhaustive cases under a Kempe
interchange on `C`.

1. If zero or two ends lie in `C`, equality of the endpoint colours is
   unchanged.
2. If exactly one end lies in `C` but the other end has a colour outside
   `{a,b}`, the row is unequal both before and after the interchange.
3. If exactly one end lies in `C` and both endpoint colours lie in
   `{a,b}`, equality is toggled.

This proves the symmetric-difference identity (1.1) edge by edge.  In
particular, the source correctly avoids the false simplification that
every matching row crossing `C` toggles.  Properness on `K` is preserved
because `C` is a whole component of the subgraph induced by the two
swapped colours.

The matching hypothesis is not needed for this edgewise identity, but it
is needed later when all equal rows are contracted simultaneously.

## 2. Exclusion of `alpha` from the literal `K_4`

The contact hypothesis is sufficient even though a vertex `q in Q_i`
need meet only one of `x_i,y_i`.  Both endpoints have colour `alpha`, and
`q` is disjoint from every endpoint of `F`; consequently every such
contact edge belongs to `K`.  Properness of `c` on `K` forces
`c(q) != alpha`.

The four vertices of the literal `K_4` have four distinct colours.  With
`alpha`, these account for five distinct labels in the six-colour
palette, so the label `gamma` exists uniquely.  This remains true if the
word “six-colouring” permits some palette labels to be unused elsewhere.
Neither `alpha` nor `gamma` occurs on `Q_i`, hence every
`alpha,gamma` component avoids `Q_i`.

No stronger contact hypothesis—such as every `q` meeting both split
endpoints—is silently used.

## 3. Exact transition from an arbitrary state

If `y_i notin C_i`, the deleted row `e_i` crosses `C_i` and both of its
ends initially have colour `alpha`.  It therefore belongs to the toggle
set `U_i` and becomes proper.  Applying Lemma 1.1 to every row at once
gives exactly

\[
  \operatorname{Eq}_F(c^{C_i})=D\triangle U_i=D_i'.
\]

Because `e_i in D cap U_i`, it is absent from `D_i'`.  This conclusion
does not require any claim about the other two rows: each is toggled if
and only if it lies in `U_i`, whether it started equal or unequal.  In
particular an originally equal row in `D-{e_i}` may be removed, and an
originally unequal row may be added.  A crossing row carrying a third
colour lies outside `U_i` and retains its original equality status.

If `D_i'` were empty, every edge of `K` would be proper after the Kempe
interchange and every edge of `F` would also be proper.  The same vertex
colouring would therefore be a six-colouring of `G`, contradicting
`chi(G)=7`.  This proves the claimed non-emptiness without using an
unproved connectivity or model statement.

For the singleton specialization `D={e_i}`, the identity reduces to

\[
 D_i'=U_i-\{e_i\}=T_i,
\]

so Corollary 2.2 and its labelled-star interpretation are correct.

## 4. Descent to the contracted minor

The state really does descend to `G/D_i'`.  Give the vertex obtained by
contracting a row of `D_i'` the common colour of its two ends.  The rows
of `D_i'` are pairwise vertex-disjoint because `F` is a matching.  Every edge
of the quotient other than a contracted loop comes from either

* an edge of `K`, whose ends have different colours under the proper
  colouring `c^{C_i}`; or
* a row of `F-D_i'`, which is proper because the exact equality signature
  is `D_i'`.

Hence the quotient colouring is proper.  Contractions cannot create an
unseen same-colour conflict: every neighbour of either end of a
contracted row already has a different colour, and simultaneous
contractions use disjoint pairs.  Since `D_i'` is nonempty, `G/D_i'` is
a proper minor.  The phrase “legal contraction state” is therefore
exact, not merely suggestive.

## 5. The strict first drop from `D=F`

When `D=F`, alternative 2 removes the chosen row `e_i`, while
non-emptiness gives

\[
       \varnothing\ne D_i'\subseteq F-\{e_i\}.
\]

As `F` has exactly three rows, the new equality set has size one or two.
Thus Corollary 2.3 proves a strict first drop from size three.  It does
not claim that a subsequent transition from a one- or two-row state
drops cardinality: symmetric difference can add as well as remove rows,
and the involutions can cycle.  The wording of the corollary and trust
boundary preserve this distinction.

## 6. The edge-critical Kempe path

The singleton-signature colouring of `K` extends to `G-e_i`, since the
other two matching rows are proper.  For any colour `beta != alpha`, if
`x_i` and `y_i` belonged to different `alpha,beta` components, swapping
the component containing `x_i` would keep `G-e_i` properly coloured and
would make `e_i` proper.  Restoring `e_i` would six-colour `G`.  Thus the
usual edge-critical Kempe connection is valid for every `beta`, including
`gamma`.

When `y_i notin C_i`, take an `alpha,gamma` path in `G-e_i` from `x_i`
to `y_i`.  It starts in the `K`-component `C_i` and ends outside it.  A
`K`-edge cannot join two distinct `alpha,gamma` components, so the first
edge of the path leaving `C_i` lies in
`(G-e_i)-K=F-{e_i}`.  Its endpoint colours are `alpha,gamma`, and exactly
one end lies in `C_i`; hence that first row belongs to `T_i`.  This
justifies the literal-carrier interpretation.

## 7. Involution and source of all nonempty states

Interchanging `alpha,gamma` does not change the vertex set or edge set of
the two-colour induced subgraph.  Its components, including `C_i`, are
therefore unchanged.  Membership in `U_i` is also unchanged: component
membership is unchanged, and the unordered condition that both endpoint
colours lie in `{alpha,gamma}` is invariant under the swap.  Repeating
the interchange consequently sends

\[
           D_i'\triangle U_i=(D\triangle U_i)\triangle U_i=D
\]

and restores the original colouring.  This is the limited involution
asserted in the source; it is not a monotonicity statement.

Finally, contracting any nonempty `D subseteq F` in a strongly
seven-contraction-critical graph and six-colouring `G/D` supplies exactly
(2.1) after expansion to `K=G-F`.  The matching condition makes the
contracted branch sets disjoint and ensures that every row in `F-D`
retains distinct ends and survives as an edge of `G/D`, so those rows are
proper.  The rows in `D` expand with equal endpoint colours.  Thus every
nonempty punctured-cube state used by Theorem 2.1 is genuinely available.

## 8. Adversarial boundary checks

The natural attempted counterexamples all fail for explicit reasons:

* a `Q_i` vertex coloured `alpha` violates its literal contact edge in
  `K`;
* a third-colour crossing row does not toggle and is excluded from
  `U_i`, exactly as required;
* an empty `D_i'` immediately extends the swapped colouring to `G`;
* quotient conflicts after contracting `D_i'` would already be
  same-colour edges of `K` or proper rows of `F-D_i'`;
* starting from `D=F`, retaining `e_i` after the swap is impossible
  because `e_i` lies in both `D` and `U_i`; and
* in the singleton specialization, an `alpha,gamma` path leaving `C_i`
  without a row of `T_i` would require a `K`-edge between distinct
  two-colour components.

None yields a counterexample to a stated quantifier.

## 9. Trust boundary

The result supplies one connected labelled carrier and an exact legal
state transition.  It does **not** prove that three such carriers can be
made disjoint, that their transition involutions cannot cycle, that the
new state preserves any chosen clique model, or that a well-founded
global rank exists.  Those remain composition obligations rather than
defects in this theorem.
