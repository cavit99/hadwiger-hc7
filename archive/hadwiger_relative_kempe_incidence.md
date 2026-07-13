# Relative Kempe incidence: repair or a two-rail web

## 1. Purpose

Ordinary D-reducibility does not preserve a fixed society state.  This
note isolates the exact obstruction to making one improving Kempe
change boundary-safe.

The resulting lemma is useful because it has only two outcomes:

1. the improving change can be completed to preserve the equality
   state on the society cycle; or
2. the configuration ring has two vertex-disjoint bichromatic tethers
   to the society boundary.

For many non-touching configurations, the second outcome concentrates
linearly many rings on one fixed pair of disjoint Kempe components.  In
a plane embedding this is a two-rail web.  An explicit family below
shows that this web outcome is real and that neither pairwise
non-touching nor linear abundance alone eliminates it.  The family has
a separator of order four, explaining why an ambient-connectivity or
portal-splitting hypothesis is indispensable.

Throughout, a *boundary state* means the equality partition of the
boundary vertices into colour classes.  Equivalently, labelled
colourings are considered modulo a global permutation of the four
colours.  This is the state relevant to colour gluing.

## 2. Completing one Kempe change

Let (phi) be a proper 4-colouring of a graph (H), let (C) be a
designated boundary, and let (R) be the ring of a deleted
configuration.  A Kempe change in the sense used by Inoue et al.
chooses a partition

\[
 {{1,2,3,4}}={{a,b},{c,d}}
\]

into complementary colour pairs and swaps any selected collection of
({a,b})-components and any selected collection of
({c,d})-components.

For one of the pairs (p\in\{ab,cd\}), let

\[
 {cal K}_p(C,R)
\]

be the set of (p)-coloured components which meet both (C) and
(R).  Record on each such component whether the proposed Kempe
change swaps it.

### Lemma 2.1 (boundary completion lemma)

For every Kempe change (sigma), at least one of the following holds.

1. There is another Kempe change (widehat\sigma), using the same
   complementary colour pairs, whose effect on (R) is identical to
   that of (sigma), and whose effect on (C) is a single global
   permutation of the four colour names.
2. For one colour pair (p), there are two distinct components
   (K_0,K_1\in{cal K}_p(C,R)) such that (sigma) swaps (K_1) and
   does not swap (K_0).

In the second outcome, (K_0) and (K_1) contain two vertex-disjoint
(R)-to-(C) paths.

#### Proof

Suppose outcome 2 does not hold.  Then, for each pair (p), the swap
indicator is constant on ({\cal K}_p(C,R)); call its value
(lambda_p\in\{0,1}).  If this set is empty, put
(lambda_p=0).

Define (widehat\sigma) as follows.  On every (p)-component which
meets (R) but not (C), use the same swap decision as (sigma).
On every (p)-component which meets (C), swap it if and only if
(lambda_p=1).  Decisions on components meeting neither set are
irrelevant and may be copied from (sigma).

Every (p)-component meeting both (R) and (C) retains its original
decision, by the definition of (lambda_p).  Every component meeting
(R) but not (C) also retains its decision.  Hence the restrictions
of (sigmaphi) and (widehat\sigmaphi) to (R) are identical.

On (C), either no (p)-component is swapped, or every (p)-component
which meets (C) is swapped.  The latter operation is precisely the
global transposition of the two colours in (p), restricted to (C).
Doing this independently for the complementary pairs changes the
colouring on (C) by

\[
 (a\ b)^{\lambda_{ab}}(c\ d)^{\lambda_{cd}},
\]

a global permutation.  This proves outcome 1.

If outcome 2 holds, each of the two distinct connected components
contains a path from (R) to (C), and the paths are vertex-disjoint
because the components are disjoint. \(\square\)

### Corollary 2.2 (one-component criterion)

If, for each colour pair (p), at most one (p)-component meets both
(R) and (C), then every improving Kempe change can be replaced by
one with the same ring effect and with boundary state unchanged.

