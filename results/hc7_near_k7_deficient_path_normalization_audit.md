# Audit: deficient-bag normalization attempt

## Verdict

**GREEN as a partial structural normalization; RED as `P1`.**  The
strengthened Theorem 1.3 is valid: every nonsingleton deficient bag in the
deficient-first lexicographic model is an induced path, and its four
neutral portal classes are singleton sets split `2+2` between the two
endpoints.  It still does not align palette colours with nonsingleton
foreign model bags or produce a rural apex pair.

## Checks

1. A detachable part of the deficient bag `A` with no monopolized neutral
   label can be deleted from the model.  If it monopolizes exactly one
   neutral bag `U_i`, transferring it into `U_i` preserves all labels:
   an old `A-U_i` edge connects it to `U_i`, and an actual edge across the
   connected partition `X | A-X` restores the new `A-U_i` adjacency.
   Deficient-first lexicographic minimality therefore forces at least two
   owners.
2. Monopoly sets of disjoint detachable parts are disjoint.  Since `A`
   has exactly four required neutral neighbours, there are at most two
   such parts.

## Strengthened Theorem 1.3

Let `X dotcup Y=A` be any partition into two nonempty connected sets.
Both are detachable.  Their monopoly sets are disjoint and each has order
at least two; since only four neutral labels exist, both sets own exactly
two labels and together own all four.  Therefore no portal set can meet
both sides of any connected bipartition.

Fix any spanning tree `T` of `G[A]`.  The two sides of every tree edge are
connected.  If a portal set contained two vertices, an edge of their
unique `T`-path would separate them, contradicting the preceding
conclusion.  Hence every neutral portal set is a singleton.

Every leaf `ell` of `T` is detachable because `T-ell` remains connected.
It therefore owns at least two singleton portal labels.  A tree on at
least two vertices has at least two leaves, and distinct leaves own
disjoint label sets.  Four labels force exactly two leaves, each owning
exactly two labels.  Since `T` was arbitrary, every spanning tree of
`G[A]` is a path.

If `G[A]` had a vertex of degree at least three, three incident edges form
a forest and extend to a spanning tree retaining degree at least three at
that vertex, a contradiction.  Thus `G[A]` has maximum degree at most two
and, being connected, is a path or a cycle.  A cycle has at least three
vertices; every singleton deletion from it is detachable and would own at
least two disjoint labels, requiring at least six labels.  Hence the cycle
case is impossible.

The path is induced because `G[A]` is the induced subgraph on the bag.  Its
unique spanning tree has the two endpoints as leaves, and the preceding
equality allocates two singleton portal classes to each endpoint and all
four labels in total.  This proves the full `2+2` assertion, including the
order-two path case.

The older block-tree conclusions remain valid but are now redundant:

3. Leaf-block interiors are detachable.  Hence the block-cutvertex tree
   has at most two leaves and is a path.  A non-cut vertex of a
   nonseparable block is itself detachable; the two-owner count permits at
   most two such vertices per block.  The stated end/internal block order
   bounds follow.
4. Along nested descendant lobes the monopoly sets are monotone subsets of
   the four neutral labels and all have order at least two.  Hence there
   are at most two strict changes.  In a constant interval, a third block
   vertex or an off-chain component is a detachable part whose owners
   occur in the larger lobe but not the smaller one.  This contradicts
   constancy, so every intervening block is a literal bridge and the
   interval induces a path.
5. An internal path vertex cannot meet a common owner bag: that occurrence
   would lie outside the deeper lobe even though the entire portal class
   is asserted to lie inside it.

With the usual convention that a 2-connected graph has at least three
vertices, the sentence "if `G[A]` is two-connected, then `|A|<=2`" means
that the two-connected case is impossible; it should not be read as
declaring a `K_2` two-connected.

## Exact failure of `P1`

The note correctly rejects the tempting next step.  Contracting foreign
branch bags does not make them monochromatic objects in the original
graph.  A list-colouring of the path combined with a colouring of the
partially contracted quotient colours only that quotient, not `G`.
Moreover one palette colour may occur in several foreign bags.  Thus the
singleton-shell palette-to-label theorem cannot be invoked.

The result now supplies a canonical induced bipartite carrier whenever the
deficient bag is nonsingleton, with exact literal `2+2` neutral ownership.
It still does not make the six foreign bags singleton or monochromatic,
does not align the fifth palette row, and does not identify one common
rural apex pair.  Therefore it is not an end-to-end proof of `P1`.
