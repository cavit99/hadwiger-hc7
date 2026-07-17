# Common neighbours at a canonical outer edge

**Status:** written proof with a separate GREEN internal audit in
[`hc7_outer_edge_common_neighbour_completion_audit.md`](hc7_outer_edge_common_neighbour_completion_audit.md).
This note
combines the canonical rooted-web theorem with the chromatic dichotomy at a
unique leaf--endpoint edge.  It eliminates the five-chromatic outcome of
that dichotomy inside the canonical order-eight branch.  It does not close
the alternative in which a spanning `K_6` model is regenerated after the
two vertices are deleted.

## 1. Setup

Use the hypotheses and notation of the
[canonical rooted-web theorem](../results/hc7_star_order_eight_rooted_web.md).
Thus

\[
 L=R\mathbin{\dot\cup}\{\ell_e,\ell_f\}
\]

is a five-clique, `e,f` are the two labelled edges, `R` has order three,
and `Q` is obtained from `G-R` by contracting `e,f` to `z_e,z_f`.
The theorem gives a web completion with outer order

\[
                 \ell_e,\ell_f,z_e,z_f.              \tag{1.1}
\]

Its distinguished facial triangle is

\[
                         T=\{z_e,z_f,x\}.             \tag{1.2}
\]

The graph `Q-T` has exactly two components.  Let `A_Q` be the component
containing `ell_e,ell_f`, and let `C` be its preimage in `G-S`, where

\[
                S=R\mathbin{\dot\cup}V(e)
                    \mathbin{\dot\cup}V(f)
                    \mathbin{\dot\cup}\{x\}.          \tag{1.3}
\]

The hypotheses of that theorem include:

1. `G` is seven-connected and has no `K_7` minor;
2. `Q` has no vertex cut of order at most two; and
3. every three-vertex cut of `Q` contains both `z_e,z_f`.

The last two properties are the branch obtained after the relevant actual
order-seven separations have been excluded.

## 2. Vertices on the leaf side belong to the planar skeleton

### Lemma 2.1

Every vertex of `A_Q` belongs to the planar skeleton of the web completion.

#### Proof

Write the web completion as `W^+`, with planar skeleton `W` and optional
attachment clique `X_U` behind each facial triangle `U` of `W`.

Suppose a vertex of `A_Q` belongs to some `X_U`.  Since `Q` is a spanning
subgraph of `W^+`, every path in `Q` from `X_U` to a skeleton vertex uses
a vertex of `U`.  Deleting `U` therefore separates a surviving vertex of
`X_U` from an outer vertex outside the three-set `U`.  Thus `U` is a
three-vertex cut of `Q`.

Every such cut contains `z_e,z_f`.  In the plane skeleton there is only
one bounded facial triangle incident with the outer edge `z_ez_f`, namely
`T` from (1.2).  Hence `U=T`.

But after deleting `T`, no vertex of `X_T` can lie in the component
`A_Q`, which contains the distinct skeleton vertices `ell_e,ell_f`:
vertices of `X_T` have no neighbour outside `T union X_T`.  This is a
contradiction.  Therefore `A_Q` contains no attachment vertex. \(\square\)

## 3. At most one common neighbour

### Theorem 3.1 (outer-edge common-neighbour uniqueness)

Let `a` be an endpoint of `e` adjacent to `ell_f`.  Then

\[
 \bigl|N_G(\ell_f)\cap N_G(a)\cap V(C-\{\ell_e,\ell_f\})\bigr|\le 1.
                                                               \tag{3.1}
\]

#### Proof

Suppose distinct vertices `u,v` belong to the intersection in (3.1).
They remain distinct after `e` is contracted, because neither belongs to
`V(e)`.  They lie in `A_Q` and hence, by Lemma 2.1, are vertices of the
planar skeleton `W`.

The literal edge `ell_f a` becomes the edge `ell_f z_e` of `Q`.  By the
outer order (1.1), this is the outer edge between the second and third
outer vertices of `W`.  The four edges from `u,v` to `ell_f,a` survive the
contraction as

\[
   u\ell_f,\ uz_e,\ v\ell_f,\ vz_e.
\]

All five displayed edges have both ends in the skeleton, so they are
edges of `W`.  Consequently `W` contains the two distinct triangles

\[
                   \ell_f z_eu,qquad \ell_f z_ev.    \tag{3.2}
\]

The separately audited
[four-connectivity theorem for the canonical skeleton](../results/hc7_canonical_web_skeleton_four_connected.md)
applies to `W`.  Hence no triangle of `W` is separating; equivalently in
this near-triangulation, every triangle is facial.  Neither triangle in
(3.2) is the outer face, whose boundary is the four-cycle (1.1).  Thus
both would have to be the bounded face incident with the outer edge
`ell_f z_e`.  A plane edge has only one bounded incident face.  Since
`u` and `v` are distinct, this is impossible. \(\square\)

## 4. Chromatic consequence

### Corollary 4.1

Assume the balanced order-eight configuration has reached the canonical
rooted-web branch after excluding a `K_7` minor and the relevant actual
order-seven separations.  Suppose `ell_f` has the unique neighbour `a` in
`V(e)` and the other hypotheses of the
[unique leaf--endpoint chromatic dichotomy](../results/hc7_unique_leaf_endpoint_chromatic_dichotomy.md)
hold.  Then

\[
                        \chi(G-\{\ell_f,a\})=6.        \tag{4.1}
\]

In particular, `G-{ell_f,a}` has a spanning `K_6`-minor model.

Equivalently, before the two terminal outcomes are excluded, the
five-chromatic alternative of that dichotomy yields a `K_7` minor or an
actual order-seven separation.

#### Proof

If the two-vertex deletion were five-chromatic, Theorem 2.1 of the cited
chromatic dichotomy would give two distinct common neighbours of
`ell_f,a` in

\[
                         C-\{\ell_e,\ell_f\}.
\]

This contradicts Theorem 3.1.  Therefore the deletion is six-chromatic.
The spanning `K_6` model is the other outcome of that same dichotomy.  The
equivalent formulation is its contrapositive with the two exclusions
restored. \(\square\)

## 5. Scope

The endpoint-mate allocation theorem is compatible with this conclusion,
but its finite endpoint classification is not needed in the proof.  Its
role upstream is to expose the unique leaf--endpoint edge to which the
chromatic dichotomy applies.  The new argument uses the placement of two
common neighbours, the labelled contraction of `e`, and the canonical
planar web geometry.

The six-chromatic outcome in (4.1) remains open: a spanning unlabelled
`K_6` model in `G-{ell_f,a}` need not have all six branch sets adjacent to
the connected pair `{ell_f,a}`.  That label-preserving model allocation is
the next obligation.
