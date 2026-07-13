# Independent adversarial audit: rural torso-tree apex gluing

## Overall verdict after the stated repairs: **GREEN**

The planar induction in Theorem 1 and the fixed-two-vertex conclusion in the
main sentence of Theorem 2 are correct, provided condition 5 is read in its
strong intended sense: every torso has one **simultaneous** system of
pairwise interior-disjoint port disks for all of its incident adhesion
occurrences.

There was one real wording defect.  The sentence claiming the same conclusion
for “fewer than two such fixed vertices, after padding arbitrarily” is false
for a zero-vertex common set unless there are no overfull triangles.  The
clean correct hypothesis is stronger and more general; the theorem file now
uses it:

> there is a fixed set `S` of at most two actual vertices which meets every
> overfull adhesion triangle.

Then `H-S` is planar, and `S` may be padded to two vertices.  For `S=empty`,
the hitting condition means that there are no overfull triangles.

The two barriers are valid for the claims they are meant to refute, although
Barrier A is a barrier to a locally-apex generalization rather than an
instance of the original all-planar-torso hypothesis.

## 1. Definition audit: **GREEN with simultaneous compatibility now explicit**

Condition 5 must mean the following literal statement.

For every torso `t`, in one fixed spherical embedding of `H_t`, choose for
every incident adhesion occurrence `s` a port disk `Delta_{t,s}`.  The disk
has the prescribed clique on its boundary (with the usual vertex/edge port
interpretation for orders one and two), its interior avoids `H_t`, and the
interiors of all `Delta_{t,s}` incident with `t` are pairwise disjoint.

Under that interpretation the definition is sufficient.  If condition 5
were interpreted only pairwise or separately for each adhesion, Theorem 1
would be false.  The sharp counterexample is:

* take three `K_4` torsos `C union {x_i}` on one common triangle
  `C={a,b,c}`;
* arrange their torso nodes in a path using two different degree-two
  adhesion nodes, both labelled by `C`.

No adhesion node is overfull.  Each copy of `C` is facial when considered
separately.  But the union is

\[
                       K_3\vee \overline{K_3},
\]

which contains `K_{3,3}` and is nonplanar.  The middle `K_4` exposes why the
strong condition 5 excludes this presentation: its one facial `C`-disk
cannot serve two distinct incidences with disjoint interiors.  Thus the word
“compatible” is doing essential mathematical work and should be formalized
as above.

The running-intersection clause should likewise be promoted from prose to an
explicit axiom: for every actual vertex, the torso nodes containing it form
a connected subtree of `T`.  This ensures that a child subtree meets the
already embedded part only in its current adhesion clique.

## 2. Theorem 1 (planar rural-tree gluing): **GREEN under the strong definition**

### Vertex adhesions

Arbitrarily many planar pages can be placed in disjoint angular sectors at a
common vertex.  Vertex sums preserve planarity.

### Repeated edge adhesions

Arbitrarily many planar pages sharing one facial edge also preserve
planarity.  Removing the shared edge from each page leaves a disk embedding
with the two adhesion vertices on its boundary; the pages can be ordered as
parallel `uv`-bridges and the literal edge drawn once.  There is no
two-sided-capacity obstruction analogous to the triangle case.

As a sharp sanity check, three `K_4` pages sharing one common edge form a
planar graph.  By contrast, three `K_4` pages sharing one common triangle
form `K_3 vee overline{K_3}` and are nonplanar.

### Triangle adhesions

If a triangle adhesion node has degree two, there is one parent page and one
child page.  Each exposes the triangle as a facial disk, so reflecting the
child places it on the unused side.  A degree-three triangle node is exactly
where three nontrivial pages could demand the two sides of one Jordan curve;
this is correctly excluded as overfull.

The possible hidden repetition of the same triangle through several
degree-two adhesion nodes is excluded by simultaneous disk compatibility,
as the counterexample above demonstrates.  With that exclusion and the
running-intersection axiom, rooting the incidence tree ensures each child is
inserted once and no orientation cycle remains.  The induction is valid.

