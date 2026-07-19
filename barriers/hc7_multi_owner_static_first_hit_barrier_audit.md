# Independent audit of the static two-owner first-hit barrier

**Verdict:** **GREEN** for the exact source revision identified below.

This is a separate internal mathematical audit, not external peer review.
It checks the finite construction, connectivity and minor exclusion, all
labelled branch-set adjacencies, the relaxed first-hit witness, the
root-preserving minimality calculation and the local neighbourhood orders.

## Audited revision

The audited source is
`barriers/hc7_multi_owner_static_first_hit_barrier.md`.

**Source SHA-256:**

```text
2bccdecb65ce1a5ca0df2122584cfab3019c4ea79bbd4f4f3f14697b100fed08
```

The deterministic verifier is
`barriers/hc7_multi_owner_static_first_hit_barrier_verify.py`.

## 1. Host construction

The twenty triangles of the deterministically labelled icosahedron produce
twenty face vertices.  The displayed incidence and face-adjacency rules
give a 32-vertex, 90-edge graph.  The verifier checks planarity and exact
vertex-connectivity five.

Joining an edge to this graph produces a 34-vertex graph of connectivity
seven.  The mathematical minor-exclusion argument is valid: at most two
branch sets of a `K_7` model can contain the two universal vertices, so the
other five would form a `K_5` model in the planar factor.

## 2. Labelled model

The seven displayed sets are nonempty, pairwise disjoint and spanning.  The
listed tree certifies connectedness of `D`, and the other six sets are
singletons or the path `13-12-14`.  The verifier checks every required
pair.  Exactly `X={11}` and `Y={0}` are nonadjacent; every other pair is
adjacent.

The fixed response subgraph is all of `D`, so it is connected and remains
inside the branch set labelled `D` in every compatible model considered.
The two edges `8-13` and `19-12` have distinct ends in `U` and place one
end on each side of the split

```text
W = {12,14},   U-W = {13}.
```

The owner calculation is exact.  The residual vertex `13` meets `Y,p,q`
and misses `X,F`; the vertex `14` supplies both old `U-X` and `U-F`
adjacencies.  Thus the owner set is precisely `{X,F}`.

## 3. Relaxed first-hit rank

The six displayed paths are actual one-edge paths.  Their six starts are
different vertices of `D`, and their six ends lie in different ranked
branch sets.  Since the paths leave `D` only at their terminal vertices,
they satisfy the relaxed first-hit definition and are pairwise disjoint
outside `D`.  They prove rank at least six.  There are only six ranked
labels, so the rank is exactly six and is globally maximum.

## 4. Minimum branch set

Fixing `Z=D` fixes all twenty-six vertices of `D`.  The six prescribed
roots outside `D` fix `11,0,13,16,p,q`.  Therefore `12,14` are the only
vertices whose labels can change.

The source's three-case proof for a smaller connected branch set containing
`13` is correct.  The verifier additionally checks all forty-nine label
assignments for `12,14`; the unique compatible assignment leaves both in
`U`.  This enumeration permits `X,Y` to become adjacent, so it does not
silently exclude a completed `K_7` model.

## 5. Full neighbourhoods

The connected nonempty subsets of `U` are exactly the six sets listed in
the source.  Their computed full-neighbourhood orders are respectively

```text
8, 8, 8, 10, 10, 12.
```

Thus no connected subset of `U`, including the two-owner side itself,
returns an order-seven full-neighbourhood separation.  Together with
`K_7`-minor exclusion and minimum `U`, this verifies all three failed
alternatives in the exact static assertion.

## 6. Trust boundary

The source does not overstate the example.  A deterministic four-colouring
of the planar factor extends to a six-colouring of the host by giving the
two universal adjacent vertices new colours.  Hence the graph is not
seven-chromatic or contraction-critical.

The graph also has unrelated order-seven separators: an old degree-five
vertex of the planar factor has degree seven after the join.  Therefore the
example does not refute a statement which uses a selected proper-minor
colouring response to return any compatible order-seven separation, or
which accepts the coherent planarizing pair formed by the two universal
vertices.

The exact audited conclusion is only that maximum relaxed first-hit rank,
minimum branch-set order, seven-connectivity and `K_7`-minor exclusion do
not resolve the two-owner split by a local branch-set exchange.
