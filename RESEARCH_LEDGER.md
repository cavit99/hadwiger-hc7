# $HC_7$ research ledger

**Last updated:** 20 July 2026
**Authoritative status:** $HC_7$ is not proved here.

This is the sole authority for the current status of the project. Exact
theorem statements and proofs live in the linked frontier and result files;
historical programme snapshots are archived rather than appended here.

## Current frontier at a glance

### 1. Exhaustive global obligation

Let `G` be a hypothetical minor-minimal counterexample to `HC_7`. The
[audited low-degree reduction](results/hc7_low_degree_adjacent_pair_alignment.md)
and its
[boundary-aligned strengthening](results/hc7_low_degree_boundary_edge_alignment.md)
give a vertex `u`, a component `C` of `G-N[u]`, and a vertex
$z\in S:=N_G(C)\subseteq N(u)$ such that

\[
 7\le |S|\le d_G(u)\le9,
 \qquad \chi(G-\{u,z\})=6.
\]

The pair

\[
 A=G[C\cup S],\qquad B=G-C
\]

is an actual separation with nonempty open sides. The connected set `C`
and the singleton `{u}` are each adjacent to every vertex of `S`, and
$\chi(G[S])\le4$. For every nonempty independent set `I` of `G[S]`, each
closed shore separately has a six-colouring in which `I` is exactly one
boundary colour class. These two colourings need not induce the same
partition on `S-I`.

The exhaustive case map stops at the following
[pole-free bridge-composition theorem](active/hc7_bounded_interface_synchronization_frontier.md#4-primary-open-theorem).
The operation-specific paths forced by failed exact-block Kempe lifts must
produce at least one of:

1. an explicit `K_7`-minor model in `G`;
2. one complete equality partition of `S` induced by six-colourings of both
   closed shores; or
3. another full bounded-interface instance in the same graph, preserving
   the named edge-deletion response and having a strictly smaller literal
   anti-neighbourhood component.

This theorem is unproved. Relative to the audited entry reduction, it is
sufficient for `HC_7` and is the sole exhaustive all-degree obligation.

### 2. Degree-seven structural refinement

When `d_G(u)=7`, the boundary is `S=N(u)` and the exterior `G-N[u]` is
connected. Audited reductions give an exact matching description of the
boundary colourings and a boundary-labelled model of `K_7` with either one
missing edge or two adjacent missing edges.

The [generic exact-seven restart](results/hc7_generic_exact7_response_restart.md)
reduces this branch to a minimum-order selected-response interface. The
[degree-seven frontier](active/hc7_degree7_model_separator_frontier.md#generic-exact-seven-restart-and-the-remaining-terminal-theorem)
asks for the same three terminal outcomes—an explicit `K_7` model, one
common complete boundary partition, or a strictly smaller same-host
interface—in each of the remaining singleton, positive-separator-excess,
and shore-filling modes. This is a sharper conditional laboratory, not an
exhaustive replacement for the global obligation above.

One particularly reusable input is the
[exact-seven full-connected-subgraph packing theorem](results/hc7_exact_seven_packet_packing.md).
If `nu_i` is the maximum number of pairwise vertex-disjoint connected
subgraphs in open shore `i` that are adjacent to every boundary vertex,
then

\[
 \nu_1+\nu_2\le4,
 \qquad \min\{\nu_1,\nu_2\}=1,
 \qquad \omega(G[S])\le6-(\nu_1+\nu_2).
\]

Thus the packing vector is, up to orientation, `(1,1)`, `(1,2)`, or
`(1,3)`. The theorem combines an explicit clique-minor construction with
independent-block contraction and colour gluing. It does **not** supply a
small transversal, an apex pair, or a common boundary partition in the
remaining cases.

### 3. Immediate pentagonal-bipyramid laboratory

In the seven-column subbranch, the only `K_5`-minor-free seven-vertex
contact graph of minimum degree at least four is the pentagonal bipyramid;
it is edge-maximal `K_5`-minor-free. After the audited spanning and
connectivity reductions, the immediate
[paired-rooted target](active/hc7_pentagonal_bipyramid_paired_rooted_target.md#3-exact-no-four-cut-target)
is:

> For the five-connected spanning core `F` and its two literal
> root-neighbourhood sets, prove that `F` is four-colourable or contains a
> `K_5`-minor model whose five branch sets each meet both root sets.

Either conclusion closes that conditional branch. Within several audited
unbounded expansion families, incompatible cyclic orders give explicit
minor models, while compatible orders give planar or four-colourable cores.
The full paired-rooted dichotomy remains conjectural;
persistent planar reroutings are treated as the prospective structural
alternative, not as another finite residue to enumerate.

The independent Codex and Grok laboratory configuration currently freezes
this target. It does not change the authoritative hierarchy above.

## Headline audited advances

- **Bounded full interface.** Every hypothetical counterexample admits the
  order-`7`, `8`, or `9` full separation described above, with a
  four-colourable boundary and exact independent-block responses on both
  closed shores.
- **Exact-seven packing.** In the hypothetical counterexample setup, the
  displayed inequalities orient every exact order-seven interface toward
  one shore with packing number one.
- **Unbounded cycle completion.** The
  [cycle-boundary theorem](results/hc7_cycle_boundary_completion.md) closes
  the induced-cycle family under its displayed universal adjacent pair,
  exactly two connected full shores, and `K_5`-minor-after-pair-deletion
  hypotheses, by an explicit `K_7` model or a planar gluing contradiction.
- **Boundary-labelled near-clique structure.** The
  [degree-seven aligned model theorem](results/hc7_degree7_aligned_near_k7_model.md)
  retains the literal boundary labels needed for branch-set surgery.
- **First-hit reductions.** Rado--gammoid and transfer results convert much
  of the palette-to-label problem into literal first-hit geometry, but the
  final response-coupling step remains open.

## Exact trust boundary

- Exact attainment of every independent boundary block is separate on the
  two shores; it does not synchronize the rest of either colouring.
- A colour name is not a branch-set label. Any claimed minor construction
  must use literal first-hit vertices or another explicit label-preserving
  lift.
- The detailed order-eight and order-nine results are conditional
  refinements. They do not form an exhaustive fine-grained case chain for
  every original low-degree entry.
- The pentagonal-bipyramid theorems close several unbounded families, not
  all compatible cyclic-order expansions.
- Internal audits establish the repository's current trust status; they are
  not external peer review.

## Navigation

| Document | Role |
|---|---|
| [`active/hc7_live_case_dag.md`](active/hc7_live_case_dag.md) | Exhaustive global chain and exact missing arrow |
| [`active/hc7_bounded_interface_synchronization_frontier.md`](active/hc7_bounded_interface_synchronization_frontier.md) | Full all-degree theorem and guardrails |
| [`active/hc7_degree7_model_separator_frontier.md`](active/hc7_degree7_model_separator_frontier.md) | Conditional degree-seven terminal theorem |
| [`active/hc7_pentagonal_bipyramid_paired_rooted_target.md`](active/hc7_pentagonal_bipyramid_paired_rooted_target.md) | Immediate structural laboratory |
| [`active/INDEX.md`](active/INDEX.md) | Concise live navigation only |
| [`README.md`](README.md) | Durable public overview |

The complete previous ledger is preserved as the dated
[20 July 2026 archive snapshot](archive/RESEARCH_LEDGER_2026-07-20.md).
If that snapshot or any other archived file conflicts with this ledger, this
ledger governs the current programme.
