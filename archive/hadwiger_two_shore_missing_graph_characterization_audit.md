# Internal audit of the two-shore missing-graph characterization

## Verdict

**GREEN within its stated scope.**  The exact criterion is a direct
normal-form proof for clique-minor models in a nine-vertex graph.  The
nonrural survivor and the abstract state-polarity example are correct.
This is an internal audit, not independent peer review.

## 1. Exhaustiveness of the minor criterion

A seven-bag model on at most nine vertices has total excess at most two.
After deleting unused vertices its branch-size profile is necessarily

\[
 1^7,quad 2,1^6,quad 3,1^6,quad\text{or}\quad2,2,1^5.
\]

There is no omitted larger branch bag or mixed profile.  In each profile,
Theorem 1.1 translates exactly:

* singleton bags require an edgeless induced subgraph in the complement;
* a two-vertex bag is connected precisely when its internal complement
  edge is absent;
* a three-vertex bag is connected precisely when its complement contains
  at most one edge; and
* adjacency to a nonsingleton bag is precisely failure of complement
  completeness to that bag.

Thus all four certificates are both necessary and sufficient.

## 2. Split-state reduction

For a split partition `V(F)=P dotunion R`, the set `P` is independent in
the boundary graph and `R` is a clique there.  Full-shore contraction
makes `P` one exact block and the vertices of `R` distinct singleton
blocks on both closed sides.  The argument does not require original
`P`--`R` completeness.  If an initial split clique has order one and
`F` has an edge, moving one neighbour into that clique preserves an
independent remainder and gives `|P|>=2`.  Hence every split `F` is
indeed excluded in the minor-critical setting.

The cited Földes--Hammer equivalence then gives the induced
`2K_2/C_4/C_5` trichotomy exactly; it is not being used to claim that all
three outcomes are planar.

## 3. The nonrural survivor

For `F=2K_3 dotunion K_1`, direct complementation gives
`H(F)=K_1 vee K_{2,3,3}`.  If a hypothetical `K_7` model uses the
universal root, removing its branch leaves a `K_6` model in
`K_{2,3,3}`; if it avoids the root, discard any one of its seven bags.
Such a
model has at most three singleton branch bags, one per multipartition
class, and consequently needs at least nine vertices; only eight exist.

The two-apex check is also exhaustive.  After deleting the universal
vertex and one other vertex, a `K_{3,3}` remains.  If the universal vertex
survives two deletions, the base contains `K_{2,3}` and hence is not
outerplanar; a planar cone would require an outerplanar base.  Therefore
no two-vertex deletion makes the graph planar.

The selected `Q` takes one vertex from each triangle plus the isolated
vertex, so it is independent in `F`; the remaining two pairs are literal
edges of `F`.  The survivor has exactly the required triangle-plus-two-
gate labels.

## 4. Private-state limitation

The two displayed abstract families really are disjoint and each contains
a witness for every nonempty exact block lying in either triangle.  All
their partitions use at most six boundary blocks.  The note correctly
does not claim these two families are realized by minor-critical
boundaried graphs; they establish only logical insufficiency of private-
block incidence constraints.
