# Audit: rigid-boundary contraction splice

## Verdict

**GREEN.**  The contractions are proper, each contraction colouring is
expanded only after deleting the contracted shore, the two restrictions
agree on the literal boundary after one palette permutation, and the
unique-colour partition argument is exact.

No current order-seven/eight normalization theorem guarantees the rigid
trace.  The theorem closes identifiable subrows, not every active
adhesion.

## 1. Proper contractions and one-sided expansion

For each shore `C_i`, fullness makes `C_i union I` connected: `C_i` is
connected and every vertex of `I` has an actual neighbour in it.  Both
sets are nonempty and disjoint, so this connected set has at least two
vertices and contracting its spanning tree contracts an actual edge.
Thus `M_i` is a proper minor and has a `(k-1)`-colouring.

Every vertex of `S-I` has an edge into `C_i`, which becomes an edge to
the contraction vertex `z_i`.  Hence the colour of `z_i` is absent from
`S-I`.

The proof does **not** expand `C_i` monochromatically.  It deletes that
shore and restores only the independent boundary set `I`, giving all of
`I` the colour of `z_i`.  Every retained edge incident with `I` was an
edge incident with `z_i` in the minor; edges into the deleted shore no
longer matter.  The result is therefore a proper colouring of the
opposite induced side `G-C_i`.

## 2. Exact boundary partition

The distinguished colour has boundary class exactly `I`: all vertices of
`I` receive it and no vertex of `S-I` does.  The restriction to `S-I`
uses at most the remaining `k-2` colours.  Since
`chi(G[S-I])=k-2`, it uses exactly `k-2` nonempty classes.

Unique `(k-2)`-colourability says precisely that the two partitions of
`S-I` into independent colour classes coincide up to a permutation.  In
both traces the additional distinguished block is `I`, and all `k-1`
boundary colours occur.  The class bijection therefore extends to one
global permutation of the `(k-1)`-colour palette aligning the entire
boundary `S`.

## 3. Crossed side choice

The colouring derived from `M_2` lives on `G-C_2` and hence colours
`G_1`; the colouring derived from `M_1` lives on `G-C_1` and hence colours
`G_2`.  After alignment they agree on `S`.  A separation has no edge
between `C_1` and `C_2`, so their union colours every original edge of
`G`.  Neither contracted shore is ever expanded.

For Corollary 2, `I={x,y}` is independent, `S-I` is a literal `K_5`, and
`K_5` is uniquely five-colourable, so all hypotheses hold with `k=7`.

## 4. Interaction with active order-seven/eight adhesions

The live exact-boundary results give actual full shores but do not force
the unique trace required here.

* For a dark exact-seven lobe in
  `../results/hc7_near_k7_active_root_face_exchange.md`, the boundary is
  two actual torso gates plus five of six literal shell labels.  If the
  missed label is the apex and the two gate vertices are nonadjacent, then
  the five retained singleton labels form `K_5`; taking the gate pair as
  `I` invokes Corollary 2.  The theorem does not guarantee either the
  missed label or gate nonadjacency.
* For a full exact-order-eight two-gate lobe in
  `hc7_near_k7_constant_owner_corridor.md`, deleting the apex and the two
  gates leaves the five-singleton clique.  The rigid splice applies only
  if that three-set is independent.  No active theorem forces those three
  nonedges.
* More generally, the exact-seven/eight lobe theorems control which
  literal rows contact a shore, but do not control all edges inside the
  boundary graph or prove unique five-colourability after an independent
  deletion.

Thus rigid traces are a genuine new closed subcase, but promoting the
splice to all P1 adhesions would require an additional boundary-structure
dichotomy.
