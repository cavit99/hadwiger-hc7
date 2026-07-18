# Barrier to a curvature-only completion of the degree-eight equality case

**Status:** barrier to an intermediate claim.  The first construction is an
unbounded family of triangulated discs with prescribed contacts to three
additional vertices.  The second construction is a finite graph proving that
even a connected subgraph meeting all eight neighbours of one equality
vertex does not, by itself, force a `K_7` minor.  Neither construction is
claimed to be a hypothetical counterexample to `HC_7`.

## 1. The intermediate principle being tested

In the alternating four-root disc from
[the two-pair disc analysis](../results/hc7_two_pair_disk_structure.md),
Euler curvature produces an interior vertex of completed degree five.  In
the saturated equality case, such a vertex `v` has five neighbours in the
disc and is adjacent to all three omitted boundary vertices.

The complete five-ring lemma closes the case in which

1. the five disc neighbours of `v` induce a literal `5`-cycle; and
2. each of the three omitted boundary vertices is adjacent to every vertex
   of that cycle.

A tempting strengthening is to assign every failure of these two conditions
to a facial or contact defect and use Hall's theorem together with Euler
curvature to force a vertex with no defect.  The family below shows that the
displayed incidence data do not support such an argument.  All positive
curvature can occur at mutually distant degree-eight vertices, while the
same omitted boundary vertex misses every surrounding five-ring.

## 2. An unbounded triangulated-disc family

Fix an integer `n>=5`.  Start with an icosahedron.  Subdivide each of its
twenty triangular faces into the triangular grid of frequency `n`: each old
edge becomes a path of `n` edges, and each old face becomes `n^2` triangular
faces.  Identify equal subdivisions on the two sides of every old edge.
Call the resulting triangulated sphere `S_n`.

This construction has the following elementary properties.

- It has `20n^2` triangular faces, `30n^2` edges, and hence
  `10n^2+2` vertices.
- The twelve old icosahedral vertices have degree five.
- Every new vertex has degree six.
- The five neighbours of each old vertex induce a literal `5`-cycle.
- For `n>=5`, the closed radius-one neighbourhoods of the twelve old
  vertices are pairwise disjoint.  Indeed, the five neighbours of an old
  vertex are the first subdivision vertices on its five incident old edges;
  when `n>=5`, none is an old vertex or a first subdivision vertex belonging
  to another old endpoint.

To obtain an outer face of order four without touching one of these
five-rings, work in one old face and use barycentric coordinates whose
entries sum to `n`.  The two grid vertices

\[
 x=(2,1,n-3),\qquad y=(1,2,n-3)
\]

are adjacent.  Their two common neighbours are

\[
 a=(2,2,n-4),\qquad d=(1,1,n-2).
\]

Delete the edge `xy` and take the merged face

\[
                         x a y d x
\]

as the outer face.  Denote this triangulated `4`-disc by `D_n`.  All twelve
old vertices are interior vertices of `D_n`; they are precisely its interior
vertices of degree five.  Every other interior vertex has degree six.  The
five-ring around every old vertex is unchanged and literal.

Introduce three further vertices

\[
                         B=\{p,q,s\}.
\]

Join `p` and `q` to every vertex of `D_n`, and join `s` exactly to the twelve
old degree-five vertices.  Planarity is asserted only for `D_n`, not for the
graph after these contacts are added.

Every positive-curvature interior vertex `v` now has total degree

\[
                         5+3=8,
\]

is adjacent to all three members of `B`, and has a literal five-ring.  Each
vertex on that ring is a new degree-six vertex, so it is adjacent to `p` and
`q` but not to `s`.  Thus every equality vertex fails the complete
five-ring hypothesis in the same contact row.

Every other interior vertex has total degree `6+2=8`.  In particular, the
curvature calculation produces no degree-seven interior vertex in this
family.

The failure also has no Hall concentration.  If `P` is the set of the
twelve degree-five vertices and

\[
 W(v)=N_{D_n}(v)\qquad(v\in P),
\]

then every member of `W(v)` misses `s`, and

\[
 |W(v)|=5,\qquad W(v)\cap W(w)=\varnothing
                         \quad(v\ne w).
\]

Consequently, for every `X subseteq P`,

