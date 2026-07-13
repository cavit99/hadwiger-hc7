# Audit: singleton-hub promotion and degree-eight transport

## Verdict

**GREEN for the stated conditional results.**  The promotion, joint-edge
rooted `K_4`, hub-graph dichotomy, palette warehouse, and transport to a
defect-one degree-eight cell follow from the minimum-fragment hypotheses
and the audited two-piece atlas.  They do not prove the final joint-edge
rooted exchange or the two-exterior degree-eight cell.

## Checks

1. A bad neighbour `w` of a hub `h` has a witness
   `s_w in S-N_S(h)` for which `w` is the unique portal in `D-h`.
   Different bad neighbours have different witnesses.  Strict atomic
   surplus gives one more internal neighbour than available witnesses,
   so a full-deletion neighbour exists.
2. Three-connectivity of the minimum shore implies that
   `B=D-{h,w}` is nonempty and connected.  Strict surplus on `B`, whose
   only possible internal boundary vertices are `h,w`, gives
   `|S-N_S(B)|<=1`.  Fullness after deleting either endpoint puts the
   possible missed label at both `h` and `w`.
3. Deleting `h` leaves a two-connected graph.  The two-fan from `w` to
   two distinct neighbours of `h` yields two internally disjoint
   `h-w` paths.  Their interiors lie in `B`; connecting and extending
   those interiors gives the claimed bipartition `B_1|B_2`.  Hence
   `{h},{w},B_1,B_2` is a literal rooted `K_4` model.
4. For every full-deletion vertex `u`, nonhub neighbours inject into the
   `7-|N_S(u)|` missing boundary labels.  Atomic surplus leaves a hub
   neighbour.  At a hub-graph leaf both counts are equal, so the
   injection is a bijection and `d_G(u)=8`.  No equality is inferred at
   a nonleaf.
5. In a colouring of `G-hw`, criticality forces `h,w` to have one
   colour.  If an `alpha/beta` component separated them, switching the
   component of one endpoint would restore the edge.  Thus both endpoints
   lie in one component and each has a neighbour of every other colour.
   Since the old shores are anticomplete, all ten labelled incidences lie
   in the named closed shore `D union S`.  Equality of boundary
   partitions is sufficient for colour alignment because different
   blocks use different colours.
6. At a tight leaf, `G-N[u]` consists of the canonical component
   containing `H union(S-P)` and the residual old-shore set `R`.  The
   first component sees every member of `N(u)` except `w`: the old
   full shore sees `P`, and each old missing label sees its private
   `y_s`.  It cannot see `w` because old shores are anticomplete and
   every `s in S-P` has unique old-shore portal `y_s`.  The degree-eight
   exterior-component theorem then makes `R` empty or connected; in the
   latter case seven-connectivity gives defect at most one.

## Exact audit boundary

The operation colouring supplies **palette** labels, not identities of
rooted-model bags.  The rooted `K_4` does not align those coordinate
systems.  In the square branch, three-connectivity also guarantees extra
interface edges, so the exact-two-edge XOR theorem is inapplicable.  The
remaining valid targets are the joint-edge rooted exchange, hub-cycle
state holonomy, and the transported degree-eight two-exterior cell.
