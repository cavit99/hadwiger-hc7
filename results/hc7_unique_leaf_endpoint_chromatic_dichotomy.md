# Chromatic dichotomy at a unique leaf--endpoint edge

**Status:** written proof with a separate GREEN internal audit in
[`hc7_unique_leaf_endpoint_chromatic_dichotomy_audit.md`](hc7_unique_leaf_endpoint_chromatic_dichotomy_audit.md).
This theorem is a local consequence of minor-criticality in the balanced
order-eight configuration.  It produces either a spanning endpoint-avoiding
`K_6` model or two distinctly coloured common neighbours in the connected
leaf-side interior.  It does not by itself produce a `K_7` minor or prove
`HC_7`.

## 1. Setup

Let `G` be a seven-connected graph with

\[
 \chi(G)=7
 \quad\text{and}\quad
 \chi(J)\le 6\text{ for every proper minor }J\text{ of }G.
\tag{1.1}
\]

Suppose `G` has the following part of the balanced order-eight
configuration.  There is an eight-vertex separator

\[
 S=R\mathbin{\dot\cup}V(e)\mathbin{\dot\cup}V(f)
       \mathbin{\dot\cup}\{x\},
 \qquad |R|=3,
\tag{1.2}
\]

and a component `C` of `G-S` containing adjacent vertices
`ell_e,ell_f` such that

\[
                         R\cup\{\ell_e,\ell_f\}
\tag{1.3}
\]

is a five-clique.  Assume that

1. `ell_e` is anticomplete to `V(e)`;
2. `ell_f` is anticomplete to `V(f)`;
3. `ell_f x` is not an edge;
4. `ell_f` has exactly one neighbour `a` in `V(e)`; and
5. the graph

   \[
                         H=C-\{\ell_e,\ell_f\}
   \tag{1.4}
   \]

   is connected.

The hypotheses imply that `ell_e a` is not an edge.  They also imply that
every boundary neighbour of `ell_f` belongs to `R union {a}`: its other
possible boundary vertices are the other endpoint of `e`, the two
endpoints of `f`, and `x`, all of which are nonneighbours by assumptions
2--4.

## 2. The dichotomy

### Theorem 2.1

Under the hypotheses above, exactly one of the following chromatic cases
holds.

1. The graph `G-{ell_f,a}` is six-chromatic.  It contains a `K_6`-minor
   model, and the model may be chosen to span all of
   `G-{ell_f,a}`.
2. The graph `G-{ell_f,a}` is five-chromatic.  In every proper
   five-colouring `phi` of this graph there are two distinct vertices

   \[
                         u,v\in V(H)
   \tag{2.1}
   \]

   adjacent to both `ell_f` and `a`.  More precisely, one can choose
   `u` with

   \[
                         \phi(u)=\phi(\ell_e),
   \tag{2.2}
   \]

   and `v` in the unique colour absent from the four-clique
   `R union {ell_e}`.

The relabelled symmetric statement holds after interchanging `e,ell_e`
with `f,ell_f`, provided the correspondingly interchanged hypotheses hold;
the unique endpoint in the new orientation is given its own name.

### Proof

Put

\[
                         J=G-\{\ell_f,a\}.
\]

The graph `J` is a proper minor of `G`, so `chi(J)<=6`.  On the other
hand, `J` is not four-colourable: a four-colouring of `J`, followed by
giving the adjacent vertices `ell_f,a` two distinct fresh colours, would
be a six-colouring of `G`.  Therefore

\[
                         5\le\chi(J)\le6.             \tag{2.3}
\]

