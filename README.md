# Hadwiger `HC_7` research programme

## Current verdict

`HC_7` is **not proved** here.

The target is to prove that every graph with no `K_7` minor is
six-colourable.  The programme works from a hypothetical minor-minimal
counterexample `G`.  Such a graph is seven-connected, seven-chromatic,
strongly seven-contraction-critical, and `K_7`-minor-free.

This is the sole authoritative status file.  The exact proof coverage is
in [the support-six checkpoint](active/hc7_support_six_coverage_checkpoint.md).
The previous long-form status is preserved in
[`archive/`](archive/README_2026-07-15_before_support_six_checkpoint.md).

## Active global target

Let `S_{<=6}(G)` be the family of vertex supports of all `K_5` minor
models using at most six vertices.  The first support-extension rung is

\[
                         \tau(S_{\le6}(G))\le2.         \tag{1}
\]

A pair meeting **every** `K_5` model, not only the small ones, is terminal:
deleting it leaves a `K_5`-minor-free graph, which is four-colourable by
known `HC_5`; two fresh colours then six-colour `G`.

The support-six rung is not yet proved.  Its purpose is to discover a
uniform labelled-model extension principle, not to start another finite
neighbourhood census.

## Audited frontier

The following are the main current results.

In parallel with the support-family extraction below, the earlier audited
literal-transversal and split-contraction theorems first produce a pair
whose smallest avoided `K_5` model has support six.  A normalized split
edge then either contracts inside a seven-connected quotient or lifts a
small quotient cut to an actual exact-seven adhesion.  This is a direct
input to `G1/G2`, not a third closed branch.

1. **Separated extraction.** If (1) fails, three small `K_5` supports can
   be selected with the sharp intersection bounds `3` for a `5/5` pair
   and `4` otherwise.  The all-literal branch gives `K_7`.
2. **Bounded critical kernel.** A minimal high-transversal support family
   has at most twenty-seven members.  Every member has a private
   transversal pair and graph-specific labelled arms.
3. **Cross-arm dichotomy.** Each private pair yields either a genuinely
   separated labelled triple or two unique near-identical arms
   `X+p,X+q` together with forced near-top replacement supports.  The
   first abstract draft was false in the `5/5` case; the corrected
   graph-specific theorem is independently audited.  A further
   composition theorem eliminates every rigid common-core outcome in
   which an avoided literal `K_5` meets `X`: the replacement cliques and
   a three-root cycle in the four-vertex deletion give a literal `K_7`
   model.  Two further audited theorems eliminate maximal overlap for an
   avoided order-six support, for either arm order.
4. **Terminal-rooted contraction kernel.** For any `k>=4` prescribed
   terminals in a simple three-connected graph, terminal-legal contractible
   edge descent gives a three-connected rooted minor on at most
   `k+floor(k/4)` vertices.  For five terminals the residue can be classified
   completely: the terminals root `F_5=K_1 join P_4`, a triangulated
   pentagon.  Combining its two actual rooted-bag chords with the audited
   cycle decoder closes the entire normalized arm-order-six overlap-four
   cross-arm cell to a literal `K_7`.  This is a uniform unbounded theorem,
   not a bounded-order census.
5. **Four-connected rooted clique-or-fan composition.**  Given at least
   five prescribed terminals in a four-connected graph and a fixed anchor
   triple, either one anchored four-set roots `K_4`, or all terminals lie on
   one facial cycle and root `K_1 join P` with any prescribed terminal bag
   universal.  In the normalized order-five-arm, overlap-three cell this
   produces a five-good-terminal dichotomy.  A fixed nine-/ten-object
   labelled decoder, independently replayed, turns every outcome into a
   literal `K_7`; in the off-face case it is essential to keep the bad
   terminal separate from the connected peripheral remainder.  Thus this
   entire unbounded normalized cell is closed.  Its global invocation first
   prunes reducible six-supports and only then selects the critical kernel;
   irredundancy is not imposed retroactively.
6. **Full six-terminal kernel composition.**  After deleting a
   three-vertex overlap and reserving one of the seven exterior terminals,
   terminal-legal contraction reduces the other six terminals to a
   three-connected rooted kernel on six or seven bags.  A complete labelled
   carrier census has 142 edge-minimal order-six carriers and 780
   terminal-irreducible order-seven kernels.  An independently audited
   ten-object decoder composes every carrier in every noncommon boundary
   state to a literal `K_7`.  This closes the entire normalized
   order-six-arm, overlap-three cell.
7. **Fixed-pair six-terminal composition.**  In the normalized
   order-five-arm, overlap-two cell, delete the two overlap vertices and
   reserve the two private roots.  The remaining six exterior terminals
   again lie in a three-connected deletion.  The exact joined relation has
   1,419 states; 1,179 have a common rooted `K_4`, and all 240 remaining
   states compose with every one of the 142/780 six-terminal kernels to a
   literal `K_7`.  The same fixed private pair works in every state.  An
   independent enumerator reproduced the state set, kernel catalogue and
   minor certificates, including a generic detector cross-check.
8. **Exact seven-terminal kernel bundle.**  For seven prescribed vertices
   in a simple three-connected graph, terminal-legal contraction leaves
   either one of 5,495 labelled edge-minimal order-seven carriers or an
   order-eight irreducible kernel.  The latter has exactly three structural
   forms: a wheel, a distance-three one-chord rim, or one specific
   two-chord rim.  These give 30,600 labelled templates, each with its full
   legal owner-absorption bundle.  The classification and its exact
   universal/existential quantifiers are independently audited.  This is a
   general rooted-carrier theorem, not yet a composition closure.
9. **Rigid double-root cover.** If the rigid outcome has nonempty overlap,
   every pair of vertices of the avoided support touching that overlap
   forces another small model containing both private roots.  With literal
   arms these compulsory models have a genuine two-state split-bag
   orientation.  This is the current labelled composition invariant.
