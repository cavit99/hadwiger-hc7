# An asymmetric shore split at the exact order-eight boundary

**Status:** proved and separately internally audited in
[`hc7_star_order_eight_asymmetric_shore_split_audit.md`](hc7_star_order_eight_asymmetric_shore_split_audit.md).
This is a branch-set lemma for the exact order-eight output of the
five-support star theorem.  It does not prove state transfer across that
boundary or Hadwiger's conjecture for `t=7`.

## Theorem 1 (an asymmetric shore split gives `K_7`)

Let `G` contain pairwise disjoint vertex sets

\[
                   A,\quad S,\quad B,
\]

with no edge between `A` and `B`.  Suppose `G[B]` is nonempty and
connected and every vertex of `S` has a neighbour in `B`.  Let

\[
       S=R\mathbin{\dot\cup}V(e)\mathbin{\dot\cup}V(f)
                     \mathbin{\dot\cup}\{x\},            \tag{1.1}
\]

where:

1. `R` is a three-vertex clique;
2. `e` and `f` are disjoint edges with no edge between them; and
3. each of `e,f` is collectively adjacent to every vertex of `R`.

Assume `A` contains two vertex-disjoint connected subgraphs `P,Q` such
that:

1. `P` has a neighbour at `x`, a neighbour in `V(f)`, and a neighbour at
   every vertex of `R`; and
2. `Q` has a neighbour at `x`, a neighbour in `V(e)`, and a neighbour in
   `V(f)`.

Then `G` contains a `K_7` minor.

### Proof

The following seven sets are pairwise vertex-disjoint:

\[
       P\cup\{x\},\qquad Q\cup V(e),\qquad B,\qquad
       V(f),\qquad \{r\}\quad(r\in R).                  \tag{1.2}
\]

They are connected.  The first set is connected because `P` has a
neighbour at `x`; the second because the connected subgraph `Q` has a
neighbour at some endpoint of `e`; the third is connected by hypothesis;
and the remaining four sets are edges or singletons.

It remains to check the branch-set adjacencies.  The edge from `x` into
`Q` joins the first two sets.  An edge from `x` into `B` joins the first
and third sets.  The hypotheses on `P` join the first set to `V(f)` and
to each singleton from `R`.  The hypotheses on `Q` join the second set to
`V(f)`; fullness of `B` at `V(e)` joins the second set to `B`; and the
collective adjacency of `e` to `R` joins the second set to every singleton
from `R`.  Fullness of `B` joins the third set to `V(f)` and to every
singleton from `R`.  Finally, the collective adjacency of `f` to `R`
joins `V(f)` to the three singleton sets, and `R` being a clique joins
those singleton sets pairwise.  Thus all pairs among the seven sets in
(1.2) are adjacent, so they are the branch sets of a `K_7` minor.
\(\square\)

The argument does not assume an edge between `P` and `Q`: the literal
boundary vertex `x`, placed with `P`, supplies the required adjacency to
`Q`.  Nor does it require `Q` to be adjacent to all of `R`: the edge
branch set `V(e)` supplies those three adjacencies.  Thus Theorem 1 asks
for substantially less than two boundary-full connected subgraphs.

## Corollary 2 (both open shores have full-subgraph packing number one)

Assume the exact order-eight hypotheses of
[`../barriers/hc7_star_order_eight_boundary_state_barrier.md`](../barriers/hc7_star_order_eight_boundary_state_barrier.md):

* `G` has no `K_7` minor;
* the separator has the decomposition (1.1), with both `e` and `f`
  collectively adjacent to `R`;
* `G-S` has exactly two connected components `A,B`; and
* every literal vertex of `S` has a neighbour in each of `A,B`.

Then neither `A` nor `B` contains two vertex-disjoint connected subgraphs
that are each adjacent to every literal vertex of `S`.

### Proof

If `A` contained two such subgraphs, assign either one to `P` and the other
to `Q`.  They satisfy the weaker hypotheses of Theorem 1, with `B` as the
opposite shore, so that theorem would give a `K_7` minor.  The same
argument with the two shores interchanged excludes two such subgraphs in
`B`.  Each component itself is connected and adjacent to every boundary
vertex, so the maximum number of pairwise disjoint boundary-full connected
subgraphs in either shore is exactly one.  \(\square\)

## Exact contribution and limitation

The two-component order-eight residue is therefore not merely a spanning
`K_7`-minus-one-edge model.  Each shore forbids the explicit asymmetric
split in Theorem 1; in particular, both shores are irreducible with
respect to packing two disjoint connected subgraphs adjacent to the whole
boundary.  This is a uniform unbounded conclusion; it uses no finite
enumeration or colouring language.

It does not supply a small vertex transversal inside either shore, a
nonseparating path repairing the missing `e`--`f` adjacency, compatible
six-colourings of the closed shores, or an order-seven separation.  Those
remain the exact bridge obligations.
