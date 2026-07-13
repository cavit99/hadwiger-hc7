# Hadwiger programme: latest high-level state

> **Correction.**  Section 14's claimed complete
> (C_6\dot\cup K_1) closure is retracted.  A leaf reflection need
> not preserve the portal-cofacial face, and the rank-one SPQR inference
> is false.  The exact counterexample is
> `c6_rank_four_leaf_counterexample.py`; see
> `hadwiger_c6_closure_spotcheck_counteraudit.md`.

**Independent workspace audit, 12 July 2026.**  This is a state ledger, not
a proof announcement.  It uses the newest uniform-rooted-model notes and
does not treat an older local case report as current merely because it says
that a case is “closed.”

## Executive verdict

Hadwiger's Conjecture has **not** been proved here.  In particular,
`HC_7` is still unproved, so there is no complete argument for arbitrary
`t >= 7`.  The accepted mathematical frontier has not moved.

The programme has nevertheless produced more than another finite atlas.
It now has a coherent, parameter-uniform mechanism based on

1. exact Hall-deficit circuits for a fixed clique model;
2. genuine portal adhesions and quantified portal capacity;
3. equality-state incompatibility under opposite proper-minor operations;
4. clean portal bases in a root-shore gammoid; and
5. dynamic tree/Gallai exchange;
6. rooted Hall block-packing with omitted clique bags used as helpers;
7. exact two-gate portal amplification in the source-tight cell;
8. contact-maximal spanning normalization and root-surplus packing;
9. an exact one-surplus rooted-model theorem with three atomic
   obstruction motifs;
10. a computer-assisted closure of the exact two-full-shore
    `C_6 disjoint-union K_1` boundary cell; and
11. a portal-SDR theorem reducing normalized six-root `K_{3,3}` Kempe
    systems to cyclic/Hall-locked portal states;
12. an audited uniform double-root theorem producing two opposed
    four-bag `P_4` gates with quantified surplus and exact operation
    states; and
13. an audited arm-rotation theorem which confines every static `P_4`
    obstruction to multi-label warehouse branches in a root block/SPQR
    torso; and
14. an audited edge-contraction warehouse theorem giving a uniform
    minimum-root-bag rotation, bounded disjoint lobe charges, full
    adhesions, and opposite operation-state incompatibility without a
    spanning-model assumption; and
15. an audited bipartite-contraction co-rooting theorem placing every
    prescribed induced path, tree, or connected induced bipartite
    subgraph inside one bag of a `K_{k-1}`-model; and
16. an audited fixed-packet normal form reducing a failed third demand to
    genuine portal capture or an alternating same-vertex web, without
    pretending that two such certificates have already been exchanged;
    and
17. an audited opposite-full-shore contraction lemma forcing canonical
    two-block boundary states and exposing two explicit orientation bits
    in the rank-two theta residue; and
18. an audited theta-crossbar descent plus rooted-cycle exchange: every
    packet nonowner strictly descends, while a common owner for the two
    transverse crossbars gives an explicit `K_7` by the rooted-`K_4`
    cycle-linkage lemma; and
19. an audited, parameter-uniform rooted Hall completion theorem: a
    protected `K_{t-2}` frame with one common boundary portal and a Hall
    transversal through the other `t-2` labels, together with one full
    shore, gives an explicit `K_t` model.

That mechanism closes several genuine infinite **rooted-model cells**: the
spanning one-complex-bag equality tree/Gallai cell, broad rooted
block-packing cells, and source-tight exact two-gate cells satisfying the
stated helper-packing hypotheses.  An apparent later closure of the whole
exact multicomponent cell was retracted under audit: its absorption move is
valid, but its proposed global potential is incompatible with a
nontrivial Hall circuit.

It does not yet show that every hypothetical counterexample lies in one of
the closed cells.  Escape paths are strict labelled-model improvements,
but the improvement may exit to a higher-contact or smaller-circuit cell.
The genuine terminal formulation is the contact-maximal multiply-rooted
branch-bag split lock; the independent near-clique route still has a
three-connected/common-dark-row owner web.

The most accurate one-line description is:

> We have a genuine uniform rooted-model toolkit and a new absorption
> descent, but the contact-maximal rooted branch-bag split theorem needed to
> turn that descent into a target minor is still missing.

## I. Established background (not new to this programme)

The following facts are legitimate starting inputs.

* Hadwiger is established for `t <= 6`; the `t=5,6` cases use major known
  results (the Four Colour Theorem and the Robertson--Seymour--Thomas
  theorem), while the workspace contains elementary proofs only through
  `t=4`.
* At a least failing parameter, put `r=t-1` and choose a proper-minor-minimal
  non-`r`-colourable graph `G`.  Every proper minor of `G` is
  `r`-colourable.  For `v in V(G)`, `H=G-v` is `r`-colourable and, by the
  already established previous parameter, contains an unrooted `K_r`
  model.
* Every colour in every `r`-colouring of `H` occurs on `N(v)`.  Contracting
  `v` with any independent set `A subseteq N(v)` gives an exact trace
  colouring whose contraction colour occurs on `N(v)` exactly on `A`.
* The final inductive objective is exact: modify a `K_r` model in `H` so
  that every branch bag meets `N(v)`; then `{v}` completes a
  `K_{r+1}` minor.
* For a hypothetical `HC_7` counterexample, the ambient input used here is
  seven-connectivity of `G` and hence six-connectivity of `G-v`.

The elementary background package is recorded in
`hadwiger_complete_affirmative_results.md`; the newer programme uses the
known `t=5,6` results as black boxes.

## II. New uniform lemmas whose notes contain complete proofs

These are programme-internal theorems.  Several have been independently
challenged by other agents, but none has been externally refereed; “proved”
below means that a complete proof is present in the workspace, not that
novelty or publication-level correctness has been certified.

### 1. Crossed splicing for arbitrary faithful minor operations

If proper-minor operations are supported on opposite shores of an actual
separation and preserve the other closed shore faithfully, their colourings
cannot induce the same marked equality state on the adhesion.  If they did,
one takes from each colouring the shore on which its deleted/contracted
object is intact, aligns the adhesion colours, and splices an `r`-colouring
of `G`.

This is proved in `hadwiger_crossed_arbitrary_minor_operations.md`.  It is
the sound replacement for vague claims that “minor-critical states should
eventually synchronize.”

### 2. Hall-deficit promotion to a genuine portal adhesion

A minimal failure to link unused neighbourhood roots to a family `I` of
uncontacted model bags is an exact gammoid circuit.  It has an interface
`X` of order `|I|-1`; every proper subfamily is linkable through all of
`X`; and the root side is separated from the deficient bags by the genuine
ambient adhesion

`{v} union X union P`,

where `P` consists of portals in accessible model bags.  In a
`k`-connected host this gives both a lower bound on `|P|` and a quantified
surplus of portal vertices over accessible bag labels.

The exact circuit and promotion proof is in
`hadwiger_relative_deficit_circuit_promotion.md`.  The associated rainbow
core, label-collision, and colour-collision inequalities are in
`hadwiger_hall_circuit_anti_diamond.md`.

### 3. Clean root-shore portal bases and co-rank-one descent

Using individual portal vertices as gammoid elements, rather than using
one artificial sink per bag, gives a root-shore rank of at least
`min(k-1, |R|)`.  A minimum linkage reaches each selected portal for the
first time at its named endpoint.  In the co-rank-one case with
`k >= r+1`, this supplies two clean portal carriers simultaneously with
the complete `X` linkage.

