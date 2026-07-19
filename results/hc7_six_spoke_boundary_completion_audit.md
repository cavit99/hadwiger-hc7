# Audit of boundary completion from six almost-full neighbours

**Verdict:** GREEN for Theorem 2.1 and Corollaries 2.2 and 3.1 in
[`hc7_six_spoke_boundary_completion.md`](hc7_six_spoke_boundary_completion.md)
at source SHA-256

```text
b56fc75d796976e084ea7b94642d96419e620ca7c564a2b427be9359d580a8d3
```

This is a separate internal mathematical audit, not external peer review.
An earlier draft was RED because it chose a boundary neighbour of `r_0`
without assuming one existed.  The audited revision adds that hypothesis
explicitly.

## Checks

1. **Injection lemma.**  For zero or one distinct forbidden labels there
   are at least five allowed labels.  With two forbidden-label classes, one
   representative may use the other class's label and the remaining four
   objects inject into the four labels outside the two forbidden labels.
   With at least three classes, cyclically assigning the class
   representatives produces no directed two-cycle, while every remaining
   object is assigned outside the entire forbidden-label set.  All
   assignments are injective and avoid each object's forbidden label.
2. **Branch-set count and disjointness.**  The sets
   `H={h,r_0,y_0}`, `V(P)`, and `Z_i={r_i,f(i)}` are exactly seven
   pairwise disjoint sets because `A`, `Y`, and `B` are disjoint and `f` is
   injective.
3. **Connectivity.**  `H` contains the path `h-r_0-y_0`; every `Z_i`
   contains its defining edge; and `P` is connected by hypothesis.
4. **Adjacency.**  `H` meets `P` through the boundary contact at `y_0`,
   `H` meets every `Z_i` through `hr_i`, and `P` meets every `Z_i` through
   `f(i)`.  If `Z_i,Z_j` were nonadjacent, the two absent cross-edges would
   force `f(j)=m_i` and `f(i)=m_j`, the excluded two-cycle.  Thus the seven
   sets form an explicit `K_7`-minor model.
5. **Five-neighbour variant.**  The explicit edge `hy_0` makes
   `{h,y_0}` the first connected branch set; the remaining check is
   unchanged.
6. **Wheel corollary.**  The hypothesis is that `G[A]` is the wheel, not
   merely that it contains one.  A rim vertex consequently has exactly
   three neighbours in `A`, hence at least six in `Y`.  For rim order at
   least six Theorem 2.1 applies.  For rim order five the hub has five
   neighbours in `A`, so its host degree at least nine forces a boundary
   neighbour and Corollary 2.2 applies.

## Trust boundary

The proof does not control an arbitrary positive-list-excess core.  It
requires one common centre and five or six literal neighbours having the
stated boundary contacts, as well as a connected boundary-full subgraph on
the opposite shore.  It neither synchronizes boundary colourings nor proves
`HC_7`.
