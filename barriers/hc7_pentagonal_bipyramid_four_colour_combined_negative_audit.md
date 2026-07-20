# Audit of the four-colourable combined-negative PB core

**Verdict:** **GREEN** for the exact source and verifier revisions below.

**Audited source:**
[`hc7_pentagonal_bipyramid_four_colour_combined_negative.md`](hc7_pentagonal_bipyramid_four_colour_combined_negative.md)

**Source SHA-256:**
`c39e1739bc24dfe70e4bebeec07de1275943ef83b5ae8cee8c34df8fad8f0771`

**Verifier SHA-256:**
`661d1970107c2a2d312e6ea011b79f77ec82504372d39c9d0d019ad0e627682c`

This is an internal mathematical audit, not external peer review.  The
example refutes only the whole-column anchored model inference.  It does
not refute, and in fact explicitly satisfies, the weaker paired-rooted
model conclusion needed in the host graph.

## 1. Host and local-negative checks

The verifier constructs the fourteen displayed vertices and thirty-seven
edges.  It checks that the seven two-vertex induced paths have contact graph
exactly the pentagonal bipyramid, that the graph has connectivity five, and
that it is nonplanar.

For each column, its only connected two-part cut is the internal path edge.
The cyclic contact calculation checks that none is four-label alternating.
For every adjacent rim pair, exhaustive enumeration of disjoint connected
subsets of its four vertices checks the exact negative Two Paths condition.

## 2. Whole-column search

For every choice of five anchor columns, the four vertices in the two
remaining columns are assigned independently to one of the five branch
sets or left unused.  This gives exactly

\[
                         {7\choose5}6^4=27,216
\]

assignments.  Connectedness and all ten pairwise adjacencies are tested.
This is exhaustive for a `K_5` model whose five bags contain five distinct
whole columns, and none exists.

## 3. Paired-rooted and chromatic certificates

The five branch sets displayed in Section 4 of the source are connected,
pairwise disjoint and pairwise adjacent.  Each contains a vertex with
second coordinate zero and one with second coordinate one.  Consequently,
when those two coordinate classes are the literal root-neighbourhood sets,
the model is paired-rooted and the two roots complete it to `K_7`.

The displayed four-colouring is proper on every edge.  The four vertices
`(0,0),(0,1),(4,0),(4,1)` induce a `K_4`, so the chromatic number is exactly
four.

## 4. Trust boundary

The example has no operation-specific proper-minor response family and is
not a candidate counterexample to `HC_7`.  It shows that whole-column
anchoring is too restrictive and that nonplanarity is not the correct
opposite of root alignment.  It supports, but does not prove, the target

\[
             \chi(F)\le4\quad\text{or paired-rooted `K_5`}.
\]

All claimed finite properties are checked at the recorded hashes.
**GREEN.**
