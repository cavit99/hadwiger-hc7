# Technical frontier: adjacent-pair colourings and rooted minor models

**Status:** active research target.  The inputs labelled as proved below
have written proofs and separate internal audits.  The exchange theorem in
Sections 3 and 4 are open.  Nothing here proves `HC_7`.

## 1. Uniform setup

Let `G` be seven-connected and seven-chromatic, have no `K_7` minor, and
suppose every proper minor of `G` is six-colourable.

The audited global adjacent-pair theorem supplies an edge `zu` such that,
for `H=G-{z,u}`:

1. `chi(H)=6` and `H` is five-connected;
2. `H` has a spanning `K_6`-minor model
   `(F_1,...,F_6)`;
3. `G-zu` has a six-colouring in which `z,u` have a common colour
   `alpha`, the nonempty `alpha`-class in `H` is anticomplete to both
   poles, and both poles have neighbours in every other colour; and
4. after choosing one neighbour of each non-`alpha` colour at each pole,
   there are five pairwise vertex-disjoint paths between the two selected
   five-sets.  Their end colours are paired by a permutation.

The edge and model are not prescribed by a previous near-complete minor
model.  This loss of labels is part of the problem, not an implicit
identification.

## 2. Proved contact consequences

For a spanning model `M=(F_1,...,F_6)`, let `C_z` and `C_u` be the sets of
branch-set indices contacted by `z` and `u`, respectively.  Put

\[
 c(M)=|C_z\cap C_u|,
 \qquad
 r(M)=|C_z\cup C_u|.
\]

The audited palette-permutation theorem proves:

- `r(M)<=5` and `c(M)<=4` in a `K_7`-minor-free host;
- if `c(M)=4`, then a common branch set contains distinct pole neighbours,
  and splitting that branch set gives an explicit `K_7`-minor model or an
  actual vertex separator;
- after excluding that separator mechanism, `c(M)=3` has an exact form:
  the three common branch sets each have one common pole-neighbour, there
  is one branch set contacted only by `z`, one contacted only by `u`, and
  one contacted by neither pole; and
- in that exact form, at least two palette colours are represented in each
  exclusive branch set, and `H` contains two disjoint paths between
  selected vertices of the two exclusive branch sets.

The separator in the second item has no proved upper bound.  The disjoint
paths in the last item preserve their two endpoint palettes only up to a
permutation and may traverse the other branch sets.

The audited bichromatic-support theorem gives a further model-independent
fork for every nonbuffer colour.  Either its pole support is split between
more than one two-colour component, in which case the full neighbourhood of
a support component together with one or both poles is an actual separator,
or all pole support lies in one two-colour component.  In the latter case a
Kempe interchange changes the common missing colour exactly, and the
root-facing side of that component has a neighbour in each of the other four
colour classes.  Equality in the separator lower bound gives order seven;
no upper bound is known.

The audited bipartite-contraction theorem extends this mechanism from the
two poles to any nontrivial connected induced bipartite subgraph `Q` of a
minor-minimal chromatic graph.  In every colouring after contracting `Q`,
both bipartition sides see all five other colours, and each colour supplies
a common bichromatic component adjacent to both sides.  Concentrated
support rotates the contracted colour; diffuse or one-sided support gives
the exact literal separator of a support component.  If `Q` is chosen
inside one model branch set, its contraction preserves that branch-set
label and all old model adjacencies.

There is also an exact limit on the rotation mechanism.  After normalizing
a concentrated pole rotation back to the old buffer-colour name, it swaps
precisely the inactive two-colour components.  Each inactive component is
anticomplete to both poles and lies behind a separator contained in `H`
whose boundary uses only the other four colours.  If there is no inactive
component anywhere in the transition orbit, every rotation is merely a
global colour relabelling and cannot improve a fixed model/linkage score.

Two further audited theorems now reorganize the residue.

First, after contracting any connected induced bipartite subgraph, every
pair of colours different from the contracted colour has a diagonal
bichromatic component forced by nonextendability.  A matching of two
colour pairs therefore gives two vertex-disjoint such components; together
with the common component for the fifth colour, this gives three disjoint
connected subgraphs adjacent to the two sides.  If the boundary contacts
for one colour pair occupy more than one bichromatic component, the full
neighbourhood of each such component is an actual separator.  These
components carry colours, not prescribed clique-minor labels.

