# Independent audit: label-preserving six-linkage classification

**Verdict:** GREEN.  The finite matching and one-bridge classifications,
the exact `K_7`-minor detector, the oriented residual tables, and the
seven-connectivity cut argument are correct at the stated quotient level.
The residual arc covers in (5.2) are abstract feasibility certificates;
they are not simultaneous path systems in a seven-connected host, and the
source note correctly makes no such claim.

**Audited theorem:**
`results/hc7_disjoint_k6minus_support6_linkage_classifier.md`.

**Theorem SHA-256:**
`fd570964333ab4388e0214445495b348b2151e5df663c88f5bb39b2e3a0b4a05`.

**Audited verifier:**
`results/hc7_disjoint_k6minus_support6_linkage_classifier.py`.

**Verifier SHA-256:**
`b27e4505f047ccd5495727d11a69af8c37cdf3468bbcdca69397c6c8aec8884d`.

The audited mathematical text had source hash `5138b774...`; the current
hash differs only by changing the status from audit-pending to audited,
updating the retained verifier's repository path after promotion, and
declaring the verifier's already-audited NetworkX 3.6.1 dependency through
PEP 723 rather than an ignored local runtime.

## 1. Configuration and normal forms

Once `Q={0,1,2,3}` is fixed as a clique and `45` as the split edge, the
only optional edges in the six-vertex support are the eight
`Q`--`{4,5}` contacts.  Every vertex of `Q` must have contact status
`4 only`, `5 only`, or `both`.  Irredundancy is exactly the requirement
that at least one vertex has each of the first two statuses.  The verifier
enumerates all

\[
                       3^4-2\cdot2^4+1=50
\]

labelled status patterns.  Thus its final invariant check covers every
support allowed by Section 1, not just the displayed minimal forms.

Deleting surplus common contacts leaves a nonconstant two-colouring of
the four vertices of `Q` by the endpoints `4,5`.  Up to permuting `Q` and
interchanging `4,5`, its class sizes are `3+1` or `2+2`.  These are exactly
the two normal forms in the theorem.

For a fixed preimage pair of the missing right edge, the remaining four
right vertices may be matched in one fixed order: every permutation of
those four vertices extends to an automorphism of `K_6^-`.  The verifier
therefore loses no matching cases by using the fixed `zip` in
`matching_for`.

## 2. Exactness of the minor search

The at-most-twelve-vertex detector is exhaustive.  If a seven-branch-set
model on `n<=12` vertices has `s` singleton bags, then

\[
                         n\ge s+2(7-s)=14-s,
\]

so `s>=14-n`; all singleton bags form a clique.  The verifier tries every
possible exact value of `s`, every singleton clique of that order, and
every collection of the remaining pairwise disjoint connected bags of
order at least two.  It tests adjacency from every non-singleton bag to
every singleton and between every pair of non-singleton bags.  Unused
vertices are correctly permitted.  Consequently a returned model is a
valid `K_7` model and every possible model is represented in the search.

The low-degree recurrence is also an equivalence.  A singleton bag of a
`K_7` model needs six distinct neighbours, one in each other bag.  If
`d(v)<6`, a model therefore either avoids `v`, or the connected
non-singleton bag containing `v` contains an incident edge `vw`.  These
two alternatives are exactly `G-v` and `G/vw`.  In a one-bridge quotient
the two added subdivision vertices have degree three, so two applications
reduce the problem to the proved at-most-twelve-vertex search.

As an independent algorithmic cross-check, I converted each of the thirty
minimal bare quotients to bit-set adjacency and ran a pure
edge-contraction search which does not enumerate branch-set partitions.
It agreed with the retained verifier on every quotient.  The retained
verifier itself was then run in full with NetworkX 3.6.1 and returned:

```text
general_contact_patterns 50
GREEN: exact matching and one-bridge classifications verified
```

The full output reproduced all eight raw bad-matching rows, all eight raw
one-bridge rows, the three oriented tables, and the three cut-cover sets
hard-coded in the script.

## 3. Matching and bridge tables

For each of the fifty contact patterns and all fifteen preimage pairs, the
computed answer is `K_7` exactly when the two preimages are adjacent on
the left.  This proves Theorem 2.1 in its invariant form.  In a negative
case the preimages must therefore be a singleton of `Q` and the opposite
endpoint of the split edge, exactly as stated.

The one-bridge graph correctly represents an external path with internal
attachments on two distinct linkage paths: subdivide the corresponding
matching edges at the attachment points and join the subdivision vertices.
The raw residual lists in the script reduce to the orbit representatives
in the theorem under the stated symmetries.  Adding surplus support edges
cannot destroy a clique minor, so it can only delete residual entries;
the monotonicity statement for nonminimal supports is valid.

For an oriented connection from `P_i-b_i` to `P_j-j`, contract the first
attachment toward `i`, the second toward `b_j`, and the connecting path
between them.  This creates the edge `i b_j`, including when an attachment
is an allowed endpoint.  The oriented table tests exactly this edge
augmentation.  Every listed target is negative under the exact detector,
and every omitted target is positive.

## 4. Seven-connectivity deduction

For fixed `i`, deleting the other five left endpoints and `b_i` deletes
six vertices.  Seven-connectivity leaves a connected graph.  In that
graph, `P_i-b_i` is connected and disjoint from the connected union of
`B-b_i` with all tails `P_j-j`, `j!=i`.  A shortest path between the two
unions has interior outside both endpoint supports and all six linkage
paths.  Its far endpoint lies on some `P_j-j`, giving precisely the
oriented connection used by the table.

The subset form is the same argument.  For nonempty proper `T`, deleting
`b_i` for `i in T` and the left endpoint `j` for `j notin T` again deletes
six vertices.  When the two displayed induced endpoint supports are
connected, their surviving linkage portions form two disjoint connected
sets; seven-connectivity forces a path from a source in `T` to a target
outside `T`.

The verifier checks every one of the 62 nontrivial subsets and every
applicable connected bipartition.  Each arc set in (5.2) consists only of
negative oriented entries and crosses all applicable bipartitions.  This
correctly proves the limited negative conclusion: repeating the endpoint
cut inequalities alone cannot select a closing orientation.  It does not
prove that those abstract arcs can be realized simultaneously, and the
theorem explicitly reserves simultaneous realizability and attachment
order as the remaining issue.

## 5. External source and exact scope

The path-forcing template agrees with Rolek--Song, *Coloring graphs with
forbidden minors*, Journal of Combinatorial Theory B 127 (2017), Lemma
1.9: after a six-vertex deletion, connectedness supplies a path between
two members of a linkage and contraction of suitable path segments creates
the extra endpoint adjacency.  The paper's lemma is stronger in its own
two-`K_6` setting; the source note uses only this elementary subargument.

The audited result classifies a deliberately edge-deleted matching
quotient and one additional linkage bridge.  It neither proves that a
seven-connected host realizes a residual table nor closes the disjoint
support configuration.  Further host edges and several interacting
bridges remain outside the finite theorem.
