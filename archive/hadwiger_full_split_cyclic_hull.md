# Cyclic hulls and full-split transitions at an order-seven adhesion

## 1. Why the conservative crossing quotient loses information

Let (G) be seven-connected and (K_7)-minor-free.  Let (S) be a
seven-vertex cut for which (G-S) has exactly two connected components
(D_1,D_2), each full to (S).  Put

\[
J=G[S],\qquad Q=\overline J.
\]

A crossed four-terminal society supplies two disjoint connected path
pieces, but contracting only those pieces forgets that the *whole shore*
is connected and full.  The following elementary extension restores that
information.

### Lemma 1.1 (connected full-split extension)

Let (D) be connected and let (X_0,Y_0\subseteq D) be disjoint,
nonempty, connected, and adjacent.  There is a partition

\[
D=X\mathbin{\dot\cup}Y
\]

such that (X,Y) are connected, adjacent, and contain (X_0,Y_0),
respectively.

#### Proof

Contract (X_0,Y_0) to adjacent vertices (x_0,y_0).  Choose a spanning
tree containing (x_0y_0), which is possible because every edge of a
connected graph belongs to a spanning tree.  Deleting that tree edge
gives two connected vertex sets.  Expanding the contractions gives the
required partition. \(\square\)

If (D) is full to (S), then

\[
N_S(X)\cup N_S(Y)=S.                              \tag{1.1}
\]

Thus a crossing carries a *covering contact pair*, not merely four
terminal incidences.

## 2. The partition crossing quotient

For (P\mathbin{\dot\cup}R=S), define
(Lambda(J;P,R)) from (J) by adjoining vertices (h,x,y), where

* (h) is complete to (S);
* (xy\in E);
* (N_S(x)=P) and (N_S(y)=R).

Extra incidences may be deleted, so it is enough to use a disjoint
partition of (S), even when the actual contact sets overlap.

Give (C=(c_0,\ldots,c_{m-1})\subseteq S), (m\ge4), a cyclic order
such that

\[
E(J[C])\subseteq
 \{c_ic_{i+1}:i\in\mathbb Z/m\mathbb Z\}.          \tag{2.1}
\]

Call this a **cyclic hull** when (J[S-C]) is bipartite.

### Theorem 2.1 (full-split web dichotomy)

Suppose (C) is a cyclic hull.  For every alternating four-tuple in
the cyclic order, let (A,B\subseteq C) be its two opposite pairs.
Assume that

\[
\eta(\Lambda(J;P,S-P))\ge7                         \tag{2.2}
\]

for every (P\subseteq S) with (A\subseteq P) and
(B\subseteq S-P), and also after interchanging (A,B).  Then

\[
G\text{ contains a }K_7\text{ minor, or }G\text{ is six-colourable}.
\]

Only (2^{7-4}=8) quotients occur for each oriented crossing.

#### Proof

If both shore societies are crossless, the two-shore web-gluing theorem
embeds (G-(S-C)) in the plane.  Four-colour that graph and colour the
bipartite graph (J[S-C]) from two new colours.  This six-colours (G).

Otherwise take a crossing in one shore.  Join its two path interiors by
a shortest connector and split that connector at an edge, obtaining
adjacent disjoint connected sets (X_0,Y_0) with the prescribed contacts
at (A,B).  Apply Lemma 1.1.  Put

\[
P_X=N_S(X),\qquad P_Y=N_S(Y).
\]

They cover (S) by (1.1).  Assign every vertex in their intersection to
one side, assigning (A) to (X) and (B) to (Y).  This gives a
partition (P\mathbin{\dot\cup}(S-P)=S) with

\[
A\subseteq P\subseteq P_X,\qquad
B\subseteq S-P\subseteq P_Y.
\]

Contract (X,Y) to (x,y), contract the opposite full shore to (h),
and delete surplus edges.  The result contains
(Lambda(J;P,S-P)).  Condition (2.2) therefore lifts a (K_7)-model to
(G). \(\square\)

### Corollary 2.2 (exact bad-split alternative)

Without (2.2), every crossing either gives a (K_7)-minor or yields an
actual connected bipartition (D=X\dot\cup Y) whose covering contact
pair contains a partition (P,S-P) with

\[
\eta(\Lambda(J;P,S-P))\le6.                        \tag{2.3}
\]

Thus the failure object is a finite **bad split** on the seven labels.
It is not an arbitrary unbounded routing failure.  In a six-minor-critical
graph, every label-preserving internal deletion or contraction on either
piece must additionally unlock a boundary state realized by the opposite
*full shore* and not by the original operated shore; this is the exact
minor-transition condition from the full-shore state theorem.

### Lemma 2.3 (tight-adhesion or surplus interface)

For an actual connected split (D=X\dot\cup Y), put

\[
P_X=N_S(X),\qquad T_X=N_Y(X).
\]

Then

\[
|P_X|+|T_X|\ge7.                                  \tag{2.4}
\]

If equality holds, (P_X\cup T_X) is another minimum seven-cut,
nested strictly inside the original (D)-side, and every component of
(G-(P_X\cup T_X)) is full to that cut.  The symmetric assertion holds
for (Y).

#### Proof

The set (P_X\cup T_X=N_G(X)) separates the nonempty set (X) from the
opposite shore, so seven-connectivity gives (2.4).  In the equality
case it is a minimum vertex cut.  Every component of a graph behind a
minimum cut is full to the cut: if a cut vertex missed one component,
deleting the other six cut vertices would still separate that component
from another component.  The cut is nested because (X\subsetneq D).
\(\square\)

