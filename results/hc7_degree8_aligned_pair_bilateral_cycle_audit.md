# Audit: aligned degree-eight bilateral response cycle

**Audit type:** separate internal cold audit

**Verdict:** **GREEN**

Audited theorem:
[`hc7_degree8_aligned_pair_bilateral_cycle.md`](hc7_degree8_aligned_pair_bilateral_cycle.md)

Audited source SHA-256:

```text
2ea4832a0c56c588511e5c944907d77fcef7e299c85bf352a51f5ace879ce2e9
```

The status-only promotion after this audit has source SHA-256

```text
cdb813d84a9eb980f1310f0d941c8c349e79988f965ea9a81b45d85d8ca4c8d9
```

and changes no mathematical statement or proof.

This is an internal mathematical audit, not external peer review.  The
result does not prove `HC_7`.

## Response sets and colour normalization

Lemma 1.1 of the audited concentrated-reserve theorem applies exactly to
the displayed degree-eight setup.  For each shore its response set is
nonempty, and the two sets are opposite singletons in the equality type of
`p,q`.  Because `I,T,{p,q}` exhaust the boundary, these types are exactly
the merged and split complete partitions in (2.1); no stronger simultaneous
response quantifier is assumed.

The colour names of the two independently chosen shore colourings may be
permuted independently.  They can therefore be normalized so that `I,T,p`
have the common names `a,b,gamma`.  On the merged shore `q` also has colour
`gamma`; on the split shore its fourth boundary colour can be named
`delta`, with `delta` chosen among the three colours absent from the merged
boundary.  Thus in both boundary colourings `{q}` is a component of the
`gamma`--`delta` boundary graph, and the two operations are the same
singleton interchange read in opposite directions.

## Failed lifts and odd cycle

If the singleton interchange lifted through the merged shore, it would
produce the forbidden split response while preserving the exact `I,T`
blocks.  Hence the full two-colour component through `q` also contains
`p`.  The reverse argument on the split shore similarly forces its full
component through `q` to contain `p`; otherwise that shore would realize
the forbidden merged response.

Only `p,q` use either selected colour on the boundary.  A shortest joining
path in each full component therefore meets `S` only at its ends, and its
open interior lies in its named component `E` or `F`.  The two interiors
are disjoint and the paths share only `p,q`, so their union is a simple
cycle.  Proper two-colour alternation makes the merged-shore path even,
because its endpoint colours agree, and the split-shore path odd, because
they differ.  Their union is consequently a literal odd cycle.  This
checks both operation provenance and parity without identifying the two
interior colourings.

## Bridge recolouring and gluing

For a bridge `e` separating `p,q` in one fixed full two-colour component,
deleting `e` and swapping the two colours on the `q`-side is proper.  Any
other two-colour edge between the sides would belong to the same full
component and contradict that `e` is a bridge; edges to other colours stay
proper.  Since the component meets `S` exactly in `{p,q}`, precisely `q`
changes on the boundary.  The resulting complete boundary partition is
the fixed opposite-shore partition.

The two shore colourings therefore align and glue on `G-u-e`.  Their
boundary uses at most four colours, so an absent colour may be assigned to
`u`, yielding the asserted colouring of `G-e`.  The source's phrase
“four-colour boundary” includes the merged direction, where only three
colours occur; this harmless wording does not affect the absent-colour
argument.

Before the swap the ends of `e` have opposite selected colours and lie on
opposite sides; afterwards they are monochromatic.  Conversely,
minor-criticality implies that every six-colouring of `G-e` makes them
monochromatic, since otherwise restoring `e` would six-colour `G`.
Identifying equal-coloured ends therefore gives the equivalent colouring
response on `G/e`.  The opposite shore is unchanged, so its named path and
the singleton boundary operation are retained.

If no bridge separates `p,q`, their minimum edge cut in the connected full
component has order at least two.  The edge form of Menger's theorem gives
two edge-disjoint `p`--`q` paths.  A separating bridge precludes such a
pair, so the two alternatives in Theorem 3.1 are exhaustive and mutually
exclusive.  No vertex-disjointness is inferred.

## Four incidence splits

Under the added hypothetical-counterexample hypotheses, the audited
low-degree bound gives `alpha(G[S])<=3`.  Since `I,T` are independent
triples, this forces an edge between them and makes each of `p,q` adjacent
to at least one vertex of each block.

The corrected Corollary 3.2 of the parallel-cycle normalization therefore
applies to the selected path `P_E`: its ambient two-shore setup,
independence bound, root-to-`T` contacts, and clean connector hypotheses all
hold.  Applying it separately with `B=I` and `B=T` shows that both
`J_I(P_E)` and `J_T(P_E)` split their block.  Interchanging `E,F` and
repeating the same two applications for `P_F` gives the other two splits.
This is four uses for the two fixed paths, not an inference from one
selected incidence witness.  Lemma 3.1 of the same input makes the stated
no-carrier formulation equivalent.

## Unresolved scope

No internal gap was found at the audited hash.  The theorem produces one
operation-compatible aligned odd cycle and a valid bridge-or-two-edge-route
dichotomy outside the odd-wheel boundary.  It does not make the doubled
routes vertex-disjoint, coordinate the four incidence splits, construct a
`K_7`-minor model, return a smaller literal anti-neighbourhood component,
close the odd-wheel case, or prove `HC_7`.
