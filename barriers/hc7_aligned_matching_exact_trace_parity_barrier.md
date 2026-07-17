# Actual exact-trace colourings do not align the balanced matching

**Status:** written barrier with a separate GREEN internal audit in
[`hc7_aligned_matching_exact_trace_parity_barrier_audit.md`](hc7_aligned_matching_exact_trace_parity_barrier_audit.md).
This is not a
counterexample to `HC_7`.  The graph constructed below is seven-connected
and seven-chromatic, but is not asserted to be `K_7`-minor-free or
seven-contraction-critical.

## 1. Statement

There is a finite graph `G` with a separation

\[
                    V(G)=L\mathbin{\dot\cup}S
                              \mathbin{\dot\cup}D
\]

such that:

1. `|S|=8`, the open shores `L,D` are nonempty and connected, there is no
   `L`--`D` edge, and every vertex of `S` has a neighbour in each shore;
2. `G` is seven-connected and `chi(G)=7`;
3. writing

   \[
      S=R\mathbin{\dot\cup}A\mathbin{\dot\cup}B
              \mathbin{\dot\cup}\{x\},
      \qquad |R|=3,\quad |A|=|B|=2,
   \]

   the graph `J=G[S]` has the balanced order-eight boundary structure:
   `R` is a clique, `A` and `B` are edges, `A` is anticomplete to `B`,
   and the two endpoint nonneighbour sets in `R` are nonempty and
   disjoint for each of `A,B`;
4. `I_2 vee J` has no `K_7` minor, and `overline J` has a perfect matching
   containing both a prescribed `x`--`R` edge and an `A`--`B` edge;
5. for every nonempty independent set `I` of `J`, and for either choice
   of retained shore, contracting the opposite open shore together with
   `I` gives an **actual proper minor** having a six-colouring in which
   `I` is exactly one boundary colour class; but
6. no partition of `S` induced by a proper six-colouring extends through
   both closed shores.

In particular, item 5 holds for all four edges of the aligned perfect
matching in item 4.  Thus the actual proper-minor exact single-pair traces,
even together with seven-connectivity and the complete aligned boundary
normalization, do not force the matching partition or any common boundary
partition.

## 2. The aligned boundary

Label

\[
 R=\{0,1,2\},\qquad A=\{3,4\},\qquad
 B=\{5,6\},\qquad x=7,
\]

and let `J` have edge set

\[
 \{01,02,04,06,12,13,15,23,25,34,56\}.              \tag{2.1}
\]

The endpoint nonneighbour sets in `R` are

\[
\begin{array}{c|cc}
 &\text{first endpoint}&\text{second endpoint}\\ \hline
 A=34&\{0\}&\{1,2\}\\
 B=56&\{0\}&\{1,2\}.
\end{array}                                             \tag{2.2}
\]

They are nonempty and disjoint in each row.  Moreover

\[
                 M=\{03,16,27,45\}                     \tag{2.3}
\]

is a perfect matching of `overline J`; it contains the prescribed edge
`27` from `x` to `R` and the cross edge `45` from `A` to `B`.

The graph `J` has the following tree decomposition of width three:

\[
 \{0,1,2,5\}-\{0,1,2,3\}-\{0,3,4\},
 \qquad
 \{0,1,2,5\}-\{0,5,6\},
 \qquad
 \{0,1,2,5\}-\{7\}.                                  \tag{2.4}
\]

Adding the two nonadjacent universal vertices of `I_2 vee J` to every
bag gives a tree decomposition of width five.  Hence `I_2 vee J` has no
`K_7` minor.

This example also answers a tempting preliminary question negatively:

\[
                         \alpha(J)\le2
\]

does not follow from the balanced and aligned boundary hypotheses.  In
fact

\[
                         \{0,3,5,7\}                  \tag{2.5}
\]

is an independent set, so `alpha(J)>=4`.

## 3. Two parity-separated extension relations

Let `Omega_6(J)` be the set of equality partitions of `S` into at most
six nonempty independent blocks of `J`, and put

\[
 \mathcal E=\{\Pi\in\Omega_6(J):|\Pi|\text{ is even}\},
 \qquad
 \mathcal O=\{\Pi\in\Omega_6(J):|\Pi|\text{ is odd}\}. \tag{3.1}
\]

Every exact independent-block cylinder meets both families.  Here is the
short argument, included to make the barrier self-contained.  Fix a
nonempty independent set `I`.  The graph `J-I` is not complete.  Indeed,
`J` is four-colourable by (2.3), and the standard proper-boundary lift
would give a `K_7` minor in `I_2 vee J` if `J-I` contained a five-clique;
when `|I|=4`, the unused endpoints of `A` and `B` are still nonadjacent.
Also `|I|<=4`, since an independent set uses at most one vertex from each
of the four cliques `R,A,B,{x}`.

