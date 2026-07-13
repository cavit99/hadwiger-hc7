# Audit of the singleton re-root and the overlapping Moser frame

## 1. Setting

Use the terminal alternative of the antipodal-gate descent.  Thus

\[
 N_G(0)=L=\{v,1,2,3,4,p,q\},\qquad d_G(0)=7,
\]

and (G-L) has exactly the two components ({0}) and (D).  In the
old degree-seven neighbourhood at (v), the labels are chosen so that

\[
 E(G[N(v)])=
 \{01,02,03,04,12,16,26,34,35,45,56\}.
 \tag{1.1}
\]

In particular, (X=\{1,2,3,4\}) induces (2K_2), with literal edges
(12,34).  The gate construction also gives

\[
 vX\subseteq E(G),\qquad vp,vq\notin E(G).
 \tag{1.2}
\]

The singleton-shore argument in Theorem 7.1 of
`hadwiger_gate_pairmode_core_placements.md` gives

\[
 pq\in E(G),\qquad p,q\hbox{ have two distinct core colours}.
 \tag{1.3}
\]

That theorem and its Corollary 7.2 are correct under the installed gate
hypotheses.  The only use of the Menger construction which must be kept
explicit is (p,q\notin K_0\cup K_{56}): if one of (p,q) had the
second gate colour, its edge to (0) would put it in (K_0).

## 2. Exact crossed-frame census

Suppose the two core-colour mates lie on different literal edges.  After
the symmetries of (2K_2), write

\[
 c(p)=c(1),\qquad c(q)=c(3).
\tag{2.1}
\]

Properness gives (p1,q3\notin E(G)).  Dirac's inequality at the new
degree-seven vertex (0) gives
(alpha(G[N(0)])\le2).  Corollary 7.2 therefore gives

\[
 p3,p4,q1,q2\in E(G).
\tag{2.2}
\]

All edges of (J=G[N(0)]) are now fixed except (p2) and (q4).  The
mandatory edge set is

\[
 \{v1,v2,v3,v4,12,34,pq,p3,p4,q1,q2\}.
\tag{2.3}
\]

This is exactly a pure Moser spindle, with centre (v), inner literal
edges (12,34), and outer edge (pq).  The two possible additional
edges are

\[
                         p2,\qquad q4.             \tag{2.4}
\]

This is the complete local census; no unlisted (pX)- or (qX)-edge is
still free.

## 3. The atlas representative (M+13) is not an optional-edge case

The phrase “the one-edge Moser extension” in the seven-vertex
small-support atlas refers to the exceptional isomorphism type

\[
                         M+13,
\tag{3.1}
\]

in the standard labelling (1.1).  It does **not** mean every graph
obtained by adding an arbitrary missing edge to (M).

There is a short isomorphism-invariant exclusion.  In (M+13), the
degree-four vertices are (0,1,3).  The subgraph induced by the
neighbourhood of each of these three vertices has exactly three edges:

\[
 E(M[N(0)])=\{12,13,34\},
\]

and the corresponding counts at (1) and (3) are also three.  In the
re-rooted graph (J), however,

\[
 d_J(v)=4,\qquad J[N_J(v)]=J[X]=2K_2,
\]

so (J[N_J(v)]) has exactly two edges.  Hence

\[
                         J\not\cong M+13.          \tag{3.2}
\]

Likewise (J\not\cong K_3\dot\cup K_4), since every vertex of that
graph has degree two or three, whereas (d_J(v)=4).

If an external classification has reduced (J) to

\[
 M,quad M+13,quad K_3\dot\cup K_4,
\]

then (3.2) and the degree argument leave only (J\cong M).  Since the
pure Moser spindle has a unique degree-four vertex, (v) must be its
centre.  The two vertices missed by that centre are then exactly (p,q),
and their edge (pq) is the outer edge.  Thus the labels are forced, not
merely chosen by an isomorphism.

## 4. What the optional edges actually give

An optional edge in (2.4) moves (J) into the generic usable-(K_4)
cell of the atlas; it does not create the exceptional type (3.1).
Explicit certificates are as follows.

If (p2\in E(G)), then

\[
        \{v,2\},\quad\{3\},\quad\{4\},\quad\{p\}
\tag{4.1}
\]

are four pairwise adjacent connected bags.  The two unused boundary
vertices (1,q) are adjacent.  Indeed, (3,4,p) form a triangle,
while ({v,2}) sees them through (v3,v4,2p).

Symmetrically, if (q4\in E(G)), then

\[
        \{v,4\},\quad\{1\},\quad\{2\},\quad\{q\}
\tag{4.2}
\]

are a (K_4)-model and the unused boundary vertices (3,p) are
adjacent.  These are the precise small-support certificates hidden by
the atlas computation.

They close a **two-exterior-component** degree-seven cell: anchor the two
full exterior components at the adjacent unused roots, obtaining an
(N(0))-meeting (K_6), and then add ({0}).  They do not by
themselves close the present singleton re-root, because (G-N[0]=D) has
only one component.  Treating (4.1) or (4.2) as an immediate (K_7)
certificate here would count a second exterior shore which does not
exist.

## 5. Audit of the descent

The label-free unique-portal descent in
`hadwiger_unique_portal_cut_descent.md` is valid with its stated
quantifiers.  In the nonsingleton case, (Y=C-\{x\}) has all external
neighbours in ((S-\{s\})\cup\{x\}), while a different component of
(G-S) lies on the far side.  Thus (N_G(Y)) is a genuine separator;
(k)-connectivity forces equality with that (k)-set.  In the singleton
case, fullness to the (k)-cut and anticompleteness of distinct
components give (N_G(x)=S).  No hidden minimality assumption is used.

