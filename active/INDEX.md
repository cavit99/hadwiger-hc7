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
- [cross-pair perfect-matching normalization](../results/hc7_balanced_cross_matching_normalization.md)
- [alignment dichotomy and Hall-obstruction closure](../results/hc7_balanced_aligned_matching_dichotomy.md)
- [all-parameter almost-universal boundary completion](../results/hc_almost_universal_straddling_completion.md)
- [endpoint allocation at the balanced boundary](../results/hc7_balanced_endpoint_allocation.md)
- [endpoint-mate exchange refinement](../results/hc7_balanced_endpoint_mate_exchange.md)
- [unique leaf--endpoint chromatic dichotomy](../results/hc7_unique_leaf_endpoint_chromatic_dichotomy.md)
- [canonical outer-edge common-neighbour completion](../results/hc7_outer_edge_common_neighbour_completion.md)
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
- endpoint-only Mader delta-matroid exchange is not label-preserving, even
  after fixed twists or static enrichment; see the
  [audited delta-matroid barrier](../barriers/hc7_labelled_mader_delta_enrichment_barrier.md).
- all exact independent-set traces from both shore contractions may still
  have disjoint extension languages; see the
  [audited aligned-trace parity barrier](../barriers/hc7_aligned_matching_exact_trace_parity_barrier.md).

The immediate open theorem is **aligned-trace lifting**, stated in Section
2 of the primary target.  In the complement of the eight-vertex boundary,
the live perfect matching contains both the prescribed common miss `xr`
and an edge crossing the two defect edges.  Every one of its four pairs is
realized as an exact boundary colour class from either shore.  The task is
to combine those host-realized traces into a common boundary partition, a
label-preserving `K_7`-minor model, a height-seven pair, or a strictly ranked
order-seven separation.

The earlier Kempe, planar critical-core, and facial-triangle results remain
available as secondary mechanisms.  They are not the current theorem by
themselves: static aligned boundary data can still fail to determine how a
colouring or clique-minor model passes through the two shores.

In the unique leaf--endpoint equality residue, the five-chromatic deletion
branch is closed by the canonical outer-edge geometry.  The surviving
six-chromatic deletion supplies a spanning `K_6` model; aligning that model
with the deleted adjacent pair is an additional concrete route into the
same host-level lifting problem.

## Frozen prior programme

The broader support-six and two-root colouring programmes remain developed
dependency chains, but neither is the current research engine:

- [technical frontier](hc7_support_six_frontier.md)
- [claim-by-claim coverage checkpoint](hc7_support_six_coverage_checkpoint.md)
- [two-root colouring-space frontier](hc7_two_root_colouring_space_frontier.md)

Revive a result from that programme only when it supplies an explicit
minor-model construction, separator, or proper-minor transition required by
the primary target.
