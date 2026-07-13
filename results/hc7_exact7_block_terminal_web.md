# Block-terminal Two-Paths certificate for the exact-six pair carrier

**Status:** proved and independently audited, with the carrier interpreted
as the induced host graph on its branch-set vertex set.  The theorem turns
the three-portal two-rail residue into one set-terminal web certificate,
rather than one web for every portal--attachment pair.  No edge of a web
completion is treated as an edge of the original graph.

## 1. Set-terminal linkage

Let `J` be a graph, let `x,y` be distinct vertices, and let `Q,P` be
nonempty disjoint subsets of

\[
                  V(J)-\{x,y\}.                         \tag{1.1}
\]

A **set-terminal cross** is a pair of vertex-disjoint paths, one joining
`x` to `y` and the other joining some member of `Q` to some member of `P`.

Form `J^+` from `J` by adjoining two new vertices `alpha,beta`, with

\[
 N_{J^+}(\alpha)=Q,\qquad N_{J^+}(\beta)=P,             \tag{1.2}
\]

and no other new edges.  Thus `alpha,beta` are bookkeeping terminals, not
vertices or branch sets in the host graph.

## 2. One web for two terminal blocks

### Theorem 2.1 (block-terminal web certificate)

Exactly one of the following alternatives holds.

1. `J` has a set-terminal cross.
2. `J^+` has a same-vertex completion to a web with frame

   \[
                         (x,\alpha,y,\beta).             \tag{2.1}
   \]

Here a same-vertex completion adds edges but no vertices.

#### Proof

An `alpha-beta` path in `J^+` has the form

\[
                  \alpha q\,R\,p\beta                  \tag{2.2}
\]

after trimming it at its first neighbour `q` of `alpha` and its last
neighbour `p` of `beta`, where `q in Q`, `p in P`, and `R` is a `q-p`
path in `J`.  Consequently vertex-disjoint `x-y` and `alpha-beta` paths in
`J^+` are equivalent to a set-terminal cross in `J`.

For the four-term tuple `(x,alpha,y,beta)`, such two paths are precisely a
crossing.  If they do not exist, the generalized Two Paths Theorem gives a
same-vertex web completion with that frame.  Conversely a frame of a web is
crossless. \(\square\)

The external input is Theorem 1.5 of S. Humeau and D. Pous, *On the Two
Paths Theorem and the Two Disjoint Paths Problem* (2025): a tuple is
crossless exactly when its graph has a same-vertex web completion with that
frame.  Only its four-terminal case is needed here.  The point of (1.2) is
that one application handles all pairs in `Q\mathbin{\times}P`; no compatibility of
separately chosen web completions is required.

## 3. Application to the three-bypass carrier

Use the exact-six pair-carrier setting of
`hc7_exact7_pair_carrier_bypass.md`.  From the outset let `K`
mean the induced host graph on the carrier's branch-set vertex set.  Adding
literal host edges inside a branch set changes neither its trace nor any
cross-block adjacency.  If one of those edges creates a labelled peel,
that is already the desired host-graph outcome; otherwise the locked
capture argument applies to this induced carrier.  Assume direct promotion
and labelled peeling both fail.  Let

\[
 Q=\{q_1,q_2,q_3\},\qquad P^\circ=P-\{x,y\}.           \tag{3.1}
\]

The audited hypotheses give `|P|>=5`, hence `|P^circ|>=3`; the sets in
(3.1) are disjoint.  For every `q in Q`, every nonseparating `x-y` path in
`K-q` contains all of `P`.

We also record the exact linkage implication used below.  In a
three-connected graph, vertex-disjoint `x-y` and `q-p` paths yield a
nonseparating `x-y` path avoiding `q,p`.  To see this, extend the two paths
to a partition `V(K)=C\mathbin{\dot\cup}D` with `K[C],K[D]` connected:
contract the paths, take a spanning tree, and delete one edge on the tree
path between the two contracted vertices.  The relative form of Tutte's
path lemma, applied to the connected induced graph `K[C]` and its connected
complement `K[D]`, gives an `x-y` path in `C` whose deletion leaves `K`
connected.  This is the connected-pair linkage equivalence used in the
proof.

### Theorem 3.1 (one literal rural certificate or a full three-gate)

The augmented graph

\[
 K^+=K+\alpha Q+\beta P^\circ                         \tag{3.2}
\]

has a same-vertex web completion with frame
`(x,alpha,y,beta)`.  Fix any such completion and write it as a plane rib
with clique cells behind facial rib triangles.

1. Every member of `Q\cup P^circ` is a rib vertex.
2. If a clique cell contains a vertex of `K`, its facial triangle contains
   neither `alpha` nor `beta`.
3. If `C` is a component of the vertices of `K` in a nonempty clique cell
   behind the rib triangle `Delta`, then

   \[
                    N_K(C)=V(\Delta).                 \tag{3.3}
   \]

   In particular `V(Delta)` is a literal three-vertex separator of `K`
   and `C` is full to it.
