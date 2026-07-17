# Audit of the portal-cone Hall alternative

**Verdict:** GREEN for Theorem 4.3 at the exact revision below.

## Audited revision and scope

The audited source is
`active/hc7_contracted_portal_path_palette_obstruction.md`.

**Source SHA-256:**
`db54125365f34361b1fe0fddb1bcf0b743aef99fd08d7aa339fdef3b7c1167ac`.

This audit covers only Theorem 4.3, including its arbitrary leaf-edge and
`q=6,m=3` conclusions.  It does not audit the other results in the source
or assert that the resulting palette saturation identifies minor-model
branch-set labels.

## 1. Necessary noncolourability hypothesis

An earlier revision omitted the hypothesis that `G` is not
`q`-colourable.  That revision was false: if `G=D` is a three-leaf star
and `q=4`, the contracted colouring has no leaf-to-leaf bypass, while all
three lists `U_i` contain all alternate colours and satisfy Hall's
condition.  The audited revision explicitly includes the missing
hypothesis, and the proof uses it only at the final restoration step.

## 2. Hall representatives and Kempe components

If no deficient set `I` exists, Hall's theorem supplies pairwise distinct
representatives `beta_i in U_i`.  The full
`{alpha,beta_i}`-component `A_i` containing `f_i` avoids `s` by the
definition of `U_i`.

If two such components intersect, their connected union contains a path
between the corresponding leaves and avoids `s`.  The same is true after
adding one edge when they are disjoint but adjacent.  This proves the
bypass conclusion in those cases.

Otherwise the components are pairwise disjoint and pairwise anticomplete.
Switching `alpha,beta_i` on each whole `A_i` is individually a valid Kempe
interchange.  Pairwise disjointness makes the assignments unambiguous, and
pairwise anticompleteness prevents a new conflict between two components
whose different palettes share the colour `alpha`.  Edges from a switched
component to the unswitched graph remain proper by maximality of the full
bichromatic component.

## 3. Restoring every edge of the contracted subgraph

After the switches, `s` retains colour `alpha`, while each `f_i` has its
representative colour `beta_i`.  Thus every centre--leaf edge is proper.
The representatives are pairwise distinct, so every allowed edge between
two leaves is also proper.  These are all edges of `G[D]`; hence restoring
the entire deleted edge set gives a proper `q`-colouring of `G`, contrary
to the explicit hypothesis.  The dichotomy follows.

## 4. Three-leaf quantitative alternatives

For six colours there are five alternate colours.  A deficient nonempty
set `I` has one of three orders.

- If `|I|=1`, its `U_i` is empty, so that leaf is linked in all five
  alternate colours.
- If `|I|=2`, the union of the two `U_i` has order at most one, so both
  leaves are linked in at least four alternate colours.
- If `|I|=3`, the union has order at most two, so each leaf is linked in
  at least three alternate colours.

These cases are exhaustive and give exactly the stated quantitative
conclusion.

## Unresolved assumptions or gaps

None for Theorem 4.3 at the audited hash.
