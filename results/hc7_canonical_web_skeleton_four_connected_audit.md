# Independent audit: four-connectivity of the canonical web skeleton

**Audited file:** `results/hc7_canonical_web_skeleton_four_connected.md`
**SHA-256:** `0a0f5db310c6896ba8e3aef9fd81a57c9d9cc697ff3b2cb9dad373f686579c08`
**Verdict:** **GREEN.**  Theorem 1.1 and its stated trust boundary are
correct under the standing convention that graphs are finite and simple
and that the four vertices on the displayed outer-face boundary are
distinct.  No substantive correction is required.

## Separator transfer

Lemma 2.1 is valid.  If `T` is a facial triangle of the skeleton and
`T-U` is nonempty, its remaining vertices are pairwise adjacent and hence
lie in one component of `W-U`.  The attached clique `X_T` has no neighbour
outside `T\cup X_T`, so it can meet only that component.  If `T` is
contained in `U`, then `X_T` has no remaining neighbour in the skeleton.
Thus no attachment clique can reconnect two components of `W-U`.

Because `Q` is spanning in `W^+`, passing from `W^+-U` to the subgraph
`Q-U` cannot create an edge between its components.  Hence every cut of
the skeleton of order at most three is a cut of `Q` of the same order.
Corollary 2.2 follows exactly from the two cut hypotheses on `Q`.

## Outer diagonals

If `ac` were an edge of `W`, then `abc` and `acd` would be triangles of
`W` and therefore facial by hypothesis.  These two faces occupy the disk
inside the outer four-cycle, leaving no room for another skeleton vertex
or edge.  The resulting graph has the two-vertex cut `{a,c}`, contrary to
Corollary 2.2.  The argument for `bd` is symmetric.  In particular, both
outer-face augmentations used later are simple.

## Maximal-planar cut argument

Adding `ac` through the outer face produces a plane graph `M` all of whose
faces are triangles; hence `M` is maximal planar.  The standard fact used
in the proof is correct: a three-vertex cut in a maximal planar graph is
the vertex set of a separating triangle, and a facial triangle is not a
three-vertex cut.

For a hypothetical three-cut `U` of `W`, Corollary 2.2 gives
`U={c,d,x}`.  Since the added edge has endpoint `c`, deleting `U` removes
that edge, so `M-U=W-U`.  The case analysis is exhaustive:

- if `x=a`, then `acd` is a new facial triangle of `M`;
- if `x=b`, then `bd` is absent, so `U` is not a triangle; and
- otherwise, a triangle `cdx` in `M` uses no added edge, is already a
  triangle of `W`, and remains facial after the outer-face augmentation.

None can be a separating triangle of `M`, so `W` has no three-cut.  Along
with Corollary 2.2, this proves that `W` is four-connected.  The second
augmentation needs no duplicate separator argument: `bd` is absent,
`W+bd` is again a simple plane triangulation, and adding an edge cannot
decrease vertex connectivity.  The same observation applies to `W+ac`.

## Hamiltonian-connectedness and its limitation

The cited bibliographic claim is correct.  Thomassen's 1983 theorem
implies that every four-connected planar graph is Hamiltonian-connected:
C. Thomassen, *A theorem on paths in planar graphs*, Journal of Graph
Theory **7** (1983), 169--176,
<https://doi.org/10.1002/jgt.3190070205>.

The draft uses this only for `W`, and correctly declines to transfer a
Hamilton path to `Q`: `Q` may omit skeleton edges.  It also correctly
notes that the alternating outer pairs `(a,c)` and `(b,d)` cannot be
joined by two vertex-disjoint paths in the plane skeleton itself.  Thus
Hamiltonian-connectedness neither supplies the missing rooted linkage nor
preserves any boundary-colouring data.

## Trust boundary

This audit establishes only the skeleton theorem.  It does not establish
four-connectivity of `Q`, replace virtual skeleton edges by paths in `Q`,
produce the missing labelled linkage, or give a colouring transfer across
the order-eight boundary.  Those limitations are accurately stated in
the audited file.