This is stronger than merely saying that a particular Kempe chain
misses the boundary.  A boundary-reaching chain is harmless provided
all ring-to-boundary components of its colour pair are treated
uniformly.

## 3. Iterating through a D-reducibility certificate

The definition of D-reducibility is universal over the exterior plane
graph and over its current colouring.  Consequently Lemma 2.1 may be
iterated even though boundary completion changes colours far from the
ring.

### Theorem 3.1 (relative repair or split tethers)

Let (Z) be a D-reducible configuration of level at most (i), with
ring (R), in a plane society with boundary (C).  From every
4-colouring of the exterior (H=Q-V(Z)), one of the following can be
obtained.

1. In at most (i) improving Kempe changes, the ring becomes directly
   extendible across (Z), while the equality state on (C) is
   preserved throughout.
2. After fewer than (i) boundary-state-preserving improving changes,
   one reaches a colouring and a positive ring level (j) such that
   **every** improving change from that colouring has a split-tether
   obstruction: for one of its colour pairs, two distinct components
   meet both (R) and (C), and the change swaps exactly one of the
   two.

#### Proof

At a positive ring level, D-reducibility supplies at least one
improving Kempe change for the current exterior colouring.  If some
improving change avoids outcome 2 of Lemma 2.1, replace it by its
boundary completion.  Its restriction to (R) is unchanged, so it
still lowers the ring level, while its effect on (C) is a global
permutation and hence preserves the equality state.

Repeat.  The level falls at every step, so after at most (i) steps
the ring is 0-extendible, unless at some stage no improving change
admits boundary completion.  At the first such stage, every improving
change has the split-tether obstruction in Lemma 2.1(2). \(\square\)

If outcome 1 holds, extending through (Z) and finally applying the
inverse global colour permutation gives a colouring with the original
labelled boundary colouring.  Thus outcome 1 is exactly the
boundary-relative reduction required by minor-critical switching.

## 4. Many configurations at one fixed colouring

The preceding obstruction has a finite incidence type on a five-vertex
boundary.

### Lemma 4.1 (sixty-type incidence lemma)

Let ({\cal Z}) be (m) uncoloured, pairwise non-touching D-reducible
configurations whose rings are coloured by one common 4-colouring of
their exterior, and let (|C|=5).  Then at least one of the following
holds.

1. Some configuration is directly extendible, or has an improving
   Kempe change which can be completed without changing the boundary
   equality state.
2. At least (lceil m/60\rceil) configuration rings meet the same
   unordered pair (K_0,K_1) of distinct (p)-components which both
   meet (C), for one fixed colour pair (p).

#### Proof

Assume outcome 1 fails.  For every (Z\in{\cal Z}), its ring has
positive level.  Choose an improving Kempe change.  By Lemma 2.1, one
of its colour pairs (p) has two distinct components (K_0,K_1) which
both meet (C) and the ring of (Z), with different swap decisions.

There are six unordered pairs of colours.  For a fixed pair (p), at
most five distinct (p)-components meet (C), because distinct
components contain disjoint nonempty subsets of the five vertices of
(C).  Hence there are at most

\[
 6\binom 52=60
\]

choices for (p) and the unordered pair of (C)-meeting components.
The pigeonhole principle proves outcome 2. \(\square\)

The constant can be improved for a specified boundary colouring by
replacing 5 with the number of boundary vertices carrying one of the
two colours, but 60 is a uniform bound.

In outcome 2, (K_0) and (K_1) are disjoint connected rails, both
running from (C) to linearly many configuration rings.  This is the
precise web-like obstruction left by failure of relative repair.

## 5. The two-rail outcome is real

Neither linear abundance nor pairwise non-touching forces a
boundary-preserving occurrence.  The following planar family is an
exact parity obstruction.

Fix an odd integer (m\ge3).  Let

\[
 C=a,p,q,b,r,a
\]

be an induced outer 5-cycle.  Inside it, take the path

\[
 x_1,z_1,y_1,x_2,z_2,y_2,\ldots,x_m,z_m,y_m.       \tag{5.1}
\]

