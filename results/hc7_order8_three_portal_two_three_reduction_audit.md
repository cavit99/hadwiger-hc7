# Independent audit: two--three linkage reduction for three portal sets

**Audit status:** separate internal mathematical audit; **GREEN**.

**Audited source:**
[`hc7_order8_three_portal_two_three_reduction.md`](hc7_order8_three_portal_two_three_reduction.md)

**Audited source SHA-256:**
`9de3848f006c61872c059a61018fae03805b603cd9ad8a56ec515c8112967c4d`

After this audit, the source status was changed only to record the GREEN
verdict and link to this file, the TeX command in (3.2) was corrected, and
three prose set expressions were converted to equivalent TeX notation.  No
theorem statement, hypothesis, proof step, conclusion, scope, or trust
boundary changed.  The resulting promoted source SHA-256 is
`96595654a3e764710485c73c9dccd1f438f49d650e1d7f7c03dba9737514b202`.

This is an internal audit, not external peer review.  It checks Theorem 2.1,
Corollary 3.1, their external and internal dependencies, and the stated trust
boundary.  It does not prove `HC_7`.

## Verdict

The exact revision identified above is correct within its stated scope.
The Hall obstruction, Xie completion, completed-cut shape, host-neighbourhood
lift, and positive-excess consequence all preserve literal vertices and use
the correct separator orders.  No palette colour is identified with a
boundary or branch-set label.

The result is a reduction, not a closure theorem.  Its order-seven output is
not colour-compatible, its small-component outcome remains open, and its
positive-excess lobe has not been converted into either a packing or a
`K_7`-minor model.

## 1. Portal representatives and Hall's theorem

Equation (1.1) means exactly that every boundary vertex has a neighbour in
`Q`, so all five portal sets are nonempty.  If these five sets have no system
of distinct representatives, Hall's theorem supplies a nonempty index set
`I` whose union `Z` has order at most `|I|-1`.

For every component `C` of `Q-Z`, a boundary vertex in `I` has no neighbour
in `C`, and every neighbour of `C` in `Q` belongs to `Z`.  Hence

\[
 N_G(C)\subseteq Z\cup(S-I),\qquad
 |N_G(C)|\le (|I|-1)+(8-|I|)=7.
\]

The second component of `G-S` lies outside `C\cup N_G(C)`, so this is an
actual separation rather than merely a neighbourhood bound.  Seven-
connectivity forces equality.  If `Q-Z` is empty, then `|Q|<=4`, which is
correctly retained inside the stated `|Q|<=6` outcome.  Thus no collision of
literal portal representatives is hidden in the linkage invocation.

## 2. Xie's five-terminal completion

The external statement was checked against Theorem 1.2.1 of Shijie Xie's
2019 dissertation, *6-Connected Graphs Are Two-Three Linked*.  For five
distinct vertices `a_1,a_2,a_3,b_d,b_e`, it assumes that the original graph
after adding

\[
 b_db_e\quad\text{and}\quad a_i b_d,a_i b_e\ (i=1,2,3)
\]

is six-connected.  It concludes that the **original** graph has two
vertex-disjoint connected vertex sets containing the nominated triple and
pair, respectively.  These are exactly the seven virtual edges and the
conclusion used in lines 145--158 of the audited source.

The five representatives are explicitly distinct.  The connected subgraph
containing `b_d,b_e` contains a nontrivial path between those two distinct
vertices; the other connected subgraph meets all three literal `x_i` portal
sets.  They therefore give precisely the packing defined in Section 1, not
an unlabelled or completion-only surrogate.

When `|Q|>=7`, failure of six-connectivity of the completion does yield a
separation of order at most five with two nonempty open sides.  No such claim
is made for `|Q|<=6`.

## 3. Shape of a completed-graph cut

The virtual edge `b_db_e` prevents surviving `b`-terminals from occupying
opposite open sides.  If either `b` survives outside the separator, its six
virtual incidences put every surviving nominated terminal on its side.
Consequently, if both open sides contain nominated terminals, both
`b_d,b_e` lie in the separator and surviving `a_i` occur on both sides.

Otherwise at least one open side is terminal-free, and any component chosen
there contains none of the five nominated vertices.  This also covers the
degenerate possibility that all five nominated vertices lie in the
separator and both open sides are terminal-free.  The source phrase “only
one open side contains nominated terminals” is narrower than necessary, but
the immediately following terminal-free-component construction applies
unchanged when neither side contains one; no theorem conclusion depends on
excluding that subcase.

For the selected component `C`, no original edge of `G[Q]` crosses from `C`
to `Q-(C\cup K)`, so `N_{G[Q]}(C)\subseteq K`.  The virtual edges are used
only to obtain this separation and are never lifted as host edges.

## 4. Host lift and separator arithmetic

Because `Q` is a component of `G-S`, every neighbour of `C` outside `Q` is a
literal member of `S`.  Thus

\[
 N_G(C)=N_{G[Q]}(C)\mathbin{\dot\cup}(N_G(C)\cap S).
\]

A vertex on the other open side of the completed separation, as well as the
assumed second component of `G-S`, lies outside `C\cup N_G(C)`.  Therefore
`N_G(C)` is the boundary of an actual separation.  Seven-connectivity gives
`|N_G(C)|>=7`: equality is outcome 2, while absence of outcome 2 gives the
integer bound `|N_G(C)|>=8`.  The source does not misread the completed cut
`K` itself as a host separator.

The two terminal forms are exhaustive: either a terminal-free component is
chosen, or the separator contains `b_d,b_e` and separates surviving members
of the nominated triple.

## 5. Positive-excess corollary

In Corollary 3.1, the selected `C` is a nonempty connected proper subset of
the original component `Q`; properness follows from the nonempty opposite
open side.  If `|N_G(C)|=8`, its internal and boundary neighbours are
disjoint and sum to eight.  The audited small-boundary lobe theorem therefore
applies literally and returns either an order-seven separation or a strict
order-eight descent.  Both are excluded by hypothesis.  Combined with the
lower bound of eight from Theorem 2.1, integrality gives
`|N_G(C)|>=9`, and

\[
 |N_G(C)\cap S|=|N_G(C)|-|N_{G[Q]}(C)|
                 \ge 9-|K|.
\]

For an edge `uv` from `C` to its full neighbourhood, `G-uv` is a proper
minor and hence has a six-colouring.  Every such colouring makes `u,v`
equal: otherwise the deleted edge can be restored and gives a six-colouring
of `G`.  This is an operation-specific literal response, not a branch-set
allocation.

## 6. Exact trust boundary

The audited result does **not** prove any of the following:

- that the small `|Q|<=6` branch is impossible;
- that the returned order-seven separation has a common equality partition
  on its two closed shores;
- that a positive-excess lobe yields three prescribed portal contacts or an
  explicit `K_7`-minor model;
- that the strict descent preserves the inherited five branch-set labels or
  selected colouring response; or
- `HC_7`.

No mathematical gap was found in the claimed reduction.
