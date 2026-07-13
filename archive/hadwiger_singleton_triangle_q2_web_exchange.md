# The singleton triangle reduces to one oriented two-path web

## 1. Exact boundary state

Retain the triangle endpoint of
`hadwiger_singleton_carrier_core_descent.md`.  Thus

\[
 B=\{h,1,2,r,a,b,c\},\qquad
 G-B=D_0\mathbin{\dot\cup}D_1,
\]

the two shores are connected, anticomplete, and full to (B).  The
boundary contains the two cliques

\[
 \{h,1,2,r\}\cong K_4,qquad \{a,b,c\}\cong K_3,
\]

and the four spokes (ha,1b,2b,rc).  In every quotient survivor,

\[
 hc,ra,hb,rb\notin E(G).                         \tag{1.1}
\]

Put

\[
 P=\{h,c\},\qquad Q=\{r,a\},\qquad R=\{1,2,b\}.
                                                               \tag{1.2}
\]

The sets (P,Q) are independent, (R) is a triangle, and

\[
 P\mid Q\mid\{1\}\mid\{2\}\mid\{b\}             \tag{1.3}
\]

has complete block quotient (K_5).  Indeed (P) and (Q) see one
another through (hr) and (ca); each sees (1,2) through (h,r),
respectively, and sees (b) through (c,a).

A **packet** in a shore (D) is a pair of vertex-disjoint connected
sets, one meeting the full (h)- and (c)-portal sets and the other
meeting the full (r)- and (a)-portal sets.  Lemma 4.2 of the carrier
descent note says that both shores cannot have a packet.

The point of this note is that the converse obstruction is not an
unstructured three-pair problem.  It is one ordinary Two Paths web, and
all its one- and two-separators disappear.

## 2. The label-free two-pair web theorem

Let (S=P\dot\cup Q\dot\cup R), where (|P|=|Q|=2) and
(|R|=3).  Let (D) be a connected full (S)-boundaried graph of
order at least two, and put

\[
 \partial_S(X)=(N_D(X)-X)\mathbin{\dot\cup}N_S(X)
 \quad(\varnothing\ne X\subsetneq D).             \tag{2.1}
\]

### Theorem 2.1 (two-pair packet or bare web)

Assume

\[
                         |\partial_S(X)|\ge7       \tag{2.2}
\]

for every nonempty proper (X\subsetneq D).  If (D) has no packet
for (P,Q), then (D) has a plane embedding with one face containing
all four full portal sets belonging to (P\cup Q).  After adding the
four boundary roots, the cycle alternating between (P) and (Q) is
facial.

#### Proof

Add four independent artificial terminals, one for each root in
(P\cup Q), and join a terminal to the complete portal set of its
root.  Give the terminals the alternating frame order.  A cross of this
society is exactly a packet.  The set-terminal Two Paths/Web Theorem
therefore gives an edge-maximal same-vertex completion consisting of a
plane rib with the four terminals on its outer face and clique parts
inserted behind facial triangles.

Suppose a nonempty set (X) of original shore vertices lies in an
inserted part supported by a facial triangle (T).  Replace every
artificial terminal in (T) by its boundary label and retain the
original shore vertices of (T).  The resulting set has order at most
three and accounts for every neighbour of (X) in (D) and in the
four represented boundary classes.  The only omitted labels are the
three vertices of (R).  The set (X) is proper: a supporting triangle
contains at most three of the four artificial terminals, whereas
fullness gives every one of those terminals an original edge into
(D); hence all of (D) cannot lie behind that triangle.  Therefore

\[
                         |\partial_S(X)|\le3+3=6,
\]

contrary to (2.2).  Thus no original vertex occurs in an inserted
part.  Delete the completion edges and the artificial terminals, and
restore the four boundary roots.  This leaves the asserted plane
embedding and facial alternating frame. \(\square\)

The theorem is deliberately a three-outcome tool in an ambient
seven-connected graph:

\[
 \boxed{\text{packet}\quad\text{or}\quad
        \text{proper exact seven-boundary}\quad\text{or}\quad
        \text{strict bare web}.}                  \tag{2.3}
\]

Indeed, ambient seven-connectivity gives (2.2); if equality occurs for
some (X), its external neighbourhood is an exact seven-cut.  In the
last outcome every proper relative boundary has order at least eight.

## 3. Atomic web structure

Call a packet-free shore **atomic** when

