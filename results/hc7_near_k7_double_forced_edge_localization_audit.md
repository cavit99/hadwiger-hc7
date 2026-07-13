# Independent audit: localization of a double-forced state

## Verdict

**GREEN after adding `|F|>=4` to Theorem 1.**  With that necessary
hypothesis, contraction of the facial edge yields a valid plane graph
with an outer cycle to which Thomassen's precoloured-edge extension
theorem applies.  The resulting colouring expands safely both to the
edge contraction and to the edge deletion while preserving the full
labelled boundary state.  Corollary 2 already earns `|F|>=4` from its
four distinct portal representatives.

## 1. Facial-edge contraction

Contract the outer edge `xy` in the displayed plane embedding and
suppress loops and parallel edges.  Since `|F|>=4`, the image of the old
outer cycle has length at least three.  The simplified contraction of an
edge in a four-connected graph remains sufficiently connected for its
outer facial boundary to be a cycle; directly in the inherited drawing,
the contracted boundary walk is the cycle `F/xy` after the harmless
parallel-edge suppression.

An internal face incident with `xy` may collapse and expose an original
interior vertex on the new outer face.  This causes no list gap: every
original vertex strictly inside `F` has the full six-element list.  The
remaining original vertices of `F-{x,y}` have lists of size at least
three by hypothesis.  Thus every outer vertex of `K'=K/xy` other than
the contracted image `p` has list size at least three, and every vertex
remaining interior has list size at least five.

The original statement's appeal to “the locked application” did not
formally supply `|F|>=4` to Theorem 1 itself; four-connected plane graphs
can have a triangular outer face.  The added explicit hypothesis closes
that scope issue.

## 2. Thomassen extension and gluing

Give `p` the singleton list `{alpha}`.  Either neighbour `q` of `p` on
the new outer cycle comes from a nonheavy old facial vertex or has a full
interior list, so `|L(q)|>=3`.  Since every list contains `alpha`, one can
choose `beta in L(q)-{alpha}`.  The adjacent singleton lists
`{alpha},{beta}` are distinct, every other outer list has size at least
three, and every interior list has size at least five.  Thomassen's
outer-face extension theorem therefore colours `K'` with
`p=alpha,q=beta`.

For a vertex other than `p`, its list excludes all colours used by the
fixed colouring `c` on its literal neighbours in `S`.  For `p`, the two
old lists `L(x)=L(y)={alpha}` show that `alpha` avoids the colour of every
boundary neighbour of either endpoint.  Hence the `K'` colouring glues
to `c` on `G-K` and gives a proper colouring of `G/xy`.

Splitting `p` back into `x,y` and assigning both colour `alpha` preserves
every edge represented at `p`; a common old neighbour is non-`alpha`
because it was adjacent to `p`.  Deleting only the mutual edge `xy`
makes the equal endpoint colours proper, yielding a colouring of
`G-xy`.  No boundary colour changes, so both operations realize exactly
the total-contraction equality partition on the full actual adhesion.

## 3. Corollary

The audited harmonica gate reduces a noncolourable exactly-two-heavy
state in the stated four-connected carrier to two singleton lists
`{alpha}`.  Four distinct literal portal representatives on `F` imply
`|F|>=4`.  If the two forced vertices are adjacent, Theorem 1 applies;
otherwise the nonadjacent pair is retained.  These are precisely the two
outcomes of Corollary 2.

## Scope

Localization replaces the whole-carrier operation by one named internal
edge operation but does not create the same partition from an opposite
shore.  The crossed-state collision, nonadjacent forced-pair case, and
global rural compatibility remain open.
