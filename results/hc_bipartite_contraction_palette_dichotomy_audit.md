# Independent audit: palette dichotomy after contracting an induced bipartite subgraph

**Audited file:** `results/hc_bipartite_contraction_palette_dichotomy.md`
**Original proof SHA-256:** `639c400113139c9d299bf2508b464cda895d2aab863340d02ece069356916efe`
**Repaired and finally audited SHA-256:** `13926a5f70db1c651a6c7927193a5c2ebf076775163d39b64318ee40a60efb64`
**Promoted theorem SHA-256:** `9856ce9908d2a2d6a3e36177d32ec4aa0d9f389b1e2fcd6632829db9ce08dbc6`
**Verdict:** **GREEN.**

The promoted theorem differs from the repaired audited revision only in
its status line.  Its statement and proof are unchanged.

The proof is self-contained.  Every theorem assertion follows from the stated
hypotheses.  No clique-minor conclusion is implicit in the argument.  The two
precision issues found in the original revision were repaired exactly as
specified and the repaired revision was rechecked.

## 1. Line-by-line mathematical audit

### Chromatic number after contraction

Contracting the connected subgraph on at least two vertices strictly reduces
the vertex count, so `G/Q` is a proper minor and is `(k-1)`-colourable.  If it
were `(k-2)`-colourable, the colour of the contracted vertex could be assigned
to `A` and one fresh colour to `B`.  Because `G[W]` is bipartite with parts
`A,B`, and no external neighbour of `W` has the contracted vertex's colour,
this would give a `(k-1)`-colouring of `G`.  This proves
`chi(G/Q)=k-1`; it also covers the possibility that the assumed colouring
uses fewer than `k-2` colours.

### Palette saturation on both sides

If one part, say `A`, has no external neighbour of a noncontracted colour
`delta`, assigning `delta` to `A` and the contracted colour `gamma` to `B`
extends the colouring of `R`.  The two possible boundary conflicts are
excluded respectively by the hypothesis and by properness at `q`.  The
argument is symmetric in `A,B` and does not require the bipartite graph on
`W` to be complete.

### Common bichromatic component

The simultaneous Kempe change is valid because it is performed on a union of
whole components of the `gamma,delta` subgraph.  If there were no common
component, switching every component containing a `delta`-neighbour of `A`
would remove colour `delta` from the external neighbourhood of `A` without
introducing colour `gamma` into the external neighbourhood of `B`.  No new
`delta`-neighbour of `A` is created, since no `gamma`-coloured vertex is
adjacent to `W` in the original colouring.  The resulting colouring extends
over `A,B`, contradicting `chi(G)=k`.

### Concentrated support and rotation

If the unique support component is `K_delta`, it contains all
`delta`-coloured neighbours of `W`.  After swapping `gamma,delta` on it,
no vertex coloured `delta` is adjacent to `W`: the old `delta` boundary
vertices became `gamma`, old `gamma` vertices were not adjacent to `W`, and
there is no second support component.  Recolouring `q` with `delta` is
therefore proper.  Commonness supplies colour `gamma` on both sides, while
Theorem 1.1(2) supplies every untouched colour on both sides.

For an additional colour `theta`, if no originally `delta`-coloured vertex
of `K_delta` has a `theta`-neighbour in `R`, all such vertices may be
recoloured `theta`: they are independent and have no neighbour of their new
colour.  This removes all `delta` boundary contacts, after which colouring
`A` with `gamma` and `B` with `delta` contradicts `chi(G)=k`.  A
`theta`-neighbour necessarily lies outside `K_delta`, since that component
contains only the two displayed colours.

### Diffuse support and the separation

