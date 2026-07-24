# Independent audit: two-vertex-shore bipartite contraction

**Verdict:** **GREEN** for Theorem 2.1, Corollary 3.1, and the stated
near-full limitation at the exact revision below.  This is a separate
internal cold audit, not external peer review.  The result remains active
and unpromoted, and it does not prove `HC_7`.

## Exact revision audited

```text
bf0b46e1d078505256e65cb0e0b08cff7a2ccf0b4ea2f9a6af84d3d8e7d1c64f  active/hc7_two_vertex_shore_bipartite_contraction.md
```

Any mathematical change to that file requires renewed audit.

## Audit of Theorem 2.1

The two contracted vertex sets are disjoint and connected: every member of
`P` is adjacent to `v`, and every member of `Q` is adjacent to `a`.
Moreover,

```text
|X-Z| >= |X|-2 >= 1,
```

so at least one of the contractions is nontrivial.  The resulting graph is
therefore a proper minor, and the proper-minor colouring hypothesis supplies
the required six-colouring.

Restricting the expanded colouring to `B` is valid.  An edge whose ends
would receive the same contraction-image colour could only have both ends
in `P` or both ends in `Q`; the two independence hypotheses exclude those
edges.  Every edge from `P` or `Q` to the other part, to `Z`, or to `B-X`
is represented by an edge incident with the corresponding contraction
image.  All other edges of `B` are unchanged.

The boundary consequently uses at most

```text
2 + |Z| <= 4
```

colours.  Two distinct colours are absent from the boundary and can be
assigned to `v` and `a`.  The edge `va` is then proper.  Since `(A,B)` is a
separation and `A-B={v,a}`, neither endpoint has a neighbour in `B-A`;
all its other neighbours lie in `X`, where both new colours are absent.
This yields the asserted forbidden six-colouring of `G`.

No connectivity, `K_7`-minor exclusion, Kempe-chain statement, or finite
enumeration is used implicitly.

## Corollary and limitation

Corollary 3.1 now imports all hypotheses of Theorem 2.1, including
`|X|>=3`.  Full adjacency of both endpoints makes either orientation of
every bipartition satisfy the endpoint-neighbourhood conditions, so an
odd-cycle transversal of order at most two would contradict the theorem.

Section 5 correctly limits the near-full inference.  In its displayed
distinct-unique-miss setting, `r` must lie in the class assigned to `a` and
`s` in the class assigned to `v`.  When they lie in one connected
bipartite component, that orientation exists exactly when they lie in
opposite bipartition classes.  The source does not claim that operation
provenance or host connectivity removes the incompatible-parity case.

## Corrections made before the pinned revision

The cold audit initially found two statement-level defects:

1. Corollary 3.1 did not import `|X|>=3`, making its literal statement false
   for a boundary of order at most two.
2. The near-full discussion inferred cross-adjacencies from the weaker
   phrase “misses `r`” and “misses `s`.”

The pinned revision fixes the first by invoking all hypotheses of Theorem
2.1 and the second by specifying distinct unique missed vertices.  Neither
correction changes the proof of Theorem 2.1.

## Trust boundary

The audit approves only the written contraction obstruction and its
full-endpoint corollary.  The computer-assisted order-eight OCT assertion
has a separate audit.  Their combination excludes the exact full/full,
order-eight, `K_4`-minor-free boundary configuration, but it does not settle
near-full endpoints, produce a rooted `K_4` or `K_7` minor model, or return a
strictly smaller exact-seven response.
