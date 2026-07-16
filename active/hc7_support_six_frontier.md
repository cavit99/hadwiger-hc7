# Active frontier: support-six extension for `HC_7`

**Status:** active proof spine.  `HC_7` and the support-six transversal
theorem are not proved.

## 1. Target

Let `G` be seven-connected, strongly seven-contraction-critical and
`K_7`-minor-free.  Let `F` be the supports of all `K_5` models using at
most six vertices.  The active target is

\[
                              \tau(F)\le2.             \tag{1.1}
\]

The exhaustive dependency map is
[`hc7_support_six_coverage_checkpoint.md`](hc7_support_six_coverage_checkpoint.md).
The two live arrows are decorated extraction (`G1`) and forest-to-carrier
composition (`G2`).

The earlier audited literal-transversal and support-six contraction
dichotomy supply a parallel normalization: choose a pair whose smallest
avoided `K_5` support has order six, normalize its split edge, and obtain
either a seven-connected contracted host or an actual exact-seven
adhesion.  This feeds the two arrows below; it does not close either one.

Sources:

* [`../results/hc7_global_literal_k5_transversal.md`](../results/hc7_global_literal_k5_transversal.md)
* [`../results/hc7_global_support_six_contraction_dichotomy.md`](../results/hc7_global_support_six_contraction_dichotomy.md)

## 2. `G1`: global decorated extraction

The proved starting data are:

* a 3-critical high-transversal subfamily of at most twenty-seven
  supports;
* one private transversal pair for every member;
* a graph-specific arm on each endpoint of every private pair; and
* the corrected cross-arm dichotomy.

The dichotomy returns either a genuinely separated labelled triple or a
rigid certificate

\[
                      X\cup\{p\},\qquad X\cup\{q\},   \tag{2.1}
\]

together with every forced replacement `(A-a)+p,(A-a)+q` for
`a in A cap X`.

The audited literal-support composition theorem closes the rigid cell
whenever `|A|=5` and `A cap X` is nonempty.  For `a in A cap X`, the
four-clique `A-a`, the two literal replacement cliques, and a common cycle
through `a,p,q` in the four-vertex deletion form a `K_7` model.  Hence a
literal avoided support is disjoint from the common arm core.

The maximal-overlap order-six cells are also closed for both arm orders.
For order-five arms, a prescribed-edge cycle theorem composes a literal
`K_4`, two complete roots, and the disjoint `K_4`-full edge forced by the
irredundant avoided support.  For order-six arms, maximal overlap supplies
all seven six-subsets of one seven-set, forcing a small `K_6` and then
`K_7`.

There is now a uniform replacement for the first unbounded exterior step.
Given `k>=4` labelled terminals in a simple three-connected graph,
terminal-legal contractible-edge descent produces a three-connected rooted
minor on at most

\[
                         k+\lfloor k/4\rfloor
\]

vertices.  For five terminals the proof classifies every residue: the
terminals always root `F_5=K_1 join P_4`.  Its two actual rooted-bag chords
repair every crossed order left by the audited cycle decoder.  Consequently
the entire normalized arm-order-six overlap-four cell is closed to a
literal `K_7`, with no separator handoff left over.

There is now a second uniform rooted carrier.  In a four-connected graph,
fix an anchor triple among at least five labelled terminals.  Either an
anchored four-set roots `K_4`, or all terminals lie on one facial cycle and
root `K_1 join P` with any prescribed terminal bag made universal.  Applying
this to the five terminals complete to the three-vertex overlap closes the
entire normalized **order-five-arm, overlap-three** cell.  The fixed decoder
has 6,960 original completions; after common rooted-`K_4` and direct-`K_7`
outcomes, all 72 residues close.  In the off-face branch the proof preserves
the exceptional terminal as a singleton and uses the nonempty connected
peripheral remainder as a separate full carrier.  This is an unbounded
four-connected composition theorem with a fixed labelled finite layer, not
an ambient-order census.

The normalized **order-six-arm, overlap-three** cell is now terminal too.
Deleting the overlap and reserving one of the seven exterior terminals
leaves six labelled terminals in a three-connected graph.  Terminal-legal
contraction reduces them to a rooted kernel of order six or seven.  The
complete labelled guarantee consists of 142 edge-minimal order-six
carriers and 780 terminal-irreducible order-seven kernels.  An independently
audited ten-object decoder composes every one of the 7,878 noncommon
relation states to a literal `K_7`; the ambient graph remains unbounded.

