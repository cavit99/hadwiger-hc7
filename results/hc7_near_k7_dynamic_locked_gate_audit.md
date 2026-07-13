# Independent audit: dynamic states at a locked rural gate

## Verdict

**GREEN.**  Equality partitions are exactly sufficient for palette
alignment and gluing, the closed-side restrictions under internal minor
operations are valid, both planar list-splice theorems and the
heavy-vertex sharpening have the stated hypotheses needed for the cited
list-colouring results and glue safely, and the square-antiprism gadget realizes the claimed
deletion/contraction palette lock without creating an improper edge at
either endpoint.

## 1. Closed sides and equality partitions

With `S=N_G(K)`, the graphs

\[
                 C=G[K\cup S],\qquad O=G-K
\]

cover `G`, intersect exactly in `S`, and no edge has one end in
`K` and the other in `O-S`.  Thus two proper side colorings which agree
on `S` glue to a proper coloring of `G`.

Suppose two side colorings induce the same labelled equality partition
of `S`.  Each boundary block has one color on each side, and distinct
blocks have distinct colors.  Mapping the color of every block on one
side to its color on the other is therefore a bijection between two
equally sized subsets of the six-color palette.  It extends to a
permutation of all six colors.  After that permutation the colorings
agree vertex by vertex on `S`, so equality partitions—not color names—
are sufficient for gluing.

This proves `Ext(C,S) cap Ext(O,S)=empty` in a non-six-colorable host.
For an edge `e` internal to `K`, a six-coloring of the proper minor
`G/e` restricts to `C/e` and unchanged `O` with the same boundary
partition.  If that state extended to `C`, the preceding gluing would
color `G`.  Splitting the contracted vertex into the two equal-colored
ends gives the corresponding coloring of `G-e`; conversely, in any
six-coloring of `G-e` the ends must be equal, or restoring `e` would
already color `G`.

## 2. Crossed-state splice

An operation strictly inside `K` leaves the whole closed opposite side
`O` unchanged.  An operation strictly in `G-(K union S)` leaves `C`
unchanged, even when its contracted vertex has neighbours in `S`.
Therefore equal boundary partitions from colorings of the two proper
minors give an `O` coloring on one side and a `C` coloring on the other.
Palette alignment as above glues them to a six-coloring of `G`.

The conclusion is quantified correctly: in a hypothetical counterexample
no state from any chosen internal operation/coloring on one shore may
equal a state from any chosen operation/coloring on the other.

## 3. Planar list-splice from a total contraction

Contracting a spanning tree of the connected carrier `K` contracts all
of `K` to one vertex `z`; because `|K| at least 2`, this is a proper
minor.  Every boundary vertex in `S=N_G(K)` is adjacent to `z`, although
the proof does not need the colour of `z` after it restricts the minor
colouring to `O=G-K`.

For each literal carrier vertex `x`, the list

\[
       L(x)=\{1,\ldots,6\}-c(N_G(x)\cap S)
\]

excludes exactly the colours appearing on all of its boundary
neighbours.  Under (1.4) it has size at least five.  Since `K` is
planar, planar five-choosability supplies a proper `L`-colouring of
`K`.  Edges internal to `K` are proper by that colouring, edges outside
`K` are proper in the restriction of `c`, and every crossing edge has
its `K`-endpoint coloured outside the colour set on its boundary
neighbours.  Thus the splice is proper.  The stated contrapositive is
quantified correctly for every six-colouring of `G/K` in a
non-six-colourable host.

This conclusion is deliberately literal rather than row-labelled: the
two boundary colours witnessed at one carrier vertex need not belong
to two prescribed model bags.

## 4. Active-face list-splice

A facial cycle can be designated as the outer facial cycle by changing
which face of the spherical embedding is viewed as outer.  Under the
attachment hypothesis, every off-cycle vertex then has no neighbour in
`S`, so its list is the full six-colour palette (in particular, has
size at least five).  Condition (1.6) gives every vertex of the outer
cycle a list of size at least three.

