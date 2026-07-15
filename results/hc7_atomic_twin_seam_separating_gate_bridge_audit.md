# Audit: atomic twin-seam separating gate bridge

**Verdict:** GREEN.

## Swap audit

Every alternate-colour component containing `z` also contains `u`, since a
swap separating them would extend across `e` to a six-colouring of `G`.

Removing the bridge `f` divides the `alpha-beta` lock into a `z`-side `X`
and a `u`-side.  Swapping on `X` repairs `e=zu` and makes the ends of `f`
equal.  No other edge becomes monochromatic.  Hence the swapped colouring
is valid on `G-f` and descends to `G/f` with the gate label `t` retained.

## Closed-side audit

At `Omega_D`, the valid comparison is `phi` on the `D`-closed side and the
swapped colouring on the opposite side.  At `Omega_E`, it is `phi` on the
`B_E`-closed side and the swapped colouring on the `E`-side.  Both chosen
`phi`-sides contain `f`.  Seeking the paths in the two opposite sides would
be wrong because those sides exclude `d`.

If no bichromatic component on a chosen `phi`-side has boundary trace on
both sides of `X intersect Omega`, componentwise Kempe swaps reproduce the
swapped colouring on that boundary and permit exact gluing.  Therefore a
survivor has a boundary-crossing component.  A shortest path inside it has
no internal boundary vertex.

The path lies in the original global lock, begins in `X` and ends outside
it, and so must contain the unique bridge `f`.  Since `t` is on the
boundary, it must be an endpoint.  This proves both literal paths with the
stated interiors.

## Scope

No disjointness between the two paths is proved.  Shortestness of an
excursion also does not force its first gate edge to be a bridge: a cycle or
theta supplies a bypass.  The theorem correctly stops at the
bridge-versus-bypass dichotomy.
