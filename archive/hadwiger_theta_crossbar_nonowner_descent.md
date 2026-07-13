# The theta crossbar nonowner is an exact-cut descent

## Status and scope

This note proves an arbitrary-order theorem for the final seven-edge theta
boundary.  It replaces the false rail-median assertion by a rural-society
argument which uses the operation-state orientation of a crossbar.

For either complete-quotient crossbar, its packet-free shore is either a
singleton or exposes a proper nested exact seven-cut.  In the theta cell
the singleton is impossible by Dirac's neighbourhood-independence bound.
Thus every crossbar nonowner strictly descends.

The theorem does **not** say that the nested boundary is again theta.
Nonedges are not preserved by minimum-cut transport.  Consequently the
result eliminates a theta crossbar nonowner at a minimum fragment and
forces both crossbars into the same minimum-fragment owner, but it does
not by itself finish that same-owner lock.

## 1. The oriented theta crossbar

Let `G` be a seven-connected, proper-minor-minimal non-six-colourable
graph with no `K_7` minor.  Let `S={0,...,6}` be an exact seven-cut with
two full components `C,D`, and suppose

\[
 E(\overline{G[S]})=\{01,02,05,12,15,24,45\}.       \tag{1.1}
\]

For the first theta crossbar put

\[
 P=\{0,5\},\qquad Q=\{1,2\},\qquad R=\{3,4,6\}.     \tag{1.2}
\]

Both `P,Q` are independent and `R` is a triangle.  Moreover

\[
                P\mid Q\mid\{3\}\mid\{4\}\mid\{6\} \tag{1.3}
\]

has complete block quotient.  The `P-Q` adjacency is `25`; the contacts
of the block `P` and `Q` with the exceptional singleton `4` are `04` and
`14`, respectively; labels `3,6` are complete to the other five labels.

A **`P,Q` packet** in a shore is a pair of disjoint connected carriers,
one meeting both `P` portal classes and the other meeting both `Q` portal
classes.

### Lemma 1.1 (operation-state orientation gives one nonowner)

Exactly one of `C,D` has a `P,Q` packet.

#### Proof

The cyclic-packet theorem supplies a packet in at least one shore.  A
packet in one shore transfers the exact five-block state (1.3) to the
opposite closed shore: contract its two carriers together with the two
independent boundary blocks and retain the three singleton blocks.  The
five images form a clique because the block quotient is complete.

If both shores had a packet, the same exact state would extend both
closed shores.  Align its five boundary colours and glue, producing a
six-colouring of `G`.  Hence at most one shore owns the packet, and the
owner is unique.  QED.

This is the only operation-sensitive input in the proof below.  It is
important: a bare web by itself carries no ownership direction.

Call the other shore `W` the **nonowner** and the packet shore `E` the
**owner**.  Fix disjoint owner carriers `X_P,X_Q`.

## 2. Relative atomicity and the bare web

For a nonempty proper set `Y subsetneq W`, put

\[
 \partial_S(Y)=(N_W(Y)-Y)\mathbin{\dot\cup}N_S(Y).   \tag{2.1}
\]

This set separates `Y` from the nonempty owner shore `E`.  Therefore
seven-connectivity gives `|partial_S(Y)|>=7`.  If equality holds, it is
an exact seven-cut; a component contained in `Y` is a proper fragment
strictly smaller than `W`, and minimum-cut fullness holds on its two
distinguished sides.

Assume, toward the atomic alternative, that no such equality occurs.
Then

\[
                  |\partial_S(Y)|\ge8
 \quad(\varnothing\ne Y\subsetneq W).              \tag{2.2}
\]

If `|W|>=2`, the label-free two-pair web theorem applied to the
packet-free shore gives a plane embedding of `W` in a disk in which all
four portal sets of `P union Q` occur on the outer face in alternating
order.  Any clique piece substituted behind a facial triangle would have
relative boundary at most

\[
                         3+|R|=6,                  \tag{2.3}
\]

contrary to (2.2).  Thus the web is bare.  Notice that the `4` portals
are not discarded: label `4` belongs to the omitted triangle `R` and is
retained in the curvature argument below.

## 3. One- and two-cuts in the nonowner

### Lemma 3.1 (portal multiplicity and no one-vertex carrier)

Under (2.2):

