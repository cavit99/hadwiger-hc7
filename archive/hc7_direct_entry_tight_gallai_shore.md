# Tight Gallai shores reduce to an exact seven-boundary or a block chain

**Status:** written proof; audit pending.  This is an unbounded structural
consequence of the shore-filling equality case in
[`hc7_direct_entry_two_edge_list_core.md`](../results/hc7_direct_entry_two_edge_list_core.md).
It eliminates every branching Gallai-tree obstruction when the simultaneous
contraction trace uses at most four boundary colours.  It does not eliminate
the remaining single-block and block-chain outcomes and does not prove
`HC_7`.

## 1. Setting

Let `G` be seven-connected, and suppose

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,qquad E_G(L,R)=\varnothing,              \tag{1.1}
\]

where `L,R` are nonempty.  Let `psi` be the simultaneous two-edge colouring
from the direct-entry list-core theorem, and define for `v in R`

\[
 A(v)=[6]\setminus
      \{\psi(s):s\in N_G(v)\cap S\}.                   \tag{1.2}
\]

Assume all of the following.

1. The list-critical core fills the open shore: `G[R]` is connected,
   vertex-minimal non-`A`-colourable, and

   \[
                          d_{G[R]}(v)=|A(v)|            \tag{1.3}
   \]

   for every `v in R`.
2. At most four colours occur on `S` under `psi`.
3. The maximum number of pairwise vertex-disjoint connected subgraphs of
   `G[R]` adjacent to every literal vertex of `S` is two.

The third hypothesis is exactly the rich-side packing number in the
remaining exact-seven `(1,2)` branch.

## 2. Endblock reduction

### Theorem 2.1 (exact boundary or Gallai block chain)

Under the hypotheses above, one of the following holds.

1. There is a nonempty proper connected set `X subset R` such that

   \[
                              |N_G(X)|=7.               \tag{2.1}
   \]

   Thus `N_G(X)` is the literal boundary of an actual order-seven
   separation and `|X|<|R|`.
2. `G[R]` is one block, and that block is a complete graph or an odd cycle.
3. The block-cutvertex tree of `G[R]` is a path.  Its two endblock lobes are
   vertex-disjoint connected subgraphs, each adjacent to every vertex of
   `S`.

More precisely, for every endblock `B` with cutvertex `w`, put

\[
                              X_B=V(B)-\{w\}.           \tag{2.2}
\]

Then `X_B` is connected and

\[
       N_G(X_B)=\{w\}\mathbin{\dot\cup}
                \bigl(N_G(X_B)\cap S\bigr),
       \qquad |N_G(X_B)\cap S|\in\{6,7\}.             \tag{2.3}
\]

The first value gives outcome 1.  If the first value never occurs, every
endblock lobe is boundary-full and there are exactly two endblocks, giving
outcome 3.

#### Proof

Equation (1.3) and non-`A`-colourability allow the
Borodin--Erdos--Rubin--Taylor degree-choosability theorem to be applied.
Hence `G[R]` is a Gallai tree: every block is a complete graph or an odd
cycle.

Suppose first that `G[R]` has only one block.  This is outcome 2.  Otherwise
let `B` be an endblock and let `w` be its unique cutvertex.  The block `B`
cannot be a single edge.  Indeed, its endpoint `v` different from `w` would
have `d_{G[R]}(v)=1`; tightness would give `|A(v)|=1`, so (1.2) would say
that `v` sees five distinct boundary colours.  This contradicts the
assumption that at most four colours occur on all of `S`.

Thus `B` is a complete graph of order at least three or an odd cycle.
In either case `X_B=B-w` is nonempty and connected.  The defining property
of an endblock gives no edge from `X_B` to
`R-(X_B\cup\{w\})`.  There is no edge from `R` to `L`.  Therefore its full
whole-graph neighbourhood is exactly the set in (2.3).  This set separates
the nonempty connected set `X_B` from the nonempty opposite shore `L`.
Seven-connectivity gives

\[
            1+|N_G(X_B)\cap S|=|N_G(X_B)|\ge7.         \tag{2.4}
\]

Since `|S|=7`, the boundary contact number is six or seven.  At six,
(2.3) is an actual order-seven separation.  The set `X_B` is a proper
subset of `R`, because `w` and at least one vertex of another block lie
outside it.  This proves outcome 1 and its strictness.

Assume now that no endblock has only six boundary contacts.  Every endblock
lobe `X_B` is then connected and adjacent to all seven vertices of `S`.
Lobes of distinct endblocks are vertex-disjoint.  The packing hypothesis
therefore permits at most two endblocks.  Every finite connected graph with
more than one block has at least two endblocks, so there are exactly two.
The block-cutvertex tree is a finite tree whose leaves are precisely the
endblock nodes.  A finite tree with exactly two leaves is a path.  This is
outcome 3.  \(\square\)

## 3. Trace inherited by the returned boundary

Retain the two deleted direct-entry edges

\[
                         e=xp,\qquad f=yq_0,            \tag{3.1}
\]

and the colouring `psi` of `G-{e,f}`.  If outcome 1 is obtained from an
endblock lobe `X_B`, let `T=N_G(X_B)`.  The restrictions of `psi` to the two
closed sides agree literally on the exact seven-set `T`.  Each of `e,f`
has one of only three placements relative to this separation:

1. its `R`-endpoint belongs to `X_B`, so the edge crosses `X_B-T` and is
   failed only on the `X_B`-side;
2. its `R`-endpoint lies outside `X_B`, and the edge is not in case 3, so
   both endpoints lie on the opposite closed side; or
3. its `R`-endpoint is `w` and its boundary endpoint belongs to `T`, so it
   is a literal boundary edge.

Consequently outcome 1 carries an exact common double-deletion trace.  It
is a proper boundary colouring except in the explicitly identified
boundary-edge placement.  This conclusion is label-preserving for the two
direct-entry edges, but it does not assert that their individual repairs
induce the old demand partition.

## 4. Trust boundary

The theorem proves a host-level reduction for the entire all-tight
shore-filling Gallai branch with at most four boundary colours.  A branching
block tree cannot survive: an endblock either gives a strict exact-seven
side or would create a third disjoint boundary-full connected subgraph.

The two surviving geometries are unbounded but standard: one complete or
odd-cycle block, or a chain of Gallai blocks between two boundary-full end
lobes.  The theorem does not synchronize a proper colouring of both
original closed shores, and the common trace on the descended boundary may
still contain one of the deleted edges as a monochromatic boundary edge.