A support vertex in a different bichromatic component is neither in `K` nor
adjacent to `K`; otherwise the two components would be joined in the induced
two-colour graph.  Thus the displayed separation has two nonempty open
sides.  Every neighbour of `K` in `R` has a colour outside
`{gamma,delta}`, and every edge from `W` into `K` ends at an originally
`delta`-coloured vertex, because no `gamma`-coloured vertex is adjacent to
`W`.  Commonness is exactly what makes the boundary meet both `A` and `B`.
The lower bound on its order in an `ell`-connected graph is then immediate.

### One-sided refinement

If `L` contains a `delta`-neighbour of `A` but none of `B`, and it contained
all `delta`-neighbours of `A`, switching `L` would permit `A` to receive
`delta` and `B` to receive `gamma`.  Original `gamma` boundary contacts do
not exist, and the hypothesis on `B` prevents the switch from creating a
`gamma` conflict there.  Hence a second support component exists and gives
the claimed nonempty opposite side.  The exact boundary description follows
by the same two-colour-component argument as in the diffuse case.

### Sharpness and edge cases

- `Q` must contain at least two vertices for `G/Q` to be a proper minor.
- The proof only needs `G[W]` to be bipartite with the displayed parts and a
  connected spanning subgraph on `W` to be contracted.  Selecting a
  non-induced bipartite subgraph while allowing extra same-part edges in
  `G[W]` invalidates the expansion step; the `K_k`/three-vertex-path example
  correctly witnesses this.
- For an edge, both parts are singletons and all arguments specialize to the
  adjacent-pair lemma.
- For `k=3` the `theta` assertion is vacuous.  For `k=2` the only
  minor-minimal example is `K_2`, and there is no second palette colour, so
  excluding it is harmless.

### Label-preserving scope

Contracting a connected subgraph contained in one branch set preserves that
branch set's connectivity and every adjacency to the other disjoint branch
sets.  No labels merge.  A palette rotation changes only a colouring, so it
does not modify the existing minor model.  The final limitations are
correct: the lemma neither splits the containing branch set nor controls how
the bichromatic component traverses other branch sets.

## 2. Adversarial checks

An independent exhaustive sanity check was run on every connected unlabeled
graph of order at most seven generated by `geng`.  To test substantially more
than the minor-minimal examples available at these orders, the checker used
the weaker local hypotheses actually consumed by the proof:

1. `chi(G)=k>=3`;
2. `W` induces a connected bipartite graph; and
3. `chi(G/W)=k-1`.

It then enumerated every normalized `(k-1)`-colouring of `G/W` and checked
both-side saturation, existence of a common component, and the external
`theta`-contact in every concentrated case.  The check covered 924
chromatic graphs, 11,563 eligible `(G,W)` pairs, and 47,409 colourings.  Of
the eligible pairs, 9,318 had `|W|>2` and a non-complete bipartite contracted
subgraph.  No counterexample was found.  This finite check is only a sanity
test; the written proof above is the basis of the verdict.

For `k<=6`, actual graphs satisfying the full proper-minor hypothesis give
no non-edge laboratory beyond the edge case: the known cases of Hadwiger's
conjecture imply such a graph is `K_k`.  The relaxed-hypothesis enumeration
therefore provides the relevant small non-complete-bipartite stress test.

## 3. Repairs incorporated in the final audited revision

These did not change the proof or theorem content.  Both are present in the
finally audited revision.

1. In Theorem 1.2(1), qualify the last assertion as referring to the
   **original colouring `psi`**.  Read literally as referring to the newly
   rotated colouring in the preceding sentence, “a `delta`-coloured vertex
   of `K_delta`” can be false: in the edge case in `K_4`, the component may
   contain no vertex coloured `delta` after the rotation.  The proof
   unambiguously establishes the assertion for vertices originally coloured
   `delta`.
2. In Section 6, replace “the common bichromatic component ... meets both
   `A` and `B`” by “is adjacent to both `A` and `B`” (or “contains a
   neighbour of each”).  The component lies in `R` and hence does not
   literally intersect either subset of `W`.

There are no unresolved mathematical gaps in the finally audited result.
