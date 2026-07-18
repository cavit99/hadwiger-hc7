# Audit: disjoint trace-linkage reflection

**Verdict:** GREEN.

**Audited source:** `hc7_disjoint_trace_linkage_reflection.md`

**SHA-256:**
`931b70417d8ec307b54088c862384983d6b172d2fc93daefca7a66ea221a4dcd`

This was a separate internal mathematical audit of the exact source revision
above.  It is not external peer review.

## 1. Simultaneous contractions

The connected subgraphs `X_i` are pairwise vertex-disjoint, so their
spanning trees may be contracted simultaneously.  At least one edge is
contracted whenever a nonsingleton trace exists.  Thus the resulting graph
is a proper minor and has a proper six-colouring under the stated
minor-criticality hypothesis.

Pullback to the unchanged far closed shore is valid.  Independence of each
`I_i` handles its internal pairs; every edge between two traces survives as
an edge between their contraction representatives; and every edge from a
trace to an unchanged far-shore vertex survives at the corresponding
representative.  Vertices of `R` are untouched because every `X_i` lies in
`L union I_i`.  Hence the pulled-back colouring is proper and every row
trace is monochromatic.  The boundary-free row triggers the separately
audited five-row reflection theorem.

When all traces are singleton or empty, deleting one vertex of the nonempty
side `L` is a proper minor and leaves the entire far closed shore unchanged,
so the same reflection argument applies.

## 2. Two-pair and disc consequences

Two vertex-disjoint pair paths can be trimmed at their named endpoints; all
their internal vertices then lie in `L`, and they satisfy Theorem 2.1.

Under the additional seven-connectivity and exact order-seven hypotheses,
the closed-shore theorem makes the four-root pair internally
four-connected.  Fabila-Monroy--Wood Lemma 2 supplies the stated web when
the prescribed pairing is absent.  An actual vertex in a facial-triangle
attachment would lie on the root-free side of a relative separation of
order at most three, contradicting internal four-connectivity.  Thus all
actual vertices lie in the planar rib, and deleting only auxiliary
completion edges yields the claimed literal disc embedding.  The source
does not mistake a completion edge for a host edge.

## 3. Trust boundary

The theorem proves a sufficient linkage-to-colouring implication.  It does
not prove that the linkage exists, nor does the disc alternative by itself
give a `K_7` minor, common boundary partition, or two-vertex transversal.
Those limitations are stated accurately.
