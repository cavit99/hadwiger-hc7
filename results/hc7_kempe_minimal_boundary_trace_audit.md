# Audit of the Kempe-minimal boundary-trace theorem

**Verdict:** GREEN for Lemma 2.1, Theorem 3.1, and Corollary 3.2 in
[`hc7_kempe_minimal_boundary_trace.md`](hc7_kempe_minimal_boundary_trace.md)
at source SHA-256

```text
1a2779dd1a5a5cfdc7e576cdb422c7c06839c01cabcc55a9202e123101bb6d35
```

This is a separate internal mathematical audit, not external peer review.

## Checks

1. Kempe switches in the contracted minor preserve both contracted
   endpoint equalities and hence remain in the normalized colouring class.
2. The incidence quantity is exactly the sum of the two changing boundary
   neighbourhood sizes.  Their union is invariant, so inclusion-exclusion
   gives the overlap-difference formula.  The displayed list-excess formula
   differs from this quantity by a fixed host constant.
3. If no bichromatic component meets both chosen boundary blocks, switching
   every component meeting the first block merges exactly those two blocks.
   They are anticomplete in the boundary graph and their union remains
   independent.
4. Removing zero or one singleton, or two nonadjacent singletons, lowers
   the singleton-block clique number by at most one.  The merger therefore
   cannot increase demand.  Lexicographic minimality first forces unchanged
   incidence and demand, after which the smaller block count is a
   contradiction.
5. A shortest mixed-component path has no internal contracted boundary
   object.  Deleting those objects leaves precisely the two anticomplete
   open shores (with the contracted entrance vertices removed), so the
   interior is shore-confined.
6. The source correctly handles lifting: each endpoint which is a
   contraction image can require its distinguished monochromatic entrance
   edge.  Up to two such endpoint edges may occur, and the lift is not
   asserted to be a proper bichromatic path in the double-deletion graph.

## Trust boundary

The theorem supplies pairwise blockwise quotient support only.  It proves
no laminarity, path disjointness, literal branch-set ownership, `K_7` minor,
compatible separator, positive-excess bound, or `HC_7`.
