# The later degree-nine adhesion: mixed carrier or literal six-bottleneck

## 1. Setting

This note addresses the exact equality produced by Theorem 4.7 of
`hadwiger_degree9_protected_portal_peel.md`, rather than the original
cut eliminated in `hadwiger_degree9_exact_cut_ordered_spine.md`.

Thus (W) is connected and

\[
 N_G(W)=\{h,1,2,6,q,d_1,d_2\},                 \tag{1.1}
\]

where (d_1,d_2\in D-{6\}), (D=L_6-K) is connected and contains
(6), and (Q=L_0-(W-K)) is connected, contains the ordinary-left
root, and retains edges to both (R_5,R_0).  The set (W) contains
the (L_6)-root and the absorbed (L_0-q) lobes.  In particular

\[
 W\sim q,6,d_1,d_2.                              \tag{1.2}
\]

The old rooted model also gives nonempty portal classes

\[
 B_5=N_D(R_5),\qquad B_0=N_D(R_0).              \tag{1.3}
\]

The edge (65) says (6\in B_5).

## 2. Mixed right-carrier linkage closes

### Theorem 2.1

If (D) has a connected bipartition

\[
                         D=X\mathbin{\dot\cup}Y              \tag{2.1}
\]

such that both sides meet ({6,d_1,d_2\}), the two sides meet
different target classes (B_5,B_0), and (6\in X), then (G)
contains a (K_7)-minor.

#### Proof

If (X\sim R_5) and (Y\sim R_0), use

\[
 \{h\},\ \{1\},\ \{2\},\ W,\ Q\cup\{q\},
 X\cup R_5,\ \{v,3\}\cup Y\cup R_0.             \tag{2.2}
\]

The last set is connected through the (Y)-(R_0) contact, the
right-root--(3) edge, and (3v).  The sixth is connected through
the (X)-(R_5) contact.  The four large sets after the first three
form a clique:

* (W) sees (Q\cup\{q\}) through (q), sees (X) through (6),
  and sees (Y) through whichever of (d_1,d_2) lies in (Y);
* (Q\cup\{q\}) sees the last two through its old right contacts;
* the last two see each other through (R_5R_0).

Their contacts to (h,1,2) come respectively from the two left roots,
from (6), and from (v) and the right roots.  Thus (2.2) is a
(K_7)-model.

If (X\sim R_0) and (Y\sim R_5), interchange (R_5,R_0) in the
last two branch sets:

\[
 \{h\},\ \{1\},\ \{2\},\ W,\ Q\cup\{q\},
 X\cup R_0,\ \{v,3\}\cup Y\cup R_5.             \tag{2.3}
\]

The same audit applies.  \(□\)

### Corollary 2.2 (the only linkage failure is at (6))

If (G) has no (K_7)-minor, then the vertex (6) meets every path
in (D) from ({6,d_1,d_2\}) to (B_5\cup B_0).  Equivalently,
every path in (D) from (d_1) or (d_2) to either right portal
class contains (6).

#### Proof

Apply the flexible two-target lemma (Lemma 4.1 of
`hadwiger_degree9_two_carrier_capacity_exchange.md`) in (D), with
source set ({6,d_1,d_2\}) and target classes (B_5,B_0).
Its linkage outcome extends to the bipartition in Theorem 2.1.  In the
other outcome one vertex (r) meets every source-to-target path.  Since
(6\in B_5) and the order-one path at (6) is allowed, necessarily
(r=6).  \(□\)

This is stronger than a generic web obstruction: the common bottleneck
is a prescribed literal boundary vertex.

## 3. Absorbing the six-bottleneck

Let ({C_i\}) be the components of (D-6) which meet
({d_1,d_2\}), and put

\[
 U=W\cup\bigcup_i C_i,
 \qquad D_0=D-\bigcup_i C_i.                    \tag{3.1}
\]

Both (U,D_0) are connected, (6\in D_0), and (W6) makes them
adjacent.  Corollary 2.2 says no (C_i) has a portal to either right
bag.

### Lemma 3.1 (a cross-literal contact closes)

If (U\sim3) or (U\sim4), then (G) contains a (K_7)-minor.

#### Proof

From a (U)-(3) contact use

\[
 \{v\},\{h\},\{1\},\{2\},\ U\cup\{3\},
 D_0\cup R_5,\ \{4,q\}\cup Q\cup R_0.           \tag{3.2}
\]

