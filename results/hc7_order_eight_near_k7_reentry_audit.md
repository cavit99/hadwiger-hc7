# Internal audit of near-`K_7` re-entry at the order-eight separation

**Audit status:** GREEN.

**Audited mathematical-content SHA-256:**
`f72e71a577e69c02be1a517a37c4a30e47ccae36785ad6aac3e996aba2eb4b42`

**Current audited source revision SHA-256:**
`afe7934f70879d4ea25dd1487b1c750d8c2a9dba97c61abe35ac079a5e361e18`

Relative to the previously audited source revision
`b592dd453073707c56fdc10b68b472dbd9f3c95698cc71cbc2a0c1690db4a622`,
the current revision only narrows the literature note after Lemma 2.5: the
counterexample concerns an attempted connected-tree corollary of the
extremal forest theorem, not that theorem's literal forest-minimality
statement.  No lemma, proof, or open target changed.  This is a separate
internal audit, not external peer review.

## Verdict

No mathematical defect was found in Lemmas 2.1--3.4 or Theorem 4.1.
The conjectural split-or-pair target in Section 5 was correctly identified
as open and was not treated as a proved conclusion.

## Checks performed

1. All 21 adjacencies in the seven branch sets of Lemma 2.1 were checked.
   The strengthened cross-adjacency condition gives exactly the adjacency
   between `V(g) union X` and `Y union {x}`.
2. The attachment-tree test and the cross-Helly argument in Lemma 2.3 and
   Corollary 2.4 are valid.  The general two-family subtree fact overlaps
   earlier bi-Helly material in the archive and is not claimed as novel.
3. The self-contained shortest-path proof of Lemma 2.5 is valid.  For each
   selected boundary neighbour, the path stops at its first vertex in the
   outside neighbour set.  The connected union therefore omits at least
   two old tree vertices and adds only one new vertex.
4. Deleting the two named edges destroys at most two members of a
   seven-path internally vertex-disjoint family, so the common deletion
   graph is five-connected.  The common-deletion colouring theorem,
   `HC_6`, spanning-model absorption, and the double contraction give all
   claims in Lemma 3.1.
5. The Kempe interchange in Lemma 3.2 preserves the bichromatic named edge
   whether or not its endpoint colours include the common colour.  The
   excluded set leaves at least three protected second colours.
6. Menger's theorem gives the exact dichotomy in Lemma 3.3.  A one-vertex
   separator lies in every protected bichromatic component and hence has
   the common colour.  Lemma 3.4 correctly obtains a different neighbour
   of each protected colour on each endpoint side.
7. The connectivity-only strengthening is correctly excluded by the
   cited join of `K_2` with the icosahedral graph.

## Scope

The audit establishes the displayed branch-set construction, the
attachment-tree normal form, and the protected-connector structure.  It
does not establish that a protected cycle produces a repair split, or that
the two nominated separator vertices meet every `K_5` model.