The normalized **order-five-arm, overlap-two** cell is now terminal as
well.  Deleting the two overlap vertices and reserving the fixed private
pair leaves six labelled terminals in a three-connected deletion.  The
exact joined relation has 1,419 states.  A common rooted `K_4` closes 1,179
of them; an independently audited decoder composes all 240 remaining
states with every order-six carrier and every order-seven irreducible
kernel from the complete 142/780 catalogue.  The fixed private pair works
for every literal state, and every certificate lifts to a literal `K_7`.

There is now also a complete **seven-terminal kernel bundle**.  Seven
prescribed vertices in a simple three-connected graph reduce to one of
5,495 labelled edge-minimal order-seven carriers or to an order-eight
irreducible kernel.  The order-eight branch has exactly three structural
forms and 30,600 labelled templates.  For each actual template, every
neighbour of the extra bag is a legal adaptive owner.  The independently
audited decoder quantifier is therefore universal over templates and
existential over the actual owners.  This is the exact carrier input needed
for the next cell; it does not itself compose the surrounding labels.

The normalized **order-six-arm, overlap-two** cell is now terminal.  Its
148,488 noncommon states reduce monotonically to 8,220 forced-edge masks in
67 category orbits.  A fixed reserve pair is genuinely false, but a pair
selected from the state before kernel exposure closes every orbit against
all 5,495 order-seven carriers and all 30,600 exact order-eight owner
families.  Twenty-one orbits already contain `K_7`; 45 use one reserve-pair
type and one uses a second.  All 176,081 queried quotient masks were
independently checked by exact contraction search.

The normalized **order-five-arm, overlap-one** cell is terminal as well.
Deleting its single overlap vertex and reserving three of the ten exterior
terminals leaves the same seven-terminal kernel in a three-connected
deletion.  The exact relation has 5,410 noncommon states, 400 minimal masks
and six symmetry orbits.  Every orbit closes against the complete kernel
catalogue; an independent natural join and witness-return detector
reproduce the result.  Consequently all positive overlaps with order-five
arms are closed.

The rigid/private-pair hypotheses also force a **double-root cover**:
every two-set of `A` meeting `A cap X` is avoided by another small support
containing both `p,q`.  When the arms are literal, `pq` is absent and each
compulsory support has exactly one root in its split bag and the other as a
singleton.  This orientation family is the active rigid-cell object.

The remaining theorem must compose the actual five-bag labels on the
separated triple or the double-root orientation family in the rigid cells.
The only live positive-overlap rigid cell is order-six arms at overlap one.
Deleting the overlap leaves a six-connected graph with eleven exterior
terminals.  Reserving two retains four-connectivity and nine terminals;
reserving three leaves a three-connected eight-terminal problem.  The next
step must choose between a labelled four-connected carrier and a new exact
eight-terminal kernel bundle, while keeping the reserve fixed before the
carrier is exposed.
Accepted outcomes are:

1. a row-compatible one-split/two-clique composition;
2. three vertex-disjoint normalized split models;
3. a literal `K_7` or one global support-six transversal pair; or
4. a state/model-preserving exact-seven handoff with a strict declared
   rank.

Unlabelled support incidence cannot prove this.  The affine and
fifteen-point barriers remain decisive.

Sources:

* [`../results/hc7_support_six_bounded_critical_kernel.md`](../results/hc7_support_six_bounded_critical_kernel.md)
* [`../results/hc7_support_six_private_pair_v_extraction.md`](../results/hc7_support_six_private_pair_v_extraction.md)
* [`../results/hc7_private_pair_cross_arm_dichotomy.md`](../results/hc7_private_pair_cross_arm_dichotomy.md)
* [`../results/hc7_private_pair_cross_arm_dichotomy_audit.md`](../results/hc7_private_pair_cross_arm_dichotomy_audit.md)
* [`../results/hc7_literal_cross_arm_overlap_elimination.md`](../results/hc7_literal_cross_arm_overlap_elimination.md)
* [`../results/hc7_literal_cross_arm_overlap_elimination_audit.md`](../results/hc7_literal_cross_arm_overlap_elimination_audit.md)
* [`../results/hc7_k4_two_vertices_one_edge_cycle_composition.md`](../results/hc7_k4_two_vertices_one_edge_cycle_composition.md)
* [`../results/hc7_k4_two_vertices_one_edge_cycle_composition_audit.md`](../results/hc7_k4_two_vertices_one_edge_cycle_composition_audit.md)
* [`../results/hc7_cross_arm_maximal_order_six_overlap_elimination.md`](../results/hc7_cross_arm_maximal_order_six_overlap_elimination.md)
* [`../results/hc7_cross_arm_maximal_order_six_overlap_elimination_audit.md`](../results/hc7_cross_arm_maximal_order_six_overlap_elimination_audit.md)
* [`../results/hc7_rigid_cross_arm_double_root_cover.md`](../results/hc7_rigid_cross_arm_double_root_cover.md)
* [`../results/hc7_rigid_cross_arm_double_root_cover_audit.md`](../results/hc7_rigid_cross_arm_double_root_cover_audit.md)
* [`../results/hc7_five_terminal_rooted_fan.md`](../results/hc7_five_terminal_rooted_fan.md)
* [`../results/hc7_five_terminal_rooted_fan_audit.md`](../results/hc7_five_terminal_rooted_fan_audit.md)
* [`../results/hc7_cross_arm_overlap_four_cycle_decoder.md`](../results/hc7_cross_arm_overlap_four_cycle_decoder.md)
* [`../results/hc7_cross_arm_overlap_four_cycle_decoder_audit.md`](../results/hc7_cross_arm_overlap_four_cycle_decoder_audit.md)
* [`../results/hc7_four_connected_terminal_fan_or_k4.md`](../results/hc7_four_connected_terminal_fan_or_k4.md)
* [`../results/hc7_four_connected_terminal_fan_or_k4_audit.md`](../results/hc7_four_connected_terminal_fan_or_k4_audit.md)
* [`../results/hc7_four_connected_five_good_terminal_carrier.md`](../results/hc7_four_connected_five_good_terminal_carrier.md)
* [`../results/hc7_four_connected_five_good_terminal_carrier_audit.md`](../results/hc7_four_connected_five_good_terminal_carrier_audit.md)
* [`../results/hc7_overlap_three_five_good_decoder.md`](../results/hc7_overlap_three_five_good_decoder.md)
* [`../results/hc7_overlap_three_five_good_decoder_audit.md`](../results/hc7_overlap_three_five_good_decoder_audit.md)
* [`../results/hc7_overlap_three_six_terminal_kernel_closure.md`](../results/hc7_overlap_three_six_terminal_kernel_closure.md)
* [`../results/hc7_overlap_three_six_terminal_kernel_closure_audit.md`](../results/hc7_overlap_three_six_terminal_kernel_closure_audit.md)
* [`../results/hc7_overlap_two_order_five_six_terminal_kernel_closure.md`](../results/hc7_overlap_two_order_five_six_terminal_kernel_closure.md)
* [`../results/hc7_overlap_two_order_five_six_terminal_kernel_closure_audit.md`](../results/hc7_overlap_two_order_five_six_terminal_kernel_closure_audit.md)
* [`../results/hc7_seven_terminal_irreducible_kernel_classification.md`](../results/hc7_seven_terminal_irreducible_kernel_classification.md)
* [`../results/hc7_seven_terminal_irreducible_kernel_classification_audit.md`](../results/hc7_seven_terminal_irreducible_kernel_classification_audit.md)
* [`../results/hc7_overlap_two_order_six_seven_terminal_kernel_closure.md`](../results/hc7_overlap_two_order_six_seven_terminal_kernel_closure.md)
* [`../results/hc7_overlap_two_order_six_seven_terminal_kernel_closure_audit.md`](../results/hc7_overlap_two_order_six_seven_terminal_kernel_closure_audit.md)
* [`../results/hc7_overlap_one_order_five_seven_terminal_kernel_closure.md`](../results/hc7_overlap_one_order_five_seven_terminal_kernel_closure.md)
* [`../results/hc7_overlap_one_order_five_seven_terminal_kernel_closure_audit.md`](../results/hc7_overlap_one_order_five_seven_terminal_kernel_closure_audit.md)

## 3. `G2`: exact two-shore residue

For three vertex-disjoint normalized split models, a minimal bad
simultaneous contraction has one of the following proved outcomes:

* `K_7`;
* an unranked actual exact-seven handoff; or
* exactly two full open shores across a boundary of order eight or nine.

In the last case the boundary is four-colourable.  The computer-assisted
order-nine exception `K_2 vee C_7` is eliminated by a separate audited
branch-set theorem.

Sources:

