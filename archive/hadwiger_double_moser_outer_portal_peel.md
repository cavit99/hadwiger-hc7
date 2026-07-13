# The overlapping-Moser outer edge peels to one eight-interface body

## 1. The double frame

Let (G) be seven-connected and (K_7)-minor-free.  Suppose (u,v)
are adjacent degree-seven vertices and, with

\[
 X=\{x_1,x_2,x_3,x_4\},\qquad A=\{a,b\},\qquad P=\{p,q\},
\]

their two neighbourhoods are the overlapping pure Moser frames

\[
 N(u)=\{v\}\mathbin{\dot\cup}X\mathbin{\dot\cup}P,
 \qquad
 N(v)=\{u\}\mathbin{\dot\cup}X\mathbin{\dot\cup}A.       \tag{1.1}
\]

Choose the labels so that the mandatory edges, besides the two stars
at (u,v), are

\[
 x_1x_2,quad x_3x_4,quad ab,quad pq,
\]

\[
 ax_1,ax_2,bx_3,bx_4,
 \qquad qx_1,qx_2,px_3,px_4.                 \tag{1.2}
\]

Thus (u) misses (A), (v) misses (P), and both miss every vertex
outside the displayed ten-vertex core.  Put

\[
 W=X\mathbin{\dot\cup}P=N(u)-\{v\}.
\]

Assume, as in the singleton re-rooting, that

\[
 C=G-N[u]
\]

is one connected component.  Since (A\subseteq C), write

\[
 C=A\mathbin{\dot\cup}R,
\]

where (R) denotes all vertices outside the two closed degree-seven
neighbourhoods.  The only (C)-neighbours of (v) are (a,b).

This note proves that (C-A) is connected.  More precisely, two or more
components already give an explicit (K_7)-minor.  The one remaining
component either exposes another exact seven-cut or is full to the eight
labels (A\cup W).

## 2. The component defect bound

Let (D) be a component of (C-A), and put

\[
 A_D=N_A(D),\qquad S_D=W-N_W(D).               \tag{2.1}
\]

### Lemma 2.1 (outer-edge defect bound)

Every such (D) satisfies

\[
 1\le |A_D|\le2,
 \qquad
 |S_D|\le |A_D|-1.                              \tag{2.2}
\]

Consequently, either

* (D) meets exactly one of (a,b) and is full to (W); or
* (D) meets both (a,b) and misses at most one vertex of (W).

Moreover, unless (A_D=A) and (S_D=\varnothing), the set

\[
                         A_D\cup(W-S_D)          \tag{2.3}
\]

is an exact seven-cut.

#### Proof

The graph (C) is connected and distinct components of (C-A) are
anticomplete.  Hence every (D) has a neighbour in (A), proving the
first inequality.  The vertices (u,v) have no neighbour in (D), and
there are no edges from (D) to another component of (C-A).  Therefore

\[
                         N_G(D)=A_D\cup N_W(D).   \tag{2.4}
\]

The vertex (u) lies beyond this neighbourhood, so (2.4) is a genuine
separator.  Seven-connectivity gives

\[
 7\le |N_G(D)|=|A_D|+6-|S_D|,
\]

which is exactly (2.2).  If the exceptional full case does not hold,
the right side is at most seven, and hence equals seven.  Equation (2.4)
then proves the exact-cut assertion.  \(\square\)

The count uses the *actual* (a,b)-portals.  It does not replace a
one-portal component by a fictitious two-portal shore.

## 3. A two-row boundary packing lemma

The graph on (W) consists of two triangles joined by the edge (pq):

\[
 T_1=\{q,x_1,x_2\},\qquad T_2=\{p,x_3,x_4\}.   \tag{3.1}
\]

### Lemma 3.1 (two one-defect rows)

Let (D_1,D_2) be distinct components of (C-A), with defects
(S_i=S_{D_i}).  Then (G) contains a (K_7)-minor.

#### Proof

Each (S_i) is empty or a singleton by Lemma 2.1.

First suppose that the two nonempty defects are not one root from each
of the two literal edges

\[
 H_1=\{x_1,x_2\},\qquad H_2=\{x_3,x_4\}.        \tag{3.2}
\]

There are distinct representatives (z_i\in W-S_i) and one of the
triangles (T\in\{T_1,T_2\}), disjoint from \(\{z_1,z_2\}\), such that

1. it is not simultaneously true that (z_1\in S_2) and
   (z_2\in S_1); and
2. if (t\in T\cap S_i), then (tz_i\in E(G[W])).

This is a six-label finite lemma.  A direct proof chooses the triangle
whose two literal roots are not split between the two defects, then
chooses two vertices from the other triangle; the bridge vertex is the
third choice that avoids a forbidden transposition.  For auditability,
`double_moser_outer_portal_peel_verify.cpp` checks all (6^2) maximal
singleton rows and finds precisely the eight excluded ordered pairs in
(H_1\times H_2\) and (H_2\times H_1).

Put (B_i=D_i\cup\{z_i\}).  The bags (B_1,B_2) are connected and
adjacent: if their shore parts do not supply an edge, the failure of both
representative incidences would be the forbidden transposition in item 1.
Each (B_i) is adjacent to every singleton in (T); only its possible
defect needs item 2.  Finally

\[
 B_1,quad B_2,quad \{v,a,b\},quad
 \{t\}\ (t\in T),quad \{u\}                  \tag{3.3}
\]

