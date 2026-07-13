# Critical-web exchange: the wheel audit and the complete order-six pentagram cell

## 1. The correct boundary for the reserved connector

In the reserved-connector separation put

\[
 S=U\mathbin{\dot\cup}\{w\},\qquad |U|=5,
 \qquad L=S\mathbin{\dot\cup}\{a\}.
\]

The terminal (a) is not in the adhesion (S), but it must be retained
when a local extension family is used.  For a shore (D) on the
(a)-side write

\[
 P_D=G[D\cup L]
\]

and let \(\mathcal E_6(P_D,L)\) be the equality partitions of (L) into
at most six independent colour classes which extend to (P_D).

### Lemma 1.1 (universal terminal-side exclusion)

If every proper six-colour state of (G[L]) extends to (P_D), then (D)
cannot occur in a proper-minor-minimal non-six-colourable graph.

### Proof

Delete the nonempty set (D).  The resulting graph is a proper minor and
therefore has a six-colouring (c).  Its restriction to (L) is a proper
six-colour state, so it extends over (P_D).  Keep (c) outside (D) and
use the extension on (D\cup L).  Every edge leaving (D) ends in (L),
so the two colourings glue to a six-colouring of the original graph.

This argument retains (v,b), and the whole opposite side.  In particular,
the colour of (v), the equality or inequality of (a,b), and every
apex-star constraint are already respected by (c).  No assumption about
an abstract opposite-side family is needed. \(\square\)

This is the safe way to use the seven-label computation.  Treating only
(S) as the boundary would lose the terminal colour and would not justify
the apex-star gluing.

## 2. Exact audit of the static wheel counterexample

Use the wheel and labels from
`hadwiger_reserved_w_majority_counterexample.md`.  Thus (D) has rim
(l_0\ldots l_4) and hub (h); the five outer portal classes are the two
consecutive rim pairs; and (r,a) are complete to (D).  The fixed graph
on

\[
 L=\{q_0,q_1,q_2,w,q_4,r,a\}
\]

is exactly the one in that note.

The complete exact computation is:

* there are (41) equality partitions of (L) into at most six
  independent classes;
* all (41) extend across (P_D);
* on (S=L-\{a\}), all (24) proper equality states extend;
* deleting any of the (32) edges incident with (D) leaves all (41)
  states extendable;
* deleting any of the six vertices of (D) leaves all (41) states
  extendable; and
* no label-preserving contraction of an edge incident with (D) creates a
  state outside the original family (there is no such state).  The exact
  sizes of the contracted families, with multiplicity over the (32)
  incident edges, are

\[
\begin{array}{c|rrrrrrrrrrrrrrr}
|\mathcal E_6|&18&19&21&22&24&29&30&31&32&33&37&38&39&40&41\\ \hline
\text{multiplicity}&1&1&1&2&1&1&1&3&1&2&2&7&2&2&5.
\end{array}
\]

For the ten internal wheel edges, in the order printed by the verifier, the
contraction-family sizes are

\[
37,38,40,39,38,39,38,38,38,38.
\]

The exact backtracking replay is
`reserved_w_wheel_transition_probe.py`.  Its contraction routine keeps the
two ends as equal-coloured twins after deleting their common edge; this is
colour-equivalent to identifying them and correctly retains every boundary
edge.  It now checks all shore--boundary edges as well as the ten internal
edges.

### Corollary 2.1

No opposite-side extension family can make this wheel into a
minor-critical reserved-connector side.

### Proof

Its full (L=S\cup\{a\}) extension family is universal, so Lemma 1.1
applies.  Equivalently, the one-step transition requirement asks for a state
in

\[
 \mathcal E_6(P_D^\mu,L)-\mathcal E_6(P_D,L),
\]

but the second family is already the complete state universe. \(\square\)

This proves more than the earlier statement that the wheel fails a static
majority assertion: it cannot participate in *any* counterexample-derived
opposite-family architecture.

## 3. The smallest all-crossless pentagram web

We next impose the actual residual geometry rather than the single-frame
wheel geometry of Section 2.  Let (D) be a three-connected full relative
shore with (|D|=6), boundary (L=U\dot\cup\{w,a\}), and

\[
 |N_D(X)-X|+|N_L(X)|\ge7
 \tag{3.1}
\]

for every nonempty proper (X\subsetneq D).  Assume all five disjoint-edge
frames of the missing (C_5) on (U) are crossless.

### Lemma 3.1 (five-portal SDR)

The five portal classes (N_D(u)), (u\in U), have distinct
representatives.

### Proof

If Hall fails for (I\subseteq U), put

\[
 R=\bigcup_{u\in I}N_D(u),\qquad |R|<|I|.
\]

If (D-R\ne\varnothing), a component of (D-R) has external
neighbourhood contained in (R\cup(L-I)), of order at most

\[
 (|I|-1)+(7-|I|)=6,
\]