\[
                         |\partial_S(X)|\ge8       \tag{3.1}
\]

for every nonempty proper (X\subsetneq D).

### Lemma 3.1 (no singular portal or cutvertex)

In an atomic nonsingleton shore:

1. every boundary label has at least two distinct portals;
2. no vertex sees both roots of (P), or both roots of (Q); and
3. (D) is two-connected.

#### Proof

If a label (s) had the unique portal (z), then for
(X=D-\{z\}),

\[
 |\partial_S(X)|\le1+|S-\{s\}|=7,
\]

contrary to (3.1).

Suppose (z) sees both roots of (P).  For a component (K) of
(D-z), packet failure makes (K) miss at least one root (q\in Q);
otherwise (\{z\}) and (K) are the two carriers.  Hence

\[
 |\partial_S(K)|\le1+|S-\{q\}|=7,
\]

again a contradiction.  The argument for (Q) is symmetric.

Finally, if (z) is a cutvertex and (K) is a component of (D-z),
(3.1) forces

\[
 8\le |\partial_S(K)|\le1+|S|=8.
\]

Thus every such component is full to all of (S).  Two distinct
components are then disjoint carriers for (P) and (Q), a
contradiction. \(\square\)

### Lemma 3.2 (a two-cut has one crossed form)

Let (Z\subseteq V(D)) be a two-cut in an atomic shore.  After
interchanging (P,Q) and relabelling (P=\{p_1,p_2\}), the graph
(D-Z) has exactly two components (L_1,L_2), and

\[
\begin{aligned}
 N_S(L_1)&=S-\{p_2\},\\
 N_S(L_2)&=S-\{p_1\},\\
 N_D(L_1)&=N_D(L_2)=Z,\\
 N_Z(p_1)&=N_Z(p_2)=\varnothing .                 \tag{3.2}
\end{aligned}
\]

Thus both lobes are full to (Q\cup R), their defects in (P) are
complementary, and the two-cut itself supplies no (P)-portal.

#### Proof

For every component (K) of (D-Z),

\[
 8\le |N_D(K)|+|N_S(K)|\le2+7.                   \tag{3.3}
\]

If (|N_D(K)|\le1), then (3.3) makes (K) full to (S).  Any other
component contacts both roots of at least one of (P,Q), because it
misses at most one boundary label.  Use it for that pair and use (K)
for the other pair, obtaining a packet.  The same argument applies if
(N_S(K)=S).  Therefore equality has the unique form

\[
                         N_D(K)=Z,\qquad
                         |N_S(K)|=6.               \tag{3.4}
\]

The one missed label cannot belong to (R), since then (K) is a
carrier for both (P) and (Q).  Nor can two components have defects
in different pair blocks: each would be full to the pair missed by the
other, giving a packet.  Hence every component misses one root of the
same pair, say (P), and is full to (Q\cup R).

If (D-Z) had at least three components, choose one component (K_0)
so that the connected union of (Z) and all remaining components still
contacts both roots of (P).  Such a choice exists: at most one
component can be the unique source of each of the two roots, so among
three components one avoids both unique-source obstructions.  Then
(K_0) is a (Q)-carrier and the remaining union is a disjoint
(P)-carrier, a contradiction.  Thus there are exactly two components.

For (i=1,2), the connected graph (Z\cup L_i), disjoint from the
other lobe, cannot contact both roots of (P), since the other lobe is
a (Q)-carrier.  Therefore the root missed by (L_i) is also missed
by (Z).  Fullness of (D) then forces the two lobe defects to be
different.  This is precisely (3.2). \(\square\)

## 4. The crossed two-cut is already a (K_7)

The label-free crossed form becomes impossible at the singleton
triangle because its sparse quotient still contains exactly the edges
needed for a clique model.

### Lemma 4.1 (crossed-lobe certificate)

In the boundary (1.1)--(1.2), suppose a shore (D) has a two-cut with
lobes (L_h,L_c) satisfying

\[
 N_B(L_h)=B-\{c\},\qquad N_B(L_c)=B-\{h\}.        \tag{4.1}
\]

Let (E) be the opposite full shore.  Then (G\succeq K_7).

#### Proof

Use the seven bags

\[
 \{h\}\mid\{1\}\mid\{2\}\mid\{r\}\mid
 (\{a\}\cup L_c)\mid(\{b\}\cup E)\mid L_h.      \tag{4.2}
\]

