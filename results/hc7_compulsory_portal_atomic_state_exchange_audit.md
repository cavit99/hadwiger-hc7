# Audit: atomic compulsory-portal state exchange

**Verdict:** GREEN at frozen source SHA-256
`81dd3068b6c473a3b80aef4e8e27253e9a9e66a90a136b69b4ee9453af660e5a`.
The only change from the source audited line by line was its status line.

The independent-trace construction, generalized block Kempe exchange, and
trace-compression-or-path theorem are correct.  The final blocking-path
implication is explicitly left open and was not used in this audit.

## 1. The width-two partition exists with `|I|>=2`

The connected width-two frontier is either a tree or a six-cycle with one
pendant vertex; in either case it is connected and bipartite.  Orient its
bipartition `I,J` so that `u in I`.  Both classes are nonempty.  Moreover
`|I|>=2`: a connected bipartite graph with a singleton bipartition class is
a star centred at that singleton.  Such a boundary cannot satisfy the
paired-state incidences.  If the star centre were `c`, no edge would join
two of the three paired blocks; if the centre were not `c`, then `c` would
have degree one and could not meet all three disjoint paired blocks.  Thus
neither bipartition class is a singleton.  Taking `K=emptyset` gives (1.1).

For the exceptional frontier `K_{1,3} dotunion K_3`, the paired-state
conditions force `c` to be the claw centre: it has at least three distinct
neighbours, while a triangle vertex has degree two and a claw leaf degree
one.  The claw leaves lie one in each paired block and the triangle
vertices are their partners.  Choose a triangle vertex `k ne u` for `K`
if `u` lies in the triangle, and any triangle vertex otherwise.  The
remaining triangle is an edge.  Its bipartition and the claw bipartition
may be oriented independently:

* if `u=c`, put `c` and one endpoint of the remaining triangle edge in
  `I`;
* if `u` is a claw leaf, put all three leaves in `I`; and
* if `u` is a surviving triangle vertex, put `u` together with `c` in
  `I`.

The complementary vertices form a nonempty independent `J`.  Hence in
every case `u in I`, `|I|>=2`, `I,J` are nonempty independent sets, and
`K` is an empty or singleton clique.  No unproved clique-OCT selection is
being assumed.

## 2. Lemma 2.1: legality and exactness of the trace

In the atomic bridge cell, `A` is connected and `S`-full, `R` is nonempty,
and `A` is anticomplete to `R`.  The unique `A-u` edge `zu` is allowed to
belong to the contracted tree; it causes no obstruction.

Every literal member of `I` has a neighbour in `A`, so `A union I` is
connected.  It contains an edge and its contraction strictly reduces the
graph; it also cannot contain all vertices because the rich shore contains
two packets.  Thus contracting a spanning tree of `A union I` is a proper
minor and every-proper-minor six-colourability applies.

When the minor colouring is restricted to `R union S`, only the boundary
vertices in `I` are expanded.  This is proper:

* `I` is independent;
* every original `I-R` or `I-(S-I)` edge became incident with the
  contracted representative `a`; and
* no vertex of the discarded interior `A` is expanded.

Finally, `A` has a neighbour at every literal member of `S-I`, so `a` is
adjacent to all of them in the minor.  None can receive the colour of `a`.
Consequently `I` is one exact equality block, including the bridge literal
`u`, and its colour is absent from all of `S-I`.

## 3. Lemma 3.1: generalized block Kempe exchange

Let the two exact boundary blocks `B,C` have colours `b,c`.  No other
boundary block contains either colour.

If one component of the `b,c`-induced graph meets both blocks, choose a
shortest path between the two boundary sets.  An internal boundary vertex
cannot belong to another block, since no other block uses `b` or `c`; and
an internal occurrence of `B` or `C` would permit a shorter choice of
endpoint.  Hence all internal vertices lie outside the boundary.

