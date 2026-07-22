# Audit: minimal degree-eight root-star response reduction

**Audit type:** separate internal cold audit

**Verdict:** **GREEN**

Audited theorem:
[`hc7_degree8_minimal_root_star_response_reduction.md`](hc7_degree8_minimal_root_star_response_reduction.md)

Audited source SHA-256:

```text
4fcf9458286ebf1686dea2af44cc64b7bc18e01747bfb739e83a182ff22937e7
```

The original mathematical content was cold-audited before promotion at
SHA-256

```text
7b5aab78681b23c3f1f6823026d71d3785b7c7661024476ea5e084a03cf9ac63
```

The current revision additionally includes Corollary 4.3 and its proof.

## Proposition 2.1

- Inclusion-minimality has the required quantifier: no proper subset of
  `J` has any proper six-colouring whose boundary trace is `tau`.  Hence a
  deleted edge which were proper under `d` could be restored, contradicting
  that minimality.  All leaves have colour `gamma`; their mutual edges are
  present in `G-J`, so properness makes `L` independent.
- For every nonempty `K subseteq J`, the vertices incident with `K` induce
  a genuine star.  Contracting it is a proper minor.  On expansion, exactly
  the edges in `K` are omitted and monochromatic.  Every edge in `J-K`
  remains an edge incident with the contraction image and is therefore
  proper.  No leaf--leaf conflict is hidden because `L` is independent.
- When `K` is proper in `J`, equality of the boundary equality partition
  with that of `tau` permits one global palette permutation of the whole
  colouring.  It would give a literally `tau`-aligned colouring after
  deleting the proper subset `K`, contrary to the definition of `J`.
- The component opposite `Q` and the pole side contain none of the deleted
  edges, so restricting `c_K` gives an extension of its literal trace
  through that side.  If the same trace extended through the intact
  `Q`-shore, it could be glued to this restriction and would six-colour
  `G`.  Thus the extension/rejection assertion uses one fixed trace and
  does not exchange existentially chosen colourings.

## Lemma 3.1

- If the `gamma`--`delta` component through a selected leaf `v` misses
  `X`, swapping that whole component fixes `tau`.  The set `R` of deleted
  star edges whose leaf lies in the component is nonempty.  Every such
  leaf changes away from `gamma`, so precisely those edges may be restored.
  If `R` is proper in `J`, this contradicts inclusion-minimality; if
  `R=J`, it directly six-colours `G`.  These two cases exhaust the
  restoration quantifier.
- A shortest path to its first boundary vertex has all internal vertices
  in `Q`, because it starts in the component `Q` of `G-X` and cannot move
  to another component before reaching `X`.  Paths for different alternate
  colours can meet only on `gamma`-coloured vertices.  They cannot share an
  edge in a proper colouring, and their first edges at `v` are distinct.

## Theorem 4.1: capacitated Menger and the exact cut

- Direct path ends have their five distinct alternate colours.  They avoid
  `x` because `xv` is deleted.  A direct end cannot equal the end of a
  non-direct path of another colour pair.  Consequently the required set
  `I` of order `ell+1`, containing `x` and all non-direct ends while
  avoiding all direct ends, exists inside the eight-set `X`.
- Menger is applied to the original induced graph
  `G[(Q-{v}) union I]`, not to `G-J`.  Unit capacity on `Q-{v}` and
  unlimited capacity on `I` gives either `ell` paths, one from every
  source and disjoint outside `I`, or a set
  `Z subseteq Q-{v}` of order at most `ell-1` meeting every source--`I`
  path.  Other edges of `J` are allowed in this graph; this does not alter
  the prescribed first edges in the packing outcome.
- In the cut outcome, a source survives because there are `ell` sources
  and fewer than `ell` cut vertices.  Its component `A` in
  `G[Q-({v} union Z)]` has no neighbour in `I`, even through another edge
  of `J`, since such an edge would itself complete a source--`I` path
  avoiding `Z`.  Componenthood then gives

  ```text
  N_G(A) subseteq (X-I) union {v} union Z.
  ```

- The pole and the other exterior component leave a vertex outside
  `A union N_G(A)`, so this neighbourhood is an actual separator.
  Its displayed upper bound is at most seven.  Seven-connectivity forces
  `|Z|=ell-1`, `|N_G(A)|=7`, and equality with the displayed disjoint
  union; no unbounded separator is being called an exact-seven output.
- Every original non-direct tail is a source--`I` path and meets `Z`.
  Choosing one cut vertex on each of the `ell` tails and using
  `|Z|=ell-1` puts one vertex on two different-colour tails.  Their colour
  intersection is exactly `gamma`.  Together with `v`, this proves the
  two asserted members of the exact boundary `gamma`-class.
