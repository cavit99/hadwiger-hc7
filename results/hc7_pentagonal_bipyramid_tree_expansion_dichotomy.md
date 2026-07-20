# Tree expansions of the pentagonal bipyramid

**Status:** written proof; separately audited **GREEN** in
[`hc7_pentagonal_bipyramid_tree_expansion_dichotomy_audit.md`](hc7_pentagonal_bipyramid_tree_expansion_dichotomy_audit.md).

This note proves a label-preserving local-to-global theorem for a spanning
tree expansion of the pentagonal bipyramid.  It eliminates every such
expansion having one inter-tree edge for each quotient edge.  With repeated
inter-tree contacts, it isolates the only remaining obstruction as a
coupled portal-order problem in which an alternating cut reuses one of at
most three quotient labels.

The theorem is conditional on the columns being trees containing all their
induced internal edges.  The maximal columns in the live order-eight
argument are arbitrary connected subgraphs, so this note does not close
that argument or prove `HC_7`.

## 1. Setup

Let

\[
                       P=C_5\vee\overline {K_2}
\]

be the pentagonal bipyramid with its unique plane embedding.  For each
`x in V(P)`, let `T_x` be a tree.  Assume that a graph `F` has the disjoint
vertex partition

\[
                         V(F)=\bigsqcup_{x\in V(P)}V(T_x),       \tag{1.1}
\]

that `F[V(T_x)]=T_x`, and that

\[
 E_F(T_x,T_y)\ne\varnothing
 \quad\Longleftrightarrow\quad xy\in E(P).                     \tag{1.2}
\]

Let `R_0,R_1` be disjoint connected subgraphs outside `F`, adjacent to one
another and each adjacent to every `T_x`.  In the order-eight application
they are `G[{v,p}]` and `G[{w}]`.

For an edge `e` of `T_x`, write `A_e,D_e` for the two components of
`T_x-e`.  A neighbour label `y in N_P(x)` occurs on the `A_e` side when
`E_F(A_e,T_y)` is nonempty, and analogously for `D_e`; a label may occur on
both sides.  The neighbour labels use their cyclic order around `x` in the
fixed embedding of `P`.

Call `e` **four-label alternating** if there are four distinct neighbours
`a,b,c,d`, in this cyclic order around `x`, such that `a,c` occur on one
side and `b,d` occur on the other side, after possibly interchanging the
two sides.

## 2. A four-label alternating tree edge is terminal

### Theorem 2.1 (alternating split gives an explicit `K_7` model)

If some edge of some `T_x` is four-label alternating, then the graph
induced by

\[
                         R_0\cup R_1\cup F
\]

contains a `K_7` minor.

### Proof

Split the quotient vertex `x` into adjacent vertices `x_A,x_D`, assigning
an old neighbour to a clone whenever the corresponding literal column has
a contact with that side of `T_x-e`.  Every old neighbour is assigned at
least once, by (1.2).  The four displayed labels give an alternating
quadruple in the rotation at `x`.

The audited pentagonal-bipyramid vertex-split theorem therefore gives a
`K_5` model in the split quotient.  We use the explicit models in its
proof, which have the additional property that every one of their five
branch sets contains an old nonsplit vertex of `P`.

Lift a quotient branch set by replacing every old vertex `y` by the whole
tree `T_y`, and replacing `x_A,x_D` by `A_e,D_e`, respectively.  Quotient
connectivity and adjacency lift through the literal edges which defined
the split incidences.  The five lifted sets are disjoint, connected and
pairwise adjacent.  Each contains a whole tree `T_y` for some `y ne x`, so
it is adjacent to both `R_0` and `R_1`.  Those two roots are connected and
adjacent to one another.  They and the five lifted sets are seven branch
sets of a `K_7` model.  \(\square\)

The use of a whole nonsplit tree in every branch set is important.  Merely
lifting an arbitrary unrooted `K_5` model would not ensure adjacency to
both fixed roots.

## 3. Coupled portal orders

For every quotient edge `xy`, put

\[
                         M_{xy}=E_F(T_x,T_y).                    \tag{3.1}
\]

Temporarily cut every edge of `M_{xy}` at its midpoint.  At the `x` end,
represent each resulting half-edge by a new pendant **incidence leaf**
attached to its actual endpoint in `T_x`.  Adding all these leaves to
`T_x` gives another tree `T_x^+`.

A **coupled bundle order** chooses a linear order on every `M_{xy}`.  In
the cyclic rotation at `x`, replace the occurrence of neighbour `y` by the
chosen order of the incidence leaves of `M_{xy}`.  At `y`, use the reverse
order in the block belonging to `x`.  Concatenating these blocks in the
fixed rotation of `P` gives a cyclic order `Omega_x` on the incidence
leaves of `T_x^+`.

The coupled order is **interval-compatible** if, for every original tree
edge `e in E(T_x)`, the incidence leaves in either component of
`T_x^+-e` form a cyclic interval of `Omega_x`.

We use the following elementary plane-tree fact.

