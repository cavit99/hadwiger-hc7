# Contracted transit trees have a perfectly matched list-obstruction core

## Status

This note proves a uniform structural lemma for a whole-tree contraction.
It aligns all local colour obstructions in one proper-minor colouring, unlike
the separate edge-deletion witnesses whose palettes and boundary states need
not agree.

The output is exact.  A minimal uncolourable subtree carries a proper
edge-colouring such that the list at each vertex is precisely the set of
colours on its incident edges.  Since the contraction colour belongs to
every list, the edges with that colour form a perfect matching.

This does not yet split a labelled clique-model bag: a minimal obstruction
inside a larger contracted tree need not allow the hanging parts to be
coloured after one core edge is deleted.  It does give a new finite object
on which a label-preserving split theorem can act.

## 1. The abstract tree-list theorem

Let (T) be a finite tree and let (L(x)) be a nonempty finite set of
colours for every (x\in V(T)).  A subtree always means a connected
induced subtree, with the inherited lists.

### Theorem 1.1 (minimal tree obstruction is an edge-colour incidence)

Suppose (T) is not (L)-colourable, and choose an inclusion-minimal
subtree (R\subseteq T) which is not (L)-colourable.  Then there is a
map

\[
                         \lambda:E(R)\longrightarrow\bigcup_x L(x)
                                                               \tag{1.1}
\]

with the following properties.

1. For an edge (e=xy), both components of (R-e) are list-colourable,
   and in every list-colouring of those components the two endpoints
   (x,y) receive the same forced colour (lambda(e)).
2. At every vertex (x), the labels on the incident edges are pairwise
   distinct and

   \[
                        L(x)=\{\lambda(e):e\ni x\}.     \tag{1.2}
   \]

In particular,

\[
                              |L(x)|=d_R(x).             \tag{1.3}
\]

#### Proof

Fix (e=xy\in E(R)), and let (R_x,R_y) be the two components of
(R-e).  Both are proper subtrees of (R), so minimality makes them
list-colourable.  Let (F_x\subseteq L(x)) and (F_y\subseteq L(y)) be
the nonempty sets of colours which can occur at their respective endpoints
in such colourings.

If (a\in F_x), (b\in F_y), and (a\ne b), the two component
colourings combine across (e) to colour (R), a contradiction.  Hence
every pair in (F_x\times F_y) is equal.  Nonemptiness implies

\[
                             F_x=F_y=\{\lambda(e)\}       \tag{1.4}
\]

for one colour (lambda(e)).  This proves assertion 1 and also shows
that (lambda(e)\in L(x)\cap L(y)).

Let (e=xy) and (f=xz) be distinct edges incident with (x).  In a
colouring of the component of (R-e) containing (x), equation (1.4)
forces (x) to have colour (lambda(e)).  Its restriction to the
(z)-side of (R-f) forces (z) to have colour (lambda(f)).
The edge (xz) is present, so

\[
                             \lambda(e)\ne\lambda(f).    \tag{1.5}
\]

Thus the incident labels are distinct members of (L(x)).

If some (a\in L(x)) were not an incident label, then for every component
of (R-x) choose a list-colouring.  Equation (1.4) says that the neighbour
in the component corresponding to edge (e) is forced to
(lambda(e)\ne a).  Giving (x) colour (a) would combine these
colourings into an (L)-colouring of (R), a contradiction.  Hence the
incident labels exhaust (L(x)), proving (1.2)--(1.3). \(\square\)

### Corollary 1.2 (a common colour becomes a perfect matching)

If one colour (alpha) belongs to (L(x)) for every (x\in V(T)), then
the edges of (R) labelled (alpha) form a perfect matching of (R).

#### Proof

By (1.2), every vertex is incident with an (alpha)-labelled edge.  By
(1.5), it is incident with exactly one. \(\square\)

Thus (R) has even order.  Every leaf edge is labelled (alpha), because
the leaf list has size one and contains (alpha).  Non-(alpha) edge
labels can occur only internally and encode the alternating forced-colour
transitions between the matched leaf layers.

## 2. Application to a contraction-critical host

Let (G) have no proper (r)-colouring.  Let (T) be an induced tree
with at least one edge, contract (T) to (z), and let (c) be a proper
(r)-colouring of the resulting graph.  Write

\[
                              c(z)=\alpha.
\]

For (x\in V(T)), define the expansion list

\[
 L_c(x)=[r]\setminus c\bigl(N_G(x)-V(T)\bigr).        \tag{2.1}
\]

### Lemma 2.1 (the contraction list obstruction)

Every list (L_c(x)) contains (alpha), and (T) is not
(L_c)-colourable.

#### Proof

Every external neighbour of (T) becomes adjacent to (z), so none has
colour (alpha).  Hence (alpha\in L_c(x)) for all (x).

An (L_c)-colouring of (T), together with the fixed colouring (c)
outside (T), would be a proper (r)-colouring of (G), contrary to the
hypothesis. \(\square\)

Combining Lemma 2.1 with Theorem 1.1 and Corollary 1.2 gives the promised
aligned certificate.

### Theorem 2.2 (perfectly matched contraction core)

There is an inclusion-minimal uncolourable subtree (R\subseteq T) and a
proper edge-colouring (lambda) of (R) such that

\[
 [r]\setminus c\bigl(N_G(x)-V(T)\bigr)
     =\{\lambda(e):e\in E(R),\ e\ni x\}              \tag{2.2}
\]

for every (x\in V(R)).  The (alpha)-labelled edges form a perfect
matching of (R).

Equivalently, a vertex of degree (d) in the core has exactly (d)
available colours and its external neighbourhood realizes all other
(r-d) colours.  Both sides of every core edge (e=xy) force (x,y) to
the common colour (lambda(e)) when the edge is cut.

## 3. Why this is stronger than separate edge witnesses

For a single edge contraction, both endpoints have singleton list
({\alpha\}); this is the familiar endpoint saturation lemma.  Theorem
2.2 packages the obstructions of a whole transit tree in **one common
outside colouring**.  Its edge labels can vary, but they obey two global
laws absent from unrelated edge-deletion colourings:

1. incident edge labels are distinct and exactly exhaust the local
   available palette;
2. the contraction-colour edges form a perfect matching.

The four-vertex path with lists

\[
                   \{\alpha\},\quad\{\alpha,\beta\},
                   \quad\{\alpha,\beta\},\quad\{\alpha\}
\]

is the smallest nontrivial example.  Its edge labels are
(alpha,\beta,\alpha).  The two end constraints jointly force the middle
edge endpoints to (eta).

## 4. Exact remaining use

Suppose (T) is a transit tree inside one branch bag of a fixed labelled
clique model.  Theorem 2.2 supplies a perfect matching of candidate split
edges and exact external-colour capacity at every core vertex.  A viable
next lemma is:

> **Matched-core split-or-adhesion lemma.**  If every edge in the
> contraction-colour matching fails to split the transit bag while retaining
> its labelled model portals, then the union of the forced-colour sides
> exposes an ambient adhesion whose boundary equality state is preserved by
> two opposite edge operations.

The second outcome enters the proved two-shore transition gate and is
incompatible with a private free trace colour.

This target is not yet proved.  Two limitations must be retained.

1. The minimal core (R) may be a proper subtree of (T).  Colourings of
   the two components of (R-e) do not automatically extend through the
   hanging vertices of (T-R).
2. The lists record external **colours**, not the labels of the fixed clique
   bags.  A colour-to-model alignment or a separator certificate is still
   required.

Within those boundaries, Theorem 2.2 is a proved scalable invariant and a
concrete multi-edge replacement for unrelated Kempe traces.