Second, suppose all five full two-colour graphs consisting of the missed
colour and one other colour are connected.  For any one of the other
colours, their union `X` is then a connected induced bipartite subgraph
dominating the rest of `G`.  The graph `Q=G-X` is five-chromatic and
`K_6`-minor-free, while deleting either pole from `Q` leaves a
five-chromatic graph.  Martinsson--Steiner's prescribed-singleton theorem
then gives two oppositely rooted near-`K_7` models.  This conclusion no
longer depends on retaining the original spanning `K_6` model.

The alternatives are exhaustive at a fixed adjacent-pair colouring.  If
one of the five full two-colour graphs is disconnected, the diffuse,
one-sided, or inactive-component analysis gives an actual separator.  If
none is disconnected, the connected-dominating compression applies.  The
separator has order at least seven but currently has no proved upper bound.
This exhaustive implication is now recorded as a separate GREEN-audited
theorem rather than only as a programme-level summary.

## 3. Primary open theorem

### Adjacent-pair colouring-space alternative

For the edge and colouring in Section 1, prove one of the following.

1. A separator returned by a disconnected two-colour graph can be replaced
   by an actual order-seven separation whose boundary partition is induced
   by compatible proper-minor six-colourings on both sides.
2. In the connected-dominating branch, the two oppositely rooted
   near-`K_7` models can be synchronized to give an explicit `K_7` minor.

Two vertices meeting every `K_5`-minor model need not be retained as a
third outcome: the promoted transversal theorem turns that condition into
an actual order-seven separation.  It supplies no compatible shore
colourings, so it enters rather than closes item 1.

The following is a sufficient four-chromatic formulation and the chosen
constructive milestone for the second outcome.  Write

\[
 X=V_\alpha\cup V_\beta,\qquad
 Q=G-X,\qquad R=Q-\{z,u\},
\]

in the connected-dominating branch, and put

\[
                    S=N_R(z),\qquad T=N_R(u).          \tag{3.1}
\]

Then `R` is four-chromatic and both `S,T` are colourful in `R`.  A
`K_4`-minor model whose every branch set meets both `S` and `T`, together
with `z,u,X`, is an explicit `K_7` model.  The open theorem is therefore a
paired colourful-set alternative in this lifted host: produce that rooted
`K_4` model, or the order-seven separation above.

The paired statement is false even for a five-connected four-chromatic
graph.  The known example already has a `K_6` minor, so it does not satisfy
the present core hypothesis.  A proof must use the `K_6`-minor exclusion,
the connected dominating lift, seven-connectivity, and exact proper-minor
colouring responses; applying Strong Hadwiger for four colours separately
to `S` and `T` does not synchronize the two models.

## 4. First concrete milestone

Fix an `S`-rooted `K_4` model `(D_1,...,D_4)` in `R`, supplied by
Martinsson--Steiner, maximizing the number of branch sets meeting `T`.
The six sets

\[
                         X,\ \{z\},\ D_1,\ldots,D_4    \tag{4.1}
\]

form a `K_6` model.  Contract them in `G`.  In every six-colouring of this
proper minor, the remaining pole `u` must repeat the colour of a branch set
`D_i` which it misses.  A promoted maximality lemma now identifies the
literal obstruction hidden by that contraction.  For every missed `D_j`,
the component `C_j` of `R` minus the other three bags that contains `D_j`
is disjoint from `T`, and

\[
 N_G(C_j)=N_R(C_j)\mathbin{\dot\cup}N_X(C_j)
                 \mathbin{\dot\cup}\{z\}.            \tag{4.2}
\]

This is the boundary of an actual separation of order at least seven.
The repeated quotient colour alone cannot improve the model: an explicit
`K_6`-minor-free core with a unique missed label realizes that response and
has no improving rooted model.

The immediate host-level theorem must use the expanded boundary in (4.2)
to do one of the following:

1. reroute a deficient `D_i` so that it also meets `T`, strictly improving
   the chosen rooted model, or directly construct `K_7`;
2. identify an actual order-seven separation with compatible boundary
   colourings.

A fixed two-vertex transversal of all `K_5` models directly contradicts
`chi(G)=7`: deleting it leaves a four-colourable `K_5`-minor-free graph,
and two fresh colours extend that colouring to `G`.  The stronger promoted
order-seven-separation consequence remains available, but is unnecessary
for this terminal chromatic argument.

