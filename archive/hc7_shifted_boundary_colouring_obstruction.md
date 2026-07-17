# Exact colouring obstruction at the connected shifted boundary

**Status:** auxiliary written reduction; independent audit pending.  The
specific shifted configuration which motivated it is now eliminated by
[`../results/hc7_shifted_boundary_completion.md`](../results/hc7_shifted_boundary_completion.md),
so this is not part of the live dependency chain.  The note records the
exact consequence of contraction-criticality for an abstract pair of
connected boundary-full shores.  It does not solve the general
edge-splitting problem or prove `HC_7`.

## 1. Setup and extension families

Let `G` be a graph with chromatic number seven such that every proper minor
of `G` is six-colourable.  Suppose

\[
                 V(G)=A\mathbin{\dot\cup}T
                         \mathbin{\dot\cup}R,          \tag{1.1}
\]

where:

1. `|T|=8`;
2. `A` and `R` are nonempty and connected;
3. there is no edge from `A` to `R`; and
4. each of `A,R` has a neighbour at every vertex of `T`.

For `X in {A,R}`, let `E_X` be the set of equality partitions of the
literal vertex set `T` induced by proper six-colourings of `G[X union T]`.
Thus two vertices of `T` belong to the same block precisely when the
colouring assigns them the same colour.

### Lemma 1.1 (the two extension families are disjoint)

\[
                              E_A\cap E_R=\varnothing. \tag{1.2}
\]

### Proof

If colourings of the two closed sides induce the same equality partition,
a permutation of the six colour names makes them agree at every vertex of
`T`.  Their union is then a proper six-colouring of `G`, because there is
no edge from `A` to `R`.  This contradicts `chi(G)=7`. \(\square\)

### Lemma 1.2 (states forced by total and rooted contractions)

Each of `E_A,E_R` contains a partition with at most five blocks.  Moreover,
for every `z in T`, each family contains a partition in which `\{z\}` is
an exact singleton block.

### Proof

Contract `R` to one vertex `r`.  The proper minor `G/R` has a
six-colouring.  The vertex `r` is adjacent to every vertex of `T`, so its
colour is absent from `T`; the restriction to `G[A union T]` therefore
gives a member of `E_A` with at most five blocks.  Contracting `A` gives
the symmetric conclusion for `E_R`.

Fix `z in T`.  The set `R union {z}` is connected.  Contract it to one
vertex and six-colour the resulting proper minor.  Expand only the vertex
`z`, assigning it the colour of the contracted vertex, and restrict the
colouring to `G[A union T]`.  This is proper: every neighbour of `z` in
`A` was adjacent to the contracted vertex.  The contracted vertex was
also adjacent to every member of `T-{z}`, because `R` has a neighbour at
every boundary vertex.  Hence no other boundary vertex has the colour of
`z`, and `\{z\}` is an exact singleton block.  This gives the required
member of `E_A`.  Contracting `A union {z}` gives the symmetric member of
`E_R`. \(\square\)

The point of Lemma 1.2 is its quantifier: both disjoint extension families
contain a rooted singleton trace for every literal boundary vertex.  Thus
the remaining obstruction cannot be removed merely by choosing a more
convenient boundary root.

## 2. Every internal edge is a boundary-essential equality constraint

### Theorem 2.1

Let `ab` be any edge of `G[A]`.  Then there is a proper equality partition
`Pi_ab` of `T` with all of the following properties.

1. `Pi_ab` is induced by a six-colouring of `G[R union T]`.
2. `Pi_ab` is induced by a six-colouring of
   `G[A union T]/ab`.
3. `Pi_ab` is not induced by any six-colouring of `G[A union T]`.
4. A colouring witnessing items 1 and 2 lifts to a six-colouring of
   `G-ab` in which `a,b` have one common colour, say `alpha`.
5. For every other colour `beta`, the vertices `a,b` lie in the same
   component of the subgraph of `G-ab` induced by colours
   `\{alpha,beta\}`.

### Proof

The proper minor `G/ab` has a six-colouring `c`.  Its restrictions to the
two closed sides of the separation induce the same equality partition
`Pi_ab` on `T`, proving items 1 and 2.

If `Pi_ab` also belonged to `E_A`, combine an `A`-side colouring which
induces it with the restriction of `c` to `G[R union T]`.  After a
permutation of colour names the two colourings agree on `T`, and their
union six-colours `G`, contrary to `chi(G)=7`.  This proves item 3.

Lift `c` from `G/ab` to `G-ab` by assigning both `a` and `b` the colour of
the contracted vertex.  This proves item 4.  More generally, every
six-colouring of `G-ab` assigns `a,b` the same colour: if their colours
were different, restoring the edge `ab` would give a six-colouring of
`G`.

Fix `beta!=alpha` in the lifted colouring.  If `a,b` lay in different
components of the subgraph induced by colours `\{alpha,beta\}`, interchange
those two colours on the component containing `a`.  The result is another
proper six-colouring of `G-ab`, now with different colours at `a,b`.
Restoring `ab` would again six-colour `G`, a contradiction.  This proves
item 5. \(\square\)

### Corollary 2.2 (the one-vertex shore)

If `A=\{a\}`, then every six-colouring of `G-a` uses all six colours on
`T`.

### Proof

Here `N_G(a)=T`.  If a six-colouring of `G-a` omitted one colour on `T`,
assigning that colour to `a` would give a six-colouring of `G`. \(\square\)

## 3. Exact remaining mechanism

In the abstract setup (1.1), Theorem 2.1 shows that
contraction-criticality already supplies a common boundary partition after
contracting **any** internal edge of the connected open side.  The
obstruction is exactly the lift of that common partition through the
contracted edge: the two endpoints are monochromatic and are joined by a
bichromatic Kempe chain for each of the other five colours.  The endpoint-
rigid shifted `HC_7` configuration no longer requires this mechanism,
because the companion completion theorem constructs a `K_7` minor
directly.

Consequently, a further theorem based only on the existence of a returned
boundary partition would add no information.  A valid continuation must
use the boundary-full separation and the old support-six `K_5` model to do
one of the following:

1. split one contracted edge while preserving the boundary partition;
2. turn the five compulsory Kempe connections into a `K_7`-minor model;
3. extract an actual separation of order at most seven which preserves the
   opposite `K_5` model; or
4. prove that the one-vertex-shore saturation in Corollary 2.2 is
   impossible in the endpoint-rigid boundary.

Static boundary fullness is not enough to select a unique returned
partition: a counterexample to that stronger intermediate claim is
recorded in
[`hc7_shifted_order8_static_transition_barrier.md`](hc7_shifted_order8_static_transition_barrier.md).
