# Audit of the order-eight two-cut chromatic fork

**Verdict:** GREEN.

**Audited source:**
`results/hc7_order8_two_cut_chromatic_fork.md`

**Audited SHA-256:**
`e9bf34db9438e64203f671917d22bb106e07e828deb112f9fd0d4322dd5c0afb`

**Promoted source SHA-256:**
`11e618c7f6fa8cb365da450e006a89edba0888949eafb33930e987a3cc635034`

The promoted revision changes only the status line and adds this audit link;
the theorem statements, proofs, dependencies, and trust boundary audited
below are unchanged.

**Audit type:** independent internal mathematical audit.  This is not
external peer review and does not prove `HC_7`.

## Construction of the equal-root colouring

Assume both open lobes are three-colourable.  If `xy` is absent, use the
same three-colour palette on the two anticomplete lobes, a fourth colour on
`x,y,d,e`, and two fresh colours on `P,R`.  This is proper because:

- `xy`, `de`, and all four cut-vertex--root edges are absent;
- the lobe palette is disjoint from the three boundary-block colours;
- `P,R` are independent and have distinct colours; and
- there are no edges between the two lobes.

It realizes `P | R | {d,e}` on the closed `C`-side, contradicting the
audited response orientation.  Thus `xy` is present.

After deleting `xy`, the same construction is proper with
`x,y,d,e` all coloured `alpha`.  Assertion 1 of the response-orientation
theorem gives the same exact equality partition on each individual closed
`Q_i`-side.  Permuting colour names aligns the three labelled boundary
blocks, and the open components `C,Q_0,Q_1` are pairwise anticomplete.
Their colourings therefore glue to the claimed six-colouring `phi` of
`G-xy`, with properties (a)--(c).

## Kempe components and path intersections

Fix `beta!=alpha`.  If `x,y` belonged to different components of the
`alpha,beta`-induced subgraph, swapping those two colours on the component
containing `x` would preserve properness and give `x,y` different colours.
Restoring `xy` would then six-colour `G`, a contradiction.  Hence an
`alpha`--`beta` path exists between them for each of the five other
colours.

Choose any simple path in each such component.  For distinct `beta,gamma`,
a common vertex must have a colour in
`{alpha,beta} intersect {alpha,gamma}={alpha}`.  A common edge is impossible:
an edge on either bichromatic path has differently coloured ends, while no
ordered pair of distinct colours belongs to both two-colour palettes.
Thus property (e) is automatic for these choices.

## Literal first boundary hits

For either boundary-block colour, no vertex of either lobe has colour
`alpha` or that block colour.  An `x`--`y` path avoiding `S` cannot enter a
different component of `G-S`, and after deleting its ends its connected
interior lies in one lobe.  Such a lobe contains neither required colour,
so this is impossible.

For a lobe colour `beta`, a path avoiding `S` again has its interior in one
lobe.  Since no lobe vertex has colour `alpha`, alternation forces exactly
one internal `beta`-coloured vertex, giving the stated two-edge path through
a common neighbour of `x,y`.  If the path meets `S`, the only boundary
vertices coloured `alpha` are `d,e`, and no boundary vertex has a lobe
colour.  Its first literal boundary hit is therefore `d` or `e`.  This is
a conclusion about actual vertices, not palette-to-label identification.

## Four-critical lobe

If a lobe is not three-colourable, choose a vertex-minimal induced
non-three-colourable subgraph.  Deleting any vertex makes it
three-colourable, while assigning the deleted vertex a fourth colour proves
four-colourability.  It is therefore an induced four-critical subgraph as
claimed.

## Lemma 3.1

If both graphs `G[L_d union {x,y}]` and
`G[L_e union {x,y}]` are three-colourable and their restrictions to
`{x,y}` have the same equality relation, a colour permutation aligns the
ordered pair and the two colourings glue to a three-colouring of `C`.

If their equality relations differ, first align the colour at `x`, then
assign `y` one fresh boundary colour—the colour of `{d,e}`—in both
colourings.  This preserves properness: the colour is absent from every
other vertex of `C`, `xy` (if present) has a differently coloured other
end, and `y` has no edge to `d` or `e`.  The glued colouring uses the three
lobe colours plus this boundary colour.  Giving `P,R,{d,e}` their three
boundary colours produces a six-colouring of the closed `C`-side with the
forbidden equality partition.

For the stronger assertion, if one full lobe-plus-cut graph is
three-colourable and the other becomes three-colourable after deleting
`y`, align the two colours at `x` and assign the same fresh root-block
colour to `y` on both sides.  Adding or recolouring `y` is proper even when
`xy` is present, for the same reasons.  This again produces the forbidden
closed-side equality response.  Symmetry in `x,y` and in the lobes proves
all displayed cases.

## Trust boundary

The five Kempe paths may share `alpha`-coloured vertices, and a lobe-colour
path may collapse to a two-edge path through one common neighbour.  The
theorem therefore does not yet produce the two disjoint labelled connected
subgraphs needed for boundary-response reflection.  Likewise, the
four-critical subgraph is not rooted at prescribed portals.  These limits
are stated accurately.

Within this scope, no gap was found.
