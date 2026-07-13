# Exact-seven rooted-triangle portal-rank funnel

## 1. Scope

Assume the audited exact-seven `(1,3)` setting

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

where there are no `LR` edges, `G` is seven-connected, `R` contains
three pairwise disjoint connected `S`-full packets, and `G[L]` is
three-connected.  Let `T={t_1,t_2,t_3}` be a three-cut of `G[L]`, and
let `C,D` be the two components of `G[L]-T`.

This note proves that every nontrivial lobe contains a literal
`T`-rooted triangle minor.  It then identifies the precise extra condition
which turns that triangle into the four labelled carriers needed for a
literal `K_7`.

## 2. Rooted triangles

We use the following elementary rooted-triangle criterion.

### Lemma 2.1 (rooted-triangle obstruction)

Let `H` be connected and let `r_1,r_2,r_3` be distinct vertices.  Exactly
one of the following alternatives holds.

1. `H` has three pairwise disjoint connected, pairwise adjacent branch
   sets `B_1,B_2,B_3` with `r_i in B_i`.
2. There is a vertex `x` such that every component of `H-x` contains at
   most one member of `{r_1,r_2,r_3}-{x}`.

#### Proof

The alternatives are incompatible: if the second holds, every branch set
not containing `x` lies in one component of `H-x`; three pairwise adjacent
rooted bags cannot place the roots in the required distinct components.

For existence, use the block--cutvertex tree of `H`, regarding a bridge as
a degenerate block.  Mark the location of each root: the cutvertex node if
the root is a cutvertex, and otherwise its unique block node.  Let `Q` be
the minimal subtree joining the three marked locations, with coincident
marks allowed.

If the median of the three marks is a cutvertex node `x`, the components
of `H-x` correspond to the incident branches of the block--cutvertex tree.
Minimality of `Q` shows that no such component contains two roots not equal
to `x`, giving alternative 2.

Otherwise the median is a genuine two-connected block `B`.  The three
root-to-`B` branches enter `B` at three distinct vertices (a root already
in `B` is its own entry); equality of two entries would make that
cutvertex, rather than `B`, the median.  A two-connected graph has a
triangle minor rooted at any three prescribed distinct vertices: take a
cycle through two of them and a two-fan from the third to the cycle, and
partition the resulting cycle-plus-ear at the three roots.  Attach to the
three bags the mutually disjoint root-to-entry branches represented by
the three arms of `Q`.  This gives alternative 1.  A bridge block cannot
be the median of three distinct arms, so there is no omitted case.
`square`

### Lemma 2.2 (every nontrivial lobe has a gate-rooted triangle)

If `K` is either `C` or `D` and `|K|>=2`, then `G[K union T]` has a
`T`-rooted `K_3` model.

#### Proof

First, every lobe meets every literal vertex of `T`.  If `K` missed
`t in T`, the other two vertices of `T` would separate `K` from the other
lobe, contrary to three-connectivity of `G[L]`.

Put `H=G[K union T]` and suppose that `H` has no `T`-rooted triangle.
By Lemma 2.1 there is a vertex `x` such that every component of `H-x`
contains at most one member of `T-{x}`.

The vertex `x` cannot lie in `T`: the connected set `K`, together with
its neighbours at the other two gate vertices, lies in one component of
`H-x` containing both of those gate vertices.

Thus `x in K`.  Since `|K|>=2`, choose a component `A` of `H-x` which
contains a vertex of `K`.  It contains at most one gate vertex; call that
vertex `t` if it exists.  Every exit in `G[L]` from `A cap K` lies through
`x` or `t`: there is no edge between the two lobes, and an edge to any
other gate vertex would put that gate vertex in `A`.  Hence deleting
`{x,t}` separates the nonempty set `A cap K` from the other lobe.  If no
such `t` exists, deleting `x` alone does so.  Either conclusion contradicts
three-connectivity of `G[L]`. `square`

The size hypothesis is exact: a singleton lobe adjacent to all three gate
vertices induces a three-leaf star with `T` and need not contain a
`T`-rooted triangle.

### Lemma 2.3 (crossed-arm necessity)

Let `K` be a lobe, let `z in K`, and let `A` be a component of `K-z`.
Then `A` has neighbours at at least two vertices of `T`.

#### Proof

Otherwise every exit from `A` in `G[L]` lies in `{z}` together with at
most one gate vertex.  Deleting those at most two vertices separates `A`
from the other lobe, contradicting three-connectivity. `square`

This is the valid content exposed by the failed clean-tripod attempt:
clean one-terminal arms are impossible, so crossed gate incidence is
mandatory.

## 3. Portal rank is the exact remaining defect

For a `T`-rooted triangle model

\[
                    \mathcal M=(B_1,B_2,B_3),
                    \qquad t_i\in B_i,
\]

inside `G[K union T]`, define its **literal portal rank** to be the maximum
size of a matching in the bipartite incidence graph between the three bags
`B_i` and the seven literal boundary vertices `S`, where `sB_i` is an
incidence precisely when `s` has a literal neighbour in `B_i`.

### Theorem 3.1 (rank-three triangle closure)

If either lobe has a `T`-rooted triangle model of literal portal rank three,
then `G` contains a literal `K_7` minor.

#### Proof

Let `K` contain the triangle model and let `J` be the other lobe.  Choose
distinct representatives `s_i in S`, one adjacent to each `B_i`.  The
three bags `B_i` are disjoint, connected and pairwise adjacent.  Also `J`
is connected and adjacent to every `B_i`, because `J` has a neighbour at
each literal root `t_i in B_i`.

Seven-connectivity gives `|N_S(J)|>=4`: deleting
`T union N_S(J)` separates `J` from `K` and from the opposite open shore.
Therefore choose

\[
                       s_0\in N_S(J)-\{s_1,s_2,s_3\}.
\]

Enlarge `J` by `s_0` and each `B_i` by `s_i`.  These are four disjoint
connected pairwise adjacent bags carrying four distinct literal vertices
of `S`.  Anchor the three disjoint `S`-full packets in `R` at the remaining
three vertices of `S`.  Fullness supplies every packet--packet and
packet--carrier adjacency, so the resulting seven bags form a literal
`K_7` model. `square`

### Corollary 3.2 (exact funnel)

In a surviving exact-seven `(1,3)` two-lobe gate cell, every `T`-rooted
triangle model in every nontrivial lobe has literal portal rank at most two.

Since the established order bound gives `|L|>=8`, at least one lobe has
order at least three and hence, by Lemma 2.2, has such a rooted triangle.
Thus the live obstruction is not absence of a gate-rooted triangle.  It is
the uniform concentration of the seven literal boundary labels into at
most two bags of every gate-rooted triangle model.

## 4. Named next exchange

Choose, over both lobes and all `T`-rooted triangle models, a model of
maximum literal portal rank.  Corollary 3.2 says its rank is at most two.
On the other hand,
the audited forbidden-label lobe matching lemma gives three distinct portal
vertices with three distinct labels in every lobe of order at least three.

The next proof link is therefore the **maximal portal-rank triangle
exchange**:

* reroute or split a multiply hit triangle bag to increase portal rank; or
* certify a literal separator/state on the actual seven-boundary; or
* show that every such certificate is governed by one fixed pair of
  vertices, yielding the permitted two-vertex endgame.

This is a label-preserving branch-set surgery problem.  Lemma 2.2 alone
does not align the three distinct portal vertices with the three rooted
bags, and this note makes no such inference.