When exactly one branch set is deficient, `C_j,u,z,X` and the other three
bags already form a `K_7`-minus-one-edge model.  Thus the first milestone is
a label-preserving split of an actual branch set that repairs that missing
adjacency, or an exact separator produced by the failure of every such
split.

That split problem now has an exact global formulation.  A two-colour path
from `C_j` to `T` repairs the missing adjacency.  After removing its
vertices from the four protected branch sets, either suitable residual
components give an explicit `K_7` model or the full neighbourhood of one
residual component is an actual separator.  Moving the cut edge along the
path gives an exact interval of valid cuts for every residual component.

More generally, for seven disjoint nonempty candidate sets `B_i`, define

\[
 \delta(\mathcal B)=
 \sum_{i<j}\bigl(c(B_i\cup B_j)-1\bigr)
 -\sum_i\bigl(c(B_i)-1\bigr),                       \tag{4.3}
\]

where `c` counts connected components.  Contracting every internal
component and applying Mader's exact edge bound gives a `K_7` minor whenever
\(\delta(\mathcal B)\le 0\).  The unsplit `K_7`-minus-one-edge model has
\(\delta(\mathcal B)=1\).  Thus branch-set repair is a strict decrease of one scalar
component defect, not a collection of unrelated labelled cases.

Within the unique-deficiency branch, fix an admissible path cut and select
nonempty collections from all four protected component classes.  Every
selected residual component is additionally required to lie in the
valid-cut interval, equivalently to be adjacent to both path-side anchor
sets at this cut, and to be adjacent to `z`.  Any `K_4` minor in their
component-contact graph
lifts, together with the two path sides and `z`, to a `K_7` model.  If that
selected graph is `K_4`-minor-free, defect one is equivalent to its being a
two-tree.  The current chain does not prove unique deficiency, four
represented eligible classes, or defect one for every connected-dominating
residue.  In the conditional two-tree branch, the constructive target is to
use the compulsory proper-minor colourings at a lifted simplicial
degree-two component to obtain an explicit `K_7` model, a colour-compatible
order-seven separation, or a new valid instance of the same eligible
defect-one setup with a lifted simplicial component `L'` satisfying
`|V(L')|<|V(L)|`.  Here `L` is chosen globally with minimum order over every
eligible simplicial lifted component in every valid configuration in the
fixed host `G`; noncanonical connector length and the order of the selected
contact graph are not rank coordinates.

For this target, a **valid defect-one configuration** is the full tuple
consisting of the adjacent pair and connected-dominating colouring frame;
the uniquely deficient rooted `K_4` model; its colour-matched path `P` and
an admissible cut `q`; four nonempty labelled selections of residual
components; eligibility of each selected component at `q`, including
adjacency to `z` and both path-side anchor sets; and a `K_4`-minor-free
component-contact graph `J` of defect one.  The subgraph `L` is the literal
component represented by a simplicial degree-two vertex of `J`.  A smaller
`L'` must belong to another full valid configuration in the original fixed
graph `G`, possibly after reselecting the model, path, cut, and components;
an image existing only in a proper minor does not count.

The clique-tree structure of the two-tree gives overlapping local `K_6`
models, but their six-colour patterns alone are not an exchange invariant.
A legal transition carries a label map from `V(J)` to the four protected
branch-set classes, the oriented path and valid-cut interval endpoints, and
chosen host edges and endpoints witnessing every `J`-edge and every contact
with `z` and the path-side anchor sets.  It must retain those witnesses under
lifting or provide explicit replacements, record the bipartition-side or
pole source of each colour response, preserve named root traces, and carry
the exact boundary equality partition.  Failure must return `N_G(Y)` for a
named connected residual piece `Y` with both shores nonempty.  Deleting or
contracting inside `L` is only a proper-minor probe; every output must lift
to the original `G`.

The proper-minor response now has a matching chromatic dichotomy.  For any
elementary minor operation wholly inside the five-chromatic core, the new
core has chromatic number four or five.  In the four-chromatic branch the
intersection of the attachment sets of the two bipartition classes of `X`
is colourful and roots a `K_4` model meeting both sets.  These are not the
pole-neighbourhoods `S,T`, and the bipartition classes need not be connected
branch sets, so this branch is not terminal.  In the five-chromatic branch,
every five-colouring satisfies the exact common-hole law but need not
preserve full saturation.  Both branches still require a label-preserving
host-level exchange or colour-gluing argument.

