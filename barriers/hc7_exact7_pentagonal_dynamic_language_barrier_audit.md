# Internal audit of the pentagonal dynamic-language barrier

**Verdict:** GREEN for the exact source and verifier revisions identified
below.

This is a separate internal audit, not external peer review.

## Audited revisions

- barrier: `hc7_exact7_pentagonal_dynamic_language_barrier.md`
- barrier SHA-256:
  `67d105e2081dfa54698951efd437a910cc7a5debff4f614c0159424ad26a4cea`
- verifier: `hc7_exact7_pentagonal_dynamic_language_barrier_verify.py`
- verifier SHA-256:
  `8df7d05e7c2b89782981319ce5553e0eaade78e729137f815272f3a2da3c3f93`

The audit checks the finite partition classification, the two disjoint
trace-complete languages, the sharp minimum-language theorem, the
closed-shore bounds, the graph-realization argument, and the stated trust
boundary.

## 1. Boundary partitions

In `K_2\vee C_5`, the two universal adjacent vertices must be distinct
singleton colour blocks.  On the remaining five vertices, every
nonsingleton independent block is an edge of the complementary five-cycle,
and distinct nonsingleton blocks form a matching.  A proper partition into
at most six blocks therefore uses a matching of order one or two.  The five
one-edge matchings and five maximum matchings give exactly the ten states
`s_i,d_i` claimed in Lemma 1.1.  Their block counts are respectively six
and five.

The only nonempty independent boundary sets are the seven singletons and
the five complementary-cycle edges.  Every such set occurs as an exact
block in both parity families: `s_i` covers its defining edge, every edge
also belongs to two maximum matchings, and the singleton assertions follow
from the unmatched vertices of the `d_i` and from nonincident `s_j`.
Thus Theorem 2.1 is correct as a finite existential response system.  The
source correctly warns that this operation-by-operation assignment is not
claimed to arise from one common host colouring.

## 2. Minimum trace-complete languages

Two states cover at most four of the five two-vertex traces, so a
trace-complete family has order at least three.  At equality, the pair-block
counts must be `2,2,1`.  The two maximum matchings are edge-disjoint and the
single-pair state uses the remaining complementary-cycle edge.  For an edge
`v_i v_{i+1}`, this is precisely

\[
                         \{s_i,d_i,d_{i+1}\}.
\]

The singleton traces then hold automatically.  Two such triples share a
`d` state exactly when their defining cycle edges share an endpoint, so
they are disjoint exactly for vertex-disjoint defining edges.  This proves
Theorem 3.1.

For an actual two-shore separation, contracting one connected full shore
together with any independent boundary set makes that set one exact block
on the unchanged opposite closed shore.  Proper-minor six-colourability
therefore makes each shore language trace-complete.  A common boundary
partition would allow colour permutation and gluing, so the languages are
disjoint.  The ten-state classification and the order-three lower bound
then give

\[
  3\le |\mathcal E_L|,|\mathcal E_R|\le7,
  \qquad |\mathcal E_L|+|\mathcal E_R|\le10.
\]

The equality conclusions in Corollary 3.2 follow from the preceding
classification.

## 3. Realization and one-step criticality

The invocation of Dvořák--Swart, Theorem 3 of *A note on extendable sets of
colorings and rooted minors* (arXiv:2504.07764), has the required scope:
each permutation-closed family of labelled six-colourings of the boundary
has a finite exact realizer.  Both parity families equate every nonedge of
the intended boundary graph, so adding exactly the edges of
`K_2\vee C_5` preserves the intended relation and forces the boundary to be
induced.

Deletion-minimizing each realizer with respect to its proper boundary
language makes every remaining open vertex deletion or nonboundary edge
deletion create a new proper state.  That state belongs to the opposite
parity family.  For an edge deletion, its endpoints must have the same
colour in a witnessing colouring, or the deleted edge could be restored;
the same colouring therefore descends through contraction.  The auxiliary
partitions equating one boundary edge and making all other boundary
vertices singleton correctly handle boundary-edge deletion and contraction,
and their restrictions handle boundary-vertex deletion.  Consequently the
glued graph is non-six-colourable while every single elementary deletion or
contraction is six-colourable.

The source correctly does **not** promote this to all-proper-minor
six-colourability: a later contraction of an already six-colourable graph
may increase chromatic number.  It also keeps connected-full augmentation,
connectivity amplification, one-step minimality, and clique-minor exclusion
separate.

## 4. Verifier replay

Running

```text
python3 barriers/hc7_exact7_pentagonal_dynamic_language_barrier_verify.py
```

returns:

```text
proper boundary partitions 10
six-block / five-block 5 5
nonempty independent traces 12
minimum trace-complete size 3
minimum trace-complete families 5
disjoint pairs of minimum families 5
oriented complementary trace-complete splits 202
PASS: exact-seven pentagonal response languages remain disjoint
```

The script independently enumerates all set partitions of the seven
labels, checks propriety and the six-block bound, verifies every independent
trace and singleton cylinder in both parity families, and exhausts all
subfamilies of the ten-state space.  Its tests agree with the written
classification.

## 5. Exact scope

The barrier proves that static exact traces, portal singleton responses,
and independently chosen deletion/contraction responses need not force the
two boundary languages to intersect.  It is not a counterexample to
`HC_7`, to the now-proved host-level pentagonal completion theorem, or to a
theorem using simultaneous `K_7`-minor exclusion, all-proper-minor
six-colourability, and labelled branch-set geometry.  No unresolved gap
remains within this stated finite and realization-level scope.