The first four form the singleton (K_4).  The last three are
connected.  The bag (\{a\}\cup L_c) sees (h) through (ah) and
sees (1,2,r) through (L_c); the other two large bags see the
singleton (K_4) by fullness.  Among the last three bags, use (ab),
the (aL_h)-contact, and the (bL_h)-contact.  Thus all seven bags
are pairwise adjacent. \(\square\)

### Corollary 4.2 (an atomic nonowner is a three-connected disk web)

In a (K_7)-minor-free triangle endpoint, every atomic nonsingleton
packet-free shore is three-connected and has the bare disk embedding of
Theorem 2.1.

#### Proof

Lemma 3.1 gives two-connectivity.  Lemma 3.2 and Lemma 4.1 exclude
every two-cut. \(\square\)

This is the promised capacity--state web reduction: all one- and
two-adhesion geometry is gone at once, without enumerating portal
orders.

## 5. Both shores cannot be webs

### Theorem 5.1 (unique orientation)

In a hypothetical minor-minimal counterexample at the triangle
endpoint, exactly one shore has a (P,Q)-packet.  The other shore is
either a full singleton or a bare planar web; in the latter case,
unless it exposes a proper exact seven-cut, it is three-connected.

#### Proof

Both shores cannot have a packet by the five-block contraction and
gluing lemma (Lemma 4.2 of the carrier descent note).

Suppose first that neither shore has a packet and both have order at
least two.  By Theorem 2.1, each graph

\[
 G[D_i\cup\{h,r,c,a\}]
\]

has a plane disk embedding with the induced frame

\[
                         h-r-c-a-h                \tag{5.1}
\]

facial.  Glue the two disks along (5.1), one on each side.  Since the
shores are anticomplete and exhaust (G-B), this is a plane embedding
of

\[
                         G-\{1,2,b\}.              \tag{5.2}
\]

The deleted vertices (1,2,b) form a triangle.  The triangle/core
dichotomy (the proved four-colour case of Strong Hadwiger, equivalently
Theorem 2.1 of `hadwiger_triangle_strong_hc4_dichotomy.md`) applied to
the planar graph (5.2) says that (G) is six-colourable or has a
(K_7)-minor.  Both conclusions contradict the standing
counterexample.  Hence at least one shore has a packet, and therefore
exactly one does in this case.

It remains to check the edge case omitted by Theorem 2.1.  Suppose
(D_0=\{d\}) is a singleton and the opposite shore has no packet.  If
(|D_1|\ge2), Theorem 2.1 embeds (D_1) behind the facial frame (5.1).
Place (d), which is adjacent to all four frame vertices and has no
edge to (D_1), in the empty side of that face.  This again makes
(G-R) planar.  If (D_1) is also a singleton, place the two vertices on
opposite sides of the frame cycle; the same conclusion holds.  The
triangle/core dichotomy again gives a contradiction.  Thus the shore
opposite a singleton must have a packet.  A singleton itself cannot
contain two disjoint carriers.  This proves exact ownership in all
cases.  Corollary 4.2 gives the nonsingleton final assertion. \(\square\)

The residue now has a direction.  Call the packet shore the **owner**
and the other shore the **web**.  Contracting the two owner carriers
transfers the universal five-block state (1.3) to the closed web side.
That state cannot also extend the owner side, or the two side colourings
would glue.  Thus the remaining problem is not symmetric portal
placement: it is a one-way minor-transition exchange from a rejecting
owner into one three-connected planar disk web.

## 6. Curvature localizes the remaining web

The triangle (R) gives one more structural restriction which is useful
for that exchange.

### Lemma 6.1 (common-neighbour curvature)

Let (D) be the atomic web and set

\[
 U=N_D(1)\cap N_D(2)\cap N_D(b).                  \tag{6.1}
\]

Then (|U|\ge6).  Moreover, if (G) has no (K_7)-minor, every
vertex of (U) lies on the same outer face which contains the four
pair-root portal sets.

#### Proof

Triangulate every bounded face of the disk embedding, without adding
vertices, and call the result (T).  By Lemma 3.1 and (3.1), every
outer vertex has (D)-degree at least three.  An interior vertex is in
none of the four pair portal sets, so it has at most the three labels in
(R) as boundary neighbours and consequently has (D)-degree at least
five.  Hence

\[
 \sum_{z\in\operatorname{int}T}(6-d_T(z))+
 \sum_{z\in\partial T}(4-d_T(z))=6               \tag{6.2}
\]

