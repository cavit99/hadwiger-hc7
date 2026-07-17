# Audit of the colour-matched path exchange-or-separator theorem

**Verdict:** GREEN (separate internal audit)

**Audited theorem revision:** SHA-256
`9f22f7f8828ed5d64b269c18e31aae82deb10fc5c57c6d1b89cdccf47af5cc6b`
of `hc7_colour_matched_path_exchange_or_separator.md`.

## Checks performed

The residual-component alternatives are exhaustive.  If no residual
component of one protected branch set meets both anchors, a missed anchor
is outside the component and its full neighbourhood.  If anchor-complete
components exist but two selected components are nonadjacent, either
component supplies a nonempty far side for the other's full-neighbourhood
separation.  If all four are pairwise adjacent, the cited component
exchange theorem supplies the explicit `K_7` model.

When a protected branch set is wholly consumed, independence of its path
intersection and connectedness force it to be a singleton.  The bipartite
set `X` cannot be consumed because its other colour class is nonempty.
The singleton is nonuniversal: otherwise its deletion is exactly
six-chromatic, `HC_6` supplies a `K_6` minor, and universality lifts that
model to `K_7`.  A non-neighbour then gives the opposite open side of the
singleton-neighbourhood separation.

Every displayed boundary is therefore an actual separator, and the stated
lower bounds follow exactly from seven-connectivity.

## Scope

The theorem proves `K_7` or an actual separation for each fixed repair
path.  It gives no upper bound on that separator and no compatible pair of
boundary colourings.  It does not prove `HC_7`.  No unresolved gap remains
within this stated scope.
