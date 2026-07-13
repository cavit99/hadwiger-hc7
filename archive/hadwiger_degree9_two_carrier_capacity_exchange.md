# The degree-nine Moser lock: clean crosses and a two-carrier capacity exchange

## 1. Purpose and status

This note isolates what can, and what cannot, be deduced from the two
symmetric bypasses in the balanced degree-nine Moser lock.  It uses the
notation of `hadwiger_degree9_protected_portal_peel.md`:

\[
 L_6=K_L\mathbin{\dot\cup}D_L,
 \qquad R_5=K_R\mathbin{\dot\cup}D_R,
 \qquad 6\in D_L,\quad 5\in D_R .                \tag{1.1}
\]

The first result is the exact label-preserving uncrossing statement.  The
second result shows why the word *label-preserving* cannot be dropped.  The
last result gives a monotone capacity exchange in one of the two locked
left bags.  It continues through every intermediate exact seven-adhesion and
closes every such exchange except the already identified root-bearing
bottleneck lobe.  No assertion that an arbitrary exact seven-adhesion is
colour-gluable is made or needed here.

## 2. A clean crossed pair always closes

Retain the conservative quotient labels

\[
 U=K_L,\quad D=D_L,\quad V=K_R,\quad C=D_R,
 \quad L=L_0,\quad R=R_0.                         \tag{2.1}
\]

Thus (U,D,L) have the left contacts to (1,2), (V,C,R) have
the right contacts to (3,4), and the fixed bag adjacencies include

\[
 UD, VC, DC, UL, VR, DR, CL, LR .          \tag{2.2}
\]

### Theorem 2.1 (terminal-clean crossed paths)

Suppose there are a (U)-to-(C) path (P) and a (V)-to-(D)
path (Q) such that

* the interior of each path is disjoint from
  (U\cup D\cup V\cup C\cup L\cup R); and
* neither path has an endpoint or an internal vertex in either of the two
  terminal bags belonging to the other path.

The paths are not required to be disjoint.  Then (G) has a
(K_7)-minor.

#### Proof

If (P,Q) are vertex-disjoint, contract their interiors so that they
become the two extra adjacencies (UC) and (VD).  The quotient has a
(K_7)-model; one convenient model is obtained by taking the branch sets

\[
 \{v\},\ \{h\},\ \{1\},\ \{2\},\
 D\cup V,\ U\cup C,\ \{3\}\cup L\cup R.          \tag{2.3}
\]

The first two nonsingleton sets are connected by the new adjacencies;
the last is connected through the right-root--(3) edge and (LR).
The fixed adjacencies in (2.2), the edges (12,34), and the literal
contacts of (5,6,v,h) audit all other pairs.

Suppose instead that (P,Q) meet.  Reroute one path along the other
between consecutive common pieces until their intersection is one
connected subpath.  Each rerouting stays in (P\cup Q), keeps the four
terminal bags, and reduces the number of components of intersection.
The four portions outside the common subpath are then internally
disjoint terminal arms.  Contract the common subpath to one vertex (z)
and each arm to one edge.  The quotient therefore contains a vertex
adjacent to (U,C,V,D).  Now use

\[
 \{v\},\ \{h\},\ \{1\},\ \{2\},\
 C\cup L,\ D\cup R,\ \{3\}\cup U\cup V\cup\{z\}. \tag{2.4}
\]

The last branch set is connected through (z); its adjacencies to the
fifth and sixth sets use the (zC,zD) edges.  The remaining audit is the
same as for (2.3).  Undoing the preliminary contractions gives a
(K_7)-model in (G).  \(□\)

This theorem shows that intersection of the two bypasses is not the
obstruction.  The only possible obstruction is that a bypass consumes a
wrong labelled terminal bag or a protected helper core.

## 3. The unreserved assertion is false

The conservative twelve-vertex quotient in
`degree9_opposite_bypass_quotient_probe.py` has the two paths

\[
                         U-D-C,qquad V-C-D.       \tag{3.1}
\]

They have the required endpoint pairs, but each uses the other pair's
terminal bag.  The graph has no (K_7)-minor.  This does not rely only
on the exhaustive minor routine: the elimination order

