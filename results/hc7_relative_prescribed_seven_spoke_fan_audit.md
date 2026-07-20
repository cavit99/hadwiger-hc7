# Audit of the relative prescribed seven-spoke fan

**Audited file:** `hc7_relative_prescribed_seven_spoke_fan.md`
**Mathematical revision SHA-256:**
`07c3c5c0df2852aea3c159f4806f5de9edac59cf4443212e897656bcf50a649e`
**Promoted revision SHA-256:**
`86ba00c00f4ffe900db1e991f95ca3907b3b63342e0ca3c665cb9c267c381bd5`
**Audit date:** 2026-07-20
**Verdict:** **GREEN.**  The prescribed-fan alternative, the
operation-specific application, and every branch-set adjacency in both
contact-minor decoders are correct at the audited revision.

The promoted revision differs from the mathematical revision only in its
status line and link to this audit.  No theorem statement or proof changed.

## 1. Prescribed-fan alternative

Let `D` be the selected first neighbours already in the boundary and `U`
the remaining first neighbours in the open component.  In

\[
                G[(C-\{v\})\cup(S-D)]
\]

set-Menger between `U` and `S-D` is applied correctly.

- A packing of order `|U|` uses every source and has distinct boundary
  ends.  Truncating at the first boundary vertex and prepending the
  prescribed edge retains the chosen first edge, keeps the paths disjoint
  outside `v`, and introduces no extra boundary vertex.
- If the packing fails, a separator `Z` of order at most `|U|-1` leaves a
  source outside `Z`.  Its component `A` has

  \[
       N_G(A)\subseteq \{v\}\cup D\cup Z,
       \qquad |N_G(A)|\le7.
  \]

  A second component of `G-S` lies outside `A union N_G(A)`, so this is a
  genuine separation.  Seven-connectivity forces equality.  Since
  `v notin A`, the returned connected set is a proper subset of `C`.

The proof also handles `U` empty separately and correctly.

## 2. Operation-specific first edges

For a proper six-colouring of `G-pv`, the endpoints `p,v` must have one
colour.  For each of the five alternate colours, the corresponding
bichromatic component containing `v` must also contain `p`; otherwise a
Kempe interchange would separate their colours and permit restoration of
the deleted edge.  The first edges of the five paths are distinct because
their other ends have distinct colours.  Together with `pv` and one more
incident edge, seven-connectivity supplies the seven prescribed spokes.

The source states the exact limitation correctly: after the Menger
rerouting, the non-direct paths retain their first edges but need not remain
bichromatic.

## 3. Contact-minor decoder

The second component `C'` is explicitly assumed adjacent to every boundary
vertex.  This is exactly the fullness required in the construction.

For each branch set of a `K_5` model in the six-vertex contact graph, the
union of its corresponding limbs is connected; contact-graph edges lift to
literal edges, so the five unions are pairwise adjacent.  Together with

\[
                    \{v\},\qquad C'\cup\{p\},
\]

they are seven disjoint connected branch sets.  The deleted edge `vp`
joins the last two special bags.  Each limb begins at a neighbour of `v`
and has a distinct boundary end, while fullness of `C'` joins
`C' union {p}` to every limb union.  These observations verify all
twenty-one pairwise adjacencies.

## 4. Paired-fan decoder

For the paired decoder, each fan uses seven distinct boundary ends and the
direct `p`-spoke, so the two fans have five or six common non-`p` ends.
The two path pieces with one common end form a connected column.  Columns
are disjoint because their interiors lie in distinct open components, each
fan is disjoint off its centre, and a relative fan path contains no other
boundary vertex.

A `K_5` model in the common column contact graph lifts to five connected
pairwise adjacent column unions.  Together with `{v,p}` and `{w}`, these
are seven disjoint connected branch sets.  The two special bags meet via
`pw`, and the prescribed first edge on each side joins each of them to
every column union.  The two edge-deletion colourings may be unrelated;
only literal paths and endpoints are used.

## 5. Trust boundary

The proof does not turn low degree, low treewidth, or four-colourability of
the abstract contact graph into a literal order-seven separator.  A
seven-connected `K_7`-minor-free two-apex planar example can have contact
graph `C_6` while every limb still has literal neighbourhood order eight.
Nor may contact graphs from two separately chosen fans be united unless a
common literal limb system or disjoint common refinement has been proved.

Contact graphs from unrelated limb systems may not be pooled.  The paired
decoder is sound precisely because the common-endpoint columns constitute
one literal disjoint system.  Accordingly, the audited theorem supplies an
unbounded fan/separator alternative and valid explicit minor decoders.  It
does not prove the remaining response-coupling implication or `HC_7`.
