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
`K_5`-model transversal is no longer a separate exit: it already forces an
order-seven separation.  That separation is raw—it does not by itself
supply compatible shore colourings—so it enters rather than closes the
order-seven colour-gluing branch.

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
same eligible defect-one setup with a declared host-level parameter strictly
smaller.  No such well-founded parameter is currently proved.

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
