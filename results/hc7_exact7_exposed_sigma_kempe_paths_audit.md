# Audit of the exposed exact-seven boundary partition theorem

**Verdict:** GREEN for Theorem 2.1, at source SHA-256
`e8495a4f1bbcc7009379af72d94a807b9ac301fae9a5bde9ae86e098f9397a07`.

The mathematical source was audited at SHA-256
`8adb13dc06505ce39e0998b14040c4da6d34203c893790ff31e225e80ae93655`.
The promoted revision changes only one dependency reference from its former
`active/` path to the promoted theorem link in `results/`; restoring that
reference reproduces the audited hash exactly.  No mathematical content
changed.

**Audit class:** separate internal adversarial audit.  This is not external
peer review.

## 1. Statement checked

The audit checked all five assertions of Theorem 2.1 in
`results/hc7_exact7_exposed_sigma_kempe_paths.md`:

1. classification of the ten at-most-six-colour boundary partitions;
2. disjointness of the two closed-shore extension languages;
3. edge coverage of each language by opposite-shore contraction;
4. existence of an exposed six-block partition; and
5. the two consecutive same-shore bichromatic connections forced by that
   partition.

Section 3 is an immediate model consequence and is not needed for the
GREEN verdict on Theorem 2.1.

## 2. Line-by-line checks

The partition classification is correct.  The adjacent universal vertices
`p,q` give two distinct singleton blocks.  On the remaining five-cycle,
nonsingleton colour classes are matchings in the complementary five-cycle.
Using at most six colours and at least five leaves exactly a one-edge or a
two-edge matching.

The gluing argument is valid.  A common equality partition permits a
permutation of all six colour names on one closed shore.  A sixth colour
absent from the boundary causes no problem because the open shores are
anticomplete.

For an edge `e=uv` of the complementary cycle, the set consisting of one
connected open shore together with `u,v` is connected.  Every other
boundary vertex is adjacent to that open shore.  After contraction and
six-colouring the proper minor, expansion therefore makes `uv` an exact
boundary colour class on the untouched closed shore.  This proves edge
coverage in both directions.

The exposed-partition count is correct.  If no six-block partition were
exposed, then in either shore every edge covered by a six-block partition
would also be covered by a two-edge-matching partition.  Hence the
two-edge-matching subfamily on each shore would cover all five cycle edges
and would have order at least three.  Language disjointness would require
six distinct two-edge matchings, but only five exist.

Finally, in a colouring inducing the exposed partition, the three
singleton cycle-root colours occur nowhere else on the boundary.  A Kempe
swap in a disconnected two-colour subgraph would create exactly one of the
two forbidden matching refinements.  Thus the asserted paths exist and
their internal vertices lie in the selected open shore.

## 3. Scope corrections

The two paths coexist in one colouring, but they need not be internally
disjoint; they may share vertices having the colour of the middle root.
The theorem alone does not produce a rooted `K_4`, rooted `K_5`, common
boundary partition, or `K_7` minor.

Most ingredients were already present in the repository.  The ten-state
classification and edge coverage are essentially Lemma 1.1 and Corollary
3.2 of `barriers/hc7_exact7_pentagonal_dynamic_language_barrier.md`, and
the singleton Kempe exchange appears in
`results/hc7_exact7_singleton_block_kempe_exchange.md`.  The new content is
the exposed-partition pigeonhole lemma and the resulting placement of both
consecutive Kempe connections in one fixed shore and one fixed colouring.

## 4. Sharp finite-language limitation

Let the complementary-cycle edges be `e_0,...,e_4` cyclically and put
`pi_i={e_i,e_{i+2}}`.  The disjoint families

\[
 \{\sigma_0,\sigma_2,\sigma_3,\pi_1,\pi_2\},
 \qquad
 \{\sigma_1,\sigma_4,\pi_0,\pi_3,\pi_4\}
\]

both cover every edge, while only `sigma_0` is exposed in the first
family.  Thus a third missing-chord connection cannot be forced from the
finite language and the elementary refinement implication alone.