4. If no clique cell contains a vertex of `K`, then `K` is a subgraph of
   the plane rib.  In particular `K` is planar.

#### Proof

For `q in Q` and `p in P^circ`, a pair of disjoint `x-y` and `q-p` paths
would, by the connected-pair linkage equivalence proved above,
give a nonseparating `x-y` path avoiding `q,p`.  That path avoids `q` but
omits the marked vertex `p`, contrary to the universal capture property.
Thus `K` has no set-terminal cross, and Theorem 2.1 gives the displayed web
completion.

The frame vertices `x,alpha,y,beta` belong to the rib.  In a web, every
vertex outside the rib belongs to one clique cell, and all its neighbours
outside that cell lie in the cell's facial triangle.

Suppose `z in Q` is in a clique cell behind `Delta`.  The actual edge
`alpha z` of `K^+` forces `alpha in V(Delta)`.  Let `C` be the component of
the actual graph induced by the `K`-vertices of that cell which contains
`z`.  In the induced carrier,

\[
                       N_K(C)\subseteq V(\Delta)-\{\alpha\}, \tag{3.4}
\]

which has order at most two.  There is a carrier vertex on the far side.
If at least one of `x,y` is outside `Delta`, use that frame root.  Otherwise
`Delta={alpha,x,y}`.  Then `beta` is not in `Delta`, so no
`p in P^circ` can lie in this cell: the literal edge `beta p` would force
`beta` into its facial triangle.  Any such `p` is therefore outside
`C\cup N_K(C)`.  In both cases (3.4) separates two nonempty carrier
sides, contradicting the three-connectivity of `K`.  Interchanging
`(alpha,Q)` with `(beta,P^circ)` proves that no member of `P^circ` lies in
a clique cell.  This proves item 1.

More generally, if a cell behind `Delta` contains an actual carrier vertex
and `Delta` contains `alpha` or `beta`, any component `C` of the actual
carrier vertices in that cell again satisfies a containment of the form
(3.4).  The frame and the two nonempty terminal blocks leave a nonempty far
side, contradicting three-connectivity.  This proves item 2.

Now let `C` lie in a nonempty cell.  Item 2 gives
`V(Delta)\subseteq V(K)`, and the web incidence rule gives

\[
                         N_K(C)\subseteq V(\Delta).     \tag{3.5}
\]

There is a vertex of `K` outside `C\cup V(Delta)`: all six vertices in
`Q\cup P^circ` are rib vertices, whereas a triangle contains only three
vertices.  Hence `N_K(C)` separates a nonempty `C` from a nonempty far
side.  Three-connectivity and (3.5) force equality, proving item 3.

If every cell is empty of actual carrier vertices, all vertices and edges
of `K` lie in the plane rib, proving item 4. \(\square\)

### Corollary 3.2 (four-connected carrier page)

If `K` is four-connected, then it is planar.  In its unique plane embedding
there is one face whose boundary contains

\[
                         \{x,y\}\cup Q\cup P^\circ,    \tag{3.6}
\]

with `Q` on one open `x-y` boundary arc and `P^circ` on the other.

#### Proof

Item 3 of Theorem 3.1 excludes nonempty clique cells, so `K` is planar.
Alternatively, apply the standard four-connected form of the Two Paths
Theorem to each tuple `(x,q,y,p)`.  Fixing one `q_0,p_0` fixes a face in
the unique embedding.  Varying `q` while retaining `x,y,p_0`, and then
varying `p` while retaining `x,y,q_0`, cannot change the face: two distinct
facial cycles of a three-connected plane graph cannot share three distinct
vertices.  Alternation puts the two terminal sets on opposite open
`x-y` arcs. \(\square\)

## 4. Ambient seven-connectivity pressure

The web cells are not harmless unlabelled debris.  They expose literal
places at which ambient connectivity must leave the carrier.

### Corollary 4.1 (four external contacts at every nonempty cell)

In the exact HC7 host, let `C` be as in Theorem 3.1(3).  Then

\[
                   |N_G(C)-V(K)|\ge4.                 \tag{4.1}
\]

Moreover `C` has no edge to the locked region `L` and contains none of the
three selected foreign portals.

#### Proof

Equation (3.3) says that exactly three neighbours of `C` lie in `K`.
The set `C` consists of open-shore vertices, so `v` is on a nonempty far
side.  Seven-connectivity gives `|N_G(C)|>=7`, proving (4.1).

Every carrier vertex adjacent to `L` belongs to
`P=N(L)\cap K`; all its nonroot members lie on the rib by Theorem 3.1(1),
and the only possible root members are `x,y`, also on the rib.  Hence no
cell component sees `L`.  The selected portals `Q` are rib vertices by the
same theorem. \(\square\)

## 5. Evacuating every nonplanar web cell