Within the conditional defect-one branch this has now been sharpened to a
labelled near-complete model.  If `L` represents a simplicial vertex of the
two-tree with neighbours `M,N`, the edge `MN` lies in another triangle
`MNR`.  The three path-cut anchors together with `M,N,R` form a fixed
`K_6`-minor model disjoint from `L`, and adding `L` gives a `K_7^-` model
whose sole missing adjacency is `L`--`R`.  Hence unrooted model regeneration
after an operation in `L` supplies no new geometry.

More globally, every proper four-labelled two-tree contains a rainbow
induced `K_4^-`.  Its shared edge separates the two nonadjacent vertices.
The host lift, together with the attachment-clique property, therefore
compresses the entire two-tree into an actual separation: one connected
open shore has full neighbourhood contained in the five common branch sets
of a labelled `K_7^-` model, and the other deficient branch set lies on the
far side.  The separator has order at least seven, but its five supporting
branch sets can contain arbitrarily many boundary vertices.

A local re-selection theorem reduces the sixth branch set to a singleton or
an induced path.  In the path case its two endpoints each uniquely support
at least two of the five common branch-set names.  This is a local model
normalization only: absorption into a named branch set can destroy the
protected label, valid-cut, or path-side role required by a full valid
defect-one configuration.

For every internal edge `xy` of `L`, deletion of its two ends leaves a graph
of chromatic number five or six.  In the five-colour case, `xy` is
double-critical and its common neighbourhood contains all five colours;
indeed every ordered list of distinct colours occurs on a generalized
Kempe `x`--`y` path.  If the common neighbourhood meets each of the five
named common branch sets, splitting `L` at `xy` gives an explicit `K_7`
model.  In the six-colour case, every colouring has the exact two-pole
missing-colour cover, and a colouring inherited from `G/xy` has one common
missing colour.  The open operation-specific step is therefore literal
colour-to-branch-set alignment, not existence of a path or of an unrooted
clique minor.

In the five-colour branch the common-neighbour set is colourful in every
five-colouring.  Any rainbow transversal roots
`F_5=K_1\vee P_4`, so the endpoints and those five rooted bags form an
explicit `K_2\vee F_5` minor.  The remaining three chords are not forced,
and the common-neighbour set avoids every branch set privately supported by
the chosen path endpoint.  The natural rooted-`K_5` upgrade is therefore a
new theorem-strength label-alignment step, not a consequence of ordinary
Kempe connectivity.

Global minimization over all oriented `K_7^-` models adds a second path
normal form.  A minimum deficient branch set is a singleton or an induced
path with endpoint-private label pattern `2+2` or `2+3`.  If it has an
internal vertex, every five-fan collides first in one common named branch
set.  In the balanced case this gives an actual separator and reduces the
order-seven problem to an upper bound of five on that branch set's boundary
contribution.  The result is model-global but does not preserve the full
defect-one path-cut data.

The reversible connected-subgraph rotation now has compulsory host-level
colouring data.  Its unique donor-side edge and a contact edge to every
newly missed named branch set lie on opposite sides of one actual
separation.  Edge deletion and contraction induce the same labelled
boundary response language for each edge, and the two languages lie in
opposite extension differences.  A common equality partition is terminal.
The exact remaining theorem is therefore an intersection of these two
labelled response languages—or an explicit `K_7`, a direct two-vertex
`K_5`-model transversal contradiction, or a valid strict defect-one
descent—not another unlabelled path construction.

An actual order-seven output is now canonical enough to be a separate
rooted-model problem.  Every boundary-vertex deletion is `K_5`-minor-free,
so the boundary is at most five-colourable.  Equality gives precisely
`K_2\vee C_5`, two connected open shores, and an unrooted `K_5` model off
the two universal vertices; that model cannot be rooted at the five cycle
vertices.  No nonempty uniquely five-colourable boundary trace survives.
Thus the sharp exact-seven task is to reroute that unrooted model to the
five named roots or force a common shore partition, not to search for a
rigid boundary trace.

