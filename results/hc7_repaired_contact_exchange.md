# Repaired-contact exchange in the exceptional `3+1` configuration

**Status:** written lemmas; independently audited in
[`hc7_repaired_contact_exchange_audit.md`](hc7_repaired_contact_exchange_audit.md).
These lemmas use
minor-critical colouring in the three residual cases of the
[six-terminal crossing decoder](hc7_disjoint_k6minus_six_terminal_crossing_decoder.md).
They do not close those cases or prove `HC_7`.

## 1. Setup

Let `G` be a graph with chromatic number seven such that every proper minor
is six-colourable.  Retain the normalized vertices

\[
 Q=\{a_0,a_1,a_2,a_3\},\qquad A=Q\cup\{x,y\},
\]

where `Q` is a clique, `xy` and `a_3y` are edges, and `x` is adjacent to
`a_0,a_1,a_2` but not to `a_3`.  Thus `A` supports a `K_5` model with
four singleton branch sets `Q` and edge branch set `xy`.

Let `R` be an `a_3`--`x` path whose internal vertices avoid `A`.  In the
six-terminal application, `R` is one member of a clean residual crossing;
the other path, from `y` to one of `p,q,r`, is not needed for the two local
lemmas below.

When the support-six maximal-pair normalization is invoked, let `P` be its
private pair: `P` is disjoint from `A`, meets every literal `K_5`, and
`mu_G(P)=6`.

## 2. Exact support exchange

### Lemma 2.1 (support order along a repaired contact)

If `R` has `m` internal vertices, then `G` has a `K_5` model on exactly
`5+m` vertices, with branch sets

\[
 \{a_0\},\quad\{a_1\},\quad\{a_2\},\quad\{x\},
 \quad V(R)-\{x\}.                                    \tag{2.1}
\]

Consequently:

1. `m=0` gives the literal `K_5` on `Q union {x}`;
2. if `m=1`, say `R=a_3wx`, then

   \[
                   A_w=(A-\{y\})\cup\{w\}             \tag{2.2}
   \]

   is another exact-six support, with singleton branch sets `Q` and edge
   branch set `wx`; and
3. if the private pair `P` is retained, the case `m=0` is impossible,
   while in the case `m=1` either `w in P` or `A_w` is a second exact-six
   model support disjoint from `P`.

#### Proof

The first four sets in (2.1) form a clique: `a_0,a_1,a_2` form a triangle
and `x` is adjacent to all three.  The last set is connected, is adjacent
to each `a_i` through `a_3`, and is adjacent to `x` through the last edge
of `R`.  This proves the model and its order.

For `m=0`, its support is the five-set `Q union {x}`.  For `m=1`, the same
model can equivalently be written with singleton branch sets `Q` and edge
branch set `wx`: the endpoint `x` contacts `a_0,a_1,a_2`, while `w`
contacts `a_3`.  This proves (2.2).

Finally, `P` is disjoint from `Q union {x}` because it is disjoint from
`A`, whereas it meets every literal `K_5`; hence `m=0` is impossible.  If
`m=1` and `w notin P`, then (2.2) is disjoint from `P`. \(\square\)

The last outcome is compatible with `mu_G(P)=6`; maximal support height
alone does not prefer `A` to `A_w`.  Thus (2.2) is a genuine model rotation,
not yet a decreasing exchange.

## 3. A label-aligned critical-colouring witness

We use the following standard edge-critical observation.  If `uv` is an
edge and `c` is a six-colouring of `G-uv`, then `c(u)=c(v)`.  Moreover, for
every other colour `gamma`, the vertices `u,v` lie in the same component of
the subgraph induced by `c(u)` and `gamma`.  Otherwise swapping those two
colours in the component containing just one of `u,v` would extend `c` to a
six-colouring of `G`.

### Lemma 3.1 (two edge-deletion witnesses for a one-vertex repair)

Suppose `R=a_3wx`.  Then:

1. in every six-colouring of `G-a_3w`, the five literal vertices
   `a_0,a_1,a_2,a_3,x` receive five distinct colours, and the two-colour
   component on the colours of `a_3` and `x` contains an `a_3`--`x` path
   avoiding the deleted edge `a_3w`;
2. in every six-colouring of `G-wx`, those same five vertices receive five
   distinct colours, and the two-colour component on the colours of `a_3`
   and `x` contains an `a_3`--`x` path avoiding the deleted edge `wx`.

#### Proof