Consequences proved in `hadwiger_corank_one_portal_basis_descent.md` are:

* the colour collision can be chosen on these clean basis portals;
* a connected split of the accessible bag which loses at most one retained
  label gives the target rooted model;
* therefore every surviving split has a named **two-label lock**; and
* any geometrically safe first-hit peel either increases contact or replaces
  the Hall circuit by a strictly smaller one.

This removes the old path-intersection ambiguity in the sharp co-rank-one
cell.  It does not remove protected-root, cut-lobe, or multi-owner
blockers.

### 4. Dynamic transition-tree collapse

For an arbitrary tree in a branch bag, colour every edge-deleted proper
minor and mark the edge by whether its forced defect colour equals the apex
colour.  Two incident lobes with the same bit either admit a clean bypass
or first hit a named foreign bag.  Hence, in the absence of those outcomes,
the tree is a path and the bits alternate.

The full-core-free statement is proved in
`hadwiger_binary_transition_tree.md`.  The stronger named-colour theorem
for a full minimal equality/list core is in
`hadwiger_dynamic_transit_tree_principle.md`.

This is a uniform geometric collapse.  It is not a termination theorem:
a clean chord can merely change the chosen spanning tree, and a foreign
transit is not automatically a legal model move.

### 5. First completely closed infinite rooted-model cell

Assume `H` has a spanning `K_r` model consisting of one complex bag `B`
and an `(r-1)`-clique of singleton bags, and assume the whole of `B` is the
minimal equality core arising from contracting it.  Then:

* every equality tree core gives a `K_{r+1}` minor;
* every equality Gallai core whose contraction-colour blocks are `K_2`s
  gives a `K_{r+1}` minor; and
* the remaining rigid alpha/delta Gallai web also gives a `K_{r+1}` minor,
  by the leaf-carrier/opposite-owner argument.

The proofs are in `hadwiger_spanning_singleton_gallai_layer_theorem.md`,
`hadwiger_dynamic_transit_tree_principle.md`, and
`hadwiger_alpha_block_leaf_carrier.md`.  They are uniform in `r`, the size
of `B`, its branching, and the block orders.  This is an actual infinite
family closure, although it is a strongly structured rooted-model family,
not a new value of Hadwiger's Conjecture.

### 6. Proper cores collapse to clean ears; the terminal society is
2-connected

In the same spanning one-complex/singleton model, an arbitrary proper
connected core has either a clean ear through a component of `B-R` or the
target `K_{r+1}` minor.  Iteration makes the whole bag a relative ear
closure.  In a target-minor-free instance, `B` is 2-connected and every
singleton bag has at least two distinct portals in `B`.

This is proved directly from `r`-connectivity in
`hadwiger_spanning_singleton_core_exchange_dichotomy.md`.  The remaining
step is dynamic: absorbing an ear must preserve or improve the selected
uncolourable core.  Static 2-connectivity and portal multiplicity do not
force the required split.

### 7. Safe foreign-transit cycles terminate

Choose a contact-maximal spanning clique model and then minimize its bag
sizes lexicographically.  Legal lobe transfers form an acyclic directed
graph.  Hence every closed foreign-transit/owner descent reaches a lobe
which either wholly owns at least two bag labels or is protected by the
contact root.  With two complex bags, contracting one gives either an ear
closure or an explicit quotient deficit of order at most `r-2` outside the
contracted bag.

These results are in `hadwiger_foreign_transit_cycle_potential.md`.  The
same note gives a sharp counterarchitecture showing why “foreign transit”
alone is not a model operation.

### 8. Uniform rooted block-packing and helper absorption

Suppose accessible rooted pieces and far Hall carriers already provide the
two sides of a prospective rooted clique model.  If the deficient old
clique labels can be partitioned into groups each adjacent to every
accessible piece assigned to it, merging each group into its far carrier
gives the target model.  An omitted old clique bag may instead be absorbed
as a helper into an accessible piece, repairing two complementary defects
at once.

This is proved in `hadwiger_corank_one_block_packing_web.md` and
`hadwiger_B_gated_capacity_state.md`.  It closes the opposite-singleton
defect and all sufficiently broad crossing-label patterns without fixing
the order or internal structure of the accessible bag.

### 9. Width-two label web and rooted-triangle closure

In a target-free 2-connected portal society, every bipolar sweep has at
most three active deficient-label intervals, and every mixed past/future
cut has at most two active labels.  For `HC_7`, a rooted triangle whose
three pieces each see at least three of the five deficient clique bags
gives `K_7`; the two exceptional support masks are closed by helper
absorption.  Thus every surviving rooted triangle contains a sparse piece
seeing at most two labels.

The proof and the exact Two Paths/web alternatives are in
`hadwiger_corank_one_block_packing_web.md`.  This replaces an unbounded
portal-order enumeration by a uniform two-active-label web, but does not
yet eliminate its named owner blocker.

### 10. Third-portal or exact two-gate source dichotomy

In the co-rank-one `(r+1)`-connected cell, portal-basis exchange gives one
of three exact outcomes: a third clean portal, an ambient adhesion of order
`r+1`, or the minimum-degree source-tight form

`N(v)-Q = X dot-union {y1,y2}`

with `|X|=r-2` and the two gates separating the interface roots from the
portal shore.  Every component beyond the gates has at least `r-1`
distinct portal neighbours.  If there are exactly `r-1` portals, every
such component has the same exact boundary `Y union P`.

This is proved in `hadwiger_B_gated_capacity_state.md` and
`hadwiger_source_tight_two_gate_web.md`.

### 11. Omitted-bag and label-escape absorption: valid descent, retracted closure

Assume the exact two-gate cell has at least two components.  If a portal's
private region sees a deficient label and wholly owns at most one label,
omit the appropriate label from the far Hall certificate and absorb that
entire old clique bag into one gate branch.  The second exact component is
a hub for the complementary part of the accessible bag.  The resulting
`r` rooted branch sets are explicit and give `K_{r+1}`.

Consequently at least `ceil((r-1)/2)` private regions are completely
label-dead.  Choose a contact-maximal labelled model, minimize its Hall
circuit, and then maximize the accessible bag.  A dead singleton is a
strict root-hub improvement.  A nontrivial dead region has a first-hit
escape.  If that escape returns to the accessible bag it enlarges the bag;
if it ends in a deficient clique bag, absorb every path vertex except its
last endpoint.  The last edge retains the named interbag adjacency, all
absorbed vertices are root-free and off-model, contact is unchanged, and
the bag again strictly enlarges.  Both endpoint types contradict the same
well-founded potential.

Thus, inside a comparison class which preserves the contact and circuit
coordinates, the family

`|P|=r-1 and c(U-Y)>=2`

has no terminal representative.  The absorption move is correct and
uniform in `r`; it is recorded in
`hadwiger_exact_gate_escape_absorption_closure.md` and independently in
Section 5 of `hadwiger_exact_gate_omitted_bag_absorption.md`.

The initially claimed target-minor closure was withdrawn.  A globally
contact-maximal model cannot support a Hall circuit of order greater than
one: every singleton proper subset is linkable and would augment contact.
Hence the claimed max-contact/min-circuit/max-bag domain is empty for the
co-rank-one cell.  The valid result is a trichotomy: absorption produces
more contact, a smaller circuit, or a strict same-coordinate bag growth.
The eventual exit still requires a rooted split theorem.

### 12. Contact-maximal spanning normalization and root-surplus packing

