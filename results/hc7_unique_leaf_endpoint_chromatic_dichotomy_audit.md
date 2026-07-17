# Independent audit: chromatic dichotomy at a unique leaf--endpoint edge

**Verdict:** GREEN.  Three non-substantive clarity and attribution repairs
identified in the first audit pass are incorporated in the exact revision
audited here.  The chromatic bounds, use of `HC_6`, spanning
absorption, five-colouring recolouring argument, localization of the two
selected colours in `H`, and the edge-deletion Kempe bypass are valid under
the stated hypotheses.  The result does not align the regenerated `K_6`
model with the two common neighbours and does not by itself give a `K_7`
minor.

**Audited source:**
`results/hc7_unique_leaf_endpoint_chromatic_dichotomy.md`.

**Source SHA-256:**
`8bc8ebcab599fd614afae5075c8e77384408d1f4750da55c5566439bd1c6d36b`.

## 1. Setup and nonadjacencies

The setup implies every nonadjacency used later.

* Since `a in V(e)` and `ell_e` is anticomplete to `V(e)`, the edge
  `ell_e a` is absent.
* Since `ell_f` has exactly one neighbour in `V(e)`, namely `a`, it is
  nonadjacent to the other endpoint of `e`.
* It is anticomplete to `V(f)` by hypothesis and nonadjacent to `x` by
  hypothesis.
* Hence the boundary neighbours of `ell_f` are contained in
  `R union {a}`.  The three vertices of `R` are indeed neighbours of
  `ell_f`, because `R union {ell_e,ell_f}` is a five-clique.
* A vertex in a component of `G-S` distinct from `C` cannot be adjacent to
  `ell_f in C`, by the definition of components of `G-S`.

No stronger contact property of `H` is used.  In particular, the proof of
the dichotomy only needs the displayed definition of `H`; its connectedness
is a harmless stronger hypothesis inherited from the balanced order-eight
configuration.

## 2. Exact chromatic fork after deleting two vertices

Put `J=G-{ell_f,a}`.  Vertex deletion is a minor operation, so (1.1) gives

\[
                              \chi(J)\le 6.
\]

If `J` had a four-colouring, assigning two new and distinct colours to
`ell_f` and `a` would be proper: the two vertices are adjacent, and neither
new colour occurs elsewhere.  This would six-colour `G`.  Therefore

\[
                              5\le\chi(J)\le6.
\]

These are the two mutually exclusive cases in Theorem 2.1.

If `chi(J)=6`, the contrapositive of the established parameter-six case of
Hadwiger's conjecture supplies a `K_6` minor.  The relevant primary source
is Robertson, Seymour and Thomas, *Hadwiger's conjecture for
`K_6`-free graphs*, Combinatorica 13 (1993), 279--361,
<https://doi.org/10.1007/BF01202354>.

The spanning conclusion is also valid.  Seven-connectivity implies that
deleting the two vertices `ell_f,a` leaves `J` connected.  The union of a
clique-minor model is connected.  Every component outside that union has
an edge to it, so one may absorb the entire component into an incident
branch set.  Connectivity and every old inter-branch-set adjacency are
preserved, and iteration yields a model spanning all of `J`.

## 3. The edge-local five-colouring recolouring

Assume `chi(J)=5` and fix an arbitrary proper five-colouring `phi` of `J`.
For a palette colour `i`, suppose there were no colour-`i` common neighbour
of `ell_f,a`.  The colour-`i` neighbours of `ell_f` form an independent
set, and none is adjacent to `a`.  Recolour all of them with a new sixth
colour, colour `ell_f` with `i`, and colour `a` with the new colour.

This is proper:

* every old colour-`i` conflict at `ell_f` was removed;
* the simultaneously recoloured vertices are independent;
* none of them is adjacent to `a`;
* the adjacent pair `ell_f,a` receives different colours; and
* the new colour occurs nowhere else.

It would six-colour `G`, a contradiction.  Thus the common neighbourhood
of `ell_f,a` contains a vertex of every one of the five colours.  This is
an edge-local consequence of the displayed chromatic hypotheses; the proof
does not assume that `G` is a double-critical graph.

## 4. Localization of the two selected colours

The clique `R union {ell_e}` uses four distinct colours.  Let `delta` be
the colour of `ell_e` and `beta` the fifth colour.  Common neighbours
`u,v` of colours `delta,beta` exist by Section 3 and are distinct because
their colours differ.

The claimed localization in `H` is exact.

* Neither vertex lies in another component of `G-S`, since both are
  adjacent to `ell_f in C`.
* Neither is `ell_e`, since `ell_e a` is absent.
* The only possible boundary locations for a neighbour of `ell_f` are
  `R union {a}`.  The vertex `a` is absent from `J`; no vertex of `R` has
  colour `delta`, and no vertex of the four-clique has colour `beta`.
* The remaining vertices in `C` are exactly those of
  `H=C-{ell_e,ell_f}`.

Consequently `u,v in V(H)`, with exactly the two asserted colour labels.
This holds for every five-colouring because `phi` was arbitrary.

## 5. Edge-deletion bypass

Let `K=G-ell_f a`, where the operation is edge deletion.  The source now
explicitly establishes the exact equality

\[
                               \chi(K)=6.                 \tag{5.1}
\]

Indeed, minor-criticality gives the upper bound, while a five-colouring of
`K` would become a six-colouring of `G` after recolouring one endpoint of
the restored edge with a fresh colour.  Thus every proper six-colouring of
`K` uses all six colours.  Its endpoints `ell_f,a` have the same colour
`alpha`, since otherwise it would already colour `G`.

The five-clique `R union {ell_e,ell_f}` is unaffected by deletion of
`ell_f a`, so it receives five distinct colours.  In view of (5.1), there
is exactly one palette colour `beta` absent from this clique.

If `ell_f` and `a` were in distinct components of the induced
`alpha`--`beta` subgraph, swapping those colours on the component containing
`ell_f` would give the endpoints different colours and hence a
six-colouring of `G`.  They are therefore in one such component, which
contains an `ell_f`--`a` path avoiding the deleted edge.

Every such path has a first internal vertex, and it is a `beta`-coloured
neighbour of `ell_f`.  It cannot lie in `R union {ell_e}`, because `beta`
is absent there.  It cannot be any other boundary vertex: outside `R`, the
only boundary neighbour of `ell_f` is `a`, whose colour is `alpha`.  It
cannot lie in a different component of `G-S`.  Hence it lies in `H`, as
claimed.  Notice that the proof establishes the first-vertex conclusion
for every such path in every proper six-colouring, not merely for one
chosen Kempe path.

## 6. Incorporated clarifications

The exact audited revision now:

1. proves `chi(G-ell_f a)=6` before using the unique absent colour in
   Lemma 2.2;
2. cites Robertson--Seymour--Thomas with the primary-source DOI at the
   invocation of `HC_6`; and
3. states explicitly that the symmetric version requires the
   correspondingly interchanged hypotheses and a newly named unique
   endpoint.

These edits make previously implicit points explicit and do not strengthen
the mathematical conclusion.

## 7. Trust boundary

The audit verifies only the stated local dichotomy.  It does not prove
that the spanning `K_6` model has six prescribed contacts, that the two
common neighbours belong to different usable branch sets, that the
Kempe path avoids a prescribed linkage or clique, or that either outcome
extends to a `K_7` model.  Those are genuine label-preserving allocation
obligations left open by the source.
