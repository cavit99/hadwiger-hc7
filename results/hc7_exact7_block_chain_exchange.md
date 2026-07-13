# Exact-seven block-chain exchange

## 1. Scope

Retain the exact-seven `(1,3)` two-lobe setting

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

where `G` is seven-connected, there are no `LR` edges, `R` contains
three pairwise disjoint connected `S`-full packets, and `G[L]` is
three-connected.  Let `T={t_1,t_2,t_3}` be a three-cut of `G[L]`, and
let `J,K` be the two components of `G[L]-T`.

The nested cutvertex exchange already closes a vertex of `J` with three
deletion components.  This note closes the other possible branching node
of the block--cutvertex tree: a two-connected block with at least three
attachment cutvertices.  Together the two results force every surviving
lobe to be a block chain.

## 2. Branches at a two-connected block

Let `B` be a maximal nontrivial two-connected block of `J`.  Every
component `A` of `J-V(B)` has neighbours in exactly one vertex `z_A` of
`B`.  It has at least one such neighbour because `J` is connected.  It
cannot have two distinct neighbours in `B`, since a path through `A`
between two such neighbours would be a `B`-ear and would place its path
vertices in a larger two-connected block.

Call `A` a **`B`-branch**, and put

\[
                         U_A=N_T(A).
\]

As in the nested cutvertex theorem,

\[
                         |U_A|\ge2.                         \tag{2.1}
\]

Indeed, deleting `z_A` together with at most one gate vertex would
otherwise separate `A` from the opposite lobe `K` in `G[L]`.

Also

\[
                         |N_S(A)|\ge3.                      \tag{2.2}
\]

All exits from `A` lie in `{z_A} union U_A union N_S(A)`.  The opposite
lobe and opposite open shore survive its deletion, so seven-connectivity
gives

\[
              1+|U_A|+|N_S(A)|\ge7,
              \qquad |N_S(A)|\ge6-|U_A|\ge3.
\]

## 3. Three distinct attachment vertices close

### Theorem 3.1 (branching-block closure)

If a maximal nontrivial two-connected block `B` of either lobe contains
at least three cutvertices of that lobe, then `G` contains a literal
`K_7` minor.

#### Proof

Choose three distinct attachment cutvertices `z_1,z_2,z_3 in B` and a
`B`-branch `A_i` at each `z_i`.  More generally, while making this choice
we may choose any branch at each of three distinct attachment vertices.
Write `U_i=U_{A_i}`.

First suppose the three sets `U_1,U_2,U_3` have an SDR

\[
                        u_i\in U_i\quad(1\le i\le3).        \tag{3.1}

Since `B` is two-connected, it has a `K_3` model rooted at
`z_1,z_2,z_3`; let its bags be `Q_1,Q_2,Q_3`.  Define

\[
                        W_i=A_i\cup Q_i\cup\{u_i\}.         \tag{3.2}

The three sets are disjoint and connected: `A_i` meets `z_i in Q_i`
and has a neighbour at `u_i`.  They are pairwise adjacent through the
three rooted bags `Q_i`.  The opposite lobe `K` is adjacent to every
`W_i` through its contact with the literal gate vertex `u_i`.

It remains to handle failure of (3.1).  Three subsets of a three-set,
each of order at least two, fail Hall only when all three are the same
two-set.  If any `B`-branch at any attachment vertex has a different
gate set, choose it together with branches at two other attachment
vertices; their three gate sets have union `T` and hence have an SDR.
Thus the only case not already covered has

\[
                         U_A=\{u,v\}                        \tag{3.3}

for every `B`-branch `A`, where `w` is the third member of `T`.

The lobe `J` meets `w`.  By (3.3), no neighbour of `w` in `J` lies
outside `B`; hence choose `y in V(B)` with `yw in E(G)`.  Extend a
`z_1,z_2,z_3`-rooted `K_3` model in `B` to a spanning rooted partition

\[
                          V(B)=Q_1\dot\cup Q_2\dot\cup Q_3.
\]

After renaming, `y in Q_3`.  Put

\[
 W_1=A_1\cup Q_1\cup\{u\},\qquad
 W_2=A_2\cup Q_2\cup\{v\},\qquad
 W_3=A_3\cup Q_3\cup\{w\}.                              \tag{3.4}

Again the three sets are disjoint, connected, and pairwise adjacent;
the last set is connected through the literal edge `yw`.  The opposite
lobe `K` is adjacent to all three through `u,v,w`.

In either case, (2.2) and Hall's theorem give distinct representatives

\[
                s_i\in N_S(A_i)\quad(1\le i\le3).          \tag{3.5}

Since `|N_S(K)|>=4`, choose

\[
                      s_0\in N_S(K)-\{s_1,s_2,s_3\}.       \tag{3.6}

Thus `W_1,W_2,W_3,K`, enlarged by their four distinct representatives,
are four literal clique carriers.  Anchor the three disjoint `S`-full
packets in `R` at the remaining boundary vertices.  Packet fullness
supplies all remaining adjacencies, and the seven bags form a literal
`K_7` model. `square`

There is one choice detail in the Hall-failure paragraph.  If a branch
with a different gate set is attached at `z_i`, use that branch at
`z_i`; the assumption that `B` has at least three distinct attachment
cutvertices supplies the other two roots.  Therefore the three rooted
vertices remain distinct even when several branches are attached at one
cutvertex.

## 4. Uniform consequence

### Corollary 4.1 (lobe block-chain theorem)

In a `K_7`-minor-free survivor, the block--cutvertex tree of each lobe is
a path.

#### Proof

The nested cutvertex exchange says every cutvertex node has degree at
most two.  Theorem 3.1 says every nontrivial block node has degree at most
two.  A bridge block has only two endpoints and hence also has degree at
most two.  The block--cutvertex graph of a connected graph is a tree; a
tree of maximum degree at most two is a path. `square`

This is an unbounded structural conclusion, not a bound on lobe order.
All remaining portal monopolies in a lobe therefore have one linear block
order.  The next exchange may use that order directly: incompatible
proper-minor states must reverse somewhere along the chain, while a
compatible order gives the rural/two-vertex endgame.  The corollary does
not yet prove either alternative.
