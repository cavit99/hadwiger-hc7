# Current proof work

**Status:** navigation only. $HC_7$ and the two-vertex transversal theorem
for $K_5$ models on at most six vertices are not proved. The authoritative
status is
[`../RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md); the detailed coverage map
is
[`hc7_support_six_coverage_checkpoint.md`](hc7_support_six_coverage_checkpoint.md),
and the technical formulations are in
[`hc7_support_six_frontier.md`](hc7_support_six_frontier.md).

## Label-preserving extraction of compatible $K_5$ models

Starting from a bounded critical family of small $K_5$-model supports,
construct an explicit $K_7$-minor model, a two-vertex transversal, three
vertex-disjoint six-vertex $K_5$ models with their prescribed branch sets,
or an order-seven separation preserving those models and a strictly
decreasing parameter.

Immediate dependencies (read each theorem with its adjacent audit):

- [three small-support extraction](../results/hc7_support_at_most_six_separated_triple_extraction.md)
- [bounded critical support family](../results/hc7_support_six_bounded_critical_kernel.md)
- [additional models through a private transversal pair](../results/hc7_support_six_private_pair_v_extraction.md)
- [dichotomy for models through a private pair](../results/hc7_private_pair_cross_arm_dichotomy.md)
- [replacement models sharing a prescribed vertex set](../results/hc7_rigid_cross_arm_double_root_cover.md)
- [barrier to a single eight-terminal rooted-minor reduction](../barriers/hc7_overlap_one_exact_eight_kernel_bundle_barrier.md)

## Composition of three six-vertex $K_5$ models

The case in which all three two-vertex branch-set edges form an
inclusion-minimal set whose simultaneous contraction destroys
seven-connectivity is eliminated.  The remaining contraction analysis gives
either an order-seven separation not yet equipped with a strict induction
parameter, or an inclusion-minimal two-edge set whose simultaneous
contraction is not seven-connected.  Expanding the latter gives an
eight-vertex boundary and a connected subgraph adjacent to every boundary
vertex on each side.

Immediate dependencies:

- [minimal contractions destroying seven-connectivity](../results/hc7_three_split_minimal_bad_contraction.md)
- [closure of the three-edge Mader-path case](../results/hc7_three_split_marked_mader_branch_closure.md)
- [absorption across an eight-vertex boundary](../results/hc7_two_full_shore_boundary_absorption.md)
- [composition of two prescribed models through five connected pieces](../results/hc7_two_model_five_cluster.md)
- [partial ranked-exchange result and remaining open step for three deleted edges](hc7_three_split_cross_star_ranked_exchange.md)
- [weighted separation after deleting the three edges](../results/hc7_matching_deletion_separator_lift.md)
- [Kempe transition for a missing colour](../results/hc7_missing_colour_matching_transition.md)
- [two-colour component alternative](../results/hc7_kempe_component_odd_cycle.md)
- [two monochromatic matching edges](hc7_five_colour_exact_two_row_linkage.md)
- [connected subgraphs forced by four double-critical edges](hc7_four_edge_double_critical_carriers.md)
- [barrier to composing those subgraphs using adjacency alone](../barriers/hc7_four_edge_double_critical_packaging_barrier.md)

Do not reopen closed intersection configurations, the three-edge contraction
case, Moser-spindle classifications, or raw boundary-attachment catalogues
unless they directly falsify one of the two problems above.
