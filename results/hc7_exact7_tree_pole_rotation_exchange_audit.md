# Independent audit: tree-pole rotation exchange

Audited file: `results/hc7_exact7_tree_pole_rotation_exchange.md`.

## Verdict

* **Theorem 2.1 — GREEN.**  The circular-split condition is necessary and
  sufficient, and a noninterval edge split really yields two
  vertex-disjoint base paths.  This remains true when several occurrences
  have one base and when one or both returned paths have length zero.
* **Corollary 3.1 — GREEN** as a connector statement.  An edge-minimal
  connected subgraph spanning the attachment bases is a tree, and the two
  alternatives lift literally to the pole graph.
* **Section 4 — GREEN only as the stated local connector output.**  It
  must be fed the full multiset of original attachment occurrences, not a
  parallel-suppressed quotient, and it does not embed the unused vertices
  or edges of the whole induced pole.

One wording clarification should accompany promotion.  A disk realization
must mean

\[
              \widehat T\cap\partial D
              =\{\ell_\omega:\omega\in\Omega\},
\]

with the occurrence leaves in the prescribed cyclic order and every other
point of the drawing in the disk interior.  This is the standard society
meaning and is what the Jordan-arc proof uses.  The phrase “only prescribed
boundary points” is slightly weaker if read literally, but no theorem
repair is needed under the standard interpretation.

There is also a harmless empty-list edge case: if `m=0`, the “minimal
subtree spanning the occurrence leaves” used in the proof is undefined.
Either assume `m>=1` (the HC7 application has many occurrences) or dispose
of `m=0` separately by drawing the tree in the disk interior.  This does
not affect the dichotomy.

## 1. Necessity of every circular edge split

Fix `e in E(T)` and let its two components be `T_1,T_2`.  If the
occurrences based in `T_1` are not a circular interval, there are four
distinct occurrences in cyclic order `a,b,c,d` with `a,c` based in
`T_1` and `b,d` based in `T_2`.

In `widehat T`, the unique leaf-to-leaf `a-c` path consists of the two
occurrence-leaf edges and the unique base path inside `T_1`.  The analogous
`b-d` path lies wholly in `T_2` apart from its occurrence leaves.  The two
paths are therefore vertex-disjoint.  In a disk realization they would be
two disjoint arcs joining alternating boundary points, impossible by the
Jordan curve theorem.  Hence both parts of every edge split are circular
intervals; on a circle, one part is an interval exactly when its complement
is.

Repeated bases cause no gap.  If `b(a)=b(c)`, the internal base path is the
single vertex `b(a)`, still contained in `T_1`.  The other base path lies
in the disjoint vertex set `V(T_2)`.  Thus the two returned carriers remain
vertex-disjoint.

## 2. Sufficiency and the induction

Pruning vertices outside the minimal subtree spanning the occurrence
leaves does not change the realization question.  Suppressing an
unlabelled degree-two vertex replaces a path by one edge; the new edge
induces the same occurrence split as every edge on that path.  Thus the
circular-split hypothesis is preserved in both directions.

After these reductions, either there is at most one internal vertex, in
which case the tree is a star and its occurrence leaves can be placed
radially in any prescribed order, or a deepest internal vertex `u` has
exactly one neighbour toward the internal root and all other neighbours
are occurrence leaves.  Let `B` be those leaves.  The parent edge separates
exactly `B`, so `B` is one circular interval.

Collapsing that pendant star to one temporary occurrence preserves every
remaining edge split.  Indeed, for an edge outside the collapsed star,
all of `B` lies on one side; replacing the consecutive block `B` by one
point preserves circularity.  Induction embeds the smaller tree.  A small
boundary neighbourhood of the temporary leaf then accommodates `u` and a
radial fan to the leaves of `B` in their original consecutive order.  This
is a valid disk realization of the original occurrence tree.

This proves the equivalence.  If a split fails, choosing two occurrences
of one part separated on both sides by occurrences of the other gives the
alternating quadruple.  The two unique base paths lie in the two distinct
components of `T-e`, so the final disjointness assertion is immediate and
does not require a separate linkage theorem.

## 3. Explicit small falsification checks

### Repeated bases on a single edge

Let `T=uv`, base `a,c` at `u`, and base `b,d` at `v`, in cyclic order
`a,b,c,d`.  The unique edge split is noninterval.  The returned carriers
are the one-vertex paths `{u}` and `{v}`, which are disjoint.  A disk
realization would contain disjoint `a-c` and `b-d` arcs with alternating
ends, so none exists.  This confirms rather than refutes the zero-length
case.

### Star and repeated central bases

For a star, every peripheral edge separates the occurrences based in one
pendant branch.  A prescribed cyclic order is realizable exactly when each
such branch block is consecutive.  Occurrences based at the centre may be
inserted between these blocks in any order by choosing their leaf-edge
rotations at the centre.  Thus repeated central bases create no missing
local-rotation constraint.

### A subdivided `Y`

After suppressing degree-two unlabelled vertices, each arm block of a `Y`
must be consecutive.  Collapsing one pendant arm and expanding it in a
boundary neighbourhood reproduces precisely the source induction.  No
pair of paths from opposite split classes can meet at the branch vertex,
because the branch vertex belongs to only one component of the selected
deleted edge.

No tree, star, or repeated-base counterexample survives the edge-split
criterion.

## 4. Corollary 3.1 and its scope

An edge-minimal connected subgraph `T` of `X` containing all attachment
bases cannot contain a cycle: deleting any cycle edge would preserve
connectivity and all bases.  Hence `T` is a tree.  A disk realization of
its occurrence expansion is exactly the repaired local substitution in a
fixed disk around the quotient pole.  In the other outcome, its two base
paths are vertex-disjoint connected subgraphs of `T`, and therefore of
`X`, with the four literal edge occurrences alternating in the supplied
rotation.

The occurrence list must retain multiplicity.  If several original pole
edges contract to parallel quotient edges, each edge end is a separate
`omega`; suppressing them before applying the theorem loses constraints.
Conversely, extra host edges and vertices of `X` may be ignored only
because the corollary claims expansion of the selected connector `T`, not
planarity of the entire induced pole.  The source states this limitation
correctly.

The “unique block-terminal rib rotation” in Section 4 should be read as
the fixed rotation of the selected rib embedding.  Canonicity across other
web completions is unnecessary for Theorem 2.1 and is not proved here.
