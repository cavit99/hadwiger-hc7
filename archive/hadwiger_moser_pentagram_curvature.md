# Portal profiles and disk curvature in the all-crossless Moser core

## 1. Setting

Work in one three-connected full relative shore (D) of the order-six
reserved-connector cell.  Its boundary is

\[
 L=U\mathbin{\dot\cup}\{w,a\},\qquad |U|=5,
\]

and for every nonempty proper (X\subsetneq D),

\[
 |N_D(X)-X|+|N_L(X)|\ge7.                         \tag{1.1}
\]

Assume all five missing-(C_5) frames are crossless.  By the bare-web and
three-connected face synchronization the shore has a plane embedding in a
closed disk whose boundary cycle contains every vertex of every root portal
set

\[
 P_i=N_D(i),\qquad i\in\mathbb Z/5\mathbb Z,
\]

where (i(i+1)) are the missing-cycle edges.  The five portal sets have an
SDR, and its facial order is a pentagram.  Theorem 5.1 of
`hadwiger_reserved_connector_rank_leaf.md` justifies the all-crossless
assumption once any three frames are crossless.

## 2. The exact overlap profile

The tempting assertion (P_i\cap P_{i+1}=\varnothing) is false.  The exact
replacement is the following lock.

### Lemma 2.1 (adjacent overlap forces the opposite singleton)

If

\[
 x\in P_i\cap P_{i+1},
\]

then

\[
 P_{i+3}=\{x\}.                                    \tag{2.1}
\]

### Proof

Fix distinct SDR representatives (b_0,\ldots,b_4).  The missing edge
(i(i+1)) is disjoint from each of

\[
 (i+2)(i+3),\qquad(i+3)(i+4).                     \tag{2.2}
\]

Use (x,x) as the two occurrences of the first missing edge.  If (x)
were distinct from both SDR occurrences at the ends of either edge in
(2.2), the singleton ({x}) and a facial arc joining those two SDR
occurrences would be disjoint supports for that frame.  Crosslessness
therefore gives

\[
 x\in\{b_{i+2},b_{i+3}\}
 \quad\hbox{and}\quad
 x\in\{b_{i+3},b_{i+4}\}.
\]

The SDR occurrences are distinct, so (x=b_{i+3}).

Now take any (y\in P_{i+3}).  Apply the first frame in (2.2), using
(x,x) and (b_{i+2},y).  If (y\ne x), both occurrences of the other
pair are disjoint from (x).  If they coincide, they and (x) are two
disjoint singleton supports; if they are distinct, a facial arc between
them avoiding (x) supplies the second support.  Both contradict
crosslessness.  Hence (y=x), proving (2.1). \(\square\)

### Corollary 2.2 (complete (U)-profile classification)

For (z\in D), put

\[
 A(z)=\{i:z\in P_i\}.
\]

Exactly one of the following holds.

1. (A(z)) is independent in the missing (C_5), and therefore
   (|A(z)|\le2).  If it has order two, it is an edge of the present graph
   (G[U]=\overline{C_5}).
2. For some (i),
   \[
   A(z)=\{i,i+1,i+3\},\qquad P_{i+3}=\{z\}.        \tag{2.3}
   \]

Indeed a missing edge in (A(z)) invokes Lemma 2.1 and gives the displayed
triple.  Adding (i+2) would apply Lemma 2.1 to
((i+2)(i+3)) and force (P_i=\{z\}); adding (i+4) would force
(P_{i+1}=\{z\}).  Either conclusion, together with
(P_{i+3}=\{z\}), contradicts the existence of an SDR.  If there is no
missing edge, (A(z)) is an independent set of a five-cycle.

The exceptional triple is real.  In pentagram order (0,2,4,1,3), put

\[
 P_0=\{b_0,b_3\},\quad P_1=\{b_1,b_3\},\quad
 P_2=\{b_2\},\quad P_3=\{b_3\},\quad P_4=\{b_4\}.
\]

