# Balanced order-eight completion frontier

**Status:** current conjectural target.  This file records one live
dependency chain inside the support-six programme.  It is not a proof of
`HC_7`; claim status is governed by the linked theorem and audit files and
by [`../RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md).

## 1. Exact host configuration

Let `G` be a hypothetical minor-minimal counterexample to `HC_7`.  The
current branch comes from the five-leaf star in the graph of globally
support-maximal private pairs.  It has an eight-vertex separator

\[
                 S=R\mathbin{\dot\cup}V(e)
                     \mathbin{\dot\cup}V(f)\mathbin{\dot\cup}\{x\},
                 \qquad |R|=3,                         \tag{1.1}
\]

with the following audited properties.

1. `R` is a clique.
2. `e` and `f` are disjoint edges and are anticomplete to one another.
3. Each of `e,f` is collectively adjacent to every vertex of `R`.
4. `G-S` has exactly two connected components `C,D`, each adjacent to
   every literal vertex of `S`.
5. The original five-clique
   `L=R union {ell_e,ell_f}`, its five labelled defect edges, and a second
   five-clique `Y` disjoint from `L` remain present in the host.
6. Unless a `K_7` minor or an actual order-seven separation has already
   occurred, every endpoint of `e` and `f` misses at least one vertex of
   `R`; for either edge its two endpoint nonneighbour sets in `R` are
   nonempty and disjoint.

Put

\[
                          F=\overline{G[S]}.
\]

The endpoint-rigid branch in which `F` has no perfect matching is now
eliminated at its terminal order-eight residue, modulo any earlier
order-seven-separation exit.  The live complementary case is

\[
                         F\text{ has a perfect matching}.           \tag{1.2}
\]

Equivalently, `S` has a proper partition into four independent pairs.
This equivalence is only boundary data; it is not yet a common extension
through `C` and `D`.

## 2. Exact theorem sought

Prove the following label-preserving completion statement.

> **Balanced order-eight completion.**  Under (1.1)--(1.2) and the full
> host hypotheses above, at least one of the following occurs:
>
> 1. `G` contains an explicit `K_7`-minor model;
> 2. the two closed shores have six-colourings inducing the same partition
>    of the literal boundary `S`, so the colourings glue to a six-colouring
>    of `G`;
> 3. there is a two-vertex set of support height at least seven; or
> 4. there is an actual order-seven separation which preserves the named
>    clique and defect-edge data and strictly decreases a declared
>    open-side rank.

This would eliminate the entire honest order-eight outcome of the
five-leaf-star reduction.  It would not orient the earlier order-seven
outputs, close the other private-pair kernels, or prove the full
support-six transversal theorem.

## 3. Constructive mechanism under test

Fix a perfect matching `M` of `F`.  For every pair `{a,b} in M` and either
shore, the connected set consisting of the opposite shore together with
`a,b` may be contracted in a proper minor.  A six-colouring of that minor
restricts to the retained closed shore and has this exact boundary trace:

- `a,b` receive one common colour; and
- no other vertex of `S` receives that colour.

Thus each matched nonedge can be selected as an exact colour class from
both orientations.  The live exchange problem is to combine these eight
host-realized traces using the two original five-cliques and the labelled
defect edges.  A successful transition must yield a common full boundary
partition, a branch-set construction, or a strict separator.  It is not
enough to move between abstract boundary partitions.

The independently useful all-parameter completion theorem in
[`../results/hc_uniform_boundary_repair_completion.md`](../results/hc_uniform_boundary_repair_completion.md)
is the preferred branch-set endpoint: once a compact labelled
`K_{k-2}` model is anchored to the appropriate boundary and one reserved
component plus a universal boundary vertex remain, it constructs the
`K_k` minor directly.

## 4. Guardrails

- Four-colourability of `G[S]`, or the perfect matching in `F`, does not
  synchronize the two shore extensions.  The state-free counterexamples
  are recorded in
  [`../barriers/hc7_balanced_four_colour_boundary_barrier.md`](../barriers/hc7_balanced_four_colour_boundary_barrier.md).
- Generic boundary-extension languages are too flexible.  Any positive
  theorem must visibly use contraction-critical transitions and the old
  clique/defect-edge labels.
- Simultaneous singletonization gives a spanning `K_7`-minus-one-edge
  model, but an unranked near-complete-model rotation or a separator of
  order greater than seven is not a terminal outcome.
- Do not restart a census of eight-vertex boundary graphs.  The matching
  is already known; the missing information is how its exact traces are
  realized inside the two shores.

## 5. Immediate dependencies

Read each promoted theorem with its adjacent audit:

- [five-leaf star structure](../results/hc7_star_private_transversal_large_kernel.md)
- [rooted-four reduction and exact order-eight output](../results/hc7_star_kernel_rooted_four_contraction.md)
- [endpoint-contact rigidity](../results/hc7_star_order_eight_endpoint_contacts.md)
- [elimination of the no-perfect-matching shifted residue](../results/hc7_shifted_boundary_completion.md)
- [uniform compact-model boundary completion](../results/hc_uniform_boundary_repair_completion.md)

The broader dependency chain and the still-open branches are recorded in
[`hc7_support_six_frontier.md`](hc7_support_six_frontier.md).
