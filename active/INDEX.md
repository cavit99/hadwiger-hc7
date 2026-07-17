# Current proof work

**Role:** navigation only.  The authoritative status is
[`../RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md).

## Primary target

[Adjacent-pair colouring and rooted-model frontier](hc7_adjacent_pair_palette_model_frontier.md)

Every hypothetical minor-minimal `HC_7` counterexample has an adjacent pair
whose deletion is six-chromatic.  Its two-colour components give an exact
dichotomy.  A disconnected component exposes an actual separator.  If all
five two-colour graphs through the missed colour are connected, any one of
them is a connected dominating induced bipartite subgraph; deleting it
leaves a tight five-chromatic, `K_6`-minor-free core with two opposite
singleton-rooted near-`K_7` models.  The active theorem is to reduce the
separator to an order-seven colour-gluing interface or synchronize the two
rooted models into an explicit `K_7` model.  A global two-vertex
`K_5`-model transversal is a direct terminal contradiction: its deletion
leaves a four-colourable `K_5`-minor-free graph, and the two vertices use
two fresh colours.

Immediate proved inputs, each with its adjacent audit:

- [global adjacent-pair palette frame](../results/hc7_global_adjacent_pair_palette_frame.md)
- [palette-permutation linkage and contact consequences](../results/hc7_adjacent_pair_palette_linkage.md)
- [bichromatic support and exact missing-colour rotation](../results/hc7_adjacent_pair_bichromatic_support_dichotomy.md)
- [palette dichotomy for a contracted induced bipartite subgraph](../results/hc_bipartite_contraction_palette_dichotomy.md)
- [diagonal bichromatic components after a bipartite contraction](../results/hc_bipartite_contraction_bichromatic_components.md)
- [normal form and separator for concentrated colour rotations](../results/hc7_concentrated_rotation_normalization.md)
- [connected two-colour compression to a five-chromatic core](../results/hc7_star_kempe_five_core_compression.md)
- [exhaustive adjacent-pair separator-or-core theorem](../results/hc7_adjacent_pair_separator_or_five_core.md)
- [deficient-component separator in a contact-maximal rooted model](../results/hc7_maximal_rooted_k4_deficient_component_separator.md)
- [two-pole contact and branch-set split](../results/hc7_atomic_two_pole_contact_trichotomy.md)
- [colour-matched path from the deficient branch set to the missed pole](../results/hc7_colour_matched_repair_path.md)
- [component criterion for absorbing that path](../results/hc7_colour_matched_path_component_exchange.md)
- [fixed-path `K_7`-model-or-separation theorem](../results/hc7_colour_matched_path_exchange_or_separator.md)
- [all-cut interval and component-defect criterion](../results/hc7_colour_matched_path_all_cut_interval_exchange.md)
- [component-contact defect theorem and two-tree equality structure](../results/hc7_component_contact_defect_theorem.md)
- [normal form around a lifted simplicial component](../results/hc7_defect_one_simplicial_normalization.md)
- [path normal form for the sixth branch set of a local `K_6` model](../results/hc7_minimal_sixth_branch_set_path.md)
- [attachment forcing from proper-minor colourings](../results/hc7_edge_response_attachment_forcing.md)
- [labelled near-`K_7` model and internal-edge colouring fork](../results/hc7_defect_one_near_k7_edge_fork.md)
- [rainbow-diamond separation in the four-labelled two-tree](../results/hc7_defect_one_rainbow_diamond_separator.md)
- [connected deficient-branch-set trichotomy](../results/hc7_connected_one_hole_trichotomy.md)
- [common-neighbour-rooted fan at a double-critical edge](../results/hc7_double_critical_edge_rooted_fan.md)
- [fan collision at a globally minimum deficient branch set](../results/hc7_near_k7_minimal_path_fan_collision.md)
- [oppositely oriented boundary responses at a reversible rotation](../results/hc7_rotation_opposite_boundary_responses.md)
- [connected transfer and extremal normalization of a supported near-complete model](../results/hc7_response_collision_quasi_transfer.md)
- [bichromatic saturation or a shared-interface bypass](../results/hc7_shared_interface_bichromatic_bypass.md)
- [Hall saturation or a leaf-to-leaf bypass at a contracted portal cone (Theorem 4.3; scoped audit)](hc7_contracted_portal_path_palette_obstruction.md#theorem-43-hall-saturation-or-a-leaf-to-leaf-bypass)
- [two-vertex `K_5`-model transversals contradict seven-chromaticity](../results/hc7_two_vertex_k5_transversal_chromatic_obstruction.md)
- [classification and no-rigid-trace theorem for exact seven-vertex boundaries](../results/hc7_exact7_no_rigid_trace.md)
- [completion theorem for two full shores behind an induced cycle](../results/hc7_cycle_boundary_completion.md)
- [completion of the pentagonal order-seven separation](../results/hc7_pentagonal_separation_completion.md)
- [universal-edge Kempe normalization at the pentagonal boundary](../results/hc7_exact7_universal_edge_kempe_normalization.md)
- [exposed six-block partition and same-shore Kempe paths](../results/hc7_exact7_exposed_sigma_kempe_paths.md)
- [one-step minor dynamics and the exact common-hole law](../results/hc7_star_core_one_step_minor_dynamics.md)
- [list-colouring obstruction on a contracted induced path](../results/hc_contracted_path_list_lock.md)
- [two-vertex `K_5`-model transversal implies an order-seven separation](../results/hc7_k5_transversal_order7_separator.md)

The first constructive milestone is the
[paired colourful-set `K_4` frontier](hc7_two_colorful_sets_rooted_k4_frontier.md).
In the connected-dominating branch, deleting the poles leaves a
four-chromatic graph with two colourful pole-neighbourhoods.  A `K_4`
model whose four branch sets meet both neighbourhoods gives `K_7`
immediately.  For a contact-maximal model rooted at one neighbourhood, a
missed branch set lies in a component whose full neighbourhood is an
actual separator of order at least seven.  The contracted repeated-colour
response does not bound this expanded boundary and cannot force an exchange
by itself.  The active task is to use the literal attachments to split a
branch set and repair the one-edge-deficient model, or reduce the boundary
to an order-seven colour-gluing interface.  The current scalar invariant is
the component defect of the seven candidate sets: a density argument gives
`K_7` as soon as the total excess disconnection of pairwise unions is no
greater than the total internal component surplus.  The unmodified
near-complete model has defect one.  A continuation must make that defect
vanish or show that a defect-preserving exchange yields the order-seven
interface.  The lift to the seven-contraction-critical host must remain
explicit.

The two-tree equality classification is conditional: it applies in the
unique-deficiency path-cut branch, for a selection representing all four
protected component classes by eligible components adjacent to `z` and
adjacent to both path-side anchor sets at the chosen cut.  Those hypotheses
are not yet exhaustive.  Within that branch, the immediate target is to turn a
lifted simplicial degree-two component into an explicit `K_7` model, a
colour-compatible order-seven separation, or a new valid instance of the
same eligible defect-one setup with a strictly smaller lifted simplicial
component.  Choose `L` globally with minimum `|V(L)|` over all valid
defect-one configurations in the fixed host.  Such a configuration includes
the complete adjacent-pair, rooted-model, repair-path, admissible-cut, and
eligible labelled-component data.  Any transition must retain or explicitly
replace the literal contact witnesses and preserve the boundary equality
partition needed for gluing; triangle colours alone are not a sufficient
state.

Inside that conditional branch, the obstruction now has a standard
near-complete form.  An inclusion-maximal defect-one selection gives a
two-tree quotient; every lifted simplicial component `L` belongs to a
labelled `K_7^-` model with five common branch sets and a second deficient
branch set `R`.  Connected subgraphs outside the selected model attach only
to clique sets of quotient labels.  The distinguished sixth branch set can
be reselected locally as a singleton or an induced path whose two endpoints
each uniquely support at least two of the five common branch-set names.
These re-selections preserve the local `K_6` model but need not preserve a
valid defect-one configuration in the original host.

The whole four-labelled two-tree can now be compressed without choosing a
particular simplicial vertex.  It contains an induced `K_4^-` whose four
vertices have the four protected labels.  The shared edge separates its two
nonadjacent vertices in the contact graph.  Lifting this separation and
absorbing all adjacent outside components produces a connected open shore
whose full neighbourhood is contained in the five common branch sets of a
labelled `K_7^-` model, with the other deficient branch set on the far side.
This is an actual host separation of order at least seven.  It replaces the
unbounded two-tree geometry by one host interface, but the five supporting
branch sets may contain arbitrarily many boundary vertices.

A parameter-uniform connected-branch-set theorem now processes that
interface geometrically.  It gives an explicit `K_7` model, a nested actual
separation (full when its order is seven), or a labelled `K_7^-` or
`K_7^\vee` model whose deficient centre is a proper connected subbag of one
supporting branch set.  The last move is exactly reversible and need not
preserve the protected component label, repair path, or valid cut.  An
[infinite capped-antiprism barrier](../barriers/hc7_five_bag_separator_excess_barrier.md)
shows that even edge-maximal `K_7`-minor exclusion and maximally distributed
portals permit unbounded separator order and cyclic rotations.  That family
is six-chromatic and has a global two-vertex `K_5`-model transversal, which
the terminal chromatic theorem proves cannot survive in the actual
seven-chromatic host.  The complementary
[`K_{3,5}` boundary-language barrier](../barriers/hc7_k35_no_common_state_or_two_vertex_transversal.md)
is seven-chromatic and has no such pair, but contains a `K_7` minor and
false twins.  Together the barriers isolate global minor exclusion and
all-operation criticality as essential inputs; their complementary failure
mechanisms are recorded in the
[barrier-upgrade no-go audit](../barriers/hc7_two_barrier_upgrade_no_go.md).

The reversible rotation itself now carries a named colouring interface.
Its unique donor-side edge and a contact edge to each newly missed branch
set lie on opposite sides of one actual separation; their deletion and
contraction response languages are oppositely oriented, and any common
boundary equality partition six-colours the host.  A new connected-transfer
theorem supplies the first well-founded normalization in this route.  Among
supported one-missing-adjacency models, minimize total branch-set order and
then maximize the deficient branch set.  Every reversible outcome either
gives a `K_7` or a smaller model, or its transferred subgraph is a
vertex-minimal connected subgraph spanning the unique donor attachment, at
most two selected lost-contact portals, and all vertices with neighbours
outside the seven old branch sets.  The current theorem-level gap is now to
eliminate this atomic connected subgraph, synchronize its opposite response
languages, or turn its full-neighbourhood separation into an exact
colour-compatible order-seven separation.

If such a failure reaches an actual order-seven separation, the boundary
is no longer arbitrary.  Deleting any boundary vertex leaves a
`K_5`-minor-free graph, so the boundary is at most five-colourable.  The
five-chromatic case is exactly `K_2\vee C_5`, with two connected open
shores, and is now completely eliminated by a theorem valid for every
induced cycle of length at least four.  Martinsson--Steiner's rooted `K_4`
planarity lemma implies that either one shore supplies four rooted branch
sets, which together with the opposite shore and the two universal
vertices form a `K_7` model, or both shores embed in discs bounded by the
cycle, making the graph off the universal pair planar.  Thus the remaining
exact-seven colour-gluing problem has boundary chromatic number at most
four.  The separate Kempe-normalization results record sharper geometry in
the now-closed pentagonal case but are no longer needed to close it.

Every internal edge of `L` has an audited five-or-six chromatic response.
In the five-colour branch it is double-critical: ordered generalized Kempe
paths exist and the common neighbourhood meets every colour class.  If that
common neighbourhood meets all five named common branch sets, splitting a
spanning tree of `L` at the edge gives an explicit `K_7` model.  In the
six-colour branch, all six-colourings obey the two-pole missing-colour cover,
and one has a common-hole colouring.  The remaining theorem must convert one
of these operation-specific colour responses into the five named contacts,
a colour-compatible order-seven separation, or a smaller full valid
configuration.  Regenerating an unrooted `K_6` model is redundant: a fixed
labelled one already avoids `L`.

In the five-colour edge branch, every five-colouring uses every colour on
the common-neighbour set, and every rainbow transversal roots
`F_5=K_1\vee P_4`.  With the two operated endpoints this gives an explicit
`K_2\vee F_5` minor.  Three fan chords are still unsupported, while the
common-neighbour witnesses avoid every branch set privately supported by an
endpoint.  This sharpens the palette-to-labelled-model obstruction; it does
not repair it.

## Label-rich laboratory

[Balanced order-eight completion](hc7_balanced_order8_frontier.md)

This branch supplies additional fixed labels with which to test the uniform
exchange.  Its latest proved inputs are:

- [cross-pair perfect-matching normalization](../results/hc7_balanced_cross_matching_normalization.md)
- [alignment dichotomy and Hall-obstruction closure](../results/hc7_balanced_aligned_matching_dichotomy.md)
- [all-parameter almost-universal boundary completion](../results/hc_almost_universal_straddling_completion.md)
- [endpoint allocation](../results/hc7_balanced_endpoint_allocation.md)
- [endpoint-mate exchange](../results/hc7_balanced_endpoint_mate_exchange.md)
- [unique leaf--endpoint chromatic dichotomy](../results/hc7_unique_leaf_endpoint_chromatic_dichotomy.md)
- [canonical outer-edge common-neighbour completion](../results/hc7_outer_edge_common_neighbour_completion.md)
- [canonical deletion model and reversible exchange](../results/hc7_outer_edge_canonical_k6_rotation.md)

The canonical adjacent-pair `K_6` model is already implicit in the old
near-complete frame and lies in a reversible exchange component.  Contact
maximization alone therefore cannot orient this branch; a continuation must
use the six-colouring response.

## Immediate guardrails

- [endpoint-only delta-matroid exchange is not label-preserving](../barriers/hc7_labelled_mader_delta_enrichment_barrier.md)
- [static exact boundary traces need not synchronize](../barriers/hc7_aligned_matching_exact_trace_parity_barrier.md)
- [the full static three-common-branch-set profile can terminate at an
  order-seven separator and a fixed two-vertex planarizing
  set](../barriers/hc7_three_common_geodesic_two_apex_barrier.md)
- [two colourful sets need not share one rooted `K_4` model, even in a
  five-connected graph](../barriers/hc7_two_colorful_sets_paired_k4_barrier.md)
- [a unique forced repeated colour does not reroute a deficient rooted
  branch set](../barriers/hc7_repeated_colour_rooted_k4_exchange_barrier.md)
- [even a planar four-connected compressed core need not synchronize the
  two colourful sets](../barriers/hc7_paired_colourful_planar_core_barrier.md)
- [connectivity-only augmentation of a `K_7`-minus-one-edge model is
  open-problem strength](../barriers/hc7_eight_connected_near_k7_augmentation_hardness.md)
- five disjoint palette paths preserve endpoint colours only up to a
  permutation and need not be bichromatic;
- an actual separator returned by a branch-set split is not automatically
  of order seven; and
- even an exact order-seven separation is nonterminal until compatible
  boundary equality partitions are realized on both closed shores;
- an unrooted regenerated `K_6` model need not align with any previously
  fixed near-`K_7` labels.

## Frozen prior programmes

The following remain developed dependency chains, not the current engine:

- [support-six technical frontier](hc7_support_six_frontier.md)
- [support-six coverage checkpoint](hc7_support_six_coverage_checkpoint.md)
- [two-root colouring-space frontier](hc7_two_root_colouring_space_frontier.md)

Revive material from a frozen programme only when it supplies an explicit
minor-model construction, separator, or proper-minor transition required by
the primary target.
