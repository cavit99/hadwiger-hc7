# Hadwiger `HC_7` research programme

## Current verdict

`HC_7` is **not proved** here.

The target is to prove that every graph with no `K_7` minor is
six-colourable.  The programme works from a hypothetical minor-minimal
counterexample `G`.  Such a graph is seven-connected, seven-chromatic,
strongly seven-contraction-critical, and `K_7`-minor-free.

This is the sole authoritative status file.  The exact proof coverage is
in [the support-six checkpoint](active/hc7_support_six_coverage_checkpoint.md).
The previous long-form status is preserved in
[`archive/`](archive/README_2026-07-15_before_support_six_checkpoint.md).

## Active global target

Let `S_{<=6}(G)` be the family of vertex supports of all `K_5` minor
models using at most six vertices.  The first support-extension rung is

\[
                         \tau(S_{\le6}(G))\le2.         \tag{1}
\]

A pair meeting **every** `K_5` model, not only the small ones, is terminal:
deleting it leaves a `K_5`-minor-free graph, which is four-colourable by
known `HC_5`; two fresh colours then six-colour `G`.

The support-six rung is not yet proved.  Its purpose is to discover a
uniform labelled-model extension principle, not to start another finite
neighbourhood census.

### Latest structural checkpoint: weighted matching deletion

The separated three-split branch now has a genuine global invariant.  If
`F` is the three-edge matching formed by the split bags and `K=G-F`, put

\[
 \lambda_F(A,B)=|A\cap B|+
 |\{e\in F:e\text{ crosses the open shores of }(A,B)\}|.
\]

The following statements are proved and independently cold-audited.

* `lambda_F` is submodular, and seven-connectivity gives
  `lambda_F>=7` on every actual separation of `K`.  Fixed roots and named
  model sides therefore turn exact weighted cuts into a genuinely
  well-founded uncrossing rank.
* Proper-minor colourings realize every nonempty equality signature on
  `F`.  At exact weighted order seven, if at least two rows cross, a
  fixed-point-free colour permutation proves that **every** endpoint
  choice leaves both shores nonempty.  Hence the endpoint choices needed
  to preserve the named split models lift literally to an exact-seven
  handoff.
* Consequently `K` is four-connected, and its entire connectivity-four
  branch is closed by a ranked, model-preserving exact-seven handoff.  The
  only label-sensitive weighted-order-seven lift not covered by the
  derangement is the already isolated one-row singleton lock.
* If the handoff is absent, `K` is at least five-connected.  Each split
  model then regenerates label-faithfully in this one common graph as its
  singleton `K_4` plus an endpoint path avoiding that clique.
* The same common deletion carries all seven non-all-proper matching
  signatures and has chromatic number five or six.  The exact new gap is
  to compose the three possibly overlapping regenerated path bags; no
  generic Kempe-equivalence or unrooted-model lift is being assumed.
* A complementary palette-component invariant is also proved and cold
  audited.  Contracting the components induced by any palette containing
  all monochromatic deleted rows gives a quotient which cannot be coloured
  by that palette.  For three rows, every all-equal colouring therefore
  supplies a literal path for one named row using at most three colours;
  in the common two-colour cell the sharper outcome is a row path or a
  triangle of three disjoint labelled carriers.  This is useful carrier
  geometry, but it does not allocate the three carriers to a common
  singleton `K_4` and hence does not close `G1` or `G2` by itself.
* There is now an exact state-level Kempe invariant.  From any nonempty
  equality state `D` and any equal row `e_i`, the unique colour missing
  from the named `K_4` gives either an `x_i-y_i` path in `K-Q_i`, or a
  literal two-colour component whose swap realizes

  \[
       D_i'=D\mathbin\triangle
       \partial_F^{\alpha,\gamma}(C_i),
       \qquad \varnothing\ne D_i'\subseteq F-\{e_i\}.
  \]

  The new state descends to the actual proper minor `G/D_i'`.  Starting
  from the all-equal state this is a strict `3 -> 1/2` first descent.
  It is not a global rank: explicit highly connected examples realize a
  double output and a directed singleton cycle.
* A second, model-side composition route now has an audited terminal
  decoder.  Contracting the three split edges gives three disjoint marked
  `K_5` cliques.  Seven disjoint Mader good paths give a literal `K_7`;
  otherwise the Robertson--Seymour--Thomas certificate has an exact parity
  and coverage count.  In the terminal disjoint `5+5+5` equality cell,
  every canonical six-cut either contains one marked contraction image or
  belongs to one unique diagonal pattern and contains two.  Hence the
  entire terminal cell is impossible when the three-edge contraction set
  is inclusion-minimal, because every six-cut of that quotient must contain
  all three marked images.  This closes the last equality matrix, not the
  earlier fan/cell induction needed to reach it.  The clean theorem still
  under test is: a six-connected graph with three disjoint marked `K_5`s in
  which every six-cut contains all three marks has a `K_7` minor.
