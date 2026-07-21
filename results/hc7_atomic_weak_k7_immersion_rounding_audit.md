# Independent audit of atomic weak-`K_7` immersion rounding

**Status:** separate internal audit GREEN, 21 July 2026.

This is an internal mathematical audit, not external peer review.

## Revision audited

- theorem:
  [`hc7_atomic_weak_k7_immersion_rounding.md`](hc7_atomic_weak_k7_immersion_rounding.md)
- exact SHA-256:
  `67bb92bade54a9cf63dbe68015e598370ff16ff883d0b63450f7922c36bbf0be`

## Verdict

GREEN.  The stated atomic classification, common-frame interface,
octahedral residual frame, paired-linkage construction, and
contact-preserving singletonization are correct under their displayed
hypotheses.  No unresolved assumption or proof defect was found.

## Checks performed

1. The role count includes transit through a branch vertex.  With total
   excess `M=1`, the two cases in Theorem 3.1 are exhaustive.
2. In the common-end case the displayed allocation gives seven disjoint
   connected branch sets and repairs both routes through the collision.
   In the other cases deleting one collision route leaves the claimed
   subdivision, and the singleton-root allocation and spanning absorption
   preserve every required adjacency.
3. In Theorem 3.3, the provenance partition has only the two possible
   missing pairs.  If the collision vertex meets all three clean bags, the
   seven displayed branch sets give an explicit `K_7` model.  Otherwise
   \(N(C)\subseteq N(x)\), seven-connectivity gives the lower boundary bound,
   and the degree of `x` gives the upper bound.
4. Both proper-minor contractions in Corollary 3.4 are connected and
   produce an exact independent boundary colour block under the explicit
   six-colourability hypothesis.
5. Theorem 3.5 repairs precisely the two missing common-frame pairs.
   Corollary 3.6 correctly proves that both pairs are absent in a
   `K_7`-minor-free host and that the residual bag-adjacency graph is
   exactly `K_{2,2,2}`.
6. Proposition 3.7 starts from the provenance partition constructed in
   Theorem 3.3.  Its retained paths preserve both collision contacts; every
   remaining component of `(G-x)` outside the seven seeds has at least
   seven neighbours and can be absorbed into a non-`e` seed.  Thus the
   new `e` bag is the literal singleton without losing the frame.
7. The cited weak-immersion theorem and Mader edge bound have the scope
   asserted in the impact section.  The deductions `M=0` implies a
   topological `K_7` and `|L|>=10` are arithmetically correct.

## Trust boundary

The result does not prove that the guaranteed weak `K_7` immersion can be
chosen with `M<=1`, that a full `(M,T,H,L)` minimizer collides at degree
at most nine, or that an extremal provenance allocation forces the paired
linkage.  It also does not complete the singleton-root near-`K_7` model or
give a strict response-preserving reduction.  These are disclosed research
gaps, not conclusions of the audited theorem.
