# Independent audit: distributed-row port exchange

## Verdict

**GREEN after repair.**  The local theorems are valid under their written
hypotheses.  They do not prove that a raw seven-root-trichotomy adhesion
supplies the distinct ports, sectors, packets, or opposite-side state needed
to invoke them.

## Necessary repair found during audit

The original common-packet statement did not require the packet and the
expansion skeleton to be disjoint from the three fixed row bags.  That
omission was real.  On the literal mismatch cycles

\[
 L=(\ell_0\ell_1\ell_2\ell_3),\qquad
 R=(r_0r_2r_1r_3),
\]

with matching edges \(\ell_i r_i\), take three pairwise adjacent singleton
rows \(a,b,c\), let \(b,c\) meet every \(\ell_i\), let \(a\) meet only
\(\ell_2,\ell_3\), choose deficient corners \(0,1\), and take the proposed
packet to be the already-used row \(\{b\}\).  This satisfied the old wording
but has treewidth at most five: the elimination order

\[
 a,b,c,r_0,r_1,\ell_2,\ell_0,\ell_1,\ell_3,r_2,r_3
\]

has fill degrees \(4,5,4,3,3,4,4,3,2,1,0\).  Hence it has no \(K_7\)
minor.  The current explicit disjointness hypotheses exclude exactly this
failure.

## Checks

1. The width-five witness in Section 0 was independently reconstructed; its
   displayed fill degrees are exact.
2. Contracting four disjoint cyclic sectors preserves the two labelled
   cyclic orders.  Lifting the rooted port-matching \(K_4\) puts each whole
   sector only into its corresponding branch set, so every retained
   sector-row contact is literal.
3. Simultaneous packet promotion preserves connectedness and disjointness
   because packets are pairwise disjoint, disjoint from all seven old bags,
   and assigned to exactly one row.
4. Off-skeleton common-packet promotion retains all six corner connections.
   On-skeleton promotion removes only the selected corner connection and
   retains literal packet-to-corner edges at its ends; this gives precisely
   the stated \(K_7^-\) model.
5. Under the explicit global minimum-centre and first-edge hypotheses, the
   deficient corner remains the same literal bag \(X\).  The resulting
   one-hole model therefore contradicts the audited height gap.
6. The equality splice performs operations strictly in opposite open shores
   of the same actual separation.  Equality of the labelled partitions of
   the actual adhesion permits one palette permutation and hence a proper
   six-colouring of the original graph.

## Trust boundary

The result closes an unbounded distributed-contact family, but its global
extraction remains open.  In particular, fullness of a component to an
adhesion does not imply pointwise contact with each fixed row inside that
component.
