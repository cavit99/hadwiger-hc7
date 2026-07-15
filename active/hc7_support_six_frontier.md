# Active frontier: support-six extension for `HC_7`

**Status:** active proof spine.  `HC_7` and the support-six transversal
theorem are not proved.

## 1. Target

Let `G` be seven-connected, strongly seven-contraction-critical and
`K_7`-minor-free.  Let `F` be the supports of all `K_5` models using at
most six vertices.  The active target is

\[
                              \tau(F)\le2.             \tag{1.1}
\]

The exhaustive dependency map is
[`hc7_support_six_coverage_checkpoint.md`](hc7_support_six_coverage_checkpoint.md).
The two live arrows are decorated extraction (`G1`) and forest-to-carrier
composition (`G2`).

The earlier audited literal-transversal and support-six contraction
dichotomy supply a parallel normalization: choose a pair whose smallest
avoided `K_5` support has order six, normalize its split edge, and obtain
either a seven-connected contracted host or an actual exact-seven
adhesion.  This feeds the two arrows below; it does not close either one.

Sources:

* [`../results/hc7_global_literal_k5_transversal.md`](../results/hc7_global_literal_k5_transversal.md)
* [`../results/hc7_global_support_six_contraction_dichotomy.md`](../results/hc7_global_support_six_contraction_dichotomy.md)

## 2. `G1`: global decorated extraction

The proved starting data are:

* a 3-critical high-transversal subfamily of at most twenty-seven
  supports;
* one private transversal pair for every member;
* a graph-specific arm on each endpoint of every private pair; and
* the corrected cross-arm dichotomy.

The dichotomy returns either a genuinely separated labelled triple or a
rigid certificate

\[
                      X\cup\{p\},\qquad X\cup\{q\},   \tag{2.1}
\]

together with every forced replacement `(A-a)+p,(A-a)+q` for
`a in A cap X`.

The audited literal-support composition theorem closes the rigid cell
whenever `|A|=5` and `A cap X` is nonempty.  For `a in A cap X`, the
four-clique `A-a`, the two literal replacement cliques, and a common cycle
through `a,p,q` in the four-vertex deletion form a `K_7` model.  Hence a
literal avoided support is disjoint from the common arm core.

The remaining theorem must use the actual five-bag models on these
supports.  Accepted outcomes are:

1. a row-compatible one-split/two-clique composition;
2. three vertex-disjoint normalized split models;
3. a literal `K_7` or one global support-six transversal pair; or
4. a state/model-preserving exact-seven handoff with a strict declared
   rank.

Unlabelled support incidence cannot prove this.  The affine and
fifteen-point barriers remain decisive.

Sources:

* [`../results/hc7_support_six_bounded_critical_kernel.md`](../results/hc7_support_six_bounded_critical_kernel.md)
* [`../results/hc7_support_six_private_pair_v_extraction.md`](../results/hc7_support_six_private_pair_v_extraction.md)
* [`../results/hc7_private_pair_cross_arm_dichotomy.md`](../results/hc7_private_pair_cross_arm_dichotomy.md)
* [`../results/hc7_private_pair_cross_arm_dichotomy_audit.md`](../results/hc7_private_pair_cross_arm_dichotomy_audit.md)
* [`../results/hc7_literal_cross_arm_overlap_elimination.md`](../results/hc7_literal_cross_arm_overlap_elimination.md)
* [`../results/hc7_literal_cross_arm_overlap_elimination_audit.md`](../results/hc7_literal_cross_arm_overlap_elimination_audit.md)

## 3. `G2`: exact two-shore residue

For three vertex-disjoint normalized split models, a minimal bad
simultaneous contraction has one of the following proved outcomes:

* `K_7`;
* an unranked actual exact-seven handoff; or
* exactly two full open shores across a boundary of order eight or nine.

In the last case the boundary is four-colourable.  The computer-assisted
order-nine exception `K_2 vee C_7` is eliminated by a separate audited
branch-set theorem.

Sources:

