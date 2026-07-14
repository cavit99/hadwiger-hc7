# Two crossed duties close the single-missing gate

**Status:** proved and independently audited.

This note closes the second one-sibling family from
`../results/hc7_exact7_one_sibling_gate_funnel.md`.  Its reusable step is
that two duties with nonadjacent portal witnesses synchronize all three
pairwise web pages; a third opposite-lobe witness is unnecessary.

## 1. Two witnesses synchronize the three pages

Use the abstract setting of Theorem 1.1 in
`../results/hc7_exact7_cross_lobe_common_face.md`, except that
nonadjacent portal witnesses are required for only two of the three duties.
Thus `G` is seven-connected, `S` is a seven-set, `C` is a three-connected
component of `G-S`, the far side `G-(S union V(C))` is nonempty, and

\[
              B_i=\{a_i,t_i\}\qquad(i=1,2,3)
\]

are three pairs of nonadjacent literal boundary vertices.  Assume that no
two distinct duties have vertex-disjoint connected carriers in `C`.

### Lemma 1.1 (two-witness common face)

Suppose that, for two distinct indices `r,s`, there are nonadjacent literal
witnesses

\[
 p_i\in N_C(a_i),\qquad q_i\in N_C(t_i)\qquad(i\in\{r,s\}).
\tag{1.1}
\]

Then `C` is planar and one face in its unique plane embedding is incident
with every vertex of

\[
             \bigcup_{i=1}^3\bigl(N_C(a_i)\cup N_C(t_i)\bigr).
\tag{1.2}
\]

#### Proof

For every pair `i!=j`, adjoin the four artificial terminals whose complete
stars encode the literal portal sets of duties `i,j`, exactly as in the
proof of the audited common-face theorem.  A crossing of the ordered four
terminals deletes to two disjoint duty carriers in `C`, so the tuple is
crossless.  The same-vertex Two Paths theorem completes the auxiliary graph
to a four-web.

The clique-cell elimination in that proof is pairwise and uses no
nonadjacent witness.  If `D` is a component of actual `C`-vertices inside a
cell with rib triangle `Delta`, then

\[
        N_G(D)\subseteq \mu(V(\Delta))\cup\{c,a_k,t_k\},
        \qquad |N_G(D)|\le6,                              \tag{1.3}
\]

where `k` is the unrepresented duty.  This separates `D` from the nonempty
far side, contrary to seven-connectivity.  Deleting completion edges and
then the four artificial terminals therefore leaves a genuine face `F_ij`
of `C` incident with all four complete literal portal sets of duties `i,j`.

Identify the plane embeddings by Whitney uniqueness.  After relabelling
take the two witnessed duties to be `2,3`.  The faces `F_12,F_23` both
contain the nonadjacent vertices `p_2,q_2`, so they are equal: two distinct
faces of a three-connected plane graph cannot meet in two nonadjacent
vertices.  Similarly `F_13=F_23` through `p_3,q_3`.  Their common value is
incident with all six complete portal sets, proving (1.2).  \(\square\)

## 2. Exact single-missing support

Use the attained paired state

\[
 S=\{c,a_1,t_1,a_2,t_2,a_3,t_3\},\qquad
 \Pi=\bigl\{\{a_i,t_i\}:i\in[3]\bigr\}\cup\{\{c\}\}.
\tag{2.1}
\]

In the rich shore let `C` be an `S`-full component, let `Q` be a disjoint
connected `S`-full packet, and let `X` be a three-cut of `C` with exactly
two lobes `K,J`.  Assume the single-missing support

\[
 N_S(K)=\{c,a_1,a_2,a_3\},\qquad
 N_S(J)=\{c,a_1,t_2,t_3\}.                              \tag{2.2}
\]

Every member of `X` has a neighbour in each lobe, as supplied by the
audited one-sibling funnel.  No assumption about the isolated or
concentrated secondary gate contacts is needed below.

### Lemma 2.1 (the component has order at least six)

If `Pi` does not reflect, then `|C|>=6`.

#### Proof

The cut and its two nonempty lobes give `|C|>=5`.  Assume equality.  Then
`K={k}` and `J={j}`.  If two duties had disjoint carriers in `C`, the full
packet `Q` would fund the third duty and reflect the attained state.  Thus
Lemma 1.1 applies: duties `2,3` have nonadjacent witnesses `k,j`, by (2.2)
and the fact that different components of `C-X` are anticomplete.  Let `F`
be the resulting common facial cycle.

Both `k,j` lie on `F` and are nonadjacent, so `4<=|F|<=5`.  If `|F|=5`,
all vertices of `C` lie on one face.  The simple outerplanar bound gives
`|E(C)|<=2|C|-3=7`, whereas three-connectivity gives
`2|E(C)|>=3|C|=15`, hence `|E(C)|>=8`, a contradiction.

If `|F|=4`, let `w` be the fifth vertex.  Every neighbour in `C` of any of
the six non-`c` boundary labels lies on `F`, so `w` has no such boundary
neighbour.  It has at most four neighbours in `C`, at most the one boundary
neighbour `c`, and no neighbour outside `C union S`.  Hence

\[
                             d_G(w)\le5,
\]

contrary to the frozen minimum-degree bound `delta(G)>=7`.  \(\square\)

### Theorem 2.2 (single-missing curvature exchange)

In a hypothetical minimal counterexample to `HC_7`, the configuration
(2.1)--(2.2) reflects.  Consequently the complete single-missing-duty
one-sibling family is impossible.

#### Proof

Assume nonreflection.  As above, the full packet `Q` makes every two
distinct duties fail to have disjoint connected carriers in `C`.  For
`i=2,3`, choose an `a_i` portal in `K` and a `t_i` portal in `J`.  The two
chosen vertices are nonadjacent, so Lemma 1.1 gives one face `F` incident
with all six complete portal sets.

Lemma 2.1 gives `|C|>=6`.  The incidence graph between the six non-`c`
boundary labels and `C` has a matching saturating those labels.  Indeed,
Hall failure supplies a nonempty label set `U` with
`|N_C(U)|<|U|`; deleting

\[
                         (S-U)\cup N_C(U)               \tag{2.3}
\]

uses fewer than seven vertices.  The set `C-N_C(U)` is nonempty because
`|C|>=6` and `|N_C(U)|<=5`; it cannot reach a surviving member of `U`,
while every other boundary exit is deleted.  The old far shore survives,
contradicting seven-connectivity.

Select the six distinct matched portals on `F`.  The endpoints of every
two duties alternate on `F`: otherwise two complementary facial subpaths
are disjoint carriers for those duties and reflect `Pi` with `Q`.  Hence,
up to rotation, reflection, and renaming, their cyclic duty word is

\[
                              A\ B\ D\ A\ B\ D.          \tag{2.4}
\]

Relabel the six complete portal sets in this cyclic order.  They now meet
all hypotheses of the audited facial portal-incidence bound in
`../results/hc7_exact7_cross_lobe_curvature_exchange.md`: failure of two
carriers gives the circle upper bound `|F|+6`, while planar Euler curvature
and `delta(G)>=7` give the lower bound `2|F|+6`.  This contradiction proves
that `Pi` reflects.  Exact attained-state gluing then six-colours `G`.
\(\square\)

## 3. Scope

The proof uses the exact paired state, a second disjoint full packet, the
one-sibling three-cut, and two duties whose two endpoint portal sets have
nonadjacent witnesses.  It closes both the isolated and concentrated gate
alternatives in the single-missing family.  It does not close an arbitrary
`(1,2)` adhesion, transport a state through a generic descended cell, or
resolve the packet vector `(1,1)`.