\[
 U,1,2,V,3,4,v,h,D,C,L,R                         \tag{3.2}
\]

has filled later-neighbour bags

\[
\begin{array}{c|l}
U&U,1,2,D,L,h\\
1&1,2,D,L,h,v\\
V&V,3,4,C,R,h\\
3&3,4,C,R,h,v\\
v&v,h,D,C,L,R
\end{array}                                      \tag{3.3}
\]

and every later bag is smaller.  Hence this is a chordal completion with
clique number at most six, so the quotient has treewidth at most five and
cannot contain (K_7) as a minor.

Consequently, the statement

> two opposite bypass paths, without reserved terminal labels, force
> (K_7)

is false.  Any valid uncrossing theorem must preserve the four terminal
bags (and, in the spanning model, enough of the ordinary bags (L,R)).

## 4. A one-carrier capacity exchange

We next record the operation that can make a bypass terminal-clean.  It
is useful independently of the Moser labels.

### Lemma 4.1 (two target classes or one bottleneck)

Let (T) be connected and let (A,B_0,B_1\subseteq V(T)), where
(|A|\ge2) and (B_0,B_1) are nonempty.  Exactly one of the following
holds:

1. there are two vertex-disjoint paths, from distinct vertices of (A),
   one ending in (B_0) and the other in (B_1), at distinct terminal
   vertices;
2. one vertex (r\in V(T)) meets every path from (A) to
   (B_0\cup B_1).

In outcome 1 the two paths extend to a connected bipartition
(T=X\mathbin{\dot\cup}Y) with both sides meeting (A), one side
meeting (B_0), and the other meeting (B_1).

#### Proof

The linkable subsets of (B_0\cup B_1) form the strict gammoid with
sink set (A).  If no pair with one member in each target class is
independent, all nonloop elements of the two classes are parallel; hence
the gammoid has rank one on their union.  Vertex Menger gives the common
one-vertex transversal.  If the pair exists, contract the two disjoint
paths to two distinct prescribed vertices, take a spanning tree, and delete
an edge on the unique tree path between those vertices.  Undoing the
contractions, and assigning every remaining tree component to its side,
gives the stated connected bipartition.  \(□\)

### Lemma 4.2 (absorption after a bottleneck)

