# Independent audit: global thin-shore minimality

**Verdict:** GREEN, with the scope in Section 3 of the source essential.

**Audited source:**
`results/hc7_exact7_global_thin_shore_minimality.md`.

## 1. Family and existence

The family consists only of literal decompositions of the fixed finite host
`G`; hence it is finite.  Conditional on one actual `(1,2)` separation
existing, a minimum of `|L|` exists.  No compactness, canonical colouring,
or choice of a minor model is being used.

The ordered orientation is unambiguous.  The two maxima are unequal, so
the same unordered separation has exactly one orientation satisfying
`(nu_L,nu_R)=(1,2)`.

## 2. Strict receiver

If the receiver data really verify

\[
 |S'|=7,\qquad (\nu_{L'}^{S'},\nu_{R'}^{S'})=(1,2),
 \qquad |L'|<|L|,
\]

then they define another member of the same globally minimized family.
Finiteness gives `|L'|<|L|`, so the contradiction is immediate.  The
returned partition may be arbitrary because membership in the minimized
family does not mention it.

## 3. Atomic application

The promoted packet-transfer theorem explicitly supplies all three facts
used by Corollary 2.2: an actual seven-boundary, lobe-oriented vector
exactly `(1,2)`, and `D,E` proper subsets of the old `A`.  Therefore, **if
that old `A` was selected by the global minimization**, the old receiver
qualification about paired versus arbitrary high-demand states disappears
for this branch.

This audit does not assert that an argument which first minimized over a
smaller stateful subclass may silently replace that choice by the global
minimum.  Any upstream reduction invoked after the choice must apply to
the globally selected separation or re-establish its hypotheses without
changing the thin shore.

## 4. Nonextensions

The proof does not apply when:

1. the returned vector is `(1,1)`;
2. the strict lobe is the packet-two side of a reversed `(1,2)` cell;
3. packet fullness or the opposite two-packet maximum is only conjectured;
4. the output is a near-model rotation rather than an actual separation;
5. the boundary order changes; or
6. strictness refers to a model bag or carrier, not the literal open shore.

Subject to these exclusions, the rank is genuinely global and cannot cycle.

## 5. Audit of the state-uniform formulation

The formulation in Section 4 of the source is logically sound as a target.
It quantifies over the entire handoff-closed family before mentioning the
returned state.  At a global minimum its smaller-cell alternative is
impossible, so no state needs to be transported into the receiver.

It is not yet a proved local theorem.  In particular, the current atomic
decoder may be invoked only after paired-triangle, connected-rich and twin-
seam normalizations.  The existing record does not prove that an arbitrary
global minimum belongs to that subclass, nor that every reduction into the
subclass preserves the same `L`.  This caveat prevents the minimum argument
from being used circularly.
