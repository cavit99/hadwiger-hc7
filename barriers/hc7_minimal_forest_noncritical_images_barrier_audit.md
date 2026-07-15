# Independent audit: minimal-forest noncritical-image barrier

**Verdict:** GREEN.

The construction and verifier were checked independently against the claimed
local hypotheses and conclusions.

## Structural checks

* The boundary is `K_4 dotcup 4K_1`, hence has chromatic number four.
* `A={a,x,y,z}` and `B={b}` are connected and anticomplete.
* Every boundary vertex has the literal neighbours `a` and `b`, one in each
  shore.
* `F_0={xy,yz}` is contained in the displayed spanning tree
  `{xy,yz,ax}` of `G[A]`.

## Chromatic checks

* `P union {a,s_2,s_3,s_4}` is a literal `K_7`, and the displayed
  seven-colouring is proper.  Thus `chi(G)=7`.
* Contracting both forest edges gives a quotient `K` with the persistent
  literal clique `Q=K_5`; the displayed five-colouring is proper.  Thus
  `chi(K)=5`.
* Contracting either one edge of `F_0` turns the triangle `P` into an edge
  whose two ends are complete to `Q-{s_1}`.  A five-colouring would force
  both ends to use the colour of `s_1`, contrary to their adjacency.  A
  fresh sixth colour supplies the matching upper bound.  Both predecessors
  therefore have chromatic number six.
* The empty, singleton, and full subsets of `F_0` consequently give
  chromatic numbers seven, six, and five.  This verifies the required
  inclusion-minimality.
* Deleting the unique nontrivial component image `w` leaves `Q`, while the
  quotient five-colouring restricts.  Hence `chi(K-w)=5`.

The verifier's quotient construction and exact DSATUR routine were also
rerun successfully.

## Scope check

The note correctly does not claim a counterexample under the full
hypothetical-`HC_7` assumptions.  The graph contains a literal `K_7`, has
minimum degree two, and is not minor-critical.  Its conclusion is exactly
that local two-shore geometry plus minimal-forest saturation cannot by
itself force a critical terminal image.
