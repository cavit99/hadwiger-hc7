# The degree-nine Moser gate: eliminating the exact cut by root and carrier exchange

## 1. Setting

Retain the balanced degree-nine Moser lock and the same-bag alternative
of `hadwiger_degree9_protected_portal_peel.md`.  Thus

\[
 K=K_L\not\sim R_5,R_0,
\]

and (q\in L_0) meets every path in (L_0) from a (K)-portal to
an (R_5)- or (R_0)-portal.  Let (e_0) be the unique exterior
root in (L_0).  Suppose the exact-cut outcome of Theorem 4.6 occurs:

\[
 S=\{q,h,1,2,3,4,6\}=N_G(Z),                  \tag{1.1}
\]

where (Z) is the component of (G-S) containing (K).  Let (H)
be the component of (G-S) containing (v).

This note first proves that the exact cut is impossible unless the left
root lies on the (K)-side.  That intermediate residue is a literal
ordered-spine bottleneck forced to miss (v,h,1,2).  A two-bag root
exchange, followed by retaining the two old far-side carrier edges,
then eliminates the ordered spine as well.  Thus the exact-cut outcome
of Theorem 4.6 does not occur.

## 2. The rigid far-side frame

### Lemma 2.1

The whole bags (R_5,R_0) lie in (H).  Every component of
(L_0-q) containing an (R_5)- or (R_0)-portal also lies in
(H).

#### Proof

The connected bag (R_5) contains (5), and (v5\in E(G)), so
(R_5\subseteq H).  The connected bag (R_0) is adjacent to (R_5),
so (R_0\subseteq H).  A component of (L_0-q) containing a portal
to either right bag has an edge to (H) in (G-S), and hence belongs
to (H).  \(□\)

Fix an edge from (L_0) to (R_0), and let (x\in L_0) be its
left endpoint.  There is a connected subgraph (P_0\subseteq L_0)
such that

\[
 q,x\in P_0,\qquad P_0-q\subseteq H.             \tag{2.1}
\]

Indeed, if (x=q), take (P_0=\{q\}).  Otherwise the component of
(L_0-q) containing (x) lies in (H) by Lemma 2.1 and has an edge
to (q), since (L_0) is connected.

## 3. The root must lie on the locked side

### Theorem 3.1 (exact-cut root transfer)

If (e_0\notin Z), then (G) contains a (K_7)-minor.  Consequently,
every (K_7)-minor-free exact-cut residue satisfies

\[
                              e_0\in Z.           \tag{3.1}
\]

#### Proof

If (e_0=q), put (P=P_0).  Otherwise let (J) be the component of
(L_0-q) containing (e_0).  Since (e_0\notin Z), the set (J)
is disjoint from (Z).  It has an edge to (q), and therefore

\[
                         P=P_0\cup J\cup\{q\}
\]

is connected and disjoint from (Z) except for the boundary vertex
(q\notin Z).  It contains (e_0) and the endpoint (x) of an edge
to (R_0).

Use the seven branch sets

\[
 \{v\},\quad \{h\},\quad \{1\},\quad \{2\},\quad
 Z\cup\{3\},\quad R_5\cup\{6\},\quad
 R_0\cup P\cup\{4\}.                            \tag{3.2}
\]

They are disjoint and connected.  The fifth set is connected because
(Z\) is full to (S), the sixth through (65), and the last through
the (P)-to-(R_0) edge and the right-root--(4) edge.

The first four sets form a clique.  The fifth sees them through (3)
and the (Z)-contacts to (1,2); the sixth through (6), the root of
(R_5), and (5v); and the last through (4), the root (e_0), and
(4v).  The last three sets are pairwise adjacent through (Z6),
(34), and the old (R_5)-(R_0) adjacency.  Thus (3.2) is a
(K_7)-model.  \(□\)

This eliminates the entire non-root-bearing exact-cut family, for bags
of arbitrary order.

## 4. Literal restrictions on the bottleneck

### Theorem 4.1

In a (K_7)-minor-free exact-cut residue,

\[
                       N(q)\cap\{v,h,1,2\}=\varnothing .     \tag{4.1}
\]

#### Proof

The vertex (q\in L_0) is outside (N[v]), so (qv\notin E(G)).
By Theorem 3.1 the unique (h)-neighbour (e_0) in (L_0) lies in
(Z), whereas (q\in S); hence (q\ne e_0).  Since (d(h)=9) and
the four exterior neighbours of (h) are exactly the four rooted-model
roots, (qh\notin E(G)).

It remains to exclude (q1,q2).  Suppose (qi\in E(G)), where
(i\in\{1,2\}).  Use

\[
 \{v\},\quad\{h\},\quad\{3\},\quad\{4\},\quad R_5,
 \quad Z\cup\{6\},\quad R_0\cup P_0\cup\{i\}.   \tag{4.2}
\]

The last set is connected through (qi) and the (P_0)-to-(R_0)
edge.  The first four sets form a clique.  The bag (R_5) sees them
through (5) and its right root.  The sixth sees them through (6)
and the fullness of (Z).  The last sees them through (i), the
right root of (R_0), and sees the preceding two large bags through
the old (R_0R_5) adjacency and the (qZ) edge.  Thus (4.2) is a
(K_7)-model, a contradiction.  \(□\)

