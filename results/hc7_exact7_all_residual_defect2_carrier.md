# Defect-two connected-subgraph reflection on every residual seven-boundary

**Status:** written computer-assisted finite theorem; separate internal audit
GREEN at the revision recorded in the adjacent audit.  This note extends
the previously audited ten-boundary calculation to every graph in the
frozen 129-boundary residual.  It is conditional on that audited residual
classification and does not prove `HC_7`.

## 1. Boundary statement

Let `S` be a literal seven-set and let `H` be one of the 129 unlabelled
boundary graphs left by the audited adaptive `(1,2)` exact-seven reduction.
For a proper partition `Pi` of `S` into independent blocks, put

\[
 d_H(\Pi)=|\Pi|-\omega
 \bigl(H[\operatorname{sing}(\Pi)]\bigr),
\tag{1.1}
\]

where `sing(Pi)` is the set of vertices occurring as singleton blocks.
Choose a maximum clique `Q` of `H[sing(Pi)]`; the blocks not represented by
`Q` will be called the **unrepresented blocks** of `Pi` relative to `Q`.

### Theorem 1.1 (uniform defect-two boundary certificate)

For every set `D subseteq S` with `|D|<=2`, there is a non-singleton
inclusion-maximal independent set `I=I(H,D)` such that every proper
partition `Pi` of `S` into at most six independent blocks having `I` as an
exact block satisfies one of the following.

1. `d_H(Pi)<=2`.
2. `d_H(Pi)=3`, and for some maximum singleton clique `Q` there is an
   unrepresented block `B` such that

   \[
        B\cap D=\varnothing,
        \qquad
        N_H(q)\cap B\ne\varnothing
        \quad(q\in Q\cap D).
   \tag{1.2}
   \]

Thus no returned partition has demand greater than three, and every
demand-three partition has a block which can be represented by a connected
subgraph adjacent to all vertices of `S-D`.

### Proof and finite certificate

The deterministic verifier
[`hc7_exact7_all_residual_defect2_probe.py`](hc7_exact7_all_residual_defect2_probe.py)
performs the following exhaustive calculation.

1. It takes one representative of every unlabelled graph on seven vertices
   from `networkx.graph_atlas_g()`, retains the `K_4`-free graphs, and applies
   exactly the two frozen residual tests: absence of a robust independent
   contraction block and absence of a two-anchor `K_4` lift.  Exactly 129
   boundary graphs remain.
2. For each graph it enumerates the empty defect, the seven singleton
   defects and the 21 two-vertex defects, giving `129*29=3741` cells.
3. It enumerates every non-singleton inclusion-maximal independent set `I`
   and every partition of `S` into at most six independent blocks containing
   `I` as an exact block.
4. For each returned partition it computes (1.1).  Demand at most two is
   accepted directly.  At demand three it enumerates every maximum clique
   among the singleton blocks and checks (1.2) for each of the three
   unrepresented blocks.  Demand above three is rejected.
5. It accepts a cell only when one choice of `I`, made before the returned
   partition is known, accepts every such partition.

The verifier asserts all census sizes and terminates with

```text
boundaries=129
cells=3741
witnesses=3741
failures=0
CERTIFIED full-residual defect-two carrier reflection
```

This proves the finite statement. \(\square\)

## 2. Host-graph lift

Consider an actual separation

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}B,
 \qquad |S|=7,
 \qquad E_G(A,B)=\varnothing,
\tag{2.1}
\]

in a graph every proper minor of which is six-colourable.  A connected
subgraph of an open shore is **boundary-full** if it has a neighbour at
every literal vertex of `S`.

### Theorem 2.1 (two full subgraphs and one defect-two subgraph)

Assume `G[S]` belongs to the frozen 129-boundary residual.  Suppose `A`
contains pairwise vertex-disjoint connected subgraphs `P_1,P_2,T`, where
`P_1,P_2` are boundary-full and

\[
                     |S-N_G(T)|\le2.                  \tag{2.2}
\]

Suppose `B` contains a boundary-full connected subgraph `R`.  Then `G` is
six-colourable.

#### Proof

Put `D=S-N_G(T)` and choose `I=I(G[S],D)` from Theorem 1.1.  Contract a
spanning tree of the connected set `R union I`.  This is a proper minor.
In any six-colouring of it, expand the literal independent set `I` with the
colour of the contracted image and restrict to `G[A union S]`.  Fullness of
`R` makes `I` an exact boundary colour class: every vertex of `S-I` is
adjacent to the contracted image.  Let `Pi` be the resulting exact equality
partition of `S`.

Choose the maximum singleton clique `Q` supplied by Theorem 1.1.  If
`d_{G[S]}(Pi)<=2`, assign `P_1,P_2` to the at most two unrepresented blocks.
If the demand is three, assign `T` to the block `B_0` supplied by (1.2) and
assign `P_1,P_2` to the other two unrepresented blocks.

In the latter case, `T union B_0` is connected because `B_0` avoids `D` and
`T` contacts every vertex outside `D`.  It is adjacent to every singleton
`q in Q`: direct contact works for `q notin D`, while (1.2) supplies a
boundary edge from `q` to `B_0` for `q in D`.  The two boundary-full
subgraphs supply all other block-to-block and block-to-singleton
adjacencies.  The same conclusion is immediate in the demand-at-most-two
case.

The resulting connected subgraphs form a partition-specific carrier system
for `Pi` on the `A` shore.  Contracting them in a proper minor therefore
returns a six-colouring of `G[B union S]` with the same exact equality
partition `Pi`.  Permute colour names on one shore and glue the two
colourings across `S`.  Hence `G` is six-colourable. \(\square\)

## 3. Exact scope

The choice of `I` depends on both the boundary graph and the literal defect
set `D`, but not on the subsequently returned proper-minor colouring.  This
is the permitted adaptive order in the exact-seven reduction.

The theorem does not assert that an arbitrary `(1,2)` shore contains the
third connected subgraph `T`.  It only completes the colouring once a
subgraph missing at most two boundary vertices is found disjointly from the
two boundary-full subgraphs.  The geometric production of `T` is a separate
host-level obligation.

## 4. Dependencies

- [adaptive `(1,2)` residual classification](../results/hc7_exact7_adaptive_12_boundary_closure.md)
- [partition-specific carrier reflection](../results/hc7_exact7_selected_response_preservation.md)
- [ten-boundary defect-two predecessor](../results/hc7_exact7_connected_rich_cutvertex_exchange.md)