The last set is connected through (qQ), the old (QR_0) edge, and
the right-root--(4) edge.  The sixth is connected through (65).
The last three are pairwise adjacent through (U6), (34), and an
old right/ordinary-bag edge.  Their contacts to the first four sets use
the left root in (U), the vertex (6), the root in (Q), and (v).
The (4)-case is symmetric.  \(□\)

### Theorem 3.2 (exact transfer to the ordinary carrier)

Assume (G) has no (K_7)-minor and put

\[
                         P_Q=N_{Q-\{q\}}(U).                 \tag{3.3}
\]

Then

\[
 N_G(U)=\{h,1,2,6,q\}\mathbin{\dot\cup}P_Q.     \tag{3.4}
\]

Consequently (|P_Q|\ge2).  Equality gives an exact seven-cut;
outside that outcome (|P_Q|\ge3).

#### Proof

Absorption removes (d_1,d_2) from the boundary.  Components of
(D-6) leave (D) only through (6).  Corollary 2.2 excludes right
contacts, and Lemma 3.1 excludes contacts to (3,4).  The bag (D)
contains no exterior (h)-root; (v) has no neighbour there.  The
spanning four-bag model therefore leaves only the displayed fixed
vertices and contacts into (Q).  Conversely, (U) sees
(h,1,2,6,q) by construction, proving (3.4).

It is a genuine separator with (v,R_5,R_0) on the far side.
Here (q\notin P_Q) by definition, so the union in (3.4) is disjoint.
Seven-connectivity gives (5+|P_Q|\ge7).  Equality is exactly order
seven, and otherwise integrality gives the strict bound.  \(□\)

Thus the exact Theorem 4.7 adhesion does not disappear from carrier
ownership alone.  It either gives (K_7) by a mixed split or transfers
to at least two actual portals in the residual ordinary bag (Q).

### Corollary 3.3 (the equality is not a terminal state)

Feed the transferred state (3.4) into Theorem 5.1 of
`hadwiger_degree9_two_carrier_capacity_exchange.md`.  Its flexible
two-target operation remains valid when (|P_Q|=2).  Therefore repeated
carrier exchange gives (K_7) unless it terminates in a root-bearing
bottleneck lobe in (Q).  No colour-gluing assertion for the intermediate
exact adhesion is needed.

## 4. Sharp counterarchitecture retaining every old allocation

The transfer alternative is real at the static level.  Contract (W,Q)
and the right bags, retain (6,q,d_1,d_2), and use

\[
 D=G[\{6,d_1,d_2\}],\qquad
 E(D)=\{6d_1,6d_2\}.                            \tag{4.1}
\]

Make (6) carry both old (L_6)-to-right adjacencies and make (Q)
carry both old (L_0)-to-right adjacencies.  Inside the connected
ordinary bag introduce two distinct portal vertices (p_1,p_2), add

\[
                  d_1p_1,\ p_1Q,\qquad d_2p_2,\ p_2Q.        \tag{4.2}
\]

The old (L_6)-(L_0) adjacency is internal to the contracted set (W).
Keep the exact boundary (1.1) and all fixed Moser/root contacts.

Then deleting (1.1) leaves exactly the two components

\[
                         \{W\},\qquad
                         \{v,3,4,p_1,p_2,Q,R_5,R_0\},        \tag{4.3}
\]

and the far component is full to all seven boundary vertices.  All six
old pairwise rooted-model adjacencies are represented.  After absorbing
(d_1,d_2), the new boundary is exactly

\[
                     \{h,1,2,6,q,p_1,p_2\},                  \tag{4.4}
\]

so the equality case (|P_Q|=2) is realized with two distinct actual
portals.  Nevertheless the graph has treewidth at most five.  A
width-five elimination order is

\[
 q,p_1,p_2,d_1,d_2,3,4,W,1,2,v,h,6,Q,R_5,R_0.   \tag{4.5}
\]

`degree9_thm47_exact_counterarchitecture_verify.py` checks the exact
boundary, fullness of the far component, every displayed allocation,
and the width-five certificate.

Therefore no theorem based only on the exact cut and ownership of the
old rooted-model edges can force (K_7).  The remaining input must use
the placement of the two-or-more (P_Q)-portals inside (Q), or the
minor-critical colouring transitions.  This is precisely the next
capacity state in the alternating exchange, not a missing static edge.