This gives the structural exit from a bad split.  A tight side recurses
to a new minimum full-shore adhesion and is governed by the finite-state
depth theorem; a nontight side has a genuine surplus of internally
distinct interface vertices.  The remaining uniform problem is to turn
that surplus, together with the one-step state transition, into a further
split or a clique model.  It is no longer a question about the existence
of the original crossing.

## 3. A cyclic hull exists uniformly at the HC7 palette wall

The next lemma is a structural reduction from all seven-vertex boundary
graphs to one already-closed exceptional geometry.

### Lemma 3.1 (seven-vertex cyclic-hull lemma)

Let (Q) be a nonsplit graph on seven vertices, put (J=\overline Q),
and suppose

\[
J\vee\overline{K_2}
\quad\text{has no }K_7\text{ minor}.               \tag{3.1}
\]

Then either

1. (J) has a cyclic hull; or
2. (Q\cong2K_3\mathbin{\dot\cup}K_1).

#### Structural reduction

By Földes--Hammer, (Q) has an induced (2K_2,C_4), or (C_5).
An induced (C_5) is already a five-vertex cyclic hull.  For a
four-vertex core (R), its complement in (J[R]) is respectively a
(C_4) or two frame edges.  If the omitted triple (Z) is not a clique
in (J), this is already a cyclic hull.

It remains that (Q[Z]) is empty.  All remaining information is the
(4\times3) incidence matrix between (R) and (Z).  The following
finite matrix assertion completes the reduction:

> For (Q[R]\in\{2K_2,C_4\}), (Q[Z]=\overline K_3), every one of the
> (2^{12}) incidence matrices either makes
> (\overline Q\vee\overline K_2) contain a (K_7)-minor, supplies a
> cyclic hull, or (only when (Q[R]=2K_2)) makes
> (Q\cong2K_3\dot\cup K_1).

This is checked exactly by `order7_cyclic_hull_matrix_verify.py`.  The
program is not an enumeration of the 783 unlabelled survivors: it checks
the single label-free (4\times3) incidence lemma arising after the
Földes--Hammer reduction.  It uses the complete branch-set search on the
nine-vertex quotient and directly verifies condition (2.1) and
bipartiteness of the omitted set.  Its output is:

\[
\begin{array}{c|r|r|r|r}
Q[R]&\text{matrices}&K_7\text{-positive}&
       \text{negative with hull}&\text{exception}\\ \hline
2K_2&4096&1214&2876&6\\
C_4 &4096& 127&3969&0
\end{array}
\]

The six exceptional labelled matrices are exactly the permutations of
the three omitted vertices in (2K_3\dot\cup K_1).  This proves the
finite matrix assertion and the lemma. \(\square\)

## 4. Uniform routing consequence for an order-seven full-shore cut

### Theorem 4.1 (routing half of the order-seven obstruction)

Let (G) be seven-connected, six-minor-critical, and (K_7)-minor-free.
Let (S) be a seven-cut with exactly two connected full shores.  Then
there is a cyclic hull whose terminal tuple is crossed in at least one
shore.  Every such crossing either gives a (K_7)-minor or realizes a
bad split (2.3) together with the one-step minor-transition condition.

#### Proof

The exact-block theorem makes (Q=\overline{G[S]}) nonsplit.  Contracting
the two shores gives (3.1).  Lemma 3.1 supplies a cyclic hull unless
(Q=2K_3\dot\cup K_1).  That exceptional boundary is impossible by the
two-piece locality and opposite rooted-triangle theorem in
`hadwiger_k331_two_piece_closure.md`.

For a cyclic hull, if both shore tuples were crossless, web gluing would
six-colour (G).  Hence one shore is crossed.  Corollary 2.2 gives the
last assertion. \(\square\)

This theorem eliminates the unbounded *existence of routing* as the issue
at an arbitrary order-seven full-shore adhesion.  The remaining object is
uniform: a covering bad split on seven labels, constrained by exact
minor-critical state transitions.  No list of 783 boundary types remains
in the statement.

## 5. Audit of the general (k\le r) theorem

`hadwiger_minimum_adhesion_core_crossing.md` is correct as written.  If
(|S|=k\le r), every induced four-vertex Földes--Hammer core is crossed:
the omitted (k-4) vertices may each receive a fresh colour, giving at
most (4+k-4=k\le r) colours in the bilateral crossless case.  A
five-core uses at most (k-1) colours.

The hypothesis (k\le r) is essential to that formulation.  At the
HC7 palette wall, (k=7) and (r=6); an arbitrary four-core leaves
three vertices and only gives seven colours.  The cyclic-hull lemma above
is the precise repair: it chooses a frame whose omitted graph is
two-colourable, rather than charging one new colour per omitted vertex.

There is a concrete sharp obstruction to simply deleting the hypothesis.
Let (Q) be the house graph plus two isolated vertices.  It has exactly
one induced Földes--Hammer core, the four-cycle of the house.  The three
omitted vertices are independent in (Q), hence form a triangle in
(J), so the induced-core web argument uses seven colours.  Enlarging
that core by the roof vertex gives a five-vertex relaxed cyclic hull and
restores the six-colour alternative.  Thus “cyclic hull”, rather than
“induced core”, is the correct invariant at (k=r+1).