## 3. Theorem 2 (fixed-pair two-apex gluing)

### Main statement: **GREEN**

If every overfull triangle contains the two distinct fixed vertices `p,q`,
then deleting them reduces each such adhesion to a singleton.  Any number of
pages can be glued at that vertex.  A non-overfull triangle still has degree
at most two, and deletion can only reduce its order.  All other adhesions have
order at most two and can be repeated without a planarity obstruction.
Theorem 1 therefore applies to the deleted presentation.

Deleting vertices from the specified torso embeddings does not create a new
port conflict: a former overfull triangle is now a vertex sum, while every
other port can be restricted or re-chosen in the merged faces.

### Exact strengthening and repair

Requiring every overfull triangle to contain **both** `p` and `q` is stronger
than necessary.  It is enough that the fixed set

\[
                            S\subseteq V(H),\qquad |S|\le2,
\]

meets every overfull triangle.  After deleting `S`, every former overfull
triangle has order at most two, and repeated edge/vertex sums are planar.
This proves `H-S` planar.

This formulation also repairs the padding sentence:

* if `S={p}`, delete `p` and pad the reported apex set arbitrarily;
* if `S=empty`, its being a hitting set says there are no overfull
  triangles, so Theorem 1 already gives planarity.

On the literal reading that an empty common set is merely “contained in”
every triangle, the current padding sentence is false.  Here is an explicit
infinite-family counterexample.  For each of five indices take the nonplanar
block

\[
 J_i=K_3\vee\overline{K_3},
\]

presented as three planar `K_4` pages around one overfull triangle `C_i`.
Join consecutive blocks at one articulation vertex outside their `C_i`, so
one vertex lies in at most two consecutive blocks.  The full incidence graph
is still a tree and all torso/port conditions can be satisfied.  The five
overfull triangles have no common vertex.  Every planarizing set must meet
each literal `J_i` (each contains `K_{3,3}`), while two vertices meet at most
four blocks.  Hence the union is not two-apex.  Arbitrarily padding an empty
“fixed set” cannot prove the conclusion.

### Corollary 2.1: **GREEN after the repaired formulation**

Width-one adhesions, repeated width-two adhesions, and non-overfull facial
triangles do not create holonomy.  A global two-vertex **hitting set** for all
overfull facial triangles gives a coherent named two-apex output.  The
stronger condition that the same pair lie in every overfull triangle is a
valid special case, but it should not be described as the exact capacity
condition.

## 4. Barrier A: **GREEN, with a scope clarification**

A chain of five literal `K_5` blocks meeting consecutively at articulation
vertices is not two-apex.  Every planarizing set must hit all five `K_5`
subgraphs, and any vertex hits at most two consecutive blocks; two vertices
hit at most four.

This example does **not** have a facial clique-tree presentation in the
definition of Section 1, because its `K_5` torsos are not planar.  It is
correctly a barrier to weakening the theorem to “each torso has its own
local apex choice.”  The text should make that distinction explicit.

The five-block construction above using overfull-triangle gadgets supplies
an analogous barrier entirely within planar torsos if one wants the barrier
phrased in the facial-presentation language.

## 5. Barrier B: **GREEN**

After suppressing the private subdivision vertices, the two boundary paths
contribute

\[
 12,23,34\qquad\hbox{and}\qquad 13,23,24.
\]

Their union is `K_4-14` with `23` doubled.  Its underlying simple graph has
the width-two tree decomposition with bags `{1,2,3}` and `{2,3,4}`.  Hence it
has no `K_4` minor; subdivision and the parallel edge do not change that.
The incompatible order-four boundary readings therefore do not alone force
a rooted `K_4` or even nonplanarity.

## Final trust boundary

After the definition and padding repairs, the theorem genuinely closes the
tree-composition problem for simultaneously port-labelled planar torsos with
adhesions of order at most three.  It does not establish that a rotation
decomposition actually has those simultaneous ports, does not create a
global two-vertex hitting set for overfull triangles, and says nothing about
an adhesion of order at least four.  Those are still the HC7 composition
edges.
