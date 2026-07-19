# Independent audit: response propagation across two cutvertex lobes

**Verdict:** **GREEN** for Theorem 2.1, Corollary 2.2, Theorem 3.1,
the two edge-deletion colourings following (3.3), Lemma 3.2, and
Proposition 3.3.
This is a separate internal mathematical audit, not external peer review.
The result is conditional on the complete setting in Section 1 and does not
prove `HC_7`.

## Audited revision

This audit checks the complete source file
[`hc7_order8_cutvertex_lobe_response_propagation.md`](hc7_order8_cutvertex_lobe_response_propagation.md)
at SHA-256

```text
5a43978e738e149140cc4f32e46a8d64c117e4c883f1c70fb52c2a32b834f7d2
```

The promoted revision differs from the audited mathematical source only in
its status line and adjacent-audit link; the theorem statement and proof are
unchanged.

No unresolved mathematical gap was found at this revision.

## 1. Geometry of the two closed sides

For the boundary

\[
B_d=\{z\}\mathbin{\dot\cup}(S-\{e\}),
\]

the two open sides are `C_d` and
`C_e dotcup {e} dotcup R`.  They are anticomplete: `C_d,C_e` are distinct
components of `G[L]-z`, there are no `L`--`R` edges, and (1.6) excludes `e`
from the neighbourhood of `C_d`.  The analogous assertion holds for
`B_e`.  Thus the two displayed sets really are order-eight separation
boundaries, and the gluing arguments in Theorem 2.1 use the complete literal
boundary rather than a quotient boundary.

The equation `c_L(z)=c_L(d)=c_L(e)` and properness do imply all three
nonedges `zd,ze,de`.  No later argument assumes an additional edge or
nonedge among these vertices.

## 2. Existence of the two opposite responses

Restricting `c_L` to `G[C_d union B_d]` gives an admissible equality
response: `X,Y,{z,d}` are three distinct monochromatic blocks.  To obtain
the complementary inequality response, the proof maps the three boundary
colours of `c_L` to the `c_R` colours on `X`, `Y`, and `e`, and then recolours
only `d` with the fourth `c_R` boundary colour.

That recolouring is proper for every possible neighbour of `d` in the
restricted graph:

- (1.6) excludes all neighbours in `C_e`;
- (1.7) excludes `z` and `e`; and
- all remaining possible neighbours lie in `X union Y`, whose two colours
  differ from the new colour of `d`.

The recoloured graph and `c_R` agree vertex by vertex on `S`, and their open
parts are anticomplete by (1.2).  They therefore glue to a proper
six-colouring of `G-C_d` with `z=e` in colour and `z!=d`.  This verifies the
claimed nonempty complementary inequality response without using
minor-criticality beyond the stated colourings.

## 3. The response sets are singletons

For an admissible boundary colouring there are exactly two possible
equality types: `z=r` and `z!=r`.  In the equality case the boundary has the
three blocks `X`, `Y`, `{z,r}`; in the inequality case it has the four blocks
`X`, `Y`, `{z}`, `{r}`.  Any two colourings with the same type can be aligned
on all literal boundary vertices by a permutation of the six colour names.

Consequently, if the `C_d`-side also had an inequality response, it would
glue to the constructed complementary inequality response; if the
complementary side also had an equality response, it would glue to the
restricted `c_L` response.  Either gluing would six-colour `G`, contradicting
`chi(G)=7`.  Thus the inference that the two response sets are the opposite
singletons is valid.  The symmetric argument for `B_e` uses exactly the
same hypotheses.

## 4. The Kempe path and the omitted root

Fix any admissible colouring of `G-C_d`, with colours `alpha=c(z)` and
`beta=c(d)`.  The singleton response gives `alpha!=beta`.  If `z,d` were in
different components of the subgraph induced by these two colours, swapping
the colours on the component containing `z` would make `z,d` equal.  Since
`X union Y` uses neither colour, the switched colouring would remain
admissible.  This would be a forbidden equality response.  Hence an
`alpha`--`beta` path from `z` to `d` exists.

Its internal vertices avoid `B_d`: the other boundary vertices are in
`X union Y` and have neither of the two path colours.  After those vertices
are removed, the only possible internal vertices are in
`C_e dotcup {e} dotcup R`.  The first internal vertex must lie in `C_e`,
because `z` has no edge to `e`, `d`, or `R`; the last internal vertex lies
in `R`, because `C_e` has no neighbour at `d` and `e d` is absent.  Since
there are no `C_e`--`R` edges, the path must pass through the omitted root
`e`.  This proves the topological passage asserted in lines 190--201.

The colour of `e` is therefore one of `alpha,beta` and avoids the two block
colours.  Restriction to `G[R union S]` satisfies the exact hypothesis of
the split-response assumption, which forces `c(e)!=c(d)`.  Hence
`c(e)=c(z)`, proving (2.1) for every complementary admissible colouring.
The interchanged proof gives (2.2).

## 5. Nonbipartiteness of each lobe

If `C_d` were bipartite, its two parts could use two colours disjoint from
four distinct colours assigned to the independent boundary blocks
`X`, `Y`, `{z}`, `{d}`.  All edges inside the boundary are proper because
different blocks have different colours, and all lobe--boundary edges are
proper because the two palettes are disjoint.  This is an admissible
inequality response on the `C_d`-side, contradicting Theorem 2.1.  The same
argument applies to `C_e`.

