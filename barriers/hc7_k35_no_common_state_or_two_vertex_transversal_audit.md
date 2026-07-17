# Audit: `K_{3,5}` boundary-state obstruction with no two-vertex transversal

## Verdict

**GREEN — separate internal audit.**

This audit checked the theorem revision with SHA-256

```text
a2ae9052b307cccae5a9499729fe8a5a2f7330c81c501910c28ca075542bf4dc
```

for
[`hc7_k35_no_common_state_or_two_vertex_transversal.md`](hc7_k35_no_common_state_or_two_vertex_transversal.md).
This is an internal mathematical audit, not external peer review.

## Checks performed

1. The cited connected-full augmentation contains an open-side edge
   `l_xc` for every boundary vertex `x`.
2. False-twin amplification with classes of order seven replaces this
   edge by a fixed `K_{7,7}`, preserves the exact boundary extension
   relations, and makes the glued graph seven-connected.
3. After deleting any set `P` of at most two vertices, each bipartition
   class of that fixed `K_{7,7}` retains at least five vertices.
4. In the surviving `K_{5,5}`, the sets

   \[
     \{a_i,b_i\}\quad (i=1,2,3,4),\qquad \{a_5\}
   \]

   are disjoint connected branch sets and are pairwise adjacent.  They
   therefore form a `K_5`-minor model in `G-P`.
5. The same `K_{7,7}` contains a `K_7` minor, using six paired branch
   sets and one singleton, so the theorem's exclusion from the actual
   `HC_7` hypothesis class is explicit and correct.
6. The source barrier supplies the remaining stated properties: the
   order-eight `K_{3,5}` boundary, connected full shores,
   seven-connectivity, chromatic number seven, disjoint proper
   six-colouring extension languages, exact independent-block responses,
   the six named deletion/contraction responses, and the `K_7`-minor-free
   quotient `K_{2,3,5}`.
7. The rigid-boundary splice theorem is invoked only as a sufficient
   positive hypothesis.  Here “uniquely five-colourable” means chromatic
   number exactly five and uniqueness of the five-colour partition up to
   permutation.

## Correction made during audit

The draft originally said that no five named model branch sets support the
boundary.  The construction proves only that it supplies no specified five
labelled `K_5`-model branch sets whose literal geometry supports the
boundary; it does not exclude the existence of such models.  The audited
revision uses the narrower, correct statement.

## Trust boundary

The audit confirms the new no-two-vertex-transversal conclusion and its
combination with the properties already proved in the cited realization
barrier.  It does not independently reprove the Dvorak--Swart exact
colouring-relation realization theorem.

The construction is not `K_7`-minor-free, is not asserted to be fully
contraction-critical, and does not supply the canonical five labelled
branch sets.  It is therefore a barrier to static extension-language
arguments, not a counterexample to `HC_7` and not a refutation of a theorem
that uses all three missing host-level hypotheses.