Every contact-maximal clique model in connected `H` can be made spanning
without changing which bags meet `N(v)`: unused components containing a
root can attach only to already contacted bags, while root-free components
may be assigned arbitrarily.  Consequently, in the terminal `HC_7` cell
with five contacted bags, all seven roots lie inside those five bags.  The
root surplus is therefore realized either by a triple-root bag or by two
double-root bags.

The explicit block-packing theorems are recorded in
`hadwiger_contact_maximal_root_surplus_packing.md` and
`hadwiger_contact_max_surplus_root_packing.md`.  They close broad crossing
patterns, give a valid two-helper compression in the triple-root case, and
reduce simultaneous double-root splits to an exact seven-piece support
graph.  Exhaustive mask checks leave ten maximal triple-root masks and
three matched-frame double-root masks; these are structural owner locks,
not a proof of `HC_7`.

### 13. Exact one-surplus rooted-model principle

Let `r+1` disjoint connected rooted pieces have support graph `Q`.  They
can be grouped, without splitting any piece, into an `N`-meeting `K_r`
model exactly when the complement of `Q` contains none of `K_3`, `P_4`,
or `3K_2` as a subgraph.  These are the three and only three
inclusion-minimal one-surplus failures.

When the pieces form a spanning partition of a `k`-connected graph, each
failure produces a genuine full-shore separator: the `K_3/P_4` motifs
concentrate it in `r-2` named pieces and the `3K_2` motif in `r-1`.  Thus
in `H=G-v` for `HC_7`, the separator has order at least six and has portal
surplus respectively at least two or one.  At equality it lifts with `v`
to an exact order-seven adhesion in `G`.

The same note proves the exhaustive four-pattern grouping theorem for
`r+2` rooted pieces after one named piece splits.  A multiply hit universal
piece opens the `K_3` motif if its two adjacent halves each see two triangle
vertices, and opens the `P_4` motif if the halves see the two opposite
end-pairs.  Persistent failure is therefore a one-sided portal-order
obstruction, not merely a contact deficit.

The proofs are in `hadwiger_one_surplus_rooted_model_principle.md`.  This
is the clearest parameter-uniform rooted-model principle obtained so far.
Its missing dynamic converse is precise: use the all-proper-minor colouring
states to force one of the sufficient bisections, or splice across the
exact adhesion.  Static portal multiplicity does not provide that step.

### 14. Exact two-full-shore `C_6 disjoint-union K_1` closure

The sole six-missing-edge boundary type in the exact order-seven,
two-full-shore equality cell is eliminated.  The proof is uniform in the
orders of the two shores: frame ownership forces a high-owner shore;
generalized Two Paths completions become bare four-webs; Hall gives a
portal transversal; three-connected shores die by simultaneous circular
order; and the remaining SPQR leaf reduces to the verified one-ear
frontier and a `K_{3,3}` planar contradiction.

The dependency audit reran the finite order-four/five certificates, both
circular-state checks, the one-ear 1,899,612-partition check, fan models,
and the final `K_{3,3}` verifier.  It found one statement repair, now made
in `hadwiger_c6_core_closure.md`: the theorem must assume Dirac's local
inequality `alpha(N(x)) <= d(x)-5` (or seven-contraction-criticality), not
minimum degree seven alone.  The exact safe theorem and audit are in
`hadwiger_c6_closure_dependency_audit_2026-07-12.md`.

This is a genuine computer-assisted infinite-family closure.  It does not
show that every `HC_7` counterexample reaches this equality cell.

### 15. Portal-SDR theorem for `K_{3,3}` routing systems

In a minimum normalized `K_{3,3}` Kempe witness, let `I_j` be the set of
row paths containing all three first portals in column `j`.  If the three
sets `I_j` have distinct representatives, the representatives explicitly
give three disjoint path bags; together with the three singleton row roots
they form the required rooted `K_{3,3}` certificate.

Every empty `I_j` has one exact form: its three first-portal supports are
the three two-subsets of a three-element set, cyclically arranged.  Hence
a normalized counterexample is reduced, at arbitrary color-class order,
to a cyclic portal lock or a three-set Hall lock, and the symmetric lock
on the other bipartition.  The proof and exact small-witness falsification
checks are in `hadwiger_k33_portal_sdr_lemma.md` and
`trianglefree_six_property_search.py`.

This is a uniform structural reduction, not yet a proof that `K_{3,3}`
has property (*).  Moreover, a property-(*) theorem alone would not finish
the degree-seven `HC_7` cell: one color is repeated on `N(v)`, and a chosen
representative of that color need not share every required Kempe component.

### 16. Sharp negative result for birooted `K_4` transport

The tempting statement that two separately colorful four-root sets in a
five-connected four-colorable graph share a `K_4` model meeting both sets
is false.  The exact counterexample `P_4 join P_4`, with explicit colorful
sets, even arises from a common compression with four color-matched Kempe
carriers.  Thus common compression origin, five-connectivity, separate
Strong-Hadwiger-4 models, and those carriers still do not synchronize the
branch sets.  The proof and exhaustive verifier are in
`hadwiger_birooted_k4_transport_audit.md` and
`birooted_k4_five_connected_counterexample.py`.

No six-connected counterexample has been found, but no theorem is being
claimed.  The induced four-color slice in the `HC_7` application need not
inherit ambient six-connectivity.

### 17. Reserved-connector/full-adhesion theorem and the universal
degree-seven `P_4` state

Let `v` have degree seven in a hypothetical `HC_7` counterexample and
use an exact trace with repeated nonedge pair `a,b`.  The other five
neighbors have unique colors.  Their missing-edge graph is triangle-free
on five vertices, hence has at most six edges; Kriesell--Mohr therefore
gives a rooted model for that missing graph, and the actual root edges
complete it to a rooted `K_5` model avoiding `a,b`.

A uniform lemma now gives the exact next step.  For any rooted `K_m`
model and two outside vertices which together see every model root,
either an outside path joins the two vertices and completes a
`K_{m+1}` model, or the model union contains a full separator of order at
least the ambient connectivity.  If connectivity exceeds `m`, a named
model bag is multiply hit.

For degree-seven `HC_7`, the outside path gives `K_7` immediately.
Otherwise the two components containing `a,b`, together with the five
model bags, have exactly the atomic missing-`P_4` support state from the
one-surplus theorem.  Each shore has at least six portal vertices
concentrated in at most four named bags, hence portal surplus at least
two.  At separator equality, adjoining `v` gives an exact full
seven-adhesion.  A label-preserving split of either private bag is proved
to close the `P_4` explicitly.

The complete proof is in
`hadwiger_reserved_connector_adhesion_principle.md`.  It replaces all
degree-seven neighborhood labels by one uniform two-shore state.  It does
not yet force the final private-bag split; that dynamic operation-state
step is now the exact degree-seven gap.

### 18. Audited double-root capacity--state gate

The repeated-pair theorem has now been sharpened uniformly.  In a
`k`-connected host, a rooted `K_m` model and two outside terminals which
jointly contact every root either extend to a terminal-meeting
`K_{m+1}` model or force two oppositely oriented separators.  Each
separator lies in only `m-1` named bags and has portal surplus at least
`k-m+1`.  For `HC_7`, these are two four-bag separators of order at least
six.

At equality, adjoining the apex gives a full seven-adhesion.  Faithful
opposite edge-transition states are disjoint, and a simultaneous pair of
portal-edge contractions forces one shore to carry a bichromatic detour or
an actual gate-reaching carrier for every other colour.  Combining this
with the audited order-seven full-shore package proves that every such
equality boundary has at least seven missing edges.  The two-shore row has
an actual crossed cyclic-hull bad split; the three-shore row is either the
`3,2,2` three-colour boundary or the pure Moser spindle.

