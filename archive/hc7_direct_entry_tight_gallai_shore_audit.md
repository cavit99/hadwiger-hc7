# Independent audit of the tight Gallai-shore reduction

**Verdict:** GREEN for Theorem 2.1 and the deleted-edge trace statement in
Section 3, at the exact source revision identified below.

**Audited source:** `hc7_direct_entry_tight_gallai_shore.md`, SHA-256

```text
ef6556490d0eba5e4affd0746f48adeb58a7c806d0375476ec338ab1ee165ab4
```

This is a separate internal mathematical audit, not external peer review.
It checks the degree-list argument, every endblock case, the literal
whole-graph neighbourhood, the packing argument, the block-cutvertex-tree
conclusion, and every placement of the two deleted direct-entry edges.  The
upstream two-edge list-critical theorem was separately audited GREEN at
source SHA-256
`ebe14cda6d5a16e0c9964ea9dd698ce538677fad9850b35ae57a3e4b3f830e8e`.

## 1. Hypotheses and the degree-choosability step

The open shore `G[R]` is assumed connected and not colourable from the fixed
lists

\[
 A(v)=[6]\setminus
      \{\psi(s):s\in N_G(v)\cap S\}.
\]

The tightness hypothesis gives `|A(v)|=d_{G[R]}(v)` at every vertex.  Thus
the Borodin--Erdos--Rubin--Taylor degree-choosability theorem applies in its
contrapositive form: a connected graph admitting a noncolourable list
assignment with list sizes at least its vertex degrees is a Gallai tree.
Consequently every block of `G[R]` is a complete graph or an odd cycle.

This implication also covers the harmless one-vertex case under the usual
convention that `K_1` is complete.  The subsequent endblock argument is
used only when `G[R]` has more than one block.

## 2. Exclusion of a single-edge endblock

Let `B` be an endblock, let `w` be its unique cutvertex, and suppose for
contradiction that `B=wv` is a single edge.  The noncutvertex endpoint `v`
belongs to no other block, so

\[
                         d_{G[R]}(v)=1.
\]

Tightness yields `|A(v)|=1`.  Since the ambient palette has six colours,
the definition of `A(v)` then says that the neighbours of `v` in `S` use
five distinct colours.  This contradicts the hypothesis that at most four
colours occur anywhere on `S`.  Therefore every endblock is either a clique
of order at least three or an odd cycle.

After deleting `w`, either kind of block remains nonempty and connected:
a clique remains a clique and an odd cycle becomes a path.  Thus

\[
                         X_B=V(B)-\{w\}
\]

is a legitimate connected open side.

## 3. Exact whole-graph neighbourhood of an endblock lobe

Every vertex of `B-w` is a noncutvertex of `G[R]`.  Hence it belongs to no
other block, and there is no edge from `X_B` to
`R-(X_B\cup\{w\})`.  The vertex `w` does have a neighbour in `X_B` because
single-edge endblocks have already been excluded.  In addition,
`E_G(L,R)=emptyset`.  It follows, with no quotienting or contraction, that

\[
 N_G(X_B)=\{w\}\mathbin{\dot\cup}
          (N_G(X_B)\cap S).
\]

The set on the right separates the nonempty connected set `X_B` from the
nonempty opposite shore `L`.  Seven-connectivity therefore gives

\[
 1+|N_G(X_B)\cap S|=|N_G(X_B)|\ge 7.
\]

Since `|S|=7`, the boundary-contact number is exactly six or seven.  Six
contacts give an actual separation of order seven.  This is a strict side
reduction: `X_B` is a proper subset of `R`, since `w` and vertices of at
least one other block lie outside it.

## 4. Packing and the block-cutvertex tree

If no endblock has six boundary contacts, every endblock lobe is connected
and adjacent to all seven literal vertices of `S`.  Lobes belonging to
distinct endblocks are vertex-disjoint, including when the endblocks share
their cutvertex, because the cutvertices were removed from the lobes.

The assumed packing maximum of two therefore bounds the number of
endblocks by two.  A finite connected graph with more than one block has at
least two endblocks, so there are exactly two.  In the block-cutvertex tree,
cutvertex nodes have degree at least two and the leaves are precisely the
endblock nodes.  A finite tree with exactly two leaves is a path.  This
proves the third outcome, including the asserted two disjoint
boundary-full endblock lobes.

No converse is used: the proof does not claim that an arbitrary Gallai
block chain has packing number two.

## 5. Exhaustion of the deleted-edge placements

For the exact order-seven outcome, write

\[
 T=N_G(X_B)=\{w\}\mathbin{\dot\cup}(N_G(X_B)\cap S).
\]

The two closed sides are `G[X_B\cup T]` and `G-X_B`; their intersection is
literally `T`.  The colouring `psi` is proper on `G-{e,f}`, so its two
restrictions agree vertex by vertex on `T` and can fail only at `e` or `f`.

Consider either deleted edge, say `e=xp` with `x in S` and `p in R`.
Exactly one of the following occurs.

1. If `p in X_B`, then `x in T` and `e` belongs only to the
   `X_B`-closed side.
2. If `p notin X_B` and the next case does not occur, both endpoints belong
   to the opposite closed side (an endpoint in `T` is, of course, shared by
   both sides, but the edge still has no endpoint in `X_B`).
3. If `p=w` and `x in T`, then both endpoints lie in `T`, so `e` is a
   literal boundary edge.

These cases are exhaustive because `T\cap R=\{w\}`.  The same analysis
applies independently to `f=yq_0`.  Thus the common assignment on `T` is
proper unless one of the deleted edges is in the explicit boundary-edge
placement; in that placement it is improper precisely on the deleted
boundary edge or edges.  This is exactly a common double-deletion trace,
not a claim that either individual edge has already been repaired.

## 6. Trust boundary

The theorem proves an unbounded host-level reduction only under all three
of its stated additional hypotheses:

1. the list-critical core fills the open shore and is tight at every
   vertex;
2. the simultaneous-contraction colouring uses at most four colours on the
   seven-vertex boundary; and
3. the shore contains at most two pairwise vertex-disjoint connected
   subgraphs adjacent to every boundary vertex.

Within that scope, every branching block-cutvertex tree yields a strict
exact order-seven side, while the only unresolved structures are one
complete or odd-cycle block and a path of Gallai blocks.  The proof does
not colour either original closed shore, synchronize a proper boundary
partition, eliminate the single-block or block-chain outcomes, preserve an
older set of five branch-set labels, or construct a `K_7`-minor model.
It therefore does not prove `HC_7` and should not be cited outside this
conditional all-tight shore-filling branch.
