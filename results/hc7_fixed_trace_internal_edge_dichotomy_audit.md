# Audit of the fixed-trace internal-edge dichotomy

**Verdict:** GREEN for Theorem 2.1, Proposition 2.2, and Corollary 3.1 in
[`hc7_fixed_trace_internal_edge_dichotomy.md`](hc7_fixed_trace_internal_edge_dichotomy.md)
at source SHA-256

```text
4ee98b67df343cc5023822b43a5291ead6929067c6bb39242447b2cd1e717f84
```

This is a separate internal mathematical audit, not external peer review.

## Checks

1. **Imported setting.**  The theorem explicitly retains the exact-seven
   separation, the special five-plus-two interface, the fixed
   double-contraction boundary colouring, minor-critical six-colourability,
   seven-connectivity, and `K_7`-minor exclusion required by its cited
   reflection results.
2. **Surviving obstruction.**  If `G[A]-f` is not list-colourable, every
   proper induced subgraph is list-colourable by the vertex-minimality of
   `G[A]`.  Disconnected components could be coloured independently, so
   `G[A]-f` is connected and vertex-minimal.  Deleting one edge lowers the
   total list-degree excess by exactly two.
3. **Boundary rejection and demand.**  A six-colouring of `G-f` is legal
   on the untouched closed `B`-shore.  Extension of its exact boundary
   partition through the intact `A`-shore would six-colour `G`.  Equality
   with the fixed partition `Pi` would directly give a list-colouring of
   `G[A]-f`.  Orienting full-subgraph and transported Hall reflection from
   `B` toward `A` therefore proves demand greater than `nu_B` and, for each
   eligible displayed auxiliary support family, the asserted Hall-deficient
   block family.
4. **Locked edge.**  A list-colouring of `G[A]-f` glues to the fixed
   opposite-shore colouring.  Its endpoints must have one common colour.
   For any other colour, if an endpoint's bichromatic component avoided
   `Y`, switching that component would separate the endpoint colours and
   permit `f` to be restored.  Distinct endpoint components consequently
   give disjoint first-hit paths to distinct literal boundary vertices.
5. **Deletion/contraction equivalence.**  Every six-colouring of `G-f`
   has equal endpoint colours.  Identifying or expanding the endpoints are
   inverse operations, so deletion and contraction of this same edge
   induce the same trace family on disjoint boundaries.
6. **All-locked normal form.**  A proper subgraph either lies in a
   colourable proper induced subgraph or, when spanning, in `G[A]-f` for
   an omitted edge.  The graph is therefore subgraph-minimal
   non-list-colourable.  The standard degree-choosability characterization
   then makes the tight-vertex subgraph a Gallai forest.

## Trust boundary

The `E-2` alternative is an edge-deleted fixed-list obstruction, not a
smaller seven-chromatic counterexample, and no recursion in hypothetical
counterexamples follows.  Deletion and contraction of the same edge do
not provide independent responses.  The theorem does not close the
positive-excess branch or prove `HC_7`.