The proof and independent audit are
`hadwiger_double_root_p4_capacity_state.md` and
`hadwiger_double_root_p4_capacity_state_adversarial_audit.md`.  The Kempe
lock does not yet preserve the five old bag labels, so this remains a
structural advance rather than a closure of degree seven.

### 19. Repeated-root split forced at every equality gate

At the two-shore equality gate, the boundary complement has at least
seven edges.  Consequently at least three boundary labels have boundary
degree at most four.  Minimum degree seven and fullness of both shores
force each such label to have two portals in one shore; two labels repeat
in the same shore.  The label-free root-multiplicity theorem now gives a
connected covering split with both labels on both sides, or an internal
cutvertex.  The cutvertex outcome produces either a nested exact
seven-cut or a connected split whose two rows are both full.

For every resulting split, each side's actual interface-neighbour set has
size at least its boundary defect.  Equality is a nested exact seven-cut;
otherwise there is strict interface surplus.  Thus the equality residue
is now a strict double-overlap covering bad split with its minor-transition
state, or a nested minimum adhesion.

At the sharp seven-missing-edge layer, an exact quotient audit gives an
additional finite funnel.  When exactly three labels have low boundary
degree, the missing graph is a triangle with four leaves.  Every leaf
distribution except `(2,1,1)` is `K_7`-positive after the repeated-root
split.  The balanced distribution has ten negative rows for each common
triangle pair, and all thirty force one prescribed two-linkage into the
same shore as the repeated-root split.  That packet alone closes the
balanced row: after making its two carriers adjacent, the seven bags
displayed in Lemma 4.3 give a `K_7` model.  Thus the entire
**three-high-degree** seven-missing-edge layer is eliminated.  The theorem and verifier are
`hadwiger_equality_repeated_root_split.md` and
`equality_gate_repeated_root_verify.py`.

This is a new derivation of the portal split, not its final exchange.  The
remaining seven-edge graphs have now also been passed through a uniform
compatibility/packet funnel.  Exact-block nonsplitness and the two-helper
test leave 31 unlabelled boundary types.  Full-split cyclic-hull closure
eliminates 18.  Define the compatibility graph on sparse boundary labels
by joining a pair when every covering split sharing that pair is
`K_7`-positive.  Portal multiplicity two-colours this graph by shores, so
a nonbipartite compatibility graph closes or descends; modulo nested
exact-cut descent, this removes three additional types beyond the cyclic
closure.

The final ten types have a common rooted-linkage form.  Seven contain a
fully positive matching-packet triangle: all three pairwise two-linkages
are forced across the shores, but a simultaneous three-linkage in either
shore gives `K_7` for every connector-tree centre.  Two are oriented
centre-locked variants, and the last is a rank-two theta packet core.
This classification and its explicit branch-bag certificates are
`hadwiger_equality_seven_edge_packet_funnel.md` and
`equality_gate_seven_edge_packet_atlas.py`.  The 31-type universe,
graph6 manifest, cyclic-hull witnesses, compatibility filter, all
connector-tree centres, and the exhaustive `7+2+1` residue have now been
independently replayed; the audit is
`hadwiger_equality_seven_edge_packet_funnel_audit.md`.

The remaining task is consequently a state-decorated packet exchange:
turn a pairwise-but-not-triple rooted linkage system into a bounded-
adhesion rope/ladder descent or a common colour-gluable operation state.
This is uniform across the ten boundaries.  Larger missing-edge layers
remain beyond it.

The first uniform one-packet normal form toward that exchange is now proved in
`hadwiger_uniform_three_demand_exchange.md`.  Given a linkage for two of
three portal demands, enlarge its carriers to adjacent rails.  If the
third carrier cannot be added, then either one residual endpoint portal
set is wholly captured by the two actual rails, or contracting the rails
produces a crossless generalized-Two-Paths web with explicit alternating
frame `(third-left, rail 1, third-right, rail 2)`.  This is an actual
set-terminal certificate, not a symbolic portal order.

At a strict seven-connected equality gate every captured boundary class
has at least two portal vertices.  Every off-rail web cell either contacts
at least five boundary labels, exposes a cut of order at most six, or
gives a nested exact seven-cut.  Proper-minor criticality further makes
the remaining rail web state-rigid: an interface transition is accepted
by the opposite shore and rejected by the original shore, satisfies the
Kempe detour/two-anchor alternative, and cannot be repaired by any
boundary-fixing web switch.  Opposite-shore transition-state sets are
disjoint.

Three exact counterexamples delimit the result.  A two-hub shore with two
portals per label has all pair packets but no triple, showing the sharp
two-vertex capacity cut.  A triangular-prism shore is three-connected
and pairwise-but-not-triple, but necessarily captures an omitted portal;
thus the capture alternative cannot be removed.  A separate
three-connected eight-vertex shore has clean pair linkages avoiding all
omitted terminals but no triple linkage; this shows that even after
capture is excluded a genuine alternating web remains.  The verifier is
`three_demand_exchange_counterexamples.py`.

For a fully positive packet triangle, one shore owns at least two packets
sharing a demand.  It now carries two capture/alternating-web
certificates.  There are three exact unproved branches, not one:

* **web--web:** align the two realizations of the shared demand by a
  common-rail exchange, or export a bounded rail-containing adhesion;
* **capture--web:** transfer the multiply represented captured class
  through the other packet's state-rigid web, or export such an adhesion;
* **capture--capture:** exchange two captured portal classes carried by
  potentially unrelated rail systems, or export such an adhesion.

Portal multiplicity alone does not turn either capture branch into the
web--web branch.  The uniform theorem therefore isolates the complete
three-branch packet residue but does not yet close it.  The static
trichotomy, separator loads, faithful operation-state splice, and all
three counterexamples have passed adversarial audit; the trichotomy is
GREEN while its use as a completed dynamic exchange is AMBER.  See
`hadwiger_uniform_three_demand_exchange_audit.md`.

### 19b. Canonical two-block states in the theta core

If `P,Q` are disjoint nonempty independent boundary blocks, their
remainder is a clique, and two opposite full shores are available, then
simultaneously contracting one shore with `P` and the other with `Q`
forces the exact state

```text
P | Q | singleton remainder vertices.
```

The two contracted images and the remainder form a clique, so this state
is independent of the colouring chosen for the proper minor.  Whenever
an exact-block hyperedge has only this state and one other, the two states
extend opposite shores.  If two such constraints share the same canonical
state, their orientations necessarily agree; only constraints with
different canonical states can retain relative freedom.

For the theta type `FwJG?`, the two forced canonical states are
`012|3|45|6` and `015|24|3|6`.  Exact NAE enumeration over all ten packet
residues finds precisely their two associated two-state constraints and
no others.  A second verifier, independent of the atlas and spectra code,
enumerates all 19 states and all 12,987 Property-B colourings modulo shore
swap.  It confirms both forced pairs and exhibits all four labelled
assignments of the canonical bits.  These abstract assignments do not
assert shore extension; actual membership of the four canonical states
comes from the two-element exact-block theorem.

The forced pairs now yield actual geometry through a label-free
merge-pair carrier lemma: two exact states oriented to opposite shores and
differing only by merging singleton blocks `{x},{y}` force an external
`xy` Kempe path in both shores whenever the merged state leaves a boundary
colour unused.  Hence both theta shores contain an external `45` path and
an external `24` path, irrespective of the two bit orientations.  Two
crossbar packet states have
complete block quotient:

```text
05|12|3|4|6,    15|02|3|4|6.
```

Each has a unique packet-owning shore by one-way transfer.  In its owner,
make the two crossbar carriers adjacent.  Any further internally disjoint
bridge across `{0,1,4}|{2,5}`, except one merely duplicating a crossbar
rail, gives one of eight explicitly verified seven-bag `K_7` models.  In
particular the centre carriers `45` and `24` close when free.  Hence a
`K_7`-free theta gate carries two certified capture-or-alternating-web
frames.  The centre paths already exist, so the certificates record forced
rail intersection or portal capture, not missing connectivity.

Before the descent theorem, the theta type's exact normal form had aligned or
crossed canonical state bits and same-shore or opposite-shore crossbar
owners.  Crossed bits have an additional rigorous consequence: Kempe
switching between `012|45` and `015|24` forces an exterior bridge across
the missing `K_{3,2}` cut `{0,1,4}|{2,5}` in each shore, while switching
between the two unmerged states forces a bridge from `{0,1}` to `{2,5}`.
The crossbar--bridge lemma makes every such path in a crossbar owner either
rail-parallel or rail-blocked.  The two bridges may arise from different
colourings and are not known to be disjoint.  The missing dynamic theorem
must convert that double rail-blocking into a bounded adhesion, or
synchronize a bridge with the two rail frames to free it and obtain the
explicit `K_7` model.

The tempting rail-median strengthening is false in this generality.  A
clean off-rail first-hit path does give the verified `K_7` quotient, but
an arbitrary component after deleting the two rail medians may absorb
whole terminal arms.  Exact component-contraction enumeration produces
many negative useful-arm and extra-target quotients.  There is also a
centre-only capture architecture in which every `4`-portal is one of the two
medians; the remainder can be full to `S-{4}` behind a natural boundary
of order eight, so no nested seven-cut follows from the rail geometry.

The atomic lock is nevertheless eliminated by a different, arbitrary-order
argument.  For the `05|12` crossbar put

```text
P={0,5}, Q={1,2}, R={3,4,6}.
```

This is exactly the audited two-pair plus singleton-triangle web mode:
`P,Q` are independent, `R` is a triangle, and the five-block quotient is
complete.  The unique crossbar owner supplies the packet.  If its
nonowner has no proper exact seven-fragment, the set-terminal web theorem,
the two explicit crossed-lobe certificates, and disk curvature give two
tagged outer vertices.  Splitting the web between them and adjoining the
owner packet yields `K_7`.  A singleton nonowner is impossible by Dirac,
because its degree-seven neighbourhood contains the independent set
`012`.  Hence **every theta crossbar nonowner strictly descends to a
nested exact seven-cut**.  This eliminates all atomic theta gates,
including centre-only and absorbed-arm versions; it does not yet prevent
an arbitrarily long descent through changing boundary types.

The canonical-state, Kempe/crossbar, and descent proofs and their verifier
are
`hadwiger_two_block_full_shore_state.md`,
`equality_gate_exact_block_state_spectra.py`, and
`equality_gate_theta_two_bit_verify.py`, together with
`equality_gate_theta_singleton_triangle_descent_verify.py`.  The full
independent audit, including the false rail theorem and the corrected
descent, is `hadwiger_two_block_full_shore_state_audit.md`.

### 20. Arm rotation and bounded warehouse branches

Fix one private bag at an atomic `P_4` gate and optimize the rooted model
lexicographically.  A detachable arm which retains all missing shore
demands has three exact outcomes: it completes the next clique model; a
unique monopolized label lets the whole arm rotate into that bag and
strictly improves the model; or the arm monopolizes at least two old bag
labels.  Only root-defect labels can be monopolized.

In the rooted block-cut tree, inclusion-minimal demand-complete warehouse
lobes are disjoint and their monopoly sets are disjoint.  Hence there are
at most `floor(|Delta_x|/2)` incomparable warehouses—only one in a
five-cycle root-defect row.  Under the exact spanning `HC_7` hypotheses,
every such lobe has at least six external portal vertices and repeats an
external owner.  A seven-connected example confirms that connectivity and
portal surplus alone do not force the split (the example contains `K_8`,
so it does not address the critical/minor-free dynamic theorem).

This result and its adversarial audit are
`hadwiger_bridge_torso_p4_exchange.md` and
`hadwiger_bridge_torso_p4_exchange_audit.md`.  The live residue is one
double-monopoly warehouse or a root-block/SPQR cross-torso, together with
the all-proper-minor state lock.

## 21. Defect-one near-`K_7` chain/web theorem (proved quotient capacity; web reduction conditional)

In the one-complex `K_7^\vee` normalization with singleton label set
`L={a,b,c,q_1,q_2,q_3}` inducing `K_6-{ab,ac}`, a connected chain piece
is *defect one* when it sees at least five of the six labels.  Exact
enumeration of all 343 three-piece support words, with direct replay of
all spanning seven-bag certificates, leaves precisely ten negative
words.  Consecutive overlap forces a four-piece obstruction to be only
`abba` or `acca`, and no five-piece word survives.  Consequently **five
arbitrarily large consecutive defect-one connected pieces force a
labelled `K_7`-minor**.

For an actual defect-one web decomposition whose child lobes lie behind
one two-cut and whose lobe deletions are boundary-faithful proper minors,
minor-critical state splicing bounds branching by 108 and the chain
theorem bounds depth by four.  Such a web has at most 1,271,485 pieces;
a globally compatible rural realization is two-apex and hence
six-colourable.  The quotient capacity theorem is uniform in piece size.
The application to an arbitrary near-`K_7` bag remains conditional: no
proof yet supplies the required defect-one decomposition for every
annular piece or central torso.  The claim and its verifier are
`hadwiger_near_k7_defect_one_capacity_state_web.md` and
`near_k7_defect_one_chain_verify.py`; an independent audit is in progress.

### 22. Uniform contraction-split warehouse theorem

For any edge `xy` of a least-parameter counterexample, root a
`K_{k-1}`-model in `G/xy` at the contracted vertex and minimize its root
bag.  Every detachable off-root piece then monopolizes at least two direct
root-defect labels.  Inclusion-minimal block lobes have disjoint monopoly
sets, so there are at most `floor((k-2)/2)` of them.  This uses no
spanning-model assumption.

After expanding `xy`, each lobe is endpoint-charged or lies behind a
genuine full adhesion of order at least the ambient connectivity.  At a
full adhesion, the equality states produced by all boundary-faithful
warehouse-side proper-minor operations are disjoint from every state of
the reference contraction.  The cutvertex-free root torso is reduced to
a full label-preserving split, an endpoint/internal pin, or an ordered
two-owner corridor.  A separate trace-rank lemma turns a boundary of order
`p` in one connected bag into exactly `p-1` concrete trace units; for a
boundary covered by four disjoint bags this gives at least `|Z|-4` units.

For `HC_7`, at most two minimal warehouse lobes survive, and a
non-endpoint one lies behind an adhesion of order at least seven.  The
remaining step is still dynamic: align the torso corridors or trace units
with the named monopoly labels, or force a common equality state across
opposite operations.  The theorem does not claim that every expanded bag
splits and does not prove `HC_7`.

The proof and audit are
`hadwiger_uniform_contraction_split_warehouse.md` and
`hadwiger_uniform_contraction_split_warehouse_audit.md`.

### 23. Uniform bipartite-contraction co-rooting