* The tempting weaker decoder based only on weighted separator order is
  now decisively false.  There is an exact 15-vertex graph with three
  disjoint marked `K_5`s covering its vertices, weighted separator order
  seven, no genuine Mader cell, and no `K_7` minor.  Its ordinary
  connectivity is five: every minimum five-cut omits exactly one mark.
  Thus ordinary six-connectivity and the all-three-marks condition are
  essential, not bookkeeping.  Every minimum two-edge augmentation of
  this graph that repairs all five-cuts already has a `K_7`, but that is
  finite evidence rather than an unbounded proof.
* The first marked replacements in the stronger theorem are now proved
  and cold-audited.  Every six-cut has exactly two open components; the
  `|W|=6` Mader branch is impossible; and the balanced equality branch is
  impossible for `|W|<=2`.  The new `|W|=2` decoder is literal: marked
  minimum cuts force two clique rows to contact both marks, and a full
  tail component splits a mark-to-mark path into the final two bags of a
  `K_7` model.  The live balanced residue has `3<=|W|<=5`, all three marks
  in `W`, and all three rows with tails.  This advances the published
  three-clique proof but does not prove the marked theorem.
* Independently, a five-colouring of the common matching deletion with
  exactly two equal rows forces their four endpoints to induce `K_4`.
  Its four cross-edges are locally double-critical, two outside colours
  lock both rows simultaneously, and Menger gives either an exact-seven
  boundary retaining the two named models or a labelled `K_6`.  In a
  complementary formulation, any two opposite cross-edges yield three
  disjoint connected carriers meeting all four endpoints; their unresolved
  packaging requirement is pairwise carrier adjacency.  A
  nonmonotone member of the resulting four-linkage splits to a literal
  `K_7`.  A four-connected example shows that a prescribed raw
  nonmonotone path need not augment to such a linkage, even with the two
  Kempe locks.  The particular near-complete four-gate realization used
  for that falsification is now itself excluded by one uniform literal
  `K_7` decoder for all endpoint attachments; arbitrary four-connected
  residues still require additional global structure.

See
[`hc7_matching_deletion_separator_lift.md`](results/hc7_matching_deletion_separator_lift.md),
its [audit](results/hc7_matching_deletion_separator_lift_audit.md), and
the [punctured-cube note](active/hc7_three_split_cross_star_ranked_exchange.md).
The state transition and its audit are
[`hc7_missing_colour_matching_transition.md`](results/hc7_missing_colour_matching_transition.md)
and
[`hc7_missing_colour_matching_transition_audit.md`](results/hc7_missing_colour_matching_transition_audit.md).
The palette-component theorem and its cold audit are
[`hc7_kempe_component_odd_cycle.md`](results/hc7_kempe_component_odd_cycle.md)
and
[`hc7_kempe_component_odd_cycle_audit.md`](results/hc7_kempe_component_odd_cycle_audit.md).
The new conditional composition notes and cold audit are
[`hc7_decorated_three_model_hwege.md`](active/hc7_decorated_three_model_hwege.md),
[`hc7_weighted_klnz_terminal_decoder.md`](active/hc7_weighted_klnz_terminal_decoder.md),
and
[`hc7_weighted_klnz_terminal_decoder_audit.md`](active/hc7_weighted_klnz_terminal_decoder_audit.md).
The exact weighted-decoder falsifier and its verifier are
[`hc7_decorated_hwege_genuine_cell_falsifier.md`](barriers/hc7_decorated_hwege_genuine_cell_falsifier.md)
and
[`hc7_decorated_hwege_genuine_cell_falsifier_verify.py`](barriers/hc7_decorated_hwege_genuine_cell_falsifier_verify.py).
The marked-cut reduction and its cold audit are
[`hc7_marked_three_clique_cut_reduction.md`](active/hc7_marked_three_clique_cut_reduction.md)
and
[`hc7_marked_three_clique_cut_reduction_audit.md`](active/hc7_marked_three_clique_cut_reduction_audit.md).
Its first live equality cell is closed in
[`hc7_marked_three_clique_w2_closure.md`](active/hc7_marked_three_clique_w2_closure.md),
with a separate
[`cold audit`](active/hc7_marked_three_clique_w2_closure_audit.md).
The exact-two-row linkage package and its cold audit are
[`hc7_five_colour_exact_two_row_linkage.md`](active/hc7_five_colour_exact_two_row_linkage.md)
and
[`hc7_five_colour_exact_two_row_linkage_audit.md`](active/hc7_five_colour_exact_two_row_linkage_audit.md).
The uniform repair of its four-gate example and the independent audit are
[`hc7_exact_two_four_gate_decoder.md`](results/hc7_exact_two_four_gate_decoder.md)
and
[`hc7_exact_two_four_gate_decoder_audit.md`](results/hc7_exact_two_four_gate_decoder_audit.md).
The edge-local three-carrier theorem, its audit, and the scoped packaging
barrier are
[`hc7_four_edge_double_critical_carriers.md`](active/hc7_four_edge_double_critical_carriers.md),
[`hc7_four_edge_double_critical_carriers_audit.md`](active/hc7_four_edge_double_critical_carriers_audit.md),
and
[`hc7_four_edge_double_critical_packaging_barrier.md`](barriers/hc7_four_edge_double_critical_packaging_barrier.md).