The old five-support/spanning-`K_6` packaging remains a falsification suite
and label-rich source of candidate reroutings, but it is no longer the
primary induction object.

## 5. Relation to the balanced order-eight branch

The balanced order-eight configuration remains the best label-rich
laboratory.  There the eligible adjacent pair has an explicit spanning
`K_6` model with `r=5`, and that model is reversibly coupled to a spanning
`K_7`-minus-one-edge model with nonadjacent singleton deficient branch
sets.  This proves that contact maximization alone cycles; it also offers
additional fixed labels with which to test the rooted-model exchange in
Section 4.

The balanced branch is no longer the definition of the main theorem.
Any mechanism discovered there must be restated in the uniform setup above
or explicitly identified as using additional balanced-boundary data.

## 6. Guardrails

- The join of `K_2` with the icosahedron shows that connectivity, a
  spanning `K_6` model, and large pole contact can end in a genuine
  separator or coherent two-vertex obstruction rather than a `K_7` model.
- A sharper audited planar-join construction realizes the exact
  three-common-singleton profile, buffer-colour saturation, all five Kempe
  connections, and the two exclusive-to-exclusive paths while forbidding
  every contact increase.  Its valid outputs are an order-seven separator
  and the universal two-vertex planarizing set; the host is six- rather
  than seven-chromatic.
- Five disjoint paths retain a palette permutation, not the individual
  colour pairing along each path.
- Even two disjoint diagonal bichromatic components plus the remaining
  common support component can cover all five model labels without
  admitting a label-preserving branch-set split.  In the audited planar
  join, the valid exits are instead a different order-seven separator and
  the fixed two-vertex planarizing set.
- Two colourful sets in a four-chromatic graph need not admit one `K_4`
  model meeting both sets in every branch set, even under substantial
  internal connectivity.  The lifted host hypotheses are essential.
- The failure persists for a planar four-connected core whose two-pole
  extension is five-chromatic and `K_6`-minor-free.  Static properties of
  the compressed core therefore do not replace the proper-minor responses.
- The connectivity-only assertion that an eight-connected graph containing
  a `K_7`-minus-one-edge minor contains `K_7` would imply the open
  seven-connected-to-`K_6` conjecture and is not used.
- A shortest locked subpath can migrate reversibly through its Kempe orbit
  while an order-seven separator is present.  Shortest-lock extremality is
  not a well-founded substitute for the component defect.
- Static exact traces on a boundary can have disjoint extension languages.
- The endpoint feasibility relation of a Mader delta-matroid does not
  preserve same-branch-set adjacencies or the internal paths needed for a
  labelled clique-minor construction.
- The recent colourful-minor structure theorem treats a related
  colour-to-branch-set problem, but its general clique-minor threshold is
  far above the present `K_6` scale.  A positive result here must use the
  exact five-connectivity and minor-critical hypotheses.

## 7. Immediate dependencies

