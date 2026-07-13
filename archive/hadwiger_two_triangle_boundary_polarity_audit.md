# Internal audit of the two-triangle boundary-polarity theorem

## Verdict

**GREEN within its explicit minimal-family hypothesis.**  The state-cover
classification and Kempe-switch conclusions are correct.  The hypothesis
that the actual extension families are inclusion-minimal is essential and
is not presently known for a hypothetical `HC_7` counterexample.

## Checks

1. In `K_1 vee K_{3,3}`, colour blocks cannot cross between the two
   independent triples and cannot contain the universal root.  The only
   seven-boundary partition exceeding six blocks is the pair of discrete
   triple partitions, giving exactly 24 states.
2. Whole-triple and pair private blocks force respectively the `O` and
   three `P` coordinate vertices.  Those three `P` coordinates also
   witness all singleton blocks, so covering the eight required vertices
   is exactly private completeness.  Covering `O_X` automatically gives
   a boundary state with at most five blocks.
3. Edge-minimality of a required-vertex cover is equivalent to every edge
   owning a degree-one required endpoint.  The injection from selected
   edges to such endpoints proves the eight-edge upper bound.  The
   common-leaf argument correctly handles the four-edge case separately,
   where all eight required vertices have degree one.
4. Every Kempe switch in Theorem 4.1 preserves the opposite boundary
   coordinate because colours used on one triple are absent from the
   other triple and from the universal root.  The three possible
   incidences of the singleton's bichromatic component in a pair state
   give exactly the claimed one-block, different-pair, or locked outcome.
5. A private contraction at a common required coordinate really selects
   the unique fibre state when the full extension family is minimal.
   Opposite-side carrier interiors are disjoint, but the carriers share
   their named boundary roots; the note does not misstate them as disjoint
   branch sets.

Selecting an inclusion-minimal subfamily of a larger extension family
does not satisfy the uniqueness hypothesis.  This is prominently recorded
as the audit boundary and prevents the result from being treated as a
closure of the general exact-cut cell.

