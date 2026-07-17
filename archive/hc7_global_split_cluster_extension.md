# Extending the Niu--Zhang cluster theorem to split `K_5` models

## Status

This note identifies the exact first obstruction in the proof of
Niu--Zhang Theorem 4.1.  It proves the correct cluster-composition statement
when model branch bags are used injectively.  It does **not** prove the full
extension from literal `K_5` cliques to support-six `K_5` models.

The obstruction is not merely that an edge contraction may lower ordinary
connectivity.  Weighted connectivity and path packing demand incompatible
uses of the second vertex of a split bag.  A valid extension needs an
indivisible-bundle version of the `H`-Wege theorem, or a decoder for the at
most three split-bag collisions.

## 1. The published proof interface

Theorem 4.1 of Niu--Zhang, *Cliques, minors and apex graphs*, proves a
cluster-traversing strengthening of their three-clique theorem.  Two steps
are decisive here.

1. In their step 4.6, `k+2` mutually disjoint good paths form a
   `(k+2)`-cluster.  Any two paths have ends in two pairs chosen from three
   cliques, so the pairs share a clique; the corresponding two literal
   endpoints are adjacent in that clique.
2. Having forbidden those paths, step 4.7 applies the Robertson--Seymour--
   Thomas form of Mader's `H`-Wege theorem and derives the partition
   `(W;Y_j,X_j)` used for every later count.

For split models, step 4.6 is false with the unmodified definition of a
good path.  Strengthening “good” to remember branch-bag ownership repairs
4.6, but then the ordinary `H`-Wege theorem no longer gives 4.7.  This is
the first break even when the three model supports are disjoint; overlap
and the induction in step 4.2 create additional issues later.

## 2. The exact positive replacement for step 4.6

Let `M_1,M_2,M_3` be vertex-disjoint `K_5` models in a graph `G`.  A
**model-good path** has one end in the support of `M_i`, the other in the
support of `M_j` for distinct `i,j`, and no internal vertex in any model
support.  A family of model-good paths is **bag-injective** if, at each
model, no two path ends belong to the same branch bag.

### Proposition 2.1 (bag-injective cluster composition)

Seven mutually vertex-disjoint, bag-injective model-good paths form, after
enlargement inside their endpoint branch bags, a `7`-cluster.  In
particular `G` contains a `K_7` minor.

#### Proof

Enlarge each path by the one branch bag containing each of its ends.  The
enlarged fragments remain disjoint: the three models are vertex-disjoint,
and bag-injectivity assigns every branch bag to at most one path.  They are
connected.

Take two paths.  Their two model-index pairs are two-element subsets of
`{1,2,3}`, so they share some index `i`.  At `M_i` their ends occupy
distinct branch bags.  Those bags are adjacent by the definition of a
`K_5` model, and hence the two enlarged path fragments are adjacent.
Thus all seven fragments are mutually adjacent.  \(\square\)

This proposition works for arbitrary branch-bag sizes.  At support six,
the only possible failure of bag-injectivity is especially small: both
vertices of the unique split edge are used by different paths.

## 3. The atomic split-bag collision

Write one support-six model as a singleton clique

\[
                         Q=\{a,b,c,d\}
\]

and a split edge `xy`, with

\[
 D_x=\{q\in Q:xq\notin E(G)\},\qquad
 D_y=\{q\in Q:yq\notin E(G)\}.
\]

The sets `D_x,D_y` are nonempty and disjoint.  Suppose two good paths use
`x` and `y` separately.  A third path ending at `q in D_x` is not forced
to be adjacent to the `x`-path, even though their model-index pairs share
this model.  If those two paths share no other model index, the literal
clique argument of Niu--Zhang 4.6 has no replacement.

This failure occurs in an explicit eighteen-vertex local shell.  Take
three disjoint copies `M_i` of the displayed model, with

\[
 D_{x_i}=\{a_i\},\qquad D_{y_i}=\{b_i\},
\]

and add the seven mutually disjoint connector edges

\[
\begin{array}{lll}
x_1x_2,&y_1y_2,&b_1a_2,\\
a_1x_3,&c_1y_3,&b_2a_3,&c_2b_3.
\end{array}
\]

They are seven disjoint good paths of type multiplicities `(3,2,2)`.  But
the path `x_1x_2` is not adjacent to the path `a_1x_3`: the only shared
model is `M_1`, where `x_1a_1` is the defining missing contact, and no
other cross-edge was added.  Thus the displayed path family is not a
cluster.  This is a counterexample to the naive replacement of “clique” by
“model” in step 4.6, not a counterexample to a full highly connected
three-model theorem.

## 4. Why weighted connectivity does not automatically fix the proof