Let `T` be any nontrivial vertex set whose induced graph is connected and
bipartite in a least-parameter proper-minor-minimal counterexample.  Then
`chi(G/T)=eta(G/T)=k-1`.  The chromatic equality follows by expanding a
hypothetical `(k-2)`-colouring: use the contraction colour on one side of
the bipartition and one new colour on the other.  Least-parameter
`HC_{k-1}` gives the clique-minor equality.  Rooting a `K_{k-1}` model at
the contracted vertex and expanding it puts all of `T` inside one branch
bag.

Consequently every pair of vertices—and indeed every prescribed induced
path or induced tree—can be co-rooted in one bag of a `K_{k-1}` model.
This is currently the cleanest uniform rooted-model principle in the
programme: the prospective path/tree may be chosen before the clique
model, rather than discovered inside a fixed bag.

Minimizing the quotient root bag also gives at most
`floor((k-2)/2)` inherited warehouse lobes.  Each is directly charged to
`T` or lies behind a full adhesion whose boundary-faithful warehouse
states are disjoint from the contraction states.  For `HC_7`, at most two
such inherited lobes survive.

The theorem is co-rooting, not a rooted transversal or a bag split.  An
arbitrary prescribed `T` can have cutvertices and block branches which
collapse at the quotient root and are therefore not controlled by the
inherited-lobe count.  The live uniform target is a label-preserving split
principle exploiting the bipartition/path/tree geometry, or a proof that
failure produces a full adhesion with a common opposite-operation state.

The proof and audit are
`hadwiger_bipartite_contraction_rooted_model.md` and
`hadwiger_bipartite_contraction_rooted_model_audit.md`.

### 24. Maximal-society omitted-colour dichotomy

For a maximal connected induced bipartite society `S=A dotcup B` in a
hypothetical `HC_7` counterexample, choose a six-colouring of `G/S`, omit
one noncontraction colour beta, and apply Strong `HC_4` to the other four
classes.  This gives an actual boundary-rooted `K_4` model.  A Kempe
exchange proves that, for each retained colour gamma, some beta--gamma
component contains portals of both colours.

The four mixed components need not coincide.  The sharp positive
dichotomy is: a beta-portal component outside the rooted model either
meets all four bags and is a fifth rooted bag, or it is separated from a
missed bag by a full adhesion of order at least seven.  Across that
adhesion, equality states of every pair of boundary-faithful proper-minor
operations on opposite open shores are disjoint, by crossed colouring
splicing.  If the fifth bag does occur, five selected society portal
pairs give a `K_7` whenever their paths in a society spanning tree share
one common edge.

An exact ten-vertex example shows sharpness: the society is a maximal
edge, the four rooted bags are singleton vertices of a `K_4`, and four
beta vertices independently supply the four mixed Kempe edges while each
touching only one rooted bag.  The graph has neither an exterior `K_5`
minor nor a `K_7` minor.  It is six-colourable, so it isolates the missing
ingredient as the all-proper-minor exchange system rather than refuting
the counterexample-derived theorem.

The theorem and verifier are
`hadwiger_maximal_bipartite_fifth_colour_dichotomy.md` and
`maximal_bipartite_fifth_colour_counterexample.py`.

### 25. Nested-cut transfer codes and the obstruction to partition descent

Between two nested exact seven-cuts, seven disjoint paths transport the
old boundary graph only as a rooted minor shell.  They do not preserve the
graph induced by the new cut or any boundary equality partition.  The
exact finite object is the two-boundary six-colour transfer relation of
the annulus.  Inner faithful-operation codes pull back through this one
relation, and successive annuli compose by ordinary relational
composition.  This gives the correct state-gluing language for continuing
the theta descent through changing boundary types.

No partition-only well-founded potential follows from the linkage.  A
connected `K_7`-minor-free annulus built from seven `K_7-e` equality
blocks implements an arbitrary permutation of the seven labelled boundary
colours; composing it with the inverse annulus returns every state.  The
exact verifier checks the six-colour equality gadgets, the block
decomposition, both seven-path linkages, and identity composition.  Thus
any termination theorem must use seven-connectivity and the full
contraction-critical operation signature to exclude permutation-like
transfer.  Repetition of a boundary graph or equality partition by itself
does not allow colouring gluing.

The theorem and verifier are `hadwiger_nested_cut_transfer_codes.md` and
`nested_cut_transfer_cycle_verify.py`.

### 26. Nested neutral-triangle rooted-model principle

If a seven-connected graph contains a triangle `Q={q1,q2,q3}` such that,
in `H=G-Q`, every neighbour of `q3` is also adjacent to `q1,q2`, then
either `G` has a `K_7` minor or deleting `q1,q2` leaves a planar graph.
Indeed `H` is four-connected.  Fabila-Monroy--Wood Theorem 6 applied to
any four of the at least five common neighbours gives either a rooted
`K_4`, which joins the singleton triangle to form `K_7`, or a planar
embedding in which every four-subset is cofacial.  Three-overlap of face
boundaries puts the whole neighbourhood on one face, where `q3` can be
inserted.

The literal nesting can be weakened only with an additional geometric
condition: four triple-common portals force a common face in the planar
outcome, but every private `q3` portal must separately be shown to lie on
that face.  Mere common owner-class incidence in a spanning near-clique
model does not suffice.

The homogeneous cross-split obstruction showing sharpness is the join of
a neutral `K_3` with a seven-vertex 2-tree.  It is `K_7`-minor-free,
not two-apex, and exactly five-connected.  A new independent verifier
checks all these assertions; the cross atlas also reruns with its claimed
480 minimal and 12,960 duplicated-contact rows.

The theorem, audit, and verifier are
`hadwiger_near_k7_nested_triangle_rooted_model.md`,
`hadwiger_near_k7_nested_triangle_rooted_model_audit.md`, and
`near_k7_nested_triangle_obstruction_verify.py`.

### 25. Full-adhesion model-clean owner exchange

A full shore can augment a labelled clique model only after branch-set
disjointness is protected explicitly.  The proved clean-donor theorem says:
if a full component is disjoint from a protected `K_r` frame, and every
frame label either meets the adhesion or is contacted by a collection of
boundary-containing donor pieces disjoint from the frame, then the shore
glues the donors into a new branch bag and gives a `K_{r+1}` model.

For two full shores, a sharper sacrifice theorem applies.  If `r-1`
pairwise adjacent protected cores lie outside both shores and meet the
adhesion, while the remaining owner contains a connected transverse trace
through two boundary vertices, split that trace at a tree edge and absorb
its two pieces into the two shores.  The resulting two shore bags plus the
protected cores form a labelled `K_{r+1}` model.  Hence, under protected
cores, every repeated owner either gives the larger clique minor or all of
its positive trace rank is forced through the two shore interiors.  This
closes the infinite family with even one transverse trace unit and leaves
an exact two-shore trace lock.

The static hypotheses cannot be strengthened further without a
label-preservation or critical-state input.  Let `I` be the icosahedron and
`G=I vee K_2`.  Then `kappa(G)=7` and `eta(G)=6`.  The set
`N_I(0) union K_2` is a full exact seven-cut with two shores and is covered
by a `K_6` model in which every bag meets the cut and one bag repeats.
Nevertheless there is no `K_7` minor.  A second `K_6` model has exactly the
promoted one-gate count: one root vertex `q`, six protected boundary
vertices in five bags, one missing owner and one repeated owner.  The
example exposes the flaw in the formerly described "easy sacrifice": the
open shores already contain vertices of retained branch bags.

