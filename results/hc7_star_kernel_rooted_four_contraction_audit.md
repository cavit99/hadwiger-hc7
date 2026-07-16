# Independent audit of the rooted-four contraction dichotomy

**Verdict:** GREEN for the exact revision audited.

## Audited revision

- theorem file: `results/hc7_star_kernel_rooted_four_contraction.md`
- SHA-256: `f039c19bd05a182e6f2167e280759709c5847ed98f5169054b3590893007a020`

This is a separate internal mathematical audit.  It checks the two-edge
contraction and lift, every separator-order calculation, the exact use of the
rooted-`K_4` theorem, the second-clique argument, both facial-boundary claims,
the simultaneous elimination of the four-connected planar outcome, and the
new refinement of the order-eight separator.
The previous audit hash is superseded by this materially strengthened
revision.

## 1. Setup and distinct nominated vertices

The promoted five-support star theorem supplies each edge `e_k` wholly in
`G-L`, anticomplete to `ell_k`, and collectively adjacent to every other
vertex of `L`.  The selected edges are vertex-disjoint.  Consequently the
two contractions do not identify either `ell_i` or `ell_j`, and their images
`z_i,z_j` are distinct from one another and from both leaves.  The four
nominated vertices are therefore legitimate distinct roots.

For Section 4, the cited Theorems 2.3 and 2.4 also supply exactly the extra
facts used: `Y` is a literal five-clique disjoint from `L`, `p` lies in `Y`,
and no normalized defect edge contains `p`.

## 2. Rooted-minor lift (Lemma 2.1)

Expanding `z_i` back to the connected edge `e_i`, and similarly for `z_j`,
preserves each of the following separately:

- branch-set connectedness, because each contracted fibre is connected;
- branch-set disjointness, because only the branch set containing `z_k`
  receives the two endpoints of `e_k`; and
- every branch-set adjacency, because every quotient edge has an original
  edge between the corresponding fibres.

Each singleton `r in R` sees the two leaf-rooted branch sets through the
clique edges `r ell_i,r ell_j`.  It sees the two edge-rooted branch sets
because `e_i` and `e_j` are each collectively adjacent to `r`.  The three
singletons in `R` form a triangle.  Hence the four lifted rooted-`K_4`
branch sets and these three singletons are seven disjoint, pairwise adjacent
connected subgraphs.  This is an explicit `K_7`-minor model.  No adjacency
is inferred from a virtual or quotient edge without lifting it.

## 3. Separator lifting and order counts (Lemma 3.1)

Let `X` be a vertex cut of `Q`.  If `z_k` belongs to `X`, deleting both
endpoints of `e_k` deletes its complete contraction fibre; if it does not,
the fibre remains connected.  Thus every component of `Q-X` has a nonempty
inverse image in `J-X^uparrow`, and an edge between inverse images of two
different components would project to an edge between those components.
Therefore `X^uparrow` really separates `J`.

The set `R` is disjoint from `X^uparrow`.  Deleting `R union X^uparrow`
from `G` leaves exactly `J-X^uparrow`, so it separates `G`.  Replacing each
of the `r_X` contracted vertices by a two-vertex edge increases the order by
`r_X`; adding the three vertices of `R` gives

\[
 |R union X^uparrow|=|X|+r_X+3.
\]

Seven-connectivity then gives the asserted exhaustive small-cut arithmetic:

- orders zero and one are impossible;
- an order-two cut must contain both `z_i,z_j` and lifts to order seven;
- an order-three cut must contain at least one contracted vertex;
- with exactly one it lifts to order seven; and
- with both it lifts only to order eight by this construction.

In every lifted case at least two inverse-image components remain, so the
two open sides are nonempty.  The uses of “actual separation” are valid.

If `Q` is not four-connected, it has a cut of order at most three unless it
is the four-vertex complete graph.  The latter already is a rooted `K_4` on
the four nominated vertices and is excluded by Lemma 2.1 in the
`K_7`-minor-free branch.  Thus Corollary 3.2 omits no small-order exception.

## 4. External rooted-`K_4` theorem (Corollary 3.2)

The invocation is exact.  Theorem 6 of R. Fabila-Monroy and D. R. Wood,
*Rooted K4-Minors*, Electronic Journal of Combinatorics 20(2) (2013), P64,
states that for four distinct nominated vertices in a four-connected graph,
either there is a `K_4` minor rooted at them, or the graph is planar and the
four vertices lie on a common face.  This is precisely the dichotomy used
for `Q`; no stronger rooted linkage or prescribed cyclic order is assumed.

## 5. Image of the second five-clique (Lemma 4.1)