Choose an edge `ab` of the facial cycle.  Lists of size at least three
contain choices `alpha in L(a)` and `beta in L(b)` with
`alpha != beta`; replacing the two lists by the distinct singleton
lists satisfies the precoloured-edge hypothesis of Thomassen's
outer-face extension theorem.  Every other outer list has size at least
three and every interior list has size at least five, so that theorem
colours `K`.  The same crossing-edge check as in Section 3 proves that
this colouring glues to `c` on `G-K`.

In the intended application `K` is an exterior component and hence is
connected.  Even without that contextual convention, any component
not containing the facial cycle has full lists and can be coloured
separately by planar five-choosability, so it creates no hidden gap.
The advertised alternative is the exact contrapositive: in a surviving
state either an attachment vertex lies off the selected face or some
facial vertex sees at least four boundary colours.

As in Theorem 3, this is not a palette-to-row identification and does
not by itself produce a prescribed linkage.

## 5. Heavy facial vertices

In a colouring of `G/K`, the contracted vertex `z` is adjacent to every
boundary vertex in `S`.  Properness therefore excludes `c(z)` from the
colour set on `N_G(x) cap S` for every literal `x in K`, and hence
`c(z)` lies in every list `L(x)`.  In particular, even a heavy facial
vertex has a nonempty list.

If there is exactly one heavy vertex `x`, all other facial lists have
size at least three.  Precolour `x` with `c(z)` and choose a different
colour from the size-at-least-three list of either facial neighbour of
`x`.  This gives the required distinctly precoloured outer edge, while
all remaining outer and inner list bounds are unchanged.  Thomassen's
theorem and the already audited splice therefore rule out zero or one
heavy vertex in a non-six-colourable host.

If the only two heavy vertices `x,y` are adjacent, distinct
representatives of `L(x),L(y)` again give a valid precoloured edge and
the same splice.  Failure of distinct representatives for two nonempty
sets is precisely the Hall failure `|L(x) union L(y)|<2`.  Since both
sets contain `c(z)`, this is equivalent to
`L(x)=L(y)={c(z)}`.  The resulting three alternatives—two nonadjacent
heavy vertices, at least three heavy vertices, or an adjacent forced
singleton pair—are exactly the logical residue; no row identity is
inferred from them.

## 6. Square-antiprism rural carrier

The graph `C_8^2` is the square-antiprism graph.  It is planar and
four-connected, and its four even vertices bound a square face.  Placing
`A_L,A_R,P_H,P_Q` cyclically on that face makes the two prescribed pairs
alternate.  The planar cross obstruction therefore forbids disjoint
paths for those pairs.

Fix the specified odd-square edge `e=uv=13`, which is disjoint from the
four even portal roots.  Give the five common neighbours
`s_1,...,s_5` five distinct colors from a six-color palette.  The planar
graph `K-{u,v}` has a proper coloring with at most four abstract colors;
relabel those colors injectively into any four of the five colors already
used on the `s_i`.  This choice is independent of which five palette
colors occur on the boundary and avoids the unique sixth color.

In the graph with `e` deleted, color both `u,v` with that sixth color.
Every neighbour they have in `K-{u,v}` uses one of the first five
colors, as does every `s_i`, and the only edge between `u,v` was deleted.
Hence all edges incident with `u` or `v` are proper.  Each leaf portal
vertex `t_L,t_R,t_H,t_Q` can then be assigned any color different from
its unique carrier neighbour; if that neighbour is `u` or `v`, choose
one of the first five.

For every extension of the resulting fixed boundary state, each of
`u,v` sees all five distinct boundary colors and is forced to the sole
sixth color.  Restoring `uv` is therefore impossible.  After contracting
`uv`, the contracted image is forced to the same sixth color and the
same coloring of `K-{u,v}` and the leaf portals extends properly.

## Scope

The gadget preserves the alternating portal order and proves that one
proper-minor palette state need not yield a labelled linkage or identify
a color with a foreign row.  It is not asserted to be contraction-
critical, `K_7`-minor-free, or part of a global two-apex host.  A valid
continuation must collide labelled equality partitions across actual
opposite shores or prove one globally coherent rural expansion.
