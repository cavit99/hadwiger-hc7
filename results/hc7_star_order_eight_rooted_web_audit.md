# Internal audit of the exact order-eight rooted-web theorem

**Verdict:** GREEN for the exact revision audited.

## Audited revision

- theorem file: `results/hc7_star_order_eight_rooted_web.md`
- SHA-256: `d02a82cd15ba652696683f79c171f448d1bbeb9ec71ae5f78fb594dffde5c08f`

This is an internal mathematical audit, not external peer review.  It checks
the repaired formal hypotheses, both prescribed linkages, the use of the
Two Paths theorem, every passage from the web completion back to the
spanning subgraph, the role of the virtual edge, the image of the second
five-clique, the exclusion of an outer-root third vertex, and the explicit
seven-branch-set construction used to force exactly two components.

## 1. Formal setup and the unresolved branch

The four nominated vertices are distinct.  The two edges are
vertex-disjoint and lie outside the five-clique `L`; contracting them
therefore creates two distinct vertices `z_i,z_j`, neither equal to
`ell_i` nor `ell_j`.

The repaired hypotheses now state, rather than merely invoke in prose, both
facts needed from the unresolved order-eight branch:

1. the two contracted edges are anticomplete; and
2. behind every relevant lifted three-vertex cut, every component is
   adjacent to all eight literal boundary vertices.

The second condition is the exact negation of the previously returned
order-seven outcome in this setting.  A component behind the lifted cut has
all its neighbours in the eight-vertex boundary.  Seven-connectivity gives
it at least seven neighbours.  If it does not meet the whole boundary, its
seven neighbours separate it from the nonempty inverse image of another
component of the quotient minus the cut.

No later step silently assumes that an arbitrary order-eight separator is
full or has two components.

## 2. The two available linkages

The edges `ell_i z_j` and `ell_j z_i` exist after contraction because each
defect edge is collectively adjacent to every nonexceptional leaf.  They
have four distinct endpoints and hence form the second displayed linkage.

For a three-vertex cut `T={z_i,z_j,x}`, the graph `Q-T` has at least two
components.  If a component failed to meet some vertex of `T`, its at most
two neighbours in `T` would separate it from another component of `Q-T`,
contrary to the absence of cuts of order at most two.  Thus every component
meets all three cut vertices.

If `x` is neither leaf root, the edge `ell_i ell_j` puts both leaf roots in
one component of `Q-T`; another component avoids both.  If `x` is one leaf
root, at most one component contains the other.  Again another component
avoids both.  A connected subgraph through that component and its contacts
with `z_i,z_j` supplies the required `z_i-z_j` path disjoint from the edge
`ell_i ell_j`.

The cited linkage characterization is Theorem 8 of Fabila-Monroy and Wood:
in a three-connected graph, a rooted `K_4` minor exists exactly when all
three pairings have linkages.  The first two pairings have just been built,
so hypothesis 4 excludes the same-index pairing.  The theorem is used with
the correct connectivity and four distinct roots.

## 3. Canonical web order

Lemma 2 of Fabila-Monroy and Wood states that failure of an
`(s_1t_1,s_2t_2)` linkage implies that the graph is a spanning subgraph of
an `(s_1,s_2,t_1,t_2)`-web.  Substitution

\[
  (s_1,s_2,t_1,t_2)=(\ell_i,\ell_j,z_i,z_j)
\]

gives exactly the outer order claimed.  No completion edge of the web is
thereby asserted to be an edge of `Q`.

## 4. Cliques in the web completion

The planar core `H` cannot contain a four-clique.  The four triangles of an
embedded `K_4` would all have to be faces because every triangle of `H` is
facial.  They exhaust the sphere, leaving `H=K_4`, incompatible with the
specified outer four-cycle.

Consequently a clique of order at least four in `H^+` contains a vertex of
some attached clique `X_T`.  Such a vertex has no neighbours outside
`T union X_T`, which confines the entire clique to this set.  After deleting
`T`, its nonempty part in `X_T` cannot reach an outer vertex outside `T`.
Thus `T` is genuinely a three-vertex cut in any relevant spanning subgraph;
this conclusion uses only absent edges of the completion and is therefore
safe when passed to `Q`.