1. every label of `S` has at least two portal vertices in `W`;
2. no vertex of `W` sees both roots of `P`, or both roots of `Q`; and
3. `W` has no cutvertex.

#### Proof

If a label `s` had unique portal `z`, apply (2.2) to `W-{z}`:

\[
 |\partial_S(W-\{z\})|\le1+|S-\{s\}|=7.           \tag{3.1}
\]

Suppose `z` sees both roots of `P`.  For any component `K` of `W-z`,
packet failure makes `K` miss a root of `Q`; otherwise `{z}` and `K`
are the two carriers.  Hence

\[
 |\partial_S(K)|\le1+6=7.                          \tag{3.2}
\]

The argument with `P,Q` interchanged is identical.

Finally, if `z` is a cutvertex and `K` is a component of `W-z`, then

\[
 |\partial_S(K)|=1+|N_S(K)|\ge8.                  \tag{3.3}
\]

Thus `K` is full to all seven labels.  Two distinct components give
disjoint `P` and `Q` carriers, contradicting packet failure.  QED.

The first two conclusions also imply `|W|>=4`: the two roots of `P`
each have two portals, while no vertex is a portal for both roots of
`P`.

### Lemma 3.2 (a two-cut forces a `K_7`)

The atomic nonowner `W` has no two-cut.

#### Proof

Suppose `Z={z_1,z_2}` is a two-cut.  Since `W` has no cutvertex, every
component `L` of `W-Z` has both vertices of `Z` in its neighbourhood.
Equation (2.2) gives `|N_S(L)|>=6`.  A full component, or a component
missing a root of `R`, immediately combines with another component to
give the forbidden packet.  Defects in two different active blocks also
give the packet.  Thus every component misses one root of the same active
pair, say `P`, and is full to `Q union R`.

There are exactly two components.  With three, choose one which is not
the unique source of either root of `P`; it is a `Q` carrier while the
connected union of `Z` and the remaining components is a disjoint `P`
carrier.  Call the two components `L_0,L_5`.  Packet failure applied to
`Z union L_i` says that `Z` also misses the defect of `L_i`.  Fullness of
`W` then makes the two defects complementary:

\[
 N_S(L_0)=S-\{5\},\qquad N_S(L_5)=S-\{0\},
 \qquad N_Z(0)=N_Z(5)=\varnothing.                \tag{3.4}
\]

Choose `z in Z` and absorb it into `L_0`.  The seven sets

\[
 P\cup X_P,\quad Q\cup X_Q,\quad
 \{3\},\quad\{4\},\quad\{6\},\quad
 L_0\cup\{z\},\quad L_5                         \tag{3.5}
\]

form a `K_7` model.  The first five form a clique by the complete block
quotient (1.3).  Each of the last two sets sees one root of `P`, both
roots of `Q`, and all of `R`, and hence sees the first five bags.  Finally
`z` has a neighbour in `L_5`, so the last two bags are adjacent.

If all defects lie in `Q`, use the identical construction with `P,Q`
interchanged.  This contradicts the standing exclusion of `K_7`.  QED.

In particular, an atomic nonsingleton nonowner has order at least four,
is three-connected, and is a bare disk web.

## 4. Curvature produces two universal tags

### Lemma 4.1 (common-triangle curvature)

Let `W` be an atomic nonsingleton nonowner.  There are at least six
vertices on the outer web face which are adjacent to all of `R` and to
one root of each of `P,Q`.

#### Proof

Triangulate every bounded face of the bare disk web without adding
vertices, and call the triangulation `T`.  Every outer vertex has
`d_W>=3` by three-connectivity.  Every interior vertex belongs to none
of the four active portal sets, so it has at most the three boundary
neighbours in `R`.  Applying (2.2) to a singleton shows that every
interior vertex has `d_W>=5`.

Euler's disk-curvature identity is

\[
 \sum_{x\in\operatorname{int}T}(6-d_T(x))+
 \sum_{x\in\partial T}(4-d_T(x))=6.              \tag{4.1}
\]

A positive interior term is therefore exactly one: its vertex has
degree five and, by (2.2), sees all three vertices of `R`.  A positive
outer term is also exactly one: its vertex has degree three and at least
five boundary neighbours.  Lemma 3.1 permits at most one neighbour in
each of `P,Q`; hence it sees exactly all of `R` and one root of each
active pair.  Every positive vertex is consequently a common neighbour
of the triangle `R`, and the total positive contribution is at least
six.

