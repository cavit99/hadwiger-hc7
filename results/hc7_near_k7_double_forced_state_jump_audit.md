# Independent audit: double-forced two-block state jump

## Verdict

**GREEN.**  The two-block contraction is a proper minor under the stated
nontrivial-side hypothesis, the total-contraction boundary state has
exactly `q-1` labelled equality blocks, palette alignment is legitimate,
and the two contracted vertices are forced to the same remaining colour
while retaining a literal edge.  The tree-cut corollary has exactly the
scope needed to invoke the theorem.  Extra edges between the two sides
do not affect the argument; a two-vertex carrier correctly yields no
eligible tree cut.

## 1. Properness and the retained two blocks

Contract a spanning tree inside each of the nonempty connected sets
`X,Y`, without contracting an edge between them.  At least one side has
at least two vertices, so at least one genuine edge contraction occurs
and the resulting graph `M` is a proper minor of `G`.  The two images
`a,b` remain distinct.  An old `XY` edge becomes an `ab` edge, so they
are adjacent.

Additional `XY` edges merely become parallel copies of the same `ab`
edge and are suppressed when the minor is viewed as simple.  They cannot
identify `a,b` or invalidate their adjacency.  Internal non-tree edges
only become loops within a contracted side and are discarded in the
usual minor operation.

If `|K|=2` with `K={x,y}`, the only partition separating the forced pair
has two singleton sides.  It is deliberately excluded: contracting the
two singleton blocks would perform no operation and would return `G`,
not a proper minor.  Thus the theorem does not hide a two-vertex edge
case.

## 2. Exact boundary partition

Every member of `S=N_G(K)` is adjacent to the total-contraction vertex
`z`.  Hence the proper colouring `c` uses no colour `alpha=c(z)` on
`S`.  The literal neighbours of `x` appearing in (1.1) witness every
one of the other `q-1` colours on `S`.  Therefore `c|S` uses exactly
those `q-1` colours and induces exactly `q-1` nonempty equality blocks.
The witnesses at `y` give the same full collection for the second
contracted block.

If a colouring `d` of `M` induces the same labelled equality partition,
then it also uses exactly `q-1` colours on `S`.  Mapping the colour of
each labelled `d`-block to the colour of the corresponding `c`-block is
a bijection on `q-1` palette colours and extends to a permutation of the
full `q`-colour palette.  After this permutation, `d` and `c` agree at
every literal boundary vertex, and the sole unused colour on `S` is
`alpha`.

## 3. Forced colours of the contracted vertices

Because `x in X`, every old edge from `x` to `S` survives as an edge
from `a` to the same boundary vertex.  These neighbours witness all
`q-1` colours different from `alpha`, so properness forces
`d(a)=alpha`.  The corresponding literal witnesses at `y in Y` force
`d(b)=alpha`.  The retained `ab` edge then contradicts properness.  This
proves exclusion of the total-contraction equality partition from the
entire colouring-state family of the two-block minor, not just failure
of one chosen colouring to extend.

## 4. Tree cuts

Deleting an edge on the `x-y` path of a spanning tree of `K` produces
two nonempty tree components, with `x` and `y` on opposite sides.  Each
side is connected in `G[K]`, and the deleted tree edge is a literal edge
between them.  If either side has order at least two, contracting the two
sides performs at least one contraction and Theorem 1 applies.  When
`K` has two vertices, the unique path edge leaves two singleton sides,
so Corollary 2 is correctly vacuous.

Edges of `G[K]` beyond the spanning tree may cross the same cut, but—as
above—they only reinforce adjacency of the two contracted images.  They
do matter for any later attempt to glue uncontracted sides, exactly as
the note's final warning states, but not for this state-exclusion result.

## Scope

Every eligible internal tree cut produces a faithful proper minor whose
boundary-state family avoids the old `q-1`-block partition.  The result
does not produce that partition on an opposite shore, a common state for
crossed gluing, or a separator across which independently coloured
uncontracted pieces already agree.