A contraction whose edge contains at most one vertex of `Y` is injective on
the five vertices of `Y`.  One contraction internal to `Y` leaves four
distinct clique images.  Hence, if at most one of the two contractions is
internal to `Y`, the image of `Y` contains a literal `K_4`.

A four-connected planar graph cannot properly contain a literal `K_4`.
In the inherited embedding, each component outside the clique lies in one
of the four triangular regions of the embedded `K_4`; its attachments are
contained in that region's boundary triangle.  Removing that triangle
separates the component from the opposite clique vertex, contradicting
four-connectivity.  Thus such a graph would have to equal `K_4`, in which
case its four distinct nominated vertices themselves give the forbidden
rooted minor.  Therefore each of `e_i,e_j` is internal to `Y`.

Because the two edges are disjoint and neither contains `p`, their four
endpoints are exactly `Y-{p}`.  The perfect-matching conclusion following
Lemma 4.1 is consequently valid.

## 6. Facial four-cycle and triangle (Lemma 4.2)

The six adjacencies/nonadjacencies among the nominated vertices are all
literal after contraction:

- `z_i z_j` comes from the clique `Y`;
- `ell_i ell_j` comes from the clique `L`;
- `z_i ell_j` and `z_j ell_i` come from collective defect-edge adjacency;
  and
- `z_i ell_i` and `z_j ell_j` are absent by defect-edge anticompleteness.

Thus the nominated vertices induce exactly the displayed chordless
four-cycle.

In a three-connected plane graph every facial boundary is a simple induced
cycle.  Since all four roots lie on one facial boundary and every edge of
their induced four-cycle is present, each such edge must be a boundary edge,
not a chord.  At each root its two neighbours on the facial boundary are
therefore its two neighbours in the four-cycle, leaving no interval in which
an additional boundary vertex can occur.  The common facial boundary is
exactly that four-cycle.

The vertices `z_i,z_j,p` form a literal triangle because `Y` is a clique and
`p` is not contracted.  Every triangle in a four-connected plane graph is
facial: a triangle with vertices on both sides is a three-vertex separator,
while if all other vertices lie on one side, the empty side is a face.
This triangle and the four-cycle are distinct facial cycles sharing the
edge `z_i z_j`; they are therefore exactly the two faces incident with that
edge.

## 7. Simultaneous use of all five defect edges (Lemma 5.1)

Assume every quotient belonging to a vertex-disjoint pair of normalized
defect edges is four-connected.  In the `K_7`-minor-free setup, Corollary 3.2
then puts each such quotient in its planar outcome, so Lemma 4.1 is applicable
to every disjoint pair; four-connectivity alone is not being used as a
substitute for that conclusion.

Choose one disjoint pair `e_i,e_j`.  Lemma 4.1 puts both edges in `Y`, and
the exclusion of `p` from every defect edge puts their four endpoints in
`W=Y-{p}`.  For another edge `e_k` there are exactly two possibilities:

- it meets both disjoint edges, in which case its two endpoints are one
  endpoint of each and hence both lie in `W`; or
- it fails to meet one of them, in which case it forms a vertex-disjoint
  pair with that edge and another application of Lemma 4.1 puts `e_k` in
  `Y`, hence in `W` because `p` is not its endpoint.

Thus all five distinct defect edges are edges of the literal four-clique
`W`.  Since `K_4` has six edges, they leave one actual clique edge `f`
unselected.

### The unselected edge is adjacent to every leaf

Fix `ell_k`, write `e_k=ab`, and write `W-{a,b}={c,d}`.  Among `ac,bc`, at
least one is selected because only `f` is unselected.  It is some `e_h`
with `h!=k`.  This selected edge is collectively adjacent to `ell_k`, while
both `a,b` are nonadjacent to `ell_k`; therefore `c` is adjacent to
`ell_k`.  Applying the same argument to `ad,bd` proves that `d` is adjacent
to `ell_k`.  Since `f` is not `ab`, it has at least one endpoint in
`{c,d}`.  Hence `f` is collectively adjacent to `ell_k`.  The argument is
uniform in `k`, so `f` is collectively adjacent to all five vertices of
`L`.

### The component containing `p` is adjacent to the whole boundary

The set `S=L union V(f)` has exactly seven vertices: `f` lies in `W`, which
is disjoint from `L`, and its endpoints are distinct.  Also `p` is outside
`S`, so the component `D` of `G-S` containing `p` is nonempty.

