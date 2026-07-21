# $HC_7$ research ledger

**Last updated:** 21 July 2026
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
- **Atomic weak-immersion classification.** The
  [atomic rounding theorem](results/hc7_atomic_weak_k7_immersion_rounding.md)
  classifies a weak `K_7` immersion having exactly one binary collision.
  The common-end case gives an explicit `K_7` minor; every other case gives
  a spanning exact `K_7`-minus-one-edge model with singleton deficient
  roots.  In the disjoint-demand case it also retains a common frame with an
  octahedral residual quotient, and a collision vertex of degree at most
  nine exposes a bounded full interface.  The
  [icosahedral barrier example](barriers/hc7_atomic_weak_immersion_icosahedral_guardrail.md)
  shows sharply that collision avoidance can relocate the collision at
  equal potential, the deficient pairs need not identify the terminal pair,
  and the proposed paired linkage can fail.  The audited
  [octahedral-frame augmentation result](results/hc7_atomic_octahedral_frame_augmentation.md)
  proves that the exact quotient is `K_8-3K_2` and any one of its three
  absent adjacencies gives an explicit `K_7` model.  A clean missing-pair
  path and a noncofacial four-connected remainder also close, as do every
  nontrivial complete substitution and every monotone augmentation of the
  icosahedral example by at most seven vertices.  The audited
  [bridge normal form](results/hc7_atomic_h0_bridge_quadrant_normal_form.md)
  gives the exact 488-case classification for one added `T`-path and
  confines every whole `T`-bridge to one of four attachment regions.  In a
  seven-connected host, the residue with at most one internal subdivision
  vertex gives an explicit `K_7` model or an exact order-seven separator;
  under strong seven-contraction-criticality that separator has the named
  proper-minor responses.  It also proves that `K_{3,2,2,2}` cannot occur as
  a subgraph of a seven-connected `K_7`-minor-free host.  The audited
  [clean-root attachment theorem](results/hc7_atomic_h0_clean_three_arm_closure.md)
  now closes every connected collision-side piece whose attachments admit
  three disjoint arms from `e,f,g`; equivalently, every surviving component
  bridge has a Hall-deficient clean-support incidence graph.  In particular,
  one contact at the third clean root and two distinct ordered contacts on
  the opposite clean--clean segment are terminal.  The audited
  [exact-quotient forest theorem](results/hc7_atomic_exact_j_minimal_forest_landing.md)
  also closes a spanning common-frame contraction when every proper
  subforest quotient remains seven-connected: only the two universal fibres
  can be nontrivial, and the host has an explicit `K_7` model or an exact
  order-seven separator with the standard proper-minor responses.  Its
  [partial-contraction barrier](barriers/hc7_atomic_exact_j_partial_contraction_lift_barrier.md)
  proves why an earlier first loss cannot be lifted by connectivity alone:
  the quotient six-cut expands to a boundary of order `6+|F_0|`, unbounded
  in the original host.  The barrier family is itself six-colourable and has
  a displayed `K_7`, so it does not survive the full hypotheses.  The audited
  [attachment-hull theorem](results/hc7_partial_loss_attachment_hull.md)
  now extracts the exact literal information which does survive that lift:
  every lifted component's attachment set spans each forest fibre, so every
  fibre leaf is adjacent to every lifted component.  It gives one exact-block
  colouring response automatically and the reverse response when another
  component has comparable attachment sets.  With one induced bipartite fibre,
  the bad quotient is exactly six-chromatic and both fibre sides meet all five
  other colour classes.  The audited
  [one-tree attachment-set classification](results/hc7_partial_loss_attachment_set_classification.md)
  makes this residue exact.  The hull condition is precisely a common-leaf
  condition.  An inclusion-minimal attachment set either lies inside another
  component's attachment set, giving the second full shore, or belongs to an
  antichain of disconnected attachment sets with private internal contacts in
  both directions.  Boundary order seven is exactly the path-fibre case with
  the two leaves as the selected attachment set, when comparison is automatic.
  Three distinctly supported common leaves close by the clean-arm theorem;
  otherwise Hall deficiency remains.  A realization theorem produces arbitrary
  such antichains under seven-connectivity and first-loss minimality alone, but
  deliberately contains a `K_7`; hence the next inference must use `K_7`-free
  labelled geometry or contraction-critical colouring.  The
  [adjacent barrier](barriers/hc7_partial_loss_chromatic_lift_barriers.md)
  shows sharply that a chorded fibre defeats the naive colour lift and that
  arbitrarily many common contacts may still occupy only two clean-support
  classes.  The adjacent
  [shared-hub defect-rotation barrier](barriers/hc7_atomic_shared_hub_defect_rotation_barrier.md)
  is an exact finite obstruction to a different shortcut: moving a common
  connector/provenance vertex changes the three absent quotient pairs, but
  need not lift to another labelled strong immersion or decrease the global
  collision potential.  Its thirteen-vertex host is only three-connected and
  three-colourable.  The audited
  [seven-fan closure](results/hc7_atomic_shared_hub_seven_fan_closure.md)
  now proves that this exact labelled obstruction is terminal in every
  seven-connected supergraph, even with arbitrarily many added vertices.
  Five checked one-edge `K_7` certificates at each of two subdivision
  vertices saturate the possible fan endpoints, force two clean paths to the
  common hub, and yield an explicit `K_7` model by a first-intersection split.
  This reusable fan-saturation mechanism does not yet reduce an arbitrary
  dirty replacement path to that thirteen-vertex labelled subgraph.  The audited
  [two-apex exclusion](results/hc7_atomic_shared_hub_two_apex_exclusion.md)
  gives an independent unbounded restriction: deleting any two vertex or edge
  objects from the exact thirteen-vertex graph leaves a checked Kuratowski
  subdivision, so no subdivision of that graph occurs in any two-apex host.
  In particular, the standard `K_2`-joined planar guardrails cannot falsify the
  exact shared-hub extension; a counterexample must weaken its literal
  subdivision structure or leave the two-apex class.  The audited
  [arbitrary-subdivision first-hit theorem](results/hc7_atomic_subdivision_first_hit_boundary.md)
  now advances that less literal case.  The two marked first-hit regions are
  anticomplete, have at least seven attachments in complementary quadrants,
  and expose an actual order-seven separator at equality.  Contacts from both
  regions inside the common `fg` route give an explicit `K_7`, as does any
  single `T`-bridge joining the open `f`- and `g`-incident route stars.  Hence
  every surviving bridge is one-sided.  A missing branch-avoiding path returns
  a separator of order eight or nine; an existing path has a normalized trace
  meeting each elementary route interval in at most one connected subpath and
  first returns outside `T_fg`.  The remaining configuration is therefore a
  genuinely multi-bridge chain through intervening route intervals, not an
  arbitrary dirty path.  The audited
  [path-absence response theorem](results/hc7_atomic_path_absence_response_boundary.md)
  now upgrades the missing-path branch: an inclusion-minimal separator in
  the nine named vertices is full on both distinguished sides, has order
  seven, eight or nine and a four-colourable boundary, realizes every
  independent boundary set as an exact block on each closed shore, and
  retains a selected edge-deletion response.  It is a bounded response
  interface, but not yet a strict same-form descent.

  The adjacent
  [dirty two-bridge-chain barrier](barriers/hc7_atomic_dirty_two_bridge_chain_barrier.md)
  refutes the bare inference that two one-sided bridges composed through one
  route interval already give a `K_7` minor.  Its exact thirteen-vertex graph
  is three-connected and four-chromatic, and the standard
  `K_2`-joined-icosahedron guardrail contains no subdivision of it.  The
  audited
  [exact-core seven-fan theorem](results/hc7_atomic_two_bridge_exact_core_seven_fan_closure.md)
  nevertheless closes that same unsplit core in every seven-connected host:
  five terminal endpoint certificates force clean fan paths to `e,x` and an
  explicit `K_7` model.  For an arbitrary subdivision, the same certificates
  confine every surviving first hit to the subdivision of the eight-vertex
  graph with edges

  \[
   qa,qg,qs,ar,rs,sc,ae,ax,ce,cg,cx,eg.
  \]

  The exact remaining local gate is to extract one fan containing both
  literal endpoints `e,x`, or convert the obstruction to such a fan into a
  bounded response interface or strict host-component descent.  The earlier
  [six-connected multipartite barrier](barriers/hc7_atomic_h0_multipartite_bridge_guardrail.md)
  shows that individually two-apex bridge certificates need not share an
  apex pair and that normalized dominating `K_5` models may regenerate
  after every two-vertex deletion without yielding the needed exchange.
  The wider remaining inference is still the interaction of dirty replacement
  paths and Hall-deficient high-attachment quadrant bridges with the first bad
  partial quotient, retaining named ownership throughout.

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
- The minimum-degree weak-immersion theorem does not force an atomic
  immersion or a collision vertex of degree at most nine.
  Contact-preserving singletonization also shows that the missed-bag
  paired-linkage formulation requires a new label-preserving ownership
  theorem.  The octahedral-frame and bridge refinements classify one path,
  confine each whole bridge, close the one-internal-vertex residue and
  exclude the multipartite saturation at seven-connectivity.  They do not
  yet combine arbitrary high-attachment quadrant bridges while retaining
  an `xe`, `ab`, or `cd` ownership augmentation, or return a strictly
  smaller full component with its named proper-minor response.  A saturating
  clean-root attachment matching is now terminal, but Hall deficiency alone
  has not been decoded.  Likewise the exact-`J` all-subsets forest landing is
  closed, but an earlier partial connectivity loss can have an unbounded
  literal lift and needs bridge ownership or chromatic response to control
  it.  Its attachment sets nevertheless span every contracted fibre tree and
  share all fibre leaves.  In the one-tree case, an inclusion-minimal set is
  either contained in another attachment set or sits in an antichain of
  disconnected sets with two-way private internal contacts; no stronger
  interval or comparison conclusion follows from connectivity and first-loss
  minimality alone.  This supplies only one closed-shore response unless a
  second component is literally full to the same boundary, and common leaves
  need not have three distinct clean-root supports.  The induced-bipartite
  one-fibre case has a stronger six-colour contact condition, but its
  label-preserving conversion remains open.  Bare reassignment of a shared
  connector/provenance vertex also fails:
  the rotated near-clique quotient need not have a labelled strong-immersion
  lift or improve the lexicographic collision potential.  The exact sparse
  example is nevertheless excluded from every seven-connected `K_7`-minor-free
  host by the new fan-saturation theorem, and no subdivision of it occurs in a
  two-apex host.  In an arbitrary subdivision, the first-hit theorem closes
  two-sided `fg` contacts and every single bridge spanning the two clean route
  stars.  The path-absence alternative now carries complete separate
  exact-block responses and a selected edge-deletion response, although it
  need not synchronize the shore colourings or give strict descent.  In the
  existing-path alternative, the exact two-bridge core closes at
  seven-connectivity and every surviving first hit is confined to the displayed
  eight-vertex skeleton.  Extracting clean paths to both `e,x`, or deriving a
  response-bearing separator from their obstruction, remains open.  The
  six-connected barrier also rules out intersecting individual two-apex
  certificates or invoking bare dominating-model regeneration.  The
  single-collision gate therefore remains open, and this route does not
  replace the primary bounded-interface obligation.
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