\[
              \left|\bigcup_{v\in X}W(v)\right|=5|X|.
\]

The natural Hall system therefore has maximum slack rather than a deficient
set.  Increasing `n` makes the twelve equality configurations arbitrarily
far apart in the disc metric of `D_n`, while preserving all of the stated
degree and contact data.  In the augmented graph they are, of course, at
distance two through `p` or `q`.

## 3. Full exterior contact still does not give a local `K_7` model

The preceding family shows that curvature and contact counting cannot force
a complete five-ring.  The following ten-vertex graph shows a second,
independent limitation: representing an exterior component by one vertex
adjacent to all eight neighbours of `v` still does not close the concentrated
missing-contact pattern.

Let

\[
 C=c_0c_1c_2c_3c_4c_0,
 \qquad B=\{p,q,s\},
\]

and add two nonadjacent vertices `v,d`.  Add precisely the following edges:

1. the five edges of `C`;
2. every edge from each of `v,d` to `B union V(C)`; and
3. every edge from each of `p,q` to `V(C)`.

There are no other edges.  In particular, `B` is independent and `s` has
neighbourhood `\{v,d\}`.  The vertex `v` has the saturated degree-eight
neighbourhood `B union V(C)`, and `d` meets every one of those eight
neighbours.

### Proposition 3.1

This ten-vertex graph has no `K_7` minor.

### Proof

First suppose that a proposed `K_7` model does not use `s`.  It then uses at
most nine vertices.  Seven nonempty branch sets on at most nine vertices
include at least five singleton branch sets.  Those five singleton vertices
would induce a `K_5` subgraph.  However, after deleting `s` the graph is

\[
                         K_{2,2}\vee C_5,
\]

where the two parts of the `K_{2,2}` are `\{v,d\}` and `\{p,q\}`.  Its
clique number is `2+2=4`, a contradiction.

Now suppose that the model uses `s`, and let `Z` be its branch set containing
`s`.  If `Z=\{s\}`, it can be adjacent to at most the two branch sets
containing `v` and `d`, rather than to the six other branch sets.  If `Z` is
larger, connectivity of `Z` forces it to contain `v` or `d`; assume by
symmetry that it contains `v`.

After deleting `Z`, the other six branch sets lie in a subgraph of

\[
                  d\vee\bigl(C_5\vee\overline{K_2}\bigr),
\]

where the two vertices of `\overline{K_2}` are `p,q`.  The graph
`C_5\vee\overline{K_2}` is the planar pentagonal bipyramid: draw `C_5` as
the equator and its two nonadjacent universal vertices on opposite sides.
It therefore has no `K_5` minor.  If adjoining the universal vertex `d`
produced a `K_6` model which used `d`, deleting the branch set containing
`d` would leave a `K_5` model in the pentagonal bipyramid.  If the model did
not use `d`, deleting any one of its six branch sets would again leave such
a `K_5` model.  Both alternatives are impossible.  Hence the six remaining
branch sets cannot exist, completing the proof.  \(\square\)

## 4. Exact trust boundary

The disc family is not asserted to extend to a graph which is simultaneously

- seven-connected;
- seven-chromatic and contraction-critical;
- `K_7`-minor-free; and
- equipped with the five named connected subgraphs on the opposite shore.

The ten-vertex graph is a local minor obstruction, not such a host.  These
examples therefore do not refute a theorem which genuinely uses
contraction-critical colourings, the named opposite-shore model, or global
`K_7`-minor exclusion.

They do refute the following proof strategy: use only Euler curvature, the
three contacts at every degree-five equality vertex, the literal status of
the five-ring edges, and Hall counting on missing boundary contacts.  The
zero-curvature degree-six vertices can absorb one common missing label at
no curvature cost, with arbitrarily dispersed witnesses; and even one
fully contacting exterior component does not repair that pattern locally.

The next positive statement must therefore be a label-diversification
theorem using the missing host hypotheses.  A suitable target is:

> In the actual contraction-critical two-pair separation, either some
> degree-eight equality vertex has sufficiently diverse five-ring contacts
> to construct an explicit `K_7`-minor model, or concentration of all
> missing contacts at one omitted boundary vertex produces an order-seven
> separation with compatible shore colourings.

That target is not proved here.
