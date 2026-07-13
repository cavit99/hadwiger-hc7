# A four-connected rural barrier to two-block list recursion

## Status

This small gadget falsifies the proposed continuation

\[
 \text{double-forced total-contraction state}
 \Longrightarrow
 \text{the next two-block state expands side-by-side}.    \tag{0.1}
\]

The carrier is planar and four-connected, all of its external attachment
vertices lie on one facial cycle, and both connected sides of the split
are full to the boundary.  The total-contraction state forces five
colours at every facial vertex.  The two-block contraction has another
proper state, but its literal lists reduce the odd facial cycle to the
same two colours and hence do not colour the original carrier.

The construction is a local state barrier, not a contraction-critical
`K_7`-minor-free host.  It identifies the exact missing hypothesis:
planarity and fullness do not lift a two-block state; one needs the
outer-face list bounds already used in the active-face theorem, a
bipartite carrier, or an actual opposite-shore equality-state collision.

## 1. Carrier and full adhesion

Let `K` be the pentagonal-antiprism graph.  Write its two pentagonal
cycles as

\[
 A=a_0a_1a_2a_3a_4a_0,qquad
 B=b_0b_1b_2b_3b_4b_0,
\]

and add the cross edges

\[
                         a_ib_i,quad a_ib_{i-1}
                         \qquad(i\bmod 5).                 \tag{1.1}
\]

This is a four-connected plane graph in which `A` is a facial
five-cycle.  Let

\[
                         S=\{s_1,s_2,s_3,s_4,s_5\}        \tag{1.2}
\]

be independent, and join every `a_i` to every member of `S`.  There are
no `B-S` edges.  Thus every external attachment vertex of `K` lies on
the one face `A`.

Put `X={a_0}` and `Y=V(K)-X`.  Both sets are connected and adjacent,
and both are collectively adjacent to every member of `S`.  A spanning
tree of `K` may be chosen with `a_0` as a leaf, so `X|Y` is literally a
two-side split obtained by deleting one spanning-tree edge.

## 2. The two incompatible local states

Contract all of `K` to `z`.  Colour the five independent boundary
vertices with five distinct colours and give `z` the sixth colour
`alpha`.  This is a proper total-contraction state.  Every vertex of the
facial cycle `A`, in particular any selected two vertices `x,y`, sees
all five non-`alpha` boundary colours.  Assigning the contraction colour
back to `A` cannot colour its edges.

Now contract `X` and `Y` separately to adjacent vertices `z_X,z_Y`.
Give these two vertices distinct colours `alpha,beta`, and colour `S`
with the other four colours, repeating one of them once.  Both contracted
vertices are adjacent to all of `S`, so this is a proper six-colouring of
the two-block contraction.

Nevertheless it does not expand to the original carrier.  For every
`a_i`, the literal list left by the boundary state is exactly

\[
                         L(a_i)=\{\alpha,\beta\}.          \tag{2.1}
\]

The vertices `a_0,...,a_4` induce the odd cycle `A`, which has no
colouring from the common two-element lists (2.1).  The bottom vertices
have full six-element lists, but they cannot repair this facial
obstruction.

Thus the new state `d` neither gives a strict side-by-side planar list
expansion nor preserves the five-singleton boundary state of the total
contraction.

## 3. Why no state collision follows locally

The equality partition of the total state has five singleton boundary
blocks.  The displayed two-block state has four blocks.  These are
different labelled partitions.  Which partitions are produced by an
operation in an opposite open shore is independent data: it is not
determined by `K`, its planar embedding, its full attachment to `S`, or
the existence of these two internal contraction states.

Accordingly a collision requires exactly the crossed-shore hypothesis of
the dynamic state-splice theorem (or a theorem forcing that hypothesis).
It cannot be inferred from the two-block recursion inside the carrier.

## 4. Exact repair hypotheses

Any valid positive recursion must add at least one condition which the
gadget violates:

1. **Outer-face list slack:** every facial vertex sees at most three
   boundary colours, giving lists of order at least three and allowing
   Thomassen's outer-face extension;
2. **Bipartite lift:** the relevant carrier is bipartite, so the two
   colours left by a full two-block state can colour it (with the
   interface orientation checked); or
3. **Faithful opposite state:** the same labelled boundary partition is
   produced by an operation in the opposite shore, so one glues rather
   than expands either contracted side.

Four-connectivity, planarity, one facial attachment cycle, full contact
of both split sides, and two distinct block colours are all present here
and are therefore insufficient.

## 5. Verification

The companion script
`hc7_near_k7_two_block_planar_list_barrier_verify.py` checks the graph,
planarity, four-connectivity, facial five-cycle in an explicit embedding,
fullness of both sides, and the two displayed colour states.
