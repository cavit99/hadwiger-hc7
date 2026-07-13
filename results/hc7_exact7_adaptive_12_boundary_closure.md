# Adaptive `(1,2)` boundary closure

**Status:** proved and independently audited.

## 1. Setting

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

with no edge between `L` and `R`.  Assume every proper minor of `G` is
six-colourable, `L` contains one connected `S`-full packet `Q`, and `R`
contains two disjoint connected `S`-full packets `P_1,P_2`.  Put
`H=G[S]`.

The exact-seven packet theorem gives `omega(H)<=3` in a hypothetical
`K_7`-minor-free graph with packet vector `(1,2)`.

For a proper equality partition `Pi` of `S`, let

\[
 d_H(\Pi)=|\Pi|-\omega\bigl(H[\operatorname{sing}(\Pi)]\bigr).
\]

The already-audited exact packet-reflection lemma says that the two packets
in `R` reproduce every returned partition of demand at most two.

## 2. Robust independent-block closure

### Lemma 2.1

Suppose `H` contains an independent set `I` satisfying one of

1. `|I|>=5`;
2. `|I|=4` and `H[S-I]` contains an edge; or
3. `|I|=3` and `H[S-I]` contains a triangle.

Then `G` has a literal `K_7` minor or `G` is six-colourable.

### Proof

Contract a spanning tree of `Q union I` and six-colour the resulting proper
minor.  Pulling the colouring back only to `G[R union S]` makes `I` one
exact boundary block.  Let `Pi` be the complete returned equality
partition.

If `|I|>=5`, then `|Pi|<=3`.  When there are three blocks at least one
singleton block exists, so `d_H(Pi)<=3-1=2`.

Let `|I|=4`.  Then `|Pi|<=4`.  At three blocks, the three outside vertices
occupy two blocks, so one is a singleton and the demand is at most two.  At
four blocks all three outside vertices are singletons; the assumed edge
among them is a two-vertex singleton clique, again giving demand at most
two.

Let `|I|=3` and let `T` be a triangle in `H[S-I]`.  Here `|Pi|<=5`.  A
three-block return would partition `S-I` into two independent sets, which
is impossible because it contains `T`.  At four blocks, `S-I` has block
sizes `2,1,1`.  The three vertices of `T` occupy three distinct blocks, so
the two singleton blocks containing two of them are adjacent.  Thus the
singleton clique has order at least two.  At five blocks every vertex of
`S-I` is a singleton and `T` is a singleton clique of order three.  In all
cases `d_H(Pi)<=2`.

Use `P_1,P_2` to reflect `Pi` exactly onto the closed thin shore.  The first
minor colouring and the reflected colouring induce the same literal
partition, so a permutation of the six colour names aligns them and they
glue.  This is a six-colouring of `G`.  The alternative literal `K_7`
outcome is the seven-block exception in exact packet reflection.  `square`

### Sharpness of the three criteria

For a fixed independent block `I` in a graph with `omega(H)<=3`, the three
conditions above are also necessary for **every** proper returned
partition containing `I` to have demand at most two.  If `|I|=4` and its
three-vertex complement is independent, the partition consisting of `I`
and three singleton blocks has demand three.  If `|I|=3` and its
four-vertex complement is triangle-free, the partition consisting of `I`
and four singleton blocks has demand at least three.  Independent blocks
of order at most two are never robust: take as many singleton blocks as
possible; `omega(H)<=3` leaves demand at least three.

## 3. Two-anchor `K_4` lift

### Lemma 3.1

If there are distinct `x,y in S` such that `H-{x,y}` contains a `K_4`
minor, then `G` contains a literal `K_7` minor.

### Proof

Let `B_1,...,B_4` be four disjoint connected pairwise adjacent branch sets
of a `K_4` model in `H-{x,y}`.  Use the seven bags

\[
 V(Q)\cup\{x\},\qquad
 V(P_1)\cup\{y\},\qquad
 V(P_2),\qquad
 B_1,B_2,B_3,B_4.                                      \tag{3.1}
\]

They are disjoint and connected.  The first two packet bags are adjacent
because `Q` has a literal edge to `y`; the unanchored packet `P_2` is
adjacent to them through `x` and `y`; and every packet bag is adjacent to
every `B_j` because each `B_j` contains a literal boundary vertex and all
three packets are `S`-full.  The last four bags are pairwise adjacent by
the `K_4` model.  Thus (3.1) is a literal `K_7` model.  `square`

This lift uses only two boundary anchors for all three packets.  It is
strictly stronger than the packet-plus-clique lift, since the four
remaining bags may be a nontrivial `K_4` model on five boundary vertices.

