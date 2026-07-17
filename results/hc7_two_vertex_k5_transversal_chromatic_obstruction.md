# A seven-chromatic graph has no two-vertex transversal of `K_5`-minor models

**Status:** written proof; separate internal audit GREEN in the adjacent
audit note.

This note records a short but terminal consequence of the established
`t=5` case of Hadwiger's Conjecture.  It does not use connectivity,
contraction-criticality, or any selected minor model.

## Theorem 1.1

Let `G` be a finite graph and let `P` be a set of at most two vertices.  If

\[
                         G-P
\]

has no `K_5` minor, then `G` is six-colourable.

Equivalently, if `G` is seven-chromatic, then for every set `P` of at most
two vertices, the graph `G-P` contains a `K_5` minor.

### Proof

The established `t=5` case of Hadwiger's Conjecture says that every graph
with no `K_5` minor is four-colourable.  Hence `G-P` has a proper
four-colouring.  Give the vertices of `P` distinct fresh colours, using at
most two additional colours.  This is a proper colouring of `G` with at
most six colours.

The equivalent formulation is the contrapositive.  \(\square\)

## Corollary 1.2 (minor-model transversal form)

No set of at most two vertices in a seven-chromatic graph meets the
vertex-union of every `K_5`-minor model.

### Proof

A `K_5`-minor model avoiding `P` is exactly a `K_5`-minor model in `G-P`.
Theorem 1.1 therefore gives the claim.  \(\square\)

## Consequence for the `HC_7` programme

In a hypothetical minimal counterexample to `HC_7`, a two-vertex
`K_5`-minor-model transversal is not an independent terminal alternative
which still needs to be converted into a colour-compatible separation.
Its existence directly contradicts seven-chromaticity.

The already audited theorem converting such a pair in a seven-connected
graph into an actual order-seven separation remains useful structural
information, but it is stronger than is needed for the chromatic
contradiction.

## External input

The only external input is the established `t=5` case of Hadwiger's
Conjecture, equivalently the Four Colour Theorem together with Wagner's
description of the `K_5`-minor-free graphs.
