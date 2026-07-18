# Independent audit: nested full-neighbourhood descent

**Verdict:** **GREEN under the exact stated hypotheses.**  The neighbourhood
identity is exact for every component of the deleted-boundary graph, the
far-side condition makes every returned neighbourhood an actual separator,
and the order-eight equality case and clique-packing construction are valid.

**Audited source:**
`results/hc7_nested_full_neighbourhood_descent.md`.

**Source SHA-256:**
`61ea0abfc8a72f04a93bf0e6f1e06660262c466ce4c50474efe1e79e5ec263f0`.

This revision differs from the line-by-line audited source
`0d59818d7140e726be827a816c4a1720dc47d74979a024e10e599259842d4bce`
only by recording the GREEN status and inserting the preliminary
`|Q|<=6` sentence explicitly requested in Section 2 of this audit.  The
theorem statement and mathematical argument are otherwise unchanged.

## 1. Components and the exact neighbourhood identity

The notation `X=N_G(R)` is the open neighbourhood of the connected vertex
set `R`.  Hence `R` has no edge to `G-(R union X)`, and `R` itself is a
component of `G-X`.  The hypothesis that `G-(R union X)` is nonempty gives
at least one further component of `G-X`.

For any component `C` of `G-X`, an edge from `C` to a vertex outside
`C union X` would join two components of `G-X`.  Therefore

\[
                         N_G(C)\subseteq X,
\]

and consequently

\[
 |N_G(C)|=|X|-|X-N_G(C)|=7+\varepsilon-d_X(C).
\]

This applies without exception to `C=R`: by the definition of `X`, its
defect is zero.  For `C=R` the assumed far side remains after deleting
`N_G(C)`; for every other `C`, the component `R` remains.  Thus both open
sides of the separation with boundary `N_G(C)` are nonempty.  Seven-
connectivity gives `|N_G(C)|>=7`, equivalently
`d_X(C)<=epsilon`.  Nonnegativity is immediate from the definition.

It follows exactly that positive defect decreases the literal separator
excess by `d_X(C)`, whereas zero defect is equivalent to `C` being adjacent
to every vertex of `X`.  When `epsilon=1`, positive defect must equal one
and hence returns an order-seven separator.  If no such component exists,
all components of `G-X`, including `R`, are `X`-full.

## 2. Clique packing

Under `K_7`-minor exclusion, the boundary clique `Q` necessarily has order
at most six; otherwise any seven vertices of `Q` already give a `K_7`
subgraph.  This implicit preliminary observation supplies the harmless
case omitted before the selection sentence in the source proof.

If `m+|Q|>=7`, there are at least `7-|Q|` components and, since
`|X|>=7`, at least `7-|Q|` distinct vertices of `X-Q`.  Assigning one such
vertex to each selected component gives connected, disjoint branch sets.
Two component-derived branch sets are adjacent because either component is
adjacent to the other's boundary anchor; each is adjacent to every
singleton in `Q`; and the singleton sets are pairwise adjacent.  Hence the
displayed seven sets form an explicit `K_7`-minor model.

The examples stated after the corollary are also correct.  A boundary
triangle gives at most three components.  A boundary four-clique gives at
most two; nontriviality of the original separation gives at least the
component `R` and one far-side component, hence exactly two.

## 3. First-entry application

The cited audited first-entry theorem gives an exact equality

\[
 N_G(K)=T_K\mathbin{\dot\cup}A_K
\]

and the nonempty opposite shore makes this an actual separation.  Thus `K`
meets all hypotheses of Theorem 1 with

\[
 \varepsilon(K)=|T_K|+|A_K|-7\ge0.
\]

Every component complementary to `K` in
`G-N_G(K)` which misses a boundary vertex therefore yields a strictly
smaller literal full-neighbourhood separator.  At excess one, absence of
such a component gives exactly the boundary-full order-eight interface;
the clique-packing restriction then applies if `G` is `K_7`-minor-free.

As sanity checks, the two sharp complete-graph-minus-edges examples behave
as asserted.  In `K_10-uv`, taking `R={u}` gives excess one and two
components both full to the eight-set boundary.  Deleting additionally an
edge from `v` to one boundary vertex makes the complementary component have
defect one and returns an order-seven separator (the resulting graph still
has connectivity seven).  These examples expose no missing case in the
identity or its equality alternative.

## 4. Exact trust boundary

The theorem is a host-level separator calculation.  It does **not** show
that a descended separator preserves:

- the seven old boundary labels;
- either selected boundary-full connected subgraph;
- a previously chosen minor-model branch set;
- the colouring partition returned on either shore; or
- the hard exact-seven `(1,2)` hypotheses needed to iterate the earlier
  first-entry theorem.

Nor does the boundary-full order-eight alternative synchronize shore
colourings or itself produce a `K_7` minor.  The GREEN verdict certifies the
strict separator-excess dichotomy and its packing consequence only; the
label-preserving descent or colour-gluing mechanism remains open.