For three contraction-clean support-six models, contract their split edges
to `z_1,z_2,z_3`.  Give each `z_i` weight two and every other vertex weight
one.  Seven-connectivity of the original graph gives

\[
                 \sum_{v\in T}w(v)\ge7                 \tag{4.1}
\]

for every separator `T` of the quotient.  This is the anchored-separator
law proved in
[`../results/hc7_global_split_model_composition.md`](../results/hc7_global_split_model_composition.md).

The quotient now has three literal `K_5` cliques, so the ordinary step 4.6
works if paths use each `z_i` at most once: expand the unique path using
`z_i` by the whole split edge.  But ordinary `H`-Wege charges `z_i` only
one unit in its obstruction, and (4.1) cannot eliminate that obstruction.

If instead a capacitated/weighted `H`-Wege theorem charges `z_i` two units,
the primal packing naturally permits two paths to use its two units.  On
lifting, those paths use `x_i` and `y_i` separately and create exactly the
collision in Section 3.  Thus the two desired properties are incompatible
under the standard packing/covering duality:

\[
\begin{array}{c|c|c}
 &\text{path capacity at }z_i&\text{separator charge at }z_i\\ \hline
\text{safe whole-bag lift}&1&1\\
\text{lifted connectivity}&2&2.
\end{array}
\]

What is needed is an **indivisible bundle** rule: the two units of a split
bag may be reserved by one path and expanded together, but may not be used
by two unrelated paths unless a defect-compatible collision decoder is
also returned.  Mader's theorem in the form used by Niu--Zhang has no such
constraint.

Even a formal weighted rewrite of their later counts is not automatic.
For example, step 4.10 moves one vertex from an even `X_j` into `W` without
changing

\[
                     |W|+\sum_j\left\lfloor|X_j|/2\right\rfloor.
\]

Moving a weight-two contraction image changes the analogous weighted
quantity differently, so the odd-cell normalization already fails.

## 5. The overlap threshold

The proposed “nonclose” bounds—intersection at most three for two literal
support-five models and at most four when a support-six model is involved—
do not by themselves reduce to Niu--Zhang's intersection-at-most-three
hypothesis.

After a clean split contraction, a support intersection of four can remain
an intersection of four between the resulting literal `K_5` cliques.  The
important example is two split models with the same singleton `K_4` core.
Three models all sharing that core and having disjoint split edges are
already closed by the common-core composition theorem in the adjacent
result note.  A lone intersection-four pair, however, is not eliminated by
the published theorem or by that three-root lemma.

Thus a complete generalized cluster theorem needs two new clauses, not one:

1. an indivisible-bundle `H`-Wege theorem (or a decoder for at most three
   split-bag collisions); and
2. a composition rule for the residual intersection-four overlap patterns.

The first is present even for three disjoint supports and is therefore the
minimal obstruction.  It should be attacked before any taxonomy of the
overlap-four cases.

## 6. The next falsifiable theorem target

The preceding analysis isolates a narrower target than a wholesale weighted
rewrite of the Niu--Zhang proof.

### Indivisible three-bundle `H`-Wege target

Let `H` contain three pairwise disjoint literal `K_5` cliques
`L_1,L_2,L_3`, and let `z_i in L_i` be a private distinguished vertex of
weight two; every other vertex has weight one.  Assume every vertex
separator has total weight at least seven.  Replace each `z_i` conceptually
by one **indivisible two-vertex bundle**.  Then one seeks a theorem returning
one of the following.

1. Seven disjoint good paths between the three cliques, with every bundle
   assigned to at most one path.  These lift bag-injectively and Proposition
   2.1 gives a `K_7`.
2. A Robertson--Seymour--Thomas `H`-Wege obstruction whose lifted separator
   has ordinary order at most six in the expanded graph.
3. A path system with at most three double-used bundles, together with a
   defect-compatible decoder that either repairs every collision or returns
   an actual seven-separation carrying the model labels.

The first two outcomes are the clean packing/covering alternatives.  The
third makes explicit the extra information that an honest theorem may need;
silently counting a double-used bundle as two ordinary paths is invalid.

This target is local and falsifiable.  It concerns only three private
two-vertex bundles and the `k=5` cluster interface.  A counterexample would
terminate the weighted Niu--Zhang route without affecting the common-core
composition theorem.  A proof would replace the exact missing implication
between steps 4.6 and 4.7 and would justify resuming the later cluster
analysis.

### Research verdict

Do not enumerate intersection-four overlap patterns yet.  First prove or
falsify the indivisible three-bundle target.  If it is false, the smallest
counterexample should be classified by the number and defect orientation of
the double-used bundles; only a decoder that eliminates an infinite collision
family would warrant promotion into the proof spine.
