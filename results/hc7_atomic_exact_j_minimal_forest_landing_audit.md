# Internal audit of the exact atomic quotient landing theorem

**Status:** separate internal audit GREEN, 21 July 2026.

This is an internal mathematical audit, not external peer review.

## Revision audited

- result:
  [`hc7_atomic_exact_j_minimal_forest_landing.md`](hc7_atomic_exact_j_minimal_forest_landing.md)
- exact SHA-256:
  `f80a94ee8dd03e48b7ecec5f5a87016492f022436b6ade40531a316197a55bb4`

The hash was computed after the result status was changed to GREEN.  The
forest and every `F'` in the theorem are explicitly edge sets.

## Verdict

GREEN.  Under the stated all-proper-subsets minimality, the proof correctly
localizes every nontrivial fibre to `f` or `g` and gives either the displayed
`K_7`-minor model or a literal host separator of order seven.  No unproved
quotient-to-host lift is used.

## Checks performed

1. For each missing pair `ab`, `cd`, or `xe`, its six-vertex complement is
   a separator of `J`.  Splitting a fibre whose label is outside that
   separator cannot join its two remaining components.  Applying this in
   every seven-connected one-edge predecessor forces every nontrivial fibre
   image into the intersection `{f,g}`.
2. When an edge of an `f`- or `g`-fibre tree is split, replacing its quotient
   label in an antipodal six-cut by the two split images gives a seven-set.
   Each member of the omitted pair has no possible neighbour outside that
   seven-set except its nonadjacent antipode.  Seven-connectivity therefore
   makes it adjacent to both split images.  Repeating over all three pairs
   proves that each split side meets all six octahedral vertices.
3. If there is exactly one edge between the `f`- and `g`-fibres, deleting the
   six literal octahedral vertices and its endpoint in a nontrivial fibre
   leaves nonempty vertices on both fibres and deletes their unique joining
   edge.  This is an actual order-seven separator, and the stated assignment
   places every labelled fibre wholly in a closed shore.
4. If there are at least two cross-fibre edges, one fibre has two distinct
   endpoints.  An edge on their forest path separates them into connected
   sets `U,V`; the other fibre `W` is connected, and the selected edges make
   `U,V,W` pairwise adjacent.  Each meets all four bags
   `{x,a}`, `{e,c}`, `{b}`, `{d}`.  Those four bags are connected and
   pairwise adjacent in `K_{2,2,2}`, so the seven displayed bags are a valid
   explicit `K_7`-minor model.
5. In the separator case every complementary component is full to the
   seven-set.  Contracting an opposite full component together with a
   nonempty independent boundary set is a proper minor; after a six-colouring
   is restricted to the desired shore, that independent set is exactly one
   boundary colour class.  The reverse-shore response is symmetric.

## Trust boundary

The theorem requires minimality for every proper edge subset of the entire
forest whose quotient is exactly `J`.  It does not cover a first bad partial
quotient larger than `J`, and its separator assignment does not by itself
preserve a named support spread across several fibres.  The main theorem is
uncoloured and does not prove the atomic collision theorem or `HC_7`.
