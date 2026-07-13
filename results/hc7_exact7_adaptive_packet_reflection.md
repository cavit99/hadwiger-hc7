# Adaptive exact-seven packet reflection

## 1. The theorem

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

with no edge between `L` and `R`.  An **`S`-full packet** is a nonempty
connected subgraph, disjoint from `S`, which has a neighbour at every
literal vertex of `S`.

### Theorem 1.1 (adaptive `(1,3)` packet reflection)

Assume that

1. every proper minor of `G` is six-colourable;
2. `L` contains an `S`-full packet `Q`; and
3. `R` contains three pairwise vertex-disjoint `S`-full packets
   `P_1,P_2,P_3`.

Then `G` has a literal `K_7` minor or `G` is six-colourable.

Consequently, a strongly seven-contraction-critical, `K_7`-minor-free
graph has no actual order-seven separation with packet vector `(1,3)`.

The proof is adaptive.  The packet in `L` first forces one large exact
colour class on the literal boundary.  Only after its proper-minor
colouring returns the *whole* boundary partition do the three packets in
`R` reproduce that exact partition.  No lobe, gate, portal order, or
palette-to-model identification is used.

## 2. Packet demand

Put `H=G[S]`.  If `Pi` is a partition of `S` into independent blocks,
write

\[
 \operatorname{sing}(\Pi)
   =\{s\in S:\{s\}\in\Pi\}
\]

and define

\[
 d_H(\Pi)=|\Pi|-\omega\bigl(H[\operatorname{sing}(\Pi)]\bigr). \tag{2.1}
\]

The clique of singleton blocks in (2.1) can remain literal.  Every other
block is attached to and contracted with a separate full packet.

### Lemma 2.1 (exact packet reflection)

Suppose one open shore contains `q` pairwise disjoint `S`-full packets.
Let `Pi` be a partition of `S` into independent blocks with

\[
                            d_H(\Pi)\le q.                 \tag{2.2}
\]

Then one of the following holds.

1. `G` contains a literal `K_7` minor; or
2. contractions supported in that closed shore produce a proper minor
   whose six-colouring pulls back to a proper colouring of the opposite
   closed shore with equality partition on `S` exactly `Pi`.

#### Proof

Choose a maximum clique

\[
 U\subseteq\operatorname{sing}(\Pi)
\]

in `H[sing(Pi)]`.  Let `B_1,...,B_m` be all blocks of `Pi` other than
the singleton blocks represented by `U`.  By (2.1)--(2.2),

\[
                         m=|\Pi|-|U|\le q.                \tag{2.3}
\]

Choose `m` of the disjoint full packets and put

\[
                         Z_i=V(P_i)\cup B_i
                              \qquad(1\le i\le m).         \tag{2.4}
\]

Every `Z_i` is connected: the packet is connected and every vertex of
`B_i` has a literal neighbour in it.  The sets are pairwise disjoint.
Contract a spanning tree of each `G[Z_i]`, and call the resulting vertex
`z_i`.

If `m=0`, every boundary block is a singleton and `U=S` is a clique.
Thus `H=K_7`, which is outcome 1.  Hence assume `m>=1`.  At least one
literal packet--boundary edge is contracted, so the resulting minor `M`
is proper.

The vertices

\[
                           z_1,\ldots,z_m,\quad U          \tag{2.5}
\]

form a literal clique in `M`.  Indeed, `P_i` has an edge to every
literal vertex of `B_j` and to every `u in U`; vertices of `U` form a
clique by choice.  The vertices in (2.5) correspond one-to-one with all
blocks of `Pi`.

If `|Pi|=7`, the original sets `Z_1,...,Z_m` together with the
singleton sets in `U` are seven disjoint connected pairwise adjacent
literal branch sets in `G`; this is outcome 1.  Hence in outcome 2 one
has `|Pi|<=6`.

Let `psi` be a six-colouring of the proper minor `M`.  Keep `psi` on the
untouched opposite open shore and on `U`; for `s in B_i`, assign

\[
                             \varphi(s)=\psi(z_i).         \tag{2.6}
\]

This is a proper colouring of the opposite closed shore.  There is no
edge inside `B_i` because each block is independent.  Every edge from
`B_i` to an untouched vertex became an edge incident with `z_i`, and
edges between different blocks are safe because all block
representatives in (2.5) form a clique.  The same clique also forces
different blocks to receive different colours.  Therefore (2.6) induces
exactly `Pi`, not a coarsening of it, on the literal set `S`. `square`

The lemma never expands a packet on the side where it was contracted.
It pulls the colouring back only across independent boundary blocks to
the untouched opposite shore.

## 3. Four packets plus a boundary triangle

### Lemma 3.1 (triangle lift)

Under the hypotheses of Theorem 1.1, if `H` contains a triangle, then
`G` contains a literal `K_7` minor.

#### Proof

The packet `Q` in `L` and `P_1,P_2,P_3` in `R` are four pairwise
disjoint `S`-full packets; call them `W_0,...,W_3`.  Let

\[
 C=\{c_1,c_2,c_3\}
\]

be a literal boundary triangle and write

\[
 S-C=\{a_0,a_1,a_2,a_3\}.
\]

The seven bags

\[
 V(W_i)\cup\{a_i\}\quad(0\le i\le3),
 \qquad \{c_1\},\{c_2\},\{c_3\}                         \tag{3.1}
\]

are disjoint and connected.  Two packet bags are adjacent because either
packet contacts the other bag's literal anchor.  Every packet bag is
adjacent to every triangle singleton by fullness, and the three
singletons are pairwise adjacent in `H`.  Thus (3.1) is a literal
seven-bag clique model. `square`