The cell alternative in Theorem 3.1 disappears after the natural
rank-first carrier optimization.  This is a geometric exchange, not a use
of completion edges.

This section retains the complete Section 3 setting: `L\subseteq W` is
fixed and connected, `P^circ\subseteq N_G(L)\cap V(K)` has order at least
three and lies on the rib, and the exact trace of `K` supplies its literal
old adjacencies to both target blocks.  These hypotheses are part of every
realization compared below.

### Lemma 5.1 (literal cell evacuation)

Retain a supported realization `K,A,B,W`, where `K,A,B` are the three
pairwise adjacent core blocks with fixed adhesion traces and `W` is the
connected decorated set.  Let `D` be a component in a nonempty web cell of
Theorem 3.1, behind the literal gate `Delta`.  Then there is another
supported realization with the same traces, with no smaller admissible or
raw contact rank of `W`, and with carrier strictly smaller than `K`.

#### Proof

By Theorem 3.1,

\[
                         N_K(D)=V(\Delta),             \tag{5.1}
\]

and `D` contains neither trace root.  The graph `K-D` is connected.  To
see this, note that `D` is a component of `K-V(Delta)` and there is another
such component containing rib vertices outside the three-vertex gate.
Three-connectivity makes every component of `K-V(Delta)` full to
`V(Delta)`.  One far-side component therefore connects all three gate
vertices, and every remaining component attaches to them.

There are four cases.

1. If `D` sees neither `W` nor `A\cup B`, discard `D` from the model.
2. If `D` sees `W` but not `A\cup B`, replace
   `W` by `W\cup D` and `K` by `K-D`.
3. If `D` sees a target block `A_0\in\{A,B\}` but not `W`, replace
   `A_0` by `A_0\cup D` and `K` by `K-D`.
4. If `D` sees both `W` and a target `A_0`, replace `W` by `W\cup D`
   and `K` by `K-D`.

Every displayed union is connected by the corresponding literal contact.
The retained carrier is connected by the preceding paragraph.  It keeps
its whole trace and hence its old literal adjacencies to both target
blocks.  In cases 2 and 4, the new `W` remains adjacent to the retained
carrier through the actual `D-Delta` edges.  In cases 1 and 3, `W` remains
adjacent to `K-D` because all members of `P^circ` are rib vertices and
therefore lie outside `D`.

No moved cell contains an adhesion vertex, so every trace is unchanged.
Old `W` contacts are retained.  Case 4 may add the target `A_0` as a new
raw, and when permitted by the fixed trace also admissible, contact; it
never removes a contact.  Thus both contact ranks are nondecreasing, while
the carrier loses the nonempty set `D`. \(\square\)

### Theorem 5.2 (lex-optimal pair carrier is low-connected or rural)

Fix the connected locked region `L\subseteq W` and restrict to supported
realizations with the fixed frame traces and
`|N(L)\cap K|>=5`.  Among them, first maximize the admissible contact rank
of `W`, then its raw contact rank, and subject to those choices minimize
`|K|`.  If the selected pair-trace
carrier `K` is three-connected and the three-bypass locked outcome holds,
then `K` is planar.  More precisely it lies in the planar-rib outcome of
Theorem 3.1; every member of `Q` and every nonroot member of `P` has the
single block-terminal web certificate from Theorem 2.1.

#### Proof

Apply Theorem 3.1.  A nonempty web-cell component has no edge to `L` by
Corollary 4.1, so its evacuation leaves the fixed region `L` in `W` and
does not change `N(L)\cap K`.  It would therefore, by Lemma 5.1,
give a realization with lexicographically no worse contact ranks and a
strictly smaller carrier, contrary to the choice of `K`.  Hence every
actual carrier vertex lies on the plane rib, and Theorem 3.1(4) gives
planarity. \(\square\)

The competitor in Lemma 5.1 need only be a valid connected branch-set
realization; it need not remain three-connected.  This is why the
optimization is taken over all supported realizations before the theorem
branches on the connectivity of its selected carrier.  Thus the conclusion
is an exact structural dichotomy:

* a lex-optimal carrier has a cut of order at most two; or
* if it is three-connected, its entire hard residue is one planar/rural
  block-terminal page.

This removes all unbounded clique-cell and three-gate recursion from the
three-connected branch.

## 6. Exact next exchange

The per-pair web drift and the nonplanar three-gate recursion are now gone
from a three-connected lex-optimal realization.  Its survivor is a planar
pair carrier carrying the three labelled foreign portals and all nonroot
locked attachments in one block-terminal rural certificate.  Completion
edges remain unavailable.

The remaining exchange is therefore sharply bilateral: either an actual
bridge crosses this rural page and supplies the clean detour of the
pair-trace theorem, or all bridges respect the same two sides and must be
turned into the fixed two-apex/color-gluing structure.  The low-connectivity
alternative is a separate cutvertex/2-cut carrier branch, not a hidden web
cell.
