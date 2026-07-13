# Hadwiger programme: strategic assessment and closure prompt

## Part I. Where the programme actually stands

### 1. The objective has never changed

The terminal objective is the full statement

\[
  K_t\not\preccurlyeq G\quad\Longrightarrow\quad\chi(G)\le t-1
  \qquad(t\ge1),
\]

for every finite simple graph, including disconnected graphs.  Closing
\(\mathrm{HC}_7\) is a compulsory first milestone, not the final result.
No reduction, finite list of residual cells, equivalent rooted-minor
statement, or new unproved separator lemma is a solution.

### 2. What the early broad search established

The first portfolio deliberately tested critical graphs, contractions,
degeneracy, density, Kempe chains, rooted minors, graph-minor structure,
flows, algebraic and topological methods, odd minors, near-clique models,
and probabilistic constructions.  Its lasting output was not a general
proof but a reliable least-counterexample package.

If the conjecture fails, choose the least failing \(t\ge7\) and a
proper-minor-minimal counterexample \(G\).  For a minimum-degree vertex
\(v\), put \(H=G-v\) and \(N=N_G(v)\).  The audited facts include

\[
 \chi(G)=t,\quad \eta(G)=t-1,\quad \delta(G)\ge t,
 \quad \kappa(G)\ge7,
\]
\[
 \chi(H)=\eta(H)=t-1,\qquad \kappa(H)\ge6.
\]

Every \((t-1)\)-colouring of \(H\) uses every colour on \(N\), and no
proper subset of \(N\) is colour-saturating.  Contracting the star
\(\{v\}\cup S\), for any independent \(S\subseteq N\), produces an exact
trace colouring in which \(S\) is precisely the boundary part with the
contracted colour.  Every edge-deletion colouring gives the deleted
edge's ends the same colour and supplies all other colours in both
neighbourhoods.  The graph \(H\) has an unrooted \(K_{t-1}\)-model but no
one whose every bag meets \(N\).

This isolates the genuine uniform obstruction:

> **(U)** Counterexample-derived saturation, exact minor-transition
> witnesses, high connectivity, and an unrooted \(K_{t-1}\)-model must
> force an \(N\)-meeting \(K_{t-1}\)-model.

No audited proof of (U) exists.

The broad search also usefully killed many seductive shortcuts.  In
particular, criticality does not give the desired vertex connectivity;
contraction can increase chromatic number; Kempe connectivity does not
give the disjoint linkage needed for a clique model; list-Hadwiger is
false; density and current connectivity are quantitatively insufficient;
and abstract boundary extension sets can be realized far too flexibly.

### 3. The contact-model phase and its correction

A contact-maximal \(K_{t-1}\)-model and a maximum fan can be selected by a
valid lexicographic potential.  For that selected pair, all last portals
are rigid.  This is real but local.  Earlier claims eliminating contact
loads \(s=1,2\) and the \(R_5\) cell used invalid potential or descent
steps and were retracted.  They must not re-enter a proof.

This episode changed the standard of proof: every bag move must preserve
connectivity, disjointness, every labelled adjacency, and the recomputed
fan optimum.  It also showed that portal identities, rather than mere
contact counts, are the right data.

### 4. The \(t=7\) local programme

Known results establish Hadwiger through \(t=6\).  For \(t=7\), the
extremal bound supplies a minimum-degree vertex of degree \(7,8\), or
\(9\).

At degree seven, every exact six-colouring has a repeated nonedge
\(a,b\subseteq N\) and five uniquely coloured roots.  Kriesell--Mohr
packages those five roots into a rooted \(K_5\)-model.  The exact issue is
to reserve, disjointly from the five bags, a connector containing the
repeated pair and meeting every rooted bag.

The two-exterior degree-seven case is now completely closed.  A labelled
enumeration of all \(2^{21}\) seven-vertex neighbourhoods reduces the hard
case to the Moser spindle and one one-edge extension.  Two-anchor gluing
eliminates the extension, and supported-pair exact-state transfer
eliminates every mixed Moser support word.  Thus a degree-seven
counterexample has one exterior component.

In the sole-exterior pure-Moser cell, every tree, unicyclic, bicyclic, and
every safely six-shore-contractible tricyclic exterior has been
eliminated.  The two remaining tricyclic quotients are the friendship of
three triangles and the chain of three triangle blocks; otherwise a
survivor has cyclomatic number at least four.  This is substantial local
progress, not closure of the one-component degree-seven case.  An
order-six reserved-connector separation has also been reduced to two full
connected shores of order at least six; every safely contractible internal
edge is terminal-tight or protected by an exact order-seven separator.
The required uncrossing theorem is missing.

For degree eight and nine, the proved component bounds are now

