# Independent audit of the critical-triangle Kempe-separated component

**Verdict:** GREEN for Theorem 2.1, Corollary 3.1, and the stated trust
boundary at the exact source revision below.  The adjacent finite barrier
and its deterministic verifier are also GREEN at their pinned revisions.

This is a separate internal mathematical audit, not external peer review.

## 1. Exact revisions audited

The theorem source `hc7_critical_triangle_kempe_separation.md` has SHA-256

```text
f036d79fb94b67859bdea86e54a1c2d08b85ba66f1171cbe3e21253b47358dc3
```

The original GREEN audit was performed on source revision
`14de28409dd0cc9d1a3bf5ac5ad80d4cf93ad471b49724a7e604572a94fae371`,
after which the promoted source had revision
`499cd3ea45703e81069b6b7193988778b40292aa11b3d4624ebb639e3a192a65`.
The present revision renames the theorem and its adjacent package from the
project shorthand “Kempe lock” to the standard description
“Kempe-separated responses,” and updates the corresponding repository
paths.  It changes no graph, hypothesis, displayed formula, proof step, or
trust-boundary conclusion.  Sections 2--5 below were replayed against the
current source, and the displayed current hash is the governing audit pin.

The barrier source
`../barriers/hc7_critical_triangle_kempe_separation_barrier.md` has SHA-256

```text
4250568504bcfbaf1d3dae76efa09c526099179ee40a9f7426a8384e9f845526
```

Its verifier
`../barriers/hc7_critical_triangle_kempe_separation_barrier_verify.py` has
SHA-256

```text
77b61c20a1bb7881ff351b55d64234b5b111383a87368dd50dcdbdf616034dc8
```

The barrier and verifier changes are likewise confined to terminology,
filenames, and path references.  The finite graph, asserted properties,
and deterministic checks are unchanged.

## 2. The forced bichromatic component

Take a colouring in `X`, with `v,a` coloured `alpha` and `b` coloured
`beta`.  Since `ab` remains in `H`, its ends lie in one
`alpha`--`beta` component.  If that component did not contain `v`, a
Kempe interchange on the component containing `v` would change `v` to
`beta` while leaving `a` coloured `alpha` and `b` coloured `beta`.
The resulting colouring would lie in `Y`, contradicting Kempe separation.
Thus the component containing `v` contains both `a` and `b`.  The argument
is symmetric for a colouring in `Y`.

The chromatic conclusion is exact.  In `H[D]`, the two colour classes
`P,Q` form a connected bipartite graph, with `v,a in P` and `b in Q`.
Restoring `va` and `vb` adds only `va` within one of these classes.
Consequently

```text
{v},  P-{v},  Q
```

are independent sets in `G[D]`.  They give a proper three-colouring,
while the triangle `vab` gives the matching lower bound.  Hence
`chi(G[D])=3`; no additional criticality or connectivity assumption is
being used in Theorem 2.1.

## 3. Separator and dominating alternatives

If `D` is not dominating, a vertex outside `N_G[D]` and the connected
nonempty set `D` lie on opposite sides of the deletion of `N_G(D)`.
Thus the displayed boundary is an actual separator, and
seven-connectivity gives its lower bound of seven.

If `D` dominates, a three-colouring of `G-D` could be combined with the
three-colouring of `G[D]` on a disjoint palette, contrary to
`chi(G)=7`.  This proves `chi(G-D)>=4`.  A `K_6`-minor model in `G-D`,
together with the connected dominating branch set `D`, would be a
`K_7`-minor model in `G`.  Hence `G-D` is `K_6`-minor-free, and the known
case `HC_6` gives `chi(G-D)<=5`.  The dominating and nondominating cases
are exhaustive and mutually exclusive.

The source correctly does not infer an upper bound on the separator,
colour compatibility across its shores, or any alignment between palette
classes and a pre-existing labelled minor model.

## 4. Independent check of the finite barrier

The verifier's graph6 decoder reproduces the eighteen displayed edges of
the nine-vertex core.  Its exhaustive vertex-deletion and colouring
searches establish that the core is four-connected and
four-vertex-critical.  After deleting `03` and `06`, exhaustive
enumeration gives 24 labelled three-colourings and exactly the four
unlabelled equality partitions displayed in the barrier.  Independent
inspection of those colourings confirms that the twelve witnesses of
each response orientation have the claimed exact trace at its contracted
edge.  The Kempe graph has two components of order twelve, one for each
orientation.

For the join with `K_3`, the exhaustive cut search gives connectivity
exactly seven and the colouring search gives seven-vertex-criticality.
A Kempe interchange involving a join colour exchanges its singleton join
vertex with an entire core colour class, so it preserves all equalities
among `0,3,6`; interchanges using two core colours are precisely the core
interchanges.  The two response families therefore remain separated.

The verifier checks that the seven displayed branch sets are disjoint,
connected, spanning, and have every required adjacency except
`{6}`--`{7}` after both incident edges are deleted.  It also independently
checks the displayed order-seven separator and all adjacencies of the
explicit `K_7`-minor model.  Thus the example has the advertised strong
local hypotheses but exits through both outcomes that its trust boundary
explicitly excludes.

The verifier was rerun at the pinned revision and produced exactly:

```text
core graph6 HCpvbqk: 4-connected and 4-vertex-critical
common deletion: 24 three-colourings in two pure Kempe components of order 12
joined host: 7-connected and 7-vertex-critical
spanning labelled K7-minus-edge model: verified
actual order-seven separator and explicit K7 model: verified
ALL CHECKS PASSED
```

## 5. Trust boundary

The barrier is not an `HC_7` counterexample: it contains a `K_7` minor,
has an actual order-seven separator, and has a proper seven-chromatic
minor.  It therefore refutes only the connectivity-and-local-data version
of an orientation-changing Kempe claim.  The theorem's only external
mathematical dependency is the established `HC_6` case, used solely for
the upper bound `chi(G-D)<=5` in Corollary 3.1.