Let (W,T,T') be pairwise disjoint connected sets.  Put
(A=N_T(W)), and suppose (r\in T) meets every
(A)-to-(B) path in (T), where (B\subseteq T).  Let
\(\mathcal C\) be the components of (T-r) which meet
(A-\{r\}), and put

\[
 W^+=W\cup\bigcup_{C\in\mathcal C}C,qquad
 T^+=T-\bigcup_{C\in\mathcal C}C.                \tag{4.1}
\]

Then (W^+,T^+) are connected, (B\subseteq T^+\cup\{r}), and

\[
                         N_T(W^+)\subseteq\{r\}. \tag{4.2}
\]

If every component in (\mathcal C) is disjoint from a prescribed external portal
class, absorption introduces no contact with that class.

#### Proof

Every absorbed component contains a neighbour of (W), so (W^+) is
connected.  The set (T^+) consists of (r) and all unabsorbed
components of (T-r), and is connected.  A component meeting both
(A) and (B) would contain an (A)-to-(B) path avoiding (r), so
no member of (B-\{r\}) is absorbed.  Distinct components of (T-r)
have no edge between them, proving (4.2).  The last statement is
immediate.  \(□\)

## 5. Application to the transferred left lock

Assume the same-bag alternative

\[
                         K_L\not\sim R_5,R_0                 \tag{5.1}
\]

and the non-root-bearing outcome of Theorem 4.7 in
`hadwiger_degree9_protected_portal_peel.md`.  Thus the (K_L)-portal
lobes in (L_0-q) can be absorbed into a connected set (W), and with

\[
 D=D_L,qquad Q=L_0-(W-K_L),qquad F=\{h,1,2,6\},             \tag{5.2}
\]

we have

\[
 N_G(W)=F\mathbin{\dot\cup}\{q\}
            \mathbin{\dot\cup}A_D,qquad A_D\subseteq D-\{6\}. \tag{5.3}
\]

The sets (D,Q) are connected, (6\in D), and the left root of
(L_0) lies in (Q).  Moreover (Q) retains portals to both
(R_5,R_0), while (D) retains a portal to (R_0); the edge (65)
is a (D)-to-(R_5) contact.

For a current carrier (T\in\{D,Q\}), call

\[
 B_i(T)=N_T(R_i)\quad(i=5,0)                                \tag{5.4}

\]

its two right target classes.  If (T=D), interpret (R_5) literally,
so (6\in B_5(D)).  Every target class which has already been protected
by a bottleneck remains nonempty.

### Theorem 5.1 (alternating capacity exchange)

Starting from (5.3), repeated application of Lemma 4.1 and Lemma 4.2
has one of the following outcomes:

1. (G) has a (K_7)-minor;
2. in the current ordinary left carrier (Q^*) there is a vertex (s)
   and a component (J) of (Q^*-s) which contains the left root and
   every current (Z)-portal into (Q^*) other than possibly (s), while
   containing no portal to (R_5\cup R_0).

Outcome 2 is exactly a root-bearing bottleneck lobe.  In particular, if
this lobe is excluded, the transferred two-carrier lock ends in outcome
1 after finitely many exchanges.

#### Proof

We maintain disjoint connected sets (Z,D^*,Q^*), initially
(W,D,Q).  Put

\[
 A_D(Z)=N_{D^*}(Z)-\{6\},\qquad
 A_Q(Z)=N_{Q^*}(Z).                                      \tag{5.4a}
\]

At every stage exactly one of these two sets is the **active** portal
set (A), while the other carrier is **inactive**.  The invariant is:

* (Z) contains the root of (L_6), while (6\in D^*);
* (Z) has no contact to (R_5,R_0,3,4);
* (D^*) retains its (R_0)-portal and the edge from (6) to (5);
* (Q^*) retains portals to both (R_5,R_0); and
* if (D^*) is inactive, then
  \(N_{D^*}(Z)=\{6\}\) or
  \(N_{D^*}(Z)=\{6,c\}\) for one vertex (c\ne6); if (Q^*) is
  inactive, then \(N_{Q^*}(Z)=\{c\}\) for one vertex (c);
* the active set (A) is precisely (A_D(Z)) or (A_Q(Z)), as
  appropriate, and has at least two vertices;
* the left root remains in (Q^*).

Equivalently, with (F=\{h,1,2,6\}), the neighbourhood of (Z) is the
disjoint union

\[
       N_G(Z)=F\mathbin{\dot\cup}C
                   \mathbin{\dot\cup}A,                    \tag{5.4b}
\]

where (C) is empty or a singleton in the inactive carrier.  The empty
case occurs only when that carrier is (D^*) and its only contact with
(Z) is the already counted fixed vertex (6).

These assertions hold initially by (5.3) and Theorem 4.7: (D) is
active, (A=A_D(W)), and (C=\{q\}).  Seven-connectivity and (5.4b)
give

\[
 |A|\ge
 \begin{cases}
  3,&C=\varnothing,\\
  2,&|C|=1.
 \end{cases}                                               \tag{5.4c}
\]

Thus even when (|N_G(Z)|=7), the active carrier supplies the two
distinct sources required by Lemma 4.1 (and it supplies three when the
inactive contact is only the fixed vertex (6)).

Apply Lemma 4.1 in the active carrier (T), with the active source set
(A) from (5.4a) and the two target classes (B_5(T),B_0(T)).  In outcome
1, extend the two paths to a connected bipartition (T=X\dot\cup Y),
where both (X,Y) see (Z), and the two sides meet different right
target classes.

First let (T=Q^*) and name the root-containing side (Y).  If
(X\sim R_5) and (Y\sim R_0), use

\[
 \{h\},\{1\},\{2\},\ Z,\ Y,
 D^*\cup R_0,\ \{v\}\cup X\cup R_5.             \tag{5.5}
\]

If (X\sim R_0) and (Y\sim R_5), use

\[
 \{h\},\{1\},\{2\},\ Z,\ Y,
 D^*\cup R_5,\ \{v,3\}\cup X\cup R_0.          \tag{5.6}
\]

The last set in (5.5) is connected through the (X)-(R_5) contact and
(v5); the last set in (5.6) is connected through the (X)-(R_0)
contact, the right-root--(3) edge, and (3v).  The sets (Z) and (Y)
are adjacent to both remaining large sets through the source and mixed
target contacts.

Now let (T=D^*) and name the side containing (6) by (Y).  If
(X\sim R_5) and (Y\sim R_0), use

\[
 \{h,3,4\},\ \{v\}\cup R_5,\ \{1\},\ \{2\},
 Z\cup X,\ Y\cup R_0,\ Q^*.                     \tag{5.7}
\]

If (X\sim R_0) and (Y\sim R_5), use

\[
 \{h\},\{1\},\{2\},\ Z,\ Q^*,
 \{3\}\cup Y\cup R_5,
 \{v,4\}\cup X\cup R_0.                        \tag{5.8}
\]

The fixed rooted-model adjacencies, (56), and the fact that both sides
meet (N_T(Z)) audit all pairs in (5.5)--(5.8).  Thus the linkage
outcome is outcome 1 of the theorem.  The dependency-free checker
`degree9_two_carrier_mixed_split_verify.py` independently audits every
branch-set connectivity and all twenty-one adjacencies in these four
models (and in (5.9) below).

Suppose Lemma 4.1 gives a bottleneck (r\in T).  Call a component of
(T-r) a **source component** if it meets (A-\{r\}).  There is at
least one source component, because (|A|\ge2).  No source component
meets (B_5(T)\cup B_0(T)): otherwise a path inside that component
from a source to a target avoids (r).

If (T=Q^*), (r) is not the left root, and the component (J) of
(Q^*-r) containing the left root is a source component, first apply
the cross-contact model (5.9)
below if another source component has a (3)- or (4)-contact, and
otherwise absorb all the other source components.  The lobe (J)
contains no right target portal, and it then contains every remaining
(Z)-portal into (Q^*) other than possibly (r).  This is outcome 2.
Thus, outside outcome 2, the root lies in no source component.  Absorb
all source components of (T-r), obtaining (Z^+) and the connected
remainder (T^+).

No absorbed component contains a right portal, by the bottleneck
property.  A component with a (3)- or (4)-contact gives the explicit
cross-half model.  For example, from a (3)-contact use

\[
 \{v\},\{h\},\{1\},\{2\},\ Z^+\cup\{3\},
 D^+\cup R_5,\ \{4\}\cup Q^+\cup R_0,            \tag{5.9}
\]

where (D^+,Q^+) denote the two connected carrier remainders after the
absorption.  Thus in the minor-free residue no absorbed component has
such a contact.
The degree-nine hypothesis says that the only (h)-neighbour in (D^*)
or (Q^*) is the protected exterior root; it was not absorbed, so no new
(h)-contact is created.  Hence no neighbour of (Z^+) lies outside
(F), the two carrier remainders, and (r).

The contact with the old active carrier is exactly

\[
 N_{T^+}(Z^+)=
 \begin{cases}
  \{r\},&T=Q^*,\\
  \{6\},&T=D^*\text{ and }r=6,\\
  \{6,r\},&T=D^*\text{ and }r\ne6.
 \end{cases}                                               \tag{5.10}
\]

Indeed, every source component has an edge to (r), and every old
active contact other than (6) and (r) was absorbed.  When (T=D^*),
the old edge from (Z) to (6) survives.  Moreover (6) is not absorbed,
because it is itself a member of (B_5(D^*)).  This explicitly accounts
for the fixed (6)-contact, which was deliberately excluded from the
active source set.

Let

\[
 A'=\bigl(N_G(Z^+)\cap\hbox{the other carrier}\bigr)-F.     \tag{5.11}
\]

The exact new boundary is the disjoint union

\[
 N_G(Z^+)=F\mathbin{\dot\cup}(\{r\}-F)
                 \mathbin{\dot\cup}A'.                     \tag{5.12}
\]

If (r=6), then (5.12) has order (4+|A'|), so
seven-connectivity gives (|A'|\ge3).  If (r\ne6), it has order
(5+|A'|), so (|A'|\ge2).  This is precisely the invariant with the
roles of the carriers exchanged: the old active carrier is now inactive,
and the other carrier is active with source set (A').  Notice in
particular that equality (|N_G(Z^+)|=7) gives three new sources when
(r=6), and two new sources when (r\ne6); equality never stops the
exchange.

For clarity, the complete count audit is

\[
\begin{array}{c|c|c|c}
\text{old active carrier}&r&\text{new inactive contact}&
                  \text{new active lower bound}\\ \hline
Q^*&r\ne6&\{r\}&|A'|\ge2\\
D^*&r=6&\{6\}&|A'|\ge3\\
D^*&r\ne6&\{6,r\}&|A'|\ge2.
\end{array}                                                \tag{5.13}
\]

There is no fourth row: (6\notin Q^*).

Every bottleneck exchange which does not output outcome 2 strictly
enlarges (Z), including at equality.  At most one member of (A) is
(r), while (|A|\ge2); hence (A-\{r\}) is nonempty, so at least one
nonempty component of (T-r) is absorbed.  Since (D\cup Q) is finite,
infinitely many strict exchanges are impossible.  The process must
therefore end with the linkage outcome or the root-bearing lobe in
outcome 2.  \(□\)

### Corollary 5.2 (symmetric pair)

The same conclusion holds with

\[
 (1,2,6,L_6,L_0)\longleftrightarrow
 (3,4,5,R_5,R_0).
\]

Consequently, in a (K_7)-minor-free host every transferred lock must
terminate in its root-bearing bottleneck lobe.  If either side avoids
that lobe, the alternating exchange gives (K_7).

## 6. What remains

Theorem 5.1 is a genuine two-carrier exchange: it replaces an unbounded
sequence of portal placements by a monotone absorption and continues
through the exact seven-adhesion equality instead of stopping there.
The two symmetric bypasses therefore need no planar-web theorem and no
boundary-state gluing at these intermediate cuts.  The sole surviving
state is the single root-bearing bottleneck lobe (and its symmetric
mate).  Static width-five examples show that this last state is real
without minor-critical transition data.

More explicitly, in the sole terminal state the active carrier is
(Q^*).  There are a vertex (s\in Q^*) and a component (J) of
(Q^*-s) such that

\[
 e_0\in J,qquad N_{Q^*}(Z)\subseteq J\cup\{s\},qquad
 N_{Q^*}(Z)\cap J\ne\varnothing,                         \tag{6.1}
\]

where (e_0) is the ordinary-left exterior root, and

\[
                  J\cap N_{Q^*}(R_5\cup R_0)=\varnothing. \tag{6.2}
\]

Every other component of (Q^*-s) which met a (Z)-portal has already
been absorbed (or gave (K_7) through a (3,4)-contact).  Thus (J) is
the only obstruction to making the old active carrier have a single
contact: absorbing it would also absorb the unique spare left root.
The symmetric terminal state is obtained by interchanging the two
halves.  No intermediate exact seven-cut is terminal.

This makes the status of the earlier exact-cut notes precise.

* The exact cut (\{q,h,1,2,3,4,6\}) from Theorem 4.6 of
  `hadwiger_degree9_protected_portal_peel.md` is eliminated outright by
  `hadwiger_degree9_exact_cut_ordered_spine.md`; the parity obstruction
  in `hadwiger_degree9_exact7_parity_obstruction.md` is therefore no
  longer a live case.
* The equality rows in Theorem 4.7 of that note and Theorem 3.2 of
  `hadwiger_degree9_transferred_gate_split.md` remain correct separator
  descriptions, but they are obsolete as stopping alternatives.  They
  are successive capacity states of Theorem 5.1 and the exchange
  continues through them with two sources (or three when the bottleneck
  is the fixed vertex (6)).
* What is not obsolete is the root-ownership warning in Section 4 of
  `hadwiger_degree9_transferred_gate_split.md`: it is exactly the reason
  that the lobe (6.1)--(6.2), rather than an exact adhesion, survives.
