# Kempe normalization at the universal edge of an exact seven-vertex boundary

**Status:** written proof; separate internal audit GREEN.  This is a
conditional theorem about the exceptional exact order-seven separation.  It
does not prove `HC_7`.

## 1. Setup

Let `G` be a graph such that

1. `chi(G)=7`;
2. `G` has no `K_7` minor; and
3. every proper minor of `G` is six-colourable.

Suppose

\[
        V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
        \qquad |S|=7,
\]

where `L` and `R` are nonempty and connected, there is no edge between
`L` and `R`, and each of `L,R` is adjacent to every vertex of `S`.  Assume

\[
        G[S]=G[\{p,q\}]\vee G[C],
        \qquad pq\in E(G),\qquad G[C]\cong C_5.       \tag{1.1}
\]

Thus `p,q` are the adjacent universal vertices of the boundary and
`C` is its five-cycle.

The nonedges of `G[C]` form another five-cycle.  We call this cycle `D`.
For a colouring `c`, write

\[
                 m(c)=|c(C)|.                           \tag{1.2}
\]

Since `G-pq` is a proper minor, it has a six-colouring.  Fix such a
colouring `c` for which `m(c)` is minimum.

## 2. The normalization theorem

### Theorem 2.1 (universal-edge Kempe normalization)

In the setup above, the following assertions hold.

1. The vertices `p,q` have one common colour, say `alpha`, and

   \[
                         m(c)\in\{3,4\}.                \tag{2.1}
   \]

2. Let `beta` be a colour absent from the literal boundary `S`.  At
   least one of the two open shores contains a `p`--`q` path all of whose
   vertices have colours in `\{alpha,beta\}` and whose internal vertices
   lie in that shore.

3. If `m(c)=3`, there are two colours absent from `S`, and one *same*
   open shore contains a path of the type in item 2 for each of them.

4. Suppose `m(c)=4`.  The repeated colour on `C` occurs on one edge
   `x_0x_1` of the nonedge-cycle `D`.  Label

   \[
       D=x_0x_1x_2x_3x_4x_0.                            \tag{2.2}
   \]

   Then `x_2,x_3` lie in one bichromatic component and `x_3,x_4`
   lie in one bichromatic component of `G-pq`.  Each corresponding path
   has all its internal vertices in a single open shore.

   Consequently `x_2,x_3,x_4` are the roots of a `K_3`-minor model.
   If paths for both `x_2x_3` and `x_3x_4` can be chosen through the
   same open shore, then `G` has the following explicit
   `K_7`-minus-one-edge minor model: all branch-set adjacencies are
   present except possibly the adjacency between the branch set rooted
   at `x_1` and the branch set rooted at `x_2`.

### Proof

Every six-colouring of `G-pq` gives `p,q` the same colour.  Otherwise the
deleted edge could be restored and the colouring would six-colour `G`.
Call this common colour `alpha`.  Since both `p` and `q` are adjacent to
every vertex of `C`, the colour `alpha` is absent from `C`.  The graph
`G[C]` is an odd cycle, so

\[
                         3\le m(c)\le5.                 \tag{2.3}
\]

We first exclude equality on the right.  Suppose `m(c)=5`.  The five
vertices of `C` then have pairwise distinct colours.  Let `xy` be any
edge of the nonedge-cycle `D`.  If `x,y` belonged to different components
of the subgraph induced by their two colours, interchange those colours
on the component containing `x`.  No other vertex of `C` has either
colour, and `y` is in the other component.  The resulting six-colouring
of `G-pq` uses only four colours on `C`, contrary to the choice of `c`.

Thus the endpoints of every edge of `D` lie in one bichromatic component,
in this one fixed colouring.  The pseudoforest theorem of
Kriesell--Mohr, applied to the five-cycle `D`, gives five pairwise
disjoint connected branch sets

\[
                         B_x\quad(x\in C)                \tag{2.4}
\]

rooted at the five vertices of `C` and adjacent for every edge of `D`.
For a pair not joined in `D`, the corresponding two roots are adjacent in
`G[C]`; hence the root edge joins the two branch sets.  The sets in (2.4)
therefore form a `K_5`-minor model rooted at `C`.  They may be chosen in
the union of the five root-colour classes and consequently avoid `p,q`,
whose colour is `alpha`.

Now add the singleton branch sets `\{p\},\{q\}`.  They are adjacent to
one another and to every set in (2.4), because every set contains its
boundary root.  This is a `K_7`-minor model, contrary to the hypothesis.
Therefore `m(c)<=4`, proving item 1.

Fix a colour `beta` absent from `S`, and let

\[
       H_L=G[L\cup S]-pq,
       \qquad H_R=G[R\cup S]-pq.                        \tag{2.5}
\]

