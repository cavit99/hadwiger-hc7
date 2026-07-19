# Independent audit: adaptive exact-seven `(1,2)` boundary closure

**Verdict:** GREEN for Lemmas 2.1, 3.1, and 3.2 and for both finite
censuses, after one diagnostic correction.

**Audited source:**
[`hc7_exact7_adaptive_12_boundary_closure.md`](hc7_exact7_adaptive_12_boundary_closure.md)
at SHA-256

```text
df8d47261337659ade312bf8a6dfab22453c92bae5841bbb6b6fd303eadf6533
```

This is a separate internal mathematical audit, not external peer review.
The deterministic verifiers were rerun at this audit revision with source
hashes

```text
hc7_exact7_adaptive_12_boundary_verify.py
9e988ecc2daf2849850f540d549719b03bd0896c7bceeda47ac28e6dfcc632d8

hc7_exact7_adaptive_12_packet_quotient_probe.py
0c44a69f09e560d8122e776c3f7c14f6a60a71dc6fd3e166ab6c259d50be4833
```

The robust independent-block argument never lifts a colouring through a
packet on the shore where that packet was contracted.  Its first contraction
is supported in `L union S` and is pulled back only to `G[R union S]`; the
two-packet reflection is supported in `R union S` and is pulled back only to
`G[L union S]`.  Both returned boundary partitions are exact and therefore
can be aligned by a permutation of the six colours.

The two-anchor construction gives seven literal, pairwise disjoint,
connected, pairwise adjacent branch sets.  No packet--packet edge and no
connectivity beyond the stated packet connectedness is being assumed.

The draft originally said that nine of the ten absolute-demand-three
residuals contain two disjoint triangles and treated the Moser spindle as the
tenth case.  This was misleading: **all ten do**, including the Moser
spindle.  The promoted draft has been corrected accordingly.

## 1. Thin-side forcing and pullback

Let `Q subseteq L` be `S`-full and let `I subseteq S` be independent.  The
set `V(Q) union I` is connected because `Q` is connected and every literal
vertex of `I` has a neighbour in `Q`.  Contracting a spanning tree therefore
produces one vertex `z` in a proper minor: `I` is nonempty in every
application and at least one literal packet--boundary edge is contracted.

Only `G[R union S]` is recovered from a six-colouring of this minor.  Giving
each vertex of `I` the colour of `z` is proper because `I` is independent and
every edge from `I` to the retained graph became an edge at `z`.  Fullness of
`Q` at every vertex of `S-I` makes `z` adjacent to every such literal vertex,
so `I` is an exact colour block on `S`, not merely a subset of one.

The complete equality partition `Pi` read from this colouring has at most six
blocks.  It is a partition into independent blocks because it comes from a
proper colouring.

## 2. Packet-demand arithmetic

The following cases exhaust the possible returned partitions containing the
exact block `I`.

* If `|I|>=5`, then `|Pi|<=3`.  In the only extremal case there is a
  singleton block, hence `d_H(Pi)<=3-1=2`.
* If `|I|=4`, then `|Pi|<=4`.  At three blocks the three outside vertices
  have residual block sizes `2,1`, yielding a singleton.  At four blocks all
  three are singletons; an edge in `H[S-I]` retains a singleton clique of
  order two.  Thus the demand is at most two.
* If `|I|=3` and `H[S-I]` contains a triangle, three blocks are impossible
  because they would bipartition that triangle.  At four blocks the residual
  sizes are `2,1,1`, and the triangle occupies all three residual blocks, so
  the two singleton vertices are adjacent.  At five blocks the residual
  vertices are all singleton and the triangle itself can be retained.  The
  demands are again at most two.

The stated criteria are sharp for robust forcing when `omega(H)<=3`.
Refining every residual block to singletons gives the maximum demand.  For
`|I|=4` this is safe exactly when the three-vertex complement has an edge;
for `|I|=3` it is safe exactly when the four-vertex complement has a
triangle.  No independent pair is robust because its five-vertex complement
would need clique number at least four.  A singleton is also not robust: use
one independent pair among the other six vertices and make the remaining
five vertices singleton blocks; this is a six-block state of demand at least
three.

The two packets on `R` now reflect `Pi` by the already-audited exact packet
reflection lemma.  At least one block is assigned to a packet because `I` is
nonsingleton, so the reflecting minor is proper.  The first and reflected
closed-shore colourings have exactly the same equality partition.  Their
injective block-to-colour maps differ by a partial permutation of a six-set,
which extends to a full palette permutation.  With no `LR` edge, the aligned
colourings glue.