- Although `d` is defined only on `G-J`, every missing edge is incident
  with `x`.  The equality for `N_G(A)` places `x in I` outside
  `A union N_G(A)`.  Hence no missing edge has both ends in the returned
  closed shore, and the restriction of `d` there is proper in the original
  graph `G`.

## Generic restart and Corollary 4.2

- For any edge from `Y=N_G(A)` to `A`, minor-criticality supplies a
  six-colouring of its deletion; its endpoints must be monochromatic or
  the edge could be restored.  The sets `A,Y,V(G)-(A union Y)` satisfy the
  definition of a generic exact-seven response interface: `A` is connected,
  both open sides are nonempty, `Y=N_G(A)`, and `|Y|=7`.  Since `v` is not
  in `A`, the returned shore has strictly smaller order than `Q`.  This is
  precisely the hypothesis set of the cited generic exact-seven response
  restart, but it does not preserve the old anti-neighbourhood labels.
- Applying Theorem 4.1 separately to every edge of `J` has the stated
  quantifiers: either one strict restart exists, or each edge has its own
  clean fan.  No mutual disjointness of those separately obtained fans is
  inferred.
- The boundary set `B` is independent because `d` is proper on the returned
  closed shore, and `A union B` is connected because every boundary vertex
  has a neighbour in `A`.  Contracting a spanning tree of that union and
  expanding the contraction image only over `B` on the opposite closed
  shore is proper.  Every vertex of `Y-B` has a neighbour in `A`, hence was
  adjacent to the contraction image and avoids its colour.  Thus `B` is an
  exact boundary class on both shores.
- If `G[Y-B]` is a clique, its vertices receive distinct colours, all
  different from the colour on `B`.  Both boundary equality partitions are
  therefore `B` together with singleton blocks.  A palette permutation
  aligns them literally and the anticomplete open shores glue, so this case
  would six-colour `G`.

## Corollary 4.3: shore-confined prescribed six-fan

- The `h` direct paths have distinct ends `D`, all different from `x`, and
  the first neighbours `S` of the `ell=5-h` non-direct paths are distinct.
  The target set

  ```text
  T=X-(D union {x})
  ```

  has order `ell+2`, so it has sufficient terminal capacity for `ell`
  paths.
- For `ell>=1`, the vertex-set form of Menger in
  `G[(Q-{v}) union T]` either gives `ell` fully vertex-disjoint
  `S`--`T` paths, hence distinct sources and distinct terminal vertices,
  or a vertex set `Z` of order at most `ell-1` separating the surviving
  sources from the surviving terminals.  Since `|S|=ell`, at least one
  source survives.
- The component `A` of that source in the graph after deleting `Z` contains
  no vertex of `T-Z`.  All its neighbours in `Q` outside `A` belong to
  `{v} union Z`; the omitted boundary vertices are exactly
  `D union {x}`, while any deleted target is already in `Z`.  Therefore

  ```text
  N_G(A) subseteq {v} union D union {x} union Z,
  ```

  whose order is at most
  `1+h+1+(ell-1)=6`.  The pole and the other exterior component remain
  outside `A union N_G(A)`, so this would be an actual separator of order
  at most six, contradicting seven-connectivity.
- Truncate the resulting linkage paths at their first vertices of `T` and
  prepend the prescribed `v`-edges.  They then have open interiors in `Q`,
  avoid `D union {x}`, and retain all non-direct prescribed first edges.
  Adding the `h` direct paths and `vx` gives six paths with distinct
  boundary ends, sharing only `v`, and meeting `X` only at those ends.
- When `ell=0`, the five direct paths and `vx` already have this form.  The
  argument for `ell=1` is also covered: failure would give `Z=emptyset`
  and the same separator of order six.

## Dependencies and unresolved limits

No internal proof gap was found.  The prescribed-spoke theorem is used with
the same five colour-indexed first edges and eight-vertex boundary; the new
argument correctly changes the Menger host to the original graph so that
all other star edges are accounted for.  The generic exact-seven restart
is invoked only after its connected-shore, exact-neighbourhood, selected
edge, proper-minor colouring, and nonempty-opposite-side hypotheses have
been established.

The result gives only a generic exact-seven shore decrease.  It does not
retain the original selected anti-neighbourhood component, boundary labels,
or complete equality partition.  The colour-derived fan in Theorem 4.1 may
have repeated boundary ends; Corollary 4.3 removes that repetition by
rerouting but does not retain the colours of the new ends.  Fans produced
for different edges of `J` may still intersect.  Proposition 2.1 also does
not transport a singleton contraction response back to `tau`; that
quantifier obstruction remains explicit in Section 5 of the theorem.

The status-only promotion of the audited source has hash

```text
8378f08308ce6fd7b4b701f76a925c61c0d3f15e09965ac185ce60e39b06a580
```

and makes no mathematical change to the revision audited above.
