# Saturation of every cut in a minimal contraction forest

**Status:** proved and independently audited.

This is a uniform colouring invariant behind the leaf-rooted chromatic-drop
construction.  It applies simultaneously to every edge of the minimal
forest and does not use boundary labels, packet states, or a chosen minor
model.

## 1. Abstract cut-saturation theorem

### Theorem 1.1 (minimal contraction cut saturation)

Let `G` be a graph, let `F` be a forest in `G`, and let `q>=2`.  Suppose
`F_0 \subseteq F` is nonempty, the graph

\[
                             K=G/F_0
\]

is `q`-colourable, and no proper subset of `F_0` has this property.  For
an edge `e in F_0`, put

\[
                         H_e=G/(F_0-\{e\}).
\]

The image of `e` in `H_e` is an edge `x_e y_e`; contracting it gives one
vertex `z_e` of `K`.  Fix any proper `q`-colouring `phi` of `K`, and write
`c=phi(z_e)`.  Then each of `x_e,y_e` has a neighbour of every colour in

\[
                              [q]-\{c\}.                \tag{1.1}
\]

Equivalently, if `T` is the component of the forest `(V(G),F_0)`
containing `e`, then each of the two components of `T-e`, after its
vertices are contracted together in `H_e`, has an external contact of
every colour different from the colour of the image of `T` in `K`.

### Proof

Minimality of `F_0` says that `H_e` is not `q`-colourable.  Every neighbour
outside `\{x_e,y_e\}` of either endpoint maps, after contracting
`x_e y_e`, to a neighbour of `z_e` in `K`.  Consequently no such neighbour
has colour `c` under `phi`.

Suppose, for example, that `x_e` has no neighbour of some colour
`d ne c`.  Keep the colouring `phi` on every vertex other than `z_e`,
give `x_e` colour `d`, and give `y_e` colour `c`.  This is proper:

* no neighbour of `x_e` has colour `d` by assumption;
* no neighbour of `y_e` outside `x_e` has colour `c`; and
* the edge `x_e y_e` has differently coloured ends.

This would be a `q`-colouring of `H_e`, a contradiction.  The argument
with the endpoints interchanged proves (1.1) for both.  \(\square\)

### Corollary 1.2 (literal leaf saturation)

In the setting of Theorem 1.1, let `u` be a leaf of a nontrivial component
`T` of `(V(G),F_0)`, and let `e` be its incident forest edge.  In `H_e`
the vertex `u` remains a literal original vertex.  For every `q`-colouring
of `K`, it has a neighbour of every colour other than the colour of the
contracted image of `T`.

The same statement holds for the connected carrier represented by
`T-u`.

### Proof

No edge of `F_0-\{e\}` is incident with `u`, so it remains literal.  Apply
Theorem 1.1 to the two sides of `e`.  \(\square\)

### Corollary 1.3 (exact chromatic ladder)

For every `e in F_0`,

\[
                         \chi(K)=q,
                  \qquad \chi(H_e)=q+1.               \tag{1.2}
\]

### Proof

The graph `H_e` is not `q`-colourable by minimality, while any
`q`-colouring of `K` lifts to a `(q+1)`-colouring of `H_e` by giving one
end of `x_e y_e` one fresh colour.  Hence `chi(H_e)=q+1`.  If `K` were
`(q-1)`-colourable, the same lift would `q`-colour `H_e`, a contradiction.
Thus `chi(K)=q`.  \(\square\)

## 2. The critical-colour branch

The cut-saturation theorem controls contacts with individual colour
classes.  When deletion of the contracted image lowers the terminal
chromatic number by one, the common-neighbour rooted theorem upgrades
those palette contacts to one labelled clique model.

### Corollary 2.1 (every critical forest edge yields a two-rooted model)

Retain the notation of Theorem 1.1.  Suppose in addition that

\[
                            \chi(K-z_e)=q-1.
                                                               \tag{2.1}
\]

Then the common-neighbour set

\[
 X_e=N_{H_e}(x_e)\cap N_{H_e}(y_e)\cap V(K-z_e)
\]

is colourful in the `(q-1)`-chromatic graph `K-z_e`.  Consequently, if
Strong Hadwiger holds for `q-1`, then `H_e` contains a `K_{q+1}` model
whose first two bags are the singleton vertices `\{x_e\},\{y_e\}`.

### Proof

Under the canonical identification of all other quotient vertices, the
graph obtained from `H_e` by deleting `x_e,y_e` is exactly `K-z_e`.
Apply the uniform common-neighbour rooted theorem (Theorem 2.3 of
`hc7_leaf_rooted_chromatic_drop.md`) with `k=q-1`.  \(\square\)

## 3. HC7 consequence and exact limit

In the four-colour two-full-shore residue, take the minimal forest `F_0`
from the leaf-rooted chromatic-drop theorem.  Here `q=5`; every predecessor
`H_e` is exactly six-chromatic and the terminal graph `K=G/F_0` is exactly
five-chromatic.  Therefore:

1. every side of every edge of `F_0` meets all four colour classes other
   than the colour of its terminal contraction image, in every
   five-colouring of `K`; and
2. whenever one such image `z_e` satisfies `chi(K-z_e)=4`, the predecessor
   has a `K_6` model with the two sides of `e` as its two named singleton
   bags.  On expansion to the original graph, those bags become the two
   literal connected sides of the forest cut.

This is stronger than the existence of one leaf-rooted drop edge: it gives
one simultaneous, colouring-independent duty condition on every cut of
the minimal forest.  It still does **not** preserve a seventh connected
carrier.  Nor does it imply that some contraction image is critical in
the terminal five-chromatic graph.  Those are the exact two remaining
composition questions; neither is claimed here.