Suppose first that `p,q` are in different components of the
`\{alpha,beta\}`-coloured subgraph of `H_L`.  Interchange `alpha` and
`beta` on the component containing `p`.  On the boundary this changes
only the colour of `p`: the colour `beta` is absent from `S`, the colour
`alpha` occurs there only at `p,q`, and `q` lies in the other component.
After the interchange the edge `pq` is proper.  We have therefore
obtained a six-colouring of the unmodified closed shore `G[L\cup S]`
whose boundary equality partition is obtained from `c|_S` by splitting
the block `\{p,q\}`.  The same assertion holds with `L` replaced by `R`.

If both sides admitted this interchange, the two closed-shore colourings
would induce the same equality partition on `S`.  Permuting colour names
on one side and gluing would six-colour `G`, a contradiction.  Hence one
side contains a `p`--`q` path in the indicated two-coloured subgraph.
No internal vertex of that path lies in `S`, so all its internal vertices
lie in one open shore.  This proves item 2.

If `m(c)=3`, exactly two colours, say `beta,gamma`, are absent from `S`.
Suppose no one shore contains both required paths.  After interchanging
the names of the shores and the two absent colours if necessary, the
`\{alpha,beta\}` connection occurs only on the left and the
`\{alpha,gamma\}` connection occurs only on the right.  The left side
therefore admits the `\{alpha,gamma\}` interchange at `p`, while the
right side admits the `\{alpha,beta\}` interchange at `p`.  The two
resulting proper closed-shore colourings induce the same equality
partition on `S`: `p,q` become distinct singleton blocks and the equality
pattern on `C` is unchanged.  They again glue after a permutation of the
six colour names, a contradiction.  This proves item 3.

It remains to prove item 4.  In a proper four-colouring of a five-cycle,
exactly one colour is repeated, on a nonadjacent pair.  This pair is one
edge `x_0x_1` of `D`, and the vertices `x_2,x_3,x_4` have three distinct
colours which occur nowhere else on `C`.

If `x_2,x_3` belonged to different components of the subgraph induced by
their two colours, a Kempe interchange on the component containing one
of them would make the two roots equal-coloured and remove one colour
from `C`.  It would produce a six-colouring of `G-pq` with `m=3`, contrary
to minimality.  The same argument applies to `x_3,x_4`.  The interiors of
the resulting paths avoid `S`, since their endpoint colours occur on no
other boundary vertices.  Each path therefore has its interior in one
open shore.

Apply the Kriesell--Mohr theorem to the two-edge path
`x_2x_3x_4`, in the subgraph consisting of these roots and two such
bichromatic paths.  It gives disjoint connected sets

\[
                         D_2,D_3,D_4                    \tag{2.6}
\]

rooted at `x_2,x_3,x_4`, respectively, with `D_2` adjacent to `D_3`
and `D_3` adjacent to `D_4`.  The pair `x_2x_4` is not an edge of `D`,
so it is an edge of `G[C]` and joins `D_2` to `D_4`.  This proves the
rooted `K_3` assertion.

Finally suppose the two required paths lie in, say, `L`.  The sets in
(2.6) may then be chosen inside

\[
                         L\cup\{x_2,x_3,x_4\}.           \tag{2.7}
\]

The following seven sets are pairwise disjoint and connected:

\[
 \{p\},\quad \{q\},\quad D_2,\quad D_3,\quad D_4,
 \quad R\cup\{x_0\},\quad \{x_1\}.                    \tag{2.8}
\]

The first two are adjacent to every other set.  The three `D_i` are
pairwise adjacent.  The connected set `R\cup\{x_0\}` is adjacent to all
other sets because `R` is adjacent to every boundary vertex.  Finally,
`x_1` is adjacent in `G[C]` to `x_3,x_4`, and hence to `D_3,D_4`.
Thus every pair in (2.8) is adjacent except possibly
`\{x_1\},D_2`.  This is the asserted `K_7`-minus-one-edge minor model.
The argument is symmetric when both paths lie in `R`.  \(\square\)

## 3. Exact remaining cases

Theorem 2.1 does not close the exceptional boundary.  It leaves precisely
the following colour-geometric obstructions.

1. **Three colours on the five-cycle.**  One shore contains two
   `p`--`q` Kempe paths for the two colours absent from the boundary, but
   the paths may share vertices of colour `alpha` and do not by themselves
   provide five disjoint rooted branch sets.
2. **Four colours, paths in different shores.**  The two forced
   bichromatic paths at `x_2x_3` and `x_3x_4` may have their interiors in
   different open shores, so the full opposite shore cannot be reserved
   in (2.8).
3. **Four colours, paths in one shore.**  Formula (2.8) gives only a
   `K_7`-minus-one-edge model.  A label-preserving connection from
   `x_1` to `D_2`, disjoint from the other six branch sets, is not proved.

In particular, the theorem does not force a common proper boundary
partition.  Its gain over the static ten-partition analysis is that every
survivor carries literal shore-supported Kempe paths obtained from one
global edge-deletion colouring.

## 4. Dependencies

- [exact seven-vertex boundary classification](../results/hc7_exact7_no_rigid_trace.md)
- M. Kriesell and S. Mohr,
  [*Kempe Chains and Rooted Minors*](https://arxiv.org/abs/1911.09998),
  Theorem 5.