Join every vertex of (5.1) to both (a) and (b), but do not add the edge
(ab).  Equivalently, start with (K_{2,3m}) and add the path edges
in (5.1).  This is the standard two-rail plane strip, with (a,b) on
the outer face.  Add the three edges

\[
 px_1,\quad qx_1,\quad ry_m.
\]

The inside of (C) is now a triangulated disk: the path is a
triangulated strip between the two rails (a,b), the first side face
is triangulated through (p,q,x_1), and the last through (r,y_m).

For completeness, this can be made a sphere triangulation without
adding a chord of (C).  On the other side of (C), add vertices
(s,t), join (s) to (a,p,q,b), and join (t) to
(s,a,b,r).  Every face is then a triangle and (C) remains induced.
There are (3m+7) vertices and (9m+15=3(3m+7)-6) edges, confirming
that the displayed plane embedding is a sphere triangulation.

For each (i), the vertex (z_i) has precisely the four neighbours

\[
 a, x_i, b, y_i
\]

in cyclic order.  Hence every singleton (z_i) is a D1-reducible
degree-four configuration.  The (z_i) are pairwise non-touching.

Give (C) the colouring

\[
 psi(a),\psi(p),\psi(q),\psi(b),\psi(r)
   =1,4,1,2,3.                                     \tag{5.2}
\]

All vertices of the strip are adjacent to (a) and (b), so they can
use only colours 3 and 4.  The edge (px_1) forces (x_1=3), and the
edge (ry_m) forces (y_m=4).  In the spherical completion, (5.2)
extends to (s=3,t=4); these vertices impose no further condition on
the strip.

If (z_i) is present, it is colourable precisely when

\[
 x_i=y_i;
\]

then (z_i) takes the other colour in ({3,4}).  The path edge
(y_i x_{i+1}) forces

\[
 y_i\ne x_{i+1}.
\]

Thus, if all (z_i) are present, the equalities and inequalities
alternate along the strip.  Since (m) is odd, (x_1=3) forces
(y_m=3), contrary to (y_m=4).  Therefore

\[
 psi\notin\operatorname{Ext}(Q,C).                \tag{5.3}
\]

On deleting any one (z_i), the relation between (x_i) and (y_i)
disappears.  The left part of the strip can be propagated from
(x_1=3), the right part backwards from (y_m=4), and the two free
colours of (x_i,y_i) can be selected independently at the gap.  All
remaining (z_j) then receive the colour opposite to
(x_j=y_j).  Hence, for every (i),

\[
 psi\in\operatorname{Ext}(Q-z_i,C).               \tag{5.4}
\]

Consequently every one of the (m) pairwise non-touching D1
configurations strictly changes the full (C_5) extension set when
deleted.  There is no boundary-preserving occurrence among them.

This family also refutes the assertion that a linear number of
pairwise non-touching configurations must contain one far from a fixed
boundary.  Every (z_i) is adjacent to the two high-degree boundary
vertices (a,b).

The obstruction is exactly a two-rail web.  The rails (a,b) transmit
the two fixed colours, while the strip transmits a parity state.  It
also has an evident separator of order four: deleting

\[
 {a,b,x_1,y_m}
\]

separates the middle of a sufficiently long strip from (C).  Thus
the example does not refute a relative-occurrence-**or-small-separator**
theorem; rather, it proves that the separator alternative is necessary.

## 6. Plane order of a clean two-rail obstruction

The web conclusion can be made topological when the ring contacts are
disjoint.

### Lemma 6.1 (two-rail order lemma)

Let (A,B) be disjoint connected subgraphs in a closed disk.  Let
(W_1,\ldots,W_s) be pairwise vertex-disjoint connected subgraphs,
disjoint from (A\cup B), each adjacent to both (A) and (B).
After contracting (A,B) and the (W_i), the resulting embedded
(K_{2,s}) has opposite cyclic orders of the (s) two-edge paths at
its two branch vertices (up to reversal and ties caused by shared
attachment intervals).

