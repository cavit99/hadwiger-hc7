# Independent audit: compulsory-edge lock-state lift

**Verdict:** GREEN.

**Audited source:** `results/hc7_compulsory_edge_lock_state_lift.md`

**Source SHA-256:**
`0af1c99fcf17870b2368455f5fad7f8107a8e8186851328f5fe26a45b9d94372`

## 1. Kempe bridge swap

In the proper colouring of `G-e`, the locked `alpha-beta` component `K`
contains both `z` and `u`. If the edge `f` is a bridge of `K`, then deleting
it separates `K` into a `z`-side `X` and a `u`-side. No other
`alpha-beta` edge of `G-{e,f}` leaves `X`: such an edge would either remain
inside the component `K` and contradict the bridge separation, or put its
other endpoint in the same `alpha-beta` component of `G-e`.

Swapping `alpha,beta` on `X` is therefore an ordinary legal Kempe swap in
`G-{e,f}`. It changes `z` but not `u`, so the restored edge `e=zu` is
proper. The original edge `f` was bichromatic, and exactly one of its ends
is swapped, so those ends become equal. Thus the result colours `G-f` and
descends to `G/f` exactly as claimed.

This remains valid if the boundary end of a boundary--rich `f` is `u`:
the other endpoint is swapped, `zu` is restored with distinct endpoint
colours, and the contracted image of `u` retains its literal label.

## 2. Boundary state and contraction labels

A literal boundary vertex changes colour exactly when it belongs to
`X intersect S=T`. Every vertex outside `T` keeps its literal colour.
When `f` is boundary--rich, contracting it identifies one boundary literal
with one rich vertex and identifies no two boundary literals. The
contracted image can therefore carry that boundary label, and lifting its
colour reproduces the asserted boundary colouring.

No equality-block identity beyond this explicit toggle is assumed.

## 3. Component-trace reproduction and gluing

The restriction of the original `G-e` colouring to `H_R=G[R union S]` is
an intact closed-shore colouring because the missing edge has its other
endpoint in `A`.

If no `alpha-beta` component of `H_R` meets both `T` and `S-T`, every
component meeting `T` has boundary trace contained in `T`. Swapping all
such components toggles exactly `T` and hence agrees literally on `S` with
the thin-shore restriction of the new `G-f` colouring. The edge `f` lies
outside `G[A union S]` in both allowed cases, while `e` has been restored
properly. The two intact closed-shore colourings therefore cover every
edge of `G`, agree on `S`, and glue because there is no `A-R` edge.

The argument also covers `T=emptyset` and `T=S`; either case falls into
this gluing outcome and hence cannot survive in a counterexample.

## 4. Literal rich path through `f`

Otherwise one `alpha-beta` component of `H_R` meets both `T` and `S-T`.
A shortest path between the two boundary sets has no internal boundary
vertex, since every boundary vertex lies in one of those sets and would
shorten the path. Its internal vertices therefore lie in `R`.

Starting at a vertex of `T subseteq X`, this path remains in the original
component `K`. Its other boundary endpoint lies outside `X` because it is
in `S-T`. Every path in `K` between the two components of `K-f` uses the
bridge `f`, so the chosen path contains `f`.

For a boundary--rich `f`, this additionally forces its boundary endpoint
to be an endpoint of the shortest path rather than an internal boundary
vertex, so the rich-interior statement remains exact.

## 5. Demand-one reflection

The source now states explicitly the part of the frozen atomic setup needed
here: the thin shore `A` is connected and `S`-full. Thus it supplies one
literal `S`-full packet for the exact packet-reflection lemma.

Let `Pi'` be the exact partition produced by the lock-bridge swap. If
`d_{G[S]}(Pi')=0`, the proof of exact packet reflection shows that all seven
blocks are singleton blocks inducing `K_7` on `S`; this is already the
literal-minor outcome. If `d_{G[S]}(Pi')=1`, exact packet reflection with
`q=1`, applied from the thin shore toward the rich shore, either displays
seven literal branch sets or contracts `A` together with the unique
nonretained boundary block in a proper minor and returns an intact colouring
of `G[R\cup S]` with exact partition `Pi'`.

In the colouring branch, Lemma 2.1 already gives an intact colouring of
`G[A\cup S]`: the edge `e` has been repaired and either allowed type of `f`
puts `f` outside that induced closed shore. Two colourings inducing the
same exact equality partition on `S` differ there only by a permutation of
their used colours; extend that permutation to the six-colour palette and
glue. Therefore a non-six-colourable, `K_7`-minor-free survivor must have
`d_{G[S]}(Pi')\ge2`, exactly as Corollary 3.2 claims.

## 6. Scope

The theorem legally couples one `G-zu` state to a specifically related
`G-f`/`G/f` state and, in the nongluing branch, to a literal two-colour
rich-interior path containing that same edge `f`. It does not prove that
such a bridge exists for a chosen lock, identify `f` with the independently
localized final-duty edge, or decode the edge-nonseparable two-route
residue. Those limitations are stated correctly.
