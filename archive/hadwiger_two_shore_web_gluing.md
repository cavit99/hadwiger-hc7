# Two-shore web gluing and the six-edge boundary table

## 1. A general boundary theorem

Let `G` be a graph, let `S=C dotcup Z`, and suppose `G-S` has exactly two
connected components `D_1,D_2` satisfying

\[
 N(D_1)=N(D_2)=S.                                   \tag{1.1}
\]

Assume that, in the cyclic order

\[
 C=(c_0,c_1,\ldots,c_{m-1}),\qquad m\ge4,
\]

every edge of `G[C]` is a frame edge
`c_ic_{i+1}` (indices modulo `m`).  Some frame edges may be absent; in
other words, `G[C]` is a subgraph of the displayed cycle.  The exact-cycle
case is the principal special case.

For each `j`, form `A_j` from `G[D_j]` by adding independent terminals
`t_0,...,t_{m-1}`, where

\[
 N_{A_j}(t_i)=N_{D_j}(c_i),                         \tag{1.2}
\]

and give the terminals the displayed cyclic order.

### Theorem 1.1 (two-shore web-gluing dichotomy)

If

\[
 \kappa(G)\ge |Z|+4,                                \tag{1.3}
\]

then one of the following holds:

1. the terminal tuple is crossed in at least one of `A_1,A_2`;
2. `G-Z` is planar.

Consequently

\[
 \text{either a shore tuple is crossed, or }
 \chi(G)\le4+\chi(G[Z]).                            \tag{1.4}
\]

#### Proof

Suppose both tuples are crossless.  Add edges on the fixed vertex set of
`A_j` until its tuple is maximally crossless.  By the generalized Two
Paths Theorem (Humeau--Pous, Theorem 1.5), the resulting edge-supergraph
`W_j` is an `m`-web whose frame is the ordered terminal cycle.  Let `R_j`
be its planar rib.

Suppose that a nonempty clique `X subseteq D_j` is inserted in a facial
triangle `F` of `R_j`.  Every `A_j`-neighbour of `X` outside `X` is one
of the three vertices of `F`.  Map a terminal `t_i in F` to `c_i` and
fix every shore vertex in `F`; call the resulting set `widehat F`.
Equation (1.2) shows that `widehat F` accounts for every neighbour of
`X` in `D_j union C`.  The two shores are anticomplete, and every other
vertex of the boundary belongs to `Z`.  Therefore

\[
 N_G(X)\subseteq\widehat F\cup Z,
 \qquad |N_G(X)|\le3+|Z|<\kappa(G).                 \tag{1.5}
\]

The set in (1.5) separates `X` from the nonempty opposite shore, a
contradiction.  Hence every actual shore vertex is a rib vertex.  Since
`A_j` is an edge-subgraph of `W_j`, replacing its terminals by the
corresponding vertices of `C` gives a disk embedding of

\[
 G[D_j\cup C]
\]

with the vertices of `C` on the boundary in the displayed cyclic order.
Every actual edge of `G[C]` is a frame edge and can be drawn along that
boundary; absent frame edges are merely auxiliary curves and need not
belong to the graph.  Embed the two disks on opposite sides of the common
cyclic boundary.  There are no edges between the shores, so they glue to
a plane embedding of `G-Z`.  This proves the dichotomy.

Four-colour `G-Z` and colour `G[Z]` with a disjoint palette of
`chi(G[Z])` colours.  All cross-edges then have differently coloured
ends, proving (1.4). \(\square\)

### Corollary 1.2 (finite crossing quotient test)

Let `J=G[S]`.  For indices occurring cyclically as `i,r,j,s`, consider
the crossing whose two paths join `c_i` to `c_j` and `c_r` to `c_s`.
Define `Gamma(J;i,r,j,s)` as follows.  Start with `J`, add a vertex `h`
complete to `S`, add adjacent vertices `x,y`, make `x` adjacent to
`c_i,c_j`, and make `y` adjacent to `c_r,c_s`.  If

\[
 \eta(\Gamma(J;i,r,j,s))\ge t                       \tag{1.6}
\]

for every crossing of `C`, then

\[
 G\text{ contains a }K_t\text{ minor}
 \quad\text{or}\quad
 \chi(G)\le4+\chi(G[Z]).                            \tag{1.7}
\]

Indeed, delete the artificial ends of an actual crossing.  The two
remaining paths are disjoint connected sets.  Since the shore is
connected, a shortest connector between them can be split at an edge,
enlarging them to adjacent disjoint connected sets `X,Y`.  Contract
`X,Y` to `x,y` and the opposite full shore to `h`.  This exhibits
`Gamma` as a minor of `G`, so (1.6) lifts.  Theorem 1.1 handles the
crossless alternative. \(\square\)

For `HC_7`, the useful numerical cell is

\[
 |S|=7,\quad |Z|\le3,\quad \chi(G[Z])\le2,
 \quad\kappa(G)\ge7.                                \tag{1.8}
\]

Under (1.8), every frame passing the finite test (1.6) closes its entire
two-full-shore boundary type, independently of the shore orders.

## 2. Exact six-missing-edge quotient classification

