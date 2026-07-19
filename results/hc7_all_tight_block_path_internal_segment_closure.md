# Closure of every all-tight multiblock exact-seven shore

**Status:** written theorem; separate internal audit GREEN at the revision
recorded in the adjacent audit.  This note
combines the all-tight Gallai-tree reduction with the full-residual
defect-two carrier theorem.  It eliminates every multiblock shore-filling
core.  The one-block `K_4` and `K_5` cases remain separate.

## 1. Setting

Let

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}B,
 \qquad |S|=7,
 \qquad E_G(A,B)=\varnothing,
\tag{1.1}
\]

be an actual separation in a seven-connected, seven-chromatic,
`K_7`-minor-free graph every proper minor of which is six-colourable.
Assume:

1. `G[S]` belongs to the frozen 129-boundary residual of the adaptive
   exact-seven `(1,2)` reduction;
2. `B` contains a connected subgraph adjacent to every vertex of `S`;
3. `G[A]` is a Gallai tree whose block--cutvertex tree is a path;
4. the two endblock lobes are adjacent to every vertex of `S`;
5. `A` contains no three pairwise disjoint boundary-full connected
   subgraphs; and
6. for a fixed six-colour boundary assignment `psi`, the lists

   \[
      \mathcal L(v)=[6]-
       \{\psi(s):s\in N_G(v)\cap S\}
   \]

   satisfy `d_{G[A]}(v)=|mathcal L(v)|` for every `v in A`, while every
   vertex of `A` has degree at least nine in `G`.

List the blocks of `G[A]` in their path order as

\[
                         D_1,D_2,\ldots,D_r,            \tag{1.2}
\]

where consecutive blocks meet in the cutvertex
`w_i in V(D_i) cap V(D_{i+1})`.

## 2. Closure theorem

### Theorem 2.1 (all multiblock cores close)

If `r>=2`, then `G` is six-colourable or contains a `K_7` minor.  Hence no
such multiblock core occurs under the hypotheses of Section 1.

#### Proof

Put

\[
 P_1=V(D_1)-\{w_1\},
 \qquad
 P_2=V(D_r)-\{w_{r-1}\}.                              \tag{2.1}
\]

Each `P_i` is nonempty and connected.  A bridge endblock leaves its leaf
vertex; deleting one vertex from a nontrivial two-connected block leaves a
connected graph.  The two sets are disjoint and are boundary-full by
hypothesis 4.

Suppose first that `r>=4`.  Let

\[
 T=\left(\bigcup_{i=2}^{r-1}V(D_i)\right)
          -\{w_1,w_{r-1}\}.                            \tag{2.2}
\]

The set `T` is nonempty and connected.  Indeed, `D_2-w_1` and
`D_{r-1}-w_{r-1}` are connected and contain the next articulation toward
the interior, and all intermediate blocks meet consecutively.  The linear
block order also gives

\[
                         N_{G[A]}(T)\subseteq
                         \{w_1,w_{r-1}\}.              \tag{2.3}
\]

Now suppose `r=3` and `D_2` is not a bridge.  Choose any component `T` of

\[
                         G[D_2]-\{w_1,w_2\}.            \tag{2.4}
\]

It is nonempty because a nonbridge block has at least three vertices.  It
is connected by choice, is disjoint from `P_1,P_2`, and satisfies

\[
                         N_{G[A]}(T)\subseteq\{w_1,w_2\}.
\tag{2.5}
\]

In either case all neighbours of `T` outside `T` lie in `S` and at most two
literal vertices of `A`.  Its full neighbourhood separates `T` from the
nonempty opposite shore `B`.  Seven-connectivity therefore gives

\[
                         |N_S(T)|\ge5.                 \tag{2.6}
\]

Thus `P_1,P_2,T` satisfy the full-residual defect-two carrier theorem.  The
boundary-full connected subgraph in `B` supplies its opposite-side
operation, and the theorem returns matching exact boundary partitions from
the two closed shores.  They glue to a six-colouring of `G`.

It remains to treat the two short path shapes.  For `v in A`, write

\[
 c(v)=|\{\psi(s):s\in N_S(v)\}|,
 \qquad b(v)=|N_S(v)|.
\tag{2.7}
\]

All-tightness gives

\[
                         d_{G[A]}(v)=6-c(v).           \tag{2.8}
\]

### Case 1: two blocks

Let `r=2`, with common cutvertex `w`.  If `b(w)>=5`, use `T={w}` with
the two end lobes in the full-residual carrier theorem.  We may therefore
assume `b(w)<=4`.

