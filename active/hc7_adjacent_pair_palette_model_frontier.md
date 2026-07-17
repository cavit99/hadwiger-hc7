# Technical frontier: coupling a five-colour linkage to a spanning `K_6` model

**Status:** active research target.  The inputs labelled as proved below
have written proofs and separate internal audits.  The exchange theorem in
Section 3 is open.  Nothing here proves `HC_7`.

## 1. Uniform setup

Let `G` be seven-connected and seven-chromatic, have no `K_7` minor, and
suppose every proper minor of `G` is six-colourable.

The audited global adjacent-pair theorem supplies an edge `zu` such that,
for `H=G-{z,u}`:

1. `chi(H)=6` and `H` is five-connected;
2. `H` has a spanning `K_6`-minor model
   `(F_1,...,F_6)`;
3. `G-zu` has a six-colouring in which `z,u` have a common colour
   `alpha`, the nonempty `alpha`-class in `H` is anticomplete to both
   poles, and both poles have neighbours in every other colour; and
4. after choosing one neighbour of each non-`alpha` colour at each pole,
   there are five pairwise vertex-disjoint paths between the two selected
   five-sets.  Their end colours are paired by a permutation.

The edge and model are not prescribed by a previous near-complete minor
model.  This loss of labels is part of the problem, not an implicit
identification.

## 2. Proved contact consequences

For a spanning model `M=(F_1,...,F_6)`, let `C_z` and `C_u` be the sets of
branch-set indices contacted by `z` and `u`, respectively.  Put

\[
 c(M)=|C_z\cap C_u|,
 \qquad
 r(M)=|C_z\cup C_u|.
\]

The audited palette-permutation theorem proves:

- `r(M)<=5` and `c(M)<=4` in a `K_7`-minor-free host;
- if `c(M)=4`, then a common branch set contains distinct pole neighbours,
  and splitting that branch set gives an explicit `K_7`-minor model or an
  actual vertex separator;
- after excluding that separator mechanism, `c(M)=3` has an exact form:
  the three common branch sets each have one common pole-neighbour, there
  is one branch set contacted only by `z`, one contacted only by `u`, and
  one contacted by neither pole; and
- in that exact form, at least two palette colours are represented in each
  exclusive branch set, and `H` contains two disjoint paths between
  selected vertices of the two exclusive branch sets.

The separator in the second item has no proved upper bound.  The disjoint
paths in the last item preserve their two endpoint palettes only up to a
permutation and may traverse the other branch sets.

## 3. Primary open theorem

### Palette-linked `K_6` exchange theorem

Under the setup in Section 1, choose jointly

- an eligible edge `zu`;
- a buffer-colour six-colouring of `G-zu`;
- one neighbour of each of the five nonbuffer colours at each pole;
- five disjoint paths joining the selected neighbour sets; and
- a spanning `K_6` model of `H`;

so as to maximize, in order,

\[
  \bigl(c(M),\ r(M),\
  -\text{number of path--branch-set interval changes},\
  -\text{total path length}\bigr).
\tag{3.1}
\]

Prove that at least one of the following occurs:

1. the data give an explicit `K_7`-minor model in `G`;
2. they give an actual order-seven separation whose boundary partition is
   induced by a named proper-minor six-colouring on both sides;
3. they identify two vertices meeting every `K_5`-minor model in `G`; or
4. a label-preserving rerouting strictly improves (3.1).

The theorem is deliberately stated with the paths and the model chosen
together.  Endpoint matchings alone, an arbitrary regenerated model, and
static boundary colouring languages have all been falsified as sufficient
invariants.

## 4. First concrete milestone

The first proof obligation is the exact three-common-branch-set case.
Let `F_z,F_u` be the two exclusive branch sets and `F_0` the branch set
contacted by neither pole.  Use the two disjoint palette paths between
`F_z` and `F_u` to prove one of:

1. a connected part can be transferred from `F_z` or `F_u` into `F_0`
   while preserving all five old branch-set adjacencies, increasing
   `r(M)`;
2. one exclusive branch set can be split into two connected parts which,
   after absorbing `z,u` appropriately, give a `K_7` model; or
3. every such transfer is blocked by one actual separator, and the
   five-connectivity of `H` plus the buffer-colour components reduce that
   separator to order five in `H`, hence order seven in `G`.

A proof must track actual vertices and branch-set adjacencies.  It is not
enough to contract each branch set to one quotient vertex or to retain only
the endpoint permutation of the five paths.

## 5. Relation to the balanced order-eight branch

The balanced order-eight configuration remains the best label-rich
laboratory.  There the eligible adjacent pair has an explicit spanning
`K_6` model with `r=5`, and that model is reversibly coupled to a spanning
`K_7`-minus-one-edge model with nonadjacent singleton deficient branch
sets.  This proves that contact maximization alone cycles; it also offers
additional fixed labels with which to test any proposed exchange in
Section 3.

The balanced branch is no longer the definition of the main theorem.
Any mechanism discovered there must be restated in the uniform setup above
or explicitly identified as using additional balanced-boundary data.

## 6. Guardrails

- The join of `K_2` with the icosahedron shows that connectivity, a
  spanning `K_6` model, and large pole contact can end in a genuine
  separator or coherent two-vertex obstruction rather than a `K_7` model.
- Five disjoint paths retain a palette permutation, not the individual
  colour pairing along each path.
- Static exact traces on a boundary can have disjoint extension languages.
- The endpoint feasibility relation of a Mader delta-matroid does not
  preserve same-branch-set adjacencies or the internal paths needed for a
  labelled clique-minor construction.
- The recent colourful-minor structure theorem treats a related
  colour-to-branch-set problem, but its general clique-minor threshold is
  far above the present `K_6` scale.  A positive result here must use the
  exact five-connectivity and minor-critical hypotheses.

## 7. Immediate dependencies

- [global adjacent-pair palette frame](../results/hc7_global_adjacent_pair_palette_frame.md)
- [palette-permutation linkage and contact consequences](../results/hc7_adjacent_pair_palette_linkage.md)
- [two-pole contact and branch-set split](../results/hc7_atomic_two_pole_contact_trichotomy.md)
- [canonical balanced deletion model and reversible exchange](../results/hc7_outer_edge_canonical_k6_rotation.md)
- [balanced order-eight technical laboratory](hc7_balanced_order8_frontier.md)
- [endpoint-only delta-matroid barrier](../barriers/hc7_labelled_mader_delta_enrichment_barrier.md)
- [static exact-trace parity barrier](../barriers/hc7_aligned_matching_exact_trace_parity_barrier.md)

## 8. Primary external inputs

- K. Kawarabayashi, A. S. Pedersen and B. Toft,
  [*Double-critical graphs and complete minors*](https://doi.org/10.37236/359),
  Electronic Journal of Combinatorics 17 (2010), R87, Theorem 7.1.
- E. Protopapas, D. M. Thilikos and S. Wiederrecht,
  [*Colorful Minors*](https://doi.org/10.4230/LIPIcs.ICALP.2026.149),
  ICALP 2026.  This is a conceptual comparison, not an invoked theorem at
  the present parameters.
