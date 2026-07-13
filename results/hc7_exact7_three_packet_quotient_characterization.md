# Exact three-packet quotient characterization

**Status:** proved and independently audited.

## 1. Statement

Let `H` be a graph on a literal seven-set `S`.  Form `J_0(H)` by adjoining
three new vertices `u_0,u_1,u_2`, each complete to `S`, with no edge among
the three.  Form `J_1(H)` in the same way, but add the one edge `u_1u_2`.

### Theorem 1.1

The following equivalences hold.

\[
 J_0(H)\succeq K_7
 \quad\Longleftrightarrow\quad
 \text{there are distinct }x,y\in S
 \text{ with }H-\{x,y\}\succeq K_4,                    \tag{1.1}
\]

and

\[
 J_1(H)\succeq K_7
 \quad\Longleftrightarrow\quad
 \text{there is }x\in S
 \text{ with }H-x\succeq K_4.                           \tag{1.2}
\]

Thus the two-anchor and connected-rich one-anchor lifts in the exact
`(1,2)` adhesion are exhaustive at the static packet-quotient level.
Any further `K_7` construction must split a packet, use an internal shore
path or bridge as an additional labelled carrier, or use a proper-minor
state transition.

## 2. The easy directions

Suppose `H-{x,y}` has a `K_4` model with bags `B_1,...,B_4`.  In `J_0(H)`
the seven bags

\[
 \{u_0,x\},\quad \{u_1,y\},\quad \{u_2\},
 \quad B_1,B_2,B_3,B_4                                  \tag{2.1}
\]

are connected, disjoint and pairwise adjacent.  The first two anchors make
the three otherwise independent universal vertices into three clique bags,
and universality joins them to every boundary-model bag.  Hence (1.1)
holds from right to left.

If `H-x` has a `K_4` model, use instead

\[
 \{u_0,x\},\quad \{u_1\},\quad \{u_2\},
 \quad B_1,B_2,B_3,B_4.                                  \tag{2.2}
\]

The edge `u_1u_2` supplies the only packet--packet adjacency not supplied
through `x`.  This proves the reverse implication in (1.2).

## 3. Independent packet vertices: necessity of two anchors

Let `M` be a `K_7` model in `J_0(H)`.  Call a model bag a **packet bag**
when it contains at least one of `u_0,u_1,u_2`, and let `r` be the number
of packet bags.  Thus `0<=r<=3`.  Every other model bag lies entirely in
`S`, so the seven-set `S` contains `7-r` pairwise disjoint connected
pairwise adjacent **boundary bags**.

We select four boundary bags and find two literal vertices outside their
union.

* If `r=0`, there are seven boundary bags.  Four selected bags leave three
  nonempty boundary bags, hence at least three literal vertices outside.
* If `r=1`, there are six boundary bags.  Four selected bags leave two
  nonempty boundary bags, hence two literal vertices outside.
* If `r=2`, there are five boundary bags.  The two packet bags are adjacent,
  but the packet vertices themselves are pairwise nonadjacent.  Therefore
  at least one of the two packet bags contains a literal boundary vertex:
  without one, no edge could join the packet bags.  Four selected boundary
  bags consequently avoid both the fifth nonempty boundary bag and that
  packet-bag boundary vertex.  These supply two distinct outside vertices.
* If `r=3`, there are four boundary bags, which we select.  For the three
  packet bags to be pairwise adjacent, at least two of them must contain a
  boundary vertex.  Indeed, one anchored packet bag can meet both other
  packet vertices, but the other two unanchored bags would remain
  nonadjacent.  Disjointness makes the two anchors distinct.  Hence the
  four boundary bags avoid at least two vertices of `S`.

In every case choose distinct `x,y` outside the four selected boundary
bags.  Those four bags remain a `K_4` model in `H-{x,y}`.  This proves the
forward implication of (1.1).

No assumption about how many vertices a boundary bag contains was used;
the unused model bags and necessary packet anchors provide the two literal
vertices outside the selected four-bag model.

## 4. One rich packet edge: necessity of one anchor

Now let `M` be a `K_7` model in `J_1(H)`, and define `r` as above.

If `r<=2`, there are at least five boundary bags.  Select four of them and
choose any literal vertex `x` in another nonempty boundary bag.  The four
selected bags give a `K_4` model in `H-x`.

Suppose `r=3`.  There are exactly four boundary bags.  The packet vertex
`u_0` is nonadjacent to both `u_1` and `u_2`.  Consequently the three
packet bags cannot be pairwise adjacent unless at least one of them contains
a boundary vertex: the sole packet edge `u_1u_2` does not join the `u_0`
bag to either rich packet bag.  Choose such a literal vertex `x`.  The four
boundary bags avoid `x` and form a `K_4` model in `H-x`.

This proves the forward implication of (1.2), and hence Theorem 1.1.

## 5. Literal lift to an actual adhesion

In an actual exact-seven `(1,2)` adhesion, replace each quotient packet
vertex by its connected `S`-full packet.  Connectivity and every quotient
edge lift literally.  If the rich open shore is connected, a shortest path
between its two disjoint full packets can be assigned to one packet to
create their mutual edge while preserving disjointness and fullness.

Therefore Theorem 1.1 exactly matches the audited two-anchor and one-anchor
adhesion lemmas.  It does **not** say that a residual adhesion is possible;
it says only that contracting each available full packet to one static
vertex has been exhausted.  The residual theorem must preserve more of the
shore than this quotient does.

## 6. Finite cross-check

`results/hc7_exact7_three_packet_quotient_verify.py` independently enumerates
all 5,880 set partitions of the ten quotient vertices into seven nonempty
branch sets for every one of the 685 unlabelled seven-vertex graphs of
clique number at most three.  Its exact minor search agrees with (1.1) and
(1.2): the independent quotient adds no boundary type beyond the
two-anchor test, while the single rich edge adds exactly the 33 one-anchor
types recorded in the adaptive `(1,2)` closure.