Since `d_G(w)>=9`, equations (2.7)--(2.8) give
`d_{G[A]}(w)>=5`.  Moreover `b(w)>0`: otherwise (2.8) would give
`d_G(w)=d_{G[A]}(w)=6`, contradicting `d_G(w)>=9`.  Thus `c(w)>=1` and
`d_{G[A]}(w)<=5`.  Consequently

\[
                         d_{G[A]}(w)=5.                \tag{2.9}
\]

The two positive contributions to this degree from `D_1,D_2` sum to five,
so one is at most two.  A degree-one contribution means that the
corresponding endblock is a bridge.  Its leaf has at most one neighbour in
`A` and at most seven in `S`, hence degree at most eight, contrary to
hypothesis 6.

A degree-two contribution means that the corresponding Gallai block is a
triangle or an odd cycle.  Every noncut vertex in that endblock has exactly
two neighbours in `A`; degree at least nine forces it to be adjacent to all
seven vertices of `S`.  The endblock lobe contains at least two such
vertices, giving two disjoint boundary-full singleton subgraphs.  The
opposite endblock lobe is a third disjoint boundary-full connected
subgraph, contrary to hypothesis 5.  Thus `r=2` is impossible.

### Case 2: three blocks with a bridge in the middle

Let `r=3` and suppose `D_2=w_1w_2` is a bridge.  Put `T={w_1,w_2}`.
If `|N_S(T)|>=5`, the full-residual carrier theorem again six-colours `G`.
Assume instead that `|N_S(T)|<=4`.

For `i=1,2`, the same calculation as above gives

\[
 d_{G[A]}(w_i)=5,
 \qquad b(w_i)=4.                                     \tag{2.10}
\]

One incident edge at `w_i` is the middle bridge, so its degree contribution
inside the corresponding endblock is four.  A Gallai block having a vertex
of degree four is the clique `K_5`; odd-cycle blocks have degree two.
Hence

\[
                         D_1\cong D_3\cong K_5.        \tag{2.11}
\]

Every noncut vertex `x in D_1-{w_1}` has four neighbours in `A`, and hence
at least five neighbours in `S`.  The family

\[
                         \{N_S(v):v\in V(D_1)\}        \tag{2.12}
\]

has a system of distinct representatives.  Indeed, the set for `w_1` has
order four, every other set has order at least five, and therefore every
subfamily of at most five sets has union at least its order.  Choose
distinct representatives `s_v in N_S(v)` for all `v in D_1`.

The five sets

\[
                         \{v,s_v\}\qquad(v\in D_1)    \tag{2.13}
\]

are connected and pairwise adjacent through the `K_5`.  Let `p,q` be the
two unused boundary vertices.  The end lobe
`P_2=D_3-{w_2}` is connected and boundary-full, as is a fixed connected
subgraph `R subseteq B` from hypothesis 2.  The seven branch sets

\[
 \{\{v,s_v\}:v\in D_1\},
 \qquad P_2\cup\{p\},
 \qquad R\cup\{q\}                                    \tag{2.14}
\]

form a `K_7`-minor model.  The last two bags are adjacent because each is
boundary-full and contains one of `p,q`; each is adjacent to every bag in
(2.13) through the representative `s_v`; and the first five bags are
pairwise adjacent through `D_1`.

All cases with `r>=2` are closed. \(\square\)

## 3. Application to the shore-filling list-critical core

In the all-tight branch of the audited shore-filling density theorem,
unless an endblock lobe already exposes an actual order-seven separation,
the block--cutvertex tree is a path with two boundary-full end lobes.  If
the path lies in the surviving adaptive `(1,2)` cell, Theorem 2.1 therefore
eliminates every multiblock core.  The only all-tight shore-filling cores
not covered here are the one-block `K_4` and `K_5` cases.  Their order is
already bounded; this theorem does not claim they are realizable.

## 4. Trust boundary

The proof does not close an order-seven separator merely because it exists;
the full-residual carrier theorem supplies the common complete equality
partition in the cases covered here.  It does not treat positive total
list-degree excess or the one-block `K_4,K_5` cases.

## 5. Dependencies

- [shore-filling density and Gallai-tree structure](../results/hc7_special_shore_filling_density.md)
- [adaptive `(1,2)` residual classification](../results/hc7_exact7_adaptive_12_boundary_closure.md)
- [exact-seven full-subgraph packing](../results/hc7_exact_seven_packet_packing.md)
- [full-residual defect-two carrier theorem](hc7_exact7_all_residual_defect2_carrier.md)
