# Hall criterion for reflecting a boundary colouring through mixed connected supports

**Status:** written proof; separate internal audit GREEN in
[`hc7_transported_partition_hall_reflection_audit.md`](hc7_transported_partition_hall_reflection_audit.md).
This theorem
gives an exact matching criterion for using a mixture of boundary-full and
labelled connected subgraphs to reproduce one selected boundary partition
on the opposite shore.  It does not produce the connected subgraphs and
does not prove `HC_7`.

## 1. Setting and duties

Let

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}B,
 \qquad E_G(A,B)=\varnothing,
 \qquad A,B\ne\varnothing .                            \tag{1.1}
\]

Assume every proper minor of `G` is `q`-colourable.  Let `Sigma` be a
partition of `S` into at most `q` independent blocks, induced by a proper
`q`-colouring of `G[A union S]`.

Choose a maximum clique `U` in the graph induced by the singleton blocks of
`Sigma`.  Regard its vertices as the blocks represented by `U`, and list all
remaining blocks as

\[
                         C_1,\ldots,C_d .               \tag{1.2}
\]

Thus

\[
 d=|\Sigma|-|U|.
\]

Assume `d>=1`.

For a block `C_i`, define its literal duty relative to `U` by

\[
 D_U(C_i)=C_i\mathbin{\cup}
   \{u\in U:E_G(u,C_i)=\varnothing\}.                  \tag{1.3}
\]

Suppose `A` contains pairwise vertex-disjoint connected subgraphs

\[
 P_1,\ldots,P_r,\quad W_1,\ldots,W_t,                  \tag{1.4}
\]

where every `P_j` is adjacent to every literal vertex of `S`, and the
subgraphs `W_1,\ldots,W_t` are pairwise adjacent.  No adjacency between two
members of the `P` family, or between a `P` and a `W`, is assumed.

Form a bipartite incidence graph with right side
`{C_1,...,C_d}`.  Its left side has

* one universal vertex for each `P_j`; and
* one vertex for each `W_k`, adjacent to `C_i` exactly when `W_k` has a
  neighbour at every literal vertex of `D_U(C_i)`.

## 2. Exact matching criterion

### Theorem 2.1 (transported-partition Hall reflection)

If the incidence graph has a matching saturating
`{C_1,...,C_d}`, then `G[B union S]` has a proper `q`-colouring inducing
exactly `Sigma` on `S`.  Consequently `G` is `q`-colourable.

Moreover, among carrier systems in which the connected open-side support
assigned to each block `C_i` is exactly one distinct member of the
displayed family (1.4), the saturating matching condition is necessary as
well as sufficient.  Hence failure is witnessed
exactly by a nonempty block family `X` satisfying

\[
       |N_{\{W_1,\ldots,W_t\}}(X)|+r<|X|.             \tag{2.1}
\]

#### Proof

Let a saturating matching assign a connected subgraph `Y_i` from (1.4) to
each `C_i`.  Put

\[
                           Z_i=V(Y_i)\cup C_i.          \tag{2.2}
\]

Each `Z_i` is connected.  If `Y_i=P_j`, every boundary vertex of `C_i`
has a neighbour in `Y_i`.  If `Y_i=W_k`, the matching edge says the same
thing because `C_i subseteq D_U(C_i)`.

The sets `Z_i` are pairwise adjacent.  Two sets assigned members of the
`W` family are adjacent by hypothesis.  If at least one, say `Y_i`, is
boundary-full, it has a neighbour at every vertex of the nonempty block
`C_j`, and therefore `Z_i` is adjacent to `Z_j`.

Every `Z_i` is adjacent to every vertex `u in U`.  This is immediate for a
boundary-full assigned subgraph.  For `Y_i=W_k`, either a boundary edge
joins `u` to `C_i`, or `u` belongs to `D_U(C_i)` and the matching edge
supplies a neighbour of `u` in `W_k`.

