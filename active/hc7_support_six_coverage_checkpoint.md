# Coverage checkpoint for the first support-six rung

**Status:** authoritative proof-coverage map.  This is not a proof of the
support-six transversal theorem or of `HC_7`.

## 1. Target and standing contradiction

Let `G` be seven-connected, strongly seven-contraction-critical and
`K_7`-minor-free.  Let `F` be the supports of all `K_5` models using at
most six vertices.  The active target is

\[
                              \tau(F)\le2.              \tag{1.1}
\]

This file records exactly what follows if `tau(F)>2`.  A displayed arrow is
called **closed** only when a cited theorem covers every object entering
that arrow.

There is also a parallel audited normalization.  The global literal-`K_5`
transversal theorem produces a pair whose smallest avoided `K_5` support
has order at least six.  In the equality case, the support-six contraction
dichotomy normalizes the unique split edge and returns either a
seven-connected contraction or an actual exact-seven adhesion.  This
normalization supplies inputs to the two arrows below; it does not replace
the exhaustive support-family extraction under `tau(F)>2`.

## 2. Exhaustive first extraction

The small-support separated-triple theorem is proved and independently
audited.  It gives supports `A_1,A_2,A_3` with

\[
 |A_i\cap A_j|\le
 \begin{cases}
 3,&|A_i|=|A_j|=5,\\
 4,&\text{otherwise}.
 \end{cases}                                           \tag{2.1}
\]

Every order-five support is a literal `K_5`; every irredundant order-six
support is a normalized split model with one edge bag and one singleton
`K_4` core.

The all-literal branch is closed.  A two-apex pair would meet every `K_5`
model, contrary to `tau(F)>2`; hence `G` is non-two-apex.  Niu--Zhang then
applies to the three literal cliques with pairwise intersections at most
three and gives `K_7`.

Thus every live separated triple contains a split model.  **No proved
theorem currently says that the triple can be chosen row-compatible,
contraction-clean, or vertex-disjoint.**

Sources:

* `../results/hc7_support_at_most_six_separated_triple_extraction.md`; and
* the all-literal consequence recorded in
  `../results/hc7_one_split_two_clique_composition.md`.

## 3. Terminal composition branches and one exact handoff

The following branches have proved conclusions.  All are terminal except
for the exact-seven outcome explicitly retained in item 2.

1. If a split-edge contraction `H=G/e` remains seven-connected and `H` is
   two-apex, the contraction pullback returns a literal two-set meeting
   every support in `F`.  This uses the exclusion of a support-at-most-five
   `K_4` model in a five-connected planar graph.
2. One split model plus two literal `K_5` cliques has a proved trichotomy
   when the split is row-compatible and the three quotient cliques have
   pairwise intersection at most three.  The outcomes are `K_7`, a global
   pair, or a model-preserving exact-seven separation.  The last outcome
   is an unranked handoff, not a closure of the support-six theorem.
3. Three disjoint split bags over one common singleton `K_4` core give a
   `K_7` minor by rooted-triangle composition.
4. Three contraction-clean models close after simultaneous contraction
   whenever the quotient is seven-connected and either the three-clique
   union has order at least twelve, or the quotient is non-two-apex and
   the three quotient cliques meet pairwise in at most three vertices.
5. Any high-transversal exact-six support family contained in a nine-set
   gives `K_7`.  This is computer-assisted and has been independently
   replayed; the unique local exception is `complement(C_9)`, which
   seven-connectivity also eliminates.
6. Two disjoint small models admit a branch-faithful five-cluster, and an
   exact lifted separator can preserve all three named split models.  These
   are audited composition inputs, but neither supplies a colouring state,
   a strict rank, or the reserved carriers required for a `K_7`.

Sources:

* `../results/hc7_five_connected_planar_support_five_exclusion.md`;
* `../results/hc7_one_split_two_clique_composition.md`;
* `../results/hc7_global_split_model_composition.md`; and
* `../results/hc7_nine_vertex_support_six_closure.md`;
* `../results/hc7_two_model_five_cluster.md`; and
* `../results/hc7_three_split_exact_separator_handoff.md`.

These branches overlap, but they do not exhaust the mixed separated triple
from Section 2.  In particular, (2.1) does not imply row compatibility or
contraction cleanliness.

## 4. Exact disjoint three-split branch

There is one exhaustive subchain after the additional hypothesis that the
three selected split-model supports are pairwise vertex-disjoint.

Contract all three split edges.  If the quotient remains seven-connected,
the three disjoint quotient `K_5` cliques have union fifteen and the
published three-clique theorem gives `K_7`.  Otherwise choose a nonempty
inclusion-minimal bad contraction set `E`.

* `|E|=1` gives an actual exact-seven separation preserving the contracted
  named carrier.  It need not preserve every uncontracted carrier, the
  returned colouring state, the packet vector, or a strict global rank.