are seven pairwise adjacent connected bags.  The bag \(\{v,a,b\}\) is
connected by the old Moser triangle and sees each (D_i) through its
nonempty (A)-portal.  It sees (T) through (vX) (and (T) contains
two roots; its third vertex causes no problem because the bags (B_i)
already account for all required adjacencies, while (u) sees all of
(W\cup\{v\})).  More explicitly, choose the triangle in (3.1); its
bridge vertex (p) or (q) is not adjacent to (v).  To retain the
claimed adjacency to \(\{v,a,b\}\), assign that bridge vertex to the
corresponding representative bag and use the literal root edge as the
two singleton bags.  This is the equivalent normalized certificate
tested by the verifier.  In this normalized form (3.3) means two
singleton roots, not all three vertices of (T).

It is cleaner to state the actual seven bags in that normalization:

\[
 B_1,\ B_2,\ \{v,a,b\},\ \{y\},\ \{z\},\ Q,\ \{u\},              \tag{3.4}
\]

where (yz) is a literal edge, and (Q) is the connected boundary bag
containing the bridge vertex of its triangle.  The finite representative
check constructs (Q) together with the two (B_i).  All incidences in
(3.4) are checked in the exact quotient search described below.

For complete transparency, the exceptional cross-root case has a short
hand certificate and does not rely on the finite lemma.  After swapping
the two shores and roots within each literal edge, suppose

\[
 S_1=\{x\}\subseteq H_1,
 \qquad S_2=\{y\}\subseteq H_2.                 \tag{3.5}
\]

Both components then meet both (a,b), by Lemma 2.1.  The following
seven bags form a (K_7)-model:

\[
 \{u\},\quad \{x_1\},\quad \{x_2\},\quad
 \{v,x_3\},\quad \{q\}\cup D_1,\quad
 \{p\}\cup D_2,\quad \{x_4,a,b\}.             \tag{3.6}
\]

If the defect in (H_2) is (x_3) or (x_4), and the defect in
(H_1) is (x_1) or (x_2), the same displayed bags work.  For example,
(D_1) sees both (x_3,x_4) and (q), while (D_2) sees both
(x_1,x_2) and (p).  The literal edges, the two Moser triangles, and
(pq) supply every remaining pairwise adjacency.  If the two defect
halves occur in the opposite shore order, interchange (D_1,D_2) and
(p,q).

The dependency-free exact branch-set search in
`double_moser_outer_portal_peel_verify.cpp` checks all 36 ordered maximal
defect pairs and reports no negative quotient.  In the non-cross cases
it also checks the simpler representative certificate; in the eight
cross cases it verifies (3.6).  Empty defects only add contacts, so the
maximal-row check covers them.  \(\square\)

### Audit repair to the displayed packing

The first draft of this lemma attempted to use all three vertices of
(T_1) or (T_2) as singleton bags together with \(\{v,a,b\}\).  That
is invalid because (v) misses (p,q).  The valid finite certificate is
the exact seven-bag quotient searched by the verifier; the cross-root
certificate is (3.6).  No proof may use the invalid all-three-singleton
shortcut.

## 4. The outer-edge peel

### Theorem 4.1 (two components close)

In the double-Moser singleton re-rooting,

\[
                         C-A\text{ is connected}.                 \tag{4.1}
\]

#### Proof

If (C-A) had two or more components, choose any two and apply
Lemma 3.1.  This contradicts the assumption that (G) is
(K_7)-minor-free.  \(\square\)

Let (R=C-A) be this sole component.  Lemma 2.1 now gives the exact
dichotomy below.

### Corollary 4.2 (exact cut or eight-interface body)

Exactly one of the following occurs.

1. (N_G(R)) is an exact seven-cut; or
2. (R) is adjacent to every vertex of
   
   \[
                             A\cup W,                              \tag{4.2}
   \]
   
   so (|N_G(R)|=8).

Thus a cut-irreducible double-Moser re-root has one connected body (R)
with both old-outer portals and all six new-boundary portal classes.  It
does not have an unbounded family of shores.

## 5. What remains inside the eight-interface body

Full contact alone is insufficient.  Contracting (R) to one vertex in
the conservative quotient does not produce a (K_7)-minor; similarly,
the fixed ten-vertex double-Moser overlap has a (K_6)-minor but no
(K_7)-minor.  These negative statements are exact branch-set searches,
not failed heuristics.

The extra information still needed is portal distribution inside (R).
The clean sufficient endpoint from
`hadwiger_singleton_reroot_classification_audit.md` is the following.

### Lemma 5.1 (cross-saturated outer split)

If (C) has disjoint connected sets (A_5,A_6), containing (b) and
(a), respectively, such that both sets meet all four portal classes
of (X), then (G) has a (K_7)-minor.

One explicit model is

\[
 A_5, A_6, \{u,x_1\}, \{v\},\
 \{x_2,p,q\}, \{x_3\}, \{x_4\},               \tag{5.1}
\]

after the harmless interchange of (p,q) dictated by (1.2).  Every
adjacency is checked in `singleton_reroot_overlap_verify.py`.

Consequently the exact remaining geometric sub-gap is:

> In the one-body eight-interface case, obtain the two disjoint
> cross-saturated outer carriers of Lemma 5.1, or turn their failure into
> another exact seven-cut.

This is a two-demand portal-splitting problem.  The peel above proves that
it cannot be replaced by further component enumeration.

## 6. Scope

The theorem closes every singleton double-Moser re-root in which deleting
the old outer edge leaves at least two components.  It also converts every
one-component case with a seven-element interface into the already present
exact-cut recursion.  Only a connected eight-interface body remains.

The argument uses seven-connectivity and the two exact degree-seven
neighbourhoods.  It does not use planarity, assume arbitrary linkedness,
or identify a quotient contact with a splittable real portal.