## 5. Image of the second five-clique

Because the two defect edges are anticomplete, a clique cannot contain an
endpoint of each.  Hence the second five-clique meets the endpoints of at
most one defect edge.  The two contractions identify at most one pair of
its vertices, so its image is a clique of order at least four in `Q`.

The preceding web lemma places that image in `T union X_T` for a facial
triangle `T`.  The image has a vertex in `X_T`, since the planar core has no
four-clique, and at least one of the four outer vertices lies outside the
three-set `T`.  Therefore `T` is a three-vertex cut of `Q`.  The hypothesis
on all such cuts then forces both `z_i,z_j` into `T`.

The edge `z_i z_j` belongs to the outer cycle of the web completion but not
to `Q`: an edge between the contracted vertices would lift to an edge
between the two anticomplete defect edges.  The proof consistently treats
this as a virtual completion edge, never as a host-graph adjacency.

## 6. The third vertex is not another outer root

Suppose the facial triangle on the outer edge `z_i z_j` had third vertex
`ell_i`.  It would use the outer diagonal `z_i ell_i`.  This diagonal
separates `ell_j` and `z_j` in the embedded planar core.  Every attached
clique belongs to one facial triangle; after deleting the diagonal's ends,
an attached clique can remain only on the side containing the third vertex
of its supporting triangle.  It cannot reconnect the two sides.

Thus deleting `{z_i,ell_i}` disconnects the whole web completion, and in
particular its spanning subgraph `Q`, while leaving `ell_j,z_j` present.
This contradicts the absence of cuts of order at most two.  The symmetric
argument excludes `x=ell_j`.  This repairs the former unsupported assertion
without treating either diagonal as an edge of `Q`.

## 7. Exactly two lifted components

The selected facial triangle is a cut of `Q`, so its lifted eight-set has at
least two complementary components.  Hypothesis 7 makes every such
component adjacent to all eight boundary vertices.

If three components `C_1,C_2,C_3` existed and `e_j=a_jb_j`, the proposed
seven branch sets are disjoint and connected:

\[
 C_1\cup\{a_j\},\quad C_2\cup\{b_j\},\quad
 C_3\cup\{x\},\quad e_i,\quad \{r\}\ (r\in R).
\]

Their adjacencies check as follows.

- The first two meet through the edge `a_jb_j`.
- Each of the first two meets the third through its component's neighbour
  at `x`.
- Full boundary adjacency makes each of the first three adjacent to the
  edge branch set `e_i` and to all three singletons in `R`.
- The edge `e_i` is collectively adjacent to each vertex of `R`.
- The three vertices of `R` form a clique.

These are all twenty-one required adjacencies of a `K_7` model.  This
contradicts the setup, so exactly two components remain.

## 8. Separation of the two five-cliques

The third vertex `x` is distinct from both leaf roots.  Their edge therefore
places `ell_i,ell_j` in one component of `Q-T`.  The portion of the image of
`Y` in `X_T` is nonempty—its image has order at least four whereas `T` has
order three—and is connected because it is part of a clique in `Q`.
Vertices of `X_T` have no neighbours outside `T union X_T`, even in the web
completion.  Hence this portion lies in a component contained in `X_T`,
different from the component containing the two outer leaf roots.  Since
there are exactly two components, it is precisely the other component.
Expanding the two contracted edges preserves this separation and yields the
stated eight-vertex boundary.

## 9. Scope

The theorem classifies the exact unresolved order-eight branch under its
explicit fullness and anticompleteness hypotheses.  It does not eliminate
that branch, produce the virtual `z_i z_j` adjacency in `Q`, construct a
`K_7` minor in the two-component outcome, or establish a two-vertex
transversal for all relevant `K_5` models.  No such stronger conclusion is
credited to this audit.