Otherwise, simultaneously interchange `b,c` on every component meeting
`B`.  These components are pairwise disjoint and none meets `C`.  Every
vertex of `B` changes to colour `c`, every vertex of `C` retains colour
`c`, and no other boundary vertex changes.  The resulting colouring is
proper by the ordinary Kempe-component argument; equivalently, the assumed
absence of a literal `B-C` edge makes the merged equality block legal.
Thus exactly `B,C` merge and every other boundary block remains unchanged.

The lemma is valid for disconnected blocks and for multiple simultaneous
component swaps.  It makes no assertion that the resulting path avoids a
preselected packet.

## 4. Detaching the singleton reservoir

Assume `K={k}` and `k` shares its colour with `J`.  Because `I` is already
one block of order at least two, the boundary initially has at most six
blocks.  The additional equality between `k` and a member of `J` reduces
this to at most five, so one of the six palette colours is absent from the
whole boundary.

Consider the two-colour graph on that spare colour and the colour of `k`.
The spare colour occurs at no boundary vertex.  If the component containing
`k` has no `J` vertex, it contains no other boundary vertex at all: the
`I` colour is exact and `S=I dotunion J dotunion {k}`.  Swapping this one
component therefore gives `k` the spare colour and makes `{k}` a singleton
block without changing any other boundary block.

If the component does meet `J`, a shortest path from `k` to the first such
boundary vertex has no internal boundary vertex.  Since the colouring
lives on `G[R union S]`, all its internal vertices lie literally in `R`.
This is exactly alternative 2 of Theorem 4.1.  If `k` was singleton from
the start, no detachment is required.

## 5. Compressing the `J` blocks

After successful detachment, every equality block meeting `J` is contained
in `J`: the exact `I` block is separate and `{k}` is separate when present.
Any two such blocks are anticomplete because `J` is independent, so Lemma
3.1 applies.

Its swap outcome strictly reduces the number of `J` blocks while leaving
`I`, `{k}`, and all other blocks unchanged.  Repetition therefore
terminates.  If a path appears at any stage, its endpoints lie in two
distinct blocks contained in `J`, and its internal vertices lie outside
`S`, hence in `R`.  All intervening colourings remain legal trace
colourings with `I` exact.  Thus the phrase "colouring supplied by Lemma
2.1" may be read as that colouring after the displayed legal Kempe moves;
no state outside its Kempe orbit is assumed.

If no path appears, the final exact boundary partition is precisely

\[
                       I\mid J
 \quad\text{or}\quad I\mid J\mid\{k\}.
\]

There can be no extra block because `S=I dotunion J dotunion K`.

## 6. Packet demand and the correct reflection theorem

For `Pi=I|J`, one has `|Pi|=2`, hence
`d_{G[S]}(Pi)<=2`.  For `Pi=I|J|{k}`, the singleton block `{k}` itself is
a clique of order one in the singleton-block graph, so

\[
 d_{G[S]}(Pi)
 =3-\omega(G[S][\operatorname{sing}(Pi)])\le2.
\]

This remains true if `J` is itself a singleton.

The invoked result is Lemma 2.1, exact packet reflection, in the audited
adaptive packet-reflection theorem.  The two disjoint `S`-full packets in
`R` fund every block outside a maximum singleton clique and produce a
proper-minor colouring of the opposite closed shore `G[A union S]` with
exact partition `Pi`.  Its exceptional `K_7` branch can only arise there
when the partition has seven blocks; the present partitions have two or
three blocks, so the reflection conclusion applies directly.

The modified rich-shore colouring already has the same exact partition on
`G[R union S]`.  A permutation of the six colour names aligns the block
colours, and the two colourings glue because there is no `A-R` edge.  Thus
absence of a blocking path really yields a six-colouring of `G`.

## 7. Exact trust boundary

The theorem proves only the stated dichotomy: a six-colouring, or a
literal bichromatic path with its internal vertices in `R`.  The path may
intersect both full packets and need not preserve the independently
manufactured trace after contraction.  No path-to-model, packet-escape,
smaller-adhesion, or fixed-pair implication follows from this source, and
none is certified by this audit.