\[
 d(v)=8\Rightarrow \#\operatorname{comp}(G-N[v])\le2,
 \qquad
 d(v)=9\Rightarrow \#\operatorname{comp}(G-N[v])\le3.
\]

Some frame families and small portal-transition cells are closed, but the
remaining one/two-component degree-eight and one/two/three-component
degree-nine cells are not classified or eliminated.  The exceptional
\(K_3\dot\cup K_4\) sole-exterior degree-seven cell also remains.

Consequently \(\mathrm{HC}_7\) has not been proved.

### 5. The exact-state and full-shore phase

This phase produced the most reusable general mathematics so far.

* **Exact boundary-state transfer.**  A complementary clique realization
  of an independent boundary partition forces that exact partition on the
  opposite piece.  Bilateral realizations with a colour absent from
  \(N\) glue to colour \(G\).
* **Portalized transfer.**  The theorem remains valid across a genuine
  adhesion \(X=N\cup P\), with portal-only colour blocks tracked exactly.
* **One-step transition theorem.**  Every label-preserving internal
  deletion or contraction forces a new low-neighbourhood exact state,
  accepted by all other pieces and rejected by the original piece.
* **Uniform shore packing and defect atlases.**  Bad two-piece quotients
  yield internal shore connectivity, bounds on components behind a cut,
  and rooted-assembly criteria.
* **Knitted small-nonclique adhesion theorem.**  For a complete
  multipartite adhesion with nonsingleton core \(T\) and singleton clique
  \(R\), if \(8|T|+|R|<t+1\), either a small relative separator exists or
  both sides knit the same exact partition and colourings glue.

For an order-seven boundary with two connected full shores, the exact
quotient programme now closes every missing-edge graph through five edges.
At six missing edges, all types but \(C_6\dot\cup K_1\) are closed.  The
last \(2K_3\dot\cup K_1\) type was eliminated by a genuine rooted-shore
theorem, not merely a finite size check.

The \(C_6\dot\cup K_1\) laboratory is tightly constrained.  Every
nonsingleton shore is internally two-connected; every internal two-cut
has exactly two sides; compatible opposite crossings give an explicit
\(K_7\); opposite frame pairs acquire unique shore owners; and neither
shore admits an antipodal two-linkage or a nonidentity prism-matching
three-linkage.  What remains is an intersecting pairwise-but-not-triple
rope/linkage system.  Symbolic portal orders cannot be compared unless
the same actual representatives are used; an earlier orientation argument
was correctly retracted.

### 6. Honest strategic judgment

The programme is much stronger than at the beginning.  It has created
several publishable-looking lemmas, closed a real degree-seven family, and
replaced vague colour-gluing with exact portalized state calculus.
Nevertheless, the logical distance to the full conjecture remains large.

The main risk is **local-atlas drift**: solving the next missing-edge
layer or the next bounded exterior can continue indefinitely without
proving that every counterexample enters such a cell.  The next run must
therefore stop treating finite classifications as the main line.  The
\(C_6\) and Moser cells should be used as laboratories for one common
theorem about stabilized separators, exact state transitions, and
label-preserving branch-set augmentation.

The decisive missing bridge is:

> From a contact-maximal labelled clique model, either augment contact, or
> extract a laminar portalized separation whose forced one-step states
> contain a common exact state; then apply portalized transfer.

The knitted theorem proves this only for one quantitatively small class of
adhesions.  The Moser tight separators and the \(C_6\) cyclic ownership
system are the two smallest nontrivial tests of the large-adhesion case.

Closing \(\mathrm{HC}_7\) without extracting this bridge would still leave
the all-\(t\) goal essentially untouched.  Conversely, a correct uniform
contact-augmentation/colour-gluable-adhesion theorem would finish the
least-failing-parameter induction and therefore the whole conjecture.

---

## Part II. Prompt for the next execution

### Mission

Prove Hadwiger's Conjecture in full:

> For every integer \(t\ge1\), every finite simple graph with no
> \(K_t\)-minor is \((t-1)\)-colourable.

Disconnected graphs are allowed.  Treat \(\mathrm{HC}_7\) as the first
mandatory milestone, then prove the uniform least-counterexample theorem
for every \(t\).  Assume for this research task that an affirmative proof
exists, but do not assume any unproved lemma or convert the instruction
into evidence.

Use up to 64 agents dynamically; if the environment exposes fewer slots,
keep every available slot on a concrete independent proof or audit task.
Do not consider termination before at least one hour of substantive search,
with repeated synthesis and reassignment after stalled or falsified routes.

Do not terminate with a reduction, an equivalent conjecture, a residual
case list, a bounded computation, or a proof only for \(t=7\).  If a full
proof is not found after the allotted exhaustive run, return only the
strongest new rigorously audited theorem and the single exact implication
still missing.