Let `q=chi(J-I)<=4`.  An optimal `q`-colouring of the noncomplete graph
`J-I` has a nonsingleton colour class.  Its colour classes, and the
partition obtained by splitting that nonsingleton class once, use `q`
and `q+1` blocks.  Adjoining `I` as one exact block gives two legal
members of `Omega_6(J)` with opposite block-count parity.  Thus

\[
 \mathcal E\cap\mathcal O=\varnothing,
 \qquad
 \mathcal E\cap\mathcal T_I\ne\varnothing,
 \qquad
 \mathcal O\cap\mathcal T_I\ne\varnothing             \tag{3.2}
\]

for every nonempty independent `I`, where `mathcal T_I` is the family of
partitions having `I` as an exact block.

To ensure exact chromatic number seven, temporarily omit the boundary edge
`01` and define

\[
 \Pi_0=\{\{0,1\},\{2,7\},\{3\},\{4\},\{5\},\{6\}\}.  \tag{3.3}
\]

This is a proper six-block partition of `J-01`.  Apply the exact finite
colouring-relation realization theorem of Dvořák--Swart (Theorem 3 of
*A note on extendable sets of colorings and rooted minors*) to the two
permutation-closed relations

\[
                \mathcal E\cup\{\Pi_0\},
                \qquad
                \mathcal O\cup\{\Pi_0\}.              \tag{3.4}
\]

Use the connected-full augmentation and the order-seven false-twin
amplification from the
[complementary-state realization theorem](hc7_state_realization_barrier.md).
Glue
the two resulting boundaried graphs along `S`, and finally add all edges
of `J` on the boundary.

Adding `J` filters the two closed-shore extension relations to exactly
`\mathcal E` and `\mathcal O`: every partition in (3.1) is proper on `J`,
whereas `Pi_0` identifies the ends of the restored edge `01`.  Therefore
the glued graph is not six-colourable.  Deleting `01` makes `Pi_0`
available on both sides, so `G-01` is six-colourable.  Recolouring one end
of `01` with a seventh colour gives `chi(G)<=7`, and hence `chi(G)=7`.
The amplification makes `G` seven-connected, while preserving the exact
extension relations and connected boundary-full open shores.

Because (3.2) contains a colouring equating every nonedge of `J`, neither
realizer can contain an additional edge between boundary vertices.  Thus
the induced boundary really is the graph in (2.1).

## 4. Why the traces are colourings of actual proper minors

Fix a nonempty independent set `I` of `J`, retain the left shore, and take
a left-shore six-colouring in which `I` is exactly one boundary colour
class; it exists by (3.2).  The connected set

\[
                         D\cup I
\]

may be contracted to one vertex `z`: boundary fullness connects every
vertex of `I` to `D`.  Give `z` the common colour of `I`.

Every vertex of `S-I` is adjacent to `D` and has a different colour by
exactness.  A vertex in the retained open shore adjacent to `z` was
adjacent to a member of `I`, and therefore also has a different colour in
the original proper shore-colouring.  There are no edges between the two
open shores.  The colouring consequently descends to a proper
six-colouring of the contracted graph.

The contraction is a proper minor because the retained open shore is
nonempty.  The opposite orientation is identical.  This proves item 5 of
the statement using actual proper-minor colourings, rather than an abstract
list of boundary partitions.

## 5. Exact scope

There is an even stronger reason that simultaneous contractions of the two
open shores do not add a state-transfer constraint.  Let `I,K` be disjoint
independent boundary pairs.  Contract

\[
                         L\cup I
       \qquad\text{and}\qquad
                         D\cup K
\]

to two distinct vertices.  The two contracted sets are connected and
disjoint.  The resulting minor has exactly

\[
                         8-2-2+2=6
\]

vertices, so assigning a different colour to every vertex is a proper
six-colouring.  When read back on the labelled boundary, its partition is

\[
                         I\mid K
          \mid\text{four singleton blocks}.           \tag{5.1}
\]

Thus every two-pair trace, including any two edges of the aligned matching
(2.3), is automatically realized after collapsing **both** shores.  This
is information about a six-vertex quotient, not a colouring of either
uncontracted closed shore, and it cannot be used for gluing.

The construction rules out every argument whose only host input beyond
the aligned boundary is:

- seven-connectivity and exact chromatic number seven;
- two connected boundary-full shores; and
- the collection of actual exact traces obtained by contracting either
  shore together with an independent boundary set.

It does **not** rule out a theorem which genuinely uses global
`K_7`-minor exclusion or the response to every proper minor.  Those are
precisely the two major hypotheses not supplied by the construction.
It also does not supply the two named five-cliques, the canonical rooted
web, or the labelled compact `K_5` models present in the full active host,
and it does not exclude an actual order-seven separation in the amplified
realizer.  In particular, it is not a counterexample to a theorem whose
conclusion permits such a separation.
Accordingly, a successful continuation of the aligned branch must couple
an internal deletion or contraction to a labelled branch-set rerouting,
or use target-minor exclusion to turn the parity lock into a separator.
No finite invariant of the star-contraction boundary partitions alone can
perform that step.