Contract a spanning tree of every `Z_i`.  At least one edge from `A` to
each nonempty block is contracted, so this is a proper minor.  The images
of `Z_1,...,Z_d`, together with the singleton vertices of `U`, form a
clique with one vertex for every block of `Sigma`.  A proper `q`-colouring
of the minor therefore assigns distinct colours to these images.  Pull the
colour of the image of `Z_i` back to every literal vertex of `C_i`, and
keep the minor colouring on `B` and `U`.  This gives a proper colouring of
`G[B union S]` whose equality partition on `S` is exactly `Sigma`.

Permute the colour names of the original colouring of `G[A union S]` so
that the two colourings agree on every block, and glue them across `S`.
This proves sufficiency.

For necessity in the stated subordinate class, a support assigned to a
block must contain a neighbour of every vertex of that independent block,
or its union with the block is disconnected.  If the support is `W_k`, it
must additionally meet every `u in U` which has no boundary edge to the
block.  Thus `W_k` is eligible exactly at the incidence edges defined
above; a boundary-full support is eligible everywhere.  Pairwise
disjointness requires distinct supports.  A subordinate carrier system is
therefore exactly a saturating matching.  Hall's theorem gives (2.1).
\(\square\)

## 3. Two full subgraphs and one additional connected subgraph

### Corollary 3.1

Suppose (1.4) consists of `r` boundary-full connected subgraphs and one
additional connected subgraph `W`, all pairwise disjoint.  Then:

1. if `d<=r`, the partition reflects without using `W`;
2. if `d=r+1`, the partition reflects exactly when, for some maximum
   singleton clique `U`, the subgraph `W` has a neighbour at every vertex
   of `D_U(C_i)` for at least one remaining block `C_i`; and
3. if `d>r+1`, these displayed supports alone cannot saturate the blocks.

In particular, with two boundary-full subgraphs, every partition of demand
at most two reflects, while a demand-three partition reflects precisely
when the additional connected subgraph meets one complete duty set.

#### Proof

The `r` universal left vertices match any `r` blocks.  When there is one
more block, the remaining left vertex must be matched to an incidence edge
of `W`.  With more than `r+1` blocks there are too few displayed supports.
Apply Theorem 2.1. \(\square\)

## 4. The seven-vertex high-demand shapes

Assume now `|S|=7` and `Sigma` has at most six blocks.  Write a block-size
shape in nonincreasing order.  The condition `d>=4` holds exactly in the
following cases:

1. shape `3+1+1+1+1`, with the four singleton vertices independent;
2. shape `2+2+1+1+1`, with the three singleton vertices independent; or
3. shape `2+1+1+1+1+1`, with the graph induced by the five singleton
   vertices triangle-free.  Here `d=5` when those five vertices are
   independent and `d=4` when their clique number is two.

For reference, `d=3` occurs exactly for:

* `3+2+2`;
* `2+2+2+1`;
* `3+2+1+1` with its singleton pair nonadjacent;
* `4+1+1+1` with its singleton triple independent;
* either five-block shape above with singleton clique number two; or
* `2+1+1+1+1+1` with singleton clique number three.

#### Proof

If `k=|Sigma|` and the singleton-block graph has clique number `omega`,
then `d=k-omega`.  The integer partitions of seven into at most six parts
are finite.  For `k=5`, the only shapes are `3+1+1+1+1` and
`2+2+1+1+1`; demand at least four is equivalent to `omega=1`.  For `k=6`
the only shape is `2+1+1+1+1+1`; demand at least four is equivalent to
`omega<=2`.  Four or fewer blocks cannot have demand at least four because
at least one singleton is present when four blocks partition seven
vertices.  The same calculation with `k-omega=3` gives the displayed
demand-three list. \(\square\)

## 5. Trust boundary

The theorem is an exact criterion only for carrier systems subordinate to
the listed connected supports.  A different connected support, a union of
several listed subgraphs, or a branch-set rerouting may still reflect a
partition after the incidence graph fails Hall's condition.

The theorem does not make a transported boundary assignment legal on an
original closed shore.  That legality must come from an actual proper
minor colouring with every failed edge repaired.  Nor does it create the
boundary-full subgraphs, meet an uncovered duty set, preserve five model
labels automatically, or prove `HC_7`.
