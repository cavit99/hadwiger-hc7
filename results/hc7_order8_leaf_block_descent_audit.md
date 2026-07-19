# Audit of leaf-block descent at a boundary-full order-eight separation

**Verdict:** GREEN after two corrections to the original corollary.

**Audited source:**
[`hc7_order8_leaf_block_descent.md`](hc7_order8_leaf_block_descent.md)

**Audited SHA-256:**
`69080155d9d7a1f860569077137c7e52a7c97ad4e96d49dbe9201ff4cd5ca90a`

After this audit, the source was moved into `results/` and its status line
was changed only to record the GREEN verdict and link to this audit.  No
theorem statement, proof, scope, or trust boundary changed.  The resulting
source SHA-256 is
`de05b3115757852ebeb863e69ffd483e80cdf4ff07b448207658f42b20c895cc`.

**Audit type:** independent internal mathematical audit.  This is not
external peer review and does not prove `HC_7`.

## Scope checked

The audit checked the stated leaf-block theorem, its proof, the restricted
iterated corollary, its trust boundary, and the following uses of earlier
promoted inputs:

1. the four-boundary-full-subgraph triangle construction;
2. the four-full-component order-eight closure; and
3. the three-component order-eight boundary classification used to restore
   the triangle hypothesis during iteration.

## Findings

### Leaf-block structure

For a leaf block `B` of the block-cutvertex tree of `G[C]`, with its unique
cutvertex `z`, the interior `L=V(B)-{z}` is nonempty and connected and has
exactly one neighbour in `G[C]`, namely `z`.  Distinct leaf-block interiors
are disjoint.

### The explicit minor model

If two leaf-block interiors are adjacent to all eight vertices of `S`, then
those two interiors and the two original complementary components are four
disjoint connected `S`-full subgraphs.  With a triangle in `G[S]`, the seven
branch sets displayed in the proof are disjoint, connected, and pairwise
adjacent.  This is a valid explicit `K_7`-minor model.

### Literal separator and boundary order

For a leaf-block interior not full to `S`, the equality

`N_G(L)={z} dot-union (N_G(L) intersect S)`

is exact.  Its neighbourhood is the boundary of a genuine separation,
because the two original other components lie outside the closed lobe.
Seven-connectivity and non-fullness force boundary order seven or eight.

### The order-eight return

At `T=N_G(L)` of order eight, `L` is a proper component of `G-T`.  If any
other component misses a vertex of `T`, its full neighbourhood has order at
most seven and separates it from `L`; seven-connectivity makes this an
actual order-seven separation.  Otherwise every component is `T`-full.
The promoted four-component closure then bounds the number of components of
`G-T` by three, so the return has exactly two or three components.

### Proper-minor colouring response

Every edge from `L` to `T` may be deleted.  The deleted-edge graph is a
proper minor and hence six-colourable.  The two ends have the same colour in
every such six-colouring, because otherwise restoring the deleted edge would
give a six-colouring of `G`.

### Restricted iteration

Iteration is valid only on returned three-component interfaces.  Under the
unchanged hypothetical-counterexample assumptions, the promoted
three-component boundary classification says that an unresolved boundary
is among the residual 82 types and hence contains a triangle.  This restores
the theorem's triangle hypothesis.  The selected component order decreases
strictly, so the restricted iteration terminates.

## Corrections made before the GREEN verdict

The initial draft made two claims that were not justified:

1. it did not explicitly stop iteration when an order-eight return had only
   two components; and
2. it claimed that an edge selected component automatically entered the
   promoted induced-path completion theorem.

The audited source now stops on a two-component return.  It also retains an
edge as unresolved unless the additional demand-pair and overlapping-
interval hypotheses of the path-completion theorem are separately
re-established.  A fresh equal-endpoint colouring after deleting one edge
does not preserve those data.

## Exact trust boundary

The result eliminates cutvertex selected components by a strict host-level
descent only while the returned interface has three components.  It does
not close:

- a two-component order-eight interface;
- a singleton or edge selected component;
- a two-connected selected component;
- compatibility of the two shore colourings at an order-seven separation;
- or preservation of an inherited boundary partition, minor-model labels,
  demand pairs, or interval data.

Within this scope, no gap remains in the written proof.  Safe to promote
with the audited source hash above.