### Corollary 4.2 (ordered root spine)

Let (J) be the component of (L_0-q) containing (e_0).  Then

\[
 J\subseteq Z,                                               \tag{4.3}
\]

and every path in (L_0) from (J) to either right portal class meets
(q).  Thus the surviving exact-cut geometry has the literal order

\[
       e_0\in J\subseteq Z
       \quad--\quad q
       \quad--\quad
       \bigl(N_{L_0}(R_5)\cup N_{L_0}(R_0)\bigr)-\{q\}
       \subseteq H.                                           \tag{4.4}
\]

Moreover (q) is anticomplete to (v,h,1,2).

#### Proof

The path in (L_0-q) from (e_0) to every vertex of (J) lies in
(G-S), so (3.1) gives (J\subseteq Z).  Lemma 2.1 puts every right
portal component in (H).  A path in (L_0-q) between the two sides
would join distinct components (Z,H) of (G-S), which is impossible.
The final assertion is Theorem 4.1.  \(□\)

## 5. Root exchange or an exact portal-order separator

Let (J) be the root component from Corollary 4.2, and let (C) be
the component of (Z-J) containing (K).  The two left roots have now
been separated: (e_0\in J), while the root of (L_6) lies in
(K\subseteq C).

### Theorem 5.1 (two-bag root exchange)

If (C) has a neighbour in ({3,4}), then (G) contains a
(K_7)-minor.

#### Proof

Suppose that (C\sim3).  The connected sets (J,C) are disjoint.
By Lemma 4.1 of `hadwiger_degree9_protected_portal_peel.md`, extend
them to a connected bipartition

\[
                             Z=X\mathbin{\dot\cup}Y,          \tag{5.1}
\]

with (J\subseteq X) and (C\subseteq Y).  The set (X) contains
the root (e_0) and is adjacent to (q), while (Y) contains (K),
is adjacent to (3), and retains the (K)-contacts to (h,1,2,6).

Use

\[
 \{v\},\quad\{h\},\quad\{1\},\quad\{2\},\quad
 Y\cup\{3\},\quad R_5\cup\{6\},\quad
 R_0\cup P_0\cup X\cup\{4\}.                    \tag{5.2}
\]

The last set is connected through (Xq), (P_0R_0), and the
right-root--(4) edge.  Its contacts to (h,1,2) come from (e_0).
The fifth set obtains the same contacts from (K), and the sixth from
the root of (R_5) and the vertex (6).  The last three sets are
pairwise adjacent through (Y6), (34), and (R_5R_0).  This is a
(K_7)-model.  The case (C\sim4) is symmetric.  \(□\)

Thus the failure of root exchange has a precise separator form.

### Theorem 5.2 (portal-order separator)

In a (K_7)-minor-free exact-cut residue put

\[
 R=N_J(C),\qquad
 \varepsilon=
 \begin{cases}
 1,&C\sim q,\\
 0,&C\not\sim q.
 \end{cases}                                                \tag{5.3}
\]

Let (Q_C=\{q\}) when (C\sim q), and let
(Q_C=\varnothing) otherwise.  Then

\[
 N_G(C)=\{h,1,2,6\}\mathbin{\dot\cup}
       Q_C\mathbin{\dot\cup}R.                              \tag{5.4}
\]
Consequently

\[
 |R|\ge3-\varepsilon.                                      \tag{5.5}
\]

Equality in (5.5) makes (5.4) an exact seven-cut.  Outside that
outcome,

\[
 |R|\ge4-\varepsilon.                                      \tag{5.6}
\]

In particular, the root-exchange obstruction does not yield a surviving
cut of order at most six: such a cut would contradict seven-connectivity.

#### Proof

The set (C) is a component of (Z-J), so all its neighbours inside
(Z) lie in (R\subseteq J).  Since (Z) is a component of (G-S),
all remaining neighbours lie in (S).  Theorem 5.1 excludes contacts
to (3,4).  The component (C) contains (K), and hence sees each of
(h,1,2,6).  The only still optional member of (S) is (q).  This
proves the exact equality (5.4).

It is a genuine separator: (C\ne\varnothing), while (v) survives on
the other side.  Seven-connectivity gives

\[
                 4+\varepsilon+|R|=|N_G(C)|\ge7,
\]

which is (5.5).  Equality is exactly order seven; otherwise integrality
gives (5.6).  \(□\)

The separator theorem is label-preserving: (R) consists of actual
portals in the root lobe (J), not a count of contracted contacts.  It
is the exact next input for a flexible two-target split inside (J).

The full rooted model supplies more than the separator count: it supplies
two right-carrier edges on the far side of the cut.  They eliminate the
ordered spine completely.

### Theorem 5.3 (the exact-cut outcome is impossible)

Under the hypotheses of (1.1), (G) contains a (K_7)-minor.

#### Proof

The case (e_0\notin Z) is Theorem 3.1, so assume (e_0\in Z) and
use (J,C) from Theorem 5.2.  If (C\sim3) or (C\sim4), Theorem
5.1 applies.  We may therefore assume