Let `U` be the set of common `R` neighbours obtained this way.  If four
members of `U` were not cofacial in the three-connected plane graph
`W`, the rooted-`K_4` theorem for four vertices in a 3-connected planar
graph would give a `K_4` model whose four bags respectively meet those
vertices.  Adding the three singleton bags of the triangle `R` gives a
`K_7`, because every selected vertex sees every member of `R`.

Thus every four members of `U` are cofacial.  Fix three of them.  Two
faces of a 3-connected plane graph share at most an edge, so all of `U`
lies on one face `F`.  If `F` were not the outer face, it would share at
most two vertices with the outer face.  Triangulate `F` as a fan.  At
most two interior members of `U` and at most two outer members could
retain positive curvature, contradicting the required positive total of
at least six.  Hence `F` is the outer face.

Triangulate the remaining bounded faces after fixing this outer face.
No positive vertex is now interior.  Equation (4.1) supplies at least six
positive outer vertices.  Each has degree three in `W` and, as proved
above, is adjacent to all of `R` and to one root of each of `P,Q`.  QED.

### Theorem 4.2 (two tags close the atomic web)

An atomic nonsingleton nonowner does not exist.

#### Proof

Choose two distinct tagged vertices `u_0,u_1` from Lemma 4.1.  A spanning
tree of `W`, split at an edge of its `u_0-u_1` path, partitions `W` into
two connected adjacent sets `W_0,W_1` with `u_i in W_i`.

Now use the seven branch bags

\[
 P\cup X_P,\quad Q\cup X_Q,\quad
 \{3\},\quad\{4\},\quad\{6\},\quad W_0,\quad W_1. \tag{4.2}
\]

The first five form a clique by (1.3).  Each tagged vertex sees one root
in each active block and all three singleton roots, so each `W_i` sees
the first five bags.  The two web bags are adjacent by construction.
This is a `K_7` model, a contradiction.  QED.

## 5. Descent theorem and the exact terminal warning

### Theorem 5.1 (theta crossbar nonowner descent)

In the setting of Section 1, the `05|12` packet nonowner contains a
nonempty proper fragment behind an exact seven-cut.

#### Proof

If the nonowner has order at least two and exposes no exact seven-cut,
Sections 2--4 give the forbidden `K_7` model.  It remains to exclude an
order-one nonowner `W={w}`.  Since `W` is a full component of `G-S`,

\[
                         N_G(w)=S,\qquad d_G(w)=7. \tag{5.1}
\]

Dirac's neighbourhood bound in a seven-contraction-critical graph gives

\[
                         \alpha(G[N(w)])\le2.       \tag{5.2}
\]

But (1.1) makes `012` an independent triple in `G[S]`, a contradiction.
Thus only the exact-cut descent remains.  QED.

The same proof, after the relabelling

\[
                P=\{1,5\},\qquad Q=\{0,2\},
                \qquad R=\{3,4,6\},               \tag{5.3}
\]

applies to the second crossbar.  Its complete block quotient uses the
same boundary witnesses `25,04,14` after interchanging the active roles.

### Corollary 5.2 (minimum-fragment orientation)

If one shore of a theta adhesion is a minimum fragment among all
components behind exact seven-cuts, then that shore owns both theta
crossbars.  Otherwise it is the nonowner of at least one crossbar and
Theorem 5.1 produces a strictly smaller fragment.

This is the rigorous conclusion.  It reduces the minimum theta cell to a
same-owner two-crossbar exchange.

### Warning: descent does not preserve the theta neighbourhood

Theorem 5.1 must not be iterated by simply relabelling the new cut as
another copy of `S`.  Seven disjoint paths can transport labels between
nested minimum cuts, but they do not preserve nonedges.  In particular,
an inner cut may acquire the edge corresponding to old nonedge `01`.
The independent triple `012` used in (5.2) can then disappear, and a
terminal singleton at the transported cut is not ruled out by Dirac.

Thus Theorem 5.1 closes the unbounded bare-web family and forces the
same-owner lock at a minimum fragment.  The remaining theorem must use
the boundary-faithful operation states of the two owner packets to split
or synchronize that common owner; it cannot be replaced by a static
claim that every nested boundary remains theta.