Hence the rest of the proof may assume

\[
                         H\text{ is triangle-free}.       \tag{3.2}
\]

## 4. The thin packet forces one large exact block

Every triangle-free graph on seven vertices has independence number at
least three, by `R(3,3)=6`.  Choose an independent set `I` as follows:

\[
 |I|=4\quad\text{if }\alpha(H)\ge4;
 \qquad
 |I|=3=\alpha(H)\quad\text{otherwise}.                  \tag{4.1}
\]

Put

\[
                            Z=V(Q)\cup I.
\]

It is connected.  Contract a spanning tree of `G[Z]` to one vertex `z`,
obtaining a proper minor `M_L`; a literal packet--boundary edge is
contracted.  Take a six-colouring of `M_L` and pull it back only to
`G[R\cup S]` by assigning every member of `I` the colour of `z`.

The pullback is proper.  The set `I` is independent, and every edge from
`I` to the untouched closed shore became an edge at `z`.  Moreover `I`
is one **exact** colour class on `S`: for each `s in S-I`, fullness of
`Q` produces the edge `zs` in `M_L`, so `s` cannot receive the colour of
`z`.

Let `Pi` be the complete equality partition of `S` returned by this
colouring.  Thus

\[
                             I\in\Pi.                    \tag{4.2}
\]

No other block of `Pi` was prescribed.

## 5. Three packets reflect every returned partition

### Lemma 5.1 (seven-vertex demand bound)

For the partition `Pi` obtained in Section 4,

\[
                              d_H(\Pi)\le3.               \tag{5.1}
\]

#### Proof

First suppose `|I|=4`.  Since `I` is one block and only three boundary
vertices remain,

\[
                              |\Pi|\le4.
\]

If `|Pi|<=3`, the empty singleton clique already shows
`d_H(Pi)<=3`.  If `|Pi|=4`, all three vertices outside `I` are singleton
blocks; retaining any one singleton gives `d_H(Pi)<=4-1=3`.

Now suppose `|I|=3=alpha(H)`.  Then `|Pi|<=5`.  The assertion is
immediate when `|Pi|<=3`.  If `|Pi|=4`, the four vertices outside `I`
have block sizes `2,1,1`; hence a singleton block exists and
`d_H(Pi)<=4-1=3`.

Finally let `|Pi|=5`.  All four vertices of `S-I` are singleton blocks.
They are not independent, since `I` is a maximum independent set.
Choose an edge `uv` in `H[S-I]`.  The two singleton blocks `{u},{v}`
form a clique, so

\[
                              d_H(\Pi)\le5-2=3.
\]

This exhausts the cases. `square`

Apply Lemma 2.1 to the three packets in `R`.  The boundary is
triangle-free, so its exceptional `K_7` case cannot occur.  We obtain a
proper minor supported in `R\cup S` and a pulled-back proper colouring
`phi_L` of `G[L\cup S]` whose exact equality partition on `S` is `Pi`.

The first contraction in `L\cup S` produced a proper colouring `phi_R`
of `G[R\cup S]` with the same exact partition `Pi`.

## 6. Palette alignment and gluing

For every block `B in Pi`, let `a_B` and `b_B` be its colours under
`phi_R` and `phi_L`, respectively.  Exactness of the two partitions says
that both maps from blocks to colours are injective.  Hence the partial
map

\[
                              b_B\longmapsto a_B
                              \qquad(B\in\Pi)
\]

extends to a permutation of the six colours.  Apply it to `phi_L`.
The two shore colourings now agree at every literal vertex of `S`.
They glue because there is no `LR` edge, giving a proper six-colouring
of `G`.  This proves Theorem 1.1. `square`

## 7. Audit boundary

1. **Closed-shore support.**  The contractions may contain literal
   boundary vertices, but no vertex of the opposite open shore.  This is
   a legal minor operation.  No colouring is lifted through a contracted
   packet on its own side.
2. **Properness.**  Every contraction used in the theorem contains a
   literal packet--boundary edge, so it strictly reduces the vertex
   count.  The only `m=0` case in the abstract reflection lemma is the
   already terminal literal `H=K_7` case.
3. **Literal blocks.**  Only independent boundary blocks are expanded.
   Every edge from such a block to the untouched shore maps to an actual
   edge at its contracted representative.
4. **Exactness.**  The first large block is exact because its packet is
   full to `S-I`.  The reflected partition is exact because its block
   representatives form a literal clique in the proper minor.
5. **No label lift.**  Packet indices are assigned only after the full
   returned partition is known.  No palette colour is identified with a
   lobe, gate, near-clique bag, or portal class.
6. **No connectivity hidden.**  Once the four packets and the actual
   seven-set `S` are supplied, no connectivity assumption is used.
7. **Exact scope.**  The theorem concerns an actual seven-vertex
   boundary and the vector `(1,3)`.  It does not prove the analogous
   `(1,2)` statement and does not apply to a quotient boundary whose
   vertices stand for nonsingleton bags.

## 8. Consequence for the active proof spine

Every exact-seven `(1,3)` subcase is eliminated before any internal
thin-shore analysis.  In particular, the pure-Moser cells, rooted-
triangle portal ranks, block-chain states, and the genuinely
two-connected lobe residue are no longer live *inside an actual `(1,3)`
adhesion*.  They remain valid local lemmas and barriers, but are not
needed for this branch.

The exact-seven packet theorem therefore leaves only packet vectors
`(1,1)` and `(1,2)` up to orientation.  The natural next target is an
adaptive `(1,2)` reflection theorem; here the rich shore can reflect
only partitions of packet demand at most two, and the simple
independence-number argument above no longer guarantees that bound.