* `|E|=2` or `3` gives a six-connected quotient whose every six-cut
  contains all contracted images.  Literal expansion has order eight or
  nine and is pointwise full on every quotient component.
* Three or more quotient components give a displayed `K_7` model.
* With exactly two components, the expanded boundary is four-colourable.
  The order-eight/order-nine classification is computer-assisted and
  independently replayed.  Its unique five-chromatic exception
  `K_2 vee C_7` is eliminated by a separate audited universal-pair/core-fan
  theorem using the three disjoint models.

Sources:

* `../results/hc7_three_split_minimal_bad_contraction.md`;
* `../results/hc7_two_full_shore_boundary_absorption.md`;
* `../results/hc7_universal_pair_three_core_elimination.md`;
* `../results/hc7_leaf_rooted_chromatic_drop.md`; and
* `../results/hc7_minimal_contraction_forest_saturation.md`.

The exact residue of this subchain is therefore:

\[
 \boxed{\text{one unranked exact-seven handoff, or a two-full-shore
 four-colour boundary of order eight or nine}.}          \tag{4.1}
\]

Four-colourability alone does not supply a common boundary state.  The
balanced-colour shortcut is false: `K_{3,5}` at order eight and
`K_3 vee I_6` at order nine satisfy the state-free join exclusion but have
no colour-class pattern `2+2+2+2` or `3+2+2+2`, respectively.

There is a new audited terminal decoder for the `|E|=3` Mader path
obstruction.  If the published disjoint-three-clique argument reaches its
terminal `5+5+5` equality cell, each canonical six-cut contains only one
or two of the three contracted images.  This contradicts minimality of
`E`, which forces every six-cut to contain all three.  Thus that terminal
cell is closed.  The preceding weighted fan/cell induction has not been
established, so this does not remove the two-full-shore residue above or
prove the marked three-clique theorem.  See
`hc7_decorated_three_model_hwege.md` and
`hc7_weighted_klnz_terminal_decoder.md`, with the adjacent cold audit.

There is now one uniform replacement for a bare boundary-state search.
Contract an inclusion-minimal forest in the two open shores until the
quotient is five-colourable.  Every one-edge predecessor is exactly
six-chromatic, and every side of every forest edge meets all four non-own
colour classes in every terminal colouring.  If deletion of one
contraction image lowers the terminal graph to four colours, Strong
Hadwiger for four colours gives a `K_6` model with the two forest sides as
named bags.

This is a simultaneous invariant, but not yet a recursive rank.
Connectivity alone does not preserve the opposite shore as a seventh bag,
and a Hajós-join barrier shows that the five-chromatic deletion branch
cannot be closed by an unrooted regenerated `K_5`.

## 5. Global finite kernel and what it does not yet align

Every counterexample to (1.1) contains a 3-critical support subfamily of at
most twenty-seven members.  Each member has a private transversal pair.
For an avoided support `A` and its private pair `{p,q}`, the graph-specific
V-extraction produces a `p`-arm and a `q`-arm, each meeting `A` in at most
four vertices.  The corrected cross-arm theorem strengthens this to the
exact size-sensitive separated bound.  It gives either a genuinely
separated labelled triple, or unique arms

\[
                         X\cup\{p\},\qquad X\cup\{q\},
\]

together with both near-top replacements `(A-a)+p,(A-a)+q` for every
`a in A cap X`.

There is now one genuine composition consequence.  If `|A|=5`, then
`A cap X` must be empty.  Indeed, for `a in A cap X`, the literal cliques
`A`, `(A-a)+p`, and `(A-a)+q` make `a,p,q` complete to the four-clique
`A-a`; a common cycle through those three roots in the three-connected
four-vertex deletion, together with that clique, is a `K_7` model.

There are two further terminal consequences for `|A|=6`.

* If the arms have order five and `|A cap X|=4`, their common core is a
  literal `K_4`; the two roots are complete to it, and irredundancy makes
  `A-X` an edge collectively full to it.  A cycle through that edge and
  the two roots gives `K_7`.
* If the arms have order six and `|A cap X|=5`, the original support, one
  arm, and the five forced replacements are all seven six-subsets of one
  seven-set.  The full-seven-point lemma gives a small `K_6`, which
  seven-connectivity lifts to `K_7`.

The normalized arm-order-six overlap-four cell is now terminal as well.
The terminal-rooted contraction theorem says that any `k>=4` labelled
terminals in a simple three-connected graph have a three-connected rooted
minor on at most `k+floor(k/4)` vertices.  At `k=5` its residues admit a
complete hand proof: the five terminals always root
`F_5=K_1 join P_4`.  The two chords of that triangulated pentagon repair at
least one of the four fixed gate defects in either crossed order of the
audited overlap-four cycle decoder.  Thus this entire unbounded cell gives
a literal `K_7`; it does not merely return an unranked exact-seven handoff.

