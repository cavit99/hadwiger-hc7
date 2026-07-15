# Three-rooted small-`K_4` composition

## Status

Proved and independently cold-audited.  See
[`hc7_three_rooted_small_k4_composition_audit.md`](hc7_three_rooted_small_k4_composition_audit.md).

This is a uniform composition criterion for the three forced replacements
over a common five-set.  The unresolved extraction question is whether the
three exact support-six models force the rooted `K_4` below, or instead
force a coherent global pair.

## Theorem

Let `G` be seven-connected.  Let `a,p,q` be three distinct vertices and let
`D_1,D_2,D_3,D_4` be a `K_4` model in
`G-{a,p,q}` whose total support has order at most five.  If each of
`a,p,q` has a neighbour in every `D_i`, then `G` has a `K_7` minor.

## Proof

Put `W=V(D_1) union ... union V(D_4)` and `H=G-W`.  Since `|W|<=5` and
`G` is seven-connected, `H` is two-connected: it contains the three
distinct vertices `a,p,q`, and deleting no vertex or any one vertex from
`H` amounts to deleting at most six vertices from `G`.  In particular the three
specified vertices `a,p,q` root a `K_3` model in `H`: there are pairwise
disjoint, pairwise adjacent connected subgraphs `R_a,R_p,R_q` containing
`a,p,q`, respectively.  This is the rooted-triangle lemma (equivalently,
apply a two-fan from the third root to a path between the other two).

Every `R_r`, for `r in {a,p,q}`, is adjacent to every `D_i`, because it
contains `r` and `r` has a neighbour in `D_i`.  Thus

```text
D_1,D_2,D_3,D_4,R_a,R_p,R_q
```

are seven pairwise disjoint, connected, pairwise adjacent branch sets.
They form a `K_7` model.  \(\square\)

## Application to a common five-set

Let `U` be a five-set disjoint from `{a,p,q}`.  Suppose each of

```text
U union {a},   U union {p},   U union {q}
```

supports a `K_5` model.  If `G[U]` contains a `K_4` model whose four bags
are each contacted by all three roots, the theorem closes this branch
immediately.  Notice that neither the three support statements alone nor
seven-connectivity restricted to the eight displayed vertices supplies
those simultaneous labelled contacts; the extraction must use the other
forced replacements, the exterior of the eight-set, or contraction-
critical state transitions.

## Sharpness of the extraction step

The three support statements alone do not force the common rooted `K_4`.
Here is a transparent eight-vertex obstruction.  Take disjoint sets

```text
Q={u_1,u_2,u_3},   T={x,y},   R={a,p,q}.
```

Make `Q` a triangle, put in every edge from `Q` to `T` and every edge from
`T` to `R`, and put in no other edges.  Let `U=Q union T`.  For every
`r in R`, the six-set `U union {r}` supports a `K_5` model: use the edge
bag `{x,r}` and the four singleton bags `u_1,u_2,u_3,y`.  None of these
six-sets contains a literal `K_5`.

On the other hand, every root in `R` has neighbourhood exactly `{x,y}`
inside `U`.  Four disjoint bags in `U` cannot all meet `{x,y}`, so no
`K_4` model in `U` is contacted by all three roots.  The eight-vertex
graph has no `K_7` minor: seven nonempty disjoint branch sets supported on
at most eight vertices include at least six singleton bags, and those six
vertices would form a literal `K_6`, while this graph has clique number
four.

This is only a local counterarchitecture, not an `HC_7` counterexample; it
is not seven-connected.  Its two-vertex middle layer `{x,y}` identifies
the exact alternative a global theorem must exploit: outside linkage must
either break this common two-gate bottleneck and create the rooted `K_4`,
or make the same pair coherent beyond the three displayed models.

## Dependency

The rooted-triangle fact is Lemma 1.1 of
[`hc7_global_split_model_composition.md`](hc7_global_split_model_composition.md),
specialized to three singleton roots in a two-connected graph.
