# Audit of one-split/two-clique composition

**Verdict:** **GREEN after repair of the seven-vertex quotient case and
strengthening to quotient row compatibility.**  Every quotient clique is
literal, the Niu--Zhang and two-apex branches apply with their exact
hypotheses, and the lifted separator contains each named carrier in a
closed shore.

## 1. Quotient models and intersections

The support-six model has a two-vertex edge bag `xy` and four singleton
rows `Q`.  Contracting `xy` therefore makes `Q union {z}` a literal
`K_5`.

The hypothesis that `C_i` contains at most one end of `xy` makes the
contraction map injective on the five vertices of `C_i`.  Every clique edge
survives, so its image `C_i^e` is again a literal `K_5`.  This remains true
when one clique contains `x`, the other contains `y`, and both images
therefore contain `z`.  The theorem states the intersection bounds after
the contraction, so such newly created intersections are counted exactly
rather than silently discarded.

## 2. Seven-connected quotient branches

One edge contraction of a seven-connected graph is six-connected.  If the
quotient is seven-connected and two-apex, a planarizing set of order at
most two may be enlarged to an actual two-set.  The audited planar
support-five pullback theorem then returns a literal pair meeting every
support-at-most-six `K_5` model in `G`, including its separate cases
according as `z` belongs to the planarizing pair.

If the quotient is non-two-apex, its three literal `K_5` cliques meet
pairwise in at most three vertices by the explicit quotient hypothesis.
Niu--Zhang Theorem 1.10 at `k=5` applies exactly and gives a `K_7` minor.
Expanding an edge contraction inside whichever quotient branch set contains
`z` preserves a literal minor model in `G`.

## 3. Exact-seven lift

The original draft omitted the complete seven-vertex quotient.  The source
now handles it correctly: a six-connected graph on seven vertices is
`K_7`, giving the first outcome.  Thus in the non-seven-connected branch
one may assume the quotient has at least eight vertices.  Its connectivity
is then exactly six, so it has a six-set `T` whose deletion has at least two
nonempty components.

The contracted image `z` must belong to `T`.  Otherwise splitting `z` into
the adjacent vertices `x,y` occurs wholly inside one component of `H-T`
and cannot join two quotient components; equivalently, every surviving
path in `G-T` maps to a surviving walk in `H-T`.  This would make `T` a
separator of the seven-connected graph `G`.

After replacing `z` by both endpoints,

\[
                    T^+=(T-\{z\})\cup\{x,y\}
\]

has order seven, and `G-T^+` is literally the same graph as `H-T` on the
uncontracted vertices.  Hence it has the same at least two nonempty
components.  Assign any nonempty proper collection of these components to
one open shore and the rest to the other; this gives an actual exact-seven
separation.

For any clique `K` of `H`, the set `K-T` lies in at most one component of
`H-T`, since vertices in distinct components have no edge.  This applies
to `Q union {z}`, `C_2^e` and `C_3^e`.  Expanding the first clique replaces
the boundary vertex `z` by the boundary pair `x,y`, yielding the entire
model carrier `Q union {x,y}` in the same closed shore.  Each other image
clique uses at most one split endpoint; replacing its possible `z` by that
literal endpoint again stays inside the boundary and restores exactly the
original `C_i`.  Thus all three named carriers genuinely lie in closed
shores.  They need not lie in the same closed shore, and the theorem does
not claim that they do.

## 4. Scope

The theorem is a terminal trichotomy for an already row-compatible
one-split/two-clique triple.  It does not extract such a triple from
transversal number greater than two, orient the exact-seven separation, or
close the resulting adhesion.  The affine pair-cover barrier still rules
out replacing quotient row compatibility by an unconditional private-edge
selection claim.
