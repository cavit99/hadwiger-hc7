# Dynamic states at a locked rural two-row gate

## Status

This note records the exact proper-minor state supplied by
contraction-criticality and falsifies the tempting palette-to-label
continuation.  A single internal deletion/contraction colouring of a
four-connected rural carrier need not create the protected fixed
linkage, change its alternating portal order, or identify any palette
colour with a foreign model row.

Thus a successful dynamic splice must compare labelled equality
partitions on the actual adhesion from opposite shores.  It cannot be
deduced from one Kempe state inside the disk.

## 1. The safe boundary-state invariant

Let `K` be an old exterior component and put `S=N_G(K)`.  Write

\[
 C=G[K\cup S],\qquad O=G-K.
\]

For a graph `J` containing the labelled boundary `S`, let `Ext(J,S)` be
the set of equality partitions of `S` induced by proper six-colourings
of `J`.  Colour names are forgotten; the labelled blocks are retained.

### Lemma 1 (minor-transition incompatibility)

Assume `G` is not six-colourable but every proper minor of `G` is.  Then

\[
                  Ext(C,S)\cap Ext(O,S)=\varnothing.       \tag{1.1}
\]

For every edge `e` internal to `K`, however,

\[
             Ext(C/e,S)\cap Ext(O,S)\ne\varnothing.       \tag{1.2}
\]

Every partition in the intersection (1.2) fails to extend to `C`.
For deletion, every six-colouring of `G-e` gives the ends of `e` the
same colour (otherwise it already colours `G`).  Its boundary partition
therefore lies in `Ext(C-e,S) cap Ext(O,S)` and not in `Ext(C,S)`.

#### Proof

If a labelled equality partition belonged to both sets in (1.1),
permute the six colours on one side so that the labelled blocks agree
and glue the two colourings across `S`.  This would six-colour `G`.

Contracting an internal edge of `K` gives a proper minor `G/e`, hence a
six-colouring.  Its restrictions to `C/e` and `O` induce the same
labelled partition of `S`, proving (1.2).  If that partition also
extended to `C`, it would contradict (1.1).  Expanding a colouring of
`G/e` to `G-e` gives the deletion formulation with equal-coloured ends.
\(\square\)

Lemma 1 is palette-free.  It records actual boundary vertices and is the
only state which can safely be used in a colour splice.

### Lemma 2 (crossed proper-minor state splice)

Let `mu` be a deletion or contraction supported strictly inside `K`,
and let `nu` be one supported strictly in the opposite open shore
`G-(K union S)`.  Choose six-colourings of the two proper minors
`G/mu` and `G/nu`, and let their labelled boundary partitions be
`Pi_mu` and `Pi_nu`.  If

\[
                         \Pi_\mu=\Pi_\nu,                 \tag{1.3}
\]

then `G` is six-colourable.

#### Proof

The operation `mu` leaves the whole closed opposite side `O` unchanged,
so the colouring of `G/mu` restricts to a colouring of `O` with boundary
partition `Pi_mu`.  Symmetrically, `nu` leaves the whole closed
`K`-side `C` unchanged, and the colouring of `G/nu` restricts to a
colouring of `C` with partition `Pi_nu`.  Under (1.3), permute the
palette on one restriction so that its labelled boundary blocks agree
with the other, and glue. \(\square\)

Consequently a hypothetical counterexample has a strong dynamic
separation property: every boundary state produced by an internal
operation in the locked disk is different from every boundary state
produced by an internal operation in the opposite shore.  This is the
concrete collision which a state-pumping or rural-composition argument
has to force.

### Theorem 3 (planar list-splice from total contraction)

Assume `K` is planar, connected, and has at least two vertices.  Contract
a spanning tree of `K` to one vertex `z`, and let `c` be any
six-colouring of the proper minor `G/K`.  If

\[
 \bigl|c(N_G(x)\cap S)\bigr|\le1
                         \qquad\text{for every }x\in K,   \tag{1.4}
\]

