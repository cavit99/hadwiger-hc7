# Protected-web absorption in a near-clique model

## 1. Label-free setting

Let \(t\ge 4\).  Suppose a graph \(G\) contains pairwise disjoint
connected bags

\[
 Q_1,\ldots,Q_{t-4},C,K,D_0,D_1.                 \tag{1.1}
\]

The \(Q_i\)'s form a clique model.  Every one of
\(C,K,D_0,D_1\) is adjacent to every \(Q_i\), and the last four bags
are pairwise adjacent except that the pair \(D_0D_1\) is not required.
Thus (1.1) is a \(K_t^-\)-model with deficient pair \(D_0D_1\).

For \(i=0,1\), put

\[
                         A_i=N_K(D_i).             \tag{1.2}
\]

Let \(W\subseteq K\) be connected, adjacent to \(C\), and adjacent to
every \(Q_i\).  We call \(W\) the protected core: any replacement of
the gate bag \(K\) by a connected set containing \(W\) retains all of
the gate's required non-shore adjacencies.

The theorem below isolates the reusable content of the degree-nine
dirty-connector exchange.  It has no Moser labels and works for every
target order \(t\).

## 2. The allocated split

### Lemma 2.1 (distributed gate capacity)

Assume \(|A_0|,|A_1|\ge2\).  Fix \(i\ne j\) in \(\{0,1\}\).  If
\(K=X\mathbin{\dot\cup}Y\) is a partition into nonempty connected
sets such that

\[
 X\sim D_i,D_j,\qquad W\subseteq Y,\qquad Y\sim D_j,       \tag{2.1}
\]

then \(G\) has a \(K_t\)-minor.

#### Proof

Keep the bags \(Q_1,\ldots,Q_{t-4}\) and use the four bags

\[
                         D_i\cup X,\quad D_j,\quad C,\quad Y. \tag{2.2}
\]

The first bag is connected through its \(D_iX\)-edge.  The four bags
in (2.2) form a clique: their six adjacencies are supplied by
\(XD_j,D_iC,XY,D_jC,YD_j,YC\), respectively.  The last edge uses
\(W\subseteq Y\) and \(W\sim C\).  Every bag in (2.2) sees every
\(Q_r\); for \(Y\) this again follows from the protected core.  Hence
these are \(t\) pairwise adjacent connected bags. \(\square\)

### Lemma 2.2 (two-target alternative)

Assume \(|A_0|,|A_1|\ge2\).  Fix \(i\ne j\), put

\[
 A=A_j,\qquad B=A_i,\qquad B'=B-V(W).
\]

At least one of the following holds.