Consequently the terminal gate really does re-root at a degree-seven
vertex with a sole exterior component.  What remains is not another
quotient classification: it is a portal-placement or splitting theorem
inside the common exterior (D).

## 6. An exact common-exterior split which closes the re-root

The two overlapping pure Moser frames contain the old outer edge (56)
inside (D).  Their mandatory incidences are

\[
 6\sim1,2,v,5,\qquad 5\sim3,4,v,6.
\tag{6.1}
\]

The following is a concrete portal-sensitive endpoint.

### Lemma 6.1 (cross-saturated (5)--(6) split)

Suppose (D) contains disjoint connected sets (A,B) such that

\[
 5\in A,\qquad6\in B,qquad
 N_X(A)=N_X(B)=X.
\tag{6.2}
\]

Then (G) has a (K_7)-minor.

#### Proof

The sets (A,B) are adjacent through the edge (56).  Consider the
seven bags

\[
 A,quad B,quad \{0,1\},quad\{v\},quad
 \{2,p,q\},quad\{3\},quad\{4\}.                \tag{6.3}
\]

They are disjoint and connected; in particular ({2,p,q}) is
connected through (2q,qp).  The last five bags are pairwise adjacent:

* ({0,1}) sees ({2,p,q}) through (12) (and also through
  the (0p,0q) edges), and sees (v,3,4) through the re-rooted star;
* (v) sees ({2,p,q},3,4) through (v2,v3,v4);
* ({2,p,q}) sees (3,4) through (p3,p4); and
* (34) is an edge.

Each of (A,B) sees those five bags through, respectively, the roots
(1,2,3,4) from (6.2), and through (v5,v6) for the singleton
({v}).  Finally (A) and (B) see each other through (56).
Thus (6.3) is a (K_7)-model. (square)

Because (5) already sees (3,4) and (6) already sees (1,2), the
new content of (6.2) is only

\[
 A\text{ reaches the portal classes of }1,2,qquad
 B\text{ reaches the portal classes of }3,4.      \tag{6.4}
\]

Thus the unresolved geometry is an exact two-carrier problem in the one
common exterior: find disjoint connected carriers, one joining
(5,P_1,P_2) and the other joining (6,P_3,P_4), or turn their
failure into a new minimum adhesion.  This statement retains portal
placement and is strictly stronger than merely contracting all of (D)
to one full shore.

## 7. Fixed (K_6) versus the genuine split (K_7)

The mandatory ten-vertex overlap alone has the (K_6)-model

\[
 \{0\},\quad\{v\},\quad\{1\},\quad\{2\},
 \quad\{3,5,6\},\quad\{4,p,q\}.                  \tag{7.1}
\]

This is not a (K_7)-model, and no seventh bag may simply be asserted:
the fixed mandatory-edge quotient itself has no (K_7)-minor.  The
dependency-free script `singleton_reroot_overlap_verify.py` exhausts all
branch-set partitions of that ten-vertex quotient and verifies this
absence.  It also verifies (4.1), (4.2), and the seven bags in (6.3).

The distinction is structural.  Model (7.1) merges the only represented
common-exterior material into one complex bag.  Lemma 6.1 gains the
seventh bag only after replacing that contraction by two disjoint
portal-distributed carriers.  Therefore the singleton re-root genuinely
reduces to a double-pure-Moser portal split; the local overlap by itself
does not finish the proof.

## 8. Exact finite contact atlas for a covering split

There is also a sharp quotient version of Lemma 6.1.  Let

\[
                         D=A\mathbin{\dot\cup}B
\tag{8.1}
\]

be a connected bipartition with (5\in A,6\in B), and contract the two
parts.  The contacts (A-v, A-3,A-4) and (B-v,B-1,B-2) are
mandatory.  Encode the four reverse contacts

\[
 A-1,quad A-2,quad B-3,quad B-4
\]

by a bit word (a_1a_2b_3b_4), and encode the contacts of each of
(p,q) by (1,2,3), meaning (A)-only, (B)-only, or both.

The dependency-free exhaustive certificate
`singleton_reroot_split_atlas.py` proves the following exact statement.
Among the (2^4 3^2=144) contact states, 41 have a (K_7)-minor in
the ten-vertex contraction quotient and 103 do not.  Under addition of
contacts, the ten maximal negative states are

\[
\begin{array}{c|c@{\qquad}c|c}
0011&33&0101&33\\
0110&33&0111&22\\
1001&33&1010&33\\
1011&22&1100&33\\
1101&11&1110&11.
\end{array}                                           \tag{8.2}
\]

Thus a covering split is quotient-positive exactly when its state is not
contained in one of the ten rows of (8.2).  The script exhausts every
partition of every used subset of the ten quotient vertices into seven
connected pairwise adjacent bags; it also checks all twelve minimal
positive states.  In particular every state (1111\mid **) is positive,
recovering Lemma 6.1 independently of the displayed hand model.

Table (8.2) is useful diagnostically but is not a new case-enumeration
programme.  It says exactly what an infinite structural lemma must force:
either a connected (5)--(6) split leaves the ten-state negative
downset, or every such split has one of the explicit deficient portal
orders in (8.2), which should uncross to a minimum adhesion.
