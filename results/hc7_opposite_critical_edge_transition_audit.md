# Internal audit of the opposite critical-edge transition

**Verdict:** GREEN.

**Promoted source:**
[`hc7_opposite_critical_edge_transition.md`](hc7_opposite_critical_edge_transition.md)

**Promoted source SHA-256:**
`fcf8e0cec7cfa77984e34272f1408e74ffe23df187796ab0c8826e62cd10f808`

**Original audited revision SHA-256:**
`ce0c793315bae913930497474269d73c9bd3c1d3ce9b1d91265cbef09e0dc622`

The promoted source differs from the independently audited revision only
in its status paragraph and three editorial clarifications requested by
the audit: the endpoint pairing is no longer called label-preserving, the
cycle notation names the deleted edges as edges rather than vertices, and
the cited icosahedron guardrail explains how its common host obtains a
spanning `K_6` model.  No hypothesis, mathematical conclusion, proof step,
or scope boundary changed.  The GREEN verdict therefore rebinds to the
promoted hash above.

This is a separate internal mathematical audit, not external peer review.

## Direct transition

Let the initial colouring make the ends `a,b` of `e` equal to `alpha`.
A Kempe interchange which makes `e` proper uses colours `alpha,beta` and
contains exactly one of `a,b`.  If the same interchange makes `f` change
from proper to equal, its component also contains exactly one endpoint of
`f`, and the two endpoints of `f` have colours `alpha,beta` beforehand.

The initial colouring extends to `G-e`.  Since `G` is not `q`-colourable,
the standard critical-edge argument puts `a,b` in one
`alpha`--`beta` component of `G-e`.  They lie in distinct such components
of `H`; the only edge in `(G-e)-H` is `f`.  Hence `f` joins the component
containing one end of `e` to the component containing the other, and each
of those two components contains exactly one end of each deleted edge.
Paths inside the two disjoint components, together with `e` and `f`, form
the asserted cycle through all four endpoints.  The proof is symmetric
under the other endpoint pairing.

## Three response chambers

The sets `X,Y` are nonempty by restricting colourings of `G-e` and `G-f`
to the common deletion.  The set `Z` is nonempty by expanding a colouring
of the proper double contraction `G/e/f`.  A colouring with both deleted
edges proper would colour `G`, so the fourth chamber is empty.

For any Kempe path from `X` to `Y`, either two consecutive colourings lie
in those two sets or, because the fourth chamber is forbidden, the path
visits `Z`.  The quantifiers in Corollary 2.1 are therefore correct.
Opposite-shore boundary incompatibility applies because an `X` colouring
extends to one internal edge deletion and a `Y` colouring extends to the
opposite one.

## Scope

At the balanced order-eight boundary the two chosen clique edges are
disjoint and lie in opposite open components, so the application is valid.
The result does not prove that the two response types share a Kempe class,
prescribe which endpoint pairing occurs, keep the path interiors away from
the two five-cliques, or turn the paths into a `K_7` model.  The cited
icosahedron construction has an ambient `K_7` model and an actual
order-seven cut, so it is only a guardrail against inferring colouring-space
connectivity from a spanning clique model.