can receive a positive summand only from an interior degree-five vertex
or an outer degree-three vertex.  In the first case, (3.1) forces the
vertex to see all three labels of (R); in the second case, it forces
the vertex to see all three labels of (R) and one root from each of
(P,Q).  Every positive summand is therefore equal to one and its
vertex belongs to (U).  Since any negative summands must also be
offset, (6.2) says that the total positive contribution is at least
six.  Hence (|U|\ge6).

If four vertices of (U) were not cofacial in the three-connected
plane graph (D), the three-connected planar specialization of the
rooted-(K_4) theorem (Fabila-Monroy--Wood, Theorem 9) would give a
(K_4)-model whose four bags meet those four vertices.  Together with
the singleton triangle (R), this is a (K_7)-model.  Thus every four
vertices of (U) are cofacial.  In a three-connected plane graph two
distinct faces meet in at most one edge.  Fix three vertices of (U)
and compare the cofacial quadruples containing them; all of (U) lies
on one face (F).

Suppose (F) is not the outer face.  At most two vertices of (U) lie
on the outer face.  Triangulate (F) as a fan.  All but at most two
vertices on its boundary receive a new incident diagonal.  An interior
vertex already has (D)-degree at least five, so only those at most two
vertices can still give a positive interior summand in (6.2).  There
are also at most two positive outer vertices.  Thus the total positive
part of the left side of (6.2) is at most four, impossible because the
whole sum is six.  Hence (F) is the outer face. \(\square\)

Let (Z^+) be the vertices which give positive summands in (6.2), for
a triangulation chosen after the conclusion of Lemma 6.1.  Since every
member of (U) is now on the outer face, there is no positive interior
vertex.  Consequently every (z\in Z^+) has

\[
 d_D(z)=3,\qquad
 N_B(z)=R\cup\{p(z),q(z)\},                       \tag{6.3}
\]

where (p(z)\in P) and (q(z)\in Q).  In particular

\[
                         d_G(z)=8,\qquad |Z^+|\ge6.\tag{6.4}
\]

Thus the web exports at least six degree-eight vertices with one of
four exact boundary tags.

### Theorem 6.2 (two curvature vertices close the atomic web)

An atomic nonsingleton web cannot occur at the triangle endpoint.

#### Proof

Choose distinct (z_0,z_1\in Z^+).  Every connected graph has a
connected bipartition separating two prescribed vertices: take a
spanning tree, delete one edge of its (z_0)-(z_1) path, and let
(W_0,W_1) be the two resulting vertex sets.  Thus

\[
 D=W_0\mathbin{\dot\cup}W_1,qquad
 z_i\in W_i,                                      \tag{6.5}
\]

both (W_i) are connected, and an edge joins them.

Let (X_P,X_Q) be the two disjoint owner carriers.  The following seven
sets are branch bags:

\[
 (P\cup X_P)\mid(Q\cup X_Q)\mid
 \{1\}\mid\{2\}\mid\{b\}\mid W_0\mid W_1.       \tag{6.6}
\]

The first two are connected.  They are adjacent through (hr) (and
also through (ca)); each is adjacent to all three singleton bags,
through (h,c) or (r,a), respectively.  The singleton bags form the
triangle (R).  By (6.3), each (z_i) sees one root in (P), one root in
(Q), and all three vertices of (R).  Hence (W_i) is adjacent to each
of the first five bags.  Finally (W_0W_1\ne\varnothing) by construction.
Thus (6.6) is a (K_7)-model, a contradiction. \(\square\)

### Corollary 6.3 (packet or proper exact adhesion)

At the exact triangle endpoint, the unique nonowner shore is either a
singleton or contains a nonempty proper connected fragment behind an
exact seven-cut.

#### Proof

For a nonsingleton nonowner, Theorem 2.1 gives the bare web.  If some
proper relative boundary is tight, it is the asserted exact cut.  If
none is tight, Corollary 4.2 and Lemma 6.1 apply, and Theorem 6.2 gives
a (K_7)-minor. \(\square\)

This closes the whole unbounded atomic web family.  The exact triangle
residue is no longer a portal-order or one-step-transition problem: it
is an exact-cut descent, with the sole terminal cell being a full
singleton nonowner opposite a packet owner.  Closing that singleton
cell still requires the protected split of one owner carrier (or an
equivalent minor-transition argument); it is not proved here.