Thus capacity, connectivity, trace rank and owner counts alone do not
close the one-gate cell.  The remaining theorem must use maximal-society
geometry or opposite deletion/contraction states to create shore-free
cores, a clean donor, or a gluable smaller adhesion.  The proof and the
explicit counterexample are in
`hadwiger_full_adhesion_owner_exchange.md`; the falsification search is
`full_adhesion_model_counterexample_search.py`.

### 26. Theta crossbar nonowner descent

The last seven-edge theta boundary has a new arbitrary-order closure on
the packet-deficient side.  For the crossbar `05|12`, put

```
P=05,  Q=12,  R={3,4,6}.
```

The two active blocks are independent, `R` is a triangle, and the
five-block quotient is complete.  Operation-state packet transfer gives a
unique packet owner, so the other shore is a genuine nonowner.  If that
nonowner has no proper exact-seven fragment, relative boundary order is
at least eight.  The Two Paths obstruction is then a bare disk web; a
label-free two-cut analysis gives an explicit `K_7` model, so an atomic
nonsingleton web is three-connected.

Disk curvature now supplies at least six outer degree-three vertices,
each adjacent to all of the triangle `R` and to one root of each active
block.  Rooted-`K_4` cofaciality forces these vertices onto the outer web
face.  Any two split the web into adjacent connected pieces; together
with the two owner carriers and the three singleton members of `R`, they
are seven explicit clique branch bags.  Thus an atomic nonsingleton
nonowner is impossible.  At the original theta boundary, a singleton
nonowner also fails: it has degree seven and neighbourhood containing the
independent triple `012`, contrary to Dirac's bound.

Consequently every theta crossbar nonowner exposes a strictly nested exact
seven-cut.  The same argument applies to `15|02`.  In particular, if one
shore of a theta adhesion is globally minimum among exact-seven fragments,
it must own **both** crossbars.

That final same-owner lock is now closed.  The `05|12` packet gives a
cycle through the active roots in order `0,5,2,1`, using the boundary edge
`52` and path `1-4-0`.  The disjoint `15` and `02` carriers from the second
packet form the opposite linkage.  Fabila-Monroy--Wood Lemma 7 therefore
gives a rooted `K_4` inside the common owner.  The untouched full shore and
the singleton universal vertices `3,6` complete seven explicit clique
bags.  Thus no theta adhesion can have a shore globally minimum among all
exact-seven fragments.

The theorem does not assert that descent preserves theta.  Minimum-cut
linkages transport labels but not nonedges; an inner cut may acquire the
old edge `01`, destroying the independent triple used at the original
singleton.  The result closes theta only after the equality-gate funnel
has produced theta on the globally minimum fragment being analysed; it
does not make arbitrary nested boundaries theta.

The descent proof is `hadwiger_theta_crossbar_nonowner_descent.md`; explicit
two-cut and curvature branch sets are replayed by
`equality_gate_theta_singleton_triangle_descent_verify.py` (and the
independent replay `theta_crossbar_nonowner_certificates.py`).  The
independent audit `hadwiger_theta_crossbar_nonowner_descent_audit.md` is
GREEN.  The same-owner exchange is
`hadwiger_theta_same_owner_crosslink_closure.md`; its independent audit is
`hadwiger_theta_same_owner_crosslink_closure_audit.md`.  The stronger
owner-independent shortcut is false: in the opposite-owner construction
the boundary vertex `4` misses `2` and `5`, so it is not an automatic
seventh bag.

### 27. Atomic packet circuits and uniform rooted Hall completion

Strict minimum-fragment surplus does **not** by itself turn three
pairwise packets into one simultaneous triple.  The sharp four-vertex
example is a `K_4` portal grid: two demands each require two vertices,
the third has singleton carriers, every pair is linkable, and every
proper shore subset has relative boundary order at least eight.  A
two-vertex all-portal example is the still smaller capacity exception.
Thus the proposed static three-packet theorem and a static
capture--capture closure are false.

Those circuits nevertheless die in the actual seven-edge equality gate.
For the `K_4` grid, all orientations of all seven fully-positive matching
rows reduce to two hand cases.  If the unmatched boundary vertex sees the
grid's common pair, seven bags are immediate.  Otherwise the audited
funnel has one exceptional oriented row, and a second explicit seven-bag
construction closes it.  The order-two all-portal circuit is closed by a
rooted `K_4` in the boundary after deleting one named vertex.  The exact
order-five `K_5` and order-six `K_6-2K_2` solver witnesses are also closed.

The scalable output is the rooted Hall completion theorem.  For arbitrary
`t`, let a boundary `S` of order `t` contain adjacent vertices `s,r`.
If `t-2` protected connected pieces form a clique frame, every piece sees
`s`, and their portal incidence into `S-{s,r}` satisfies Hall, then attach
the Hall roots to those pieces and add the full shore and the bag
`{s,r}`.  These are a literal `K_t` model.  This is a genuine uniform
rooted-model principle rather than an `HC_7` label calculation.

The two independent verifiers replay the strict-surplus circuits and
construct 336 branch-set certificates at each displayed order
`2,4,5,6`.  The proof and GREEN audit are
`hadwiger_atomic_three_packet_core_completion.md` and
`hadwiger_atomic_three_packet_core_completion_audit.md`; the replayers are
`atomic_three_packet_circuit_verify.py` and
`atomic_three_packet_core_completion_verify.py`.

The scope limit is important.  The satisfiability run returns one witness
at each of orders four through six; it does not classify every portal
pattern of those orders.  The whole capture--capture/web--web branch is
still open.  Any survivor must avoid the rank-two grid completion and the
rooted Hall transversal, after which boundary-faithful operation states
again become the missing input.

## III. Computational, conditional, or not yet certification-ready work

The large `HC_7` local dossier remains valuable as a laboratory, but it
cannot currently be promoted to a proof package.

* Pure-Moser and other degree-seven neighbourhoods have many reported
  quotient, cut, web, and small-component eliminations.
* Degree-eight and degree-nine work gives component-count bounds, portal
  constraints, and many explicit minor certificates, but no complete
  elimination of either degree class.
* Numerous finite atlases classify labelled contact rows, missing-edge
  graphs, or components only up to a fixed order.  Some scripts emit
  explicit branch sets and some results have second verifiers.
* The workspace currently contains roughly 300 Python scripts.  Their
  collective encoding coverage, symmetry reductions, and certificate
  checkers have not been assembled into one independently reproducible,
  formally audited proof chain.
* Several local web closures also depend on exact hypotheses of rooted
  two-path/web theorems.  Those mappings must be checked individually; a
  computationally surviving quotient is not by itself an actual graph
  obstruction, and a quotient certificate can forget portal order.

Accordingly, local claims should be used as conjecture generators and
countertests for uniform lemmas.  They do not currently prove `HC_7`.

There is also a document-control issue: the workspace has nearly 400
Hadwiger markdown notes, and some older “remaining gap” reports have been
superseded by later work.  Any eventual proof needs a dependency-ordered
master manuscript and reproducible certificate manifest; the existence of
many internally consistent notes is not a substitute.

## IV. Explicitly false or exhausted routes

The workspace now contains counterexamples precise enough to close several
attractive shortcuts.

1. **Static saturation is insufficient.**  Every independent trace,
   colourful portal sets, and an unrooted clique model need not give the
   rooted model (`hadwiger_all_independent_trace_counterexample.md` and
   `hadwiger_uniform_bipartite_compression_barrier.md`).
