# Internal audit: critical boundary-edge fan descent

**Verdict:** GREEN.

**Audited source:** `results/hc7_exact7_critical_edge_fan_descent.md`

**SHA-256:**

```text
d359b4a14520fc4d558ebc600c4e64b7f6bf65ef9fa425b107effa498afc3bfa
```

This is a separate internal mathematical audit, not external peer review.

## 1. Critical-edge colours

All five alternate colours must occur.  If one were absent, recolouring
the internal end of the deleted boundary edge with it would restore a
proper six-colouring of the host.  The usual two-colour interchange then
correctly forces an endpoint path for every alternate colour.

## 2. Prescribed-first-edge fan

The direct prescribed boundary edges are separated first.  After removing
their `r` distinct ends, there are `5-r` internal sources and `6-r`
available targets.  Failure of the set linkage gives a separator of order
at most `4-r`.  The component containing a surviving source has
neighbourhood contained in that separator, the two distinguished vertices,
and the `r` removed ends, hence of order at most six.  This contradicts
seven-connectivity.  The repaired linkage therefore has six distinct
boundary ends and preserves all five first edges.

## 3. Reusable-target Menger calculation

For the target-retaining packing, the `r` direct paths use no vertex
outside the permitted common set.  A failed routing of the other `5-r`
sources gives `Z subseteq C-{v}` with `|Z|<=4-r`.  The selected source
component has no target neighbour, so its neighbourhood has order at most
`7-r`.  Seven-connectivity forces `r=0`, `|Z|=4`, and equality in the
displayed full neighbourhood.  Thus all five original colour-indexed tails
meet the same four-set `Z`.

## 4. Colour and exact-block conclusions

Five chosen tail intersections in four vertices give one vertex on two
paths with different alternate colours.  Their palette intersection is
only the common endpoint colour, so that vertex has colour `alpha`.  The
deleted boundary endpoint is outside the returned closed shore, making the
restricted colouring proper there.  Its exact `alpha` boundary class
contains two distinct vertices.

The union of the returned component and that class is connected and can be
contracted in a proper minor.  The class is independent, and fullness of
the component makes the contraction image adjacent to every other boundary
vertex.  Pullback therefore gives an opposite-shore colouring in which the
same class is exact.

## 5. Component-order rank

The returned connected set is a component behind an actual order-seven
boundary, is full to that boundary, and is strictly smaller than the old
component.  Any new boundary-to-component edge is again critical because
its deletion is a proper minor and the host is not six-colourable.  Hence
component order is a valid well-founded rank over unstructured
critical-edge instances.

This re-entry may use a different edge-deletion colouring.  It does not
preserve the former full equality partition or the inherited minor-model
labels.  At minimum component order, the theorem forces six distinct
first-hit support or, when the original support has order at most five,
the clean target-retaining packing.

No hidden use of `K_7`-minor-freeness or identification of palette colours
with branch-set labels was found.