Each lobe is a connected component of `G[L]-z`; a connected nonbipartite
graph contains an odd cycle, and an odd cycle has a `K_3` minor.  Corollary
2.2 is therefore correct.

## 6. Construction of the crossed colouring of `G-z`

The complementary colouring for `B_d` induces on `S` the four blocks
`X`, `Y`, `{d}`, `{e}`, because (2.1) identifies `z` with `e`.  The
complementary colouring for `B_e` induces the same four literal blocks,
because (2.2) identifies `z` with `d`.  A colour permutation can therefore
align the two colourings on every vertex of `S`.

Taking `C_d` from the aligned `G-C_e` colouring and taking
`C_e union R union S` from the `G-C_d` colouring gives a proper colouring
after deleting `z`: the two lobe colourings agree on their boundary
neighbours in `S`, the lobes are anticomplete to each other, and neither
lobe has an edge to `R`.  This verifies the gluing in Theorem 3.1.

Before `z` is deleted, its colour in the `G-C_e` colouring is the colour of
`d`; properness therefore excludes that colour from its neighbours in
`C_d`.  The symmetric exclusion holds in `C_e`.  In the resulting
six-colouring of `G-z`, every one of the six colours must occur in `N_G(z)`,
or a missing colour could be assigned to `z` and would six-colour `G`.
Neither root is adjacent to `z`, there are no `z`--`R` edges, and the
neighbours of `z` in `S` use the two block colours.  Thus the missing root
colour on one lobe must occur on the other lobe.  All four assertions in
(3.2), including nonemptiness of `Z_d,Z_e`, follow.

## 7. The proper-minor edge-deletion colourings

Under `psi`, every neighbour of `z` with colour `delta=psi(d)` lies in
`Z_d`: that colour is absent from `N(z) cap C_d`, the two roots are
nonneighbours of `z`, `R` is anticomplete to `z`, and `X,Y` use different
colours.  Deleting every edge from `z` to `Z_d` therefore removes exactly
all conflicts created by assigning colour `delta` to `z`.  The extended
colouring is proper.  The symmetric assertion for `Z_e` and colour
`epsilon=psi(e)` is identical.

Both deletion sets are nonempty, so each resulting graph is a proper
subgraph and hence a proper minor of `G`.  When the relevant set is a
singleton this is one elementary edge deletion.  When it has more than one
vertex, the source correctly claims only the colouring after deleting all
of those edges; it does not claim that one single-edge deletion has already
produced that colouring.

## 8. Single-edge deletion saturation

For every `u in Z_d` and `v in Z_e`, the edges `zu,zv` exist by definition.
Deleting either one produces a proper minor and hence a colouring from a
palette of six colours by (1.1).  In every such colouring the deleted edge's
endpoints must have the same colour: if they differed, restoring the edge
would leave the colouring proper and contradict `chi(G)=7`.

Fix one endpoint and any one of the other five palette colours.  If the
endpoint had no neighbour of that colour, recolouring only that endpoint
would be proper.  It would then differ in colour from the other endpoint,
so the deleted edge could again be restored, giving a six-colouring of `G`.
This contradiction proves neighbour saturation at both endpoints in every
one of the other five colours.  The reasoning also shows that all five other
colour classes are nonempty; an unused palette colour would itself permit
the forbidden recolouring.  Lemma 3.2 is therefore valid for every crossed
edge, not merely for an edge selected from the particular colouring `psi`.

## 9. The full-subgraph bottleneck

The complementary open side of `B_d` is
`C_e dotcup {e} dotcup R`.  A connected subgraph in it that is adjacent to
`z` must meet `C_e`, because `z` has no neighbour at `e` or in `R`.  If it
also meets `R`, connectedness forces it through `e`: there is no
`C_e`--`R` edge and no other boundary vertex belongs to this open side.
Thus two such connected subgraphs cannot be vertex-disjoint.

Every connected extension of either named subgraph `P_i` to a subgraph full
to `B_d` meets `R` and is adjacent to `z`, so two disjoint such extensions
are impossible.  The symmetric bottleneck is the literal vertex `d` for
`B_e`.  Proposition 3.3 is therefore valid and does not assume that either
`P_i` alone is already full to the new boundary.

## 10. Trust boundary

The audited result proves, for the exact conditional two-lobe structure:

- opposite singleton equality responses on the two exact order-eight
  boundaries;
- forced passage of the complementary Kempe path through the omitted root;
- nonbipartiteness, hence a `K_3` minor, in each lobe;
- a six-colouring of `G-z` with the two crossed nonempty neighbour-colour
  sets;
- the corresponding batch edge-deletion colourings; and
- endpoint equality and five-colour neighbour saturation in every
  six-colouring after deleting any one crossed edge; and
- the literal one-vertex bottleneck preventing both named `R`-subgraphs
  from descending as disjoint boundary-full subgraphs.

It does **not** prove that every live order-eight interface has this
cutvertex structure.  It does not turn a palette colour into a named
branch-set contact, construct a `K_7`-minor model, return a compatible
order-seven separation, preserve the selected response through a strict
host-level descent, or prove the cyclic-contact allocation conclusion.  A
further operation-specific Kempe or first-hit theorem is still required.
