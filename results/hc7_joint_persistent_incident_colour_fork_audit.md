# Independent audit of the jointly persistent incident-edge colouring fork

**Verdict:** GREEN for Proposition 2.1, Theorem 3.1, Corollary 3.2,
and the stated application to a fixed spanning labelled
`K_7`-minus-one-edge model, under the explicit hypotheses in the source.

**Audited source:** `hc7_joint_persistent_incident_colour_fork.md`, SHA-256

```text
21b5fd5c523efb673ca11b0e604e0e81d173a5dbda677baa235efd8924d4b865
```

After the GREEN audit, the source was moved from `active/` to `results/`
and only its status paragraph was changed to link this audit.  The theorem
statement and proof are unchanged; this audit is repinned to the resulting
promoted source hash above.

This is a separate internal mathematical audit, not external peer review.
The audit reconstructed the two contraction colourings, every possible
one-interchange transition between the two response signatures, the
saturation recolourings, the neighbourhood and separation assertions, and
the dominating-subgraph chromatic conclusion.  No counterexample to the
statements at the pinned hash was found.

## 1. Nonadjacent outer ends

When `ab` is absent, contracting the two-edge tree on `v,a,b` gives a
proper minor.  Expanding a `q`-colouring of that minor to
`H=G-{va,vb}` is proper because there is no third edge inside
`{v,a,b}`.  Every other neighbour of `v` remains adjacent to the
contracted vertex, so

\[
 c(v)=c(a)=c(b),\qquad
 N_G(v)\cap c^{-1}(c(v))=\{a,b\}.
\]

These are exactly the hypotheses needed for Theorem 1.1 of the cited,
audited bichromatic saturation-or-bypass theorem.  Its alternatives give
the stated universally linked incident edge or an `a-b` path in `H-v`,
together with the two opposite one-edge response colourings.  No additional
minor-model property is used in this part.

## 2. The two critical-triangle responses

Assume `ab` is an edge.  It remains an edge of `H`.

- A `q`-colouring of `H` cannot make both `va` and `vb` proper, since then
  both deleted edges could be restored and `G` would be `q`-colourable.
- It cannot make both pairs equal, since `a` and `b` are adjacent in `H`.

Thus every colouring has exactly one of the two displayed response
signatures.

Contracting `va` and expanding a colouring of `G/va` gives a colouring of
`G-va` in which `v,a` are equal and `v,b` are proper.  Every other neighbour
of `v` sees the contracted vertex, so the same-colour trace at `v` is
exactly `{a}`.  Contracting `vb` gives the symmetric signature and exact
trace `{b}`.  Both response classes are therefore nonempty.

If one Kempe-reconfiguration component meets both response classes, a
shortest path in that component has one edge crossing between them.  This
justifies the reduction to a single bichromatic-component interchange.

## 3. Exhaustive form of one transition

In the initial response write

\[
 \phi(v)=\phi(a)=\alpha,\qquad \phi(b)=\beta.
\]

Breaking the first equality requires exactly one of `v,a` to be switched.
Creating equality between `v,b` then forces the two switched colours to be
exactly `alpha,beta`.

- If `v` is switched, it changes from `alpha` to `beta`; `a` and `b` must
  both remain outside the switched component.
- If `v` is not switched, then `a` must change from `alpha` to `beta` and
  `b` from `beta` to `alpha`; hence the switched component contains `a,b`
  but not `v`.

There is no third placement.  In particular, switching both `v,a` would
preserve their equality, while switching both `v,b` would exchange rather
than equalize their two distinct colours.

## 4. Saturation recolourings

In the first placement, the `alpha` side of the transition component is an
independent set containing `v`.  If it had no neighbour of an untouched
colour `theta`, recolouring the whole side `theta` would remain proper in
`H`; restoring `va` and `vb` would also be proper because `a,b` retain
colours `alpha,beta`.  This would `q`-colour `G`, a contradiction.

In the second placement, recolouring the initial `alpha` side similarly
makes `va` proper while `vb` was already proper.  After the interchange,
the old `beta` side contains `b` and is the equality side of `vb`;
recolouring it to a missing untouched colour makes both incident edges
proper.  Hence both sides have a neighbour of every untouched colour.

These arguments assert one contact from each whole colour side for every
untouched palette colour.  They do not assert that every vertex of a side
has every such contact or identify a palette colour with a branch-set
label.

## 5. Full neighbourhood and separator

The transition set `D` is a component of the induced `alpha,beta` subgraph
of `H`.  Therefore it has no `H`-edge to an outside vertex of either
transition colour.

- When `D` contains `v`, the only possible additional such boundary
  vertices in `G` are `a,b`, through the two deleted edges.
- When `D` contains `a,b`, the only possible additional such boundary
  vertex is `v`.

This proves the two displayed neighbourhood-colour inclusions.  The two
colourings differ only on `D`, so they agree pointwise on its open
neighbourhood `S=N_G(D)`.

If `G-N_G[D]` is nonempty, deleting `S` leaves the connected nonempty set
`D` and a nonempty opposite side with no edge between them.  Thus `S` is an
actual separator.  In a `k`-connected graph it has order at least `k`; at
equality the two opposite one-edge responses have the same labelled
colouring on the exact order-`k` boundary.

## 6. Dominating transition component

In either transition placement, neither deleted edge has both ends in
`D`.  Consequently `G[D]=H[D]`, and the transition colours make `D` a
connected bipartite subgraph of `G`.

If `D` dominates and `G-D` contained a `K_6`-minor model, then `D` would be
a seventh connected branch set adjacent to all six model bags.  This would
give a `K_7` minor, contrary to the `HC_7` hypotheses.  Hence `G-D` is
`K_6`-minor-free, and the established case `HC_6` gives
`chi(G-D)<=5`.  Conversely, a four-colouring of `G-D`, using colours
disjoint from a two-colouring of `D`, would six-colour `G`.  Therefore

\[
 \chi(G-D)=5,\qquad K_6\not\preccurlyeq G-D.
\]

The repaired proof in the source makes the `K_6`-minor exclusion precede
the invocation of `HC_6`, so there is no inference from chromatic number to
minor exclusion in the wrong direction.

## 7. Trust boundary

The audited note proves an exhaustive **colouring** fork for two jointly
deletion-persistent incident edges while retaining the same fixed labelled
minor model as a collection of branch sets.  It does not prove any of the
following:

1. that the two critical-triangle response classes lie in the same Kempe
   component;
2. that a separator returned by the transition has order exactly seven;
3. that agreement of the two response colourings on a separator already
   gives compatible proper colourings of both closed shores;
4. that a saturated palette colour is realized in a prescribed labelled
   branch set;
5. that the bypass or the dominating five-chromatic core repairs the sole
   missing adjacency of the fixed `K_7`-minus-one-edge model; or
6. that the note proves `HC_7`.

The fixed spanning model is unchanged by recolouring, but this is only
setwise persistence of its branch sets.  No colour-to-label correspondence
is obtained.