In particular, failure of this order condition gives a crossing and
cannot occur in a plane society.

#### Proof

Choose in each (W_i), together with one edge to (A) and one edge to
(B), an (A)-to-(B) arc.  The interiors of these arcs are pairwise
disjoint.  Two disjoint arcs in a disk cannot have alternating ends on
the boundary of a regular neighbourhood of (A\cup B).  Applying this
to every pair gives the common linear order, reversed at the two ends.
Equivalently, this is the standard plane embedding order of parallel
paths in (K_{2,s}). \(\square\)

This lemma explains why the obstruction should be treated as an
ordered portal system rather than as more finite quotient cases.

## 7. Strongest plausible next theorem

### Lemma 7.1 (HC7 lift and five-fan constraint)

Let (G=L\cup_S M) be a proper separation of a 7-connected graph,
where

\[
 S=A\mathbin{\dot\cup}V(C),\qquad |A|=2,qquad C=C_5,
\]

and put (Q=L-A).  Assume (Q) is the plane society under
consideration.  Then the following hold.

1. No set of at most four vertices of (Q) separates a nonempty
   subset of (L-S) from (C).
2. Every vertex (v\in L-S) has a 5-fan to the five distinct vertices
   of (C) in (Q).

#### Proof

For (1), if (X\subseteq V(Q)) of order at most four separates a
nonempty set (D\subseteq L-S) from (C) inside (Q), then
(A\cup X) separates (D) from the nonempty open side (M-S) in
(G).  Its order is at most six, contrary to 7-connectivity.

For (2), apply the Fan Lemma in (G) to (v) and the seven-vertex set
(S).  There are seven internally disjoint paths from (v) to
distinct vertices of (S), hence one to every vertex of (S).
Truncate each path at its first vertex of (S).  Because (S) is the
adhesion, the truncated paths lie in (L).  Discard the two paths
ending in (A) and delete (A); the other five form the required
fan in (Q). \(\square\)

Thus a four-gate two-rail parity strip is killed immediately in the
actual HC7 cell.  Conversely, any surviving split-tether obstruction
must coexist with a 5-fan from every internal vertex to the (C_5).
The fan paths are not automatically disjoint from the two Kempe rails;
extracting three rail-avoiding spokes is precisely the remaining
linkage step.  Even without that extraction, the fan constraint is
substantially more rigid than the abstract parity-strip counterexample.

The same lift with (|A|=a) and ambient connectivity (kappa) rules
out a planar relative adhesion (X) whenever

\[
 |X|<\kappa-a.
\]

For HC7, (kappa=7,a=2), so the exact forbidden range is
(|X|\le4).  For general (t), present connectivity bounds need not
exceed the protected-clique cost (a); this is why this fan argument
is presently a sharp (t=7) tool rather than a uniform proof.

### Remaining portal theorem

The preceding results reduce the boundary-aware use of the 2026
reducibility theorem to a genuinely structural target.

> **Critical two-rail exclusion target.**  In a residual four-palette
> Moser (C_5) web inherited from a 7-connected contraction-critical
> graph, a pair of disjoint bichromatic components cannot both meet the
> society boundary and the rings of a long ordered family of
> non-touching reducible configurations.  Either a bounded set of rail
> portals lifts to a separator of the ambient graph of order at most
> six, or two distributed rail contacts split a shore and produce the
> required rooted minor.

The incidence lemma proves the input to this target.  The parity-strip
family proves that planarity, D-reducibility, and a (C_5) boundary are
insufficient without the ambient connectivity/minor-critical
hypotheses.  The remaining work is therefore no longer a reducibility
enumeration: it is a portal-distribution theorem for two coloured
rails.

## 8. Ambient connectivity still does not force a four-cut

There is a sharp counterexample to the purely topological strengthening

> repeated two-rail contacts plus the HC7 five-fan constraint force an
> adhesion of order at most four.

