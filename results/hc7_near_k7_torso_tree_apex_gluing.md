# Rural torso trees: planar gluing or one fixed two-apex pair

## Status and role

This is an **audited compatibility theorem** after the exact definition
and hitting-set repairs recorded in the accompanying audit.
It addresses the width-one/width-two/facial-triangle part of the remaining
rotation composition edge.  Such decompositions are trees, so compatible
rural pieces have no signed holonomy: child embeddings may be reflected
independently.

The only local capacity obstruction is a triangle used by at least three
pages.  If every overfull triangle contains one fixed pair of actual
vertices, deleting that pair reduces all overfull joins to vertex-sums and
gives one coherent two-apex structure.

The fixed pair is essential.  Different local apex pairs do not compose.
Likewise no analogous claim is made for an adhesion of order at least four.

## 1. Facial clique-tree presentations

A **facial clique-tree presentation** of a graph `H` consists of a
bipartite tree `T` with torso nodes `t` and adhesion nodes `s`, together
with subgraphs `H_t` and adhesion cliques `C_s`, such that:

1. `H` is the union of the `H_t` and has no edge outside a torso;
2. if torso nodes `t,u` have a common adhesion neighbour `s`, then
   `V(H_t) cap V(H_u)=C_s`; otherwise their intersection is forced only
   by the running-intersection property along `T`; explicitly, for every
   actual vertex `x`, the torso nodes containing `x` form a connected
   subtree of `T`;
3. `|C_s|<=3`;
4. each `H_t` has a specified plane embedding in which every incident
   adhesion clique is facial; and
5. for every torso `t`, one fixed spherical embedding of `H_t` admits a
   simultaneous choice of a port disk `Delta_{t,s}` for every incident
   adhesion occurrence `s`: the adhesion clique lies on its boundary,
   its interior avoids `H_t`, and all these port-disk interiors are
   pairwise disjoint.  For an adhesion of order one or two this is the
   usual vertex/edge-sum port.  For an adhesion triangle, the triangle
   bounds the disk used by that incidence.

An adhesion triangle is **overfull** when its adhesion node has degree at
least three, so at least three nontrivial torso pages use the same
triangle.

This is the literal structure returned by a tree of rural web expansions:
the virtual adhesion clique records where the child disk is inserted, and
condition 5 is the port-labelled condition which a contracted planar
quotient alone would not supply.

## Theorem 1 (planar rural-tree gluing)

If no adhesion triangle is overfull, then `H` is planar.

### Proof

Root `T` at any torso.  Embed that torso as specified.  Proceed away from
the root.  At an adhesion of order one, place each child component in a
small disk incident with the common vertex.  At an adhesion of order two,
reflect a child embedding if necessary and insert it as a parallel disk
between the two adhesion vertices; repeated vertex- and edge-sums of
planar graphs preserve planarity.

At a triangle adhesion of degree two there is exactly one torso piece on
each side of the adhesion node.  The triangle is facial in both specified
embeddings.  Reflect the child if necessary and put its disk on the side
of the triangle opposite the already embedded parent.  The compatibility
condition makes disks belonging to distinct child incidences disjoint.

Since the incidence graph is a tree, every child is inserted once and no
later choice can impose a cyclic orientation constraint.  Induction over
the torso nodes gives a plane embedding of their union. \(\square\)

## Theorem 2 (fixed hitting-set two-apex gluing)

Let `S` be one fixed set of at most two actual vertices which meets every
overfull adhesion triangle.  Then

\[
                              H-S\quad\text{is planar}.       \tag{2.1}
\]

If `|S|<2`, the reported apex set may be padded arbitrarily after the
planarity conclusion.  In particular, `S=emptyset` is allowed only when
there is no overfull adhesion triangle.

### Proof

Delete `S` from every torso and adhesion.  Each torso remains planar.
Every formerly overfull adhesion triangle now has order at most two, so an
arbitrary number of its incident pages can be joined as repeated edge- or
vertex-sums without destroying planarity.  A triangle disjoint from `S`
was not overfull by hypothesis; after deletion it still has at most two
nontrivial incident pages.  All remaining adhesions therefore satisfy the
capacity condition of Theorem 1 (and the simultaneous facial disks restrict
or merge compatibly).  Apply that theorem to the deleted presentation.
\(\square\)

### Corollary 2.1 (no width-two holonomy)

For a port-labelled SPQR/web decomposition, cutvertices, 2-vertex
adhesions, and non-overfull facial triangles cannot by themselves create
global rural-order holonomy.  They glue to one planar society.  If all
triangle capacity failures meet one fixed set of at most two actual
vertices, the whole society is planar after deleting that set.

Thus a target-free rotation chain which remains inside such a torso tree
has one of the two terminal geometric outputs required by the `HC_7`
spine: planar, or coherent two-apex with a named pair.

## 2. Why the hypotheses cannot be weakened

### Barrier A: local apex pairs do not compose

As a barrier to replacing the planar-torso hypothesis by separately chosen
local apex vertices, take a chain of five copies of `K_5`, with consecutive copies sharing one
articulation vertex and all other vertices distinct.  This has a
clique-tree presentation using adhesions of order one.  Each torso becomes
planar after deleting one locally chosen vertex.

Nevertheless the union is not two-apex.  Every planarizing set must meet
each of the five literal `K_5` subgraphs.  A vertex belongs to at most two
consecutive blocks, so two deleted vertices meet at most four blocks; one
intact `K_5` remains.  Hence Theorem 2 cannot permit a different apex pair
in every torso.  One fixed actual pair is indispensable.

These `K_5` blocks are not themselves planar torsos; the example tests only
that proposed local-apex weakening.  This barrier is low-connectivity, as
intended: in the `HC_7` application,
seven-connectivity and the literal row contacts must be used to force the
same pair or a `K_7`/state output.

### Barrier B: order-four mismatch alone is not a rooted `K_4`

Let the common boundary be `S={1,2,3,4}`.  On one side take a subdivided
path through the boundary in the order

\[
                              1,2,3,4,
\]

and on the other side an internally disjoint subdivided path through it in
the order

\[
                              1,3,2,4.
\]

Use distinct subdivision vertices on the two sides, so the closed sides
intersect exactly in `S`.  Both are rural tree societies, and their
boundary orders are not reversals.  After suppressing degree-two
subdivision vertices, their union is `K_4` minus the edge `14`, with the
edge `23` doubled.  It has a width-two tree decomposition and hence no
`K_4` minor, rooted or otherwise.

Therefore a cyclic-order mismatch at an adhesion of order at least four
does not, without additional 2-connectivity/full-contact hypotheses,
produce a rooted `K_4`, a `K_7`, or even nonplanarity.  The remaining
actual-adhesion theorem must use the near-model contacts or a proper-minor
boundary state; order data alone is insufficient.

## 3. Exact remaining transport edge

Together with fixed-connector rural holonomy, Theorems 1--2 leave only the
following changing-root obstruction.

* Some actual adhesion of order at least four carries incompatible rural
  societies which are not a facial clique-tree sum; or
* two overfull facial triangles demand different actual apex pairs.

To finish the `HC_7` spine, seven-connectivity and contraction-criticality
must turn either event into a literal private linkage/`K_7`, or force the
same equality partition from proper-minor operations on the two open
shores.  The barriers above show why neither conclusion follows from
abstract local planarity alone.