Let `F=overline{J}` have six edges on the seven boundary vertices.  Add
two nonadjacent helpers, each complete to the boundary; these represent
the two contracted full shores.  An exact enumeration gives twelve
unlabelled types for which this nine-vertex quotient has no `K_7` minor.
They are listed below.  The displayed labels are the representatives
used by the verifier.

| type | missing-edge graph `F` | labelled orbit | split? | forcing frame from Corollary 1.2 | status |
|---:|---|---:|:---:|---|---|
| 1 | `K4 + 3K1` | 35 | yes | none | excluded already by exact-block nonsplitness |
| 2 | `(K4-e)` with a leaf on a degree-two vertex, plus `2K1` | 1260 | yes | none | excluded already |
| 3 | net graph (a triangle with three leaves), plus `K1` | 840 | yes | none | excluded already |
| 4 | house graph plus `2K1` | 1260 | no | none | residual |
| 5 | a triangle with a pendant two-edge path, plus `K2` | 1260 | no | `(1,3,2,4)`, `Z=(0,5,6)` | **closed** |
| 6 | a `C4` with leaves at adjacent vertices, plus `K1` | 2520 | no | none | residual |
| 7 | the one-subdivision of `K_{1,3}` | 840 | no | none | residual |
| 8 | a `C5` with one leaf, plus `K1` | 2520 | no | none | residual |
| 9 | `2K3 + K1` | 70 | no | none | residual |
| 10 | `K3 + P4` | 420 | no | `(0,3,1,5)`, `Z=(2,4,6)` | **closed** |
| 11 | `C5 + K2` | 252 | no | `(0,3,2,1,4)`, `Z=(5,6)` | **closed** |
| 12 | `C6 + K1` | 420 | no | none | residual |

The orbit sizes sum to `11697`, the exact number of labelled quotient
exceptions.  Types 1--3 are split and hence cannot be the missing-edge
graph of a counterexample-derived full-shore adhesion.  Among the nine
nonsplit quotient exceptions, the web-gluing theorem closes types 5, 10,
and 11, leaving exactly types 4, 6, 7, 8, 9, and 12 on this six-edge
quotient track.

The exhaustive script `contact_order7_sixedge_web_probe.py` performs two
independent finite tasks:

1. it enumerates all `C(21,6)=54264` labelled missing-edge graphs and all
   750 possible seven-bag partitions of a nine-vertex quotient, then
   groups the 11,697 failures under all boundary relabellings;
2. for every induced cycle with a bipartite omitted set, it tests every
   crossing quotient in (1.6) by an exact connected-branch-set search.

The hand proof of Theorem 1.1 is independent of this enumeration.  The
script is the exact audit of the applicability table.

## 3. Explicit crossing certificates for the three new closures

In the following, `X,Y` are the adjacent connected sets obtained from
the two crossing paths and `D'` is the opposite full shore.

### Type 5

Use

\[
 E(F)=\{01,02,03,12,34,56\},
 \quad C=(1,3,2,4),\quad Z=\{0,5,6\}.
\]

The unique crossing joins `1` to `2` and `3` to `4`.  The seven bags

\[
 \{1\},\ \{3\},\ \{5\},\ D',\ \{0,6\},\
 X\cup\{2\},\ Y\cup\{4\}                           \tag{3.1}
\]

form a `K_7` model.  Connectivity of `{0,6}` uses `06`; its contacts
with the first three singleton bags use `61,63,05`.  The last two bags
use their crossing contacts, and every other required adjacency is a
present boundary edge (or the edge between `X,Y`).  The graph `J[Z]` is
the path `5-0-6`, so it is two-colourable.

### Type 10

Use

\[
 E(F)=\{01,02,12,34,35,46\},
 \quad C=(0,3,1,5),\quad Z=\{2,4,6\}.
\]

The crossing joins `0` to `1` and `3` to `5`.  The bags

\[
 \{0\},\ \{3\},\ \{6\},\ D',\ \{2,4\},\
 X\cup\{1\},\ Y\cup\{5\}                           \tag{3.2}
\]

form a `K_7` model.  Here `{2,4}` is connected; it sees the first three
singletons through `40,23,26`.  The rooted crossing bags see all four
base bags through their path contacts and present boundary edges.  The
omitted graph `J[Z]` is the path `4-2-6`.

### Type 11

Use

\[
 E(F)=\{01,02,13,24,34,56\},
 \quad C=(0,3,2,1,4),\quad Z=\{5,6\}.
\]

Both `F[C]` and `J[C]` are five-cycles.  All five crossings are
equivalent under their dihedral automorphism group.  For the crossing
joining `0` to `2` and `3` to `1`, use

\[
 \{2\},\ \{3\},\ \{5\},\ D',\ \{4,6\},\
 X\cup\{0\},\ Y\cup\{1\}.                          \tag{3.3}
\]

The bag `{4,6}` is connected and sees the first three singleton bags
through `62,63,45`.  The two rooted bags see one another through the
edge between `X,Y`; all their remaining adjacencies are crossing
contacts or present boundary edges.  Finally `J[Z]` is edgeless, so one
fresh colour would already suffice for `Z`.

Equations (3.1)--(3.3) prove the positive entries in the table without
using the computer-found models; the verifier independently replays all
seven-bag adjacencies for every crossing.