1. \(G\) has a \(K_t\)-minor.
2. \(B'=\varnothing\).
3. A vertex \(s\in K-W\) meets every path in \(K\) from \(A\) to
   \(B'\cup W\), or \(W\) meets every \(A\)-\(B'\) path.

#### Proof

Assume \(B'\ne\varnothing\), contract \(W\) to a vertex \(w\), and
apply the two-target form of vertex Menger to the sink set given by the
image of \(A\), with target classes \(B'\) and \(\{w\}\).  If there
are two disjoint paths, one to each target class and starting at
distinct sink vertices, lift them.  Truncate one at its first vertex of
\(B'\) and the other at its first vertex of \(W\).  Their vertex sets
give disjoint connected sets \(X_0,Y_0\), where

\[
 X_0\sim D_i,D_j,\qquad W\subseteq Y_0,
 \qquad Y_0\sim D_j.                                \tag{2.3}
\]

Contract \(X_0,Y_0\), choose a spanning tree of the resulting connected
graph, and delete one edge on the tree path between the two contracted
vertices.  Lifting the two tree components gives a connected
bipartition \(K=X\dot\cup Y\) extending (2.3); the deleted tree edge
also gives \(XY\ne\varnothing\).  Lemma 2.1 gives a \(K_t\)-minor.

Paths of order one are allowed when a sink is itself a target.  Every
member of \(B'\cup\{w\}\) is a nonloop of the resulting strict
gammoid because \(K/W\) is connected.  If the two paths do not exist,
each member of \(B'\) is parallel to \(w\), so their union has rank
one.  The rank-one case of vertex Menger therefore gives a one-vertex
transversal after \(W\) is contracted.  A transversal other than \(w\)
lifts to the displayed vertex \(s\); the transversal \(w\) says exactly
that every \(A\)-\(B'\) path meets \(W\). \(\square\)

The last use of Menger is only a two-target statement.  It does not
assert arbitrary linkedness of \(K\).

## 3. Absorption of the entire path-bridge web

### Theorem 3.1 (protected-web absorption)

Assume that \(G\) has no \(K_t\)-minor, that \(K\) is two-connected,
that \(|A_0|,|A_1|\ge2\), and that \(|W|\ge2\).  Then every component
\(U\) of \(K-W\) is portal-pure: it meets at most one of
\(A_0,A_1\).

Moreover one may remove \(U\) from \(K\), discarding it if it has no
shore portal and otherwise absorbing it into its unique shore.  The
result is another model of the form (1.1), with the same protected core
and deficient pair.  The new gate is connected and retains at least two
portals to each shore, unless it is no longer two-connected.

Consequently all components of \(K-W\) can be consumed in finitely
many label-preserving exchanges while the gate remains two-connected.
The process ends either with a non-two-connected gate or with the gate
equal to \(W\).

#### Proof

Apply Lemma 2.2 in both orientations.  A singleton transversal
\(s\notin W\) is impossible: choose \(a\in A-s\), which is possible
because \(|A|\ge2\), and \(w\in W\).  The connected graph \(K-s\)
contains an \(a\)-\(w\) path avoiding \(s\).  Hence, for either
orientation, either the relevant portal class is contained in \(W\),
or \(W\) meets every path from the other class to an off-\(W\) member
of that class.  If neither class is contained in \(W\), a component of
\(K-W\) meeting both classes would contain such a path avoiding \(W\).
Thus every component is portal-pure in all cases.

Let \(U\) be one component.  Put \(K'=K-U\).  The graph \(K'\) is
connected because it contains \(W\), and every other component of
\(K-W\) attaches to \(W\).  If \(U\) is unlabelled, simply leave its
vertices unused.  If it has only \(D_i\)-portals, replace \(D_i\) by
\(D_i\cup U\).  This enlarged shore is connected and remains
anticomplete to \(D_j\): an edge from \(U\) to \(D_j\) would make
\(U\) meet \(A_j\), contrary to purity.

The component \(U\) has at least two distinct neighbours in \(W\).
Indeed, one neighbour \(x\) would make \(x\) a cutvertex separating
\(U\) from the nonempty set \(W-x\); here \(|W|\ge2\).  After an
absorption these two attachment vertices become two distinct portals
from \(K'\) to the enlarged shore.  The opposite portal class was
disjoint from \(U\), so its two old portals remain.  All adjacencies to
the \(Q_r\)'s and to \(C\) are retained by \(W\).

Whole components of \(K-W\) have no edges between them.  Thus the same
argument can be repeated with the fixed protected core, recomputing the
portal classes after each absorption.  Each step deletes vertices from
the gate, so the process is finite and has the asserted terminal form.
\(\square\)

### Corollary 3.2 (two-terminal normal form)

If \(W\) is an induced path, repeated absorption reaches a gate which
is not two-connected.  In particular, when \(W\) is a shortest path
between two distinct protected terminals, the terminal gate is a
singleton, a two-vertex bag, or has a cutvertex.

#### Proof

If the process never lost two-connectivity before all off-path
components were consumed, the terminal gate would be exactly the
induced path \(W\), which is not two-connected. \(\square\)

## 4. What remains at a cutvertex

The cutvertex endpoint also has a label-free normal form.  It explains
precisely where two units of portal capacity can collapse to one.

### Theorem 4.1 (portal-owner lobe normal form)

Retain (1.1)--(1.2), assume \(|A_0|,|A_1|\ge2\), and let \(q\) be a
cutvertex of the connected gate \(K\).  Let \(P\) be the union of
\(\{q\}\) and all components of \(K-q\) meeting the protected core
\(W\).  Then \(P\) is connected and contains \(W\).

By label-preserving absorptions, one can remove every component
\(U\) of \(K-q\) disjoint from \(W\), except for one of the following
two terminal configurations:

1. one mixed lobe \(U\) contains every portal in \(A_0\cup A_1\),
   and \(q\notin A_0\cup A_1\); or
2. there are at most two labelled lobes, each portal-pure, with at most
   one lobe for each label \(i\), and its class satisfies
   \[
                  A_i\subseteq U_i\cup\{q\}.       \tag{4.1}
   \]

Every other nonprotected lobe is either discarded or absorbed into its
unique shore.  Unless \(G\) already has a \(K_t\)-minor, these are the
only ways in which the two-portal hypothesis can fail to survive the
absorption.

#### Proof

The set \(P\) is connected because every component of \(K-q\) which it
contains is adjacent to \(q\).  Let \(U\) be any other component and
put \(Y=K-U\).  Both \(U\) and \(Y\) are connected and adjacent.

If \(U\) contains portals of both labels and \(Y\) contains a portal of
either label, orient Lemma 2.1 so that the latter label is the repeated
one, and take \(X=U\).  This gives a \(K_t\)-minor.  Hence in a
\(K_t\)-minor-free graph every mixed lobe contains all portals of both
labels; in particular \(q\), which belongs to \(Y\), has neither
label.  No other lobe is then labelled.  This is outcome 1.

Suppose instead that \(U\) is pure of label \(i\).  If
\(A_i-U\) contains a vertex other than \(q\), absorb \(U\) into
\(D_i\).  The enlarged shore is connected and remains anticomplete to
\(D_{1-i}\).  The edge from \(q\) into \(U\) makes \(q\) a new
\(D_i\)-portal, while the portal in \(A_i-(U\cup\{q\})\) supplies a
second distinct one.  The other label is disjoint from \(U\), so its
two portals remain.  Thus all hypotheses are preserved and the gate
strictly shrinks.  An unlabelled lobe may simply be discarded.

The only pure lobe which cannot be absorbed by this argument satisfies
(4.1); call it an \(i\)-owner.  Two distinct \(i\)-owners cannot
coexist, because each would have to contain every \(i\)-portal outside
\(q\).  There are only two labels.  Repeating the preceding operations
therefore leaves at most the two owner lobes in outcome 2. \(\square\)

This theorem is an actual termination statement.  It does not call a
portal-owner lobe a contradiction: such a lobe is the operation-level
state on which contraction-critical colouring information must act.

### Corollary 4.2 (capacity-one terminal form)

If retaining two distinct portals is no longer required, every pure
owner lobe in outcome 2 of Theorem 4.1 can also be absorbed.  The gate
then retains its adjacency to that shore only through the cutvertex
\(q\).  Therefore all nonprotected lobes can be consumed unless one
mixed lobe owns both portal classes while the protected side has neither.

#### Proof

For a pure owner \(U_i\), replace \(D_i\) by \(D_i\cup U_i\) and
replace \(K\) by \(K-U_i\).  The two sets remain connected, the
deficient pair remains anticomplete, and the edge from \(q\) into
\(U_i\) retains the required \(KD_i\)-adjacency.  What may be lost is
only a second distinct \(D_i\)-portal in \(K\).  The absorption can be
performed independently for the two labels.  A mixed owner cannot be
absorbed into either shore without creating the deficient
\(D_0D_1\)-edge through its contacts to the other shore. \(\square\)

## 5. Scope

Theorems 3.1 and 4.1 eliminate every crossing, nested, or laminar bridge web
outside a protected core.  It is a genuine all-\(t\) model-surgery
lemma, but it does not prove Hadwiger's conjecture: portal capacity may
collapse at a cutvertex, and a protected core with more than two
terminals need not be an induced path.  Those are operation-level
critical states, not further bridge-order cases.