then `G` is six-colourable.

Consequently, in a hypothetical counterexample, every six-colouring of
`G/K` has some literal carrier vertex `x` whose boundary neighbours use
at least two different colours.

#### Proof

The contracted vertex `z` is adjacent to every member of `S=N_G(K)`.
Delete `z` from the coloured minor, retaining the colouring `c` on
`O=G-K`.  For each `x in K`, give `x` the list

\[
 L(x)=\{1,\ldots,6\}-c(N_G(x)\cap S).                       \tag{1.5}
\]

Under (1.4), every list has order at least five.  By the planar
five-choosability theorem, `K` has a proper colouring from these lists.
The list definition makes every edge from `K` to `S` proper, while the
old colouring `c` handles every edge outside `K`.  Gluing the two
colourings therefore six-colours `G`. \(\square\)

Theorem 3 is a genuine infinite-family closure: a rural carrier cannot
remain locked if some total-contraction state is boundary-monochromatic
at every carrier vertex.  Its surviving obstruction is literal but not
yet label-aligned: at least one vertex sees two boundary colours, which
may occur in the same foreign bag or in unrelated bags.

### Theorem 4 (active-face list-splice)

Let the planar carrier `K` have a plane embedding with facial cycle `F`.
Assume every vertex of `K` having a neighbour in `S` lies on `F`.  In a
six-colouring `c` of `G/K`, suppose

\[
 \bigl|c(N_G(x)\cap S)\bigr|\le3
                         \qquad\text{for every }x\in V(F). \tag{1.6}
\]

Then `G` is six-colourable.

Consequently every total-contraction state of a surviving fully rural
society has a facial vertex whose boundary neighbours use at least four
different colours.  If no such vertex exists, some literal external
attachment lies off the proposed active face.

#### Proof

Use the lists (1.5).  Every vertex of `F` has a list of order at least
three by (1.6).  Every vertex inside `F` has no boundary neighbour by
hypothesis, and hence has the full six-colour list, of order at least
five.

Choose an edge `ab` of the facial cycle and choose distinct colours
`alpha in L(a)`, `beta in L(b)`; this is possible because both lists
have order at least three.  Temporarily replace the two lists by
`{alpha}` and `{beta}`.  Thomassen's outer-face list-extension theorem
(two adjacent outer vertices precoloured differently, every other
outer list of order at least three, every interior list of order at
least five) colours `K` from these lists.  As in Theorem 3, the lists
avoid all colours on the corresponding boundary neighbours, so this
colouring glues to `c` on `G-K`. \(\square\)

Unlike a palette-to-label assertion, Theorem 4 does not name which rows
supply the four colours.  It gives a safe structural alternative:
off-face literal attachment, a four-colour facial load, or an immediate
six-colour splice.

### Corollary 5 (two heavy facial vertices are necessary)

Retain the fully rural hypotheses of Theorem 4 and a colouring `c` of
`G/K`.  Let

\[
 B_c=\{x\in V(F):|c(N_G(x)\cap S)|\ge4\}.                 \tag{1.7}
\]

If `G` is not six-colourable, then `|B_c|>=2`.  Moreover, if
`B_c={x,y}` and `xy` is an edge of `F`, then

\[
                         L(x)=L(y)=\{c(z)\},              \tag{1.8}
\]

where `z` is the contracted image of `K`.

#### Proof

Every boundary vertex is adjacent to `z`, so no member of `S` has colour
`c(z)`.  Hence `c(z)` belongs to every list `L(x)`.

If `B_c` is empty, apply Theorem 4.  If `B_c={x}`, precolour `x` with
`c(z)` and precolour either facial neighbour `y` of `x` with a different
colour from its list; `y notin B_c` has a list of order at least three.
Every other facial list has order at least three and every interior list
has order at least five, so the same outer-face extension theorem and
splice colour `G`.

