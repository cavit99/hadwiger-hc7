# Audit: the atomic compulsory edge is not double-critical

**Verdict:** GREEN after correcting the scope of the lock-arm paragraph.

## 1. Colourwise common neighbours

Assume `F-{x,y}` has a proper `(k-2)`-colouring and fix a colour `i`.
If no colour-`i` vertex is adjacent to both ends of `xy`, recolour every
colour-`i` neighbour of `x` with one fresh colour, give `x` colour `i`,
and give `y` the fresh colour.  The recoloured vertices were one old
colour class and hence are independent; none is adjacent to `y` by the
failure of a common neighbour.  All remaining edges retain a proper pair.
This really is a `(k-1)`-colouring, so Lemma 2.1 is correct even when the
original colouring did not use all `k-2` names.

## 2. Atomic localization and carrier closure

If `chi(G-{z,u})=5`, Lemma 2.1 gives five distinct common neighbours,
one in every colour.  Such a neighbour cannot lie in `R`, since `z in A`
and there is no `A-R` edge.  It cannot lie in `A`, since `zu` is the
unique `A-u` edge.  Therefore all five lie in `S-{u}=W`.

The carrier partition is oriented correctly for the audited unordered
asymmetric theorem:

\[
                         X=A-z,\qquad Y=\{z\}.
\]

The set `X` is nonempty, connected and `W`-full, so its support has order
at least six.  The singleton `Y` sees `u` and the five common neighbours,
so its support also has order at least six.  The sets cover `A`, are
adjacent because `A` is connected, and `z in Y`.  Hence the `(5,6)`
theorem applies and contradicts the counterexample.

Deleting two adjacent vertices from a 7-critical graph leaves chromatic
number at most six.  A value at most four would extend using two fresh
colours, so the only possibilities are five and six.  Excluding five
therefore proves equality six.  Known `HC_6` legitimately supplies an
unrooted `K_6` model avoiding `z,u`.

The same location and carrier argument does not require a colouring once
five common neighbours exist.  It therefore proves
`|N(z) cap N(u)|<=4`.  Since distinct alternate-colour locks use common
neighbours of distinct colours when they have length two, at least one of
the five locks has length at least three.  This gives distinct internal
vertices, but not distinct model rows.

## 3. Literal two-pole model lemmas

Lemma 5.1 is branch-set correct.  Five common rows together with the two
singleton poles give seven bags.  With four common rows and complementary
exclusive rows `F_a,F_b`, the connected union `F_a union F_b` is adjacent
to both poles and every common row; it gives the seventh bag.  Corollary
5.2 follows because two contact sets of order at least five either have at
least five common rows or have exactly four common rows and one exclusive
row on each side.

In Lemma 5.3 the bags `{z} union X_z` and `{u} union X_u` are connected,
disjoint and adjacent through the literal edge `zu`.  Their assumed five
foreign-row contacts, together with the five retained clique-model rows,
give all 21 adjacencies of a literal `K_7` model.

## 4. Trust boundary

The theorem regenerates only an unrooted model.  After it is enlarged to a
spanning model, the complementary twin-seam path through `zu` splits into
two vertex-disjoint end segments and hence has two distinct first-hit
vertices.  Those vertices may lie in one row.  The corrected source does
not claim two labelled rows.  Promoting the five-rung response still
requires the row-duty split of Lemma 5.3 or a terminal/receiver outcome;
path or palette multiplicity alone is insufficient.