2. **Nested private-colour flags and pairwise Kempe paths are
   insufficient.**  They can choose mutually incompatible roots
   (`hadwiger_colourful_elimination_flag_counterexample.md`).
3. **A fixed model plus a full root-to-bag transversal is insufficient.**
   First-hit labels can be locked in a transit comb
   (`hadwiger_linkage_model_cleaning_counterexample.md`).
4. **Finite boundary-state novelty is insufficient in the abstract.**  A
   Hajós-type transition diamond realizes incompatible one-shore states;
   even high connectivity and an unrooted clique can be added if
   minor-criticality is dropped (`hadwiger_boundary_state_diamond_counterexample.md`
   and `hadwiger_hall_circuit_anti_diamond.md`).
5. **Clean rotations are not a decreasing model potential.**  Inside a
   spanning bag they may only exchange one spanning tree chord for another.
   Triangles already cycle.
6. **Foreign-transit cycles are not automatically augmentations.**  A
   spanning, contact-maximal, minimal-bag, `K_7`-minor-free two-complex-bag
   architecture realizes such a cycle; the missing hypothesis is the full
   minor-transition system (`hadwiger_foreign_transit_cycle_potential.md`).
7. **One edge state plus all its Kempe detours is insufficient.**  The
   strict-surplus owner gadget realizes every such detour while blocking
   the required labelled rerouting (`hadwiger_strict_surplus_operation_states.md`).
8. **Connectivity, density, products, fractional minors, or portal
   multiplicity alone do not bridge the gap.**  The workspace contains
   sharp quantitative and wiring counterarchitectures; all of these omit
   the indispensable all-minor exchange information.
9. **A repeated separator owner is not automatically sacrificial.**  Even
   a seven-connected `K_7`-minor-free graph can have a full exact seven-cut
   covered by a `K_6` model, with every bag meeting the cut and one bag
   repeated.  The icosahedral join in
   `hadwiger_full_adhesion_owner_exchange.md` shows that shore/model
   overlap defeats the naive branch-set construction.  A valid exchange
   must exhibit protected shore-free cores or use critical operation
   states to manufacture them.
10. **A rail-median first hit is not automatically a clique certificate.**
   The former theta rail probe accepted arbitrary `K_4` minors and then
   appended the singleton bags `3,6` and the opposite full shore.  That
   append is valid only when every one of the four branch bags contains a
   boundary anchor.  Its junction-arm witnesses use an internal singleton
   bag and therefore do not give `K_7`; moreover, a component meeting an
   open tree arm swallows that whole arm after the medians are deleted.
   `theta_rail_component_absorption_verify.py` records the corrected
   anchored test.  The valid replacement is the rural nonowner descent in
   Section 26, not a static arm-absorption claim.

These negative results are useful: a viable proof must use actual labelled
Hall geometry and the compatible family of colourings of **all** proper
minor operations, not one colouring, one linkage, or one abstract state
system.

## V. Narrowest current obstructions

The two sharpest live cells can be stated without Moser labels.

First, a general co-rank-one `HC_7` model can still leave an
operation-sensitive **two-label owner lock**: a 2-connected lobe or ear
which wholly owns at least two deficient labels, or is contact-protected,
and for which every connected split loses those labels.  Static portal
multiplicity and one operation state do not eliminate it.

The sharpest terminal object comes from the genuinely contact-maximal
specialization of the Hall promotion theorem.  Every uncontacted singleton
bag is individually nonlinkable, the root side is separated from all of
them by portals lying in contacted bags, and absorbing a root-side path
produces a **multiply rooted contacted bag**.  Contact maximality then
forces every connected split of that bag to lose named adjacencies to the
retained clique bags.  For `HC_7` this is an explicit two-by-four
label-preserving split lock.

The co-rank-one source-tight cells remain useful nonterminal waypoints.
Root-free bag saturation moves out of all their portal branches—exact or
surplus, one component or many—but no proof yet shows that every resulting
exit reaches the target rather than the contact-maximal split lock.

On the independent near-`K_7` route, a one-complex `K_7^-` or
`K_7^vee` model now gives an explicit split at every sufficiently varied
two-cut.  The residue is a three-connected portal society or a common
dark-row lobe whose faithful operation states are disjoint from those on
the opposite shore.

A new independently audited capacity lemma closes another unbounded
subfamily in the one-complex `K_7^vee` setting.  Relative to the six
singleton labels inducing `K_6-{ab,ac}`, any chain of five disjoint
consecutive connected pieces, each meeting at least five label rows,
contains a `K_7`-minor.  Three pieces have exactly ten negative type words;
four reduce to `abba` or `acca`; no five-letter word survives.  Conditional
on an actual defect-one web decomposition, faithful-state splicing bounds
branching by 108 and the whole decomposition by 1,271,485 pieces, while a
globally compatible rural expansion is two-apex.  The condition is not yet
known to follow from the Norin--Totschnig minor: a general model need not
have one complex bag, and nested annular pieces need not have defect at
most one.  Thus the chain theorem is genuine progress, but the claimed web
normal form remains an explicit open structural input.

In the contact-maximal five-contact specialization, the same obstruction
now has a finite *type* but unbounded geometry: it is one of the atomic
`K_3`, `P_4`, or `3K_2` support motifs, with a multiply hit named separator
piece whose every rooted split has one-sided portal order.  The piece may
have arbitrary order, so this is the immediate dynamic theorem target,
not another bounded enumeration.

Two cautions matter:

* Closing this cell would be a substantial infinite-family theorem, but
  one must still route arbitrary `HC_7` models with several nontrivial bags
  into it or extend the exchange to them.
* For general `t`, known connectivity of a minimal counterexample is far
  smaller than `r+1`; the two-clean-portal count used above is unavailable.
  A general proof needs operation-state capacity, not merely stronger
  counting.

## VI. What would count as the next genuine frontier advance

The highest-value next result is an **atomic-motif dynamic rooted split
theorem** in the actual minor-critical setting:

> A contacted clique-model bag containing two distinct roots can be split
> into two adjacent connected rooted bags while preserving all but one of
> its named clique adjacencies in one of the exact two-surplus packing
> patterns for `K_3`, `P_4`, or `3K_2`; or else the failed split exposes a
> smaller owner core, a sub-connectivity cut, or a faithful state already
> realized on the opposite shore.

To count as genuine progress, its proof must:

* work for arbitrary size of the 2-connected lobe, not an enumerated order;
* preserve named interbag adjacencies explicitly;
* use more than one proper-minor operation (the one-edge gadget refutes the
  single-state version);
* terminate under a stated well-founded potential; and
* pass the transition-diamond and two-complex foreign-cycle
  counterarchitectures by using the exact hypotheses they lack.

A proof in the co-rank-one/singleton setting would close a genuinely
infinite `HC_7` family and be the first substantial frontier advance of the
programme.  Extending it to two complex bags and then arbitrary Hall
circuits would provide a credible route to all of `HC_7`.  Only after that
should one claim a route to general `t`; that extension additionally needs
a replacement for the `k >= r+1` portal-surplus step.

## Final assessment

The current work is stronger than promising casework: it has isolated and
proved reusable dynamic lemmas, and it has closed multiple unbounded
rooted-model families.  But it remains pre-proof infrastructure.  There is no
complete `HC_7`, no new established value of Hadwiger, and no justified
claim that the general conjecture is close.  The programme will have
substantively pushed the frontier further only when the contact-maximal
split lock or the near-clique owner lock is eliminated in an
independently checkable theorem.