## Audited frontier

The following are the main current results.

In parallel with the support-family extraction below, the earlier audited
literal-transversal and split-contraction theorems first produce a pair
whose smallest avoided `K_5` model has support six.  A normalized split
edge then either contracts inside a seven-connected quotient or lifts a
small quotient cut to an actual exact-seven adhesion.  This is a direct
input to `G1/G2`, not a third closed branch.

1. **Separated extraction.** If (1) fails, three small `K_5` supports can
   be selected with the sharp intersection bounds `3` for a `5/5` pair
   and `4` otherwise.  The all-literal branch gives `K_7`.
2. **Bounded critical kernel.** A minimal high-transversal support family
   has at most twenty-seven members.  Every member has a private
   transversal pair and graph-specific labelled arms.
3. **Cross-arm dichotomy.** Each private pair yields either a genuinely
   separated labelled triple or two unique near-identical arms
   `X+p,X+q` together with forced near-top replacement supports.  The
   first abstract draft was false in the `5/5` case; the corrected
   graph-specific theorem is independently audited.  A further
   composition theorem eliminates every rigid common-core outcome in
   which an avoided literal `K_5` meets `X`: the replacement cliques and
   a three-root cycle in the four-vertex deletion give a literal `K_7`
   model.  Two further audited theorems eliminate maximal overlap for an
   avoided order-six support, for either arm order.
4. **Terminal-rooted contraction kernel.** For any `k>=4` prescribed
   terminals in a simple three-connected graph, terminal-legal contractible
   edge descent gives a three-connected rooted minor on at most
   `k+floor(k/4)` vertices.  For five terminals the residue can be classified
   completely: the terminals root `F_5=K_1 join P_4`, a triangulated
   pentagon.  Combining its two actual rooted-bag chords with the audited
   cycle decoder closes the entire normalized arm-order-six overlap-four
   cross-arm cell to a literal `K_7`.  This is a uniform unbounded theorem,
   not a bounded-order census.  At eight terminals there is now a second
   uniform theorem: the terminals root `C_8`, `K_{3,5}`, or one explicit
   twisted `K_{3,5}` carrier.  Its hand proof and independent audit are
   complete.
5. **Four-connected rooted clique-or-fan composition.**  Given at least
   five prescribed terminals in a four-connected graph and a fixed anchor
   triple, either one anchored four-set roots `K_4`, or all terminals lie on
   one facial cycle and root `K_1 join P` with any prescribed terminal bag
   universal.  In the normalized order-five-arm, overlap-three cell this
   produces a five-good-terminal dichotomy.  A fixed nine-/ten-object
   labelled decoder, independently replayed, turns every outcome into a
   literal `K_7`; in the off-face case it is essential to keep the bad
   terminal separate from the connected peripheral remainder.  Thus this
   entire unbounded normalized cell is closed.  Its global invocation first
   prunes reducible six-supports and only then selects the critical kernel;
   irredundancy is not imposed retroactively.
6. **Full six-terminal kernel composition.**  After deleting a
   three-vertex overlap and reserving one of the seven exterior terminals,
   terminal-legal contraction reduces the other six terminals to a
   three-connected rooted kernel on six or seven bags.  A complete labelled
   carrier census has 142 edge-minimal order-six carriers and 780
   terminal-irreducible order-seven kernels.  An independently audited
   ten-object decoder composes every carrier in every noncommon boundary
   state to a literal `K_7`.  This closes the entire normalized
   order-six-arm, overlap-three cell.