### Lemma 3.2 (one-anchor lift when the rich shore is connected)

Assume in addition that `G[R]` is connected.  If some `x in S` satisfies

\[
                         H-x\succeq K_4,                 \tag{3.2}
\]

then `G` contains a literal `K_7` minor.

### Proof

Choose a shortest path in `G[R]` from `P_1` to `P_2`.  Its internal
vertices avoid both packets.  Add the path, except for its endpoint in
`P_2`, to `P_1`.  The enlarged `P_1` remains connected and `S`-full, stays
disjoint from `P_2`, and is now adjacent to `P_2`.

Let `B_1,...,B_4` be the branch sets of a `K_4` model in `H-x`.  The seven
bags are

\[
 V(Q)\cup\{x\},\qquad V(P_1),\qquad V(P_2),\qquad
 B_1,B_2,B_3,B_4.                                      \tag{3.3}
\]

The first packet bag is adjacent to the other two through their literal
contacts at `x`.  The two rich packet bags are adjacent by the path
extension.  Every packet bag meets every boundary model bag by fullness,
and the four model bags are pairwise adjacent.  Thus (3.3) is a literal
`K_7` model.  `square`

Connectedness is essential to this proof: when the two rich packets lie in
different open-shore components, no packet--packet path avoiding `S`
exists and the one-anchor construction is unavailable.

## 4. Combined theorem and finite trust boundary

### Theorem 4.1

The exact `(1,2)` cell is impossible whenever `H` has either

1. a robust independent block from Lemma 2.1; or
2. a pair `x,y` for which `H-{x,y}` has a `K_4` minor.

Among the 685 unlabelled seven-vertex graphs with clique number at most
three, exhaustive enumeration gives

\[
\begin{array}{c|r}
\text{has a robust independent block}&446\\
\text{has the two-anchor }K_4\text{ lift}&246\\
\text{has both}&136\\ \hline
\text{closed by their union}&556\\
\text{residual}&129.
\end{array}
\]

The residual is defined invariantly, not by labels:

> `H` has no independent set satisfying Lemma 2.1, and every graph
> `H-{x,y}` is `K_4`-minor-free.

Of these 129 boundary graphs, 119 admit at least one demand-at-most-two
partition but have no block which forces all returned partitions to be
safe.  The remaining ten have minimum packet demand three.  All ten contain
two vertex-disjoint triangles; this includes the eleven-edge Moser spindle,
whose disjoint triangles in the standard labelling are `{1,2,6}` and
`{3,4,5}`.  This last census is diagnostic only: no claim is made that an
arbitrary favourable partition is realized by the thin-shore minor.

If the rich shore is connected, Lemma 3.2 closes 33 additional graphs from
this 129-graph residual.  The connected-rich residual has 96 unlabelled
boundaries, distributed as follows:

\[
\begin{array}{c|c|r}
\alpha(H)&\min d_H&\text{count}\\ \hline
4&2&22\\
3&2&67\\
3&3&7.
\end{array}
\]

In particular both independence-number-two residuals, including the Moser
spindle, close whenever the rich open shore is connected.  The seven
remaining absolute-demand-three boundaries all have independence number
three and two disjoint boundary triangles.

## 5. Reproducible verification

The verifier

`active/hc7_exact7_adaptive_12_packet_quotient_probe.py`

uses the complete NetworkX atlas of unlabelled graphs through order seven.
For each of the 685 graphs it:

* enumerates all proper equality partitions with at most six blocks;
* computes exact packet demand;
* checks the robust-block criterion directly; and
* searches every one- and two-vertex deletion exhaustively for four
  disjoint, connected, pairwise adjacent branch sets.

The count is a finite certificate supporting the structural theorem; the
two mathematical closure lemmas themselves do not depend on computation.

## 6. Exact remaining mechanism

This theorem does **not** close `(1,2)`.  The unresolved issue is no longer
mere packet demand.  In the 119 adaptive residuals, a safe state exists but
minor-criticality has not yet been shown to select it.  A demand-three
return must be converted by a shore-internal exchange into one of:

1. a third partial labelled carrier, so the returned state can be
   reflected;
2. a different thin-packet colouring with demand at most two; or
3. one fixed pair whose deletion is `K_5`-minor-free.

The ten absolute demand-three boundaries show that state selection alone
cannot be a complete argument.  In the connected-rich cell the one-anchor
lift removes three of them, including Moser; the remaining seven still
require a genuine labelled-carrier or fixed-pair mechanism.  In the
disconnected-rich cell all ten remain possible at this level.