All five exact disk rules hold.  The verifier
`moser_c5_portal_overlap_probe.py` checks every occurrence choice.  Placing
these portals on the rim of a wheel gives a three-connected planar disk
realization, so three-connectivity alone cannot delete (2.3).

## 3. Disk curvature

Triangulate every bounded face of (D), without changing its outer facial
cycle, and call the plane supergraph (T).  For a triangulated disk,

\[
 \sum_{z\in\operatorname{int}T}(6-d_T(z))
 +\sum_{z\in\partial T}(4-d_T(z))=6.               \tag{3.1}
\]

Every interior shore vertex has no (U)-contact, because all five full
portal sets lie on the outer face.  It has at most the two external
neighbours (w,a), so (delta(G)\ge7) gives

\[
 d_D(z)\ge5\qquad(z\in\operatorname{int}D).        \tag{3.2}
\]

If all interior vertices had (T)-degree at least six and all facial
vertices had (T)-degree at least four, the left side of (3.1) would be
nonpositive.  Hence one of the following exact alternatives occurs.

### Theorem 3.1 (curvature profile dichotomy)

There is a vertex (x\in D) of one of these types.

* **Interior profile.**  (x\) is interior,
  \[
  d_D(x)=5,qquad N_L(x)=\{w,a\},qquad d_G(x)=7.   \tag{3.3}
  \]
* **Ordinary facial profile.**  (x\) is facial,
  \[
  d_D(x)=3,qquad A(x)=\{s,t\},                    \tag{3.4}
  \]
  where (st\in E(G[U])), and (x) sees both (w,a).  Again
  (d_G(x)=7).
* **Triple-lock facial profile.**  (x\) is facial,
  \[
  d_D(x)=3,quad A(x)=\{i,i+1,i+3\},quad
  P_{i+3}=\{x\},                                   \tag{3.5}
  \]
  and (x) sees at least one of (w,a).  Its degree is seven if it sees
  one and eight if it sees both.

### Proof

An interior vertex of (T)-degree at most five has (D)-degree exactly
five by (3.2), and then minimum degree forces both possible external
contacts.  A facial vertex of (T)-degree at most three has (D)-degree
exactly three because (D) is three-connected.  It needs at least four
external contacts.  Corollary 2.2 now gives exactly (3.4) or (3.5), with
the asserted (w,a)-contacts. \(\square\)

## 4. What Dirac adds

For a degree-seven vertex in a 7-contraction-critical graph, Dirac's bound
is

\[
 \alpha(N_G(x))\le2.                               \tag{4.1}
\]

It gives the following exact local restrictions, but not an immediate
contradiction.

1. In (3.3), put (R=N_D(x)), (|R|=5).  The plane graph (G[R]) is
   outerplanar and has independence number at most two.  Consequently it
   contains, as a spanning subgraph, either (C_5) or (K_3\dot\cup K_2)
   (these are the two edge-minimal outerplanar graphs on five vertices with
   independence number two).  For each (c\in\{w,a\}), the set of
   (c)-nonneighbours in (R) is a clique; if (wa\notin E(G)), every
   vertex of (R) sees at least one of (w,a).
2. In (3.4), let (R=N_D(x)), (|R|=3), and
   (Q=\{s,t,w,a\}).  Then (alpha(G[Q])\le2), and for every
   (y\in R), the set (Q-N_Q(y)) is a clique.  These are exactly the
   independent-triple exclusions involving one shore neighbour.
3. The degree-seven subcase of (3.5) is impossible.  Let (p,q) be the
   two outer-face neighbours of (x), and let (h) be its third shore
   neighbour.  If (pq\in E(D)), the Jordan triangle (pxq) encloses
   (h).  A component inside that triangle has shore boundary contained in
   ({p,x,q}), has no (U)-contact because every (U)-portal vertex is
   on the outer face, and can see externally only (w,a).  Thus
   ({p,x,q,w,a}) is a vertex cut of order at most five, contrary to
   seven-connectivity.  Hence (pq\notin E(D)).

   Put (z=i+3), so the triple lock gives (P_z=\{x\}).  The vertices
   (p,q) are an independent pair in (N_G(x)).  Dirac's bound (4.1)
   forces every other neighbour of (x), in particular (z), to be
   adjacent to (p) or (q).  But then (p\in P_z) or (q\in P_z),
   contradicting (P_z=\{x\}).  When (d_G(x)=8), Dirac gives only
   (alpha(N(x))\le3), so this argument does not apply.