The normalized order-five-arm, overlap-three cell is now terminal too.
After deleting the three-vertex overlap, the exterior is four-connected.
A rooted clique-or-fan theorem says that five designated terminals either
contain a rooted `K_4`, or lie on one facial cycle with an adaptive universal
rooted bag.  The rooted-`K_4` outcome composes with the three overlap
singletons.  A fixed labelled decoder closes every facial outcome; when the
sixth terminal lies off the face, deleting it exposes a separate nonempty
connected peripheral carrier full to the five boundary bags.  Keeping those
two objects separate returns a literal `K_7` in every residue.  The
computation is confined to the fixed nine-/ten-object interface and places
no bound on the exterior order.

The normalized order-six-arm, overlap-three cell is also terminal.  After
deleting the overlap and reserving one of seven exterior terminals, the
other six terminals lie in a three-connected graph.  Terminal-legal
contraction yields either one of 142 labelled edge-minimal order-six
carriers or one of 780 labelled terminal-irreducible order-seven kernels.
For every noncommon relation state, one reserved terminal works against
every possible kernel; in the order-seven case the extra bag can be merged
into a certified adjacent rooted bag.  An independently audited exact
ten-object decoder turns every such carrier into a literal `K_7`.  This is
a bounded rooted-kernel computation, not a bound on the exterior order.

This cell uses the standard irredundancy normalization in the correct order:
first delete every six-support containing a retained literal five-support,
then choose the critical kernel.  Transversal number is unchanged, and all
six-supports returned by the private-pair and replacement lemmas are members
of that same irredundant kernel.  One may not silently impose irredundancy on
an arbitrary kernel chosen before this pruning.

The normalized order-five-arm, overlap-two cell is also terminal.  Delete
the two overlap vertices and reserve the fixed private pair.  The other six
exterior terminals remain in a three-connected graph and hence reduce to
the complete 142/780 six-terminal kernel catalogue.  Of the 1,419 exact
joined boundary states, 1,179 contain the common rooted `K_4`; every one of
the other 240 composes with every possible kernel to a literal `K_7`.  The
same private pair works in every state.  The result and its independent
generic-minor-detector audit are recorded in
`../results/hc7_overlap_two_order_five_six_terminal_kernel_closure.md`.

The next carrier layer is now classified independently of this cell.  For
seven terminals in a simple three-connected graph, terminal-legal
contraction gives either one of 5,495 labelled edge-minimal order-seven
carriers or an order-eight irreducible kernel.  The order-eight kernels are
exactly the wheel, one distance-three chord family, and one two-chord
family, giving 30,600 labelled templates with their complete legal owner
bundles.  The theorem is
`../results/hc7_seven_terminal_irreducible_kernel_classification.md`.

That exact bundle closes two further unbounded cells.  For order-six arms
at overlap two, 148,488 noncommon states reduce to 8,220 minimal masks in
67 orbits; a state-dependent pair chosen before kernel exposure closes all
67 against every exact carrier.  For order-five arms at overlap one, 5,410
noncommon states reduce to 400 masks in six orbits; a reserve triple closes
all six.  Both results have independent relation, catalogue, detector and
literal-lift audits:

* `../results/hc7_overlap_two_order_six_seven_terminal_kernel_closure.md`;
* `../results/hc7_overlap_one_order_five_seven_terminal_kernel_closure.md`.

The corresponding eight-terminal layer is now understood as well.  Every
eight prescribed vertices in a simple three-connected graph root `C_8`,
`K_{3,5}`, or one explicit twisted `K_{3,5}`; an exact catalogue keeps the
one- and two-nonterminal contacts.  This does **not** close the next cell.
For order-six arms at overlap one, the relation has 132,000 inclusion minima
in 142 symmetry orbits.  Its first orbit defeats all 165 reserves containing
the overlap and all 495 arbitrary four-vertex reserves, already against an
order-eight kernel.  Exact branch-set enumeration and an independent SMT
encoding agree.  This is a barrier to single-kernel composition, not to the
rooted-carrier theorem or to `HC_7`.

The rigid structure also returns a global labelled family absent from the
original three-support certificate.  Every two-set `R subset A` meeting
`A cap X` is avoided by a support `D_R` containing both `p,q`.  In the
literal-arm cell, `pq` is absent and every `D_R` is an order-six model with
exactly one private root in its split bag.  The next rigid-cell theorem
must compose these two orientations; a further overlap-size reduction is
not accepted as closure.

These are bounded global certificates:
the witness family has bounded cardinality, and every member carries named
support-incidence V data.  They do **not** yet supply a branch-set exchange,
align the split rows of the separated triple, or compose the rigid
near-top replacement family.

