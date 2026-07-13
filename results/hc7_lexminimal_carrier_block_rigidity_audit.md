# Audit of lex-minimal carrier block rigidity

## Verdict

**GREEN, under the comparison hypotheses stated in the two active notes.**

This audit covers:

* Lemma 1, Theorem 2, and Corollaries 3--6 of
  `results/hc7_lexminimal_carrier_block_rigidity.md`;
* the matching normalization formerly stated as Theorem 1.6 and
  Corollary 1.7 of `active/hc7_three_anchor_capacity_web.md`.

It does **not** audit the later certified-interface assumptions `(C1)--(C2)`.

## 1. Permitted model moves

For a noncutvertex `x` of a nonsingleton carrier `R`, `R-x` is nonempty
and connected.

* If `x` owns no duty, deleting it from the displayed bag preserves every
  required `R-Q_i` adjacency: for each nonempty duty, failure of ownership
  by `x` supplies an edge whose `R`-end is different from `x`.
* If `x` owns exactly duty `i`, moving `x` into `Q_i` is legal.  The old
  `x-Q_i` edge connects the enlarged `Q_i`; connectedness of `R` supplies
  an `x-(R-x)` edge, which restores the `R-Q_i` adjacency; and every other
  row duty has an edge ending in `R-x`.  Enlarging `Q_i` cannot destroy a
  labelled adjacency not incident with `R`.

Thus every noncutvertex owns at least two duties.  Two distinct vertices
cannot own the same nonempty duty, so at most three noncutvertices exist
when there are six exhaustive row duties.

The word **exhaustive** matters: in the application, the `Q_i` are all six
other bags of the seven-bag `K_3 join C_4` carrier.  The conclusion would
not follow if an unlisted required adjacency incident with `R` were
allowed.

## 2. Block-cutvertex argument

The injection used for a block `B` is valid.  A cutvertex `b` of `G[R]`
lying in `B` has, on the `b` side of `T_H-B`, a leaf block distinct from
`B`; that leaf block contains a global noncutvertex.  Distinct vertices
`b` give disjoint branches, while noncutvertices already in `B` map to
themselves.  Consequently `|B|` is at most the total number of global
noncutvertices, hence at most three.  In a finite simple connected graph
with at least two vertices, its blocks are therefore bridges or triangles.

Two triangle blocks would contribute four distinct global noncutvertices:
at each end of the unique block-tree path, the two triangle vertices not
used toward the other triangle either are themselves noncutvertices or
lead into distinct off-path leaf branches.  Hence at most one triangle
exists.

Leaf blocks inject into global noncutvertices, so there are at most three
leaves in the block-cutvertex tree.  Its maximum degree is therefore at
most three.  With two global noncutvertices all blocks are bridges and the
carrier is a path.  With three, either it is a subdivided claw or its sole
triangle has at most three edge-path branches.  The path/claw
classification and the assertion that deleting a cutvertex leaves at
most three components are consequently valid.

## 3. Exact owner cells

In the three-noncutvertex case, three pairwise disjoint owner sets of size
at least two exhaust the six duties.  Each is therefore a two-set, and all
literal row contacts occur at the corresponding three roots.  In the
two-noncutvertex case at least four duties are concentrated at the two
path endpoints, leaving at most two mobile duty classes.  These are exact
counting consequences; no palette-to-label inference is used.

## 4. Corollary 1.7 / result Corollary 5

The revised absorption argument is valid under its explicit closure
hypothesis.

Let an unused component `C` meet a foreign bag `Q_i`, and absorb `C` into
that bag.  The operation preserves connectivity and `|R|`, loses no
labelled adjacency, and can only improve the primary defect measure.  If
the measure improves, primary minimality is contradicted.  Otherwise the
new model is equally optimal and the ownership lemma applies again.

If `C` had a neighbour in `R-Z`, the root which formerly owned duty `i`
would lose that duty while retaining exactly its other paired duty; none
of the other five original portal sets changes.  That unchanged
noncutvertex would then own exactly one duty, contradicting the ownership
lemma.  Hence every component absorbed in this way has all of its
`R`-neighbours in `Z` (in fact the same argument gives the stronger
restriction that they cannot meet a wrong root of `Z`, though this is not
needed).

After all such absorptions, every still-unused component meets model bags
only in `R`.  All edges from `R-Z` to a foreign bag are also absent by the
three-owner conclusion.  Therefore any component of the remaining
envelope after deleting `Z` has neighbourhood contained in the
three-vertex set `Z`, while the six foreign bags remain on the other side.
Seven-connectivity forces the envelope to equal `Z`.  Thus `R=Z`; a
connected three-vertex graph in which all three vertices are
noncutvertices is `K_3`.

## 5. Result Corollary 6

Corollary 6 is also **GREEN**, with `M` and `P` understood to be computed
in the final model after all non-improving absorptions.

Each absorption either improves the primary defect measure, immediately
contradicting its minimality, or leaves an equally optimal model to which
Lemma 1 applies again.  Since the row graph is unchanged, its only
noncutvertices remain the path endpoints.  They therefore still own at
least two duties each, with disjoint owner sets, so at most two duties
belong to `M`.

Put `S=P union {a,b}` and let `E` consist of `R` and the components still
unused.  In the final model, every edge from `R-S` to a foreign bag is
excluded by the definition of endpoint-owned duties and `P`.  A component
still unused meets no foreign bag, and distinct unused components are
anticomplete.  Hence every component of `G[E-S]` has neighbourhood
contained in the literal vertex set `S`.  If `G[E-S]` is nonempty and
`|S|<=6`, this is an actual cut contradicting seven-connectivity; otherwise
either `E subseteq S` or `|S|>=7`, exactly as claimed.

When `|R|>=7`, both alternatives force `|S|>=7` because `R subseteq E`.
Thus at least five vertices of `S` differ from the two endpoints.  They lie
in `P`, are internal path vertices, and are distributed over at most two
mobile duties; one duty consequently has at least three distinct internal
portals.  This also covers the apparent `M=0` case: it is impossible when
`|R|>=7`.

## 6. Trust boundary

The green verdict is conditional on:

1. lexicographic minimality over a comparison class permitting the stated
   deletion, transfer, and absorption operations;
2. all six required adjacencies incident with the common row being the
   listed duties; and
3. the six foreign bags being nonempty and disjoint from the row and all
   unused components.

The result proves literal carrier geometry only.  It does not by itself
turn the remaining path portals into compatible colour states, a global
adhesion, or the two diagonal packets needed to repair `K_3 join C_4`.
