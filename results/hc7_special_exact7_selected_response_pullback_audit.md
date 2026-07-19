# Audit of selected-response pullback through a proper list-critical core

**Verdict:** GREEN for Theorem 2.1 and Corollary 3.1 in
[`hc7_special_exact7_selected_response_pullback.md`](hc7_special_exact7_selected_response_pullback.md)
at source SHA-256

```text
993af43382b88c10ba75566e2e588c9486cd28908aeaf9bfe35805508dfb895b
```

This is a separate internal mathematical audit, not external peer review.

## Checks

1. The one-edge colouring is proper on the opposite closed shore because
   its sole potentially improper edge has one endpoint inside `K`.
2. Attainment of the same exact boundary partition on the intact `K`-shore
   would align by a colour permutation and six-colour `G`.
3. Connectedness of `A` supplies a vertex `t in N_A(K)`.  Under
   `|T|=7` and `Y_0 subseteq T`, the seven vertices
   `Y_0 union {z_i,t}` exhaust `T`.  This proves `N_A(K)={t}`, excludes
   `z_j` from `T`, and makes `a_i` the unique marked entrance vertex in
   `K`.
4. The opposite side is nonempty because the original nonempty shore `B`
   lies outside `K union T`.  Seven-connectivity therefore makes every
   component of `G-T` adjacent to all seven boundary vertices.
5. Exact-seven packing and adaptive `(1,3)` reflection leave only `(1,1)`
   and `(1,2)`, up to orientation.  The exact-seven boundary classification
   and cycle-boundary completion eliminate the five-chromatic case.
6. Full-subgraph reflection is correctly oriented from the shore on which
   the selected colouring is legal toward `K`; it proves demand greater
   than the opposite packing number.
7. The bridge corollary is the exact set calculation from its two returned
   boundaries and correctly disclaims preservation of the old response.

## Trust boundary

The result produces a generic selected-response five-plus-two interface,
not the formal concentrated-order-eight provenance assumed by the older
special theorem.  It preserves the five literal vertices `Y_0` and the
one-edge witness, not the old equality partition, old full-subgraph
identities, or five branch-set labels.  Its noncomposable-placement claim
is confined to the proper-core and bridge pullbacks treated in the source.
It does not prove `HC_7`.