\[
                         C\not\sim\{3,4\}.                    \tag{5.7}
\]

Put (X=Z-C).  The set (X) is connected: it consists of (J)
together with all components of (Z-J) other than (C), and every
such component has an edge to (J).  It contains (e_0), has an edge
to (q), and, by (1.1) and (5.7), has neighbours to both (3) and
(4).

We next retain the two old rooted-model edges on the (H)-side.

* Choose an (L_6)-(R_0) edge with left endpoint (d).  Since
  (K\not\sim R_0), the vertex (d) is not in (K).  If (d=6),
  put (D_0=\{6\}).  Otherwise let (M_d) be the component of
  (L_6-6) containing (d), and put (D_0=M_d\cup\{6\}).  The edge
  to (R_0\subseteq H) puts (M_d) in (H); connectedness of (L_6)
  gives an (M_d)-(6) edge.  Thus (D_0) is connected, disjoint
  from (Z), and adjacent to (R_0).
* Choose left endpoints (x_5,x_0\in L_0) of old edges to
  (R_5,R_0), respectively.  For (i\in\{5,0\}), if (x_i\ne q),
  let (M_i) be the component of (L_0-q) containing (x_i).
  Lemma 2.1 puts (M_i) in (H).  Let (P) be (q) together with
  the distinct sets among the (M_i).  Every component of (L_0-q)
  has an edge to (q), so (P) is connected and has edges to both
  (R_5) and (R_0).

Use the seven branch sets

\[
 \{v\},\quad\{h\},\quad\{3\},\quad\{4\},\quad
 R_5,\quad D_0\cup R_0,\quad X\cup P\cup\{1\}.   \tag{5.8}
\]

They are pairwise disjoint.  The sixth is connected by the
(D_0)-(R_0) edge.  The last is connected through an (Xq) edge,
the connected set (P), and the root edge (e_01).

The first four sets form a clique.  The bag (R_5) sees them through
(5) and its right root.  The sixth sees them through (6) and the
right root of (R_0).  The last sees them through (1), the root
(e_0), and the two (X)-contacts to (3,4).  Finally, the last
three sets are pairwise adjacent through the old (R_5R_0) edge and
the two retained (P)-to-right-bag edges.  Hence (5.8) is a
(K_7)-model.  \(□\)

Thus neither the abstract equality of the seven-cut nor a colouring
alignment theorem is needed: the actual ownership of the two old
rooted-model edges supplies the missing label-preserving exchange.

## 6. Sharp partial-data counterarchitectures

The ordered spine is not eliminated by fullness and the conservative
right frame alone.  Contract (Z) to one vertex, contract (R_5,R_0),
and retain the vertices of (S\cup\{v\}).  Keep exactly these data:

* (Z) is adjacent to all seven vertices of (S);
* (v) has its Moser contacts and is adjacent to the vertex (R_5)
  carrying (5);
* (R_5,R_0) have their right-root contacts and are adjacent;
* (6R_5) and (qR_0) are edges; and
* (q) misses (v,h,1,2).

Then (G-S) has exactly the two components

\[
                         \{Z\},\qquad \{v,R_5,R_0\},         \tag{6.1}
\]

and both are full to (S).  Nevertheless the graph has treewidth at
most five.  One width-five elimination order is

\[
 q,R_0,3,4,R_5,v,h,1,2,6,Z.                    \tag{6.2}
\]

The dependency-free verifier
`degree9_exact_cut_root_spine_verify.py` checks the filled-neighbour
bags and also checks the explicit models (4.2) after adding (q1) or
(q2).

This is a precise counterarchitecture to any claim that the exact cut,
two full shores, and the rigid right frame alone force (K_7).  The next
valid target must also retain the ownership of the old left-to-right
rooted-model edges.  This is exactly the information used in Theorem 5.3.

There is also a sharp counterarchitecture to strengthening Theorem 5.2
from portal surplus alone.  Replace the contracted (Z) by two root
vertices (K,E), both complete to (h,1,2).  Join (K) to (6), join
(E) to (q,3,4), and connect them through three length-two paths

\[
                         K-r_i-E\qquad(i=1,2,3).              \tag{6.3}
\]

Interpret (J=\{E,r_1,r_2,r_3\}) and (C=\{K\}).  Then

\[
 N(C)=\{h,1,2,6,r_1,r_2,r_3\}                              \tag{6.4}
\]

is an exact seven-interface, all (3,4,q) portals are ordered on the
root side, and the root exchange is impossible.  Nevertheless the graph
still has treewidth at most five; a width-five elimination order is

\[
 q,r_1,r_2,r_3,R_0,3,4,R_5,v,h,1,2,6,K,E.       \tag{6.5}
\]

The verifier checks (6.5) and checks that adding a (K)-(3) contact
immediately realizes the branch sets in (5.2).  This shows exactly what
the quotient forgets: not portal *number*, but both the order of the
(R)-portals inside the connected root lobe (J) and the two forced
far-side carrier edges.  Neither construction in this section is a
counterexample to Theorem 5.3; both deliberately omit at least one of
those carrier realizations.
