# Adversarial audit: the singleton triangle two-pair web

## Verdict

The central chain in
`hadwiger_singleton_triangle_q2_web_exchange.md` is **GREEN after three
small statement/proof corrections**.  In particular:

* the relative two-pair theorem really gives a bare disk web;
* the two-cut normal form and its explicit (K_7) certificate are sound;
* bilateral packet failure really glues to a planar core and is excluded
  by the proved four-colour Strong-Hadwiger theorem; and
* the curvature argument really produces at least six distinct tagged
  vertices of degree eight on the web face.

There is also a simpler final use of those tagged vertices than the SDR
argument currently recorded as Lemma 6.2: **any two of them already close
the atomic web**.  Thus every nonsingleton packet-free shore either exposes
a proper exact seven-cut or gives a (K_7)-minor.  This is an
arbitrary-order closure, not a finite-order computation.

The corrections needed in the main note are:

1. justify that an inserted web part is a proper subset before applying
   the relative-boundary inequality;
2. handle a shore of order one separately in Theorem 5.1; and
3. qualify the final three-connectivity assertion by (|D|\ge2).

The only external dependency is the stated same-vertex web form of the
Two Paths Theorem (and, in Lemma 6.1, the standard rooted-(K_4)
characterization for a 3-connected planar graph).

## 1. Set-terminal lifting and the bare web

Adjoining four distinct artificial terminals is a valid reduction from
portal sets to ordinary terminals, even when portal sets overlap.  A pair
of vertex-disjoint terminal paths cannot use either endpoint of the other
path internally.  Deleting the four artificial endpoints therefore leaves
two disjoint connected carriers in the shore.  Conversely, paths inside
two disjoint carriers, with their two incident artificial terminal edges,
give the terminal linkage.

The web theorem is used at exactly its legitimate strength: take an
edge-maximal crossless completion on the same vertex set, whose rib is
plane and whose non-rib pieces are cliques inserted behind facial
triangles.  If an inserted clique contains an original shore set (X),
then its neighbours in the shore and in the four represented boundary
classes are accounted for by at most three supporting vertices.  The
three omitted labels contribute at most three more, so

\[
                         |\partial_S(X)|\le6.
\]

One omitted sentence is needed here: (X\ne D).  If the whole shore lay
in one inserted part, fullness to all four represented labels would put a
neighbour of that part at each of four artificial terminals, while its
supporting triangle contains at most three of them.  This contradicts the
defining neighbourhood property of an inserted part.  Hence (X) is a
proper nonempty shore subset and the displayed inequality applies.

After deleting the artificial terminals, all four portal sets lie on the
face obtained from the web frame.  In the triangle application the four
actual frame edges are

\[
                         hr,\ rc,\ ca,\ ah,
\]

and the two diagonals (hc,ra) are absent, so restoring the labels gives
the literal facial cycle (h-r-c-a-h).

This step is conditional only on the cited same-vertex web theorem.  If a
final source states Two Paths only for four fixed vertices, the artificial
terminal derivation above is sufficient; what must still be checked in the
source is that its maximal obstruction has exactly the rib-plus-facial-
cliques form used here.

## 2. Atomic one- and two-separators

Lemma 3.1 is correct for shores of order at least two.  Atomicity forces a
unique portal or a one-vertex carrier to expose a relative boundary of
order at most seven.  A cutvertex component has relative boundary at most
(1+7=8); equality forces it to be full to all seven labels, and two such
components give the two carriers.

Lemma 3.2 is also correct.  For every component (K) of (D-Z), where
(|Z|=2), atomicity and packet failure force

\[
             N_D(K)=Z,\qquad |N_S(K)|=6.
\]

The missed label cannot lie in (R), because then (K) carries both
active pairs while every other component carries at least one.  Defects in
different pair blocks give the packet directly.  If there are three or
more lobes, choose a lobe which is not the unique source of either root of
the common defective pair; the union of (Z) and the remaining lobes is
connected, carries that pair, and the chosen lobe carries the other pair.
Thus exactly two lobes remain.  Applying the same packet test to
(Z\cup L_i) forces (Z) to miss the defect of (L_i), and fullness
then makes the two defects complementary.  This proves every clause of
(3.2), including the absence of both defective-pair portal classes on
(Z).

The crossed-lobe model in Lemma 4.1 has all 21 adjacencies.  The four
singleton bags form (K_4).  The three remaining bags

\[
             aL_c,\qquad bE,\qquad L_h
\]

are connected; their mutual edges are supplied by (ab), the
(aL_h)-contact, and the (bL_h)-contact.  Their contacts to the
singleton (K_4) are exactly those stated.  The version in which the
defective pair is (Q=\{r,a\}) follows from the same certificate after
the base symmetry ((h\ r)(a\ c)); optional boundary edges are irrelevant
because the certificate only uses the protected base edges.

Therefore a nonsingleton atomic packet-free shore is indeed
three-connected.

## 3. Bilateral gluing and the order-one correction

Theorem 5.1's main conclusion—exactly one packet owner—is correct.  Two
owners are excluded by exact five-block transfer.  If neither shore is an
owner, the two disk embeddings glue along the same labelled facial
(C_4), producing a plane embedding of

\[
                         G-\{1,2,b\}.
\]

The omitted set is the triangle (12b).  The audited
Martinsson--Steiner/Strong-HC4 triangle-core dichotomy then gives a
six-colouring or a (K_7)-minor.

