# Current proof work

**Role:** navigation only. The authoritative status is
[`../RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md).

## Primary target

[Balanced order-eight completion](hc7_balanced_order8_frontier.md)

Immediate proved inputs, each to be read with its adjacent audit:

- [five-leaf star structure](../results/hc7_star_private_transversal_large_kernel.md)
- [rooted-four reduction and exact order-eight output](../results/hc7_star_kernel_rooted_four_contraction.md)
- [endpoint-contact rigidity](../results/hc7_star_order_eight_endpoint_contacts.md)
- [elimination of the no-perfect-matching shifted residue](../results/hc7_shifted_boundary_completion.md)
- [canonical four-root web and localization of the second five-clique](../results/hc7_star_order_eight_rooted_web.md)
- [four-connectivity of the canonical planar web skeleton](../results/hc7_canonical_web_skeleton_four_connected.md)
- [split-edge `K_7`-minor construction](../results/hc7_star_order_eight_split_edge_completion.md)
- [closure when deleting the two clique vertices disconnects their shore](../results/hc7_star_order_eight_disconnected_leaf_side_completion.md)
- [opposite-shore proper-minor colouring incompatibility](../results/hc_opposite_shore_minor_response_incompatibility.md)
- [direct Kempe transition between opposite critical edges](../results/hc7_opposite_critical_edge_transition.md)
- [common two-edge-deletion `K_6` fork](../results/hc7_common_edge_deletion_k6_fork.md)
- [common double-contraction response](../results/hc7_common_host_double_contraction_lock_allocation.md)
- [generalized Kempe fork for two deleted edges](../results/hc7_two_deleted_edge_generalized_kempe_fork.md)
- [reachability-maximal cyclic normal form](../results/hc7_reachability_maximal_kempe_normal_form.md)
- [disjoint-palette coupling of the two critical edges](../results/hc7_disjoint_palette_two_edge_coupling.md)
- [fixed-boundary criticality of a simultaneous-equality trace](../results/hc7_double_equality_boundary_criticality.md)
- [planar tight-core structure and zero-slack four-clique closure](../results/hc7_planar_boundary_critical_core_tight_case.md)
- [explicit completion of the two-vertex critical core](../results/hc7_two_vertex_fixed_boundary_core_completion.md)
- [removable-path normalization of the facial-triangle core](../results/hc7_facial_triangle_removable_path_normalization.md)
- [uniform compact-model boundary completion](../results/hc_uniform_boundary_repair_completion.md)

Immediate guardrails:

- a perfect matching in the complement of the boundary does not by itself
  synchronize the two shore colourings;
- abstract boundary-extension languages are too flexible without the old
  clique and defect-edge labels;
- simultaneous singletonization is not terminal unless its separator or
  near-complete-model output carries a strict host rank;
- a Kempe path through a double-equality colouring does not itself transfer
  a restorable boundary response; see the
  [exact opposite-response barrier](../barriers/hc7_opposite_response_kempe_bridge_barrier.md).
- opposite cyclic paths and even a strongly connected three-colour
  component need not repair the canonical rooted web; see the
  [quotient-level web barrier](../barriers/hc7_balanced_order8_two_missing_colour_paths.md);
- four disjoint-palette replacement paths across two five-cliques do not
  force a `K_7` minor; see the
  [width-five barrier](../barriers/hc7_disjoint_palette_two_edge_decoder_barrier.md);
- local boundary locks and a planar list-critical core remain insufficient
  without `K_7`-minor exclusion and minor-minimality; see the
  [eight-connected lock barrier](../barriers/hc7_balanced_order8_double_equality_lock_barrier.md); and
- the static facial triangle, canonical web, both five-cliques, and full
  boundary data do not force completion without cut rigidity and
  proper-minor transitions; see the
  [facial-triangle barrier](../barriers/hc7_facial_triangle_static_completion_barrier.md).

The immediate open theorem is the balanced order-eight completion stated in
Section 2 of the primary target.  Its current engine is the interaction
between a reachability-maximal simultaneous-equality colouring, the planar
fixed-boundary critical core, and the canonical missing rooted linkage.
The zero-slack four-clique and two-vertex cores are closed.  The exact live
core forms are the bounded facial triangle at the opposite outer edge and
the positive-slack case.  A completion must yield a `K_7` model,
a common boundary colouring, a height-seven pair, or a strict
model-preserving order-seven separation.

For the facial triangle, path existence is now normalized: a removable
path reaches the three-clique while avoiding the two leaves and the other
two clique vertices.  The immediate local obligation is to split that
path and its connected complement without losing the six named
adjacencies in the displayed seven-branch-set construction.

## Frozen prior programme

The broader support-six and two-root colouring programmes remain developed
dependency chains, but neither is the current research engine:

- [technical frontier](hc7_support_six_frontier.md)
- [claim-by-claim coverage checkpoint](hc7_support_six_coverage_checkpoint.md)
- [two-root colouring-space frontier](hc7_two_root_colouring_space_frontier.md)

Revive a result from that programme only when it supplies an explicit
minor-model construction, separator, or proper-minor transition required by
the primary target.