## 3. Two-anchor `K_4` lift

Suppose `H-{x,y}` has a `K_4` model with branch sets
`B_1,...,B_4`.  The seven proposed bags are

```text
Q union {x},  P_1 union {y},  P_2,  B_1, B_2, B_3, B_4.
```

They are pairwise disjoint.  The first two are connected through their
literal anchors and the third packet is connected by definition.  The three
packet-derived bags are pairwise adjacent as follows:

* `Q union {x}` to `P_1 union {y}` through a `Q`--`y` edge;
* `Q union {x}` to `P_2` through a `P_2`--`x` edge;
* `P_1 union {y}` to `P_2` through a `P_2`--`y` edge.

Every packet-derived bag meets every `B_j` by fullness at any literal vertex
of `B_j`; the four `B_j` are pairwise adjacent by the model.  These account
for all 21 adjacencies of a literal `K_7` model.  In particular, the proof
does not assume an edge between the open shores or between the two packets
on `R`.

## 4. Independent finite verification

The supplied probe and a second structural verifier both used the complete
NetworkX atlas.  The latter used an independent exact test for a `K_4` minor
on five vertices: either four singleton vertices form a `K_4`, or an edge is
the unique two-vertex branch set and the other three vertices form a triangle
seen by that edge.

Both computations give:

```text
K4-free seven-vertex boundary graphs       685
proper equality partitions                 876
graphs with a robust independent block     446
graphs with a two-anchor K4 lift            246
overlap                                    136
closed by their union                       556
residual                                   129
residual with some demand-at-most-2 state   119
residual with minimum demand 3               10
```

The structural verifier also checked, for all 18,264 independent-set/boundary
pairs, the exact maximum-demand formula and the split-remainder criterion.
All ten absolute-demand-three residuals have two vertex-disjoint triangles.
One of them is the eleven-edge Moser spindle; in its standard labelling the
triangles `{1,2,6}` and `{3,4,5}` are disjoint.

This census is only a boundary classification.  In particular, the existence
of an abstract demand-at-most-two partition in 119 residual graphs does not
show that a proper-minor colouring of the thin shore returns it.

## 5. Connected-rich one-anchor lift

Assume `G[R]` is connected.  Take a shortest path in `G[R]` between the
disjoint vertex sets `V(P_1)` and `V(P_2)`.  No internal vertex of this path
belongs to either packet: an internal occurrence in either endpoint set
would give a shorter set-to-set path.  Add every path vertex except the
endpoint in `P_2` to `P_1`.  The enlarged first packet is connected,
`S`-full, disjoint from `P_2`, and adjacent to `P_2` by the last path edge.
This also covers a path of length one.

If `H-x` has a `K_4` model with bags `B_1,...,B_4`, use

```text
Q union {x},  enlarged P_1,  P_2,  B_1, B_2, B_3, B_4.
```

The first bag meets each rich packet bag through that packet's literal
contact at `x`; the two rich packet bags are adjacent by the path extension.
All three packet-derived bags meet every `B_j` by fullness, and the four
boundary bags are pairwise adjacent by the model.  Disjointness and
connectedness are literal.  Thus all 21 `K_7` adjacencies are present.

Connectedness of the rich open shore, or at least a path in the open shore
between the selected packets, is indispensable to this construction.  It
must not be applied when the two rich packets lie in different components.

The connected-rich count was checked twice.  The supplied verifier uses
exhaustive connected branch sets.  An independent check used the equivalence
between `K_4`-minor-freeness and treewidth at most two and computed exact
treewidth over all elimination orders of each six-vertex deletion graph.
Both give 33 additional closures among the previous 129 residuals and the
same 96-boundary residue:

```text
(alpha, minimum demand) = (4,2): 22
                           (3,2): 67
                           (3,3):  7
```

Thus no independence-number-two boundary remains in the connected-rich
cell.  In particular, this conditional one-anchor lemma removes the Moser
spindle there; it says nothing about a disconnected rich shore.

## 6. Exact promoted scope

The result eliminates an infinite exact-adhesion family: every actual
packet-vector `(1,2)` cell whose boundary satisfies either the robust-block
criterion or the two-anchor `K_4` criterion.  It does **not** eliminate all
of `(1,2)`, and it does not convert an arbitrary favourable boundary state
into a realizable shore state.  When the rich shore is connected, the
one-anchor lemma eliminates a further 33 boundary types, leaving 96.
