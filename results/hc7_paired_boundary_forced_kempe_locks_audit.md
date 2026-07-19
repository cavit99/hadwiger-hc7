# Audit of boundary-forced Kempe locks in the paired exact-seven response

**Verdict:** GREEN.  The theorem, both paired-partition corollaries, and the
stated scope limitations are correct.

**Audited source:**
[`hc7_paired_boundary_forced_kempe_locks.md`](hc7_paired_boundary_forced_kempe_locks.md)

**Source SHA-256:**
`d7a7f3788928f5ddb9fee1ef4776bcc0ffe9c8751a925f505a9774665eba2c08`

The only change from the audited `5a5d1723...` revision is the source's
status line and link to this audit; no mathematical content changed.

This is a separate internal mathematical audit, not external peer review.

## 1. Hypotheses and endpoint equalities

The hypotheses give a proper `q`-colouring `psi` of the common edge-deletion
host `G-{e,f}` with the selected literal boundary trace.  If the ends of
`e` had different colours, restoring `e` would give a proper colouring of
`G-f` inducing the selected equality partition on `X`, contrary to the
hypothesis on `f`.  The symmetric argument makes the ends of `f`
monochromatic.  Vertex-disjointness of `e,f` is exactly the hypothesis used
later when invoking the common-host allocation theorem.

## 2. Boundary-component criterion

Suppose the ends `a,b` of `e` have colour `i` and lie in distinct
`i`--`j` components `Q_a,Q_b`.  Switching either whole component preserves
properness in `G-{e,f}` and makes `e` proper.  If, say, `Q_a` avoided `X`,
the switch would preserve the selected boundary trace; restoring `e` would
then colour `G-f` with that trace.  This contradicts the assumed failure of
the single-edge trace.  Thus both endpoint components meet `X`.

Their boundary intersections lie in `B_i union B_j`.  A path between those
intersections in `G[X][B_i union B_j]` would also be an `i`--`j` path in the
common edge-deletion host and would join the two endpoint components.
Therefore the two intersections belong to distinct nonempty components of
the displayed boundary graph.  Lemma 2.1 and its contrapositive are valid.

Each block rule is then exact:

1. an empty block together with a singleton induces one vertex;
2. two adjacent singleton blocks induce one edge; and
3. a singleton complete to an independent block induces a connected star.

The third rule correctly requires contact with every literal member of the
independent block; a single contact would not establish connectedness of the
whole boundary subgraph.

## 3. The `(2,3)` paired partition

Here the six blocks are `M`, `{x}`, `{y}`, and the three singleton vertices
of the clique `K`, so all six palette colours occur on `X`.  If the equality
colour is carried by a vertex of `K`, the two clique edges to the other
members of `K` force two locks.  More generally, every edge between two
singleton blocks forces the corresponding lock, and a singleton complete to
`M` forces the lock involving the colour of `M`.

No further positive lower bound follows from the stated boundary hypotheses
when the equality colour is carried by `x`, `y`, or `M`: the hypotheses do
not impose an edge incident with `x` or `y` beyond any edge explicitly
present, and do not require any singleton vertex to be complete to `M`.
The corollary therefore does not infer an unstated boundary adjacency.

## 4. The `(3,2)` paired partition

The five blocks use exactly five of the six palette colours, so the colour
`o` absent from `X` is unique.  Pairing its empty boundary block with any
singleton block forces a lock.  Consequently:

* equality colour `o` gives the four locks indexed by `x`, `y`, and the two
  vertices of `K`;
* equality colour at `x` or `y` gives at least the lock indexed by `o`; and
* equality colour at a vertex of `K` gives the `o` lock and the lock indexed
  by the other member of `K`.

If the equality colour is carried by the three-vertex independent block
`M`, its union with the empty `o` block is three isolated vertices.  The
boundary-component criterion therefore supplies no `M`--`o` lock.  The
source correctly states only the locks obtained from singleton vertices
complete to `M`.

All arguments are symmetric in `e` and `f`.

## 5. Stronger minor-critical allocation and trust boundary

Section 4 now expressly restricts the three-/four-lock common-host
allocation to the stronger setting `chi(G)=7` in which every proper minor is
six-colourable.  Those are the hypotheses of the separately audited
common-host double-contraction theorem, and the selected `psi` descends to
the simultaneous contraction because both endpoint pairs are monochromatic.

The new result is only a boundary-forced palette-lock statement.  It does
not make any of the following invalid inferences:

* a palette colour identifies a named minor-model branch set;
* lock paths for different colours are internally disjoint;
* a boundary lock alone yields a `K_7`-minor model; or
* the selected boundary partition is induced by colourings of both closed
  shores.

The stated remaining need for literal first-hit information and a
partition-specific connected-subgraph system is therefore accurate.

## Final audit conclusion

The repaired `q=6` hypothesis makes the absent-colour count exact, and the
minor-critical qualification in Section 4 matches the cited allocation
theorem.  No unresolved mathematical assumption remains in the stated
claims.  The source is GREEN at the pinned hash above.
