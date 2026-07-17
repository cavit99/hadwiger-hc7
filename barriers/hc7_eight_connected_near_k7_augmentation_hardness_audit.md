# Audit of the connectivity-only near-`K_7` augmentation hardness reduction

**Verdict:** GREEN (separate internal audit)

**Audited revision:** SHA-256
`f165b53691bc24afbad933d4f334ab9c1ce02fb10f79cad42b1e9f266b7542b6`
of `hc7_eight_connected_near_k7_augmentation_hardness.md`.

## Checks performed

For an arbitrary seven-connected graph `F`, the stated order, minimum
degree, and nonplanarity conclusions are valid, so Lo's Theorem 1.3
applies and supplies a `K_6`-minus-one-edge minor.  The join `K_1 vee F`
is eight-connected under the explicit deletion split, and the universal
singleton lifts the near-`K_6` model to a `K_7`-minus-one-edge model.

If the proposed augmentation produced a `K_7` model, the proof correctly
handles both possibilities: no branch set uses the universal vertex, or
exactly one does.  In either case six pairwise adjacent branch sets remain
inside `F`, giving a `K_6` minor.

The source statements and numbering were checked.  Lo's Theorem 1.3 has
the quoted hypotheses and conclusion.  The authors' 26 June 2024 revision
of Chudnovsky--Scott--Seymour--Spirkl states the exact conclusion as
Conjecture 1.6 and the stronger minimum-degree assertion as Conjecture 1.4.

## Scope

The note proves a hardness implication, not the falsity of the
connectivity-only augmentation claim.  It correctly concludes only that
using that claim as the next local lemma would replace the `HC_7` gap by
another major open problem.  No unresolved gap remains in this stated
scope.