### Lemma 3.1 (prescribed leaf order for a tree)

Let `T` be a tree with a specified set of pendant leaves and a cyclic order
`Omega` on those leaves.  There is a plane embedding of `T` in a disc with
the specified leaves on the boundary in order `Omega` if and only if, for
every edge of `T`, the specified leaves in either component after deleting
that edge form a cyclic interval of `Omega`.

### Proof

In a plane embedding, the part of the tree on either side of an edge is
entered and left consecutively during the boundary walk, so its boundary
leaves form an interval.

Conversely, at a vertex `z`, the specified-leaf sets in the components of
`T-z` are disjoint cyclic intervals which partition the specified leaves
(components without a specified leaf may be inserted arbitrarily).  Give
the edges at `z` the cyclic order of these intervals.  These rotations at
all vertices define a plane embedding of the tree.  Its outer-face walk
visits the specified leaves in `Omega`, because crossing any edge enters
exactly the interval assigned to the component beyond that edge.  Put the
leaves on the boundary of a disc and isotope the remaining tree into its
interior.  \(\square\)

### Theorem 3.2 (compatible portal orders give a planar core)

If an interval-compatible coupled bundle order exists, then `F` is planar.
In the order-eight root setup

\[
 R_0=G[\{v,p\}],\qquad R_1=G[\{w\}],\qquad
 vp,pw\in E(G),\quad vw\notin E(G),                         \tag{3.2}
\]

and if these three roots and `F` span `G`, then `G` is six-colourable.

### Proof

Use Lemma 3.1 to embed each `T_x^+` in a small closed disc replacing `x`
in the fixed plane embedding of `P`, with its incidence leaves in order
`Omega_x`.  For a quotient edge `xy`, the two incidence blocks appear in
opposite orders at the ends of a narrow rectangular corridor around the
old edge.  Hence the members of `M_{xy}` can be drawn as pairwise disjoint
arcs across that corridor.  Different corridors and vertex discs are
disjoint.  Removing the artificial incidence leaves gives a plane
embedding of every tree edge and every inter-tree edge of `F`.

For the last assertion, four-colour `F`, give the nonadjacent vertices
`v,w` one new common colour, and give `p` a sixth colour.  Every edge from a
root to `F` is proper because the root colours are new, and (3.2) handles
the three edges among the roots.  \(\square\)

## 4. The single-contact family closes completely

### Corollary 4.1 (one contact per quotient edge)

Assume

\[
                         |E_F(T_x,T_y)|=1
                         \quad(xy\in E(P)).                    \tag{4.1}
\]

Then at least one of the following conclusions holds, and the portal-order
test in the proof selects exactly one of the two construction cases.

1. The two roots and the tree expansion contain an explicit `K_7`-minor
   model.
2. The core `F` is planar; in the spanning root setup (3.2), `G` is
   six-colourable.

In particular, no hypothetical minor-minimal counterexample to `HC_7` has
such a spanning tree expansion.

### Proof

There is no ordering choice inside a bundle.  Fix `x` and an edge `e` of
`T_x`.  Because every neighbour label occurs exactly once among the
incidence leaves, the two sides of `e` partition the cyclically ordered set
`N_P(x)`.  If one side is not a cyclic interval, two members of it and two
members of its complement alternate.  Their labels are distinct, so
Theorem 2.1 gives outcome 1.

Otherwise every tree-edge split is an interval.  Pendant incidence-leaf
edges have singleton sides and are intervals automatically.  Thus the
unique coupled bundle order is interval-compatible and Theorem 3.2 gives
outcome 2.  The conclusions themselves need not be logically exclusive if
the ambient graph has an unrelated `K_7` model.  \(\square\)

This closes an unbounded family: the seven trees may have arbitrary order
and shape.

## 5. Exact residual with repeated contacts

Theorems 2.1 and 3.2 give the promised structural dichotomy at their exact
scope:

- a portal-order crossing supported on four distinct old neighbour labels
  gives an explicit `K_7` model; and
- one globally compatible family of portal orders gives a plane core and a
  six-colouring.

If repeated edges are allowed in the bundles `M_{xy}`, these need not be
exhaustive.  Failure of the interval condition gives four alternating
**incidences**, but two incidences may have the same old neighbour label.
The pentagonal-bipyramid split theorem then does not apply.  Equivalently,
after all four-label crossings have been excluded, every obstruction to
every coupled bundle order is concentrated on at most three old neighbour
labels.  This is a genuine repeated-label bundle-order obstruction, not a
new finite list of pentagonal-bipyramid labellings.

The actual maximal columns in the order-eight spanning-core theorem may
also contain cycles and additional internal edges.  A spanning tree of
such a column preserves connectivity and portal locations but discarding
the other internal edges is legitimate only for constructing a minor, not
for deducing planarity of the original core.  Therefore neither arbitrary
connected columns nor the repeated-label obstruction are claimed closed
here.

## Dependencies

- the audited pentagonal-bipyramid vertex-split classifier; and
- the Four Colour Theorem.
