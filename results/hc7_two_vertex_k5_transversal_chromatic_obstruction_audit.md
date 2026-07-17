# Independent audit: two-vertex `K_5`-model transversals

**Verdict:** **GREEN — separate internal audit.**

This audit checked the theorem revision with SHA-256

```text
6420cfd2b2d018070446fca5b69240593b4673c4f801f69c6e883a029c0b8d05
```

for
[`hc7_two_vertex_k5_transversal_chromatic_obstruction.md`](hc7_two_vertex_k5_transversal_chromatic_obstruction.md).
This is an internal mathematical audit, not external peer review.

The promoted source has SHA-256
`4c3c4283c0fa1c74a8711467a49b946bf056d2df53f6edce15f7c765d6fed1f9`.
It differs from the audited revision only in the opening status line, which
records this GREEN verdict; no theorem statement, proof, dependency, or
scope claim changed.

## Checks performed

1. The established `t=5` case of Hadwiger's Conjecture gives a proper
   four-colouring of every `K_5`-minor-free graph.
2. If `|P|<=2`, assigning the vertices of `P` pairwise distinct fresh
   colours uses at most two further colours and is proper regardless of
   the edges inside `P` or from `P` to `G-P`.  Thus `G-P` being
   `K_5`-minor-free implies `chi(G)<=6`.
3. A `K_5`-minor model in `G` avoids `P` exactly when all of its branch
   sets lie in `G-P`, equivalently when it is a `K_5`-minor model of
   `G-P`.  The minor-model-transversal formulation is therefore precisely
   the contrapositive of the colouring statement.
4. The consequence for a hypothetical `HC_7` counterexample uses only
   `chi(G)=7`.  Connectivity, contraction-criticality, and a selected
   minor model are correctly stated as unnecessary.

## Trust boundary

The only external input is the established `t=5` case of Hadwiger's
Conjecture.  The note does not construct a `K_5` model, identify a
colour-compatible separation, or prove any statement about transversals
of larger minor models.  Its exact conclusion is that no set of at most
two vertices can meet every `K_5`-minor model in a seven-chromatic graph.
