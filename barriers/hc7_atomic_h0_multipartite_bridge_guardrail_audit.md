# Independent audit of the atomic `H_0` multipartite guardrail

**Status:** separate internal audit GREEN, 21 July 2026.

This is an internal mathematical audit, not external peer review.

## Revision audited

- barrier:
  [`hc7_atomic_h0_multipartite_bridge_guardrail.md`](hc7_atomic_h0_multipartite_bridge_guardrail.md)
- exact SHA-256:
  `ed78d9076f114a58504b3d3e192312dc6ce778626dc24d538dae5410b8a3cccb`

The hash was computed with `shasum -a 256` after the barrier status was
changed to GREEN.  The adjacent one-bridge checker was rerun at SHA-256
`ba78a7f17e3685aeca3a4a4fd014f5cf8a69007d080e170ad2bd7158e09511a3`.

## Verdict

GREEN.  Both obstruction graphs have exactly the claimed properties.  The
barrier correctly refutes common clean-apex compatibility and regeneration
of an unlabelled normalized dominating `K_5` model as stand-alone proof
mechanisms, without claiming a counterexample to `HC_7`.

## Checks performed

1. In `R`, each added bridge path separately has the stated planarizing pair.
   For their union, deletion of `e,f` leaves the displayed literal `K_{3,3}`;
   after either of the other two deletions, the five displayed connected sets
   are pairwise adjacent.  Thus none of the three one-bridge clean-apex
   certificates planarizes the union.
2. The exact eight-set common-frame partition of `R` has precisely the
   nonadjacencies `xe,ab,cd`.  The graph `R-p` is complete multipartite with
   parts of orders three, two, two, and one, while `N_R(p)={e,f,x}` is
   independent.  Hence `omega(R)=4`.  A spanning seven-bag model on nine
   vertices would force six or five singleton bags forming a clique, so `R`
   has no `K_7` minor.  Its displayed three-cut is real, and deleting at most
   two vertices leaves the remainder connected, proving `kappa(R)=3`.
3. One bridge path always has a planarizing pair by the exact classifier.  On
   eight vertices, two bridge paths can only be two missing branch-to-branch
   edges of the literal frame; the safe possibilities are among `xe,xf,xg`,
   and the corresponding two clean labels give a common planarizing pair.
   This verifies the stated minimum number of paths and minimum order.
4. Adding `pa,pb,pc,pd` produces exactly `M=K_{3,2,2,2}` with the four
   displayed parts.  The stated atomic immersion is edge-disjoint, has only
   the binary collision at `x`, and retains the exact common-frame partition
   and the two required contacts.
5. The standard complete-multipartite connectivity calculation gives
   `kappa(M)=9-3=6`.  Its clique number is four, so the same spanning
   partition argument excludes a `K_7` minor.  Every missing edge is internal
   to one part.  The models (2.4) and (2.5) are connected and pairwise
   adjacent, covering respectively the part of order three and every part of
   order two; hence `M` is edge-maximal `K_7`-minor-free.
6. The four deleted-pair orbits are exhaustive: two vertices of the
   three-part, one from that part and one from a two-part, a whole two-part,
   and vertices from two distinct two-parts.  In each of (2.6)--(2.9), every
   vertex of every later branch set has a neighbour in each earlier branch
   set.  The last three sets are singleton vertices in distinct parts and
   induce a triangle.  Thus every two-set is avoided by a normalized
   dominating `K_5` model, proving the no-transversal claim.
7. If two vertices of the three-part lie in one component of `G-S`, a path
   between consecutive visits to that part has all internal vertices outside
   `M` and contracts to a missing edge of `M`.  Edge maximality then lifts a
   `K_7` model.  Therefore in a `K_7`-minor-free supergraph the six-set `S`
   remains an actual separator, so seven-connectivity excludes the
   configuration.

## Trust boundary

The saturation `M` is four-colourable and only six-connected.  It is not a
counterexample to `HC_7`, strong seven-contraction-criticality, or an exchange
using actual proper-minor colour responses.  The note does not derive the
multipartite saturation from an arbitrary family of quadrant-confined
bridges; that label-sensitive interaction theorem remains unresolved.