Now suppose `B_c={x,y}` and `xy in E(F)`.  If the two lists admit
distinct representatives, precolour the edge `xy` with them and apply
the theorem again.  Therefore they admit no distinct representatives.
Both are nonempty and both contain `c(z)`, so the two-set Hall condition
fails exactly when both are the same singleton `{c(z)}`.  This proves
(1.8). \(\square\)

Thus a target-free rural contraction state contains either two
nonadjacent heavy portal vertices, at least three heavy vertices, or one
literal facial edge whose ends are both forced to the contraction
colour.  This is the precise dynamic geometry left after list splicing.

## 2. A four-connected rural palette lock

Let `K` be the square-antiprism graph `C_8^2` in its standard plane
embedding.  Its four even vertices bound one square face.  Assign them,
in cyclic order around that face, to

\[
                         A_L, A_R, P_H, P_Q.            \tag{2.1}
\]

Thus the prescribed pairs `(A_L,P_H)` and `(A_R,P_Q)` alternate.

The graph `K` is four-connected.  By the Jordan curve theorem it has no
disjoint `A_L-P_H` and `A_R-P_Q` paths for the alternating order in
(2.1), exactly the rural outcome of the audited locked-two-row theorem.

For a literal local realization, add four outside vertices
`t_L,t_R,t_H,t_Q`, joining each only to its corresponding even portal
vertex.  They may be regarded as the first vertices of four larger
connected path-side/row sets; here they simply witness the four named
portal edges.

Label `C_8^2` cyclically modulo eight and choose the odd-square edge
`e=uv=13`.  This edge is disjoint from the four even portal roots, so
its deletion or contraction does not identify any prescribed portal.
Outside `K`, add five independent
boundary vertices `s_1,...,s_5`, each adjacent to both `u` and `v`.
Consider the explicit boundary state in which the `s_i` have five
distinct colours.  Since `K-{u,v}` is planar, colour it with at most
four of those colours.  In the graph with `e` deleted, give both `u,v`
the sixth colour.  This is a proper six-colouring after choosing the
four-colouring of `K-{u,v}` to avoid the sixth colour.

Colour each of `t_L,t_R,t_H,t_Q` with any colour different from its one
neighbour in `K`.  Thus the displayed boundary state includes the
literal portal edges as well as the five locking vertices.

In every extension of this same boundary state to the displayed graph
with `e` deleted, both `u` and `v` are forced to the sixth colour,
because each sees all five colours on the `s_i`.  Hence this boundary
state does not extend after restoring `e`.  Contracting `e` gives the
same locked state at its contracted image.

The portal order (2.1) and the absence of the protected linkage are
unchanged.  The five colours on `s_i` do not identify `H`, `Q`, or any
other foreign model row; the `s_i` are merely literal boundary vertices
which happen to realize five palette colours in this state.

The example evades Theorem 4 in exactly the permitted way: the locking
vertices attach at the odd-square edge `13`, off the active even-square
face carrying the four named portals.  It therefore witnesses the
off-face-contact branch, rather than refuting the active-face list
splice.

This is a coloured boundary gadget, not a claimed full
seven-contraction-critical `K_7`-minor-free host.  It proves the needed
logical negative: from one internal proper-minor colouring, even in a
four-connected rural carrier with the exact alternating portals, one
cannot infer a labelled rerouting or attach a palette colour to `H` or
`Q`.

## 3. Exact remaining dynamic theorem

For the locked rural carrier, a genuine continuation must prove one of:

1. some transition partition in (1.2) forces a literal fixed linkage in
   `K` after a label-preserving rerouting;
2. the same labelled partition is produced by a faithful operation on
   an actual opposite shore, contradicting (1.1) by gluing; or
3. the rural disk containing (2.1) composes with every other expansion
   society using one fixed global pair of literal apex vertices.

The palette-lock example rules out replacing item 2 by a comparison of
colour names or Kempe-path colours.  What remains is an equality-state
exchange across the actual adhesion `S`, not a local planar recolouring
lemma.