10. **Disjoint three-split branch.** Minimal simultaneous contraction of
   two or three split edges either gives `K_7`, an actual exact-seven
   handoff, or a two-component boundary of order eight or nine that is
   pointwise full on both shores.
11. **Two-shore boundary absorption.** In that two-component residue from
   two or three disjoint normalized split models, every surviving
   order-eight/nine boundary is four-colourable.  The sole five-chromatic
   census exception `K_2 vee C_7` is eliminated by a separate branch-set
   theorem.
12. **Uniform common-neighbour rooted principle.** If

   \[
   \chi(J)=k+2,\quad uv\in E(J),\quad
   \chi(J-\{u,v\})\le k,
   \]

   then `N(u) cap N(v)` is colourful in the `k`-chromatic deletion.
   Whenever Strong Hadwiger holds for `k`, this gives a `K_{k+2}` model
   with singleton bags `{u},{v}`.  Martinsson--Steiner proves the needed
   strong theorem for `k=4`, so the `HC_7` four-colour branch has a
   label-faithful `K_6` model.
13. **Minimal contraction-forest saturation.** If a forest contraction is
   inclusion-minimal for lowering a quotient to `q` colours, then every
   side of every forest edge meets every non-own colour class in every
   terminal colouring.  Each one-edge predecessor has chromatic number
   exactly `q+1`.  This is simultaneous over the whole forest and is
   independently audited.

The principal theorem and audit files are linked from
[`active/hc7_support_six_frontier.md`](active/hc7_support_six_frontier.md).

## Exact live gaps

There are two live arrows.  Neither is hidden by the results above.

### G1. Decorated extraction and composition

Starting from the bounded private-pair kernel, turn the corrected
cross-arm dichotomy into one of:

* a row-compatible composition already covered by the proved split-model
  theorems;
* three disjoint normalized split models;
* a literal `K_7` or one global two-vertex transversal; or
* a state/model-preserving exact-seven handoff with a declared strict
  rank.

Bare support incidence is insufficient: explicit affine and fifteen-point
families falsify the strongest unlabelled alignment claims.  The
positive-overlap rigid cell is closed whenever the avoided support has
order five; both maximal-overlap cells are closed for an avoided order-six
support; the rooted-fan theorem closes the normalized arm-order-six
overlap-four cell; and finite rooted-kernel composition closes both
normalized overlap-three cells and the order-five-arm, overlap-two cell.
The live rigid cells are therefore overlap one for order-five arms, and
overlaps one and two for order-six arms, alongside the separated-triple
branch.
Every two-set in the avoided support meeting the overlap still forces a
compulsory double-root model.  The next concrete cell is the
order-six-arm, overlap-two interface.  Deleting the overlap and reserving
the fixed private pair leaves seven labelled terminals in a
three-connected deletion.  The complete seven-terminal kernel is now
classified; the active test is whether a state-dependent reserved pair
composes against every exact carrier bundle.  A bare cycle/biclique carrier
and a fixed reserved pair are both insufficient.  Further portal taxonomy
is not the target.

### G2. Forest-to-carrier composition

In the disjoint branch, the four-colour two-shore residue now gives a
minimal contraction forest and an exact `6 -> 5` predecessor at every
forest edge.

* If a terminal contraction image `z` has `chi(K-z)=4`, the two sides of
  its forest edge are the named bags of a `K_6` model.  The missing step is
  to preserve or extract a seventh connected carrier, equivalently to
  turn this model into an `S`-meeting `K_6` disjoint from a reserved full
  shore, a global pair, or a ranked exact-seven/near-`K_7` handoff.
* If `chi(K-z)=5`, every terminal five-colouring has an exact trichotomy:
  one side sees all five colours, the other side sees all five colours, or
  both sides omit the same unique colour.  A Hajós-join example realizes
  the last lock and proves that an unrooted regenerated `K_5` cannot break
  it.  Ambient seven-connectivity and the original shore/model labels must
  be used.

The forest size is currently a local witness size, **not** a proved
recursive rank.

## Decisive guardrails

Do not retry the following without a materially new hypothesis.

* Connectivity plus a same-shore singleton-rooted `K_6` does not force
  `K_7`; `I_2 vee` the icosahedron gives an exact two-full-shore
  counterarchitecture.
* In the five-colour leaf branch, a six-critical Hajós join satisfies all
  local chromatic equalities and has a literal `K_5` avoiding the edge,
  but has treewidth five and no `K_7` minor.
* Four-colourability, two-shore join exclusion, and every private-block
  query do not force a common boundary state.  The two parity languages on
  `K_4 dotcup K_4` are disjoint.
* Unrooted quotient regeneration supplies no labelled carrier by itself.
* No further union-size or Moser census is active.

These barriers are in [`barriers/`](barriers/); they are guardrails, not
counterexamples to `HC_7`.

## Trust labels

* **Proved:** a written mathematical proof is present.
* **Independently audited:** a separate agent cold-checked the statement
  and proof; corrections are recorded beside the theorem.
* **Computer-assisted:** the reduction and exhaustive encoding are written
  separately, and the scripts are retained in [`active/`](active/).
* **Barrier:** a concrete counterexample to a proposed intermediate lemma,
  not to Hadwiger's Conjecture.

Computational results are not treated as proofs of unbounded statements.

## Repository layout

```text
.
├── README.md    # this authoritative status
├── results/     # proved lemmas and adjacent audits
├── active/      # current spine, finite checks, and falsifiers
├── barriers/    # counterexamples to intermediate mechanisms
└── archive/     # superseded work retained for provenance
```

The project is licensed under the [MIT License](LICENSE).
