# Independent audit: rainbow block and torso Helly cores

## Verdict

**GREEN AS PATCHED.**  Projection of inclusion-minimal rainbow connected
subgraphs to either the block--cut tree or an arbitrary decomposition tree
is valid.  Pairwise intersection becomes a pairwise-intersecting family of
subtrees, so tree Helly gives one common block/bag.  The isolated
one-vertex block case and one decomposition-tree wording point were
patched.  No claim that virtual edges are literal, or that arbitrary
portal marks are rainbow-forcing, is needed for the proved conclusions.

## 1. Minimal rainbows and extension

In a finite connected carrier, every rainbow connected subgraph contains
an inclusion-minimal one.  Portal-indecomposability is exactly the absence
of two vertex-disjoint minimal rainbows: two disjoint connected witnesses
can be contracted, joined in a spanning tree, and extended by deleting an
edge of the path between them to a connected adjacent rainbow
bipartition.  Conversely, either side of such a bipartition is a disjoint
rainbow witness.

## 2. Block--cut projection

The block--cut trace of a connected subgraph is a subtree.  If two
rainbows share a cutvertex, both traces contain its cut node; if they
share a non-cutvertex, both contain that vertex's unique block node.
Thus actual pairwise intersection implies trace intersection, which is
the only direction used.

A common cut node gives a literal universal vertex.  A common block node
means every rainbow meets that block.  For a bridge block `uv`, a rainbow
whose endpoint trace is `{u}` lies entirely on the `u` side and one whose
trace is `{v}` lies entirely on the `v` side; such two rainbows would be
disjoint.  Hence the nonempty endpoint traces have a common endpoint,
again giving a universal vertex.  The omitted isolated-block edge case
has now been patched: its sole vertex is universal.  If neither gate case
occurs, the common block has order at least three and is 2-connected.

Every component outside a maximal 2-connected block has exactly one
neighbour in it.  Two distinct attachments would add an external ear to
the block and produce a larger 2-connected subgraph.  Such a component
is portal-dark because it is a connected subgraph disjoint from the
block that meets every rainbow.

## 3. Arbitrary tree decompositions

For a connected subgraph `K`, the union of the bag-subtrees of its
vertices is connected: subtrees for the ends of each edge meet in a bag,
and the edges of `K` connect the union.  Two intersecting rainbows have
intersecting traces through any bag containing a common vertex.  Helly
therefore produces a bag meeting every rainbow.

If `C` is a component outside the common bag `V_z`, every vertex of `C`
has its bag-subtree in one component of `T-z`; adjacency and
connectedness put all bags meeting `C` in the same component.  If `u` is
its neighbour of `z`, every neighbour of `C` in `V_z` belongs to
`V_z cap V_u`.  The adhesion bound therefore gives at most `k` such
neighbours.  The theorem statement and proof now express this precisely.

## 4. Tutte specialization and lift boundary

Combining block and SPQR/Tutte decompositions gives adhesion at most two.
Its relevant torso types are order-at-most-two gates, cycle torsos, and
3-connected torsos.  Hence every indecomposable carrier has one such bag
meeting every rainbow, and every omitted component is portal-dark with at
most two attachments to the bag.

Cycle and 3-connected torsos contain virtual edges.  A model using one
must be expanded through its named decomposition bridge; the source
correctly warns that it is not an original edge.  Similarly, the web
corollary is conditional on a tuple being rainbow-forcing and uses only
same-vertex web completion.  It does not infer label preservation from a
bare crossing.

## 5. Exact research consequence

The unbounded carrier residue is now confined to one torso.  What remains
unproved is a label-selection theorem inside that torso: either choose a
crossing/rooted model whose expansion yields two rainbow carriers, or
show that all cofacial orders are compatible with one rural/two-apex
state.  With two quotient carriers, their cross-edges still have to be
handled as one combined network; separate torso gates cannot be lifted
independently.
