# Current proof work

**Role:** navigation only.  The authoritative status is
[`../RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md).

## Primary target

[Bounded-interface bridge composition](hc7_bounded_interface_synchronization_frontier.md)

Every hypothetical minor-minimal counterexample to `HC_7` now has a vertex
`u` of degree seven, eight, or nine and a component `C` of `G-N[u]` whose
boundary `S=N(C)` has order at most nine.  The second endpoint of the
adjacent-pair colouring framework can be chosen in `S`.  The boundary is
four-colourable, and both closed shores realize every independent subset of
`S` as an exact boundary colour block.

The split-boundary branch already glues.  In every remaining nonsplit case,
the exact-block Kempe theorem produces, for each `x in S`, a bichromatic
path avoiding `u,x`, with its interior wholly in one open shore.  On the
`u`-side it uses at most three other components of `G-N[u]`, each adjacent
to all but at most two vertices of `S`.  The immediate theorem is to compose
these literal paths into an explicit `K_7`-minor model, a common boundary
partition, or a strictly smaller bounded full separation with the relevant
colouring data preserved.

Immediate proved inputs, each with an adjacent audit:

- [low-degree adjacent pair and bounded full separation](../results/hc7_low_degree_adjacent_pair_alignment.md)
- [boundary-aligned adjacent pair and singleton trace](../results/hc7_low_degree_boundary_edge_alignment.md)
- [degree-nine finite local completion](../results/hc7_degree9_pole_verifier.md)
- [split-boundary synchronization](../results/hc7_split_boundary_synchronization.md)
- [exact-block Kempe reduction and pole-free bridge](../results/hc7_bounded_interface_exact_block_kempe_reduction.md)
- [two-connected boundary-core completion](../results/hc7_two_connected_boundary_completion.md)
- [two-full-shore boundary absorption](../results/hc7_two_full_shore_boundary_absorption.md)
- [cycle-boundary completion](../results/hc7_cycle_boundary_completion.md)
- [adjacent-pair palette linkage](../results/hc7_adjacent_pair_palette_linkage.md)

Immediate barriers:

- [four-colour parity-language barrier](../barriers/hc7_four_colour_parity_language_barrier.md)
- [eight-boundary state-transfer barrier](../barriers/hc7_eight_boundary_gallai_state_transfer_barrier.md)
- [two colourful sets need not share a rooted `K_4`](../barriers/hc7_two_colorful_sets_paired_k4_barrier.md)

The static obstruction is now exact: independent-block completeness alone
forces gluing precisely for split boundaries.  Every nonsplit boundary has
an abstract even/odd parity obstruction, so new work must retain the literal
Kempe paths, operation endpoints, or minor-model branch sets.

## Secondary structural laboratory

[Adjacent-pair rooted-model and component-defect frontier](hc7_adjacent_pair_palette_model_frontier.md)

The earlier adjacent-pair/five-core route remains a developed source of
label-preserving branch-set exchanges.  Its defect-one two-tree theorem is
conditional on a complete eligible path-cut configuration and is not the
global normal form.  Reuse it only when it constructs one of the branch-set
splits required by the bounded-interface target.

[Paired colourful-set rooted-`K_4` frontier](hc7_two_colorful_sets_rooted_k4_frontier.md)

This file records the detailed conditional defect-one branch and its exact
trust boundary.

## Frozen programmes

- [balanced order-eight laboratory](hc7_balanced_order8_frontier.md)
- [support-six frontier](hc7_support_six_frontier.md)
- [support-six coverage checkpoint](hc7_support_six_coverage_checkpoint.md)
- [two-root colouring-space frontier](hc7_two_root_colouring_space_frontier.md)

Revive a frozen result only when it supplies an explicit minor-model
construction, separator, or proper-minor transition required by the primary
target.