The counterexample is the concentric pentagonal disk already used in
the uniform web construction, now with an explicit periodic colouring
which preserves two rails through arbitrarily many layers.

Let

\[
 R_j=r^j_0r^j_1r^j_2r^j_3r^j_4r^j_0
 \qquad (0\le j\le L)
\]

be concentric 5-cycles, with (R_0=C).  Between (R_{j-1}) and
(R_j), add

\[
 r^{j-1}_i r^j_i,qquad r^{j-1}_i r^j_{i-1}
 \quad (i\in\mathbb Z_5).
\]

Finally add a hub adjacent to all vertices of (R_L).  This is a
triangulated pentagonal disk.

Take (L) divisible by 12 and colour successive rings by the following
periodic words, with positions indexed (0,1,2,3,4):

\[
\begin{array}{c|c|c|c}
j\pmod {12}&\text{word on }R_j&
 \text{positions on rail }K_0&\text{positions on rail }K_1\\ \hline
0 &01202&0,1&3\\
1 &20313&1&3\\
2 &12020&0,4&2\\
3 &03132&0&2\\
4 &12013&0&2,3\\
5 &03202&0&3\\
6 &10313&0,1&3\\
7 &31202&1&3\\
8 &03131&0,4&2\\
9 &12023&0&2\\
10&03102&0&2,3\\
11&12313&0&3
\end{array}                                          \tag{8.1}
\]

At (j=12), the word and the two position sets return to the row
(j=0).  Give the hub colour 3; the final word (01202) uses only
colours 0,1,2.

### Lemma 8.1 (periodic persistent rails)

The words in (8.1) give a proper 4-colouring of every such disk.  In
the subgraph induced by colours ({0,1}), the vertices listed in the
third column all belong to one component (K_0), those in the fourth
column all belong to a different component (K_1), and both
components meet every ring (R_j) and the boundary (C).

#### Proof

Each word is a proper colouring of a 5-cycle.  For each two consecutive
rows, direct inspection gives

\[
 \phi(r^{j-1}_i)\ne\phi(r^j_i),\qquad
 \phi(r^{j-1}_i)\ne\phi(r^j_{i-1})
 \quad(i\in\mathbb Z_5),
\]

so all annular edges are proper.  The last-to-first transition is the
same as the (j=11) to (j=0) transition, proving periodicity.

Now restrict each annulus to colours 0 and 1.  The annular edges join
the positions in the third column to the third column of the next row,
and similarly for the fourth column.  Within a row, consecutive listed
positions are joined when needed.  No 0--1 edge joins a third-column
position to a fourth-column position.  Induction through the twelve
rows proves that the two components persist, remain distinct, and meet
every ring. \(\square\)

There is no relative adhesion of order at most four separating an
inner ring from (C): the five column paths

\[
 r^L_i r^{L-1}_i\cdots r^0_i
 \qquad(i\in\mathbb Z_5)
\]

are pairwise vertex-disjoint.  On the other hand, each intermediate
(R_j) is a separator of order exactly five.  Thus the disk has the
precise nested-web geometry left open by Lemma 7.1.

Glue two copies along (C), and join a (K_2) completely to the
result.  As proved for the uniform pentagonal-web family, the resulting
graph is 7-connected; the adhesion is (K_2\cup C) of order seven.
Hence even the full ambient HC7 connectivity does not turn these two
rails into a planar four-cut.

This example is boundary-universal and 6-colourable, so it fails the
critical boundary minor-switching axiom.  It does **not** refute a
theorem which uses the selected-versus-unselected status in Lemma 2.1
for actual D-configurations.  It does refute any proof which discards
that information and attempts to derive the four-cut from two-rail
topology, non-touching, five-fans, and 7-connectivity alone.

The corrected closure target is therefore narrower:

> In a minor-switching-critical pentagonal web, a persistent pair of
> rails cannot support the *nonuniform swap decisions* forced by a
> linear family of D-reducibility certificates across nested
> 5-adhesions.

This is an exchange theorem about colouring states across a 5-sum, not
a planar separator theorem.
