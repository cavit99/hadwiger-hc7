# Audit of the five-connected planar support-five exclusion

**Verdict:** **GREEN.**  The connectivity loss, planar separating-triangle
argument, and both branches of the contraction pullback are correct as
stated.  No mathematical correction is required.

## 1. Connectivity and planarity checks

Lemma 1.1 uses the correct deletion count.  If the contracted vertex is
deleted together with at most `k-3` other quotient vertices, its lift
deletes both edge ends and therefore at most `k-1` original vertices.  If
the contracted vertex is retained, the connected graph before contraction
maps onto the required quotient deletion.  Thus an edge contraction of a
`k`-connected graph is `(k-1)`-connected.

Lemma 1.2 is also literal.  In a fixed plane drawing of the displayed
`K_4`, every component outside the clique lies in one face of the clique
drawing.  Its clique neighbours lie on that face's boundary triangle, so
deleting the triangle separates it from the fourth clique vertex.  The
argument needs an outside vertex, which is supplied in every later use.

For a support-five `K_4` model, the bag sizes are exactly `(2,1,1,1)` and
the two-vertex bag is an edge.  Contracting it yields a literal `K_4` in a
planar four-connected graph.  A five-connected graph has at least six
vertices, so the contraction has at least five and Lemma 1.2 has the
required outside vertex.  This proves Theorem 2.1 without a hidden rooted
or embedding-uniqueness assumption.

## 2. Pullback audit

Let `J=H-R`.  Seven-connectivity of `H` makes `J` five-connected, and the
theorem assumes it planar.

When `z` is not in `R`, contracting `xy` preserves a five-row model unless
`x` and `y` occupy two different rows.  In that exceptional case the edge
contraction merges exactly those rows and leaves a `K_4` model in `J`; its
support drops by one and is therefore at most five.  Theorem 2.1 excludes
it.  This covers models using neither split endpoint, one endpoint, or both
endpoints in one row, as well as the split-row case.

When `R={z,r}`, for each retained vertex `q in {x,y,r}` the graph obtained
by deleting the other two vertices is literally `J+q`.  A surviving
`K_5` model must use `q`, since `J` is planar.  If the `q`-row is a
singleton, deleting it leaves a support-at-most-five `K_4` model in `J`.
If it is not a singleton, five nonempty bags on at most six vertices force
the unique size pattern `(2,1,1,1,1)`, and the other four rows are a
literal `K_4` in `J`.  Both alternatives contradict Theorem 2.1.  Hence all
three displayed pairs are genuine support-at-most-six transversals.

Removing `z` from `H` is exactly removing both `x,y` before contraction,
so no extra quotient edge survives in this identification.  Corollary 3.2
therefore applies Theorem 3.1 with the correct literal graph `J`.

## 3. Sharpness checks

The two examples in Section 5 were checked in the standard NetworkX
labelling.  The displayed octahedral edge bag is connected, the three
singleton vertices form a triangle and each meets the edge bag.  In the
icosahedron, the displayed three-vertex bag is connected, the singleton
vertices form a triangle and each meets that bag.  They witness precisely
support five at connectivity four and support six at connectivity five.

The result closes only the planar terminal-contraction response.  It does
not address a nonterminal contraction response, a four-connected planar
core, support-six rooted `K_4` models, or a non-seven-connected quotient.