7. **Fixed-pair six-terminal composition.**  In the normalized
   order-five-arm, overlap-two cell, delete the two overlap vertices and
   reserve the two private roots.  The remaining six exterior terminals
   again lie in a three-connected deletion.  The exact joined relation has
   1,419 states; 1,179 have a common rooted `K_4`, and all 240 remaining
   states compose with every one of the 142/780 six-terminal kernels to a
   literal `K_7`.  The same fixed private pair works in every state.  An
   independent enumerator reproduced the state set, kernel catalogue and
   minor certificates, including a generic detector cross-check.
8. **Exact seven-terminal kernel bundle.**  For seven prescribed vertices
   in a simple three-connected graph, terminal-legal contraction leaves
   either one of 5,495 labelled edge-minimal order-seven carriers or an
   order-eight irreducible kernel.  The latter has exactly three structural
   forms: a wheel, a distance-three one-chord rim, or one specific
   two-chord rim.  These give 30,600 labelled templates, each with its full
   legal owner-absorption bundle.  The classification and its exact
   universal/existential quantifiers are independently audited.  This is a
   general rooted-carrier theorem, not yet a composition closure.
9. **Adaptive seven-terminal composition.**  In the normalized
   order-six-arm, overlap-two cell, a fixed reserve pair is false but a
   state-dependent pair selected before kernel exposure succeeds.  The
   148,488 noncommon states reduce monotonically to 8,220 masks in 67
   symmetry orbits.  All 67 close against all 5,495 order-seven carriers
   and all 30,600 order-eight owner bundles.  An independent contraction
   search agreed with the exact detector on all 176,081 queried quotients.
10. **Reserve-triple seven-terminal composition.**  In the normalized
   order-five-arm, overlap-one cell, deleting the overlap and reserving
   three terminals again exposes the exact seven-terminal kernel.  The
   5,410 noncommon states reduce to 400 masks in six orbits, all of which
   close.  Two independent verifiers agree on every relation count,
   catalogue quantifier and branch-set certificate.  Thus every positive
   overlap cell with order-five arms is now terminal.
11. **Rigid double-root cover.** If the rigid outcome has nonempty overlap,
   every pair of vertices of the avoided support touching that overlap
   forces another small model containing both private roots.  With literal
   arms these compulsory models have a genuine two-state split-bag
   orientation.  This is the current labelled composition invariant.
12. **Disjoint three-split branch.** Minimal simultaneous contraction of
   two or three split edges either gives `K_7`, an actual exact-seven
   handoff, or a two-component boundary of order eight or nine that is
   pointwise full on both shores.
13. **Two-shore boundary absorption.** In that two-component residue from
   two or three disjoint normalized split models, every surviving
   order-eight/nine boundary is four-colourable.  The sole five-chromatic
   census exception `K_2 vee C_7` is eliminated by a separate branch-set
   theorem.
14. **Uniform common-neighbour rooted principle.** If

   \[
   \chi(J)=k+2,\quad uv\in E(J),\quad
   \chi(J-\{u,v\})\le k,
   \]

   then `N(u) cap N(v)` is colourful in the `k`-chromatic deletion.
   Whenever Strong Hadwiger holds for `k`, this gives a `K_{k+2}` model
   with singleton bags `{u},{v}`.  Martinsson--Steiner proves the needed
   strong theorem for `k=4`, so the `HC_7` four-colour branch has a
   label-faithful `K_6` model.
15. **Minimal contraction-forest saturation.** If a forest contraction is
   inclusion-minimal for lowering a quotient to `q` colours, then every
   side of every forest edge meets every non-own colour class in every
   terminal colouring.  Each one-edge predecessor has chromatic number
   exactly `q+1`.  This is simultaneous over the whole forest and is
   independently audited.

The principal theorem and audit files are linked from
[`active/hc7_support_six_frontier.md`](active/hc7_support_six_frontier.md).

## Exact live gaps

There are two live arrows.  Neither is hidden by the results above.

### G1. Decorated extraction and composition

Starting from the bounded private-pair kernel, turn the corrected
cross-arm dichotomy into one of:

* a row-compatible composition already covered by the proved split-model
  theorems;
* three disjoint normalized split models;
* a literal `K_7` or one global two-vertex transversal; or
* a state/model-preserving exact-seven handoff with a declared strict
  rank.

