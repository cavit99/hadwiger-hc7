# Audit of the global support-six contraction dichotomy

## Verdict

**GREEN.**  The normal forms, contraction/separator dichotomy, and palette
conclusion in
[`hc7_global_support_six_contraction_dichotomy.md`](hc7_global_support_six_contraction_dichotomy.md)
are correct.  The small-order convention for connectivity and the mutual
exclusivity of the structural alternatives are both harmless and are made
explicit below.

## 1. Support-six normal forms

Five nonempty disjoint bags with total support six have orders
`(2,1,1,1,1)`.  Connectivity makes the two-vertex bag an edge `xy`; the
four singleton bags form a literal clique `Q` of order four.  Every
`q in Q` contacts the edge-bag, so it is adjacent to at least one of `x,y`
and hence `D_x cap D_y` is empty.

Neither deficiency set can be empty.  If, for example, `D_x` were empty,
then `Q union {x}` would be a literal `K_5` disjoint from the chosen
literal-`K_5` transversal `P`.  Thus `D_x,D_y` are nonempty disjoint subsets
of a four-set.  After interchanging `x,y`, their orders and the remaining
common-contact order are exactly

\[
 (1,1,2),\quad(1,2,1),\quad(1,3,0),\quad(2,2,0).
\]

This is exhaustive and uses no hidden induced-subgraph assumption.

## 2. Exterior and contraction dichotomy

The support `W=Q union {x,y}` has order six.  Seven-connectivity makes
`G-W` connected.  It is nonempty, and every vertex of `W` has a neighbour
outside `W`: minimum degree is at least seven, while a vertex has at most
five neighbours inside `W`.

The only small-order point in the contraction argument is valid.  A
seven-connected graph has at least eight vertices; if this `G` had exactly
eight, minimum degree seven would force `G=K_8`, contradicting
`K_7`-minor-freeness.  Hence `|G|>=9` and `H=G/xy` has at least eight
vertices.  If `H` is not seven-connected, it therefore has a separator
`T` of order at most six.

The contracted vertex `z` must lie in `T`.  Otherwise the adjacent split
vertices `x,y` replace `z` inside its one component of `H-T`; this cannot
join that component to any other component, so the same `T` would separate
`G`, contrary to seven-connectivity.  With `z in T`,

\[
 S=(T-\{z\})\cup\{x,y\}
\]

separates `G` and has order `|T|+1<=7`.  Seven-connectivity forces equality,
and partitioning the components of `G-S` into two nonempty groups gives the
claimed actual seven-separation.

The alternatives are mutually exclusive as well as exhaustive.  If an
actual seven-separation with `x,y` in its boundary exists, replacing
`x,y` by `z` yields a six-vertex separator of `H`, with both open shores
still nonempty.  Thus that separation exists only when `H` is not
seven-connected.

## 3. Critical coloring conclusion

In a minor-minimal `HC_7` counterexample, the proper minor `H` is
six-colourable.  A colouring of `H` using at most five colours would pull
back to `G-xy` with `x,y` sharing the colour of `z`; recolouring one endpoint
with a fresh sixth colour would then properly six-colour `G`.  Therefore
`chi(H)=6`.

Fix any six-colouring and let `alpha` be the colour of `z`.  Pulling it back
colours both `x,y` with `alpha` and is proper except at `xy`.  If `x` missed
one of the other five colour classes `beta`, recolouring `x` with `beta`
would resolve `xy` without creating a monochromatic edge, again
six-colouring `G`.  Hence `x` contacts every non-`alpha` class; the identical
argument applies independently to `y`.  Since `chi(H)=6`, all six classes
are nonempty.

## 4. Trust boundary

The result gives a normal form and a valid handoff only.  It neither pulls a
two-vertex transversal through the contraction nor assigns the five colour
contacts to prescribed model bags.  No such stronger conclusion is used in
the proof.