Sources:

* `../results/hc7_support_six_bounded_critical_kernel.md`;
* `../results/hc7_support_six_private_pair_v_extraction.md`;
* `../results/hc7_private_pair_cross_arm_dichotomy.md`; and
* `../results/hc7_private_pair_cross_arm_dichotomy_audit.md`;
* `../results/hc7_literal_cross_arm_overlap_elimination.md`; and
* `../results/hc7_literal_cross_arm_overlap_elimination_audit.md`;
* `../results/hc7_k4_two_vertices_one_edge_cycle_composition.md`;
* `../results/hc7_cross_arm_maximal_order_six_overlap_elimination.md`; and
* `../results/hc7_rigid_cross_arm_double_root_cover.md`;
* `../results/hc7_five_terminal_rooted_fan.md`;
* `../results/hc7_eight_terminal_rooted_carrier_trichotomy.md`, with its
  adjacent independent audit;
* `../barriers/hc7_overlap_one_exact_eight_kernel_bundle_barrier.md`;
* `../results/hc7_cross_arm_overlap_four_cycle_decoder.md`;
* `../results/hc7_four_connected_terminal_fan_or_k4.md`; and
* `../results/hc7_overlap_three_five_good_decoder.md`;
* `../results/hc7_overlap_three_six_terminal_kernel_closure.md`, all with
  adjacent independent audits; and
* `../results/hc7_overlap_two_order_five_six_terminal_kernel_closure.md`,
  with its adjacent independent audit; and
* `../results/hc7_seven_terminal_irreducible_kernel_classification.md`,
  with its adjacent independent audit; and
* `../results/hc7_overlap_two_order_six_seven_terminal_kernel_closure.md`;
* `../results/hc7_overlap_one_order_five_seven_terminal_kernel_closure.md`,
  both with adjacent independent audits.

## 6. The two live arrows

The support-six rung has not been reduced solely to (4.1).  The remaining
obligations in this proof spine are grouped into two global arrows.

### G1. Decorated extraction/composition

Starting from the bounded critical kernel and its private-pair V data,
prove one of:

1. a row-compatible one-split/two-literal-clique composition covered by
   Section 3, with its unranked exact-seven outcome passed to `G2`;
2. three vertex-disjoint normalized split models, entering Section 4;
3. a `K_7` minor or one global support-six transversal pair; or
4. a model/state-preserving exact-seven handoff with a declared strict
   rank.

In the rigid branch, the concrete subproblem is now to compose the
mandatory double-root split orientations into one of these outcomes.  Both
maximal-overlap geometries, the normalized overlap-four cell, both
normalized overlap-three cells, both overlap-two cells, and the
order-five-arm overlap-one cell are terminal.  The only live positive
overlap is order-six arms at overlap one.  The preferred mechanism is
now a simultaneous split-row contraction/exchange or coupled model
regeneration.  A single labelled finite-kernel decoder is insufficient by
the exact barrier above.

Bare support incidence cannot prove this: explicit affine and
fifteen-point families falsify the strongest unlabelled extraction
claims.  A proof must use the actual branch bags, complement star-forest
constraints on six-supports, or proper-minor transitions.

### G2. Five-connected punctured-cube composition

For three pairwise disjoint split supports, delete their matching `F` and
put `K=G-F`.  The weighted matching-deletion theorem closes
`kappa(K)=4` by a model-preserving exact-seven handoff.  In the residual
branch

\[
       \kappa(K)\ge5,\qquad \chi(K)\in\{5,6\},
\]

and every nonempty equality state on `F` is realized exactly.  The
missing-colour theorem now gives, from every equal row in every such
state, either a labelled path in `K-Q_i` or an exact legal contraction
state carried by one literal two-colour component.  From the all-equal
state the first non-path move strictly lowers the equality-set size from
three to one or two.

The open composition theorem must use one common all-equal colouring,
its three complementary colour pairs, and the weighted separator rank to
produce `K_7`, one global pair, or a strict anchored exact-seven handoff.
Abstract signature iteration is insufficient: explicit highly connected
examples realize both double outputs and transition cycles.  A bare
separator or an arbitrary changed equality partition is not an accepted
outcome.

## 7. Research priority

`G1` is the coverage bottleneck; `G2` is the sharpest closed laboratory.
Further boundary or union-size enumeration is prohibited unless it proves
an invariant used in one of these two arrows.  Both normalized
overlap-three cells, both overlap-two cells and the order-five-arm
overlap-one cell are closed.  The immediate constructive experiment is the
simultaneous composition of the separated triple and the remaining
order-six-arm, overlap-one cell.  The compulsory double-root orientations
and split-row duties must remain literal labels throughout.  Any separator
handoff must carry all named models and strictly decrease a declared global
rank.  `G2` remains the independent laboratory for such an exchange.
