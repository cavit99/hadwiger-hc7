# Audit of the singleton-shore nonbipartiteness theorem

**Verdict:** GREEN for Theorem 1.1 and Corollary 1.2 in
[`hc7_singleton_shore_nonbipartite.md`](hc7_singleton_shore_nonbipartite.md)
at source SHA-256

```text
dbdae8295af908bce6101bd4d28d48a8f7e1de442f3749c9a7163d1d023ced4d
```

This is a separate internal mathematical audit, not external peer review.

## Checks

1. Independence number at most two makes every boundary colour class have
   order at most two.  Seven boundary vertices therefore require at least
   four colours, and the assumed upper bound gives equality.
2. If the opposite shore were bipartite, use four colours on the boundary
   and two disjoint new colours on that shore.  The singleton vertex can
   use one of the latter colours because it is anticomplete to the opposite
   shore.  All boundary--shore edges are proper because the palettes are
   disjoint.  This is a forbidden six-colouring of `G`.
3. In the active singleton branch, the cited two-root reduction gives
   `N(a)=Y` and the connected opposite shore.  Dirac's inequality gives
   `alpha(G[Y])<=2`, and the special exact-seven response theorem gives
   `chi(G[Y])<=4`.  The corollary therefore invokes Theorem 1.1 with no
   hidden assumption.

## Trust boundary

The theorem proves only that the exterior contains an odd cycle.  It does
not close binary cutvertices, nonbipartite two-connected exteriors, the
whole singleton branch, or `HC_7`.
