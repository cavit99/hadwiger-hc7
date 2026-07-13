# Absorbing a detachable common-row portal in a `q=2 <-> q=2` rotation

## Status and proof-spine role

This is an **active theorem awaiting independent audit**.  It uses the
literal labelled rotation datum, not the false abstract assertion that a
4-connected connector always supplies three of four rooted demands.

Its role is to discharge every shared-row portal core which is freely
detachable.  A surviving common portal is therefore forced to be a real
cut/monopoly pinch; if the same singleton is also both attachment roots,
the critical-pinch theorem puts a proper-minor equality state on an actual
adhesion.

## 1. Rotation datum with one common missing row

Use the rotation datum of
`../results/hc7_near_k7_rotation_edge.md`.  Thus the old model has bags

\[
                      X,U,F_1,\ldots,F_5,
             \qquad U=Z\mathbin{\dot\cup}W,
\]

and the rotated model has bags

\[
                      W,X\cup Z,F_1,\ldots,F_5.
\]

Assume their missing-row sets are

\[
                       D=\{a,b\},\qquad E=\{a,c\},       \tag{1.1}
\]

where `a,b,c` are distinct.  In particular, both `X` and `W` are
anticomplete to `F_a`, and every `Z-F_a` portal lies in the nonempty set

\[
                            P_a=N_Z(F_a).                \tag{1.2}
\]

For `K subseteq Z`, say that `K` is **old-pure** when

\[
   (Z-K)\cup W\text{ is connected and meets every }F_i\ (i\ne a),
                                                               \tag{1.3}
\]

and **new-pure** when

\[
   X\cup(Z-K)\text{ is connected and meets every }F_i\ (i\ne a).
                                                               \tag{1.4}
\]

The word pure records exactly that removing `K` does not steal a second
foreign-row adjacency.  No assertion about colours is built into the
definition.

## Theorem 1 (literal common-row absorption)

Let `K` be a nonempty connected proper subset of `Z` containing every
member of `P_a`.

1. If `K` is old-pure and `E(K,X)\ne\varnothing`, then `G` has a labelled
   `K_7^-` model whose deficient centre is the **same bag `X`** as in the
   old `q=2` model.
2. If `K` is new-pure and `E(K,W)\ne\varnothing`, then `G` has a labelled
   `K_7^-` model whose deficient centre is the **same bag `W`** as in the
   rotated `q=2` model.

### Proof

For the first assertion use the seven bags

\[
           X,\quad (Z-K)\cup W,\quad F_a\cup K,
                    \quad F_i\ (i\ne a).                \tag{1.5}
\]

The enlarged row `F_a union K` is connected because `K` contains an
`F_a`-portal.  It meets `X` through the assumed `X-K` edge, repairing the
old missing spoke `XF_a`.  The residual donor `(Z-K) union W` is connected
by old-purity.  It meets every unchanged row by (1.3), and it meets the
enlarged row through an edge across the connected proper cut
`K | (Z-K)` in `Z`.  The other five foreign bags retain all of their old
pairwise adjacencies.

The centre `X` still meets the residual donor through the literal `XW`
edge of the rotation datum.  It meets every unchanged row except `F_b`,
and remains anticomplete to `F_b`.  Thus (1.5) is a `K_7^-` model with
the same centre `X`.

The second assertion is symmetric but is worth checking literally.  Use

\[
           W,\quad X\cup(Z-K),\quad F_a\cup K,
                    \quad F_i\ (i\ne a).                \tag{1.6}
\]

New-purity supplies the residual donor and all its unchanged row edges;
the cut edge supplies its edge to `F_a union K`; the assumed `WK` edge
repairs `WF_a`; and `W` remains anticomplete exactly to `F_c`.  Its edge
to the residual donor survives through the literal `WX` edge.  Hence
(1.6) is the asserted `K_7^-` model. \(\square\)

## Corollary 2 (orientation at the minimum two-hole floor)

Suppose either

* `G` has no `K_7^-` minor; or
* the one-hole height-gap theorem applies with `mu>=2`, and `X` (in the
  first case) or `W` (in the second case) has order `mu`.

Then the corresponding pure detachable core in Theorem 1 cannot exist.

### Proof

In the first branch Theorem 1 directly contradicts the exclusion of
`K_7^-`.  In the second branch it constructs a one-hole model with centre
order `mu`, whereas the height-gap theorem says every one-hole centre has
order at least `mu+1`. \(\square\)

## Corollary 3 (a singleton common portal is a literal pinch)

Assume `P_a={p}`.

1. If `p` meets `X` and the old endpoint is protected by Corollary 2,
   then at least one of the following holds:
   * `G[U-p]` is disconnected; or
   * `p` is the unique `U-F_c` portal.
2. If `p` meets `W` and the new endpoint is protected by Corollary 2,
   then at least one of the following holds:
   * `G[(X union Z)-p]` is disconnected; or
   * `p` is the unique `(X union Z)-F_b` portal.

Thus a surviving singleton common portal which touches an endpoint centre
is not an abstract capacity failure: it is a cutvertex or a two-row
monopoly in one of the two literal donors.

### Proof

Take `K={p}`.  In the old orientation, `W` already meets every row except
`F_a,F_c`; hence a connected residual donor can lose a second row only
when `p` is the unique `U-F_c` portal.  Thus if neither listed obstruction
occurs, `K` is old-pure.  In the new orientation, `X` already meets every
row except `F_a,F_b`, so the only possible second monopoly is `F_b` and
`K` is new-pure.  Theorem 1 and Corollary 2 give a contradiction.
\(\square\)

## Corollary 4 (shared attachment gives an actual-adhesion state)

Retain `P_a={p}` and suppose `p` is adjacent to both `X` and `W`.
Assume additionally that `G` is not six-colourable and that every proper
minor and every proper edge-deleted subgraph of `G` is six-colourable.
Choose an edge `pw` with `w in W`.  Then the critical-pinch theorem in
`../results/hc7_near_k7_critical_pinch_state.md` applies with shared
attachment vertex `p`: the edge `pw` produces a proper-minor equality
state on the actual adhesion `N_G(W)`.

### Justification

The new defect set contains `c`, so `W` is anticomplete to the nonempty
far bag `F_c`.  Hence `F_c` lies outside `W union N(W)`, making the
separation actual.  The hypotheses of the cited critical-pinch theorem
are therefore literal, not quotient hypotheses.

## Trust boundary and exact residue

The theorem does not claim that every common portal core is detachable.
After it is applied, the only singleton residue is:

* a donor cutvertex;
* a portal owning at least two literal row classes;
* a portal internal to the connector and anticomplete to one endpoint
  centre; or
* the actual-adhesion equality state of Corollary 4.

Those alternatives are precisely the width-one input for a web/state
composition theorem.  Calling them planar or colour-gluable without the
additional composition argument would be invalid.
