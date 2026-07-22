# Audit: fourfold-incidence shore-filling barrier

## Verdict

**GREEN** at the exact revisions

```text
0c4976fe7213f35e663e320ac7a49d4146f545c2a5d833ce30e115da2d278f6b  barriers/hc7_degree8_fourfold_incidence_bridge_interval_barrier.md
b16efd4e33a02fcf21432f23d05f2c68da49655d9452e37b2a176ce05fa719db  barriers/hc7_degree8_fourfold_incidence_bridge_interval_barrier_verify.py
```

This is a separate internal audit, not external peer review.  The example
refutes only the stated local bridge-interval inference; it is not a
counterexample to `HC_7` or to a theorem using the full seven-connected,
seven-chromatic contraction-critical setup.

## Mathematical check

The construction has exactly the asserted forty edges on twelve vertices.
Its boundary has independent triples `I,T`, nonadjacent roots, all four
root-to-block contacts, an `I`--`T` edge, and independence number three.
The displayed width-two boundary elimination order proves the required
`K_4`-minor exclusion after every two-vertex deletion.  The two components
of `G-N[u]` are precisely the full shores `E={e}` and `F={x,y}`.

Both fixed shore colourings are proper and realize the stated merged and
split boundary partitions.  Their full `gamma`--`delta` components are
exactly `p-e-q` and `p-x-y-q`; their union is the induced five-cycle
`p-e-q-y-x-p`.  Each path fills its open shore, so all four incidence
graphs consist of three isolated block vertices and there is no residual
component from which to choose a bridge interval.  The graph off the cycle
is connected and meets every cycle vertex, so its attachment hull is the
whole cycle.  The two additional colourings correctly show that both shores
also realize the opposite endpoint equality type.

The displayed host elimination order has width five.  Since treewidth is
minor-monotone and `tw(K_7)=6`, this proves `K_7`-minor exclusion and also
that every minor is six-colourable.  Exhaustive colouring and cut searches
verify `chi(G)=5` and `kappa(G)=5`; in particular the example explicitly
fails the two global hypotheses identified in the source.  The twelve-
vertex minimality count for two internally shore-disjoint paths of opposite
parity is correct.

## Verifier replay

All checks use the always-active `require` function.  The shore sets and
path interiors are explicit, and the ordinary and optimized runs produced
identical output:

```text
python3 barriers/hc7_degree8_fourfold_incidence_bridge_interval_barrier_verify.py
python3 -O barriers/hc7_degree8_fourfold_incidence_bridge_interval_barrier_verify.py

vertices 12
edges 40
boundary_alpha 3
boundary_fill_width 2
host_fill_width 5
chromatic_number 5
vertex_connectivity 5
minimum_cut i1 t1 u e x
aligned_paths p-e-q p-x-y-q
PASS degree8_fourfold_incidence_bridge_interval_barrier
```

No unresolved issue remains within the barrier's stated scope.
