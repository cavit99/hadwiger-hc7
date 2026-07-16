# Closure of the size-three minimal bad contraction branch

**Status:** proved and independently cold-audited in
[`hc7_three_split_marked_mader_branch_closure_audit.md`](hc7_three_split_marked_mader_branch_closure_audit.md).

This note composes the audited marked Mader reductions and decoders.  Its
exact conclusion is that an inclusion-minimal bad contraction set cannot
consist of all three split edges of three vertex-disjoint six-vertex
`K_5` models.  It does not treat a minimal bad set of order two or prove
the global support-six theorem.

## Theorem

Let `G` be a seven-connected `K_7`-minor-free graph containing three
pairwise vertex-disjoint six-vertex `K_5` models

\[
 M_i=Q_i\mathbin{\dot\cup}\{x_i,y_i\}\qquad(i=1,2,3),             \tag{1}
\]

where each `Q_i` is the literal four-clique of singleton bags and
`x_iy_i` is the edge forming the fifth branch bag.  Put

\[
                         F=\{x_1y_1,x_2y_2,x_3y_3\}.              \tag{2}
\]

Then `F` cannot be an inclusion-minimal nonempty set of these split edges
such that `G/F` is not seven-connected.

## Proof

Suppose otherwise and put `H=G/F`, writing `z_i` for the image of
`x_iy_i` and

\[
                         L_i=Q_i\cup\{z_i\}\cong K_5.             \tag{3}
\]

The three `L_i` are pairwise disjoint.  The minimal-bad-contraction
theorem
[`hc7_three_split_minimal_bad_contraction.md`](hc7_three_split_minimal_bad_contraction.md)
gives all of the following.

1. `H` is six-connected and `K_7`-minor-free.
2. Every separator of `H` of order at most six has order exactly six and
   contains `z_1,z_2,z_3`.
3. For every `a`, the one-edge predecessor

   \[
                   H_a=G/(F-\{x_ay_a\})                          \tag{4}
   \]

   is seven-connected.

The last assertion is exactly inclusion-minimality: every proper subset
of `F` has a seven-connected quotient.  The matching required by the
predecessor decoders follows from the vertex-disjoint supports in (1).

Call a path **good** when its two ends lie in two different members of
`\{L_1,L_2,L_3\}`.  If `H` has seven pairwise vertex-disjoint good paths,
shorten them so their interiors avoid the three cliques and use their
vertex sets as seven branch bags.  Any two paths have a common endpoint
label among three labels; their distinct endpoint vertices in that
literal clique are adjacent.  Thus the seven bags form a `K_7` model in
`H`, and hence in `G`, a contradiction.  This is the literal path-packing
decoder proved in
[`hc7_decorated_three_model_hwege.md`](../active/hc7_decorated_three_model_hwege.md).

We may therefore take the Robertson--Seymour--Thomas/Mader obstruction
certificate, chosen with `|W|` maximum and then with the number of cells
maximum.  Put `w=|W|`.  Its budget gives `0\le w\le6`.  The marked cut
reduction
[`hc7_marked_three_clique_cut_reduction.md`](../active/hc7_marked_three_clique_cut_reduction.md)
defines three disjoint rows `B_i` and proves

\[
                 |B_i|\ge5-w,qquad
                 \sum_i|B_i|\le3(6-w).                           \tag{5}
\]

Call the row vector **balanced** when

\[
                         |B_1|=|B_2|=|B_3|=6-w.                  \tag{6}
\]

For `w<=5`, if (6) fails, integrality and (5) force some row to have order
`5-w`.  Thus “balanced” and “unbalanced” exhaust every certificate after
the separately treated `w=6` case.  We now list every value of `w` and its
audited discharge.

* **`w=6`.**  Lemma 3 of the marked cut reduction excludes the certificate:
  the marked six-cut is binary, whereas the order-zero/one cell gateways
  preserve at least three quotient components.
* **`w=0,1`, balanced.**  Section 3 of the marked cut reduction constructs
  seven literal branch sets and excludes (6).
* **`w=0,1`, unbalanced.**  The capacity-tight-cell theorem
  [`hc7_marked_three_clique_low_w_unbalanced_closure.md`](hc7_marked_three_clique_low_w_unbalanced_closure.md)
  excludes the deficient row.  Its symmetric-difference six-cuts force
  both outside marks into every tight cell, giving at most two large
  cells, fewer vertices than the three rows require.
* **`2\le w\le5`, unbalanced.**  The unbalanced-row collapse
  [`hc7_marked_three_clique_unbalanced_collapse.md`](hc7_marked_three_clique_unbalanced_collapse.md)
  proves (6), contradicting the assumption that the vector is unbalanced.
* **`w=2`, balanced.**  The audited literal decoder
  [`hc7_marked_three_clique_w2_closure.md`](../active/hc7_marked_three_clique_w2_closure.md)
  constructs a `K_7` model in `H`.
* **`w=3`, balanced.**  The audited predecessor decoder
  [`hc7_marked_three_clique_w3_predecessor_closure.md`](hc7_marked_three_clique_w3_predecessor_closure.md)
  splits one mark in a graph `H_a` from (4) and constructs a literal
  `K_7` model there.
* **`w=4,5`, balanced.**  The audited uniform one-split decoder
  [`hc7_marked_three_clique_w45_predecessor_closure.md`](hc7_marked_three_clique_w45_predecessor_closure.md)
  likewise constructs a literal `K_7` model in one of the seven-connected
  predecessors (4).

This covers all integers `0\le w\le6` and both possible row-vector types.
Every branch contradicts `K_7`-minor-freeness of `G`.  Therefore a
minimal bad contraction set cannot have order three.  \(\square\)

## Trust boundary

The theorem closes the size-three branch only.  In the larger support-six
programme, an inclusion-minimal bad set may still have order one or two.
The order-one branch is an exact-seven handoff; the unresolved composition
obligation is the order-two branch.  Nothing here proves that every
hypothetical `HC_7` counterexample supplies the three initial models in
(1), nor does it prove `HC_7`.