Let `c` colour `G-a_3w`.  Edge-criticality gives
`c(a_3)=c(w)=alpha`.  The clique `Q` uses four distinct colours.  Since
`x` is adjacent to `a_0,a_1,a_2,w`, its colour `beta` differs from all four
colours on `Q`.  Thus the five named vertices are rainbow.  Apply the
edge-critical observation to `a_3w` with the colour `beta`.  Its
`alpha,beta` component contains `a_3` and `w`, and it also contains `x`
through the edge `wx`.  A path inside that component gives the first
conclusion.

Now let `c` colour `G-wx`.  We have `c(w)=c(x)=beta`.  The vertices of `Q`
again use four distinct colours.  The common colour `beta` differs from
the colours of `a_0,a_1,a_2` because they are adjacent to `x`, and from the
colour `alpha=c(a_3)` because `a_3w` is an edge.  The five named vertices
are therefore rainbow.  Apply the edge-critical observation to `wx` with
the colour `alpha`.  Its `alpha,beta` component contains `w,x`, and it
contains `a_3` through `a_3w`.  This gives the second path. \(\square\)

Lemma 3.1 is a genuine palette-to-label statement: the five colours are
attached to the five prescribed vertices of the repaired `K_5` interface.
It supplies two independently attained bichromatic repairs, one avoiding
each edge of the rotated two-vertex branch set.  It does not show that
either repair avoids the six original linkage paths, the second residual
crossing path, or the private pair.

### Lemma 3.2 (the two witnesses give a simultaneous edge bypass)

There is an `a3`--`x` path in `G` which uses neither `a3w` nor `wx` and
whose internal vertices avoid `A`.  Moreover, it may be chosen inside the
union of the two bichromatic components supplied by Lemma 3.1 (for one
choice of a six-colouring after each edge deletion).

#### Proof

Choose a six-colouring of `G-a3w`.  In the bichromatic component used in
the first part of Lemma 3.1, choose an `a3`--`w` path `L_3`.  If `L_3`
contains `x`, its `a3`--`x` subpath uses neither deleted edge: it avoids
`a3w` because that edge is absent, and it cannot use `wx` before its first
arrival at `x`.  This is the required path.  Otherwise `L_3` avoids both
`a3w` and `wx`.

Likewise, choose a six-colouring of `G-wx` and a `w`--`x` path `L_x` in
the bichromatic component from the second part of Lemma 3.1.  If `L_x`
contains `a3`, its `a3`--`x` subpath avoids both displayed edges.  Otherwise
`L_x` avoids both `wx` and `a3w`.

In the remaining case, `L_3 union L_x` is a connected subgraph containing
`a3` and `x`, and every one of its edges is different from `a3w` and
`wx`.  A shortest `a3`--`x` path in this union has the required property.

It remains to check the asserted avoidance.  In either colouring, the
vertices `a0,a1,a2,a3,x` are rainbow.  The vertex `y` is adjacent to both
`a3` and `x`, so its colour is also different from the two colours that
induce the component in question.  Consequently each of the two
bichromatic components avoids `A-{a3,x}`, and so does the path just
constructed.
\(\square\)

Thus minor-criticality repairs the missing contact without either edge of
the original two-edge path.  This is stronger than having one witness
which merely avoids the edge deleted in its own colouring.  It is still
not a local `K_7` certificate: the simultaneous bypass may be long, may
meet the six linkage paths, and may meet the other residual path.

If a simultaneous bypass has exactly one internal vertex `u`, Lemma 2.1
applied to that path gives the exact-six support `(A-{y}) union {u}`.  If
instead its interior and the interior of
the clean `y`--`z` residual path meet while avoiding the linkage system,
the [intersecting-path lemma](hc7_repaired_contact_intersection.md) gives
an explicit `K_7` minor when `z` is `p` or `q`.

## 4. Exact remaining step

The repaired-contact route now has two sharply different residues.

- A one-internal-vertex repair gives the exact support rotation (2.2).
  More generally, Lemmas 3.1--3.2 give a path repairing the same contact
  while avoiding both edges of the original repair.  A closure must use
  the second residual path, the six linkage paths, or the private-pair
  incidence to make this bypass strictly preferable.
- With at least two internal vertices, (2.1) has support order at least
  seven and leaves the support-six family.  Edge-criticality at a single
  edge of the path no longer forces `a_3` and `x` to have different
  colours.  A uniform proof therefore needs either a shortening/rerouting
  theorem or a literal bounded separator; Lemma 3.1 cannot simply be
  iterated along the path.