### Authoritative starting state

Work from the repository root.  Read these files fully,
in this precedence order, before proposing lemmas:

1. `hadwiger_active_goal_checkpoint.md`
2. `hadwiger_strategic_assessment_and_closure_prompt.md`
3. `hadwiger_execute_round_results.md`
4. `hadwiger_strongest_valid_derivation.md`
5. `hadwiger_corrected_package_audit.md`
6. `hadwiger_portal_exact_boundary_transfer.md`
7. `hadwiger_exact_block_hypergraph.md`
8. `hadwiger_defect_atlas_connectivity_principle.md`
9. `hadwiger_defect_star_principle.md`
10. `hadwiger_defect_atlas_rooted_assembly.md`
11. `hadwiger_balanced_chain_exact_state.md`
12. `hadwiger_small_nonclique_knitted_adhesion.md`
13. `hadwiger_c6_two_piece_locks.md`
14. `hadwiger_c6_opposite_crossing_dichotomy.md`
15. `hadwiger_c6_three_linkage_exclusion.md`
16. `hadwiger_reserved_connector_portal_transfer.md`
17. `hadwiger_relative_shore_contraction.md`

Later adversarial audits control over earlier optimistic notes.  In
particular, do not reuse the old \(s=1,s=2,R_5\) contact closures or the
retracted selected-representative orientation argument.

### The theorem that must drive the run

Let \(t\) be the least failing parameter, \(r=t-1\), \(G\) a
proper-minor-minimal counterexample, \(v\) a minimum-degree vertex,
\(H=G-v\), and \(N=N(v)\).  Fix a labelled \(K_r\)-model in \(H\)
maximizing contact with \(N\) under the audited lexicographic potential.

Prove the following, or a strictly weaker statement that still yields the
same conclusion:

> **Contact-transition closure theorem.**  Either the model can be changed
> to increase the number of bags meeting \(N\), or there is an
> \(X\)-piece decomposition, with all branch-set labels and portal
> vertices retained in the adhesion \(X\), and an exact independent
> partition \(\Pi\) of \(X\) such that:
> 1. every piece complement clique-realizes \(\Pi\);
> 2. at most \(t-2\) blocks of \(\Pi\) meet \(N\); and
> 3. all contractions and expansions are proper minor operations.

In the second outcome, apply the already proved portalized exact-transfer
theorem to colour \(G\).  Iterating the first outcome reaches an
\(N\)-meeting \(K_r\)-model, which with \(\{v\}\) is a \(K_t\)-minor.
This closes the least-failing-parameter induction.

This statement is a target, not a permissible black box.  A successful
run must prove the mechanism producing the decomposition and common state.

### Required proof architecture

Run four mutually checking tracks, using as many independent agents as are
available and reallocating them dynamically.

#### Track A: labelled gammoid and laminar separators

1. Build the vertex-capacitated gammoid from \(N\) to the labelled model
   bags.
2. Express failure of contact augmentation by an explicit minimum
   separator, with every last portal and affected bag label recorded.
3. Uncross inclusion-minimal separators.  Prove submodularity statements
   with the actual terminal sets; do not assume laminarity.
4. Produce either a label-preserving rerouting that raises contact, or a
   lean tree decomposition rooted at \(N\).
5. At every adhesion give quantitative thresholds.  If it is small, apply
   the knitted theorem.  If it is large, build the required disjoint
   labelled routes.  Do not leave “small/large” qualitative.

The first deliverable is a fully proved augmentation-or-one-adhesion lemma,
including the precise separator order and the branch-set surgery.

#### Track B: exact-state transitions and holonomy

For a laminar chain of adhesions, decorate each state by:

* its exact equality partition, not just its defect;
* branch-set and portal labels;
* the color permutation induced when passing the adhesion; and
* the one-step deletion/contraction operation forcing the state.

Prove an exact transfer theorem along a path of bags.  On a cyclic
decomposition, prove one of:

1. the color holonomy has a compatible fixed exact state, so the pieces
   glue; or
2. a nontrivial orbit supplies explicitly connected, disjoint,
   pairwise-adjacent branch sets and therefore augments the clique model.

Nontrivial holonomy by itself does not imply a minor.  The proof must give
the branch sets.  Defect stabilization alone is insufficient.

Use the one-step transition theorem aggressively: for every internal
edge/vertex operation, the operated side must acquire a state accepted by
all other pieces and rejected by the original side.  Prove a finite-state
minimality lemma from this operation-indexed collision property.  Static
extension families alone are known to be too flexible.

#### Track C: two hard laboratories