The outerplanar five-vertex assertion in item 1 is a finite elementary
classification: deleting edges to a minimal graph converts its complement
to a maximal triangle-free graph; the outerplanar survivors are precisely
(C_5) and (K_3\dot\cup K_2).

## 5. The defect-at-most-one body and quotient replay

Since (D) is three-connected, (D-x) is connected.  Apply (1.1) to
(D-x).  Its internal boundary is the singleton ({x}), so

\[
 |N_L(D-x)|\ge6.                                   \tag{5.1}
\]

Contract (D-x) to one body vertex and contract the opposite full shore
to a second body vertex.  The first body misses at most one label of (L),
and fullness says that any missed label is seen by (x).  This is the
strongest quotient which forgets the placement of the three or five
neighbours of (x).

The dependency-free exhaustive verifier
`moser_curvature_quotient_probe.py` checks every partition of six or seven
Moser boundary vertices into six nonempty branch bags and every assignment
of the four helper vertices.  Its exact conclusions on the (a=1) side
are:

* the interior profile has no quotient model for any allowed body defect;
* among ordinary profiles, (A(x)=\{4,5\}) has a quotient model unless
  the body uniquely misses label (4); the other four present pairs remain
  quotient-negative;
* in a triple lock the body necessarily misses the unique label (i+3).
  Section 4 eliminates every degree-seven triple (exactly one of (w,a)).
  In the remaining degree-eight case (x) sees both (w,a); the quotient
  is positive for missing pairs (52,24,46), and negative for (05,60).

Thus the exact triple-lock curvature residual consists only of the two
degree-eight profiles based on missing edges (05) and (60).

Every positive quotient lifts: (5.1) supplies every body contact used by
the certificate, and connectedness lets the contracted bodies be expanded.
The negative entries are not counterexamples; they prove that contact
existence, even with defect at most one, no longer suffices.  Their missing
information is exactly the distribution of the incident shore edges.

## 6. Safe contraction frontier

Choose (D) minimum among no-model relative shores.  Corollary 2.2 of
`hadwiger_relative_shore_contraction.md` applies to every edge (xy) incident
with a curvature vertex.  It says that either

1. (x,y) are both terminal neighbours and
   \[
   \mathbf1_{aw}+|N_D(a)|=3,                       \tag{6.1}
   \]
   or
2. there is (Y_{xy}\subseteq D-\{x,y\}) with
   \[
   |N_D(Y_{xy})-Y_{xy}|+|N_L(Y_{xy})|=7,
   \qquad x,y\in N_D(Y_{xy}).                      \tag{6.2}
   \]

At most three shore edges in the whole graph can be of type 1, because
(6.1) leaves at most three terminal neighbours.  Thus an interior curvature
vertex has at least two incident tight witnesses.  A facial triple vertex
which does not see (a) has three; a facial vertex seeing (a) either has a
tight witness or belongs to the at-most-three-edge terminal-tight core.

Every component of a witness (Y_{xy}) is a full shore for its exact
order-seven boundary.  Intersecting tight shores uncross as sets by boundary
submodularity, but witnesses preserving two prescribed edge ends need not be
laminar; the explicit obstruction in `hadwiger_k34_c8_uncrossing.md` warns
against that inference.  The exact remaining curvature gap is therefore:

> Convert two crossing incident witnesses into an (N)-meeting (K_6), or
> orient the incident witnesses into a nested chain.  A nested chain has
> bounded exact-state depth by `hadwiger_minimum_separator_state_depth.md`;
> an all-terminal-tight incident set must be eliminated inside the
> at-most-three-vertex terminal portal core.

This is a finite-valence separator problem (three or five incident edges),
not an unstructured planar shore, but the crossing-to-model conversion is
not yet proved.