As written, Theorem 2.1 assumes (|D|\ge2), whereas Theorem 5.1 does not
exclude a singleton shore.  This is not fatal: a singleton full to the
four frame labels, together with the facial (C_4), is simply a wheel and
has the required disk embedding directly.  Add this one-line case before
invoking Theorem 2.1.

The statement

> the nonowner is three-connected unless it exposes a proper exact
> seven-cut

also needs the qualifier (|D|\ge2).  For a singleton, atomicity is
vacuous and the proofs of Lemma 3.1 deliberately do not apply.  The
correct conclusion is:

\[
\boxed{
\text{the nonowner is a singleton, exposes a proper exact seven-cut, or
is a three-connected bare web.}}
\]

## 4. Curvature and the common face

Lemma 6.1 is correct in the nonsingleton atomic branch.  In a triangulated
disk, an outer shore vertex has (d_D\ge3), while an interior vertex has
no active-pair portal and hence has (d_D\ge5).  Thus every positive term
in

\[
 \sum_{\operatorname{int}}(6-d_T)+
 \sum_{\partial}(4-d_T)=6
\]

equals one and belongs to
(U=N_D(1)\cap N_D(2)\cap N_D(b)).  Negative terms can only increase the
number of positive terms needed, so (|U|\ge6).

For any four distinct members of (U), the rooted-(K_4)
characterization for a 3-connected planar graph says that either they are
cofacial or there is a rooted (K_4).  The latter plus the singleton
triangle is a (K_7).  Hence every four-subset of (U) is cofacial.
Fixing three members shows that all of (U) lies on one face, since two
faces of a 3-connected plane graph cannot share three vertices.

If that face were not the web's outer face, it would meet the outer face
in at most two vertices.  Retriangulate it as a fan.  All but at most two
of its vertices gain a diagonal, so at most two interior vertices and at
most two outer vertices can retain a positive curvature contribution.
The positive part would then be at most four, incompatible with total
curvature six.  Therefore the common face is the outer face.

With a triangulation chosen after this conclusion there are no positive
interior vertices.  Every positive vertex (z) is an outer degree-three
vertex, and atomicity plus the no-single-vertex-carrier conclusion forces

\[
 N_B(z)=R\cup\{p(z),q(z)\},\quad p(z)\in P,\ q(z)\in Q,
 \qquad d_G(z)=8.
\]

There are at least six distinct such original shore vertices.  No
completion edge or repeated portal occurrence is being counted as a
vertex.

## 5. Audit of the SDR lemma

Lemma 6.2 is sound, although it is superseded by the two-vertex closure
below.  The owner packet supplies internally disjoint paths for the two
diagonals of the boundary frame, hence a subdivision of (K_4) rooted at
(h,r,c,a).  A rooted (K_4)-minor can be obtained by assigning each
subdivision path's internal vertices to its endpoint bags.  If four
distinct tagged web vertices form an SDR, attach each to its boundary
root by its actual boundary edge.  The four bags remain connected and
disjoint and each now contains a common neighbour of the singleton
triangle, so adjoining that triangle gives (K_7).

The Hall classification is exact.  Each tagged vertex lies in exactly one
(P)-family and one (Q)-family.  A two-family Hall failure cannot use
both labels on the same side, whose union is all of (Z^+); it can only
use a cross-pair and then its union has order at most one.  Every set of
three labels contains all of (P) or all of (Q), and (|Z^+|\ge6).
Thus the only failures are an empty single family or a cross-pair covering
at most one vertex, exactly as stated.

## 6. Stronger closure: two tagged vertices suffice

### Lemma (two-tag atomic-web closure)

Let (D) be the atomic web and let (X,Y) be the two owner carriers,
where (X) joins the (h,c) portal classes and (Y) joins the (r,a)
portal classes.  If (D) contains two distinct vertices (u,v), each
adjacent to all of (R=\{1,2,b\}) and to at least one member of each of
(P=\{h,c\}) and (Q=\{r,a\}), then (G\succeq K_7).

#### Proof

Take a spanning tree of (D).  Delete an edge on its unique (u)-(v)
path, and let (A,B) be the vertex sets of the two resulting components,
with (u\in A) and (v\in B).  Then (A,B) are disjoint connected
sets covering (D), and the deleted tree edge is an (A)-(B) edge of
(G).

Use the seven bags

\[
 \{1\}\mid\{2\}\mid\{b\}\mid
 (X\cup\{h,c\})\mid(Y\cup\{r,a\})\mid A\mid B.   \tag{6.1}
\]

The first three bags form a triangle.  The (Xhc)-bag sees them through
(h1,h2,cb), and the (Yra)-bag sees them through (r1,r2,ab).  The
two owner bags see one another through (hr) (and have several other
frame edges available).  The vertex (u) makes (A) adjacent to every
singleton bag and to both owner bags; the vertex (v) does the same for
(B).  Finally (A\sim B) through the deleted tree edge.  All seven
bags are disjoint and connected, so they form a (K_7)-model. \(\square\)

Every member of (Z^+) has precisely the required tag, and
(|Z^+|\ge6).  Choosing any two proves:

### Corollary (atomic web excluded)

In a (K_7)-minor-free triangle endpoint, the unique packet-free shore
is either a singleton or contains a nonempty proper subset with relative
boundary exactly seven.  A nonsingleton atomic web cannot occur.

This is the strongest rigorously justified conclusion of the present
round.  It closes the full arbitrary-order atomic web family.  It does
not yet eliminate a nested exact-seven-cut shore or the singleton shore;
those are now the exact remaining descendants.