* [`../results/hc7_three_split_minimal_bad_contraction.md`](../results/hc7_three_split_minimal_bad_contraction.md)
* [`../results/hc7_two_full_shore_boundary_absorption.md`](../results/hc7_two_full_shore_boundary_absorption.md)
* [`../results/hc7_universal_pair_three_core_elimination.md`](../results/hc7_universal_pair_three_core_elimination.md)

### 3.1 The new contraction-forest invariant

Choose spanning trees in the two shores and an inclusion-minimal forest
`F_0` whose contraction makes the graph five-colourable.  Put

\[
                            K=G/F_0.
\]

For every edge `e in F_0`, let `H_e=G/(F_0-e)` and let `x_e,y_e` be the
two sides of the split contraction image `z_e`.  The audited forest
saturation theorem gives, simultaneously for every edge,

\[
                    \chi(K)=5,\qquad\chi(H_e)=6,       \tag{3.1}
\]

and in every five-colouring of `K`, each side meets every colour other
than the colour of `z_e`.

If `chi(K-z_e)=4`, the uniform common-neighbour rooted theorem and Strong
Hadwiger for four colours give a `K_6` model in `H_e` with singleton bags
`{x_e},{y_e}`.  On expansion these are the two literal connected sides of
the forest cut.

Sources:

* [`../results/hc7_leaf_rooted_chromatic_drop.md`](../results/hc7_leaf_rooted_chromatic_drop.md)
* [`../results/hc7_leaf_rooted_chromatic_drop_audit.md`](../results/hc7_leaf_rooted_chromatic_drop_audit.md)
* [`../results/hc7_minimal_contraction_forest_saturation.md`](../results/hc7_minimal_contraction_forest_saturation.md)
* [`../results/hc7_minimal_contraction_forest_saturation_audit.md`](../results/hc7_minimal_contraction_forest_saturation_audit.md)

### 3.2 Exact remaining carrier problem

The next theorem must use the original shore/model attachments, not just
the six-chromatic kernel.

**Critical-image branch.**  Starting from the singleton-sided `K_6`,
produce an `S`-meeting `K_6` disjoint from a reserved connected full shore,
a literal `K_7`, one global pair, or a ranked exact-seven/labelled
near-`K_7` handoff.  Connectivity alone is false: `I_2 vee` the
icosahedron supplies a seven-connected, `K_7`-free, two-full-shore
counterarchitecture with such a `K_6`.

**Noncritical-image branch.**  If `chi(K-z_e)=5`, every five-colouring has
the exact availability trichotomy: one side sees all five colours, or both
sides have one common missing colour.  A Hajós join realizes the common
lock and has no `K_7`.  Thus the regenerated unrooted `K_5` is not enough;
ambient attachments must break the lock or expose a labelled separator.

Sources:

* [`../results/hc7_leaf_drop_five_colour_lock.md`](../results/hc7_leaf_drop_five_colour_lock.md)
* [`../barriers/hc7_leaf_drop_hajos_barrier.md`](../barriers/hc7_leaf_drop_hajos_barrier.md)
* [`../barriers/hc7_same_shore_singleton_k6_connectivity_barrier.md`](../barriers/hc7_same_shore_singleton_k6_connectivity_barrier.md)
* [`../barriers/hc7_four_colour_parity_language_barrier.md`](../barriers/hc7_four_colour_parity_language_barrier.md)

## 4. Uniform rooted principle extracted from `G2`

The following theorem is independent of the `HC_7` notation.  If

\[
 \chi(J)=k+2,\quad uv\in E(J),\quad
 \chi(J-\{u,v\})\le k,
\]

then `N_J(u) cap N_J(v)` is colourful in the `k`-chromatic deletion.
Therefore Strong Hadwiger for `k` produces a `K_{k+2}` model with
singleton branch bags `{u},{v}`.

For `k=4` this is unconditional by Martinsson--Steiner.  This closes the
palette-to-labelled-carrier gap **inside** the four-chromatic leaf kernel;
it does not supply the seventh carrier in the original graph.

## 5. Research rule

No new Moser taxonomy, raw portal classification, union-size census, or
unranked separator is admitted to this spine.  Both normalized
overlap-three cells, both overlap-two cells and the order-five-arm
overlap-one cell are closed.  The immediate `G1` experiment is the sole
remaining positive-overlap cell, order-six arms at overlap one.  It must
produce either a labelled four-connected carrier or an exact
eight-terminal kernel bundle before another finite composition layer.  A promotion
must discharge one of `G1` or `G2` for an infinite family, create
a genuinely strict handoff, or falsify the stated carrier architecture in
a way that changes the global target.
