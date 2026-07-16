# Boundary incompatibility of proper-minor responses on opposite shores

**Status:** written proof; separately internally audited in
[`hc_opposite_shore_minor_response_incompatibility_audit.md`](hc_opposite_shore_minor_response_incompatibility_audit.md).
The theorem is uniform in the number of colours and the boundary order.
It isolates a global constraint on colourings of proper minors; it does
not by itself produce a clique minor or bound the boundary order.

## 1. Definitions

Let `(A,S,B)` be a vertex separation of a graph `G`: the three sets are
pairwise disjoint, `V(G)=A union S union B`, and there is no edge between
`A` and `B`.

A minor operation is **internal to `A`** if every deleted vertex and every
deleted or contracted edge has all its ends in `A`, and no contraction
identifies a vertex of `A` with a vertex of `S`.  In particular, such an
operation leaves the closed subgraph `G[B union S]` unchanged.  Define an
operation internal to `B` symmetrically.

A colouring of a graph containing `S` induces a **boundary partition**:
two vertices of `S` are in the same block exactly when they receive the
same colour.  This forgets the names of the colours but retains all
equalities on the literal boundary.

## 2. Opposite-shore incompatibility

### Theorem 2.1

Let `q` be a positive integer and let `G` be a graph which is not
`q`-colourable.  Let `(A,S,B)` be a vertex separation of `G` with both
open sides nonempty.  Let `mu_A` be a minor operation internal to `A` and
`mu_B` a minor operation internal to `B`.

If `G mu_A` and `G mu_B` are `q`-colourable, then no `q`-colouring of
`G mu_A` and `q`-colouring of `G mu_B` induce the same boundary partition
on `S`.

### Proof

Suppose that `c_A` is a `q`-colouring of `G mu_A`, that `c_B` is a
`q`-colouring of `G mu_B`, and that their boundary partitions agree.
Because `mu_A` is internal to `A`, the restriction of `c_A` to
`G[B union S]` is a proper colouring of that original closed shore.
Similarly, the restriction of `c_B` to `G[A union S]` is proper on the
other original closed shore.

Equality of the boundary partitions gives a bijection between the colour
names used by `c_A` on `S` and those used by `c_B` on `S`.  Extend this
bijection arbitrarily to a permutation of the `q` colour names and apply
it to `c_B`.  The two restricted colourings now agree at every vertex of
`S`.

Use the renamed `c_B` on `A union S` and use `c_A` on `B union S`.  This
is well defined on `S`.  It is proper on each closed shore, and every edge
of `G` belongs to at least one of the two closed shores because there are
no edges between `A` and `B`.  The resulting colouring is therefore a
proper `q`-colouring of `G`, a contradiction.  \(\square\)

### Corollary 2.2 (disjoint response languages)

Under the hypotheses of Theorem 2.1, let `P_A` be the set of boundary
partitions induced by all `q`-colourings of all specified proper minors
obtained by operations internal to `A`, and define `P_B` symmetrically.
If every specified minor is `q`-colourable, then

\[
                              P_A\cap P_B=\varnothing.
\]

In particular, this applies to all nonempty internal minor operations in
a minor-minimal non-`q`-colourable graph.

### Proof

An element of the intersection would be realized by one operation and
colouring from each shore, contrary to Theorem 2.1.  \(\square\)

## 3. Critical edges in opposite shores

### Corollary 3.1

Let `G` be a minor-minimal non-`q`-colourable graph, let `(A,S,B)` be a
vertex separation, and let `uv` and `yz` be edges with

\[
                         \{u,v\}\subseteq A,
             \qquad     \{y,z\}\subseteq B.
\]

Every `q`-colouring of `G-uv` induces on `S` a partition different from
the partition induced by every `q`-colouring of `G-yz`.

Moreover, in every such colouring of `G-uv`, the vertices `u,v` receive
one common colour `alpha` and lie in the same `alpha`--`beta` Kempe
component for every other colour `beta`.  The symmetric statement holds
for `y,z` in a colouring of `G-yz`.

### Proof

The two edge deletions are proper minors and are therefore
`q`-colourable.  Their boundary partitions are incompatible by
Theorem 2.1.

If a `q`-colouring of `G-uv` gave `u,v` different colours, it would
already colour the restored edge and hence all of `G`, a contradiction.
Write their common colour as `alpha`.  If, for another colour `beta`, the
vertices `u,v` belonged to distinct components of the subgraph induced by
the two colours, interchange `alpha` and `beta` on the component containing
`u`.  The interchange preserves properness on `G-uv` and gives `u,v`
different colours, again producing a `q`-colouring of `G`.  Thus they lie
in the same component for every `beta`.  The other shore is symmetric.
\(\square\)

## 4. Relation to the current `HC_7` frontier

At the balanced order-eight boundary, the original five-clique has an
internal edge in one open shore and the second five-clique has an internal
edge in the other.  Corollary 3.1 supplies two globally realized, mutually
incompatible boundary partitions, each carrying five edge-critical Kempe
connections.  This is stronger than choosing unrelated colourings of the
two closed shores: the partition on either side comes from a colouring of
one proper minor of the whole host graph.

The theorem deliberately stops at incompatibility.  Abstract disjoint
families of boundary partitions can exist, so a completion still needs a
label-preserving transition, an explicit `K_7`-minor construction, or a
strict separation.  The value of Theorem 2.1 is that any such transition
can now be organized around a uniform, host-level invariant rather than a
list of local boundary configurations.
