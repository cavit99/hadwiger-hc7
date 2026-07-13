# Spanning-only minimality does not normalize the deficient bag

## Status

This unbounded family falsifies the stronger but tempting claim

\[
 \text{``a spanning-minimal deficient bag in a }K_7^\vee
       \text{ model is a path.''}                            \tag{0.1}
\]

The valid deficient-path theorem minimizes over **nonspanning** labelled
models, so that a zero-owner part may be left outside the model.  If the
comparison is restricted to spanning models, arbitrary zero-owner filler
trees are forced to remain in the deficient bag.

The family is `K_7`-minor-free and has a spanning `K_7^vee` model.  It is
not seven-connected or contraction-critical; its order-one adhesion is
exactly the hypothesis which those global assumptions must eliminate.

## 1. Construction

Let `T` be any finite rooted tree, with root `a`.  Add six vertices

\[
                         B,C,U_1,U_2,U_3,U_4.                \tag{1.1}
\]

Make these six vertices a clique.  Join `a` to `U_1,...,U_4` and to
neither `B` nor `C`.  No vertex of `T-a` has a neighbour outside `T`.
Call the resulting graph `G_T`.

### Proposition 1.1 (forced arbitrary deficient tree)

The seven bags

\[
                T,\{B\},\{C\},\{U_1\},\ldots,\{U_4\}       \tag{1.2}
\]

form a spanning labelled `K_7^vee` model with deficient pairs `AB,AC`.
Moreover, in **every** spanning labelled model on this fixed graph, the
bag with label `A` contains all of `T`.  Consequently the first bag can be
an arbitrarily long or arbitrarily branching tree even after minimizing
its order among spanning labelled models.

#### Proof

The displayed model assertion is immediate: the six singleton bags form
a clique, while the connected bag `T` sees precisely the four required
neutral labels.

Consider any spanning labelled `K_7^vee` model.  The six foreign bags
form a `K_6` model.  Across the one-separation at `a`, all foreign bags
not containing `a` must lie on the same side.  Indeed, two such bags on
opposite sides would have no edge between them.  They cannot all lie on
the tree side, since a tree has no `K_3` minor, let alone the clique minor
left after deleting the possible `a`-bag.  Hence the five (or six)
foreign bags avoiding `a` lie in the core side.

Every such bag contains one of the six clique vertices in (1.1).  If the
foreign bag containing `a` contained no clique vertex, it could meet
other foreign bags through only the four literal edges from `a` to the
`U_i`, fewer than the five adjacencies it requires.  Thus it too contains
a clique vertex.  Disjointness and equality of the two counts force
exactly one clique vertex into each foreign bag, leaving no clique vertex
for the `A` bag.

The root `a` cannot lie in a foreign bag.  If it did, the `A` bag, which
has no clique vertex, would lie wholly in one component of `T-a`.  It
would then be adjacent to at most the single foreign bag containing `a`,
contradicting the four required `A-U_i` adjacencies.  Thus `a` lies in
the `A` bag.

Finally a vertex of `T-a` cannot lie in a different bag from `a`.  The
component of that vertex in `T-a` reaches the rest of the graph only
through `a`; a foreign bag containing it but not `a` could not be
connected to its forced clique vertex.  Spanningness therefore puts every
vertex of `T` in the `A` bag.  \(\square\)

### Proposition 1.2 (`K_7`-minor exclusion)

Every `G_T` is `K_7`-minor-free.

#### Proof

The graph is a one-sum at `a` of the seven-vertex graph `K_7^vee` and
the branches of the tree `T`.  A clique minor of order at least three
cannot use branch sets essentially on both sides of a one-separation:
any branch set wholly in a tree branch sees the rest only through the
unique bag containing `a`, and hence cannot be adjacent to the other five
bags of a `K_7` model.  Deleting all such inessential tree vertices from
a hypothetical model leaves a `K_7` model in the literal seven-vertex
`K_7^vee` core.

That core has no `K_7` minor: on seven vertices, a seven-bag minor model
would have seven singleton bags and hence would require a literal `K_7`,
but the two edges `aB,aC` are absent.  \(\square\)

## 2. Exact quantifier boundary

Every proper branch of `T-a` is a detachable zero-owner part of the
`A` bag.  Under nonspanning lexicographic minimization it can simply be
removed from the model, which is why the audited deficient-path theorem
is unaffected.  Under spanning-only minimization it cannot be removed or
transferred, and Proposition 1.1 forces it to stay.

The ambient neighbourhood of such a branch is the singleton `{a}`.
Thus seven-connectivity detects the obstruction immediately.  The family
does not refute a theorem which first returns an actual low-order adhesion
and only applies path normalization after that adhesion has been excluded.
It does refute any proof which silently keeps the word *spanning* during
the deletion step in the two-owner rule.
