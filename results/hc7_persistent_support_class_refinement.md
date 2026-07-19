# Quantitative persistence and the support-class graph

**Status:** written proof; separate internal audit GREEN in
[`hc7_persistent_support_class_refinement_audit.md`](hc7_persistent_support_class_refinement_audit.md).

This note sharpens the count in the rooted incident-edge persistence
theorem and records the exact pairwise structure of the persistent edges.
It does not change the selected labelled model.

## Theorem

Use the hypotheses, extremal model, and notation of Theorem 2.1 or Theorem
2.2 in
[the rooted persistence theorem](../results/hc7_rooted_persistent_model_edge.md).
Thus `F=K_t-e`, the root label `r` has `m` required foreign labels, `v` is
in the minimum rooted branch set `R`, and `p(v)` is the number of edges
incident with `v` whose individual deletion leaves the same spanning
labelled `F`-model.

Let `k_0` and `k_1` count the components of `G[R]-v` with respectively one
and at least two edges to `v`.  Let `ell` count the nonpersistent edges from
`v` to foreign branch sets, and let `q` count the foreign labels receiving
a persistent edge from `v`.  Define the nonnegative integer

\[
 s=m-\bigl(2(k_0+k_1)+\ell+q\bigr).
\]

Then

\[
 \boxed{\quad
 p(v)=d_G(v)-m+k_0+2k_1+q+s
 \quad}                                                     \tag{1}
\]

and consequently

\[
                         p(v)\ge d_G(v)-m+1.                 \tag{2}
\]

Partition the persistent incident edges into **support classes** as
follows.

- Persistent edges from `v` to the same component of `G[R]-v` form one
  internal support class.
- Persistent edges from `v` to the same foreign branch set form one
  external support class.

Make a graph `J_v` whose vertices are the persistent incident edges, with
two vertices adjacent when the corresponding two edges may be deleted
simultaneously while the same labelled model survives.  Then

\[
                   \overline {J_v}\text{ is a matching}.      \tag{3}
\]

More precisely, two edges in distinct support classes are adjacent in
`J_v`; every pair in a support class of order at least three is adjacent in
`J_v`; and a nonedge of `J_v` can only be the unique pair in a support class
of order two.  In an external class such a pair is nonadjacent only when no
other edge joins `R` to that foreign branch set.

### Proof

The rooted persistence proof gives

\[
 2(k_0+k_1)+\ell+q\le m,
 \qquad
 d_G(v)=k_0+\ell+p(v).                                    \tag{4}
\]

The definition of `s` turns the first relation into

\[
 \ell=m-2k_0-2k_1-q-s.
\]

Substitution in the degree identity gives (1).  The value `p(v)=0` is
impossible: (4) would give `d_G(v)<=m<=t-1`, contrary to `t`-connectivity.
Hence a persistent internal edge exists, so `k_1>0`, or a persistent
external edge exists, so `q>0`.  Thus

\[
                         k_0+2k_1+q+s\ge1,
\]

and (2) follows.

For (3), deleting edges from two distinct internal support classes leaves
one attachment from `v` to each affected component.  Deleting an internal
and an external edge independently preserves, respectively, connectivity
of `R` and the required foreign adjacency.  Deleting edges at two distinct
external labels leaves a separate backup edge at each label.  Thus edges
in distinct classes are jointly deletion-persistent.

If an internal class has order at least three, deleting any two of its
edges leaves a third `v`-attachment to the same connected component.  The
same argument applies to an external class of order at least three.  A
two-edge external class is also jointly persistent whenever a further,
possibly nonincident, edge still joins `R` to that foreign branch set.
Consequently a nonjoint pair is confined to one two-edge support class.
Different such pairs are vertex-disjoint because support classes partition
the persistent edges.  This proves (3).  \(\square\)

## Consequences for the common-label `HC_7` case

Suppose `t=7` and the root label is not an endpoint of the missing edge.
Then `m=6`, so

\[
                         p(v)\ge d_G(v)-5.                    \tag{5}
\]

If the host has no actual order-seven separation, then `d_G(v)>=8`.
Indeed, a degree-seven vertex has a seven-vertex open neighbourhood; the
usual eight-vertex exception would be `K_8` by seven-connectivity and is
excluded by the absence of a `K_7` minor.  Hence (5) gives `p(v)>=3`.
Any independently established inequality `d_G(v)>=9` gives `p(v)>=4`.

There is also a precise induced-star alternative.  Let `U` be the set of
other endpoints of the persistent incident edges.  If no two jointly
persistent edges have nonadjacent endpoints in `U`, then every nonedge of
`G[U]` is the endpoint pair of a nonjoint, two-edge support class.
Therefore

\[
                          G[U]=K_{p(v)}-M                     \tag{6}
\]

for some matching `M`, and every pair in `M` belongs to one fragile
two-edge support class.  In particular, endpoints chosen from distinct
support classes are pairwise adjacent, while the endpoints of every class
of order at least three form a clique.  This is the complete structural
alternative supplied by the persistence count alone.

The stronger assertion that `p(v)>=3` by itself forces the desired induced
two-leaf star is false; see
[the dual-truncated-icosahedron example](../barriers/hc7_persistent_induced_star_barrier.md).
That example has an actual order-seven separation, so it does not refute a
future theorem which uses the absence of every such separation as an
essential host-level hypothesis.

The near-clique structure also bounds the dense alternative.  Suppose the
host has no `K_7` minor.  If `p(v)>=8`, then any eight vertices of `U`
induce `K_8` minus a matching.  This graph has a `K_6` minor.  For a
matching of order at most two, six singleton vertices suffice.  For a
matching of order three, use five mutually adjacent singleton
representatives and one connected two-vertex branch set made from two
mates.  For a matching of order four, use one representative from each of
the four pairs as singleton branch sets and use the other four vertices in
two connected two-vertex branch sets.  Each new branch set meets every
singleton and the other new branch set.  Since `v` is adjacent to every
vertex of `U`, adjoining `{v}` would give a `K_7` minor.  Therefore the
dense alternative has

\[
                              p(v)\le7.                    \tag{7}
\]

If equality holds in (7), then the matching `M` in (6) has order exactly
three.  Indeed, when `|M|<=2`, five mutually adjacent singleton
representatives together with one connected bag containing the two mates
of the missing pairs form a `K_6` model in `G[U]` (with the evident
simplification when fewer pairs are missing).  Thus the common-label
`HC_7` case has the further consequence

\[
  \text{no induced persistent two-leaf star}
       \quad\Longrightarrow\quad d_G(v)\le12,             \tag{8}
\]

and equality in (8) forces `p(v)=7` and
`G[U]=K_7-3K_2`.  In particular, degree at least thirteen forces two
jointly deletion-persistent incident edges with nonadjacent outer ends.

## Trust boundary

The theorem supplies more persistent edges, shows that the obstruction to
pairwise simultaneous deletion is only a matching of fragile two-edge
support classes, and forces the induced two-leaf star at degree at least
thirteen.  It does not place a persistent edge in a chosen shore,
synchronize a boundary colouring, split a labelled branch set, or prove
the induced-star assertion at degrees eight through twelve under the
additional no-order-seven-separation hypothesis.