Suppose first that `chi(J)=6`.  The established case `HC_6`, due to
[Robertson, Seymour and Thomas](https://doi.org/10.1007/BF01202354), gives
a `K_6` minor in `J`.  The graph `J` is connected, since otherwise the
two-set `{ell_f,a}` would be a vertex cut of `G`, contrary to
seven-connectivity.  Starting from any `K_6` model, absorb each component
outside the model union into an adjacent branch set.  Repeating this
operation gives a spanning `K_6` model in `J`.  This proves outcome 1.

It remains to assume that `chi(J)=5` and fix a proper five-colouring
`phi` of `J`.  We first record the standard double-critical consequence
in the form needed here.

For every colour `i`, the set of common neighbours of `ell_f,a` contains
a vertex of colour `i`.  Indeed, suppose no common neighbour had colour
`i`.  Recolour every colour-`i` neighbour of `ell_f` with one fresh sixth
colour.  These neighbours form an independent set, and none is adjacent
to `a` by the supposition.  Now colour `ell_f` with `i` and colour `a`
with the fresh colour.  This gives a proper six-colouring of `G`, a
contradiction.

The four vertices of `R union {ell_e}` form a clique in `J`, so they
receive four distinct colours.  Let

\[
       \delta=\phi(\ell_e)
       \quad\text{and}\quad
       \beta=\text{the fifth colour absent from }R\cup\{\ell_e\}.
\tag{2.4}
\]

Choose common neighbours `u,v` of `ell_f,a` having colours `delta,beta`,
respectively.  They are distinct because their colours differ.  We show
that both lie in `H`.

Neither is in the component of `G-S` opposite to `C`, because
`ell_f in C` has no edge to a different component of `G-S`.  Neither is
`ell_e`: the vertex `a in V(e)` is nonadjacent to `ell_e`.  A boundary
vertex adjacent to `ell_f` belongs to `R union {a}`.  The vertex `a` has
been deleted from `J`; no vertex of `R` has colour `delta` or `beta`,
because the three colours on `R` are the three colours of the four-clique
other than `delta`, while `beta` is absent from the whole four-clique.
Thus neither `u` nor `v` lies in `S`.  The only remaining vertices of `C`
are those of `H`, proving (2.1)--(2.2) and outcome 2.  The two chromatic
cases in (2.3) are mutually exclusive and exhaustive.  The symmetric
statement has the same proof. \(\square\)

### Lemma 2.2 (the edge-deletion bypass starts in the interior)

In every proper six-colouring `psi` of `G-ell_f a`, let

\[
                         \alpha=\psi(\ell_f)=\psi(a)
\]

and let `beta` be the unique colour absent from the five-clique
`R union {ell_e,ell_f}`.  The subgraph induced by the colours
`alpha,beta` contains an `ell_f`--`a` path avoiding the deleted edge, and
the first internal vertex of every such path belongs to `H`.

### Proof

The edge-deletion host `G-ell_f a` is exactly six-chromatic.
Minor-criticality gives the upper bound.  If it had a five-colouring,
recolouring `ell_f` with one fresh sixth colour would make the restored
edge proper and would six-colour `G`, a contradiction.  Thus every proper
six-colouring of this host uses all six colours.

The two ends of the deleted edge have the same colour; otherwise `psi`
would already colour `G`.  The five-clique remains intact after deleting
`ell_f a`, so it uses five distinct colours and determines the unique
sixth colour `beta` absent from it.

If `ell_f,a` belonged to distinct `alpha`--`beta` components, interchanging
the two colours on the component containing `ell_f` would make the
deleted edge proper and again six-colour `G`.  They therefore lie in one
component, which supplies the asserted path.

The first internal vertex on such a path is a `beta`-coloured neighbour
of `ell_f`.  No vertex of `R union {ell_e}` has colour `beta`.  Among the
other boundary vertices, `ell_f` is adjacent only to `a`, which has colour
`alpha`; and `ell_f` has no neighbour in the opposite component of
`G-S`.  Hence the first internal vertex lies in
`C-{ell_e,ell_f}=H`. \(\square\)

## 3. Exact contribution and remaining gap

Outcome 1 regenerates a spanning `K_6` model while avoiding the two ends
of the unique leaf--endpoint edge.  Turning it into a `K_7` model still
requires a branch-set choice in which the connected pair
`{ell_f,a}` contacts all six labelled branch sets, or an equivalent
label-preserving rerouting.

Outcome 2 is stronger than the minimum-degree fact that `ell_f` has at
least three neighbours in `H`: it gives two distinct vertices in `H`
which are simultaneously adjacent to the leaf and its unique boundary
endpoint, and it fixes their two colour labels in every five-colouring of
the two-vertex deletion.  These two common neighbours still do not force
the crossed linkage required by the split-edge completion.  In standard
terms, the remaining task is to find two disjoint connected subgraphs of
`H` which allocate the common neighbours and the contact sets of `x` and
the two unused defect endpoints to the prescribed branch sets.  Failure
of that allocation must be converted into an actual order-seven
separation or a boundary-colouring response; connectedness alone does not
make this conversion.