Use the laboratories to falsify or prove the abstract lemmas, not as ends
in themselves.

1. **\(C_6\dot\cup K_1\) two-full-shore cell.**  Starting from the exact
   28 maximal bad defect pairs, two-cut structure, frame ownership, and
   linkage exclusions, close the remaining pairwise-but-not-triple rope
   system.  Seek either a common actual portal representation, a positive
   crossing/linkage, or an exact-state cycle with gluable holonomy.  Any
   symbolic-order proof must first identify the same portal vertices in
   all comparisons.
2. **Moser order-six reserved connector.**  In a minimum no-model shore,
   uncross the exact order-seven separators protecting non-terminal-tight
   edges.  Prove that a laminar outcome transfers a common portal state,
   while a crossing pair yields either the reserved \(a\)-\(b\) connector
   or six rooted bags.  Dispatch the two tricyclic cactus quotients only as
   a sanity check; do not stop there.

Success on either laboratory must be abstracted into a lemma usable by
Track A or B.  Conversely, every Track A/B lemma must be tested on both
laboratories.

#### Track D: independent closure and red-team audit

Keep independent work on:

* the remaining degree-eight/nine cells using portal transitions rather
  than static contact rows;
* the exceptional \(K_3\dot\cup K_4\) sole exterior;
* the port-labelled \(K_7^\vee\) peel-or-separator route, with
  contraction-critical color witnesses aligned to the model; and
* adversarial construction of boundaried counterexamples to every proposed
  intermediate lemma.

A counterexample must be used to state the minimal additional hypothesis,
not merely to abandon the route.

### Agent management

Maintain a live registry with columns:

| family | precise target lemma | required hypotheses | latest concrete output | audit status | blocker |
|---|---|---|---|---|---|

Do not let finite enumeration dominate merely because it returns quickly.
Preserve at least three incompatible proof mechanisms through multiple
rounds.  Cross-pollinate only after independent agents have produced a
proof, construction, or counterexample.  When a route reaches a lemma
equivalent to (U), mark it blocked unless it supplies a new invariant or a
constructive induction.

Every agent return must contain one of:

* a proved lemma with explicit branch sets or exact colour alignment;
* a concrete counterexample and the exact failed hypothesis;
* an independently replayable finite certificate plus a hand theorem; or
* a precise separator configuration and a proved next implication.

Reject broad strategy summaries and unaudited “routine” compatibility
claims.  Continue launching rounds after local successes; do not stop at
the first new theorem.

### Forbidden shortcuts and mandatory audits

Do not assume:

* \(\chi(G/e)\le\chi(G)\);
* critical graphs have the needed vertex connectivity;
* pairwise Kempe paths are simultaneously disjoint;
* arbitrary support labels are realizable;
* a spanning model has an outside component;
* connectivity alone gives a removable path or labelled bag split;
* state equality on \(N\) is enough when portal colors differ;
* symbolic portal precedence compares different representatives;
* a static boundary extension family encodes minor-criticality; or
* a local quotient model lifts without checking connectedness,
  disjointness, every pairwise bag adjacency, and exact boundary traces.

For every candidate terminal proof, assign independent red teams to check:

1. every minor operation and its lifting;
2. branch-set connectivity, disjointness, and all adjacencies;
3. exact rather than coarsened boundary states;
4. palette alignment across every portalized adhesion;
5. the exact proved connectivity bound;
6. noncircular use of Hadwiger, Strong Hadwiger, Hajós, list-Hadwiger, or a
   rooted assertion of equivalent strength;
7. the induction at the least failing \(t\); and
8. disconnected graphs and the base cases \(t\le6\).

### Computational discipline

Computations may discover finite lemmas but cannot substitute for the
uniform theorem.  Every computational claim needs an exact mathematical
statement, separated discovery and verification, exhaustive coverage,
explicit witnesses, and a stated trust boundary.  Do not extrapolate from
bounded shore order, cyclomatic number, or missing-edge count without a
proved reduction.

Public search may be used only for ordinary background and standard named
theorems, not to search for a solution to this exact conjecture.

### Terminal condition

The successful terminal proof has this form:

1. handle disconnected graphs by components and verify \(t\le6\);
2. assume a least failing \(t\ge7\) and take a proper-minor-minimal
   counterexample;
3. prove the contact-transition closure theorem from its stated
   hypotheses;
4. obtain an \(N\)-meeting \(K_{t-1}\)-model or an exact portalized
   coloring of \(G\); and
5. derive a contradiction in both cases.

Return a self-contained proof only after this chain survives independent
audit.  Closing \(\mathrm{HC}_7\), \(C_6\dot\cup K_1\), the Moser cell, or
another finite layer is progress but not permission to terminate.
