# Independent audit: repaired-contact exchange

**Verdict:** GREEN for Lemmas 2.1, 3.1, and 3.2 as stated.  The note
does not close the repaired-contact configuration or prove `HC_7`.

**Audited source:**
`results/hc7_repaired_contact_exchange.md`.

**Source SHA-256:**
`c2dc1cd6d2a4967d53c7a11be65e1a13a272f615afd970ae2f7f36eae03c648a`.

After the mathematical audit, the source was moved from `active/` to
`results/` and only its status, adjacent-audit link, and cross-reference
metadata were updated.  The hash above binds the audit to that exact
promoted revision; the audited mathematical content is unchanged.

## 1. Exact support exchange

For an `a3`--`x` path with `m` internal vertices, the five displayed
branch sets are disjoint and connected.  The first four form a clique,
and the last branch set meets `a0,a1,a2` through `a3` and meets `x`
through the final path edge.  Their total support order is `5+m`.

When `m=1`, the alternative description by singleton branch sets
`a0,a1,a2,a3` and the edge branch set `wx` is valid: `x` supplies the
first three contacts and `w` supplies the contact with `a3`.  If the
private pair is disjoint from the original six-vertex support, a literal
`K5` on `Q union {x}` would miss that pair, while the rotated support is
disjoint from it whenever `w` is.  These are exactly the conclusions
claimed; no strict descent is inferred.

## 2. Edge-critical colourings

For an edge `uv`, every six-colouring of `G-uv` makes `u,v`
monochromatic.  Otherwise it colours `G`.  If their two-colour component
with another colour failed to contain both ends, a Kempe swap in one
component would again colour `G`.  This standard observation is applied
with the correct deleted edge in both parts of Lemma 3.1.

After deleting `a3w`, the vertices of `Q` are rainbow,
`c(a3)=c(w)`, and adjacency of `x` to `a0,a1,a2,w` gives a fifth colour
at `x`.  The relevant two-colour component contains `a3,w,x`.  After
deleting `wx`, one has `c(w)=c(x)`; the edge `a3w` and the three contacts
from `x` again make `Q union {x}` rainbow, and the relevant component
contains `a3,w,x`.

## 3. Simultaneous bypass from two unrelated colourings

Lemma 3.2 does not identify the two colourings or their colour names, and
does not need to.  In the first component choose an `a3`--`w` path.  If
it meets `x`, its initial `a3`--`x` segment avoids both displayed edges;
otherwise the whole path avoids both.  Symmetrically, an `w`--`x` path
in the second component either contains a suitable `a3`--`x` segment or
avoids both displayed edges.  In the remaining case the two paths meet at
`w`; their union is connected and contains an `a3`--`x` path using
neither `a3w` nor `wx`.

In each colouring, `a0,a1,a2` use neither of the two relevant colours,
and `y` uses neither because it is adjacent to both `a3` and `x`.
Consequently both components, despite coming from different colourings,
avoid `A-{a3,x}`.  The resulting path therefore has the asserted literal
avoidance.

## 4. Trust boundary

The proof supplies a new path but gives no control over its intersections
with the six prescribed linkage paths, the second residual path, or the
private pair.  It also supplies no well-founded improvement when the new
path has one internal vertex.  The source states these limitations
correctly.