Because `D` is a component of `G-S`, all its neighbours lie in `S`.  If a
vertex `s in S` had no neighbour in `D`, then
`N_G(D) subseteq S-{s}` would have order at most six.  Deleting `N_G(D)`
would leave both the nonempty component `D` and the vertex `s`, with no path
between them, contradicting seven-connectivity.  Therefore `D` has a
neighbour at every literal vertex of `S`.  In particular it is adjacent to
both endpoints of `f` and to every leaf in `L`.

The connected subgraphs `D` and `f` are disjoint, adjacent to one another,
and each is adjacent to all five singleton branch sets in the clique `L`.
They and those five singletons are consequently an explicit `K_7`-minor
model.  This contradiction proves Lemma 5.1 without assuming a common
planar embedding for different quotients.

## 8. Final separator output (Theorem 5.2)

Lemma 5.1 supplies a disjoint pair whose quotient is not four-connected.
The quotient has four distinct nominated vertices.  If it has exactly four
vertices and is complete, those vertices already root a `K_4`, contrary to
Lemma 2.1; every other non-four-connected possibility has a cut of order at
most three.  Lemma 3.1 excludes cuts of order at most one and classifies the
remaining cuts exactly by how many of `z_i,z_j` they contain.  This yields
the two stated actual order-seven separations and the stated actual
order-eight separation.  The order-eight open sides are nonempty for the
same inverse-component reason used in Lemma 3.1; “actual” is justified
there too.

## 9. Refinement of the order-eight separator (Lemma 6.1)

For a three-cut `{z_i,z_j,x}` containing both contracted vertices, its full
inverse image together with `R` is exactly the eight-set

\[
 S=R union V(e_i) union V(e_j) union \{x\}.
\]

The edges `e_i,e_j` are disjoint and lie outside `L`, while `x` is a
quotient vertex different from `z_i,z_j`; hence all eight displayed
vertices are distinct.  Because both contraction fibres are deleted, the
components of `G-S` correspond exactly to the components of
`Q-{z_i,z_j,x}`.  In particular there are at least two, and every such
component has all its neighbours in `S`.

For each component `D`, another component remains outside it, so
seven-connectivity applies to its external neighbourhood and gives
`|N_G(D)|>=7`.  If this order is seven, deleting `N_G(D)` leaves `D` and at
least one other inverse-image component on opposite open sides; it is an
actual order-seven separation.  If no component has neighbourhood order
seven, every component has neighbourhood exactly the entire eight-set `S`.

In this full-boundary outcome the two defect edges must be anticomplete.  If
they had a cross-edge, choose distinct complementary components `C,D`.  The
seven sets `C union {x}`, `D`, `e_i`, `e_j`, and the three singleton
vertices of `R` are connected and disjoint.  Fullness supplies all
component-to-boundary adjacencies, including adjacency of `D` to
`C union {x}` through `x`; the assumed cross-edge joins the edge branch
sets; each defect edge is collectively adjacent to all three vertices of
`R`; and `R` is a clique.  They are therefore an explicit `K_7`-minor
model.  The anticompleteness conclusion is valid.

There are exactly two complementary components.  If `C_1,C_2,C_3` were
distinct components and `e_j=a_jb_j`, the seven sets
`C_1 union {a_j}`, `C_2 union {b_j}`, `C_3 union {x}`, `e_i`, and the
three singletons in `R` would be connected and disjoint.  The first two are
adjacent through `a_jb_j`; fullness of `C_3` joins the third to both through
`a_j,b_j`; fullness joins all three to `e_i` and every singleton in `R`;
and the defect-edge/R and R/R adjacencies are already available.  These are
seven pairwise adjacent branch sets, contradicting `K_7`-minor-freeness.
At least two components come from the quotient cut, so exactly two remain.

In the latter case choose any two components.  They are nonempty, connected,
and anticomplete, and every vertex of `S` has a neighbour in each.  These are
exactly the hypotheses of the independently audited Theorem 1 in
`results/hc7_two_full_shore_boundary_absorption.md`.  Since the host is
`K_7`-minor-free and `|S|=8`, that theorem gives that `G[S]` is
four-colourable.  The invocation uses the theorem's order-eight conclusion
only; it does not infer that either boundary colouring extends across a
shore.

## Scope

The draft eliminates the four-connected planar outcome simultaneously over
the five normalized defect edges.  It also refines the order-eight lift to
an actual order-seven separation unless there are exactly two complementary
components, each adjacent to the full eight-vertex boundary; in that residue
the boundary is four-colourable and the two distinguished defect edges are
anticomplete.  It
correctly leaves open state-preserving colouring
composition across that full order-eight boundary, and assigns no unproved
rank or orientation to the order-seven outputs.