* [`../results/hc7_three_split_minimal_bad_contraction.md`](../results/hc7_three_split_minimal_bad_contraction.md)
* [`../results/hc7_two_full_shore_boundary_absorption.md`](../results/hc7_two_full_shore_boundary_absorption.md)
* [`../results/hc7_universal_pair_three_core_elimination.md`](../results/hc7_universal_pair_three_core_elimination.md)

### 3.1 The new contraction-forest invariant

Choose spanning trees in the two shores and an inclusion-minimal forest
`F_0` whose contraction makes the graph five-colourable.  Put

\[
                            K=G/F_0.
\]

For every edge `e in F_0`, let `H_e=G/(F_0-e)` and let `x_e,y_e` be the
two sides of the split contraction image `z_e`.  The audited forest
saturation theorem gives, simultaneously for every edge,

\[
                    \chi(K)=5,\qquad\chi(H_e)=6,       \tag{3.1}
\]

and in every five-colouring of `K`, each side meets every colour other
than the colour of `z_e`.

If `chi(K-z_e)=4`, the uniform common-neighbour rooted theorem and Strong
Hadwiger for four colours give a `K_6` model in `H_e` with singleton bags
`{x_e},{y_e}`.  On expansion these are the two literal connected sides of
the forest cut.

Sources:

* [`../results/hc7_leaf_rooted_chromatic_drop.md`](../results/hc7_leaf_rooted_chromatic_drop.md)
* [`../results/hc7_leaf_rooted_chromatic_drop_audit.md`](../results/hc7_leaf_rooted_chromatic_drop_audit.md)
* [`../results/hc7_minimal_contraction_forest_saturation.md`](../results/hc7_minimal_contraction_forest_saturation.md)
* [`../results/hc7_minimal_contraction_forest_saturation_audit.md`](../results/hc7_minimal_contraction_forest_saturation_audit.md)

### 3.2 Exact remaining carrier problem

The next theorem must use the original shore/model attachments, not just
the six-chromatic kernel.

**Critical-image branch.**  Starting from the singleton-sided `K_6`,
produce an `S`-meeting `K_6` disjoint from a reserved connected full shore,
a literal `K_7`, one global pair, or a ranked exact-seven/labelled
near-`K_7` handoff.  Connectivity alone is false: `I_2 vee` the
icosahedron supplies a seven-connected, `K_7`-free, two-full-shore
counterarchitecture with such a `K_6`.

**Noncritical-image branch.**  If `chi(K-z_e)=5`, every five-colouring has
the exact availability trichotomy: one side sees all five colours, or both
sides have one common missing colour.  A Hajós join realizes the common
lock and has no `K_7`.  Thus the regenerated unrooted `K_5` is not enough;
ambient attachments must break the lock or expose a labelled separator.

Sources:

* [`../results/hc7_leaf_drop_five_colour_lock.md`](../results/hc7_leaf_drop_five_colour_lock.md)
* [`../barriers/hc7_leaf_drop_hajos_barrier.md`](../barriers/hc7_leaf_drop_hajos_barrier.md)
* [`../barriers/hc7_same_shore_singleton_k6_connectivity_barrier.md`](../barriers/hc7_same_shore_singleton_k6_connectivity_barrier.md)
* [`../barriers/hc7_four_colour_parity_language_barrier.md`](../barriers/hc7_four_colour_parity_language_barrier.md)

## 4. Uniform rooted principle extracted from `G2`

The following theorem is independent of the `HC_7` notation.  If

\[
 \chi(J)=k+2,\quad uv\in E(J),\quad
 \chi(J-\{u,v\})\le k,
\]

then `N_J(u) cap N_J(v)` is colourful in the `k`-chromatic deletion.
Therefore Strong Hadwiger for `k` produces a `K_{k+2}` model with
singleton branch bags `{u},{v}`.

For `k=4` this is unconditional by Martinsson--Steiner.  This closes the
palette-to-labelled-carrier gap **inside** the four-chromatic leaf kernel;
it does not supply the seventh carrier in the original graph.

## 5. Research rule

No new Moser taxonomy, raw portal classification, union-size census, or
unranked separator is admitted to this spine.  A promotion must discharge
one of `G1` or `G2` for an infinite family, create a genuinely strict
handoff, or falsify the stated carrier architecture in a way that changes
the global target.