Bare support incidence is insufficient: explicit affine and fifteen-point
families falsify the strongest unlabelled alignment claims.  The
positive-overlap rigid cell is closed whenever the avoided support has
order five; both maximal-overlap cells are closed for an avoided order-six
support; the rooted-fan theorem closes the normalized arm-order-six
overlap-four cell; and finite rooted-kernel composition closes both
normalized overlap-three cells, both overlap-two cells, and the
order-five-arm overlap-one cell.  Hence every positive-overlap cell with
order-five arms is terminal.  The only live positive-overlap rigid cell is
order-six arms at overlap one, alongside the separated-triple branch.
Every two-set in the avoided support meeting the overlap still forces a
compulsory double-root model.  The next concrete cell is the
order-six-arm, overlap-one interface.  A complete exact eight-terminal
kernel bundle was derived and tested here, but it does **not** close this
interface.  The first of 142 minimal state orbits defeats every one of the
165 overlap-plus-triple reserves and, more strongly, every one of all 495
arbitrary four-vertex reserves.  Independent exact and SMT minor checks
agree.  Thus another single rooted carrier cannot be the next step: the
proof must couple several regenerated models, retain ambient contraction
data, or establish a simultaneous split-row/separator exchange.

### G2. Five-connected common-deletion composition

In the separated branch, three pairwise disjoint support-six models have
split edges `F={e_1,e_2,e_3}` and one common deletion `K=G-F`.

* The branch `kappa(K)=4` is closed by the weighted exact-seven theorem
  above.  This is a ranked output, not merely another separator.
* In the residual branch, `kappa(K)>=5` and `chi(K) in {5,6}`.  Every
  nonempty subset of the three rows occurs as the exact equality set of a
  six-colouring of `K`, while the all-proper state is absent.
* For each named model, `K-Q_i` is connected; an `x_i-y_i` path in that
  deletion regenerates the fifth branch bag beside the literal singleton
  clique `Q_i`.  These three paths are individually label-faithful but may
  overlap.
* The missing-colour theorem upgrades bare path existence to an exact
  alternative at every punctured-cube state: a named path, or a legal
  contraction-state transition carried by a literal two-colour component.
  At the all-equal state the first transition strictly removes the chosen
  row.  Lower-state cycling remains possible and is explicitly guarded
  against.

The live theorem is now a weighted indivisible-bundle composition theorem:
in this five-connected punctured-cube kernel, compose the three regenerated
models or the coherent transition carriers into a literal `K_7`, a global
two-vertex transversal, or a strict anchored weighted cut.  The immediate
constructive experiment starts from one common all-equal colouring and
retains the complementary colour pair of every named `K_4`; three
independently selected singleton colourings are no longer the proof
object.  Static endpoint graphs, abstract signature iteration, and a
single rooted carrier are already known to be insufficient; ambient
connectivity, literal colour components, and the weighted rank must be
used together.

## Decisive guardrails

Do not retry the following without a materially new hypothesis.

* Connectivity plus a same-shore singleton-rooted `K_6` does not force
  `K_7`; `I_2 vee` the icosahedron gives an exact two-full-shore
  counterarchitecture.
* In the five-colour leaf branch, a six-critical Hajós join satisfies all
  local chromatic equalities and has a literal `K_5` avoiding the edge,
  but has treewidth five and no `K_7` minor.
* Four-colourability, two-shore join exclusion, and every private-block
  query do not force a common boundary state.  The two parity languages on
  `K_4 dotcup K_4` are disjoint.
* The exact eight-terminal kernel bundle does not universally compose the
  remaining order-six-arm overlap-one cell, even when any four boundary
  vertices may be reserved.  See
  [`barriers/hc7_overlap_one_exact_eight_kernel_bundle_barrier.md`](barriers/hc7_overlap_one_exact_eight_kernel_bundle_barrier.md).
* Unrooted quotient regeneration supplies no labelled carrier by itself.
* Missing-colour transitions have no signature-only rank.  One singleton
  can transition to both other rows, and singleton transitions can cycle;
  see
  [`hc7_missing_colour_transition_sharpness.md`](barriers/hc7_missing_colour_transition_sharpness.md).
* No further union-size or Moser census is active.

These barriers are in [`barriers/`](barriers/); they are guardrails, not
counterexamples to `HC_7`.

## Trust labels

* **Proved:** a written mathematical proof is present.
* **Independently audited:** a separate agent cold-checked the statement
  and proof; corrections are recorded beside the theorem.
* **Computer-assisted:** the reduction and exhaustive encoding are written
  separately, and the scripts are retained in [`active/`](active/).
* **Barrier:** a concrete counterexample to a proposed intermediate lemma,
  not to Hadwiger's Conjecture.

Computational results are not treated as proofs of unbounded statements.

## Repository layout

```text
.
├── README.md    # this authoritative status
├── results/     # proved lemmas and adjacent audits
├── active/      # current spine, finite checks, and falsifiers
├── barriers/    # counterexamples to intermediate mechanisms
└── archive/     # superseded work retained for provenance
```

The project is licensed under the [MIT License](LICENSE).
