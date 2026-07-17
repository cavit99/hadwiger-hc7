# Current proof work

**Role:** navigation only.  The authoritative status is
[`../RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md).

## Primary target

[Couple a five-colour linkage to a spanning `K_6` model](hc7_adjacent_pair_palette_model_frontier.md)

Every hypothetical minor-minimal `HC_7` counterexample has an adjacent pair
whose deletion is six-chromatic.  It also has, on the common five-connected
remainder, a spanning `K_6` model and five disjoint paths whose two endpoint
sets realize the complete five-colour palettes.  The active theorem is to
choose and reroute the paths and model jointly until they give an explicit
`K_7` model, a colour-compatible order-seven separation, a global
two-vertex `K_5`-minor transversal, or a strict improvement of the declared
joint invariant.

Immediate proved inputs, each with its adjacent audit:

- [global adjacent-pair palette frame](../results/hc7_global_adjacent_pair_palette_frame.md)
- [palette-permutation linkage and contact consequences](../results/hc7_adjacent_pair_palette_linkage.md)
- [bichromatic support and exact missing-colour rotation](../results/hc7_adjacent_pair_bichromatic_support_dichotomy.md)
- [palette dichotomy for a contracted induced bipartite subgraph](../results/hc_bipartite_contraction_palette_dichotomy.md)
- [normal form and separator for concentrated colour rotations](../results/hc7_concentrated_rotation_normalization.md)
- [two-pole contact and branch-set split](../results/hc7_atomic_two_pole_contact_trichotomy.md)

The first concrete milestone is the exact three-common-branch-set profile.
Choose an induced bipartite split candidate inside a named branch set and
contract it.  Five common bichromatic components then join its two sides.
The task is to package those components against the five external model
labels, or to turn the returned literal separator into an order-seven
colour-compatible separation or fixed two-vertex transversal.  Exact
missing-colour rotations alone cannot improve the fixed model score: after
normalization they only swap inactive components, each already lying behind
a four-coloured separator.

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
- five disjoint palette paths preserve endpoint colours only up to a
  permutation and need not be bichromatic;
- an actual separator returned by a branch-set split is not automatically
  of order seven; and
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
