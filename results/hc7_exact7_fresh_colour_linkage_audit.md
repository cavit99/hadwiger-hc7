# Internal audit of the fresh-colour linkage theorem

**Verdict:** GREEN for Theorems 2.1, 3.1 and 5.1 and Lemma 4.1, subject to
the exact limitations in Section 6 of the source.

**Audited source:** `hc7_exact7_fresh_colour_linkage.md`, SHA-256

```text
d4725d119bac52e27f72a92645d9e1506473bcd66308378868027718539aad29
```

This is a separate internal mathematical audit, not external peer review.
Two independent agents checked the fresh-colour/disjointness argument and
the corrected augmented-boundary argument.

## 1. Fresh colour or a path through one shore

The trace argument is correct after dispatching the small case explicitly.
If fewer than all five non-`alpha` colours occur on `F`, a colour is already
absent from `Y`.  Otherwise `|F|=5` and the trace is injective.  A full
two-colour component containing both endpoints of the selected nonedge
gives the asserted path; its shortest boundary-to-boundary subpath has
interior in one component of `G-Y`.  If the endpoints lie in different full
components, switching the component containing one endpoint merges their
boundary colours and frees the other colour.  The switch avoids `alpha`, so
it preserves the exact block `J` and, in the edge-deletion colouring, the
equal colours at `p,v`.  Independent palette permutations can then give the
two absent colours the common name `beta`.

An earlier draft incorrectly inferred `|F|=5` merely from injectivity.  The
audited source now first handles the case in which fewer than five colours
occur, which is the only correction required by the independent audits.

## 2. The two vertex-disjoint obstruction paths

The noncomplete graph `F` has order at most five and is three-degenerate.
Las Vergnas--Meyniel therefore connects its proper four-colourings using the
palette outside `{alpha,beta}`.  If the boundary sequence lifts through the
closed `A`-shore, the final trace glues to the opposite-shore colouring.  At
the first failed lift, the standard full-component argument gives a path
`P` through `A` joining distinct boundary two-colour components.

Criticality of the deleted edge forces `p,v` into one full
`alpha`--`beta` component of the edge-deletion colouring; otherwise a
single Kempe interchange would make the missing edge proper.  This gives
the path `Q`, and absence of `beta` on `Y` makes `Q cap Y` a subset of `J`.

The simultaneous disjointness claim is valid.  Every successful lift and
the failed move uses colours outside `{alpha,beta}`, so the set of
`alpha`/`beta` vertices in `A` is literally unchanged.  Thus the internal
vertices of `P` and `Q` are disjoint.  Their boundary vertices are disjoint
because `P` ends in `Y-J`, whereas `Q cap Y subseteq J`; also `p` does not
belong to `P`.

## 3. Kempe connectivity of the eight-vertex boundary

If the boundary graph is five-degenerate, Las Vergnas--Meyniel applies.
Otherwise an eight-vertex spanning subgraph of minimum degree at least six
has complementary graph a matching.  Matching size at most one gives a
`K_7` subgraph; matching size two gives a `K_7` minor by contracting an edge
joining endpoints from the two missing pairs.  Hence a `K_7`-minor-free
exception is `K_8` minus a matching of size at least three.

That graph is complete multipartite with at most five parts.  Kempe moves
first make every two-vertex part monochromatic and then use the sixth colour
as a buffer to connect all labelled part-colourings.  This proves Lemma 4.1.

## 4. Actual augmented-boundary transition

Recolouring `p` from `alpha` to the fresh colour `beta` is proper on the
closed `A`-shore: `p` has no neighbour in `A`, `beta` is absent from `Y`,
and the restored edge `pv` is now proper.  Both shore traces are therefore
proper colourings of the actual graph on `X=Y union {p}`.

Lemma 4.1 supplies a boundary Kempe path.  A common trace glues the two
shores.  At the first right-side gain, read backwards, the two distinct
boundary bichromatic components cannot be joined merely by an edge of
`G[X]`, because every such edge is already present in the boundary
two-colour graph.  The obstruction path consequently has nonempty interior
in one component `D` of `G-X`.  Since `N(D) subseteq X` and `A` is another
nonempty component of `G-X`, seven-connectivity forces `|N(D)|` to be seven
or eight.  These are exactly outcomes 2 and 3 of Theorem 5.1.

The inclusion of the actual edge `pv` in `G[X]` is essential.  A prior
formulation deleted it on one side, allowing the alleged obstruction to be
the direct edge itself; the audited theorem fixes that flaw by recolouring
`p` before comparing traces.

## 5. Trust boundary

The source proves a genuine simultaneous rooted-two-path alternative and a
selected order-eight-full component.  It does **not** allocate those paths
among five inherited branch-set labels, decode them into a `K_7` model,
make every component of the order-eight complement boundary-full, give a
common full partition on the order-seven output, or provide a ranked
recursive descent.  None of those stronger statements was used in this
audit.
