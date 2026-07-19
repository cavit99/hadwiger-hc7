# Triangle-transversal structure behind a two-cut

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_two_cut_triangle_transversal_audit.md`](hc7_order8_two_cut_triangle_transversal_audit.md).
This statement is not a proof of `HC_7`.

## Theorem (two-cut triangle-transversal residue)

Let `G` be a seven-connected graph satisfying

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G.
\]

Let `S` have order eight and suppose that `G-S` has exactly three components
`C,Q_0,Q_1`, all adjacent to every vertex of `S`.  Suppose also that
`G[S]` contains two vertex-disjoint triangles and that `G[C]` is
two-connected.

Fix a two-vertex cut `X={x,y}` of `G[C]`.  Assume that the small-boundary
lobe descent returns neither an actual order-seven separation nor a strict
order-eight descent for any component of `G[C]-X`.

Then the following hold.

1. `G[C]-X` has exactly two components.
2. Neither component is adjacent to all eight vertices of `S`.
3. Each component `L` has a unique missed boundary vertex

   \[
                         m(L)\in S-N_G(L).               \tag{1}
   \]

4. The two missed vertices are distinct and form a transversal of all
   triangles of `G[S]`.  For every fixed pair of disjoint boundary
   triangles, one missed vertex belongs to each triangle.

Thus every unresolved two-cut in the explicit two-triangle boundary class
has exactly two defect-one lobes, controlled by a two-vertex triangle
transversal in the literal boundary.

## Proof

By the audited two-separator corollary of the small-boundary lobe descent,
every component of `G[C]-X` has at least seven neighbours in `S`, and at
most one is full to `S`.  Hence every non-full component has the unique
missed vertex in (1).

In fact no component is full.  If `F` were full, choose another component
`L`; it is non-full and has a unique missed vertex `a`.  Of two disjoint
boundary triangles, at least one triangle `R` avoids `a`.  Choose three
distinct anchor vertices in `S-(R\cup\{a\})`.  The four connected
subgraphs `F,L,Q_0,Q_1` are all adjacent to every vertex of `R` and to all
three anchors.  Adding one anchor to three of the four subgraphs and
leaving the fourth bare gives, together with the three singleton vertices
of `R`, the standard explicit seven-branch-set `K_7` model.  This is a
contradiction.  Therefore every component has exactly seven neighbours in
`S`, proving assertions 2 and 3.

We next prove assertion 4.  Let `L,L'` be two non-full components and put

\[
                         a=m(L),\qquad b=m(L').           \tag{2}
\]

Suppose that `G[S]` has a triangle `R={r_1,r_2,r_3}` disjoint from
`{a,b}`.  The set

\[
                         S-(R\cup\{a,b\})                \tag{3}
\]

has order at least three (and exactly three when `a\ne b`).  Choose three
distinct vertices `t_1,t_2,t_3` from it.  Then the seven branch sets

\[
 L,\quad L'\cup\{t_1\},\quad Q_0\cup\{t_2\},
 Q_1\cup\{t_3\},\quad \{r_1\},\{r_2\},\{r_3\}          \tag{4}
\]

are pairwise disjoint and connected.  Both `L` and `L'` see every vertex
used in `R\cup\{t_1,t_2,t_3\}` because those six vertices avoid their
respective missed vertices.  The two `Q_i` are `S`-full.  It follows that
all adjacencies involving the first four branch sets are supplied through
the boundary anchors, and the last three form a triangle.  Thus (4) is an
explicit `K_7`-minor model, a contradiction.  Hence `{a,b}` meets every
boundary triangle.

It remains to prove assertion 1 and the final part of assertion 4.  Fix two
vertex-disjoint triangles `R_0,R_1` in `G[S]`.  There cannot be three
non-full components.  Indeed, let their missed vertices be `a,b,c`.
By assertion 4, each of the pairs `{a,b}`, `{a,c}`, `{b,c}` meets both
`R_0` and `R_1`.  Since the triangles are disjoint, each such pair must
contain one vertex of each triangle.  But among three vertices, two lie on
the same side of the bipartition `R_0,R_1` (and a vertex outside
`R_0\cup R_1` makes a pair miss one side immediately), so their pair misses
the other triangle.  This is impossible.

There are therefore at most two components.  Since `X` is a cut, there are
at least two, proving assertion 1.  Their missed vertices are distinct: if
they were equal, one of the two disjoint triangles would avoid that common
vertex, contradicting the triangle-transversal statement.  Finally, their
two missed vertices meet each of `R_0,R_1`; because the triangles are
disjoint, exactly one lies in each. \(\square\)

## Trust boundary

The theorem describes every unresolved two-cut under its explicit
two-disjoint-triangle hypothesis but does not eliminate the resulting
two-lobe residue.  It does not cover the two census boundary types whose
certified disjoint odd-cycle packing has orders `(3,5)` rather than `(3,3)`.
It does not produce compatible shore
colourings, preserve an inherited equality partition or minor-model labels,
or close the two-component order-eight interface.  Its conclusion is a
literal boundary triangle-transversal constraint, not a generic linkage
claim.

## Dependencies

- the audited small-boundary lobe descent and its two-separator corollary;
- the explicit hypothesis that the boundary contains two vertex-disjoint
  triangles (satisfied by the 80 census types with packing `(3,3)`, but not
  asserted for the two `(3,5)` types); and
- the standard four-full-connected-subgraph plus boundary-triangle minor
  construction, used here in the defect-one form displayed explicitly in
  (4).