contrary to (3.1).  If (D=R), then (|D|\le4), contrary to
(|D|=6). \(\square\)

### Lemma 3.2 (forced wheel)

The common portal face is a 5-cycle and the sixth vertex is adjacent to
all five facial vertices.  Hence (D\cong W_5).

### Proof

The bare-web theorem puts every portal occurrence on a common face; in the
three-connected all-crossless cell the five frame faces agree.  Lemma 3.1
makes that face contain at least five distinct vertices.  If it contained
all six vertices, (D) would be a three-connected outerplanar graph, which
is impossible.  Thus its boundary is a 5-cycle (C), and the sixth vertex
is (h\notin C).

All edges other than those of (C) lie in the closed complementary disk.
The vertex (h) has at least three neighbours on (C).  If two consecutive
(h)-neighbours (p,q), in the cyclic order of (N_C(h)), enclose a
nonempty (pCq)-interval containing no (h)-neighbour, the Jordan cycle

\[
 hp\cup pCq\cup qh
\]

bounds a sector.  Every vertex in the open interval lies in that sector,
and an edge from it to the complementary sector would cross the Jordan
cycle.  Thus ({p,q}) separates the open interval from (h) and the
complementary interval, contrary to three-connectivity.  Hence there is no
gap between consecutive (h)-neighbours: (h) sees all five vertices of
(C).  The five spokes divide the complementary disk into triangular
sectors, so no chord of (C) can be drawn without crossing a spoke.  Hence
(D\cong W_5). \(\square\)

No (U)-portal occurs at the hub.  Portal coincidence on the rim must be
handled by the exact overlap lemma from
`hadwiger_moser_pentagram_curvature.md`; the simpler assertion that every
root profile has order at most two is false.  For a rim vertex (x), its
root profile is exactly one of:

1. a two-set which is an edge of the present graph
   (G[U]=\overline{C_5}); or
2. a triple lock
   
   \[
   \{i,i+1,i+3\},\qquad P_{i+3}=\{x\}.
   \tag{3.2}
   \]

The singleton cut inequality gives the complete row universe.  An ordinary
two-root row must see both (a,w).  A triple-lock row must see a nonempty
subset of ({a,w}).  The hub sees no root and must see both (a,w).

The remaining occurrence calculation is finite and exact.  There are five
ordinary row types and (5\cdot3) decorated triple-lock row types, hence 20
types at each rim position.  Enforce the singleton shield in (3.2), full
root attachment, all 62 inequalities (3.1), and absence of all five
linkages.  Of the 8,895 row systems surviving the elementary profile and
shield filters, exactly ten are all-crossless, and none contains a triple
lock.  They are the two orientations and five rotations of

\[
 02,03,13,14,24.                                  \tag{3.2}
\]

In particular each edge of the present (C_5=\overline{C_5}) occurs once,
and (a,w) are complete to (D).  The verifier
`pentagram_critical_web_fullprofile_probe.py` constructs the exact 20-type
universe and checks the shield condition.  It imports only the elementary
cut, linkage, and colouring routines from
`pentagram_critical_web_probe.py`, and prints

```text
row types 20 examined 8895 all-crossless 10 with triple lock 0
```

### Theorem 3.3 (order-six critical pentagram exclusion)

Every order-six three-connected all-crossless pentagram shore satisfying
(3.1) is boundary-universal on (L=S\cup\{a\}).  It therefore cannot occur
in a proper-minor-minimal counterexample.

### Proof

By Lemmas 3.1--3.2 and the full-profile calculation above, it is one of the
ten wheel incidence systems.
It is enough to take the sparsest allowed graph on (L): the pure-Moser
graph on (U), the fixed edges from (a) to its three Moser neighbours,
and no optional edge incident with (w).  Adding optional boundary edges
only removes boundary states from consideration.

For this sparse boundary there are exactly (111) independent equality
partitions into at most six classes.  Exact backtracking extends all (111)
over each of the ten incidence systems.  It also verifies that all (25)
decorated (T)-states are already present; every internal edge deletion
and every internal vertex deletion preserves the entire family; and no
internal contraction creates a new state.  This is replayed by
`pentagram_critical_web_fullprofile_probe.py`, whose imported transition
routine asserts all counts.

Thus the actual boundary extension family is universal, and Lemma 1.1
excludes the shore. \(\square\)

## 4. Exact scope

Theorem 3.3 is the first complete critical-exchange closure of the
three-connected all-crossless pentagram cell: the minimum permitted shore
order is impossible without appealing to a static branch-set majority.
It does not prove the same statement for arbitrary shore order.  At larger
order the common portal face may contain portal-free intervals and the
interior is a genuine four-colour canvas.  Proving that such a canvas has an
extension-preserving reduction, or that a reduction creates a missing
decorated (T)-state, remains the boundary-relative reducibility step.