- [global adjacent-pair palette frame](../results/hc7_global_adjacent_pair_palette_frame.md)
- [palette-permutation linkage and contact consequences](../results/hc7_adjacent_pair_palette_linkage.md)
- [bichromatic support and exact missing-colour rotation](../results/hc7_adjacent_pair_bichromatic_support_dichotomy.md)
- [palette dichotomy for contracted induced bipartite subgraphs](../results/hc_bipartite_contraction_palette_dichotomy.md)
- [diagonal bichromatic components after a bipartite contraction](../results/hc_bipartite_contraction_bichromatic_components.md)
- [concentrated-rotation normalization and separator](../results/hc7_concentrated_rotation_normalization.md)
- [connected two-colour compression to a five-chromatic core](../results/hc7_star_kempe_five_core_compression.md)
- [exhaustive adjacent-pair separator-or-core theorem](../results/hc7_adjacent_pair_separator_or_five_core.md)
- [deficient-component separator in a contact-maximal rooted model](../results/hc7_maximal_rooted_k4_deficient_component_separator.md)
- [colour-matched repair path](../results/hc7_colour_matched_repair_path.md)
- [component exchange criterion](../results/hc7_colour_matched_path_component_exchange.md)
- [fixed-path exchange or separation](../results/hc7_colour_matched_path_exchange_or_separator.md)
- [all-cut interval and component-defect criterion](../results/hc7_colour_matched_path_all_cut_interval_exchange.md)
- [component-contact defect theorem and two-tree equality structure](../results/hc7_component_contact_defect_theorem.md)
- [normal form around a lifted simplicial component](../results/hc7_defect_one_simplicial_normalization.md)
- [path normal form for a distinguished sixth branch set](../results/hc7_minimal_sixth_branch_set_path.md)
- [attachment forcing from proper-minor colourings](../results/hc7_edge_response_attachment_forcing.md)
- [labelled near-`K_7` model and internal-edge colouring fork](../results/hc7_defect_one_near_k7_edge_fork.md)
- [rainbow-diamond separation in the four-labelled two-tree](../results/hc7_defect_one_rainbow_diamond_separator.md)
- [connected deficient-branch-set trichotomy](../results/hc7_connected_one_hole_trichotomy.md)
- [common-neighbour-rooted fan at a double-critical edge](../results/hc7_double_critical_edge_rooted_fan.md)
- [fan collision at a globally minimum deficient branch set](../results/hc7_near_k7_minimal_path_fan_collision.md)
- [oppositely oriented boundary responses at a reversible rotation](../results/hc7_rotation_opposite_boundary_responses.md)
- [two-vertex `K_5`-model transversals contradict seven-chromaticity](../results/hc7_two_vertex_k5_transversal_chromatic_obstruction.md)
- [classification and no-rigid-trace theorem for exact seven-vertex boundaries](../results/hc7_exact7_no_rigid_trace.md)
- [one-step minor dynamics and the exact common-hole law](../results/hc7_star_core_one_step_minor_dynamics.md)
- [contracted-path list obstruction](../results/hc_contracted_path_list_lock.md)
- [two-vertex transversal implies an order-seven separation](../results/hc7_k5_transversal_order7_separator.md)
- [paired colourful-set `K_4` frontier](hc7_two_colorful_sets_rooted_k4_frontier.md)
- [two-pole contact and branch-set split](../results/hc7_atomic_two_pole_contact_trichotomy.md)
- [canonical balanced deletion model and reversible exchange](../results/hc7_outer_edge_canonical_k6_rotation.md)
- [balanced order-eight technical laboratory](hc7_balanced_order8_frontier.md)
- [endpoint-only delta-matroid barrier](../barriers/hc7_labelled_mader_delta_enrichment_barrier.md)
- [static exact-trace parity barrier](../barriers/hc7_aligned_matching_exact_trace_parity_barrier.md)
- [exact three-common-branch-set two-apex barrier](../barriers/hc7_three_common_geodesic_two_apex_barrier.md)
- [five-connected two-colourful-set rooted-`K_4` barrier](../barriers/hc7_two_colorful_sets_paired_k4_barrier.md)
- [planar four-connected paired-colourful-set barrier](../barriers/hc7_paired_colourful_planar_core_barrier.md)
- [connectivity-only near-`K_7` augmentation hardness](../barriers/hc7_eight_connected_near_k7_augmentation_hardness.md)
- [static boundary responses plus seven-chromaticity still need global minor exclusion](../barriers/hc7_k35_no_common_state_or_two_vertex_transversal.md)
- [shortest locked interval orbit barrier](../barriers/hc7_contracted_path_shortest_lock_orbit_barrier.md)
- [forced repeated colour without a rooted-model exchange](../barriers/hc7_repeated_colour_rooted_k4_exchange_barrier.md)

## 8. Primary external inputs

- K. Kawarabayashi, A. S. Pedersen and B. Toft,
  [*Double-critical graphs and complete minors*](https://doi.org/10.37236/359),
  Electronic Journal of Combinatorics 17 (2010), R87, Theorem 7.1.
- A. Martinsson and R. Steiner,
  [*Strengthening Hadwiger's conjecture for 4- and 5-chromatic graphs*](https://doi.org/10.1016/j.jctb.2023.08.009),
  Journal of Combinatorial Theory, Series B 164 (2024), 1--16,
  Theorem 1.3 and Corollary 1.4.
- E. Protopapas, D. M. Thilikos and S. Wiederrecht,
  [*Colorful Minors*](https://doi.org/10.4230/LIPIcs.ICALP.2026.149),
  ICALP 2026.  This is a conceptual comparison, not an invoked theorem at
  the present parameters.
